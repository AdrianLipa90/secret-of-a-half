from __future__ import annotations

from fractions import Fraction

from secret_of_a_half.half_kernel_critical_exponent import (
    CRITICAL_ALPHA,
    build_receipt,
    critical_exponent_margin,
    derivative_ratio_qs,
    l2_zero_interval,
    reciprocal_deficit_data,
    r_second_over_r_direct,
    r_second_over_r_ratio_form,
)


def test_critical_alpha_is_exactly_two() -> None:
    assert CRITICAL_ALPHA == Fraction(2)
    assert critical_exponent_margin(Fraction(2)) == 0
    assert critical_exponent_margin(Fraction(3, 2)) > 0
    assert critical_exponent_margin(Fraction(5, 2)) < 0


def test_L2_zero_is_strictly_positive_with_margin() -> None:
    interval = l2_zero_interval()
    assert interval.a > 18


def test_corrected_second_stieltjes_ratio_identity() -> None:
    f0, f1, f2, f3 = Fraction(5), Fraction(3), Fraction(1), Fraction(1, 5)
    assert r_second_over_r_direct(f0, f1, f2, f3) == r_second_over_r_ratio_form(
        f0, f1, f2, f3
    )


def test_reciprocal_deficit_normal_form_exactly_matches_ratio_term() -> None:
    f0, f1, f2, f3 = Fraction(5), Fraction(3), Fraction(1), Fraction(1, 5)
    q0, q1 = derivative_ratio_qs(f0, f1, f2, f3)
    _, _, _, normalized = reciprocal_deficit_data(q0, q1)
    assert normalized == 2 - 3 * q0 + q0 * q0 * q1


def test_v07_receipt_keeps_higher_claims_open() -> None:
    receipt = build_receipt()
    assert receipt["status"] == "PASS"
    assert receipt["rh_claim"] is False
    assert receipt["open"]["higher_stieltjes_derivative_signs"] is True
    assert receipt["open"]["global_sqrt_kernel_PF3"] is True
    assert receipt["open"]["riemann_hypothesis"] is True
