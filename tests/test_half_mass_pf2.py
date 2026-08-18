from __future__ import annotations

import mpmath as mp
import pytest

from secret_of_a_half.half_mass_pf2 import (
    canonical_half_mass_weight,
    canonical_radius_numeric,
    pf2_minor_numeric,
    quotient_coefficient_numeric,
    sharpened_coefficient_envelope,
)


def test_half_mass_at_zero_exact() -> None:
    assert canonical_half_mass_weight(0, dps=60) == mp.mpf("0.5")


def test_first_weights_are_positive_and_strictly_decreasing() -> None:
    mp.mp.dps = 60
    weights = [canonical_half_mass_weight(n, dps=60) for n in range(6)]
    assert all(value > 0 for value in weights)
    assert all(weights[n] > weights[n + 1] for n in range(len(weights) - 1))


def test_first_pf2_minors_are_positive() -> None:
    mp.mp.dps = 60
    for n in range(1, 5):
        assert pf2_minor_numeric(n, dps=60) > 0


def test_positive_mass_partial_sum_stays_below_half() -> None:
    mp.mp.dps = 60
    positive_partial = sum(canonical_half_mass_weight(n, dps=60) for n in range(1, 6))
    assert positive_partial < mp.mpf("0.5")
    assert positive_partial > mp.mpf("0.49")


def test_sharpened_envelope_holds_for_first_coefficients() -> None:
    mp.mp.dps = 60
    for n in range(1, 6):
        assert quotient_coefficient_numeric(n, 60) < sharpened_coefficient_envelope(n, dps=60)


def test_radius_is_inherited_from_g019() -> None:
    mp.mp.dps = 60
    radius = canonical_radius_numeric(60)
    assert mp.mpf("30") < radius < mp.mpf("31")


def test_invalid_indices_fail_closed() -> None:
    with pytest.raises(ValueError):
        quotient_coefficient_numeric(-1, 60)
    with pytest.raises(ValueError):
        pf2_minor_numeric(0, dps=60)
    with pytest.raises(ValueError):
        sharpened_coefficient_envelope(0, dps=60)
