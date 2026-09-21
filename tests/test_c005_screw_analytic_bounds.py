from __future__ import annotations

import pytest

from secret_of_a_half.c005_screw_analytic_bounds import (
    cutoff_for_uniform_mixed_norm,
    screw_analytic_gate_receipt,
    screw_l2_envelope,
    uniform_mixed_norm_upper,
)


def test_screw_l2_envelope_is_positive() -> None:
    env = screw_l2_envelope(0.25)
    assert env.T == pytest.approx(0.5)
    assert env.g_l2_sq_upper > 0.0
    assert env.gprime_l2_sq_upper > 0.0
    assert env.pointwise_g_abs_upper > 0.0


def test_screw_envelopes_increase_with_a0_for_test_range() -> None:
    small = screw_l2_envelope(0.1)
    large = screw_l2_envelope(0.5)
    assert large.g_l2_sq_upper > small.g_l2_sq_upper
    assert large.gprime_l2_sq_upper > small.gprime_l2_sq_upper


def test_uniform_mixed_norm_decreases_with_cutoff() -> None:
    b100 = uniform_mixed_norm_upper(0.25, 100)
    b400 = uniform_mixed_norm_upper(0.25, 400)
    assert b400 == pytest.approx(b100 / 2.0, rel=1e-12)


def test_uniform_mixed_cutoff_meets_target() -> None:
    cert = cutoff_for_uniform_mixed_norm(0.25, 0.1)
    assert cert.pass_target
    assert cert.mixed_norm_upper <= 0.1
    if cert.cutoff_N > 1:
        assert uniform_mixed_norm_upper(0.25, cert.cutoff_N - 1) > 0.1


def test_receipt_exposes_only_low_block_as_first_major_gate() -> None:
    receipt = screw_analytic_gate_receipt(0.25, 0.1)
    assert receipt["mixed_gate_pass"] is True
    assert receipt["proof_of_rh"] is False
    assert "finite localized low Fourier block interval enclosure" in receipt["open"]


def test_invalid_inputs_fail_closed() -> None:
    with pytest.raises(ValueError):
        screw_l2_envelope(0.0)
    with pytest.raises(ValueError):
        cutoff_for_uniform_mixed_norm(0.25, 0.0)
