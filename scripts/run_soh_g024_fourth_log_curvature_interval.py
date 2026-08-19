#!/usr/bin/env python3
from __future__ import annotations

import json
from decimal import Decimal, getcontext
from fractions import Fraction
from math import comb
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports" / "SOH_G024_FOURTH_LOG_CURVATURE_INTERVAL_V1.json"

Q = [
    [Fraction(-3), Fraction(2)],
    [Fraction(-15, 2), Fraction(15), Fraction(-4)],
    [Fraction(-75, 4), Fraction(165, 2), Fraction(-56), Fraction(8)],
    [Fraction(-375, 8), Fraction(1635, 4), Fraction(-529), Fraction(180), Fraction(-16)],
    [
        Fraction(-1875, 16),
        Fraction(15465, 8),
        Fraction(-4256),
        Fraction(2588),
        Fraction(-528),
        Fraction(32),
    ],
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


def _log_curvature_margin_interval(lo: Fraction, hi: Fraction):
    phi0, phi1, phi2, phi3, phi4 = _theta_derivative_intervals(lo, hi)
    a1 = phi1 / phi0
    a2 = phi2 / phi0
    a3 = phi3 / phi0
    a4 = phi4 / phi0
    l2 = a1 * a1 - a2
    l4 = -a4 + 4 * a3 * a1 + 3 * a2 * a2 - 12 * a2 * a1 * a1 + 6 * a1**4
    return 20 * l2 - l4


def _shift_polynomial(coefficients: list[Fraction], shift: int) -> list[Fraction]:
    out = [Fraction(0) for _ in coefficients]
    for power, coefficient in enumerate(coefficients):
        for j in range(power + 1):
            out[j] += coefficient * comb(power, j) * Fraction(shift) ** (power - j)
    return out


def _positive_after_shift(coefficients: list[Fraction], shift: int) -> list[Fraction]:
    shifted = _shift_polynomial(coefficients, shift)
    if not all(value > 0 for value in shifted):
        raise RuntimeError(f"polynomial positivity after r=x+{shift} failed: {shifted}")
    return shifted


def _analytic_bound_checks() -> dict[str, object]:
    theta_ratio = Fraction(6, 5) ** 12 / Fraction(20) ** 11
    if not theta_ratio < Fraction(1, 1001):
        raise RuntimeError("theta-tail ratio certificate failed")

    abs_q_sums = [sum(abs(c) for c in coefficients) for coefficients in Q]
    for order, coefficient_sum in enumerate(abs_q_sums):
        first = (
            4
            * coefficient_sum
            * Fraction(22, 7) ** (order + 2)
            * 5 ** (2 * order + 4)
            / Fraction(20) ** 25
        )
        total = first * Fraction(1001, 1000)
        if not total < THETA_TAIL_BOUNDS[order]:
            raise RuntimeError(f"theta derivative tail bound failed for order {order}")

    exp_four_fifths_lower = Fraction(1) + Fraction(4, 5) + Fraction(4, 5) ** 2 / 2
    if not exp_four_fifths_lower > 2:
        raise RuntimeError("exp(4/5)>2 certificate failed")

    p1_minus_390_num = [
        Fraction(-31590),
        Fraction(92880),
        Fraction(-106128),
        Fraction(52800),
        Fraction(-12384),
        Fraction(1024),
    ]
    shifted = _positive_after_shift(p1_minus_390_num, 6)
    expected_shifted = [
        Fraction(22842),
        Fraction(457488),
        Fraction(381168),
        Fraction(124224),
        Fraction(18336),
        Fraction(1024),
    ]
    if shifted != expected_shifted:
        raise RuntimeError("single-channel P1>390 polynomial identity mismatch")

    # Explicit channel logarithmic-derivative checks for r>=6.  Since each g^(j)
    # is negative there, |g^(j)| < c_j r is equivalent to c_j r + g^(j)>0.
    # Clearing positive denominators yields the following numerators.
    channel_bound_numerators = {
        1: [Fraction(-15), Fraction(18)],
        2: [Fraction(-15), Fraction(-12), Fraction(4)],
        3: [Fraction(0), Fraction(144), Fraction(96)],
        4: [Fraction(-459), Fraction(-3384), Fraction(696), Fraction(-480), Fraction(80)],
    }
    channel_bound_shifts = {
        order: _positive_after_shift(coefficients, 6)
        for order, coefficients in channel_bound_numerators.items()
    }

    # Bell-polynomial safety constants for rho_n=exp(g_n-g_1).  For n>=2,
    # r_1<=r_n/4 and r_n>24.  The channel bounds imply
    # |d1|<5R/2, |d2|<25R/4, |d3|<10R, |d4|<105R/4, R=r_n.
    # Normalize the exact Bell formulas by R^k and use R>=24.
    R0 = Fraction(24)
    d1 = Fraction(5, 2)
    d2 = Fraction(25, 4)
    d3 = Fraction(10)
    d4 = Fraction(105, 4)
    bell_required = [
        Fraction(1),
        d1,
        d2 / R0 + d1**2,
        d3 / R0**2 + 3 * d1 * d2 / R0 + d1**3,
        d4 / R0**3
        + 4 * d1 * d3 / R0**2
        + 3 * d2**2 / R0**2
        + 6 * d1**2 * d2 / R0
        + d1**4,
    ]
    bell = [Fraction(1), Fraction(4), Fraction(26), Fraction(204), Fraction(1886)]
    if not all(required < declared for required, declared in zip(bell_required[1:], bell[1:])):
        raise RuntimeError(f"Bell safety constants failed: required={bell_required}, declared={bell}")

    rho_ratio = Fraction(3, 2) ** 12 / Fraction(20) ** 10
    if not rho_ratio < Fraction(1, 1001):
        raise RuntimeError("rho derivative ratio certificate failed")

    rho_targets = [
        Fraction(1, 10**6),
        Fraction(1, 19000),
        Fraction(9, 1000),
        Fraction(17, 10),
        Fraction(378),
    ]
    rho_envelopes: list[Fraction] = []
    for order, constant in enumerate(bell):
        first = (
            2
            * constant
            * Fraction(44, 7) ** order
            * 2 ** (4 + 2 * order)
            / Fraction(20) ** 6
        )
        total = first * Fraction(1001, 1000)
        rho_envelopes.append(total)
        if not total < rho_targets[order]:
            raise RuntimeError(f"rho derivative envelope failed for order {order}")

    r1, r2, r3, r4 = rho_targets[1:]
    log_second = r2 + r1**2
    log_fourth = r4 + 4 * r1 * r3 + 3 * r2**2 + 12 * r1**2 * r2 + 6 * r1**4
    perturbation = log_fourth + 20 * log_second
    if not log_second < Fraction(1, 100):
        raise RuntimeError("log(1+rho) second derivative bound failed")
    if not log_fourth < 379:
        raise RuntimeError("log(1+rho) fourth derivative bound failed")
    if not perturbation < 380:
        raise RuntimeError("analytic tail perturbation bound failed")

    return {
        "theta_tail_ratio_upper": str(theta_ratio),
        "theta_tail_bounds": [str(value) for value in THETA_TAIL_BOUNDS],
        "exp_four_fifths_series_lower": str(exp_four_fifths_lower),
        "single_channel_margin_lower": "390",
        "channel_log_derivative_bounds": ["|g'|<2r", "|g''|<5r", "|g'''|<8r", "|g''''|<21r"],
        "channel_bound_shifted_numerators": {
            str(order): [str(value) for value in values]
            for order, values in channel_bound_shifts.items()
        },
        "bell_required_normalized": [str(value) for value in bell_required],
        "bell_declared": [str(value) for value in bell],
        "rho_ratio_upper": str(rho_ratio),
        "rho_derivative_envelopes": [str(value) for value in rho_envelopes],
        "log_rho_second_abs_upper": str(log_second),
        "log_rho_fourth_abs_upper": str(log_fourth),
        "tail_perturbation_upper": str(perturbation),
        "analytic_tail_margin_lower": "10",
    }


def _interval_core_certificate() -> dict[str, object]:
    stack: list[tuple[Fraction, Fraction, int]] = [(Fraction(0), Fraction(2, 5), 0)]
    boxes = 0
    max_depth = 0
    min_lower = float("inf")

    while stack:
        lo, hi, depth = stack.pop()
        margin = _log_curvature_margin_interval(lo, hi)
        if margin.a > 0:
            boxes += 1
            max_depth = max(max_depth, depth)
            min_lower = min(min_lower, float(margin.a))
            continue

        if depth >= 14:
            raise RuntimeError(
                f"interval enclosure failed to certify positivity on [{lo}, {hi}]"
            )
        mid = (lo + hi) / 2
        stack.append((mid, hi, depth + 1))
        stack.append((lo, mid, depth + 1))

    return {
        "interval": ["0", "2/5"],
        "theta_terms_explicit": 4,
        "certified_boxes": boxes,
        "max_bisection_depth": max_depth,
        "minimum_interval_lower_margin": format(min_lower, ".17g"),
        "claim": "20*L''(t)-L''''(t)>0 on 0<=t<=2/5",
    }


def main() -> None:
    analytic = _analytic_bound_checks()
    interval = _interval_core_certificate()

    payload = {
        "certificate": "SOH_G024_FOURTH_LOG_CURVATURE_INTERVAL_V1",
        "status": "COMPUTER_ASSISTED_INTERVAL_PLUS_ANALYTIC_TAIL_PASS",
        "claim": "For L=-log K of the even full-line Riemann kernel, L''''(t)<20 L''(t) for every real t.",
        "symmetry": "L is even, so certification on t>=0 covers the full line.",
        "interval_core": interval,
        "analytic_tail": analytic,
        "proof_boundary": {
            "interval_engine": "mpmath.iv outward interval arithmetic",
            "infinite_theta_tail_bounded_analytically": True,
            "analytic_tail_from_t_ge_2_over_5": True,
            "channel_and_bell_bounds_checked_as_exact_rational_inequalities": True,
            "rh_proved": False,
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
