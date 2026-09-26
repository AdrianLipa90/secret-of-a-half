#!/usr/bin/env python3
"""Regression for the explicit large-a finite-cross Weil error envelope."""
from __future__ import annotations

import math


def phi(k: float, a: float) -> float:
    if abs(k) < 1e-15:
        return 2.0 * a
    return math.expm1(2.0 * a * k) / k


def pointwise_bound(a: float, y: float) -> float:
    if not (a >= 1.0 and 1.0 <= y <= 2.0):
        raise ValueError("regression domain is a>=1 and 1<=y<=2")
    c = y + 1.0
    d = math.exp(-2.0 * c * a)
    D = 1.0 - d

    Eel = (
        d / D
        * (
            phi(y + 0.5, a)
            + phi(y - 0.5, a)
            + phi(1.5, a)
            + phi(0.5, a)
        )
        + 2.0 * math.exp(-a)
        + (2.0 / 3.0) * math.exp(-3.0 * a)
        + math.exp(-2.0 * a * (y - 0.5)) / (y - 0.5)
        + math.exp(-2.0 * a * (y + 0.5)) / (y + 0.5)
    )

    Ep = (
        2.0 * a / D
        * (math.exp(-a) + math.exp(-a * (2.0 * y - 1.0)))
        + (4.0 * a + 4.0) * math.exp(-a)
        + math.exp(-2.0 * a * (y - 0.5))
        * (
            2.0 * a / (y - 0.5)
            + 1.0 / (y - 0.5) ** 2
        )
    )

    Ereg = (
        d * c * (1.0 + 4.0 * a) / (2.0 * D)
        * (phi(y - 0.5, a) + phi(0.5, a))
        + 1.0 / (1.0 - math.exp(-2.0))
        * (
            (2.0 / 3.0) * math.exp(-3.0 * a)
            + math.exp(-2.0 * a * (y + 0.5)) / (y + 0.5)
        )
    )
    return Eel + Ep + Ereg


def uniform_bound(a: float) -> float:
    D = 1.0 - math.exp(-4.0 * a)
    Eel = (
        (4.0 + 4.0 / (3.0 * D)) * math.exp(-a)
        + (4.0 / 3.0 + 4.0 / D) * math.exp(-3.0 * a)
    )
    Ep = (
        4.0 * a / D + 8.0 * (a + 1.0)
    ) * math.exp(-a)
    Ereg = (
        6.0 * (1.0 + 4.0 * a) / D
        + 4.0 / (3.0 * (1.0 - math.exp(-2.0)))
    ) * math.exp(-3.0 * a)
    return Eel + Ep + Ereg


def main() -> None:
    cases = 0
    previous = None
    for a in [1.0, 2.0, 4.0, 8.0, 16.0]:
        U = uniform_bound(a)
        for j in range(101):
            y = 1.0 + j / 100.0
            E = pointwise_bound(a, y)
            assert E <= U + 1e-12
            cases += 1
        if previous is not None and a >= 4:
            assert U < previous
        previous = U

    assert uniform_bound(16.0) < uniform_bound(8.0)
    print("SOH_EXPLICIT_LARGE_A_FINITE_CROSS_WEIL_ERROR_V0_1: PASS")
    print("CASES=", cases)
    print("UNIFORM_BOUND_A8=", uniform_bound(8.0))
    print("UNIFORM_BOUND_A16=", uniform_bound(16.0))
    print("ASYMPTOTIC_ORDER=O(a exp(-a))")
    print("RH_USED=false")
    print("ZERO_LIST_USED=false")
    print("STATUS=EFFECTIVE_DENOMINATOR_CHANNEL_CLOSED")


if __name__ == "__main__":
    main()
