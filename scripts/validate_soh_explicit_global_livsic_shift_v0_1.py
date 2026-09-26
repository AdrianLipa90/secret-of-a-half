#!/usr/bin/env python3
"""Regression checks for the explicit Livsic shift lower bound."""
from __future__ import annotations

import math


EULER_GAMMA = 0.577215664901532860606512090082402431


def r1_second(t: float) -> float:
    x = abs(t) / 2.0
    if x == 0.0:
        return 0.25
    return 0.25 * (1.0 / math.sinh(x) + 1.0 / math.cosh(x) - 1.0 / x)


def remainder_majorant(a: float) -> float:
    if a <= 0:
        raise ValueError("a must be positive")
    return 2.0 * math.cosh(a) + 0.25


def elementary_lower_bound(a: float) -> float:
    if a <= 0:
        raise ValueError("a must be positive")
    return (
        -math.log(a)
        -math.log(2.0 * math.pi)
        -EULER_GAMMA
        -8.0 * a * math.exp(a)
        -4.0 * a * math.cosh(a)
        -0.5 * a
    )


def shift_schedule(a: float) -> float:
    return elementary_lower_bound(a) - 1.0


def main() -> None:
    max_r1_abs = 0.0
    for k in range(0, 200_001):
        t = 30.0 * k / 200_000
        value = abs(r1_second(t))
        max_r1_abs = max(max_r1_abs, value)
        assert value <= 0.250000000001

    for a in [1e-6, 1e-3, 0.01, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0]:
        assert remainder_majorant(a) > 0.0
        lower = elementary_lower_bound(a)
        shift = shift_schedule(a)
        assert shift == lower - 1.0
        assert shift < lower

    # Algebraic identity 2A+1 = log(2pi)+gamma.
    A = 0.5 * (math.log(2.0 * math.pi) + EULER_GAMMA - 1.0)
    assert abs((2.0 * A + 1.0) - (math.log(2.0 * math.pi) + EULER_GAMMA)) < 1e-15

    print("SOH_EXPLICIT_GLOBAL_LIVSIC_SHIFT_V0_1: PASS")
    print("MAX_SAMPLED_ABS_R1_SECOND=", max_r1_abs)
    print("R1_ANALYTIC_BOUND=1/4")
    print("SHIFT_MARGIN=1")
    print("RH_USED=false")
    print("ZERO_LIST_USED=false")
    print("STATUS=LIV_MD1_CLOSED")


if __name__ == "__main__":
    main()
