#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from decimal import Decimal, getcontext
from fractions import Fraction
from math import comb
from pathlib import Path

import mpmath as mp

OUT = Path("reports/SOH_HYB009_EIGHT_CURVATURE_CERTIFICATE_V1.json")

Q = [
    [Fraction(-3), Fraction(2)],
    [Fraction(-15, 2), Fraction(15), Fraction(-4)],
    [Fraction(-75, 4), Fraction(165, 2), Fraction(-56), Fraction(8)],
    [Fraction(-375, 8), Fraction(1635, 4), Fraction(-529), Fraction(180), Fraction(-16)],
    [Fraction(-1875, 16), Fraction(15465, 8), Fraction(-4256), Fraction(2588), Fraction(-528), Fraction(32)],
]

THETA_TAIL_BOUNDS = [
    Fraction(4, 10**28),
    Fraction(2, 10**25),
    Fraction(8, 10**23),
    Fraction(5, 10**20),
    Fraction(3, 10**17),
]


def _fraction_iv(value: Fraction):
    return mp.iv.mpf(value.numerator) / value.denominator


def _fraction_decimal(value: Fraction) -> str:
    getcontext().prec = 100
    return format(Decimal(value.numerator) / Decimal(value.denominator), "f")


def _poly_iv(coefficients: list[Fraction], x):
    value = mp.iv.mpf(0)
    for coefficient in reversed(coefficients):
        value = value * x + _fraction_iv(coefficient)
    return value


def _theta_derivative_intervals(lo: Fraction, hi: Fraction):
    t = mp.iv.mpf([_fraction_decimal(lo), _fraction_decimal(hi)])
    exp2t = mp.iv.exp(2 * t)
    exp5t2 = mp.iv.exp(mp.iv.mpf("2.5") * t)
    totals = [mp.iv.mpf(0) for _ in range(5)]
    for n in range(1, 5):
        a = mp.iv.pi * n * n
        r = a * exp2t
        common = 4 * a * exp5t2 * mp.iv.exp(-r)
        for order in range(5):
            totals[order] += common * _poly_iv(Q[order], r)
    for order, tail in enumerate(THETA_TAIL_BOUNDS):
        bound = _fraction_decimal(tail)
        if order == 0:
            totals[order] += mp.iv.mpf(["0", bound])
        else:
            totals[order] += mp.iv.mpf([f"-{bound}", bound])
    return totals


def _l2_l4_intervals(lo: Fraction, hi: Fraction):
    phi0, phi1, phi2, phi3, phi4 = _theta_derivative_intervals(lo, hi)
    a1 = phi1 / phi0
    a2 = phi2 / phi0
    a3 = phi3 / phi0
    a4 = phi4 / phi0
    l2 = a1 * a1 - a2
    l4 = -a4 + 4 * a3 * a1 + 3 * a2 * a2 - 12 * a2 * a1 * a1 + 6 * a1**4
    return l2, l4


def _certify_compact() -> dict[str, object]:
    mp.iv.dps = 36
    end = Fraction(9, 20)
    stack: list[tuple[Fraction, Fraction, int]] = [(Fraction(0), end, 0)]
    boxes = 0
    max_depth = 0
    min_l4_lower = float("inf")
    min_eight_margin_lower = float("inf")
    while stack:
        lo, hi, depth = stack.pop()
        l2, l4 = _l2_l4_intervals(lo, hi)
        m1 = l4
        m2 = 8 * l2 - l4
        if m1.a > 0 and m2.a > 0:
            boxes += 1
            max_depth = max(max_depth, depth)
            min_l4_lower = min(min_l4_lower, float(m1.a))
            min_eight_margin_lower = min(min_eight_margin_lower, float(m2.a))
            continue
        if depth >= 18:
            raise RuntimeError(f"compact interval certification failed on [{lo}, {hi}]")
        mid = (lo + hi) / 2
        stack.append((mid, hi, depth + 1))
        stack.append((lo, mid, depth + 1))
    return {
        "interval": ["0", "9/20"],
        "theta_terms_explicit": 4,
        "theta_tail_enclosed": True,
        "certified_boxes": boxes,
        "max_bisection_depth": max_depth,
        "minimum_L4_lower_margin": format(min_l4_lower, ".17g"),
        "minimum_8L2_minus_L4_lower_margin": format(min_eight_margin_lower, ".17g"),
    }


