from __future__ import annotations

import math

import pytest

from secret_of_a_half.c005_yoshida_constants import (
    c1_majorant_c_eq_2,
    c2_majorant_c_eq_2,
    choose_constant_envelope,
    constant_gate_receipt,
)


def test_c1_majorant_is_five_sixths() -> None:
    assert c1_majorant_c_eq_2() == pytest.approx(5.0 / 6.0)


def test_c2_majorant_has_correct_small_window_limit() -> None:
    tiny = 1e-8
    value = c2_majorant_c_eq_2(tiny)
    assert value == pytest.approx(1.0, rel=1e-7)


def test_c2_majorant_is_monotone_on_positive_windows() -> None:
    values = [c2_majorant_c_eq_2(a1) for a1 in (0.1, 0.2, 0.5, 1.0)]
    assert values == sorted(values)


def test_constant_envelope_satisfies_source_gate_strictly() -> None:
    env = choose_constant_envelope(0.5, 1.0, safety_margin=0.25)
    assert env.pass_source_gate
    assert env.source_inequality_margin == pytest.approx(0.25)
    assert env.bulk_coefficient > env.target_mu


def test_constant_receipt_keeps_gamma_gate_open() -> None:
    receipt = constant_gate_receipt(0.5, 1.0)
    assert receipt["source_gate_pass"] is True
    assert receipt["proof_of_rh"] is False
    assert "rigorous gamma-tail threshold t0 for the chosen C" in receipt["open"]
    assert "rigorous compact gamma maximum C0 on |z|<=t0" in receipt["open"]


def test_invalid_constant_parameters_fail_closed() -> None:
    with pytest.raises(ValueError):
        c2_majorant_c_eq_2(0.0)
    with pytest.raises(ValueError):
        choose_constant_envelope(0.5, 0.0)
    with pytest.raises(ValueError):
        choose_constant_envelope(0.5, 1.0, safety_margin=0.0)
