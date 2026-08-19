from __future__ import annotations

from fractions import Fraction

import mpmath as mp
import pytest

from secret_of_a_half.half_mass_pf3_no_go import (
    adjacent_ratio_numeric,
    counterexample_weight_numeric,
    normalization_cubic,
    normalizing_ratio_numeric,
    pf2_minor_numeric,
    positive_mass_closed_form_numeric,
    solid_pf3_margin_exact,
    solid_pf3_minor_k2_numeric,
)


def test_normalizing_ratio_is_unique_root_in_unit_interval() -> None:
    mp.mp.dps = 80
    x = normalizing_ratio_numeric(80)
    assert 0 < x < 1
    assert abs(normalization_cubic(x)) < mp.mpf("1e-60")
    assert mp.mpf("0.83") < x < mp.mpf("0.85")


def test_half_mass_normalization() -> None:
    mp.mp.dps = 80
    assert abs(positive_mass_closed_form_numeric(dps=80) - mp.mpf("0.5")) < mp.mpf("1e-60")
    assert counterexample_weight_numeric(0, dps=80) == mp.mpf("0.5")


def test_weights_are_positive_and_strictly_decreasing() -> None:
    mp.mp.dps = 70
    weights = [counterexample_weight_numeric(n, dps=70) for n in range(12)]
    assert all(value > 0 for value in weights)
    assert all(weights[n] > weights[n + 1] for n in range(len(weights) - 1))


def test_adjacent_ratios_are_nonincreasing_pf2() -> None:
    mp.mp.dps = 70
    ratios = [adjacent_ratio_numeric(n, dps=70) for n in range(1, 12)]
    assert all(0 < value < 1 for value in ratios)
    assert all(ratios[n] >= ratios[n + 1] for n in range(len(ratios) - 1))
    for n in range(1, 10):
        assert pf2_minor_numeric(n, dps=70) >= -mp.mpf("1e-65")


def test_g020_monotone_envelope_property() -> None:
    mp.mp.dps = 70
    for n in range(1, 12):
        b_n = 2 * counterexample_weight_numeric(n, dps=70)
        assert b_n < mp.mpf(1) / n


def test_pf3_margin_is_exactly_negative() -> None:
    assert solid_pf3_margin_exact() == Fraction(-1271, 2500)
    assert solid_pf3_margin_exact() < 0


def test_solid_pf3_minor_is_negative() -> None:
    mp.mp.dps = 70
    assert solid_pf3_minor_k2_numeric(dps=70) < 0


def test_invalid_indices_fail_closed() -> None:
    with pytest.raises(ValueError):
        adjacent_ratio_numeric(0, dps=60)
    with pytest.raises(ValueError):
        counterexample_weight_numeric(-1, dps=60)
    with pytest.raises(ValueError):
        pf2_minor_numeric(0, dps=60)
