import mpmath as mp

from secret_of_a_half.riemann_kernel import (
    completed_xi,
    even_moment,
    riemann_kernel,
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


def test_first_even_moments_are_strictly_positive():
    mp.mp.dps = 30
    moments = [even_moment(order) for order in range(4)]
    assert all(moment > 0 for moment in moments)


def test_kernel_api_fails_closed_on_invalid_inputs():
    try:
        riemann_kernel(-1)
    except ValueError:
        pass
    else:
        raise AssertionError("negative y must be rejected")

    try:
        even_moment(-1)
    except ValueError:
        pass
    else:
        raise AssertionError("negative moment order must be rejected")
