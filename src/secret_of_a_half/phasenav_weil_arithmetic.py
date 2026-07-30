"""Prime-side auditor for the native PhaseNav--Weil arithmetic operator.

The authoritative execution profile is
``construction/phasenav/secret_of_half_weil_arithmetic.pnv``.

The matrix entries are evaluated through the Guinand--Weil explicit formula
using pole terms, the archimedean gamma factor, and a truncated prime-power
sum.  The arithmetic evaluation does not consume a zero list.  A separate
low-height spectral matrix is used only as a regression cross-check.

Mathematical status
-------------------
The Gaussian Fourier transform and the formal explicit-formula decomposition
are exact.  Prime cutoffs and numerical integration are numerical.  A single
positive-semidefinite sample is not a proof of the Riemann Hypothesis and does
not promote SOH-C005.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
import math
from pathlib import Path
import re

import mpmath as mp

from .phasenav_weil_probe import Hermitian2

_EQUATION_RE = re.compile(r"^Μ\(([^)]+)\)\s*=\s*(.+)$")


@dataclass(frozen=True)
class ArithmeticWeilProgram:
    """Parsed execution profile for the prime-side PhaseNav--Weil audit."""

    path: Path
    equations: dict[str, str]

    @classmethod
    def load(cls, path: str | Path) -> "ArithmeticWeilProgram":
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
            "CHANNEL_COUNT",
            "TARGET_ORDINATE",
            "GAUSSIAN_WIDTH",
            "PRIME_CUTOFF",
            "AUDIT_PRIME_CUTOFF",
            "INTEGRATION_RADIUS",
            "MP_DPS",
            "STABILITY_TOLERANCE",
            "SPECTRAL_MATCH_TOLERANCE",
            "PSD_TOLERANCE",
            "FOURIER_NORMALIZATION",
            "INVOLUTION",
            "OPERATOR",
            "SPECTRAL_ZERO_INPUT",
            "STATUS",
        }
        missing = sorted(required.difference(self.equations))
        if missing:
            raise ValueError(f"missing PhaseNav equations: {', '.join(missing)}")
        if self.channel_count != 2:
            raise ValueError("the arithmetic v0.2 profile requires two channels")
        if self.target_ordinate <= 0.0 or self.gaussian_width <= 0.0:
            raise ValueError("target ordinate and Gaussian width must be positive")
        if self.prime_cutoff < 2 or self.audit_prime_cutoff <= self.prime_cutoff:
            raise ValueError("audit cutoff must be larger than the primary prime cutoff")
        if self.integration_radius <= 0.0 or self.mp_dps < 30:
            raise ValueError("integration radius and precision are too small")
        if min(
            self.stability_tolerance,
            self.spectral_match_tolerance,
            self.psd_tolerance,
        ) <= 0.0:
            raise ValueError("all tolerances must be positive")
        if self.equations["SPECTRAL_ZERO_INPUT"] != "NONE_FOR_ARITHMETIC_SUM":
            raise ValueError("arithmetic profile must not consume a zero list")

    @property
    def channel_count(self) -> int:
        return int(float(self.equations["CHANNEL_COUNT"]))

    @property
    def target_ordinate(self) -> float:
        return float(self.equations["TARGET_ORDINATE"])

    @property
    def gaussian_width(self) -> float:
        return float(self.equations["GAUSSIAN_WIDTH"])

    @property
    def prime_cutoff(self) -> int:
        return int(float(self.equations["PRIME_CUTOFF"]))

    @property
    def audit_prime_cutoff(self) -> int:
        return int(float(self.equations["AUDIT_PRIME_CUTOFF"]))

    @property
    def integration_radius(self) -> float:
        return float(self.equations["INTEGRATION_RADIUS"])

    @property
    def mp_dps(self) -> int:
        return int(float(self.equations["MP_DPS"]))

    @property
    def stability_tolerance(self) -> float:
        return float(self.equations["STABILITY_TOLERANCE"])

    @property
    def spectral_match_tolerance(self) -> float:
        return float(self.equations["SPECTRAL_MATCH_TOLERANCE"])

    @property
    def psd_tolerance(self) -> float:
        return float(self.equations["PSD_TOLERANCE"])

    @property
    def half_separation(self) -> float:
        return math.pi / self.target_ordinate

    @property
    def channel_centres(self) -> tuple[float, float]:
        return -self.half_separation, +self.half_separation


def default_arithmetic_program_path() -> Path:
    return (
        Path(__file__).resolve().parents[2]
        / "construction"
        / "phasenav"
        / "secret_of_half_weil_arithmetic.pnv"
    )


@dataclass(frozen=True)
class ExplicitFormulaComponents:
    """Four additive components of one Guinand--Weil matrix entry."""

    pole: complex
    conductor: complex
    archimedean: complex
    prime: complex

    @property
    def total(self) -> complex:
        return self.pole + self.conductor + self.archimedean + self.prime


def spectral_test_value(
    r: complex | mp.mpc,
    left_centre: float,
    right_centre: float,
    program: ArithmeticWeilProgram,
) -> mp.mpc:
    """Return H_ij(r) = psi_i#(r) psi_j(r) for the Gaussian channels."""
    width = mp.mpf(str(program.gaussian_width))
    target = mp.mpf(str(program.target_ordinate))
    difference = mp.mpf(str(right_centre - left_centre))
    shifted = mp.mpc(r) - target
    return mp.exp(-width * width * shifted * shifted + 1j * difference * shifted)


