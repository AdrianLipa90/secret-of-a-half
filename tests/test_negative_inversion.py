import mpmath as mp
import pytest

from secret_of_a_half.negative_inversion import (
    centered_t_from_u,
    euler_half_turn_t,
    euler_half_turn_u,
    euler_half_turn_w,
    euler_half_turn_z,
    functional_reflection_s,
    li_coordinate,
    li_coordinate_via_negative_inversion,
    log_negative_inversion,
    log_negative_inversion_fixed,
    negative_inversion_fixed_s,
    negative_inversion_fixed_u,
    negative_inversion_fixed_z,
    negative_inversion_t,
    negative_inversion_u,
    negative_inversion_w,
    negative_inversion_z,
    quotient_fixed_w,
    riemann_reflection_t,
    riemann_reflection_u,
    riemann_reflection_w,
    riemann_reflection_z,
    s_from_u,
    u_from_s,
)


def _close(a, b, tol="1e-50") -> bool:
    return abs(a - b) < mp.mpf(tol)


def test_v4_operator_algebra_in_u() -> None:
    mp.mp.dps = 70
    samples = [mp.mpc("0.7", "0.4"), mp.mpc("-0.3", "1.2"), mp.mpc("2.1", "-0.8")]
    for u in samples:
        r = riemann_reflection_u
        e = euler_half_turn_u
        n = negative_inversion_u
        assert _close(r(r(u)), u)
        assert _close(e(e(u)), u)
        assert _close(n(n(u)), u)
        assert _close(r(e(u)), n(u))
        assert _close(e(r(u)), n(u))
        assert _close(r(e(u)), e(r(u)))


def test_functional_reflection_and_li_negative_inverse_crosswalk() -> None:
    mp.mp.dps = 70
    samples = [mp.mpc("0.31", "0.27"), mp.mpc("0.62", "-0.41"), mp.mpc("1.3", "0.2")]
    for s in samples:
        u = u_from_s(s)
        reflected_u = u_from_s(functional_reflection_s(s))
        assert _close(reflected_u, riemann_reflection_u(u))
        assert _close(li_coordinate(s), -1 / u)
        assert _close(li_coordinate(s), negative_inversion_u(u))
        assert _close(li_coordinate(s), li_coordinate_via_negative_inversion(s))


def test_coordinate_conjugacy_u_to_t() -> None:
    mp.mp.dps = 70
    for u in [mp.mpc("0.8", "0.2"), mp.mpc("1.7", "-0.9"), mp.j]:
        t = centered_t_from_u(u)
        assert _close(centered_t_from_u(riemann_reflection_u(u)), riemann_reflection_t(t))
        assert _close(centered_t_from_u(euler_half_turn_u(u)), euler_half_turn_t(t))
        assert _close(centered_t_from_u(negative_inversion_u(u)), negative_inversion_t(t))


def test_negative_inversion_z_and_w_diagram() -> None:
    mp.mp.dps = 70
    for z in [mp.mpc("0.31", "0.27"), mp.mpc("-0.42", "0.18"), mp.mpc("0.7", "-0.3")]:
        w = z * z
        assert _close(negative_inversion_z(z), riemann_reflection_z(euler_half_turn_z(z)))
        assert _close(negative_inversion_z(z), euler_half_turn_z(riemann_reflection_z(z)))
        assert _close(negative_inversion_z(z) ** 2, negative_inversion_w(w))
        assert _close(euler_half_turn_z(z) ** 2, euler_half_turn_w(w))
        assert _close(riemann_reflection_z(z) ** 2, riemann_reflection_w(w))
        assert _close(negative_inversion_w(w), euler_half_turn_w(w))


def test_negative_inversion_fixed_pair_is_on_critical_line() -> None:
    mp.mp.dps = 70
    us = negative_inversion_fixed_u()
    ss = negative_inversion_fixed_s()
    zs = negative_inversion_fixed_z()
    for u, s, z in zip(us, ss, zs):
        assert _close(negative_inversion_u(u), u)
        assert _close(s_from_u(u), s)
        assert _close(mp.re(s), mp.mpf("0.5"))
        assert _close(s - mp.mpf("0.5"), z)
        assert _close(negative_inversion_z(z), z)
        assert _close(z * z, mp.mpf("-0.25"))


def test_euler_phase_generates_negative_inversion_fixed_condition() -> None:
    mp.mp.dps = 70
    for u in negative_inversion_fixed_u():
        assert _close(u * u, mp.e ** (mp.j * mp.pi))
        assert _close(u * u, -1)


def test_log_cylinder_negative_inversion_and_fixed_lifts() -> None:
    mp.mp.dps = 70
    lam = mp.mpc("0.27", "0.41")
    transformed = log_negative_inversion(lam)
    assert _close(mp.exp(transformed), negative_inversion_u(mp.exp(lam)))
    for k in range(-3, 4):
        fixed = log_negative_inversion_fixed(k)
        # Fixed modulo the full logarithmic period 2*pi*i.
        residual = log_negative_inversion(fixed) - fixed
        assert _close(mp.exp(residual), 1)
        assert _close(negative_inversion_u(mp.exp(fixed)), mp.exp(fixed))


def test_w_quotient_has_two_fixed_values_with_distinct_origins() -> None:
    mp.mp.dps = 70
    plus, minus = quotient_fixed_w()
    assert _close(negative_inversion_w(plus), plus)
    assert _close(negative_inversion_w(minus), minus)

    # w=-1/4 is the image of genuine N_z fixed points z=+/- i/2.
    for z in negative_inversion_fixed_z():
        assert _close(z * z, minus)
        assert _close(negative_inversion_z(z), z)

    # w=+1/4 is fixed only after the z -> z^2 quotient: N_z swaps +/-1/2.
    z_plus = mp.mpf("0.5")
    z_minus = mp.mpf("-0.5")
    assert _close(negative_inversion_z(z_plus), z_minus)
    assert _close(negative_inversion_z(z_minus), z_plus)
    assert _close(z_plus * z_plus, plus)
    assert _close(z_minus * z_minus, plus)


def test_fail_closed_singularities() -> None:
    with pytest.raises(ValueError):
        li_coordinate(0)
    with pytest.raises(ValueError):
        li_coordinate_via_negative_inversion(0)
    with pytest.raises(ValueError):
        li_coordinate_via_negative_inversion(1)
    with pytest.raises(ValueError):
        riemann_reflection_u(0)
    with pytest.raises(ValueError):
        negative_inversion_u(0)
    with pytest.raises(ValueError):
        euler_half_turn_t(0)
    with pytest.raises(ValueError):
        negative_inversion_t(0)
    with pytest.raises(ValueError):
        euler_half_turn_z(0)
    with pytest.raises(ValueError):
        negative_inversion_z(0)
    with pytest.raises(ValueError):
        negative_inversion_w(0)
