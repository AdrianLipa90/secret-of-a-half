import mpmath as mp

from secret_of_a_half.g024_hermitian_correction import (
    dyadic_external_and_hermitian_witness,
    gaussian_fourier_entire,
    odd_tilt_fourier_from_entire,
    riemann_relative_susceptibility,
    tent_internal_jensen_transform,
    theta_partition_identity_residual,
    wick_rotated_partition,
    wick_rotated_relative_susceptibility,
)
from secret_of_a_half.theta_nbody_rigidity import (
    hermitian_jensen_value,
    tent_transform,
    xi_fourier_entire,
)


def test_odd_tilt_fourier_has_required_i_factor():
    mp.mp.dps = 60
    x = mp.mpf("1.7")
    y = mp.mpf("0.4")
    z = mp.mpc(x, y)
    odd = odd_tilt_fourier_from_entire(gaussian_fourier_entire, x, y)
    expected = 1j * mp.im(gaussian_fourier_entire(z))
    assert mp.almosteq(odd, expected, rel_eps=mp.mpf("1e-55"), abs_eps=mp.mpf("1e-58"))
    assert abs(mp.re(odd)) < mp.mpf("1e-58")


def test_direct_internal_tent_kernel_is_hermitian_jensen():
    mp.mp.dps = 30
    x, y = mp.pi, mp.mpf("0.1")
    direct = tent_internal_jensen_transform(x, y)
    hermitian = hermitian_jensen_value(tent_transform, mp.mpc(x, y))
    assert mp.almosteq(direct, hermitian, rel_eps=mp.mpf("1e-22"), abs_eps=mp.mpf("1e-25"))


def test_wick_rotated_partition_is_half_modulus_square():
    mp.mp.dps = 60
    x = mp.mpf("3.2")
    y = mp.mpf("0.21")
    z = mp.mpc(x, y)
    lhs = wick_rotated_partition(tent_transform, x, y)
    rhs = mp.mpf("0.5") * abs(tent_transform(z)) ** 2
    assert mp.almosteq(lhs, rhs, rel_eps=mp.mpf("1e-50"), abs_eps=mp.mpf("1e-55"))


def test_wick_rotated_relative_susceptibility_is_jensen():
    mp.mp.dps = 55
    x = mp.mpf("3.2")
    y = mp.mpf("0.21")
    lhs = wick_rotated_relative_susceptibility(tent_transform, x, y)
    rhs = hermitian_jensen_value(tent_transform, mp.mpc(x, y))
    assert mp.almosteq(lhs, rhs, rel_eps=mp.mpf("1e-45"), abs_eps=mp.mpf("1e-50"))


def test_riemann_susceptibility_matches_hermitian_jensen():
    mp.mp.dps = 55
    x = mp.mpf("14.134725141734693790")
    y = mp.mpf("0.1")
    lhs = riemann_relative_susceptibility(x, y)
    rhs = hermitian_jensen_value(xi_fourier_entire, mp.mpc(x, y))
    assert mp.almosteq(lhs, rhs, rel_eps=mp.mpf("1e-40"), abs_eps=mp.mpf("1e-48"))


def test_theta_potential_is_same_partition_free_energy_displacement():
    mp.mp.dps = 50
    for y in [mp.mpf("0"), mp.mpf("0.1"), mp.mpf("0.25"), mp.mpf("0.49")]:
        assert abs(theta_partition_identity_residual(y)) < mp.mpf("1e-45")


def test_smooth_lp_dyadic_numeric_witness_splits_external_and_hermitian():
    mp.mp.dps = 70
    external, hermitian = dyadic_external_and_hermitian_witness(n_terms=80)
    assert external < 0
    assert hermitian > 0
