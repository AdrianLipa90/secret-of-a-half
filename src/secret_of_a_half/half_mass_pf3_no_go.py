"""SOH-G021: G020-type half-mass PF2 structure does not imply PF3.

This module constructs an exact one-parameter probability law.  The parameter
x is the unique root in (0, 1) of

    36 x^3 + 205 x^2 + 1295 x - 1250 = 0.

With adjacent mass ratios

    q1 = x,
    q2 = x/5,
    q3 = 9x/50,
    qn = 9x/250  (n >= 4),

the resulting sequence has pi_0 = 1/2, total positive-index mass 1/2,
strictly decreasing positive masses, and PF2/log-concavity.  Nevertheless its
G006 solid PF3 ratio-curvature margin at k=2 is exactly -1271/2500.

This is a structural no-go only: it proves that the properties established in
SOH-G020, taken by themselves, cannot imply PF3.  It does not decide PF3 for
the actual Riemann-xi quotient coefficients.
"""
from __future__ import annotations

from fractions import Fraction

import mpmath as mp


PF3_MARGIN_EXACT = Fraction(-1271, 2500)


def normalization_cubic(x: mp.mpf) -> mp.mpf:
    """Return P(x)=36x^3+205x^2+1295x-1250."""

    return 36 * x**3 + 205 * x**2 + 1295 * x - 1250


def normalizing_ratio_numeric(dps: int = 80, iterations: int = 240) -> mp.mpf:
    """Return the unique root x in (0,1) by deterministic bisection."""

    if dps < 40:
        raise ValueError("dps must be at least 40")
    if iterations < 80:
        raise ValueError("iterations must be at least 80")

    with mp.workdps(dps):
        lo = mp.mpf("0")
        hi = mp.mpf("1")
        flo = normalization_cubic(lo)
        fhi = normalization_cubic(hi)
        if not (flo < 0 < fhi):
            raise RuntimeError("normalization cubic is not bracketed on (0,1)")

        for _ in range(iterations):
            mid = (lo + hi) / 2
            fmid = normalization_cubic(mid)
            if fmid < 0:
                lo = mid
            else:
                hi = mid
        return +((lo + hi) / 2)


def adjacent_ratio_numeric(n: int, *, dps: int = 80) -> mp.mpf:
    """Return q_n=pi_n/pi_(n-1) for the G021 counterexample."""

    if n < 1:
        raise ValueError("n must be at least 1")
    with mp.workdps(dps):
        x = normalizing_ratio_numeric(dps=dps)
        if n == 1:
            return +x
        if n == 2:
            return +(x / 5)
        if n == 3:
            return +(9 * x / 50)
        return +(9 * x / 250)


def counterexample_weight_numeric(n: int, *, dps: int = 80) -> mp.mpf:
    """Return pi_n for the normalized G021 counterexample law."""

    if n < 0:
        raise ValueError("n must be nonnegative")
    with mp.workdps(dps):
        if n == 0:
            return mp.mpf("0.5")
        value = mp.mpf("0.5")
        for j in range(1, n + 1):
            value *= adjacent_ratio_numeric(j, dps=dps)
        return +value


def positive_mass_closed_form_numeric(*, dps: int = 80) -> mp.mpf:
    """Return the exact-series positive-index mass evaluated numerically."""

    with mp.workdps(dps):
        x = normalizing_ratio_numeric(dps=dps)
        scaled_tail = (
            x
            + x**2 / 5
            + 9 * x**3 / 250
            + (81 * x**4 / 62500) / (1 - 9 * x / 250)
        )
        return +(scaled_tail / 2)


def pf2_minor_numeric(n: int, *, dps: int = 80) -> mp.mpf:
    """Return pi_n^2-pi_(n-1)pi_(n+1)."""

    if n < 1:
        raise ValueError("n must be at least 1")
    with mp.workdps(dps):
        left = counterexample_weight_numeric(n - 1, dps=dps)
        center = counterexample_weight_numeric(n, dps=dps)
        right = counterexample_weight_numeric(n + 1, dps=dps)
        return +(center * center - left * right)


def solid_pf3_margin_exact() -> Fraction:
    """Return the exact G006 margin at k=2."""

    u = Fraction(1, 5)
    v = Fraction(9, 10)
    w = Fraction(1, 5)
    margin = (1 - v) ** 2 - v**2 * (1 - u) * (1 - w)
    if margin != PF3_MARGIN_EXACT:
        raise RuntimeError("internal exact-margin invariant failed")
    return margin


def solid_pf3_minor_k2_numeric(*, dps: int = 80) -> mp.mpf:
    """Return the k=2 solid 3x3 Toeplitz determinant numerically."""

    with mp.workdps(dps):
        p0, p1, p2, p3, p4 = [
            counterexample_weight_numeric(n, dps=dps) for n in range(5)
        ]
        determinant = (
            -p0 * p2 * p4
            + p0 * p3**2
            + p1**2 * p4
            - 2 * p1 * p2 * p3
            + p2**3
        )
        return +determinant
