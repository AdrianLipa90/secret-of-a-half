import mpmath as mp

from secret_of_a_half.g024_achilles_radial_gate import (
    complex_laguerre_I,
    gaussian_control,
    hermitian_from_q,
    hermitian_jensen,
    off_axis_control,
    q_laplacian_residual,
    q_partition,
    radial_response,
    touchdown_leading_coefficient,
)


def test_q_partition_off_axis_control_is_exact_touchdown():
    mp.mp.dps = 60
    for q in [mp.mpf("0"), mp.mpf("0.1"), mp.mpf("0.5"), mp.mpf("1"), mp.mpf("1.3")]:
        observed = q_partition(off_axis_control, 0, q)
        expected = mp.mpf("0.5") * (1 - q) ** 2
        assert mp.almosteq(observed, expected, rel_eps=mp.mpf("1e-55"), abs_eps=mp.mpf("1e-58"))


def test_radial_response_matches_complex_laguerre_I():
    mp.mp.dps = 60
    x = mp.mpf("0.7")
    y = mp.mpf("0.3")
    q = y * y
    lhs = 2 * radial_response(gaussian_control, x, q)
    rhs = complex_laguerre_I(gaussian_control, x, y)
    assert mp.almosteq(lhs, rhs, rel_eps=mp.mpf("1e-50"), abs_eps=mp.mpf("1e-55"))


def test_off_axis_zero_forces_radial_descent_control():
    mp.mp.dps = 50
    # f(z)=z^2+1 has q-touchdown Q_0(q)=1/2(1-q)^2 at q0=1.
    assert radial_response(off_axis_control, 0, mp.mpf("0.25")) == mp.mpf("-0.75")
    assert mp.almosteq(
        radial_response(off_axis_control, 0, mp.mpf("0.9")),
        mp.mpf("-0.1"),
        rel_eps=mp.mpf("1e-45"),
        abs_eps=mp.mpf("1e-48"),
    )
    assert q_partition(off_axis_control, 0, 1) == 0


def test_touchdown_leading_coefficient_for_simple_zero():
    mp.mp.dps = 60
    # At z0=i the zero is simple and Q_0(q)=1/2(q-1)^2.
    coeff = touchdown_leading_coefficient(off_axis_control, 0, 1, 1)
    assert mp.almosteq(coeff, mp.mpf("0.5"), rel_eps=mp.mpf("1e-55"), abs_eps=mp.mpf("1e-58"))


def test_hermitian_q_identity():
    mp.mp.dps = 55
    x = mp.mpf("0.4")
    q = mp.mpf("0.36")
    lhs = hermitian_from_q(off_axis_control, x, q)
    rhs = hermitian_jensen(off_axis_control, x, mp.sqrt(q))
    assert mp.almosteq(lhs, rhs, rel_eps=mp.mpf("1e-45"), abs_eps=mp.mpf("1e-50"))


def test_q_laplacian_identity():
    mp.mp.dps = 50
    residual = q_laplacian_residual(gaussian_control, mp.mpf("0.8"), mp.mpf("0.16"))
    assert abs(residual) < mp.mpf("1e-40")


def test_gaussian_lp_control_has_nonnegative_radial_response():
    mp.mp.dps = 50
    for x in [mp.mpf("0"), mp.mpf("1"), mp.mpf("3")]:
        for q in [mp.mpf("0"), mp.mpf("0.01"), mp.mpf("0.1"), mp.mpf("0.24")]:
            assert radial_response(gaussian_control, x, q) >= 0
