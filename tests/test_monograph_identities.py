"""Regression tests for the exact elementary results used in the monograph."""

from __future__ import annotations

import math

import pytest

from secret_of_a_half.core import binary_entropy, complementary_amplitude, involution


def test_entropy_is_strictly_smaller_away_from_half() -> None:
    peak = binary_entropy(0.5)
    for sigma in (0.01, 0.1, 0.25, 0.49, 0.51, 0.75, 0.9, 0.99):
        assert binary_entropy(sigma) < peak


def test_entropy_is_complement_symmetric() -> None:
    for sigma in (0.01, 0.1, 0.23, 0.49):
        assert math.isclose(
            binary_entropy(sigma),
            binary_entropy(1.0 - sigma),
            rel_tol=0.0,
            abs_tol=1e-14,
        )


def test_pi_locked_cancellation_has_unique_balanced_zero_on_grid() -> None:
    zeros: list[float] = []
    for k in range(1001):
        sigma = k / 1000.0
        if abs(complementary_amplitude(sigma, math.pi)) < 1e-13:
            zeros.append(sigma)
    assert zeros == [0.5]


def test_half_state_requires_pi_phase_for_zero() -> None:
    for phase in (0.0, math.pi / 3.0, math.pi / 2.0, 2.0 * math.pi / 3.0):
        assert abs(complementary_amplitude(0.5, phase)) > 1e-8
    assert abs(complementary_amplitude(0.5, math.pi)) < 1e-14


def test_involution_is_an_involution() -> None:
    for s in (0.23 + 7.1j, 0.5 + 14.2j, 1.3 - 4.0j):
        recovered = involution(involution(s))
        assert math.isclose(recovered.real, s.real, rel_tol=0.0, abs_tol=1e-15)
        assert math.isclose(recovered.imag, s.imag, rel_tol=0.0, abs_tol=1e-15)


def test_involution_swaps_complementary_real_parts() -> None:
    s = 0.23 + 7.1j
    image = involution(s)
    assert math.isclose(image.real, 0.77, rel_tol=0.0, abs_tol=1e-15)
    assert math.isclose(image.imag, 7.1, rel_tol=0.0, abs_tol=1e-15)


def test_domain_guards() -> None:
    with pytest.raises(ValueError):
        binary_entropy(0.0)
    with pytest.raises(ValueError):
        binary_entropy(1.0)
    with pytest.raises(ValueError):
        complementary_amplitude(-0.01, 0.0)
    with pytest.raises(ValueError):
        complementary_amplitude(1.01, 0.0)
