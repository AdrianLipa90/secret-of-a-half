import mpmath as mp
import pytest

from secret_of_a_half.negative_inversion_zero_set import (
    completed_xi,
    mapped_critical_height,
    negative_inversion_defect_from_half,
    negative_inversion_fixed_s,
    negative_inversion_s,
)


def _close(a, b, tol="1e-45") -> bool:
    return abs(a - b) < mp.mpf(tol)


def test_exact_s_plane_formula_is_involution() -> None:
    mp.mp.dps = 60
    samples = [mp.mpc("0.2", "0.7"), mp.mpc("1.3", "-0.4"), mp.mpc("-2.1", "1.2")]
    for s in samples:
        assert _close(negative_inversion_s(negative_inversion_s(s)), s)


def test_exact_defect_from_half_identity() -> None:
    mp.mp.dps = 60
    for s in [mp.mpc("3.2", "1.1"), mp.mpc("-4.7", "0.9"), mp.mpc("0.8", "2.4")]:
        assert _close(
            negative_inversion_s(s) - mp.mpf("0.5"),
            negative_inversion_defect_from_half(s),
        )
        assert _close(
            negative_inversion_defect_from_half(s),
            -1 / (4 * s - 2),
        )


def test_fixed_pair_matches_g012() -> None:
    mp.mp.dps = 60
    for s in negative_inversion_fixed_s():
        assert _close(negative_inversion_s(s), s)
        assert _close(mp.re(s), mp.mpf("0.5"))
        assert _close(abs(mp.im(s)), mp.mpf("0.5"))


def test_critical_line_height_map() -> None:
    mp.mp.dps = 60
    for t in [mp.mpf("2"), mp.mpf("14.1347251417347"), mp.mpf("100")]:
        s = mp.mpc(mp.mpf("0.5"), t)
        expected = mapped_critical_height(t)
        assert _close(negative_inversion_s(s), expected)
        assert _close(mp.re(expected), mp.mpf("0.5"))
        assert _close(mp.im(expected), 1 / (4 * t))


def test_unbounded_inputs_contract_to_half() -> None:
    mp.mp.dps = 60
    radii = [mp.mpf("10"), mp.mpf("100"), mp.mpf("1000"), mp.mpf("10000")]
    defects = [abs(negative_inversion_s(mp.mpc(r, r / 3)) - mp.mpf("0.5")) for r in radii]
    assert all(b < a for a, b in zip(defects, defects[1:]))
    assert defects[-1] < mp.mpf("3e-5")


def test_xi_half_is_nonzero_and_positive() -> None:
    mp.mp.dps = 60
    value = completed_xi(mp.mpf("0.5"))
    assert abs(mp.im(value)) < mp.mpf("1e-50")
    assert mp.re(value) > 0


def test_first_nontrivial_zeros_are_not_sent_to_zeros() -> None:
    mp.mp.dps = 50
    for n in range(1, 4):
        rho = mp.zetazero(n)
        image = negative_inversion_s(rho)
        assert abs(mp.zeta(rho)) < mp.mpf("1e-40")
        # The image lies close to 1/2 and is numerically far from a xi zero.
        assert abs(completed_xi(image)) > mp.mpf("0.1")


def test_fail_closed_at_affine_pole_and_zero_height() -> None:
    with pytest.raises(ValueError):
        negative_inversion_s(mp.mpf("0.5"))
    with pytest.raises(ValueError):
        negative_inversion_defect_from_half(mp.mpf("0.5"))
    with pytest.raises(ValueError):
        mapped_critical_height(0)
