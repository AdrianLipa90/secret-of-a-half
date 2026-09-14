from __future__ import annotations

from fractions import Fraction

from secret_of_a_half.sqrt_kernel_ulc import (
    analytic_tail_certificate,
    coefficient_ulc_factor,
    log_rho_third_abs_bound,
    pf2_first_stieltjes_counterexample,
    ulc_moment_ratio_lower,
)


def test_exact_ulc_factors() -> None:
    assert ulc_moment_ratio_lower(1) == Fraction(1, 3)
    assert ulc_moment_ratio_lower(2) == Fraction(3, 5)
    assert coefficient_ulc_factor(1) == Fraction(2, 1)
    assert coefficient_ulc_factor(2) == Fraction(3, 2)


def test_analytic_tail_closes_strictly() -> None:
    tail = analytic_tail_certificate()
    assert tail["L3_lower"] == "38"
    assert log_rho_third_abs_bound() < 2


def test_pf2_alone_does_not_force_first_stieltjes_sign() -> None:
    witness = pf2_first_stieltjes_counterexample()
    assert witness["pf2_margin"] >= 0
    assert witness["log_derivative_derivative_at_zero"] == Fraction(1, 2)
