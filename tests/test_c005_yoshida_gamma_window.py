from __future__ import annotations

import mpmath as mp
import pytest

from secret_of_a_half.c005_yoshida_gamma_window import (
    compact_C0_upper,
    explicit_t0_for_target_C,
    gamma_profile_lower,
    gamma_profile_upper,
    gamma_radius,
    gamma_window_certificate,
    gamma_window_gate_receipt,
    simple_tail_lower,
)


def test_gamma_radius_matches_exact_geometry() -> None:
    z = mp.mpf("7.25")
    expected = abs(mp.mpc(mp.mpf("0.25"), -z / 2))
    assert gamma_radius(z) == pytest.approx(float(expected))


def test_dlmf_envelopes_are_ordered() -> None:
    for z in ("0", "0.5", "1", "10", "100"):
        assert gamma_profile_lower(z) <= gamma_profile_upper(z)


def test_explicit_tail_threshold_clears_target() -> None:
    for C in ("0.1", "1", "5", "10"):
        t0 = explicit_t0_for_target_C(C)
        assert simple_tail_lower(t0) > mp.mpf(C)
        assert simple_tail_lower(2 * t0) > simple_tail_lower(t0)


def test_compact_upper_envelope_is_finite() -> None:
    for t0 in ("1", "10", "100"):
        value = compact_C0_upper(t0)
        assert mp.isfinite(value)


def test_gamma_window_certificate_is_fail_closed() -> None:
    cert = gamma_window_certificate("7.5")
    assert cert.pass_tail
    assert mp.mpf(cert.tail_lower_at_t0) > mp.mpf(cert.target_C)
    assert mp.mpf(cert.C0_upper) > 0


def test_gamma_window_receipt_keeps_operator_frontier_open() -> None:
    receipt = gamma_window_gate_receipt("5")
    assert receipt["tail_gate_pass"] is True
    assert receipt["proof_of_rh"] is False
    assert (
        "extract exact coefficients of Suzuki equation (4.11) in repository normalization"
        in receipt["open"]
    )


def test_invalid_gamma_inputs_fail_closed() -> None:
    with pytest.raises(ValueError):
        explicit_t0_for_target_C(0)
    with pytest.raises(ValueError):
        gamma_radius(-1)
    with pytest.raises(ValueError):
        compact_C0_upper(0)
