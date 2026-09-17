import mpmath as mp

from secret_of_a_half.g024_relative_moment_structure import (
    extended_laguerre_value,
    gaussian_B_fourier_2x,
    gaussian_fourier,
    gaussian_relative_moment,
    oscillatory_gaussian_fourier_scaled,
    oscillatory_gaussian_l2_witness,
    oscillatory_gaussian_log_curvature_margin,
    radial_first_gate_bound,
    scaled_laguerre_prediction,
    strong_marginal_curvature_bound,
)


def test_gaussian_marginal_strong_curvature_saturates_bound():
    mp.mp.dps = 50
    a = mp.mpf("1.5")
    kappa = 2 * a
    assert strong_marginal_curvature_bound(kappa) == 4 * a
    assert radial_first_gate_bound(kappa) == kappa


def test_gaussian_relative_moments_form_hankel_positive_sequence():
    mp.mp.dps = 50
    a, u = mp.mpf("1.5"), mp.mpf("0.4")
    c0 = gaussian_relative_moment(a, u, 0)
    c1 = gaussian_relative_moment(a, u, 1)
    c2 = gaussian_relative_moment(a, u, 2)
    assert c0 > 0 and c1 > 0 and c2 > 0
    assert c0 * c2 - c1 * c1 > 0


def test_gaussian_generating_fourier_is_half_modulus_square():
    mp.mp.dps = 60
    a, x, y = mp.mpf("1.3"), mp.mpf("0.7"), mp.mpf("0.2")
    lhs = gaussian_B_fourier_2x(a, x, y)
    rhs = mp.mpf("0.5") * abs(gaussian_fourier(a, mp.mpc(x, y))) ** 2
    assert mp.almosteq(lhs, rhs, rel_eps=mp.mpf("1e-55"))


def test_oscillatory_gaussian_is_stronger_than_riemann_curvature_margin():
    mp.mp.dps = 50
    margin = oscillatory_gaussian_log_curvature_margin()
    assert mp.almosteq(margin, 16)
    assert margin > 10


def test_strong_log_concavity_does_not_force_second_laguerre_gate():
    mp.mp.dps = 70
    base, scaled_x, scaled = oscillatory_gaussian_l2_witness()
    assert base < 0
    assert scaled < 0
    assert mp.almosteq(scaled_x, mp.mpf("48.88"))
    assert mp.almosteq(
        scaled,
        scaled_laguerre_prediction(base, 40, 2),
        rel_eps=mp.mpf("1e-55"),
        abs_eps=mp.mpf("1e-65"),
    )


def test_scaled_control_negative_gate_recomputed_directly():
    mp.mp.dps = 60
    f = lambda z: oscillatory_gaussian_fourier_scaled(z)
    value = extended_laguerre_value(f, mp.mpf("48.88"), 2)
    assert value < 0
    assert mp.almosteq(
        value,
        mp.mpf("-2.2386691430209876197666034779115969455534550379336e-10"),
        rel_eps=mp.mpf("1e-45"),
    )
