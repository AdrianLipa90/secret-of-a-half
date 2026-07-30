from __future__ import annotations

import math
from pathlib import Path

import pytest

from secret_of_a_half.zero_undefined_duality import (
    DEFINED_ZERO,
    UNDEFINED_BOTTOM,
    ZeroUndefinedProgram,
    amplitude_state,
    binary_entropy,
    classify_implementation_value,
    complement,
    conjugacy_residual,
    fisher_rao_distance,
    inverse_odds,
    projective_odds,
    reciprocal,
    run_duality_audit,
    self_dual_probability,
)

ROOT = Path(__file__).resolve().parents[1]
PROGRAM_PATH = ROOT / "construction" / "phasenav" / "secret_of_half_zero_undefined_duality.pnv"


def program() -> ZeroUndefinedProgram:
    return ZeroUndefinedProgram.load(PROGRAM_PATH)


def test_native_profile_keeps_nan_out_of_arithmetic() -> None:
    profile = program()
    assert profile.equations["LEFT_VERTEX"] == DEFINED_ZERO
    assert profile.equations["RIGHT_VERTEX"] == UNDEFINED_BOTTOM
    assert "NAN" in profile.equations["NAN_BOUNDARY"]
    assert profile.equations["NO_PROMOTION"].endswith("DOES_NOT_PROVE_RH")


def test_complement_is_an_involution() -> None:
    for p in (0.0, 0.01, 0.25, 0.5, 0.8, 1.0):
        assert abs(complement(complement(p)) - p) < 1e-15


def test_odds_conjugates_complement_to_reciprocal() -> None:
    for p in (0.0, 0.01, 0.1, 0.25, 0.5, 0.75, 0.99, 1.0):
        assert conjugacy_residual(p) < 1e-14


def test_extended_endpoints_are_swapped() -> None:
    assert projective_odds(0.0) == 0.0
    assert math.isinf(projective_odds(1.0))
    assert math.isinf(reciprocal(0.0))
    assert reciprocal(math.inf) == 0.0
    assert inverse_odds(0.0) == 0.0
    assert inverse_odds(math.inf) == 1.0


def test_half_is_unique_self_dual_weight_and_swap_fixed_state() -> None:
    p = self_dual_probability()
    assert p == 0.5
    assert complement(p) == p
    assert projective_odds(p) == 1.0
    state = amplitude_state(p)
    assert abs(state[0] - state[1]) < 1e-15
    assert abs(sum(value * value for value in state) - 1.0) < 1e-15


def test_half_is_fisher_rao_midpoint() -> None:
    left = fisher_rao_distance(0.0, 0.5)
    right = fisher_rao_distance(0.5, 1.0)
    assert abs(left - math.pi / 2.0) < 1e-15
    assert abs(right - math.pi / 2.0) < 1e-15
    assert abs(fisher_rao_distance(0.0, 1.0) - math.pi) < 1e-15


def test_entropy_alignment() -> None:
    assert abs(binary_entropy(0.5) - math.log(2.0)) < 1e-15
    for p in (0.0, 0.1, 0.25, 0.75, 0.9, 1.0):
        assert binary_entropy(p) <= binary_entropy(0.5) + 1e-15


def test_nan_is_only_an_implementation_marker() -> None:
    marker = float("nan")
    assert classify_implementation_value(marker) == UNDEFINED_BOTTOM
    assert classify_implementation_value(0.0) == DEFINED_ZERO
    with pytest.raises(ValueError):
        projective_odds(marker)
    with pytest.raises(ValueError):
        reciprocal(marker)


def test_receipt_is_internally_consistent() -> None:
    receipt = run_duality_audit(program())
    assert receipt["ieee_nan_is_numeric_endpoint"] is False
    assert receipt["max_conjugacy_residual"] < 1e-14
    assert receipt["self_dual"]["p"] == 0.5
    assert receipt["fisher_rao"]["midpoint_residual"] < 1e-14
    assert receipt["claim_boundary"]["proof_of_rh"] is False
