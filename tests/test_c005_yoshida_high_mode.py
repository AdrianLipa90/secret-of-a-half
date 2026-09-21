from __future__ import annotations

import mpmath as mp
import pytest

from secret_of_a_half.c005_yoshida_high_mode import (
    c1_upper_c_eq_2_mp,
    c2_upper_c_eq_2_mp,
    explicit_high_mode_certificate,
    high_mode_gate_receipt,
    leakage_B_mp,
    raw_integral_floor,
)


def test_mp_source_constants_match_elementary_envelopes() -> None:
    assert c1_upper_c_eq_2_mp() == mp.mpf(5) / 6
    a1 = mp.mpf("0.25")
    assert c2_upper_c_eq_2_mp(a1) == pytest.approx(
        float(mp.expm1(4 * a1) / (4 * a1))
    )


def test_leakage_B_is_positive_and_increases_with_t0() -> None:
    b1 = leakage_B_mp("0.1", "2")
    b2 = leakage_B_mp("0.1", "3")
    assert b1 > 0
    assert b2 > b1


def test_raw_integral_floor_increases_with_cutoff() -> None:
    C = mp.mpf("10")
    p = mp.mpf("1")
    C0 = mp.mpf("4")
    B = mp.mpf("3")
    f10 = raw_integral_floor(C, p, C0, B, 10)
    f100 = raw_integral_floor(C, p, C0, B, 100)
    assert f100 > f10


def test_explicit_high_mode_certificate_hits_requested_floor() -> None:
    cert = explicit_high_mode_certificate(
        a0="0.05",
        a1="0.06",
        target_mu="0.1",
        C_margin="0.25",
    )
    assert cert.pass_floor
    assert mp.mpf(cert.certified_raw_integral_floor) >= mp.mpf("0.1")
    assert int(cert.cutoff_N) >= 1


def test_high_mode_receipt_is_source_level_only() -> None:
    receipt = high_mode_gate_receipt("0.05", "0.06", "0.1")
    assert receipt["source_level_gate_pass"] is True
    assert receipt["proof_of_rh"] is False
    assert (
        "repository-to-Suzuki localized operator/domain/Friedrichs join"
        in receipt["open"]
    )


def test_invalid_high_mode_inputs_fail_closed() -> None:
    with pytest.raises(ValueError):
        explicit_high_mode_certificate("1", "1", "0.1")
    with pytest.raises(ValueError):
        raw_integral_floor("2", "1", "1", "1", 0)
