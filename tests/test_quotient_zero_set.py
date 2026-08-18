import mpmath as mp
import pytest

from secret_of_a_half.quotient_zero_set import (
    quotient_F,
    quotient_F_branch_residual,
    quotient_fixed_w,
    quotient_negative_inversion_w,
    w_from_xi_zero,
)


def _close(a, b, tol="1e-45") -> bool:
    return abs(a - b) < mp.mpf(tol)


def test_quotient_involution() -> None:
    mp.mp.dps = 60
    samples = [mp.mpc("2.3", "0.4"), mp.mpc("-3.7", "1.1"), mp.mpc("0.8", "-2.2")]
    for w in samples:
        assert _close(quotient_negative_inversion_w(quotient_negative_inversion_w(w)), w)


def test_quotient_fixed_values() -> None:
    mp.mp.dps = 60
    for w in quotient_fixed_w():
        assert _close(quotient_negative_inversion_w(w), w)


def test_F_branch_independence() -> None:
    mp.mp.dps = 60
    for w in [mp.mpc("0.3", "0.2"), mp.mpc("-4.1", "0.7"), mp.mpf("-10")]:
        assert quotient_F_branch_residual(w) < mp.mpf("1e-45")


def test_F_zero_origin_and_positive_center() -> None:
    mp.mp.dps = 60
    assert abs(mp.im(quotient_F(0))) < mp.mpf("1e-50")
    assert mp.re(quotient_F(0)) > 0
    assert mp.re(quotient_F(mp.mpf("0.25"))) > 0


def test_first_xi_zeros_map_to_F_roots_but_quotient_images_do_not() -> None:
    mp.mp.dps = 50
    for n in range(1, 4):
        rho = mp.zetazero(n)
        w = w_from_xi_zero(rho)
        image = quotient_negative_inversion_w(w)
        assert abs(quotient_F(w)) < mp.mpf("1e-35")
        assert mp.re(w) < 0
        assert abs(mp.im(w)) < mp.mpf("1e-40")
        assert abs(image) < mp.mpf("0.001")
        assert abs(quotient_F(image)) > mp.mpf("0.1")


def test_large_w_contracts_to_zero() -> None:
    radii = [mp.mpf("10"), mp.mpf("100"), mp.mpf("1000"), mp.mpf("10000")]
    images = [abs(quotient_negative_inversion_w(-r)) for r in radii]
    assert all(b < a for a, b in zip(images, images[1:]))
    assert _close(images[-1], mp.mpf(1) / mp.mpf(160000))


def test_fail_closed_at_zero() -> None:
    with pytest.raises(ValueError):
        quotient_negative_inversion_w(0)
