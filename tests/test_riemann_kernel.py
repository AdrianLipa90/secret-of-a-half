import mpmath as mp

from secret_of_a_half.riemann_kernel import (
    compactified_kernel_weight,
    compactified_radius_from_x,
    completed_xi,
    even_moment,
    modular_density,
    riemann_kernel,
    x_from_compactified_radius,
    xi_from_compactified_kernel,
    xi_from_kernel,
)


def test_kernel_terms_sum_to_positive_values_on_half_line():
    mp.mp.dps = 30
    for y in [0, mp.mpf("0.25"), mp.mpf("0.5"), mp.mpf("1"), mp.mpf("2")]:
        assert riemann_kernel(y) > 0


def test_kernel_representation_matches_completed_xi():
    mp.mp.dps = 30
    for z in [0, mp.mpf("0.25"), 1j, mp.mpc("0.2", "0.7")]:
        direct = completed_xi(mp.mpf("0.5") + z)
        kernel = xi_from_kernel(z)
        assert abs(direct - kernel) < mp.mpf("1e-20")


def test_modular_density_and_compactified_weight_are_positive():
    mp.mp.dps = 30
    for x in [1, mp.mpf("1.5"), 2, 4, 16]:
        assert modular_density(x) > 0
    for eta in [0, mp.mpf("0.1"), mp.mpf("0.5"), mp.mpf("0.9")]:
        assert compactified_kernel_weight(eta) > 0


def test_modular_inversion_becomes_signed_compact_radius_reflection():
    mp.mp.dps = 30
    for raw_x in ["0.2", "0.5", "1", "2", "5"]:
        x = mp.mpf(raw_x)
        eta = compactified_radius_from_x(x)
        eta_inverse = compactified_radius_from_x(mp.mpf("1") / x)
        assert abs(eta_inverse + eta) < mp.mpf("1e-28")
        assert abs(x_from_compactified_radius(eta) - x) < mp.mpf("1e-28")


def test_compactified_kernel_is_exact_change_of_variables():
    mp.mp.dps = 30
    for z in [0, mp.mpf("0.25"), 1j, mp.mpc("0.2", "0.7")]:
        direct_kernel = xi_from_kernel(z)
        compactified = xi_from_compactified_kernel(z)
        assert abs(direct_kernel - compactified) < mp.mpf("1e-20")


def test_first_even_moments_are_strictly_positive():
    mp.mp.dps = 30
    moments = [even_moment(order) for order in range(4)]
    assert all(moment > 0 for moment in moments)


def test_kernel_api_fails_closed_on_invalid_inputs():
    for call in [
        lambda: riemann_kernel(-1),
        lambda: modular_density(mp.mpf("0.5")),
        lambda: compactified_kernel_weight(mp.mpf("-0.1")),
        lambda: compactified_kernel_weight(1),
        lambda: x_from_compactified_radius(1),
        lambda: compactified_radius_from_x(0),
        lambda: even_moment(-1),
    ]:
        try:
            call()
        except ValueError:
            pass
        else:
            raise AssertionError("invalid kernel input must fail closed")
