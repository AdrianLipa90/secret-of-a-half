#!/usr/bin/env python3
"""Regression for the zero-free xi'/xi prime truncation bound."""
from __future__ import annotations

import math

import mpmath as mp


mp.mp.dps = 50


def von_mangoldt(n: int) -> mp.mpf:
    m = n
    factors = []
    p = 2
    while p * p <= m:
        if m % p == 0:
            k = 0
            while m % p == 0:
                m //= p
                k += 1
            factors.append((p, k))
        p = 3 if p == 2 else p + 2
    if m > 1:
        factors.append((m, 1))
    if len(factors) == 1:
        return mp.log(factors[0][0])
    return mp.mpf("0")


def xi_log_derivative(s: mp.mpf) -> mp.mpf:
    return (
        1 / s
        + 1 / (s - 1)
        - mp.log(mp.pi) / 2
        + mp.digamma(s / 2) / 2
        + mp.diff(mp.zeta, s) / mp.zeta(s)
    )


def truncated_target(s: mp.mpf, M: int) -> mp.mpf:
    arch = (
        1 / s
        + 1 / (s - 1)
        - mp.log(mp.pi) / 2
        + mp.digamma(s / 2) / 2
    )
    prime = mp.fsum(
        von_mangoldt(n) / mp.power(n, s)
        for n in range(2, M + 1)
    )
    return arch - prime


def elementary_tail_bound(s: mp.mpf, M: int) -> mp.mpf:
    if s <= 1:
        raise ValueError("s must exceed 1")
    if M < 3:
        raise ValueError("M must be at least 3")
    eta = s - 1
    return mp.power(M, -eta) * (
        mp.log(M) / eta + 1 / (eta * eta)
    )


def main() -> None:
    max_ratio = mp.mpf("0")
    cases = 0

    for a in [1, 2, 3, 4]:
        M = int(mp.floor(mp.e ** (2 * a)))
        for s0 in ["1.2", "1.5", "2.0", "3.0"]:
            s = mp.mpf(s0)
            exact = xi_log_derivative(s)
            approx = truncated_target(s, M)
            error = abs(exact - approx)
            bound = elementary_tail_bound(s, M)
            assert error <= bound
            max_ratio = max(max_ratio, error / bound)
            cases += 1

    print("SOH_LIVSIC_CAYLEY_LOG_DERIVATIVE_PRIME_BRIDGE_V0_1: PASS")
    print("CASES=", cases)
    print("MAX_ERROR_TO_BOUND_RATIO=", mp.nstr(max_ratio, 18))
    print("ZERO_LIST_USED=false")
    print("RH_USED=false")
    print("STATUS=LIV_MD2A_B_CLOSED")


if __name__ == "__main__":
    main()
