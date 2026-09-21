"""Rigorous finite-dimensional interval plumbing for the C005 Schur frontier.

The purpose of this module is to certify matrix/spectral inequalities on an
*a-interval* once interval enclosures for the localized matrix entries are
available.

No floating-point matrix assembled here is promoted to an operator theorem.
The certification rule is deliberately elementary:

    lambda_min(A) >= lambda_min(A0) - ||A-A0||_2

and for an entrywise absolute radius matrix R,

    ||A-A0||_2 <= sqrt(||R||_1 ||R||_inf).

For Hermitian/symmetric R this reduces to max row sum.  The same bound is used
for coupling operator norms.

This module is therefore the bridge from future interval enclosures of
A_LL(a), B(a), A_HH(a) to a certified scalar Schur gap.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Sequence

import numpy as np


@dataclass(frozen=True)
class MatrixIntervalCertificate:
    midpoint_min_eigenvalue: float
    perturbation_norm_upper: float
    certified_min_eigenvalue: float

    @property
    def positive(self) -> bool:
        return self.certified_min_eigenvalue > 0.0


@dataclass(frozen=True)
class CouplingIntervalCertificate:
    midpoint_norm: float
    perturbation_norm_upper: float
    certified_norm_upper: float


@dataclass(frozen=True)
class SchurIntervalCertificate:
    mu_lower: float
    epsilon_upper: float
    nu_lower: float
    effective_floor_lower: float
    scalar_block_gap_lower: float

    @property
    def strict(self) -> bool:
        return (
            self.mu_lower > 0.0
            and self.nu_lower > 0.0
            and self.effective_floor_lower > 0.0
            and self.scalar_block_gap_lower > 0.0
        )


@dataclass(frozen=True)
class ContinuationCell:
    center: float
    halfwidth: float
    center_gap_lower: float
    lipschitz_upper: float
    certified_gap_lower: float

    @property
    def strict(self) -> bool:
        return self.certified_gap_lower > 0.0

    @property
    def interval(self) -> tuple[float, float]:
        return (self.center - self.halfwidth, self.center + self.halfwidth)


def _as_square_complex(matrix: np.ndarray | Sequence[Sequence[complex]]) -> np.ndarray:
    a = np.asarray(matrix, dtype=complex)
    if a.ndim != 2 or a.shape[0] != a.shape[1] or a.shape[0] == 0:
        raise ValueError("matrix must be a non-empty square array")
    return a


def _as_radius(radius: np.ndarray | Sequence[Sequence[float]], shape: tuple[int, int]) -> np.ndarray:
    r = np.asarray(radius, dtype=float)
    if r.shape != shape:
        raise ValueError("radius matrix shape mismatch")
    if not np.all(np.isfinite(r)) or np.any(r < 0.0):
        raise ValueError("radius matrix must be finite and entrywise non-negative")
    return r


def absolute_radius_operator_norm_upper(radius: np.ndarray | Sequence[Sequence[float]]) -> float:
    """Bound spectral norm from an entrywise absolute radius matrix."""
    r = np.asarray(radius, dtype=float)
    if r.ndim != 2 or r.size == 0:
        raise ValueError("radius matrix must be non-empty")
    if not np.all(np.isfinite(r)) or np.any(r < 0.0):
        raise ValueError("radius matrix must be finite and non-negative")
    norm_inf = float(np.max(np.sum(r, axis=1)))
    norm_one = float(np.max(np.sum(r, axis=0)))
    return math.sqrt(norm_inf * norm_one)


def hermitian_interval_min_eigenvalue(
    midpoint: np.ndarray | Sequence[Sequence[complex]],
    radius: np.ndarray | Sequence[Sequence[float]],
    *,
    hermitian_tolerance: float = 1e-12,
) -> MatrixIntervalCertificate:
    """Certify a lower eigenvalue over an entrywise Hermitian interval family."""
    a0 = _as_square_complex(midpoint)
    r = _as_radius(radius, a0.shape)
    if not np.allclose(a0, a0.conjugate().T, atol=hermitian_tolerance, rtol=0.0):
        raise ValueError("midpoint must be Hermitian")
    midpoint_min = float(np.min(np.linalg.eigvalsh(a0)))
    perturb = absolute_radius_operator_norm_upper(r)
    return MatrixIntervalCertificate(
        midpoint_min_eigenvalue=midpoint_min,
        perturbation_norm_upper=perturb,
        certified_min_eigenvalue=midpoint_min - perturb,
    )


def rectangular_interval_norm_upper(
    midpoint: np.ndarray | Sequence[Sequence[complex]],
    radius: np.ndarray | Sequence[Sequence[float]],
) -> CouplingIntervalCertificate:
    """Certify ||B|| from a rectangular midpoint plus entrywise radii."""
    b0 = np.asarray(midpoint, dtype=complex)
    if b0.ndim != 2 or b0.size == 0:
        raise ValueError("midpoint must be a non-empty matrix")
    r = _as_radius(radius, b0.shape)
    midpoint_norm = float(np.linalg.norm(b0, ord=2))
    perturb = absolute_radius_operator_norm_upper(r)
    return CouplingIntervalCertificate(
        midpoint_norm=midpoint_norm,
        perturbation_norm_upper=perturb,
        certified_norm_upper=midpoint_norm + perturb,
    )


def scalar_block_gap_lower(mu_lower: float, epsilon_upper: float, nu_lower: float) -> float:
    """Worst-case lower eigenvalue of the scalar 2x2 block envelope."""
    if not all(math.isfinite(x) for x in (mu_lower, epsilon_upper, nu_lower)):
        raise ValueError("bounds must be finite")
    if epsilon_upper < 0.0:
        raise ValueError("epsilon_upper must be non-negative")
    return 0.5 * (
        mu_lower
        + nu_lower
        - math.hypot(mu_lower - nu_lower, 2.0 * epsilon_upper)
    )


def schur_interval_certificate(
    mu_lower: float,
    epsilon_upper: float,
    nu_lower: float,
) -> SchurIntervalCertificate:
    """Propagate interval block bounds into a strict effective Schur gap."""
    if nu_lower <= 0.0:
        raise ValueError("nu_lower must be strictly positive")
    if epsilon_upper < 0.0:
        raise ValueError("epsilon_upper must be non-negative")
    if not all(math.isfinite(x) for x in (mu_lower, epsilon_upper, nu_lower)):
        raise ValueError("bounds must be finite")

    effective = mu_lower - epsilon_upper * epsilon_upper / nu_lower
    block_gap = scalar_block_gap_lower(mu_lower, epsilon_upper, nu_lower)
    return SchurIntervalCertificate(
        mu_lower=mu_lower,
        epsilon_upper=epsilon_upper,
        nu_lower=nu_lower,
        effective_floor_lower=effective,
        scalar_block_gap_lower=block_gap,
    )


def interval_schur_from_matrix_enclosures(
    low_midpoint: np.ndarray | Sequence[Sequence[complex]],
    low_radius: np.ndarray | Sequence[Sequence[float]],
    coupling_midpoint: np.ndarray | Sequence[Sequence[complex]],
    coupling_radius: np.ndarray | Sequence[Sequence[float]],
    high_midpoint: np.ndarray | Sequence[Sequence[complex]],
    high_radius: np.ndarray | Sequence[Sequence[float]],
) -> tuple[MatrixIntervalCertificate, CouplingIntervalCertificate, MatrixIntervalCertificate, SchurIntervalCertificate]:
    """End-to-end finite block interval certificate."""
    low = hermitian_interval_min_eigenvalue(low_midpoint, low_radius)
    coupling = rectangular_interval_norm_upper(coupling_midpoint, coupling_radius)
    high = hermitian_interval_min_eigenvalue(high_midpoint, high_radius)
    schur = schur_interval_certificate(
        low.certified_min_eigenvalue,
        coupling.certified_norm_upper,
        high.certified_min_eigenvalue,
    )
    return low, coupling, high, schur


def continuation_cell(
    center: float,
    halfwidth: float,
    center_gap_lower: float,
    lipschitz_upper: float,
) -> ContinuationCell:
    """Certify a scalar gap over [center-halfwidth,center+halfwidth].

    If g(center) >= g0 and |g(a)-g(center)| <= L |a-center|, then
        g(a) >= g0 - L*halfwidth.
    """
    if not all(math.isfinite(x) for x in (center, halfwidth, center_gap_lower, lipschitz_upper)):
        raise ValueError("continuation parameters must be finite")
    if halfwidth < 0.0 or lipschitz_upper < 0.0:
        raise ValueError("halfwidth and lipschitz_upper must be non-negative")
    lower = center_gap_lower - lipschitz_upper * halfwidth
    return ContinuationCell(
        center=center,
        halfwidth=halfwidth,
        center_gap_lower=center_gap_lower,
        lipschitz_upper=lipschitz_upper,
        certified_gap_lower=lower,
    )


def cover_is_strict(cells: Sequence[ContinuationCell], start: float, stop: float, *, tol: float = 1e-12) -> bool:
    """Check that strict cells form a gap-free cover of [start,stop]."""
    if not math.isfinite(start) or not math.isfinite(stop) or not start < stop:
        raise ValueError("invalid target interval")
    ordered = sorted(cells, key=lambda cell: cell.interval[0])
    if not ordered or any(not cell.strict for cell in ordered):
        return False
    left = ordered[0].interval[0]
    right = ordered[0].interval[1]
    if left > start + tol:
        return False
    for cell in ordered[1:]:
        a, b = cell.interval
        if a > right + tol:
            return False
        right = max(right, b)
    return right >= stop - tol


def interval_gate_map() -> dict[str, object]:
    return {
        "schema": "SOH_C005_INTERVAL_SCHUR_CONTINUATION_V0_1",
        "closed": [
            "entrywise-radius to spectral-norm perturbation bound",
            "Hermitian eigenvalue lower bound by Weyl perturbation",
            "rectangular coupling norm upper bound",
            "scalar Schur effective-floor propagation",
            "Lipschitz continuation cell and gap-free cover logic",
        ],
        "open": [
            "rigorous interval enclosures for localized operator matrix entries as functions of a",
            "rigorous Lipschitz/derivative bounds for the effective Schur gap",
            "repository-to-Suzuki localized operator/domain/Friedrichs join",
            "all-scale interval cover",
            "completion null-mode exclusion",
            "SOH-C005",
            "Riemann Hypothesis",
        ],
        "proof_of_rh": False,
    }
