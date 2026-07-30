"""Prime-side Hermite-ladder auditor for the native PhaseNav--Weil programme.

The authoritative profile is
``construction/phasenav/secret_of_half_weil_hermite_ladder.pnv``.

Exact layer
-----------
* translated-scaled Hermite functions form an explicit Schwartz dense core;
* the product kernel has a closed Fourier transform;
* positivity of every finite principal matrix gives positivity on the finite
  Hermite span, and continuity would extend it to the dense core.

Numerical layer
---------------
Only finitely many principal matrices and finite prime cutoffs are evaluated.
No result in this module proves the Riemann Hypothesis or promotes SOH-C005.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
import math
from pathlib import Path
import re
from typing import Iterable

import mpmath as mp
import numpy as np
from numpy.polynomial.hermite import hermgauss

_EQUATION_RE = re.compile(r"^Μ\(([^)]+)\)\s*=\s*(.+)$")


@dataclass(frozen=True)
class HermiteLadderProgram:
    """Parsed execution profile for the Hermite dense-core audit."""

    path: Path
    equations: dict[str, str]

    @classmethod
    def load(cls, path: str | Path) -> "HermiteLadderProgram":
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
            "TARGET_ORDINATE",
            "GAUSSIAN_WIDTH",
            "PRIME_CUTOFF",
            "AUDIT_PRIME_CUTOFF",
            "HERMITE_QUADRATURE_ORDER",
            "MP_DPS",
            "STABILITY_TOLERANCE",
            "PSD_TOLERANCE",
            "FOURIER_TOLERANCE",
            "SYNTHETIC_OFF_AXIS_DELTA",
            "SYNTHETIC_NEGATIVITY_THRESHOLD",
            "FOURIER_NORMALIZATION",
            "INVOLUTION",
            "BASIS",
            "OPERATOR",
            "SPECTRAL_ZERO_INPUT",
            "STATUS",
        }
        missing = sorted(required.difference(self.equations))
        if missing:
            raise ValueError(f"missing PhaseNav equations: {', '.join(missing)}")
        if self.max_basis_size < 2:
            raise ValueError("MAX_BASIS_SIZE must be at least 2")
        if self.target_ordinate <= 0.0 or self.gaussian_width <= 0.0:
            raise ValueError("target ordinate and Gaussian width must be positive")
        if self.prime_cutoff < 2 or self.audit_prime_cutoff <= self.prime_cutoff:
            raise ValueError("audit cutoff must be larger than primary cutoff")
        if self.quadrature_order < 32 or self.mp_dps < 30:
            raise ValueError("quadrature order or precision is too small")
        if min(self.stability_tolerance, self.psd_tolerance, self.fourier_tolerance) <= 0:
            raise ValueError("all tolerances must be positive")
        if self.equations["SPECTRAL_ZERO_INPUT"] != "NONE_FOR_ARITHMETIC_SUM":
            raise ValueError("arithmetic audit must not consume a zero list")

    def _int(self, key: str) -> int:
        return int(float(self.equations[key]))

    def _float(self, key: str) -> float:
        return float(self.equations[key])

    @property
    def max_basis_size(self) -> int:
        return self._int("MAX_BASIS_SIZE")

    @property
    def target_ordinate(self) -> float:
        return self._float("TARGET_ORDINATE")

    @property
    def gaussian_width(self) -> float:
        return self._float("GAUSSIAN_WIDTH")

    @property
    def prime_cutoff(self) -> int:
        return self._int("PRIME_CUTOFF")

    @property
    def audit_prime_cutoff(self) -> int:
        return self._int("AUDIT_PRIME_CUTOFF")

    @property
    def quadrature_order(self) -> int:
        return self._int("HERMITE_QUADRATURE_ORDER")

    @property
    def mp_dps(self) -> int:
        return self._int("MP_DPS")

    @property
    def stability_tolerance(self) -> float:
        return self._float("STABILITY_TOLERANCE")

    @property
    def psd_tolerance(self) -> float:
        return self._float("PSD_TOLERANCE")

    @property
    def fourier_tolerance(self) -> float:
        return self._float("FOURIER_TOLERANCE")

    @property
    def synthetic_off_axis_delta(self) -> float:
        return self._float("SYNTHETIC_OFF_AXIS_DELTA")

    @property
    def synthetic_negativity_threshold(self) -> float:
        return self._float("SYNTHETIC_NEGATIVITY_THRESHOLD")


def default_program_path() -> Path:
    return (
        Path(__file__).resolve().parents[2]
        / "construction"
        / "phasenav"
        / "secret_of_half_weil_hermite_ladder.pnv"
    )


def physicists_hermite(order: int, value: complex | float) -> complex:
    """Evaluate the physicists' Hermite polynomial H_order by recurrence."""
    if order < 0:
        raise ValueError("Hermite order must be non-negative")
    if order == 0:
        return 1.0 + 0.0j
    z = complex(value)
    if order == 1:
        return 2.0 * z
    previous = 1.0 + 0.0j
    current = 2.0 * z
    for n in range(1, order):
        previous, current = current, 2.0 * z * current - 2.0 * n * previous
    return current