def spectral_test_fourier(
    x: float | mp.mpf,
    left_centre: float,
    right_centre: float,
    program: ArithmeticWeilProgram,
) -> mp.mpc:
    """Closed Fourier transform with exp(-2*pi*i*x*r) normalization."""
    width = mp.mpf(str(program.gaussian_width))
    target = mp.mpf(str(program.target_ordinate))
    difference = mp.mpf(str(right_centre - left_centre))
    x_mp = mp.mpf(x)
    return (
        mp.sqrt(mp.pi)
        / width
        * mp.exp(-2j * mp.pi * x_mp * target)
        * mp.exp(-((difference - 2 * mp.pi * x_mp) ** 2) / (4 * width * width))
    )


@lru_cache(maxsize=8)
def prime_power_terms(cutoff: int) -> tuple[tuple[int, float], ...]:
    """Return (p^k, log p) terms up to cutoff, i.e. von Mangoldt support."""
    if cutoff < 2:
        return ()
    sieve = bytearray(b"\x01") * (cutoff + 1)
    sieve[0:2] = b"\x00\x00"
    for prime in range(2, int(math.isqrt(cutoff)) + 1):
        if sieve[prime]:
            start = prime * prime
            sieve[start : cutoff + 1 : prime] = b"\x00" * (
                ((cutoff - start) // prime) + 1
            )

    result: list[tuple[int, float]] = []
    for prime in range(2, cutoff + 1):
        if not sieve[prime]:
            continue
        log_prime = math.log(prime)
        power = prime
        while power <= cutoff:
            result.append((power, log_prime))
            if power > cutoff // prime:
                break
            power *= prime
    result.sort(key=lambda item: item[0])
    return tuple(result)


def explicit_formula_entry(
    left_centre: float,
    right_centre: float,
    program: ArithmeticWeilProgram,
    *,
    prime_cutoff: int,
) -> ExplicitFormulaComponents:
    """Evaluate one matrix entry from the prime side of the explicit formula."""
    mp.mp.dps = program.mp_dps
    two_pi = 2 * mp.pi

    pole = spectral_test_value(1 / (2j), left_centre, right_centre, program)
    pole += spectral_test_value(-1 / (2j), left_centre, right_centre, program)

    conductor = -(
        mp.log(mp.pi)
        / two_pi
        * spectral_test_fourier(0, left_centre, right_centre, program)
    )

    target = mp.mpf(str(program.target_ordinate))
    radius = mp.mpf(str(program.integration_radius))

    def archimedean_integrand(r: mp.mpf) -> mp.mpc:
        gamma_log_derivative = mp.re(mp.digamma(mp.mpf("0.25") + 0.5j * r))
        return spectral_test_value(r, left_centre, right_centre, program) * gamma_log_derivative

    archimedean = mp.quad(
        archimedean_integrand,
        [target - radius, target, target + radius],
    ) / two_pi

    prime_sum = mp.mpc(0)
    for n, mangoldt in prime_power_terms(prime_cutoff):
        x = mp.log(n) / two_pi
        transforms = spectral_test_fourier(x, left_centre, right_centre, program)
        transforms += spectral_test_fourier(-x, left_centre, right_centre, program)
        prime_sum += mp.mpf(str(mangoldt)) / mp.sqrt(n) * transforms
    prime = -prime_sum / two_pi

    return ExplicitFormulaComponents(
        pole=complex(pole),
        conductor=complex(conductor),
        archimedean=complex(archimedean),
        prime=complex(prime),
    )


def arithmetic_weil_matrix(
    program: ArithmeticWeilProgram,
    *,
    prime_cutoff: int,
) -> tuple[Hermitian2, dict[str, ExplicitFormulaComponents]]:
    """Build the two-channel Hermitian matrix from arithmetic data only."""
    minus, plus = program.channel_centres
    diagonal = explicit_formula_entry(minus, minus, program, prime_cutoff=prime_cutoff)
    off_diagonal = explicit_formula_entry(minus, plus, program, prime_cutoff=prime_cutoff)

    matrix = Hermitian2(
        a=diagonal.total.real,
        b=off_diagonal.total,
        d=diagonal.total.real,
    )
    return matrix, {"diagonal": diagonal, "off_diagonal": off_diagonal}


def matrix_entry_distance(left: Hermitian2, right: Hermitian2) -> float:
    """Maximum independent-entry distance between two Hermitian matrices."""
    return max(abs(left.a - right.a), abs(left.b - right.b), abs(left.d - right.d))


def _complex_json(value: complex) -> dict[str, float]:
    return {"real": float(value.real), "imag": float(value.imag)}


def _components_json(components: ExplicitFormulaComponents) -> dict[str, object]:
    return {
        "pole": _complex_json(components.pole),
        "conductor": _complex_json(components.conductor),
        "archimedean": _complex_json(components.archimedean),
        "prime": _complex_json(components.prime),
        "total": _complex_json(components.total),
    }


def run_arithmetic_audit(
    program: ArithmeticWeilProgram,
    *,
    spectral_reference: Hermitian2 | None = None,
) -> dict[str, object]:
    """Run cutoff stability, PSD sample, and optional spectral cross-check."""
    primary, _ = arithmetic_weil_matrix(program, prime_cutoff=program.prime_cutoff)
    audited, components = arithmetic_weil_matrix(
        program,
        prime_cutoff=program.audit_prime_cutoff,
    )

    stability_error = matrix_entry_distance(primary, audited)
    eigenvalues = audited.eigenvalues()
    receipt: dict[str, object] = {
        "program": program.equations["PROGRAM"],
        "version": program.equations["VERSION"],
        "status": program.equations["STATUS"],
        "arithmetic_sum_uses_zero_list": False,
        "target_ordinate_is_declared_probe_centre": True,
        "prime_cutoff": program.prime_cutoff,
        "audit_prime_cutoff": program.audit_prime_cutoff,
        "matrix": {
            "a": audited.a,
            "b": _complex_json(audited.b),
            "d": audited.d,
        },
        "eigenvalues": {
            "lambda_min": eigenvalues[0],
            "lambda_max": eigenvalues[1],
        },
        "cutoff_stability": {
            "max_entry_error": stability_error,
            "pass": stability_error <= program.stability_tolerance,
        },
        "psd_sample": {
            "pass": eigenvalues[0] >= -program.psd_tolerance,
        },
        "components": {
            name: _components_json(value) for name, value in components.items()
        },
    }

    if spectral_reference is not None:
        match_error = matrix_entry_distance(audited, spectral_reference)
        receipt["spectral_cross_check"] = {
            "max_entry_error": match_error,
            "pass": match_error <= program.spectral_match_tolerance,
            "reference_role": "validation_only_not_arithmetic_input",
        }

    return receipt
