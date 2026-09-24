from __future__ import annotations

from fractions import Fraction

import mpmath as mp

from secret_of_a_half.second_stieltjes_global import (
    _shift_polynomial,
    analytic_moment_tail_upper,
    analytic_z_tail_certificate,
    second_stieltjes_numerator,
)


def test_correct_second_stieltjes_numerator_identity_fixture() -> None:
    assert second_stieltjes_numerator(
        Fraction(5), Fraction(3), Fraction(1), Fraction(1, 5)
    ) == Fraction(14)


def test_analytic_moment_tail_is_tiny() -> None:
    assert analytic_moment_tail_upper() < mp.mpf("1e-40")


def test_tail_baseline_shift_polynomial_is_positive() -> None:
    coefficients = [13, 26, -636, -568, -7056, -2336, -3392, 384]
    shifted = _shift_polynomial(coefficients, 11)
    assert shifted == [
        993584055,
        1275452842,
        517546988,
        103342408,
        11596624,
        749536,
        26176,
        384,
    ]
    assert all(value > 0 for value in shifted)


def test_analytic_z_tail_closes_with_margin() -> None:
    tail = analytic_z_tail_certificate()
    assert mp.mpf(tail["q_total_lower_at_11"]) > mp.mpf("0.09")
