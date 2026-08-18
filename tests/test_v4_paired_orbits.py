from __future__ import annotations

import mpmath as mp
import pytest

from secret_of_a_half.negative_inversion_zero_set import completed_xi
from secret_of_a_half.paired_spectrum_quotient import quotient_map_s_to_w
from secret_of_a_half.v4_paired_orbits import (
    euler_halfturn_fixed_pair,
    euler_halfturn_s,
    negative_inversion_fixed_pair,
    orbit_cardinality,
    paired_set_cardinality,
    quotient_paired_set_cardinality,
    reflection_fixed_point,
    reflection_s,
    v4_algebra_residuals,
)


mp.mp.dps = 80


def test_v4_algebra_closes_numerically() -> None:
    s = mp.mpc("0.37", "2.125")
    residuals = v4_algebra_residuals(s)
    assert max(residuals.values()) < mp.mpf("1e-70")


def test_euler_halfturn_is_R_after_N() -> None:
    s = mp.mpc("0.19", "1.75")
    from secret_of_a_half.negative_inversion_zero_set import negative_inversion_s

    assert abs(euler_halfturn_s(s) - reflection_s(negative_inversion_s(s))) < mp.mpf(
        "1e-70"
    )


def test_fixed_loci_are_exact() -> None:
    r0 = reflection_fixed_point()
    assert reflection_s(r0) == r0

    for s in negative_inversion_fixed_pair():
        from secret_of_a_half.negative_inversion_zero_set import negative_inversion_s

        assert abs(negative_inversion_s(s) - s) < mp.mpf("1e-70")
        assert abs(quotient_map_s_to_w(s) + mp.mpf("0.25")) < mp.mpf("1e-70")

    for s in euler_halfturn_fixed_pair():
        assert euler_halfturn_s(s) == s


def test_nonzero_xi_excludes_R_and_E_fixed_points_from_zero_orbits() -> None:
    assert completed_xi(0) == mp.mpf("0.5")
    assert completed_xi(1) == mp.mpf("0.5")
    assert abs(completed_xi(mp.mpf("0.5"))) > mp.mpf("0.1")


def test_generic_v4_orbit_has_four_points() -> None:
    assert orbit_cardinality(mp.mpc("0.37", "2.125")) == 4


def test_negative_inversion_fixed_pair_forms_two_point_v4_orbit() -> None:
    plus, minus = negative_inversion_fixed_pair()
    assert orbit_cardinality(plus) == 2
    assert orbit_cardinality(minus) == 2
    assert reflection_s(plus) == minus
    assert reflection_s(minus) == plus


def test_exact_cardinality_formula_matches_g016_two_to_one() -> None:
    for generic_orbits in range(8):
        for exceptional in (False, True):
            pn = paired_set_cardinality(generic_orbits, exceptional)
            pj = quotient_paired_set_cardinality(generic_orbits, exceptional)
            assert pn == 2 * pj
            assert pn % 4 == (2 if exceptional else 0)
            assert pj % 2 == (1 if exceptional else 0)


def test_cardinality_helpers_reject_invalid_counts() -> None:
    with pytest.raises(ValueError):
        paired_set_cardinality(-1, False)
    with pytest.raises(TypeError):
        quotient_paired_set_cardinality(True, False)


def test_affine_pole_is_fail_closed() -> None:
    with pytest.raises(ValueError):
        euler_halfturn_s(mp.mpf("0.5"))
    with pytest.raises(ValueError):
        orbit_cardinality(mp.mpf("0.5"))
