#!/usr/bin/env python3
"""Regression for the piecewise-exponential Weil / cross-convolution bridge."""
from __future__ import annotations

import math

import mpmath as mp


mp.mp.dps = 50


def xi_arch_log_derivative(s: mp.mpf) -> mp.mpf:
    return (
        1 / s
        + 1 / (s - 1)
        - mp.log(mp.pi) / 2
        + mp.digamma(s / 2) / 2
    )


def arch_weil_piecewise(p: mp.mpf, q: mp.mpf) -> mp.mpf:
    first = (
        1 / (p - mp.mpf("0.5"))
        + 1 / (p + mp.mpf("0.5"))
        + 1 / (q - mp.mpf("0.5"))
        + 1 / (q + mp.mpf("0.5"))
    )

    def integrand(x):
        return (
            mp.e ** (-p * x)
            + mp.e ** (-q * x)
            - 2 * mp.e ** (-x / 2)
        ) * mp.e ** (x / 2) / (mp.e ** x - mp.e ** (-x))

    regularization = -mp.quad(integrand, [0, 1, mp.inf])
    constant = -(mp.log(4 * mp.pi) + mp.euler)
    return first + constant + regularization


def overlap(a: mp.mpf, y: mp.mpf) -> mp.mpf:
    return 2 * mp.sinh((y + 1) * a) / (y + 1)


def normalized_cross_closed(t: mp.mpf, a: mp.mpf, y: mp.mpf) -> mp.mpf:
    c = y + 1
    d = mp.e ** (-2 * c * a)
    if abs(t) > 2 * a:
        return mp.mpf("0")
    if t >= 0:
        return mp.e ** (-t) * (
            1 - mp.e ** (-c * (2 * a - t))
        ) / (1 - d)
    return mp.e ** (y * t) * (
        1 - mp.e ** (-c * (2 * a + t))
    ) / (1 - d)


def normalized_cross_direct(t: mp.mpf, a: mp.mpf, y: mp.mpf) -> mp.mpf:
    lo = max(-a, t - a)
    hi = min(a, t + a)
    if lo > hi:
        return mp.mpf("0")
    value = mp.quad(
        lambda u: mp.e ** (y * u) * mp.e ** (-(t - u)),
        [lo, hi],
    )
    return value / overlap(a, y)


def limit_piecewise(t: mp.mpf, y: mp.mpf) -> mp.mpf:
    return mp.e ** (-t) if t >= 0 else mp.e ** (y * t)


def main() -> None:
    max_arch_error = mp.mpf("0")
    for p0, q0 in [
        ("1", "1"),
        ("1", "0.8"),
        ("1", "1.5"),
        ("2", "1.2"),
    ]:
        p = mp.mpf(p0)
        q = mp.mpf(q0)
        actual = arch_weil_piecewise(p, q)
        expected = (
            xi_arch_log_derivative(p + mp.mpf("0.5"))
            + xi_arch_log_derivative(q + mp.mpf("0.5"))
        )
        max_arch_error = max(max_arch_error, abs(actual - expected))
        assert abs(actual - expected) < mp.mpf("1e-40")

    max_convolution_error = mp.mpf("0")
    for a0 in ["0.75", "1.0", "2.0"]:
        a = mp.mpf(a0)
        for y0 in ["0.75", "1", "1.5", "2"]:
            y = mp.mpf(y0)
            for frac in ["-1.75", "-1", "-0.25", "0", "0.25", "1", "1.75"]:
                t = mp.mpf(frac) * a
                actual = normalized_cross_direct(t, a, y)
                expected = normalized_cross_closed(t, a, y)
                max_convolution_error = max(
                    max_convolution_error,
                    abs(actual - expected),
                )
                assert abs(actual - expected) < mp.mpf("1e-40")
                assert expected >= -mp.mpf("1e-45")
                assert expected <= limit_piecewise(t, y) + mp.mpf("1e-40")

    # Pointwise convergence regression.
    for y0 in ["0.75", "1", "1.5"]:
        y = mp.mpf(y0)
        for t0 in ["-2", "-0.5", "0.5", "2"]:
            t = mp.mpf(t0)
            errors = []
            for a0 in ["3", "4", "5"]:
                a = mp.mpf(a0)
                errors.append(
                    abs(
                        normalized_cross_closed(t, a, y)
                        - limit_piecewise(t, y)
                    )
                )
            assert errors[-1] <= errors[0]

    print("SOH_PIECEWISE_EXPONENTIAL_WEIL_CROSS_CONVOLUTION_V0_1: PASS")
    print("MAX_ARCH_IDENTITY_ERROR=", mp.nstr(max_arch_error, 18))
    print("MAX_CROSS_CONVOLUTION_ERROR=", mp.nstr(max_convolution_error, 18))
    print("RH_USED=false")
    print("ZERO_LIST_USED=false")
    print("OPERATOR_DOMAIN_BINDING=false")
    print("STATUS=EXACT_FUNCTIONAL_BRIDGE")


if __name__ == "__main__":
    main()
