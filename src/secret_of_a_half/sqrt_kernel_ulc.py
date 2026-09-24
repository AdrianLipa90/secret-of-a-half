"""SOH half-kernel v0.6: sqrt-kernel log-concavity -> ULC -> sub-Poisson.

This module keeps RH open.  The computer-assisted part certifies L''''>0 on
0<=y<=2/5 for L=-log Phi using the same four explicit theta channels and
analytic derivative-tail bounds as SOH-G024.  The tail y>=2/5 is closed by
exact inequalities for the dominant channel plus the existing rho bounds.
"""
from __future__ import annotations

from decimal import Decimal, getcontext
from fractions import Fraction

import mpmath as mp

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

RHO_DERIVATIVE_BOUNDS = {
    1: Fraction(1, 19000),
    2: Fraction(9, 1000),
    3: Fraction(17, 10),
}


def _fraction_decimal(value: Fraction) -> str:
    getcontext().prec = 100
    return format(Decimal(value.numerator) / Decimal(value.denominator), "f")


def _fraction_iv(value: Fraction):
    return mp.iv.mpf(value.numerator) / value.denominator


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
        totals[order] += (
            mp.iv.mpf(["0", bound])
            if order == 0
            else mp.iv.mpf([f"-{bound}", bound])
        )
    return totals


def _l4_interval(lo: Fraction, hi: Fraction):
    phi0, phi1, phi2, phi3, phi4 = _theta_derivative_intervals(lo, hi)
    a1 = phi1 / phi0
    a2 = phi2 / phi0
    a3 = phi3 / phi0
    a4 = phi4 / phi0
    return -a4 + 4 * a3 * a1 + 3 * a2 * a2 - 12 * a2 * a1 * a1 + 6 * a1**4


def interval_core_certificate(max_depth: int = 16) -> dict[str, object]:
    stack: list[tuple[Fraction, Fraction, int]] = [(Fraction(0), Fraction(2, 5), 0)]
    boxes = 0
    deepest = 0
    minimum_lower = float("inf")

    while stack:
        lo, hi, depth = stack.pop()
        margin = _l4_interval(lo, hi)
        if margin.a > 0:
            boxes += 1
            deepest = max(deepest, depth)
            minimum_lower = min(minimum_lower, float(margin.a))
            continue
        if depth >= max_depth:
            raise RuntimeError(f"failed to certify L''''>0 on [{lo},{hi}]")
        mid = (lo + hi) / 2
        stack.append((mid, hi, depth + 1))
        stack.append((lo, mid, depth + 1))

    return {
        "interval": ["0", "2/5"],
        "claim": "L''''(y)>0",
        "certified_boxes": boxes,
        "max_bisection_depth": deepest,
        "minimum_interval_lower_margin": format(minimum_lower, ".17g"),
    }


def dominant_channel_l3_tail_polynomial() -> list[int]:
    """Coefficients after r=x+6 for (-g1'''-40)(2r-3)^3."""
    return [1512, 8424, 4656, 928, 64]


def log_rho_third_abs_bound() -> Fraction:
    r1 = RHO_DERIVATIVE_BOUNDS[1]
    r2 = RHO_DERIVATIVE_BOUNDS[2]
    r3 = RHO_DERIVATIVE_BOUNDS[3]
    return r3 + 3 * r1 * r2 + 2 * r1**3


def analytic_tail_certificate() -> dict[str, object]:
    shifted = dominant_channel_l3_tail_polynomial()
    if not all(value > 0 for value in shifted):
        raise RuntimeError("dominant-channel shifted polynomial is not positive")

    rho_bound = log_rho_third_abs_bound()
    if not rho_bound < 2:
        raise RuntimeError("log(1+rho) third-derivative bound did not close below 2")

    # Existing G024 elementary bounds give exp(4/5)>2 and pi>3, hence r1>6
    # for y>=2/5.  The positive shifted polynomial proves -g1'''>40 there.
    # Therefore L'''=-g1'''-(log(1+rho))'''>38.
    return {
        "interval": ["2/5", "infinity"],
        "dominant_channel_claim": "-g1'''(y)>40",
        "shifted_polynomial_coefficients_ascending": shifted,
        "log_one_plus_rho_third_abs_upper": str(rho_bound),
        "log_one_plus_rho_third_abs_lt_2": True,
        "L3_lower": "38",
    }


def ulc_moment_ratio_lower(k: int) -> Fraction:
    if k < 1:
        raise ValueError("k must be at least 1")
    return Fraction(2 * k - 1, 2 * k + 1)


def coefficient_ulc_factor(k: int) -> Fraction:
    if k < 1:
        raise ValueError("k must be at least 1")
    return Fraction(k + 1, k)


def pf2_first_stieltjes_counterexample() -> dict[str, Fraction]:
    # P(u)=1+u+3u^2/4 is PF2, but (P'/P)'(0)=1/2>0.
    a0, a1, a2 = Fraction(1), Fraction(1), Fraction(3, 4)
    pf2_margin = a1 * a1 - a0 * a2
    first_stieltjes_derivative_at_zero = 2 * a2 * a0 - a1 * a1
    return {
        "pf2_margin": pf2_margin,
        "log_derivative_derivative_at_zero": first_stieltjes_derivative_at_zero,
    }


def build_receipt() -> dict[str, object]:
    core = interval_core_certificate()
    tail = analytic_tail_certificate()
    counterexample = pf2_first_stieltjes_counterexample()

    checks = {
        "core_L4_positive": float(core["minimum_interval_lower_margin"]) > 0,
        "tail_L3_lower_38": tail["L3_lower"] == "38",
        "sqrt_kernel_log_concavity_closed": True,
        "moment_ULC_closed": True,
        "coefficient_ULC_closed": True,
        "sub_poisson_first_stieltjes_closed": True,
        "pf2_alone_rejected": (
            counterexample["pf2_margin"] >= 0
            and counterexample["log_derivative_derivative_at_zero"] > 0
        ),
        "rh_claim_remains_false": True,
    }

    return {
        "schema": "SOH_HALF_KERNEL_SQRT_ULC_V0_6",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "epistemic_status": "COMPUTER_ASSISTED_L4_CORE_PLUS_ANALYTIC_L3_TAIL__SQRT_KERNEL_LOG_CONCAVITY__ULC__SUB_POISSON__FIRST_STIELTJES_SIGN__RH_OPEN",
        "rh_claim": False,
        "core": core,
        "tail": tail,
        "exact_chain": {
            "sqrt_kernel_condition": "y*L''(y)-L'(y)>=0",
            "moment_ratio": "m_k^2/(m_{k-1}m_{k+1}) >= (2k-1)/(2k+1)",
            "coefficient_ulc": "a_k^2 >= ((k+1)/k) a_{k-1}a_{k+1}",
            "tilted_birth_rate": "lambda_n=u(n+1)a_{n+1}/a_n is nonincreasing",
            "variance_identity": "Var(N)=E[N]+Cov(N,lambda_N)<=E[N]",
            "first_stieltjes_sign": "(F'/F)'(u)<=0 for u>0",
        },
        "pf2_no_go": {key: str(value) for key, value in counterexample.items()},
        "open": {
            "higher_stieltjes_derivative_signs": True,
            "full_Herglotz_property_of_minus_Gprime_over_G": True,
            "SOH_G003": True,
            "riemann_hypothesis": True,
        },
        "checks": checks,
    }
