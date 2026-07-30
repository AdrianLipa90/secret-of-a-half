"""Basis-adaptive cutoff schedule for the PhaseNav--Weil Hermite tail."""
from __future__ import annotations

from dataclasses import dataclass
import math
from pathlib import Path
import re

import mpmath as mp

from .phasenav_weil_hermite_core import channel_normalization, hermite_linearization_terms
from .phasenav_weil_prime_tail_integrals import tail_term_integral_gamma

_EQUATION_RE = re.compile(r"^Μ\(([^)]+)\)\s*=\s*(.+)$")


@dataclass(frozen=True)
class AdaptiveCutoffProgram:
    path: Path
    equations: dict[str, str]

    @classmethod
    def load(cls, path: str | Path) -> "AdaptiveCutoffProgram":
        source = Path(path)
        equations: dict[str, str] = {}
        for raw in source.read_text(encoding="utf-8").splitlines():
            line = raw.strip()
            if not line or line.startswith("#") or line.startswith("───"):
                continue
            match = _EQUATION_RE.match(line)
            if match:
                equations[match.group(1).strip()] = match.group(2).strip()
        item = cls(source, equations)
        item.validate()
        return item

    def validate(self) -> None:
        required = {
            "PROGRAM", "VERSION", "BASE_HEAD", "MAX_BASIS_SIZE",
            "GAUSSIAN_WIDTH", "BASE_CUTOFF", "LOG_CUTOFF_SLOPE",
            "OPERATOR_NORM_TARGET", "MP_DPS", "SCHEDULE",
            "SPECTRAL_ZERO_INPUT", "STATUS",
        }
        missing = sorted(required.difference(self.equations))
        if missing:
            raise ValueError(f"missing PhaseNav equations: {', '.join(missing)}")
        if self.max_basis_size < 2 or self.gaussian_width <= 0:
            raise ValueError("invalid basis size or Gaussian width")
        if self.base_cutoff < 3 or self.log_cutoff_slope <= 0:
            raise ValueError("invalid cutoff schedule")
        if self.operator_norm_target <= 0 or self.mp_dps < 40:
            raise ValueError("invalid precision or target")
        if self.equations["SPECTRAL_ZERO_INPUT"] != "NONE":
            raise ValueError("adaptive cutoff audit must not consume zeros")
        if "MAX(LOG_BASE_CUTOFF" not in self.equations["SCHEDULE"]:
            raise ValueError("unexpected adaptive schedule")

    def _int(self, key: str) -> int:
        return int(float(self.equations[key]))

    def _float(self, key: str) -> float:
        return float(self.equations[key])

    @property
    def max_basis_size(self) -> int:
        return self._int("MAX_BASIS_SIZE")

    @property
    def gaussian_width(self) -> float:
        return self._float("GAUSSIAN_WIDTH")

    @property
    def base_cutoff(self) -> int:
        return self._int("BASE_CUTOFF")

    @property
    def log_cutoff_slope(self) -> float:
        return self._float("LOG_CUTOFF_SLOPE")

    @property
    def operator_norm_target(self) -> float:
        return self._float("OPERATOR_NORM_TARGET")

    @property
    def mp_dps(self) -> int:
        return self._int("MP_DPS")


def default_adaptive_cutoff_program_path() -> Path:
    return Path(__file__).resolve().parents[2] / "construction/phasenav/secret_of_half_weil_adaptive_cutoff_schedule.pnv"


def adaptive_log_cutoff(basis_size: int, *, base_cutoff: int, slope: float) -> float:
    if basis_size < 1 or base_cutoff < 3 or slope <= 0:
        raise ValueError("invalid adaptive schedule parameters")
    return max(math.log(base_cutoff), slope * basis_size)


def adaptive_cutoff(basis_size: int, *, base_cutoff: int, slope: float) -> int:
    log_base = math.log(base_cutoff)
    growth = slope * basis_size
    if growth <= log_base:
        return base_cutoff
    return int(math.ceil(math.exp(growth)))


def logarithmic_decay_rate(degree: int, log_cutoff: float, width: float) -> float:
    if degree < 0 or log_cutoff <= 0 or width <= 0:
        raise ValueError("invalid decay-rate parameters")
    return log_cutoff / (2 * width * width) - 0.5 - (degree + 1) / log_cutoff


def elementary_tail_integral_envelope(degree: int, log_cutoff: float, width: float) -> mp.mpf:
    rate = logarithmic_decay_rate(degree, log_cutoff, width)
    if rate <= 0:
        raise ValueError("cutoff is below the positive decay-rate threshold")
    u = mp.mpf(str(log_cutoff))
    w = mp.mpf(str(width))
    density = u ** (degree + 1) * mp.exp(-(u * u) / (4 * w * w) + u / 2) / (w ** degree)
    return density / mp.mpf(str(rate))


