import mpmath as mp
import pytest

from secret_of_a_half.euler_crossings import (
    centered_t_from_u,
    complex_scale_defect,
    crossing_quotient_argument,
    euler_half_turn,
    euler_half_turn_centered_inversion,
    forced_u_crossings,
    log_scale_defect,
    logarithmic_crossing,
    logarithmic_reflection,
    numerical_log_crossing_derivative,
    xi_u_complex,
)


def test_forced_u_crossing_pair_for_32() -> None:
    mp.mp.dps = 60
    plus, minus = forced_u_crossings(32)
    assert plus == 1 / mp.sqrt(32)
    assert minus == -plus
    assert abs(complex_scale_defect(plus, 32)) < mp.mpf("1e-45")
    assert abs(complex_scale_defect(minus, 32)) < mp.mpf("1e-45")


@pytest.mark.parametrize("a", [2, 3, 32])
def test_logarithmic_forced_family_vanishes(a: int) -> None:
    mp.mp.dps = 60
    for k in range(-3, 4):
        lam = logarithmic_crossing(a, k)
        assert abs(log_scale_defect(lam, a)) < mp.mpf("1e-44")


def test_log_scale_defect_antisymmetry() -> None:
    mp.mp.dps = 60
    a = mp.mpf(32)
    lam = mp.mpc("0.271", "0.413")
    reflected = logarithmic_reflection(lam, a)
    residual = log_scale_defect(reflected, a) + log_scale_defect(lam, a)
    assert abs(residual) < mp.mpf("1e-45")


def test_log_scale_defect_two_pi_i_periodicity() -> None:
    mp.mp.dps = 60
    a = mp.mpf(32)
    lam = mp.mpc("-0.37", "0.22")
    residual = log_scale_defect(lam + 2 * mp.pi * mp.j, a) - log_scale_defect(lam, a)
    assert abs(residual) < mp.mpf("1e-45")


def test_euler_half_turn_exchanges_forced_classes() -> None:
    mp.mp.dps = 60
    a = mp.mpf(32)
    for k in range(-2, 3):
        u0 = mp.exp(logarithmic_crossing(a, k))
        u1 = mp.exp(logarithmic_crossing(a, k + 1))
        assert abs(u1 - euler_half_turn(u0)) < mp.mpf("1e-50")
        assert abs(u1 + u0) < mp.mpf("1e-50")


def test_euler_half_turn_is_centered_reciprocal_inversion() -> None:
    mp.mp.dps = 60
    samples = [
        mp.mpc("0.3", "0.7"),
        mp.mpc("2.0", "0.4"),
        mp.mpc("-0.4", "0.6"),
    ]
    for u in samples:
        t = centered_t_from_u(u)
        image = euler_half_turn_centered_inversion(u)
        assert abs(image - 1 / t) < mp.mpf("1e-50")


def test_log_half_period_is_t_inversion() -> None:
    mp.mp.dps = 60
    lam = mp.mpc("0.47", "0.31")
    t0 = mp.tanh(lam / 2)
    t1 = mp.tanh((lam + mp.pi * mp.j) / 2)
    assert abs(t1 - 1 / t0) < mp.mpf("1e-50")


def test_crossing_quotient_arguments_are_positive() -> None:
    mp.mp.dps = 60
    for a in [2, 3, 32]:
        w_even = crossing_quotient_argument(a, 0)
        w_odd = crossing_quotient_argument(a, 1)
        assert w_even > 0
        assert w_odd > 0
        assert w_even < mp.mpf("0.25")
        assert w_odd > mp.mpf("0.25")


def test_forced_crossings_are_numerically_simple() -> None:
    mp.mp.dps = 60
    for k in [0, 1]:
        derivative = numerical_log_crossing_derivative(32, k)
        assert abs(derivative) > mp.mpf("1e-30")


def test_complex_domain_fails_closed_at_mobius_poles() -> None:
    with pytest.raises(ValueError):
        xi_u_complex(-1)
    with pytest.raises(ValueError):
        complex_scale_defect(-1, 32)
    with pytest.raises(ValueError):
        complex_scale_defect(mp.mpf(-1) / 32, 32)
    with pytest.raises(ValueError):
        euler_half_turn_centered_inversion(1)


def test_invalid_scale_rejected() -> None:
    for bad in [1, 0, -2, mp.inf]:
        with pytest.raises(ValueError):
            forced_u_crossings(bad)
