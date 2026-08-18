from fractions import Fraction

import mpmath as mp

from secret_of_a_half.fixed_root_exclusion import (
    fixed_root_lower_ratio,
    fixed_root_numeric_values,
    g004_variance_upper,
    log_phi_curvature_upper,
    safe_strong_concavity_kappa,
    second_moment_ratio_upper,
)


def test_g004_rational_constants_certify_strong_concavity_margin() -> None:
    assert g004_variance_upper() < Fraction(2, 1)
    assert log_phi_curvature_upper() < Fraction(-10, 1)
    assert safe_strong_concavity_kappa() == Fraction(10, 1)


def test_moment_and_fixed_root_bounds_are_exact_rationals() -> None:
    assert second_moment_ratio_upper() == Fraction(1, 10)
    assert fixed_root_lower_ratio() == Fraction(79, 80)
    assert fixed_root_lower_ratio() > 0


def test_numeric_fixed_root_value_respects_analytic_lower_bound() -> None:
    mp.mp.dps = 60
    values = fixed_root_numeric_values(60)
    f0 = values["F0"]
    fm = values["F_minus_quarter"]
    ratio = values["ratio"]
    assert abs(mp.im(f0)) < mp.mpf("1e-50")
    assert abs(mp.im(fm)) < mp.mpf("1e-50")
    assert mp.re(f0) > 0
    assert mp.re(fm) > 0
    assert mp.re(ratio) > mp.mpf(79) / 80


def test_g012_negative_inversion_fixed_pair_is_not_xi_zero_numerically() -> None:
    mp.mp.dps = 60
    values = fixed_root_numeric_values(60)
    xi_value = values["xi_half_plus_i_half"]
    assert abs(xi_value) > mp.mpf("0.49")