def _shift_polynomial(coefficients: list[Fraction], shift: int) -> list[Fraction]:
    out = [Fraction(0) for _ in coefficients]
    for power, coefficient in enumerate(coefficients):
        for j in range(power + 1):
            out[j] += coefficient * comb(power, j) * Fraction(shift) ** (power - j)
    return out


def _positive_after_shift(coefficients: list[Fraction], shift: int) -> list[Fraction]:
    shifted = _shift_polynomial(coefficients, shift)
    if not all(value > 0 for value in shifted):
        raise RuntimeError(f"polynomial positivity after shift {shift} failed")
    return shifted


def _analytic_tail() -> dict[str, object]:
    x = Fraction(9, 10)
    exp_lower = sum(x**k / Fraction(math.factorial(k)) for k in range(5))
    if not exp_lower > Fraction(7, 3):
        raise RuntimeError("e^(9/10)>7/3 certificate failed")

    single_l4_minus_100_num = [Fraction(-8100), Fraction(23760), Fraction(-22752), Fraction(13440), Fraction(-3136), Fraction(256)]
    single_eight_margin_minus_100_num = [Fraction(-8100), Fraction(23760), Fraction(-29664), Fraction(13440), Fraction(-3136), Fraction(256)]
    _positive_after_shift(single_l4_minus_100_num, 7)
    _positive_after_shift(single_eight_margin_minus_100_num, 7)

    R0 = Fraction(28)
    d1 = Fraction(5, 2)
    d2 = Fraction(25, 4)
    d3 = Fraction(10)
    d4 = Fraction(105, 4)
    bell_required = [
        Fraction(1),
        d1,
        d2 / R0 + d1**2,
        d3 / R0**2 + 3 * d1 * d2 / R0 + d1**3,
        d4 / R0**3 + 4 * d1 * d3 / R0**2 + 3 * d2**2 / R0**2 + 6 * d1**2 * d2 / R0 + d1**4,
    ]
    bell = [Fraction(1), Fraction(4), Fraction(26), Fraction(204), Fraction(1886)]
    if not all(required < declared for required, declared in zip(bell_required[1:], bell[1:])):
        raise RuntimeError("Bell constants failed")

    rho_ratio = Fraction(3, 2) ** 12 / Fraction(20) ** 10
    if not rho_ratio < Fraction(1, 1001):
        raise RuntimeError("rho derivative ratio failed")

    rho_envelopes = []
    for order, constant in enumerate(bell):
        first = 2 * constant * Fraction(44, 7) ** order * 2 ** (4 + 2 * order) / Fraction(20) ** 7
        rho_envelopes.append(first * Fraction(1001, 1000))

    _, r1, r2, r3, r4 = rho_envelopes
    log_second = r2 + r1**2
    log_fourth = r4 + 4 * r1 * r3 + 3 * r2**2 + 12 * r1**2 * r2 + 6 * r1**4
    perturb8 = log_fourth + 8 * log_second
    if not log_second < Fraction(1, 1000):
        raise RuntimeError("tail second derivative perturbation failed")
    if not log_fourth < Fraction(19):
        raise RuntimeError("tail fourth derivative perturbation failed")
    if not perturb8 < Fraction(20):
        raise RuntimeError("tail eight-curvature perturbation failed")
    return {
        "interval": ["9/20", "infinity"],
        "r1_lower": "7",
        "log_second_abs_upper": str(log_second),
        "log_fourth_abs_upper": str(log_fourth),
        "eight_perturbation_abs_upper": str(perturb8),
        "L4_tail_lower_margin": ">81",
        "8L2_minus_L4_tail_lower_margin": ">80",
    }


def main():
    payload = {
        "certificate": "SOH_HYB009_EIGHT_CURVATURE_CERTIFICATE_V1",
        "status": "COMPUTER_ASSISTED_INTERVAL_PLUS_ANALYTIC_TAIL_PASS",
        "claim": "For L=-log K: 0 < L''''(t) < 8 L''(t) for every real t.",
        "compact": _certify_compact(),
        "analytic_tail": _analytic_tail(),
        "proof_boundary": {"PF3_proved": False, "RH_proved": False},
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
