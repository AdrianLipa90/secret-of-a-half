import mpmath as mp
import pytest

from secret_of_a_half.negative_inversion_zero_set import completed_xi, negative_inversion_s
from secret_of_a_half.paired_spectrum_quotient import (
    diagram_residual,
    negative_inversion_fiber_action,
    quotient_fiber,
    quotient_map_s_to_w,
    reflection_s,
)
from secret_of_a_half.quotient_zero_set import quotient_F, quotient_negative_inversion_w, w_from_xi_zero


def _close(a, b, tol="1e-45") -> bool:
    return abs(a - b) < mp.mpf(tol)


def test_q_identifies_functional_reflection_pair() -> None:
    mp.mp.dps = 60
    for s in [mp.mpc("0.3", "1.1"), mp.mpc("1.2", "-0.7"), mp.mpc("0.5", "2.3")]:
        assert _close(quotient_map_s_to_w(s), quotient_map_s_to_w(reflection_s(s)))


def test_commutative_negative_inversion_quotient_diagram() -> None:
    mp.mp.dps = 60
    for s in [mp.mpc("0.3", "1.1"), mp.mpc("1.2", "-0.7"), mp.mpc("-2.4", "0.9")]:
        assert diagram_residual(s) < mp.mpf("1e-45")
        w = quotient_map_s_to_w(s)
        assert _close(
            quotient_map_s_to_w(negative_inversion_s(s)),
            quotient_negative_inversion_w(w),
        )


def test_nonzero_quotient_fiber_has_exactly_two_distinct_points() -> None:
    mp.mp.dps = 60
    for w in [mp.mpc("0.3", "0.4"), mp.mpf("-2"), mp.mpf("0.25")]:
        s_plus, s_minus = quotient_fiber(w)
        assert not _close(s_plus, s_minus)
        assert _close(reflection_s(s_plus), s_minus)
        assert _close(quotient_map_s_to_w(s_plus), w)
        assert _close(quotient_map_s_to_w(s_minus), w)


def test_negative_inversion_maps_whole_fiber_to_J_fiber() -> None:
    mp.mp.dps = 60
    for w in [mp.mpc("0.7", "0.2"), mp.mpf("-5"), mp.mpf("0.25")]:
        source, images = negative_inversion_fiber_action(w)
        target_w = quotient_negative_inversion_w(w)
        for s in source:
            assert _close(quotient_map_s_to_w(s), w)
        for s in images:
            assert _close(quotient_map_s_to_w(s), target_w)
        assert _close(reflection_s(images[0]), images[1])


def test_first_xi_root_fibers_match_F_root_fibers() -> None:
    mp.mp.dps = 50
    for n in range(1, 4):
        rho = mp.zetazero(n)
        w = w_from_xi_zero(rho)
        s_plus, s_minus = quotient_fiber(w)
        assert abs(quotient_F(w)) < mp.mpf("1e-35")
        assert min(abs(completed_xi(s_plus)), abs(completed_xi(s_minus))) < mp.mpf("1e-35")
        assert max(abs(completed_xi(s_plus)), abs(completed_xi(s_minus))) < mp.mpf("1e-35")
        assert _close(quotient_map_s_to_w(rho), w)


def test_fixed_quotient_minus_quarter_lifts_to_g012_fixed_pair() -> None:
    mp.mp.dps = 60
    s_plus, s_minus = quotient_fiber(mp.mpf("-0.25"))
    expected = [mp.mpc("0.5", "0.5"), mp.mpc("0.5", "-0.5")]
    actual = [s_plus, s_minus]
    assert all(any(_close(a, e) for e in expected) for a in actual)
    for s in actual:
        assert _close(negative_inversion_s(s), s)


def test_fail_closed_at_branch_point_for_diagram_and_fiber_action() -> None:
    with pytest.raises(ValueError):
        diagram_residual(mp.mpf("0.5"))
    with pytest.raises(ValueError):
        negative_inversion_fiber_action(0)
