"""Native profile parser and monotonicity threshold for the prime-tail certificate."""
from __future__ import annotations
from dataclasses import dataclass
import math
from pathlib import Path
import re

_EQUATION_RE = re.compile(r"^Μ\(([^)]+)\)\s*=\s*(.+)$")

@dataclass(frozen=True)
class PrimeTailProgram:
    """Parsed native profile for the finite-section tail certificate."""

    path: Path
    equations: dict[str, str]

    @classmethod
    def load(cls, path: str | Path) -> "PrimeTailProgram":
        source_path = Path(path)
        equations: dict[str, str] = {}
        for raw_line in source_path.read_text(encoding="utf-8").splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#") or line.startswith("───"):
                continue
            match = _EQUATION_RE.match(line)
            if match:
                equations[match.group(1).strip()] = match.group(2).strip()
        program = cls(source_path, equations)
        program.validate()
        return program

    def validate(self) -> None:
        required = {
            "PROGRAM",
            "VERSION",
            "BASE_HEAD",
            "MAX_BASIS_SIZE",
            "GAUSSIAN_WIDTH",
            "TAIL_CUTOFF",
            "MP_DPS",
            "INTEGRAL_MATCH_TOLERANCE",
            "OPERATOR_NORM_TARGET",
            "RECIPROCAL_MAP",
            "FOURIER_NORMALIZATION",
            "VON_MANGOLDT_MAJORANT",
            "SPECTRAL_ZERO_INPUT",
            "STATUS",
        }
        missing = sorted(required.difference(self.equations))
        if missing:
            raise ValueError(f"missing PhaseNav equations: {', '.join(missing)}")
        if self.max_basis_size < 1:
            raise ValueError("MAX_BASIS_SIZE must be positive")
        if self.gaussian_width <= 0.0:
            raise ValueError("GAUSSIAN_WIDTH must be positive")
        if self.tail_cutoff < 3:
            raise ValueError("TAIL_CUTOFF must be at least 3")
        if self.mp_dps < 40:
            raise ValueError("MP_DPS is too small for the declared certificate")
        if self.integral_match_tolerance <= 0.0 or self.operator_norm_target <= 0.0:
            raise ValueError("declared tolerances must be positive")
        if self.equations["SPECTRAL_ZERO_INPUT"] != "NONE":
            raise ValueError("the tail certificate must not consume a zero list")
        if "1 / LOG_X" not in self.equations["RECIPROCAL_MAP"]:
            raise ValueError("the declared tail map must be reciprocal in log x")
        if math.log(self.tail_cutoff) <= self.gaussian_width**2:
            raise ValueError("TAIL_CUTOFF is too small for the gamma expansion used")

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
    def tail_cutoff(self) -> int:
        return self._int("TAIL_CUTOFF")

    @property
    def mp_dps(self) -> int:
        return self._int("MP_DPS")

    @property
    def integral_match_tolerance(self) -> float:
        return self._float("INTEGRAL_MATCH_TOLERANCE")

    @property
    def operator_norm_target(self) -> float:
        return self._float("OPERATOR_NORM_TARGET")


def default_prime_tail_program_path() -> Path:
    return (
        Path(__file__).resolve().parents[2]
        / "construction"
        / "phasenav"
        / "secret_of_half_weil_prime_tail_certificate.pnv"
    )


def monotone_log_threshold(degree: int, width: float) -> float:
    """Return the positive log-coordinate threshold for a degree-d tail term.

    For
        g_d(x)=x^(-1/2)(log x)^(d+1) exp(-(log x)^2/(4 w^2)),
    the function is decreasing once log(x) is at least this threshold.
    """
    if degree < 0 or width <= 0.0:
        raise ValueError("degree must be non-negative and width positive")
    w2 = width * width
    return 0.5 * (math.sqrt(w2 * w2 + 8.0 * w2 * (degree + 1)) - w2)


def monotonicity_margin(degree: int, cutoff: int, width: float) -> float:
    """Positive values certify that the integral test applies."""
    if cutoff < 2:
        raise ValueError("cutoff must be at least 2")
    return math.log(cutoff) - monotone_log_threshold(degree, width)

