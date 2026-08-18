"""SOH-G019 coefficient-majorant positive-real-part disk for the xi quotient.

Let F be defined by

    xi(1/2 + z) = F(z**2) = sum_{n>=0} a_n w**n,

with the previously proved coefficients a_n > 0.  The analytic theorem defines
R_* as the unique positive solution of F(R_*) = 2 F(0).  Then Re F(w) > 0 on
the closed disk |w| <= R_*.  Numerical helpers below are regression/receipt
utilities only; they are not the proof of existence, uniqueness, or zero
exclusion.
"""
from __future__ import annotations

import mpmath as mp

from .quotient_zero_set import quotient_F


def _nonnegative_real(value: float | mp.mpf, *, name: str) -> mp.mpf:
    value = mp.mpf(value)
    if not mp.isfinite(value) or value < 0:
        raise ValueError(f"{name} must be a finite nonnegative real")
    return value


def F0_numeric() -> mp.mpf:
    """Return the numerical regression value F(0)=xi(1/2)."""

    return mp.re(quotient_F(mp.mpf("0")))


def positive_axis_F(radius: float | mp.mpf) -> mp.mpf:
    """Evaluate F(r) on the nonnegative real axis."""

    radius = _nonnegative_real(radius, name="radius")
    value = quotient_F(radius)
    return mp.re(value)


def coefficient_majorant_margin(radius: float | mp.mpf) -> mp.mpf:
    r"""Return 2 F(0) - F(r).

    For |w| <= r, positivity of all Taylor coefficients gives

        Re F(w) >= 2 F(0) - F(r).

    Thus a positive return value is a rigorous consequence of the analytic
    coefficient theorem, once r is known to lie below R_*.
    """

    radius = _nonnegative_real(radius, name="radius")
    return 2 * F0_numeric() - positive_axis_F(radius)


def majorant_threshold_numeric(*, dps: int = 80, iterations: int = 260) -> mp.mpf:
    r"""Numerically locate R_* defined by F(R_*) = 2F(0) by monotone bisection.

    This routine is a deterministic regression helper.  The theorem's
    existence and uniqueness follow analytically from a_n>0, a_1>0, and the
    unbounded growth F(r) >= F(0)+a_1 r.
    """

    if dps < 30:
        raise ValueError("dps must be at least 30")
    if iterations < 80:
        raise ValueError("iterations must be at least 80")

    with mp.workdps(dps):
        target = 2 * F0_numeric()
        lo = mp.mpf("0")
        hi = mp.mpf("1")
        while positive_axis_F(hi) <= target:
            hi *= 2
        for _ in range(iterations):
            mid = (lo + hi) / 2
            if positive_axis_F(mid) < target:
                lo = mid
            else:
                hi = mid
        return +(lo + hi) / 2


def centered_z_radius_numeric(*, dps: int = 80) -> mp.mpf:
    """Return sqrt(R_*), the corresponding radius in z=s-1/2."""

    with mp.workdps(dps):
        return +mp.sqrt(majorant_threshold_numeric(dps=dps))


def sampled_min_real_part(radius: float | mp.mpf, *, samples: int = 96) -> mp.mpf:
    """Sample min Re F(w) on |w|=radius as a regression diagnostic only."""

    radius = _nonnegative_real(radius, name="radius")
    if samples < 8:
        raise ValueError("samples must be at least 8")
    values = []
    for k in range(samples):
        theta = 2 * mp.pi * k / samples
        w = radius * mp.e ** (mp.j * theta)
        values.append(mp.re(quotient_F(w)))
    return min(values)
