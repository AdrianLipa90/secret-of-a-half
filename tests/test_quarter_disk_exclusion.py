from __future__ import annotations

from fractions import Fraction

import mpmath as mp

from secret_of_a_half.quarter_disk_exclusion import (
    QUARTER,
    XI_HALF_LOWER,
    ZERO_FREE_MARGIN,
    boundary_regression,
    exact_certificate_checks,
    inversion_modulus,
    maps_root_modulus_into_zero_free_disk,
    positive_boundary_numeric,
    xi_half_numeric,
    xi_half_rational_lower_bound,
    zero_free_margin_lower_bound,
)


def test_exact_rational_certificate_checks_are_true() -> None:
    assert all(exact_certificate_checks().values())
    assert xi_half_rational_lower_bound() == XI_HALF_LOWER
    assert zero_free_margin_lower_bound() == ZERO_FREE_MARGIN


def test_xi_half_lower_bound_strictly_exceeds_quarter() -> None:
    assert XI_HALF_LOWER == Fraction(54723, 203125)
    assert XI_HALF_LOWER > QUARTER


def test_zero_free_margin_is_exactly_positive() -> None:
    assert ZERO_FREE_MARGIN == Fraction(15767, 406250)
    assert ZERO_FREE_MARGIN > 0


def test_numeric_xi_half_dominates_rational_certificate() -> None:
    mp.mp.dps = 80
    value = xi_half_numeric()
    assert abs(mp.im(value)) < mp.mpf("1e-70")
    assert mp.re(value) > mp.mpf(XI_HALF_LOWER.numerator) / XI_HALF_LOWER.denominator


def test_positive_boundary_is_one_half() -> None:
    mp.mp.dps = 80
    value = positive_boundary_numeric()
    assert abs(mp.im(value)) < mp.mpf("1e-70")
    assert abs(mp.re(value) - mp.mpf("0.5")) < mp.mpf("1e-60")


def test_negative_inversion_sends_every_root_radius_inside_quarter_disk() -> None:
    mp.mp.dps = 50
    for radius in [mp.mpf("0.2500001"), mp.mpf("1"), mp.mpf("100")]:
        assert inversion_modulus(radius) < mp.mpf("0.25")
        assert maps_root_modulus_into_zero_free_disk(radius)


def test_boundary_sampling_stays_above_proved_margin() -> None:
    mp.mp.dps = 60
    sampled = boundary_regression(samples=32)
    margin = mp.mpf(ZERO_FREE_MARGIN.numerator) / ZERO_FREE_MARGIN.denominator
    assert sampled > margin
