import mpmath as mp

from secret_of_a_half.g024_nbody_laguerre_hierarchy import (
    extended_laguerre_value,
    finite_real_zero_q_coefficients,
    jensen_from_laguerre_coefficients,
    quartic_first_gate_exact,
    quartic_non_lp,
    real_axis_first_gate_matches_jensen,
    real_zero_pair_q_factor,
    real_zero_product_function,
    transverse_partition_q,
    transverse_q_coefficient,
    transverse_q_coefficients,
    xi_transverse_q_coefficients,
)
from secret_of_a_half.theta_nbody_rigidity import hermitian_jensen_value


def test_q_coefficient_is_half_extended_laguerre_and_l1_is_jensen_on_real_axis():
    mp.mp.dps = 60
    f = real_zero_product_function([1, 2, mp.mpf("3.5")])
    x = mp.mpf("0.7")
    for n in range(5):
        assert mp.almosteq(
            2 * transverse_q_coefficient(f, x, n),
            extended_laguerre_value(f, x, n),
            rel_eps=mp.mpf("1e-52"),
            abs_eps=mp.mpf("1e-55"),
        )
    assert abs(real_axis_first_gate_matches_jensen(f, x)) < mp.mpf("1e-50")


def test_real_zero_pair_q_factor_is_nonnegative():
    mp.mp.dps = 60
    for x in [mp.mpf("0"), mp.mpf("1"), mp.mpf("1.25"), mp.mpf("4")]:
        coeffs = real_zero_pair_q_factor(mp.mpf("1.25"), x)
        assert all(c >= 0 for c in coeffs)


def test_real_zero_product_derivative_coefficients_equal_positive_factor_convolution():
    mp.mp.dps = 60
    gammas = [mp.mpf("1"), mp.mpf("2"), mp.mpf("3.5")]
    f = real_zero_product_function(gammas)
    for x in [mp.mpf("0.7"), mp.mpf("1"), mp.mpf("2.4")]:
        direct = transverse_q_coefficients(f, x, 2 * len(gammas))
        factorized = finite_real_zero_q_coefficients(gammas, x)
        assert len(direct) == len(factorized)
        for a, b in zip(direct, factorized):
            assert mp.almosteq(a, b, rel_eps=mp.mpf("1e-45"), abs_eps=mp.mpf("1e-50"))
            assert a >= -mp.mpf("1e-50")


def test_finite_real_zero_hierarchy_generates_full_hermitian_jensen_curvature():
    mp.mp.dps = 60
    gammas = [mp.mpf("1"), mp.mpf("2")]
    f = real_zero_product_function(gammas)
    x = mp.mpf("0.63")
    y = mp.mpf("0.27")
    # Degree four in z gives Q_x degree four in q, so n=0..4 is exact.
    laguerre = [extended_laguerre_value(f, x, n) for n in range(5)]
    from_hierarchy = jensen_from_laguerre_coefficients(laguerre, y)
    direct = hermitian_jensen_value(f, mp.mpc(x, y))
    assert mp.almosteq(from_hierarchy, direct, rel_eps=mp.mpf("1e-48"), abs_eps=mp.mpf("1e-52"))


def test_non_lp_quartic_fails_first_q_cone_gate():
    mp.mp.dps = 60
    x = mp.mpf("1")
    c1 = transverse_q_coefficient(quartic_non_lp, x, 1)
    exact = quartic_first_gate_exact(x)
    assert mp.almosteq(c1, exact, rel_eps=mp.mpf("1e-55"), abs_eps=mp.mpf("1e-58"))
    assert c1 == -4


def test_q_partition_is_generated_by_coefficients_for_finite_real_zero_control():
    mp.mp.dps = 60
    gammas = [mp.mpf("1"), mp.mpf("2")]
    f = real_zero_product_function(gammas)
    x = mp.mpf("0.3")
    q = mp.mpf("0.41")
    coeffs = finite_real_zero_q_coefficients(gammas, x)
    series = sum(c * q**n for n, c in enumerate(coeffs))
    direct = transverse_partition_q(f, x, q)
    assert mp.almosteq(series, direct, rel_eps=mp.mpf("1e-50"), abs_eps=mp.mpf("1e-55"))


def test_xi_q_cone_low_order_samples_are_positive_diagnostic_only():
    mp.mp.dps = 60
    for x in [mp.mpf("0"), mp.mpf("10"), mp.mpf("14.134725141734693790")]:
        coeffs = xi_transverse_q_coefficients(x, 4)
        assert all(c >= 0 for c in coeffs)
