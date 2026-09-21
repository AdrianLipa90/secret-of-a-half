from __future__ import annotations

import cmath
import math

import pytest

from secret_of_a_half.c005_suzuki_normalization import (
    fourier_phase_soh,
    fourier_phase_suzuki,
    normalization_crosswalk_receipt,
    soh_prime_shift,
    soh_spectral_r,
    soh_support_halfwidth,
    soh_x_from_suzuki_x,
    suzuki_prime_shift,
    suzuki_spectral_z,
    suzuki_x_from_soh_x,
)


def test_spectral_coordinates_differ_by_sign() -> None:
    samples = [0.5 + 14j, 0.3 + 7.2j, 0.8 - 2.5j]
    for s in samples:
        assert suzuki_spectral_z(s) == pytest.approx(-soh_spectral_r(s))


def test_fourier_phase_matches_under_coordinate_crosswalk() -> None:
    samples = [
        (0.125, 14.0 + 0j),
        (-0.3, 2.5 - 0.2j),
        (1.2, -3.0 + 0.7j),
    ]
    for x_repo, r in samples:
        x_suzuki = suzuki_x_from_soh_x(x_repo)
        z = -r
        assert fourier_phase_soh(x_repo, r) == pytest.approx(
            fourier_phase_suzuki(x_suzuki, z)
        )
        assert cmath.exp(fourier_phase_soh(x_repo, r)) == pytest.approx(
            cmath.exp(fourier_phase_suzuki(x_suzuki, z))
        )


def test_prime_shift_and_support_scaling() -> None:
    for n in (2, 3, 5, 17, 101):
        assert suzuki_x_from_soh_x(soh_prime_shift(n)) == pytest.approx(
            suzuki_prime_shift(n)
        )
    a = 3.25
    assert suzuki_x_from_soh_x(soh_support_halfwidth(a)) == pytest.approx(a)
    assert soh_x_from_suzuki_x(a) == pytest.approx(a / (2.0 * math.pi))


def test_crosswalk_stays_fail_closed_at_operator_level() -> None:
    receipt = normalization_crosswalk_receipt()
    assert receipt["proof_of_rh"] is False
    assert receipt["exact"]["fourier_phase_matches_under_crosswalk"] is True
    assert "localized form equality with all boundary terms" in receipt["open"]
