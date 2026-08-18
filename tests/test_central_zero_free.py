import mpmath as mp
import pytest

from secret_of_a_half.central_zero_free import (
    F_on_negative_axis_from_t,
    central_radius,
    central_radius_squared,
    normalized_lower_bound,
    xi_on_critical_line,
)
from secret_of_a_half.quotient_zero_set import quotient_F


def test_exact_safe_radius_squared() -> None:
    assert central_radius_squared() == 20


def test_normalized_lower_bound_on_interval() -> None:
    mp.mp.dps = 60
    r = central_radius()
    for t in [0, 1, 2, 4, r]:
        assert normalized_lower_bound(t) >= 0
    assert abs(normalized_lower_bound(r)) < mp.mpf("1e-55")


def test_xi_and_F_negative_axis_agree() -> None:
    mp.mp.dps = 60
    for t in [mp.mpf("0"), mp.mpf("0.5"), mp.mpf("2"), mp.sqrt(20)]:
        assert abs(xi_on_critical_line(t) - F_on_negative_axis_from_t(t)) < mp.mpf("1e-45")


def test_numeric_critical_line_values_are_positive_through_safe_endpoint() -> None:
    mp.mp.dps = 60
    for t in [0, 1, 2, 3, 4, mp.sqrt(20)]:
        value = xi_on_critical_line(t)
        assert abs(mp.im(value)) < mp.mpf("1e-45")
        assert mp.re(value) > 0


def test_F_is_positive_on_sampled_real_points_from_minus_20_upwards() -> None:
    mp.mp.dps = 60
    for w in [-20, -10, -1, 0, 1, 10]:
        value = quotient_F(w)
        assert abs(mp.im(value)) < mp.mpf("1e-45")
        assert mp.re(value) > 0


def test_fail_closed_for_nonreal_t() -> None:
    with pytest.raises(ValueError):
        normalized_lower_bound(1 + 1j)
    with pytest.raises(ValueError):
        xi_on_critical_line(1 + 1j)