def hermite_values(max_order: int, values: np.ndarray) -> np.ndarray:
    """Return H_0,...,H_max_order evaluated on a real numpy array."""
    result = np.empty((max_order + 1, values.size), dtype=float)
    result[0] = 1.0
    if max_order == 0:
        return result
    result[1] = 2.0 * values
    for n in range(1, max_order):
        result[n + 1] = 2.0 * values * result[n] - 2.0 * n * result[n - 1]
    return result


def channel_normalization(order: int, width: float) -> float:
    """L2 normalization for the translated-scaled Hermite channel."""
    return math.sqrt(width / (math.sqrt(math.pi) * (2**order) * math.factorial(order)))


def channel_value(
    order: int,
    r: complex | float,
    program: HermiteLadderProgram,
) -> complex:
    """Evaluate the normalized Hermite channel psi_n(r)."""
    width = program.gaussian_width
    y = width * (complex(r) - program.target_ordinate)
    return (
        channel_normalization(order, width)
        * physicists_hermite(order, y)
        * np.exp(-0.5 * y * y)
    )


def kernel_value(
    left_order: int,
    right_order: int,
    r: complex | float,
    program: HermiteLadderProgram,
) -> complex:
    """Return H_mn(r)=conj(psi_m(conj(r))) psi_n(r)."""
    z = complex(r)
    return np.conjugate(channel_value(left_order, np.conjugate(z), program)) * channel_value(
        right_order, z, program
    )


def hermite_linearization_terms(left_order: int, right_order: int) -> tuple[tuple[int, int], ...]:
    """Return (resulting_order, integer coefficient) for H_m H_n."""
    terms: list[tuple[int, int]] = []
    for k in range(min(left_order, right_order) + 1):
        coefficient = (
            (2**k)
            * math.factorial(k)
            * math.comb(left_order, k)
            * math.comb(right_order, k)
        )
        terms.append((left_order + right_order - 2 * k, coefficient))
    return tuple(terms)


def kernel_fourier_closed(
    x: float | np.ndarray,
    left_order: int,
    right_order: int,
    program: HermiteLadderProgram,
) -> complex | np.ndarray:
    """Closed Fourier transform under exp(-2*pi*i*x*r)."""
    width = program.gaussian_width
    target = program.target_ordinate
    x_array = np.asarray(x, dtype=float)
    kappa = 2.0 * math.pi * x_array / width
    polynomial = np.zeros_like(kappa, dtype=complex)
    for resulting_order, coefficient in hermite_linearization_terms(left_order, right_order):
        polynomial += coefficient * (-1j * kappa) ** resulting_order
    prefactor = (
        channel_normalization(left_order, width)
        * channel_normalization(right_order, width)
        / width
        * math.sqrt(math.pi)
    )
    result = (
        prefactor
        * np.exp(-2j * math.pi * x_array * target)
        * np.exp(-(kappa**2) / 4.0)
        * polynomial
    )
    if np.ndim(x_array) == 0:
        return complex(result)
    return result


