import math
import mpmath as mp
import pytest

from secret_of_a_half.scale_defect import (
    quotient_argument_from_lambda,
    scale_defect,
    scale_defect_crossing,
    scale_defect_sign_region,
    xi_log_coordinate,
)


def test_quotient_argument_is_even_and_strict_in_abs_lambda() -> None:
    vals = [0.0, 0.2, 0.8, 1.7]
    ws = [quotient_argument_from_lambda(v) for v in vals]
    assert ws == sorted(ws)
    for v in vals:
        assert quotient_argument_from_lambda(v) == pytest.approx(quotient_argument_from_lambda(-v))


def test_xi_log_coordinate_is_even_numerically() -> None:
    mp.mp.dps = 50
    for v in [0.2, 0.7, 1.4]:
        assert abs(xi_log_coordinate(v) - xi_log_coordinate(-v)) < mp.mpf('1e-40')


def test_unique_scale_defect_crossing_for_32() -> None:
    mp.mp.dps = 50
    a = 32.0
    c = scale_defect_crossing(a)
    assert c == pytest.approx(1 / math.sqrt(32.0))
    assert abs(scale_defect(c, a)) < mp.mpf('1e-35')
    assert scale_defect(0.05, a) < 0
    assert scale_defect(0.5, a) > 0


def test_sign_classifier_matches_numerical_defect() -> None:
    mp.mp.dps = 50
    for a in [2.0, 3.0, 32.0]:
        c = scale_defect_crossing(a)
        for u in [c / 4, c / 2, c * 2, c * 4]:
            observed = -1 if scale_defect(u, a) < 0 else 1
            assert observed == scale_defect_sign_region(u, a)
        assert scale_defect_sign_region(c, a) == 0


@pytest.mark.parametrize('u,a', [(0,2),(-1,2),(1,1),(1,0.5)])
def test_fail_closed(u,a) -> None:
    with pytest.raises(ValueError):
        scale_defect_sign_region(u,a)
