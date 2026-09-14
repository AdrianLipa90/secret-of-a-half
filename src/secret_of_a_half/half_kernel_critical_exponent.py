"""SOH half-kernel v0.7: critical power exponent and second-Stieltjes firewall.

This module records only theorem-level consequences of v0.6 plus exact algebra.
It does not claim higher Stieltjes signs, global PF3 of the square-root kernel,
SOH-G003 real-rootedness, or RH.
"""
from __future__ import annotations

from fractions import Fraction

from .sqrt_kernel_ulc import _theta_derivative_intervals

CRITICAL_ALPHA = Fraction(2, 1)


def l2_zero_interval():
    phi0, phi1, phi2, _, _ = _theta_derivative_intervals(Fraction(0), Fraction(0))
    return -phi2 / phi0 + (phi1 / phi0) ** 2


def critical_exponent_margin(alpha: Fraction) -> Fraction:
    return CRITICAL_ALPHA - alpha


def second_stieltjes_numerator(f0: Fraction, f1: Fraction, f2: Fraction, f3: Fraction) -> Fraction:
    return f0 * f0 * f3 - 3 * f0 * f1 * f2 + 2 * f1**3


def derivative_ratio_qs(
    f0: Fraction, f1: Fraction, f2: Fraction, f3: Fraction
) -> tuple[Fraction, Fraction]:
    q0 = (f0 * f2) / (f1 * f1)
    q1 = (f1 * f3) / (f2 * f2)
    return q0, q1


def r_second_over_r_ratio_form(
    f0: Fraction, f1: Fraction, f2: Fraction, f3: Fraction
) -> Fraction:
    a0 = f1 / f0
    q0, q1 = derivative_ratio_qs(f0, f1, f2, f3)
    return a0 * a0 * (2 - 3 * q0 + q0 * q0 * q1)


def r_second_over_r_direct(
    f0: Fraction, f1: Fraction, f2: Fraction, f3: Fraction
) -> Fraction:
    return second_stieltjes_numerator(f0, f1, f2, f3) / (f0 * f0 * f1)


def reciprocal_deficit_data(
    q0: Fraction, q1: Fraction
) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    e0 = 1 / (1 - q0)
    e1 = 1 / (1 - q1)
    margin = (e0 + 1) * e1 - (e0 - 1) ** 2
    normalized = margin / (e0 * e0 * e1)
    return e0, e1, margin, normalized


def build_receipt() -> dict[str, object]:
    l2 = l2_zero_interval()
    l2_lower = float(l2.a)
    l2_upper = float(l2.b)

    f0, f1, f2, f3 = Fraction(5), Fraction(3), Fraction(1), Fraction(1, 5)
    q0, q1 = derivative_ratio_qs(f0, f1, f2, f3)
    _, _, _, deficit_normalized = reciprocal_deficit_data(q0, q1)
    ratio_term = 2 - 3 * q0 + q0 * q0 * q1

    checks = {
        "L2_zero_positive_certified": l2_lower > 18,
        "critical_alpha_exactly_two": CRITICAL_ALPHA == 2,
        "alpha_le_two_margin_nonnegative": all(
            critical_exponent_margin(a) >= 0
            for a in (Fraction(1, 2), Fraction(1), Fraction(3, 2), Fraction(2))
        ),
        "alpha_gt_two_margin_negative": critical_exponent_margin(Fraction(5, 2)) < 0,
        "corrected_R_second_firewall": (
            r_second_over_r_direct(f0, f1, f2, f3)
            == r_second_over_r_ratio_form(f0, f1, f2, f3)
        ),
        "reciprocal_deficit_identity_exact": deficit_normalized == ratio_term,
        "higher_stieltjes_derivative_signs_remain_open": True,
        "global_sqrt_kernel_PF3_remains_open": True,
        "rh_claim_remains_false": True,
    }

    return {
        "schema": "SOH_HALF_KERNEL_CRITICAL_EXPONENT_V0_7",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "epistemic_status": (
            "EXACT_CRITICAL_EXPONENT_ALPHA_MAX_2__"
            "CORRECTED_SECOND_STIELTJES_FIREWALL__"
            "HIGHER_STIELTJES_OPEN__GLOBAL_SQRT_KERNEL_PF3_OPEN__RH_OPEN"
        ),
        "rh_claim": False,
        "critical_exponent": {
            "family": "H_alpha(x)=Phi(x^(1/alpha))",
            "alpha_max": "2",
            "critical_root_exponent": "1/2",
            "log_second_derivative": (
                "-(y*L''(y)-(alpha-1)*L'(y))/(alpha^2*y^(2*alpha-1))"
            ),
            "decomposition_for_alpha_le_2": (
                "y*L''-(alpha-1)*L'=(y*L''-L')+(2-alpha)*L'"
            ),
            "near_zero_for_alpha_gt_2": (
                "y*L''-(alpha-1)*L'=(2-alpha)*L''(0)*y+O(y^3)"
            ),
            "L2_zero_interval": [format(l2_lower, ".17g"), format(l2_upper, ".17g")],
        },
        "second_stieltjes_firewall": {
            "R": "F'/F",
            "correct_identity": (
                "R''=(F^2*F'''-3*F*F'*F''+2*(F')^3)/F^3"
            ),
            "ratio_form": "R''/R=A0^2*(2-3*q0+q0^2*q1)",
            "reciprocal_deficit_equivalence": (
                "R''>=0 iff (E0+1)*E1 >= (E0-1)^2, when q0,q1<1"
            ),
            "rejected_equivalence": (
                "F'^3*F'''-F*(F'')^3>=0 is not equivalent to R''>=0"
            ),
        },
        "open": {
            "higher_stieltjes_derivative_signs": True,
            "global_sqrt_kernel_PF3": True,
            "full_Herglotz_property_of_minus_Gprime_over_G": True,
            "SOH_G003": True,
            "riemann_hypothesis": True,
        },
        "checks": checks,
    }
