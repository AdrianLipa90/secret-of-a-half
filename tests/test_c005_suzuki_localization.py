from __future__ import annotations

import cmath
import math

import pytest

from secret_of_a_half.c005_suzuki_localization import (
    derivative_conjugation_factor,
    localization_crosswalk_receipt,
    pulled_convolution_kernel_argument,
    pulled_convolution_kernel_multiplier,
    pulled_full_kernel_B_derivative_prefactor,
    raw_scaled_kernel_B_prefactor,
    pullback_basis_via_definition,
    soh_halfwidth_from_suzuki_a,
    soh_pulled_back_fourier_basis_value,
    soh_x_from_suzuki_y,
    suzuki_fourier_basis_value,
    suzuki_y_from_soh_x,
    unitary_amplitude_factor,
    zero_mean_integral_scale,
)


def test_coordinate_maps_are_inverse() -> None:
    for x in (-2.0, -0.25, 0.0, 0.75, 3.0):
        assert soh_x_from_suzuki_y(suzuki_y_from_soh_x(x)) == pytest.approx(x)


def test_localization_halfwidth_scaling() -> None:
    a = 5.0
    h = soh_halfwidth_from_suzuki_a(a)
    assert suzuki_y_from_soh_x(h) == pytest.approx(a)
    assert suzuki_y_from_soh_x(-h) == pytest.approx(-a)


def test_unitary_basis_pullback_formula() -> None:
    a = 2.75
    for n in (-3, -1, 0, 2, 5):
        for x in (-0.2, 0.0, 0.13):
            explicit = soh_pulled_back_fourier_basis_value(n, a, x)
            direct = pullback_basis_via_definition(n, a, x)
            assert explicit == pytest.approx(direct)


def test_basis_density_is_constant_and_norms_match_analytically() -> None:
    a = 3.0
    half = soh_halfwidth_from_suzuki_a(a)
    value = soh_pulled_back_fourier_basis_value(7, a, 0.123)
    density = abs(value) ** 2
    assert density == pytest.approx(math.pi / a)
    # Interval length in x is a/pi, so the pulled-back basis has L2 norm 1.
    assert density * (2.0 * half) == pytest.approx(1.0)


def test_derivative_and_zero_mean_scales_are_nonzero_exact_constants() -> None:
    assert derivative_conjugation_factor() == pytest.approx(1.0 / (2.0 * math.pi))
    assert zero_mean_integral_scale() == pytest.approx(math.sqrt(2.0 * math.pi))
    assert unitary_amplitude_factor() == pytest.approx(math.sqrt(2.0 * math.pi))


def test_source_fourier_basis_has_unit_density_integral() -> None:
    a = 4.0
    value = suzuki_fourier_basis_value(3, a, 0.7)
    assert abs(value) ** 2 * (2.0 * a) == pytest.approx(1.0)


def test_localization_receipt_keeps_kernel_pullback_open() -> None:
    receipt = localization_crosswalk_receipt()
    assert receipt["proof_of_rh"] is False
    assert "generic convolution pullback G -> kernel 2*pi*g(2*pi*delta)" in receipt["closed"]
    assert "instantiate the actual zeta screw kernel g in repository-native localized code" in receipt["open"]


def test_invalid_a_fails_closed() -> None:
    with pytest.raises(ValueError):
        soh_halfwidth_from_suzuki_a(0.0)
    with pytest.raises(ValueError):
        suzuki_fourier_basis_value(0, -1.0, 0.0)


def test_generic_convolution_and_DGD_pullback_factors() -> None:
    assert pulled_convolution_kernel_multiplier() == pytest.approx(2.0 * math.pi)
    assert pulled_convolution_kernel_argument(0.25) == pytest.approx(0.5 * math.pi)
    assert raw_scaled_kernel_B_prefactor() == pytest.approx(1.0 / (2.0 * math.pi))
    assert pulled_full_kernel_B_derivative_prefactor() == pytest.approx(
        1.0 / (4.0 * math.pi * math.pi)
    )
