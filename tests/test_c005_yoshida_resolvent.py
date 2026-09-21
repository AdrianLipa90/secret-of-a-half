from __future__ import annotations

import math
import pytest

from secret_of_a_half.c005_yoshida_resolvent import (
    cutoff_for_leakage,
    fourier_tail_sum_upper,
    high_mode_resolvent_certificate,
    integrated_low_frequency_leakage_upper,
    leakage_coefficient,
    low_block_effective_floor,
    pipeline_gate_map,
    scalar_schur_certificate,
)


def test_fourier_tail_bound_decreases_like_inverse_cutoff() -> None:
    for n in (1, 2, 5, 10, 100):
        value = fourier_tail_sum_upper(n)
        assert value == pytest.approx(2.0 / (math.pi * math.pi * n))
        assert fourier_tail_sum_upper(2 * n) == pytest.approx(value / 2.0)


def test_leakage_schedule_is_fail_closed_and_monotone() -> None:
    a0 = 2.0
    t0 = 1.5
    tolerances = (1e-2, 1e-3, 1e-4)
    schedules = [cutoff_for_leakage(a0, t0, eta) for eta in tolerances]
    assert [item.cutoff for item in schedules] == sorted(
        [item.cutoff for item in schedules]
    )
    for item in schedules:
        assert item.pass_bound
        assert item.certified_bound <= item.tolerance
        if item.cutoff > 1:
            previous = integrated_low_frequency_leakage_upper(
                a0, t0, item.cutoff - 1
            )
            assert previous > item.tolerance


def test_leakage_coefficient_matches_closed_formula() -> None:
    a0 = 1.25
    t0 = 0.75
    expected = (
        8.0
        * a0
        / (math.pi * math.pi)
        * (t0 + a0 * t0**2 + a0**2 * t0**3 / 3.0)
    )
    assert leakage_coefficient(a0, t0) == pytest.approx(expected)


def test_resolvent_bound_uses_positive_spectral_gap() -> None:
    cert = high_mode_resolvent_certificate(3.0, 1.75)
    assert cert.admissible
    assert cert.gap == pytest.approx(1.25)
    assert cert.norm_upper_bound == pytest.approx(0.8)

    with pytest.raises(ValueError):
        high_mode_resolvent_certificate(1.0, 1.0)
    with pytest.raises(ValueError):
        high_mode_resolvent_certificate(1.0, 2.0)


def test_scalar_schur_margin_and_effective_floor_agree() -> None:
    mu = 2.0
    epsilon = 0.5
    nu = 3.0
    cert = scalar_schur_certificate(mu, epsilon, nu)
    assert cert.strict
    assert cert.determinant_margin == pytest.approx(mu * nu - epsilon**2)
    effective = low_block_effective_floor(mu, epsilon, nu)
    assert effective == pytest.approx(cert.determinant_margin / nu)
    assert effective > 0.0


def test_pipeline_keeps_proof_frontier_open() -> None:
    gates = pipeline_gate_map()
    assert gates["proof_of_rh"] is False
    assert "Riemann Hypothesis" in gates["open"]
    assert "exact repository-to-Suzuki normalization/domain join" in gates["open"]
    assert "HIGH_MODE_RESOLVENT_BOUND" in gates["flow"]
