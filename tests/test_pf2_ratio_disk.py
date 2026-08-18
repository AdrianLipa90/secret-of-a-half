from __future__ import annotations

import mpmath as mp
import pytest

from secret_of_a_half.pf2_ratio_disk import (
    boundary_regression,
    canonical_pf2_zero_free_radius_numeric,
    first_two_coefficients_numeric,
    pf2_ratio_zero_free_radius,
    pf2_tail_majorant,
    ratio_majorant_certificate,
)


def test_pf2_ratio_radius_formula_is_exact() -> None:
    mp.mp.dps = 60
    a0 = mp.mpf("5")
    a1 = mp.mpf("2")
    assert pf2_ratio_zero_free_radius(a0, a1) == mp.mpf("1.25")


def test_boundary_geometric_parameter_is_exactly_half() -> None:
    mp.mp.dps = 80
    a0, a1 = first_two_coefficients_numeric()
    cert = ratio_majorant_certificate(a0, a1)
    assert cert["boundary_qr_is_half"] is True
    assert cert["q0_times_radius"] == mp.mpf("0.5")


def test_open_disk_tail_majorant_is_strictly_below_a0() -> None:
    mp.mp.dps = 80
    a0, a1 = first_two_coefficients_numeric()
    radius = pf2_ratio_zero_free_radius(a0, a1)
    tail = pf2_tail_majorant(a0, a1, mp.mpf("0.999") * radius)
    assert tail < a0


def test_canonical_radius_is_about_twenty_one_point_six() -> None:
    mp.mp.dps = 80
    radius = canonical_pf2_zero_free_radius_numeric()
    assert mp.mpf("21.6") < radius < mp.mpf("21.7")


def test_boundary_sampling_is_nonzero_regression_only() -> None:
    mp.mp.dps = 50
    assert boundary_regression(samples=32) > mp.mpf("0.25")


def test_fail_closed_on_invalid_coefficients() -> None:
    with pytest.raises(ValueError):
        pf2_ratio_zero_free_radius(0, 1)
    with pytest.raises(ValueError):
        pf2_ratio_zero_free_radius(1, 0)
    with pytest.raises(ValueError):
        pf2_tail_majorant(1, 1, 1)
