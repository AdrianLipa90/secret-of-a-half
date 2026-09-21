"""Finite quotient/Feshbach certificate for the localized C005 form.

Suppose H_N is the high Fourier-moment kernel and R_N is any finite-dimensional
right inverse of the low-moment map.  Every admissible psi decomposes as

    psi = ell(c) + h,   h in H_N.

If the high form is coercive,
    q(h,h) >= nu ||h||^2,
and ell(c) lies in the source operator domain so that
    q(ell,h) = <B ell,h>,
then completing the square gives

    q(ell+h)
      >= q(ell,ell) - ||P_H B ell||^2 / nu
      >= q(ell,ell) - ||B ell||^2 / nu.

Thus C005 on the whole form space follows from positivity of a finite effective
matrix

    F = Q_low - G_B / nu,

where (G_B)_ij = <B ell_i, B ell_j>.

This module only propagates supplied finite matrices and interval radii.  It
does not construct the actual localized lift ell_i or evaluate B_a.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Sequence

import numpy as np

from .c005_interval_schur import absolute_radius_operator_norm_upper


@dataclass(frozen=True)
class QuotientFeshbachCertificate:
    low_form_min_lower: float
    B_image_gram_max_upper: float
    high_coercivity_lower: float
    effective_gap_lower: float

    @property
    def strict(self) -> bool:
        return self.effective_gap_lower > 0.0


@dataclass(frozen=True)
class MatrixFeshbachCertificate:
    effective_midpoint_min_eigenvalue: float
    effective_radius_norm_upper: float
    effective_gap_lower: float

    @property
    def strict(self) -> bool:
        return self.effective_gap_lower > 0.0


def _hermitian(a: np.ndarray | Sequence[Sequence[complex]], name: str) -> np.ndarray:
    m = np.asarray(a, dtype=complex)
    if m.ndim != 2 or m.shape[0] != m.shape[1] or m.shape[0] == 0:
        raise ValueError(f"{name} must be a non-empty square matrix")
    if not np.allclose(m, m.conjugate().T, atol=1e-12, rtol=0.0):
        raise ValueError(f"{name} must be Hermitian")
    return m


def quotient_feshbach_scalar_certificate(
    low_form_min_lower: float,
    B_image_gram_max_upper: float,
    high_coercivity_lower: float,
) -> QuotientFeshbachCertificate:
    """Safe scalar lower bound lambda_min(Q)-lambda_max(G_B)/nu."""
    if not all(
        math.isfinite(x)
        for x in (
            low_form_min_lower,
            B_image_gram_max_upper,
            high_coercivity_lower,
        )
    ):
        raise ValueError("bounds must be finite")
    if B_image_gram_max_upper < 0.0:
        raise ValueError("B-image Gram upper bound must be non-negative")
    if high_coercivity_lower <= 0.0:
        raise ValueError("high coercivity must be strictly positive")
    gap = (
        low_form_min_lower
        - B_image_gram_max_upper / high_coercivity_lower
    )
    return QuotientFeshbachCertificate(
        low_form_min_lower=low_form_min_lower,
        B_image_gram_max_upper=B_image_gram_max_upper,
        high_coercivity_lower=high_coercivity_lower,
        effective_gap_lower=gap,
    )


def quotient_feshbach_from_interval_matrices(
    low_midpoint: np.ndarray | Sequence[Sequence[complex]],
    low_radius: np.ndarray | Sequence[Sequence[float]],
    Bgram_midpoint: np.ndarray | Sequence[Sequence[complex]],
    Bgram_radius: np.ndarray | Sequence[Sequence[float]],
    high_coercivity_lower: float,
) -> QuotientFeshbachCertificate:
    """Interval-safe scalar Feshbach gap from Q_low and G_B enclosures."""
    q0 = _hermitian(low_midpoint, "low_midpoint")
    g0 = _hermitian(Bgram_midpoint, "Bgram_midpoint")
    if q0.shape != g0.shape:
        raise ValueError("low and B-image Gram matrices must have same shape")

    qr = np.asarray(low_radius, dtype=float)
    gr = np.asarray(Bgram_radius, dtype=float)
    if qr.shape != q0.shape or gr.shape != g0.shape:
        raise ValueError("radius matrix shape mismatch")
    if np.any(qr < 0.0) or np.any(gr < 0.0):
        raise ValueError("radius matrices must be non-negative")

    q_min_lower = (
        float(np.min(np.linalg.eigvalsh(q0)))
        - absolute_radius_operator_norm_upper(qr)
    )
    g_max_upper = (
        float(np.max(np.linalg.eigvalsh(g0)))
        + absolute_radius_operator_norm_upper(gr)
    )
    # G_B is theoretically PSD.  A negative numerical upper bound can only be
    # caused by an inconsistent enclosure; fail closed rather than clip it.
    if g_max_upper < 0.0:
        raise ValueError("B-image Gram enclosure has negative spectral upper bound")

    return quotient_feshbach_scalar_certificate(
        q_min_lower,
        g_max_upper,
        high_coercivity_lower,
    )


def quotient_feshbach_matrix_certificate(
    low_midpoint: np.ndarray | Sequence[Sequence[complex]],
    low_radius: np.ndarray | Sequence[Sequence[float]],
    Bgram_midpoint: np.ndarray | Sequence[Sequence[complex]],
    Bgram_radius: np.ndarray | Sequence[Sequence[float]],
    high_coercivity_lower: float,
) -> MatrixFeshbachCertificate:
    """Sharper effective-matrix enclosure for F=Q-G_B/nu.

    Since only a lower bound on nu is known, this matrix-level formula is safe
    when G_B is supplied as a PSD enclosure and the subtraction uses nu_lower.
    The interval radius is propagated linearly.
    """
    if high_coercivity_lower <= 0.0 or not math.isfinite(high_coercivity_lower):
        raise ValueError("high coercivity must be finite and positive")

    q0 = _hermitian(low_midpoint, "low_midpoint")
    g0 = _hermitian(Bgram_midpoint, "Bgram_midpoint")
    if q0.shape != g0.shape:
        raise ValueError("matrix shapes must agree")
    if float(np.min(np.linalg.eigvalsh(g0))) < -1e-12:
        raise ValueError("Bgram midpoint must be positive semidefinite")

    qr = np.asarray(low_radius, dtype=float)
    gr = np.asarray(Bgram_radius, dtype=float)
    if qr.shape != q0.shape or gr.shape != g0.shape:
        raise ValueError("radius matrix shape mismatch")
    if np.any(qr < 0.0) or np.any(gr < 0.0):
        raise ValueError("radius matrices must be non-negative")

    effective_mid = q0 - g0 / high_coercivity_lower
    effective_radius = qr + gr / high_coercivity_lower
    midpoint_min = float(np.min(np.linalg.eigvalsh(effective_mid)))
    radius_norm = absolute_radius_operator_norm_upper(effective_radius)
    return MatrixFeshbachCertificate(
        effective_midpoint_min_eigenvalue=midpoint_min,
        effective_radius_norm_upper=radius_norm,
        effective_gap_lower=midpoint_min - radius_norm,
    )


def quotient_feshbach_gate_map() -> dict[str, object]:
    return {
        "schema": "SOH_C005_QUOTIENT_FESHBACH_V0_1",
        "identity": (
            "q(ell+h) >= q(ell)-||B ell||^2/nu for h in high kernel, "
            "assuming q_HH>=nu||h||^2 and q(ell,h)=<B ell,h>"
        ),
        "finite_target": "F_N,a = Q_low - G_B/nu",
        "closed": [
            "finite scalar Feshbach lower-bound propagation",
            "interval Q_low and B-image Gram spectral envelopes",
            "effective finite matrix gap plumbing",
        ],
        "open": [
            "construct a form-domain right inverse of the low Fourier-moment map",
            "rigorous localized low-form matrix Q_low(a)",
            "rigorous B_a-image Gram matrix G_B(a)",
            "uniform interval continuation in a",
            "SOH-C005",
            "Riemann Hypothesis",
        ],
        "proof_of_rh": False,
    }