def crude_log_operator_envelope(basis_size: int, log_cutoff: float, width: float) -> float:
    if basis_size < 1:
        raise ValueError("basis_size must be positive")
    degree = 2 * basis_size - 2
    rate = logarithmic_decay_rate(degree, log_cutoff, width)
    if rate <= 0:
        raise ValueError("cutoff is below the coarse monotonicity threshold")
    return (
        2 * math.log(basis_size)
        + (3 * basis_size - 3) * math.log(2)
        + math.lgamma(basis_size)
        - math.log(math.pi)
        + (degree + 1) * math.log(log_cutoff)
        - degree * math.log(width)
        - log_cutoff * log_cutoff / (4 * width * width)
        + log_cutoff / 2
        - math.log(rate)
    )


def scheduled_operator_norm_bound(
    basis_size: int, *, base_cutoff: int, slope: float, width: float, mp_dps: int
) -> tuple[int, float]:
    mp.mp.dps = mp_dps
    log_cutoff = adaptive_log_cutoff(basis_size, base_cutoff=base_cutoff, slope=slope)
    cutoff = adaptive_cutoff(basis_size, base_cutoff=base_cutoff, slope=slope)
    integrals = [tail_term_integral_gamma(d, cutoff, width) for d in range(2 * basis_size - 1)]
    norms = [mp.mpf(str(channel_normalization(n, width))) for n in range(basis_size)]
    rows: list[mp.mpf] = []
    for left in range(basis_size):
        row = mp.mpf("0")
        for right in range(basis_size):
            polynomial = mp.mpf("0")
            for degree, coefficient in hermite_linearization_terms(left, right):
                polynomial += coefficient * integrals[degree]
            prefactor = norms[left] * norms[right] * mp.sqrt(mp.pi) / mp.mpf(str(width)) / mp.pi
            row += prefactor * polynomial
        rows.append(row)
    return cutoff, float(max(rows))


def run_adaptive_cutoff_audit(program: AdaptiveCutoffProgram) -> dict[str, object]:
    sections: list[dict[str, object]] = []
    maximum = 0.0
    maximum_basis = 0
    for basis_size in range(1, program.max_basis_size + 1):
        log_cutoff = adaptive_log_cutoff(
            basis_size, base_cutoff=program.base_cutoff, slope=program.log_cutoff_slope
        )
        cutoff, bound = scheduled_operator_norm_bound(
            basis_size,
            base_cutoff=program.base_cutoff,
            slope=program.log_cutoff_slope,
            width=program.gaussian_width,
            mp_dps=program.mp_dps,
        )
        if bound > maximum:
            maximum, maximum_basis = bound, basis_size
        sections.append({
            "basis_size": basis_size,
            "log_cutoff": log_cutoff,
            "cutoff": cutoff,
            "operator_norm_bound": bound,
            "target_pass": bound <= program.operator_norm_target,
            "coarse_log_envelope": crude_log_operator_envelope(
                basis_size, log_cutoff, program.gaussian_width
            ),
            "decay_rate": logarithmic_decay_rate(
                2 * basis_size - 2, log_cutoff, program.gaussian_width
            ),
        })
    tail = sections[-8:]
    return {
        "program": program.equations["PROGRAM"],
        "version": program.equations["VERSION"],
        "base_head": program.equations["BASE_HEAD"],
        "status": program.equations["STATUS"],
        "spectral_zero_input": False,
        "schedule": "log_Q_N=max(log_Q0,c*N)",
        "base_cutoff": program.base_cutoff,
        "log_cutoff_slope": program.log_cutoff_slope,
        "gaussian_width": program.gaussian_width,
        "max_basis_size": program.max_basis_size,
        "operator_norm_target": program.operator_norm_target,
        "sections": sections,
        "all_target_pass": all(item["target_pass"] for item in sections),
        "maximum_certified_bound": maximum,
        "maximum_bound_basis_size": maximum_basis,
        "coarse_envelope_decreasing_on_final_window": all(
            tail[i + 1]["coarse_log_envelope"] < tail[i]["coarse_log_envelope"]
            for i in range(len(tail) - 1)
        ),
        "claim_boundary": {
            "exact": [
                "adaptive logarithmic cutoff definition",
                "elementary h(U)/alpha(U) tail envelope",
                "coarse Hermite coefficient and finite-section norm envelope",
                "for every c>0, Q_N=exp(c*N) forces the coarse envelope to zero",
            ],
            "numerical": f"exact v0.5 tail certificate evaluated for N<={program.max_basis_size}",
            "open": [
                "fixed-cutoff uniformity in basis size",
                "global arithmetic positivity",
                "null-structure implication to native closure",
            ],
            "proof_of_rh": False,
        },
    }
