"""SOH-G017 fixed-root exclusion from quantitative Xi-kernel curvature.

The theorem-level proof is analytic and lives in the accompanying note and
monograph chapter.  This module exposes the conservative rational constants
and numerical regression checks only.
"""
from __future__ import annotations

from fractions import Fraction

import mpmath as mp

from .negative_inversion_zero_set import completed_xi
from .quotient_zero_set import quotient_F


def g004_variance_upper() -> Fraction:
    """Return the conservative rational variance bound already used by G004."""
    n2_bound = Fraction(14112, 8000)
    n3_bound = Fraction(98 * 81 * 64, 20**8)
    tail_ratio = Fraction(12, 20**7)
    return n2_bound + n3_bound / (1 - tail_ratio)


def log_phi_curvature_upper() -> Fraction:
    """Conservative upper bound for (log Phi)'' from G004 channel bounds."""
    return Fraction(-12, 1) + g004_variance_upper()


def safe_strong_concavity_kappa() -> Fraction:
    """Safe integer curvature constant kappa with -(log Phi)'' > kappa."""
    bound = log_phi_curvature_upper()
    if not bound < -10:
        raise AssertionError("G004 constants no longer certify kappa=10")
    return Fraction(10, 1)


def second_moment_ratio_upper() -> Fraction:
    """Analytic consequence m2/m0 < 1/kappa for kappa=10."""
    return Fraction(1, 1) / safe_strong_concavity_kappa()


def fixed_root_lower_ratio() -> Fraction:
    """Analytic lower ratio F(-1/4)/F(0) > 1 - 1/(8*kappa)."""
    kappa = safe_strong_concavity_kappa()
    return Fraction(1, 1) - Fraction(1, 8) / kappa


def fixed_root_numeric_values(dps: int = 60) -> dict[str, mp.mpf | mp.mpc]:
    """High-precision regression values; not used as the proof."""
    if dps < 30:
        raise ValueError("dps must be at least 30")
    with mp.workdps(dps):
        f0 = quotient_F(mp.mpf("0"))
        fm = quotient_F(mp.mpf("-0.25"))
        xi_fixed = completed_xi(mp.mpc("0.5", "0.5"))
        return {
            "F0": +f0,
            "F_minus_quarter": +fm,
            "ratio": +(fm / f0),
            "xi_half_plus_i_half": +xi_fixed,
        }
