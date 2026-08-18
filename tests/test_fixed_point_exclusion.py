from __future__ import annotations

import mpmath as mp

from secret_of_a_half.fixed_point_exclusion import (
    certified_margin,
    coarse_positive_bound,
    coarse_tail_bound,
    elementary_bound_checks,
    kernel_negative_fixed_value,
    oscillatory_tail_upper_bound,
    positive_block_lower_bound,
    quotient_negative_fixed_value,
)
from secret_of_a_half.quotient_zero_set import (
    quotient_F,
    quotient_fixed_w,
    quotient_negative_inversion_w,
)


def test_elementary_integer_bounds_are_exactly_true() -> None:
    checks = elementary_bound_checks()
    assert all(checks.values())


def test_closed_form_bounds_dominate_coarse_certificate() -> None:
    mp.mp.dps = 80
    assert positive_block_lower_bound() > coarse_positive_bound()
    assert oscillatory_tail_upper_bound() < coarse_tail_bound()
    assert certified_margin() > 0


def test_both_quotient_fixed_points_are_exact() -> None:
    plus, minus = quotient_fixed_w()
    assert quotient_negative_inversion_w(plus) == plus
    assert quotient_negative_inversion_w(minus) == minus


def test_negative_fixed_point_is_strictly_nonzero() -> None:
    mp.mp.dps = 80
    value = quotient_negative_fixed_value()
    assert abs(mp.im(value)) < mp.mpf("1e-60")
    assert mp.re(value) > certified_margin()


def test_positive_fixed_point_remains_positive() -> None:
    mp.mp.dps = 80
    assert mp.re(quotient_F(mp.mpf("0.25"))) > 0


def test_kernel_regression_matches_completed_xi() -> None:
    mp.mp.dps = 60
    direct = quotient_negative_fixed_value()
    kernel = kernel_negative_fixed_value(n_terms=10, y_cutoff=4)
    assert abs(direct - kernel) < mp.mpf("1e-35")
