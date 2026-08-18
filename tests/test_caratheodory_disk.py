from __future__ import annotations

import mpmath as mp
import pytest

from secret_of_a_half.caratheodory_disk import (
    F0_numeric,
    centered_z_radius_numeric,
    coefficient_majorant_margin,
    majorant_threshold_numeric,
    positive_axis_F,
    sampled_min_real_part,
)


def test_F0_is_positive() -> None:
    mp.mp.dps = 60
    assert F0_numeric() > mp.mpf("0.49")


def test_majorant_threshold_is_unique_numeric_regression() -> None:
    mp.mp.dps = 70
    radius = majorant_threshold_numeric(dps=70, iterations=220)
    assert mp.mpf("30") < radius < mp.mpf("31")
    residual = abs(positive_axis_F(radius) - 2 * F0_numeric())
    assert residual < mp.mpf("1e-55")


def test_threshold_strictly_extends_G018_quarter_disk() -> None:
    mp.mp.dps = 60
    radius = majorant_threshold_numeric(dps=60, iterations=200)
    assert radius > mp.mpf("0.25")
    assert radius / mp.mpf("0.25") > 120


def test_centered_z_radius_regression() -> None:
    mp.mp.dps = 60
    z_radius = centered_z_radius_numeric(dps=60)
    assert mp.mpf("5.54") < z_radius < mp.mpf("5.55")


def test_majorant_margin_changes_sign_across_threshold() -> None:
    mp.mp.dps = 60
    assert coefficient_majorant_margin(mp.mpf("30")) > 0
    assert coefficient_majorant_margin(mp.mpf("31")) < 0


def test_sampled_real_part_positive_inside_threshold() -> None:
    mp.mp.dps = 50
    radius = mp.mpf("30")
    assert sampled_min_real_part(radius, samples=48) > 0


def test_invalid_inputs_fail_closed() -> None:
    with pytest.raises(ValueError):
        positive_axis_F(mp.mpf("-1"))
    with pytest.raises(ValueError):
        majorant_threshold_numeric(dps=20)
    with pytest.raises(ValueError):
        sampled_min_real_part(mp.mpf("1"), samples=4)
