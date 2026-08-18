"""SOH-G020 canonical half-mass PF2 law for the even xi quotient.

Analytic input:
- SOH-G019: R_* is defined by F(R_*)=2F(0), so the scaled positive
  coefficients carry exactly half of the normalized mass away from index 0.
- SOH-G005: the coefficient sequence a_n is PF2/log-concave.

The theorem is algebraic. Numerical helpers are regression checks only.
"""
from __future__ import annotations

from functools import lru_cache

import mpmath as mp

from .caratheodory_disk import F0_numeric, majorant_threshold_numeric
from .negative_inversion_zero_set import completed_xi


@lru_cache(maxsize=None)
def canonical_radius_numeric(dps: int = 70) -> mp.mpf:
    """Return the numerical G019 radius R_* for regression work."""

    if dps < 40:
        raise ValueError("dps must be at least 40")
    with mp.workdps(dps):
        return +majorant_threshold_numeric(dps=dps, iterations=220)


@lru_cache(maxsize=None)
def quotient_coefficient_numeric(n: int, dps: int = 70) -> mp.mpf:
    r"""Return a_n = xi^(2n)(1/2)/(2n)! numerically."""

    if n < 0:
        raise ValueError("n must be nonnegative")
    if dps < 40:
        raise ValueError("dps must be at least 40")
    with mp.workdps(dps):
        order = 2 * n
        derivative = mp.diff(
            lambda z: completed_xi(mp.mpf("0.5") + z),
            mp.mpf("0"),
            order,
        )
        return +mp.re(derivative / mp.factorial(order))


def canonical_half_mass_weight(n: int, *, dps: int = 70) -> mp.mpf:
    r"""Return pi_n for the G020 probability law.

    pi_0 = 1/2,
    pi_n = a_n R_*^n / (2 F(0)) for n>=1.
    """

    if n < 0:
        raise ValueError("n must be nonnegative")
    if n == 0:
        return mp.mpf("0.5")
    with mp.workdps(dps):
        radius = canonical_radius_numeric(dps)
        a_n = quotient_coefficient_numeric(n, dps)
        return +(a_n * radius**n / (2 * F0_numeric()))


def pf2_minor_numeric(n: int, *, dps: int = 70) -> mp.mpf:
    """Return pi_n^2-pi_(n-1)pi_(n+1) as a regression diagnostic."""

    if n < 1:
        raise ValueError("n must be at least 1")
    with mp.workdps(dps):
        left = canonical_half_mass_weight(n - 1, dps=dps)
        center = canonical_half_mass_weight(n, dps=dps)
        right = canonical_half_mass_weight(n + 1, dps=dps)
        return +(center * center - left * right)


def sharpened_coefficient_envelope(n: int, *, dps: int = 70) -> mp.mpf:
    r"""Return F(0)/(n R_*^n), the exact G020 envelope for n>=1."""

    if n < 1:
        raise ValueError("n must be at least 1")
    with mp.workdps(dps):
        radius = canonical_radius_numeric(dps)
        return +(F0_numeric() / (n * radius**n))
