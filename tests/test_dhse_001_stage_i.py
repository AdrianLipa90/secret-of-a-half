from fractions import Fraction
import json
from pathlib import Path

from secret_of_a_half.dhse_001_stage_i import (
    EXPECTED_MAP_COUNT,
    LENGTHS,
    SCALE,
    admissible_maps,
    run_stage_i,
    words_of_length,
)


def _canonicalize_rational_pairs(value):
    """Reduce legacy two-integer exact-rational pairs recursively.

    Stage I contains no two-integer coefficient vectors: every two-integer list
    in its receipt schema is an exact rational pair.  This migration therefore
    preserves value while removing the historical non-reduced serialization.
    """
    if isinstance(value, dict):
        return {key: _canonicalize_rational_pairs(item) for key, item in value.items()}
    if isinstance(value, list):
        if len(value) == 2 and all(type(item) is int for item in value) and value[1] != 0:
            fraction = Fraction(value[0], value[1])
            return [fraction.numerator, fraction.denominator]
        return [_canonicalize_rational_pairs(item) for item in value]
    return value


def test_word_sets_are_complete() -> None:
    assert LENGTHS == (1, 2, 3, 4)
    for length in LENGTHS:
        words = words_of_length(length)
        assert len(words) == 2**length
        assert len(set(words)) == len(words)
        assert all(len(word) == length for word in words)


def test_complete_k6_universe_is_used() -> None:
    assert SCALE == 6
    assert len(admissible_maps(SCALE)) == EXPECTED_MAP_COUNT == 1073


def test_length_two_reproduces_stage_g_profile() -> None:
    receipt = run_stage_i()
    length_two = next(row for row in receipt["length_census"] if row["length"] == 2)
    assert [row["forcing_count"] for row in length_two["centre_scan"]] == [
        302,
        4366,
        45644,
        156190,
        367516,
        156190,
        45644,
        4366,
        302,
    ]


def test_every_declared_length_passes_frozen_gate() -> None:
    receipt = run_stage_i()
    assert receipt["technical_status"] == "PASS"
    assert receipt["scientific_status"] == "WORD_LENGTH_ROBUST_HALF_EXCESS"
    assert receipt["primary_rule"]["pass_by_length"] == {
        "1": True,
        "2": True,
        "3": True,
        "4": True,
    }
    for row in receipt["length_census"]:
        assert row["target"]["strict_first"] is True
        assert row["target"]["ratio_pass"] is True
        assert row["symmetry"]["reciprocal_centre_counts_equal"] is True


def test_target_rate_is_nondecreasing_over_declared_lengths() -> None:
    receipt = run_stage_i()
    rates = [Fraction(*value) for value in receipt["secondary"]["target_rate_sequence"]]
    assert rates == sorted(rates)
    assert receipt["secondary"]["target_rate_trend"] == "NONDECREASING"


def test_persisted_stage_i_receipt_is_semantically_reproducible_after_v07_migration() -> None:
    root = Path(__file__).resolve().parents[1]
    persisted = json.loads(
        (root / "data" / "processed" / "dhse_001_stage_i_receipt.json").read_text(encoding="utf-8")
    )
    repair = json.loads(
        (root / "data" / "processed" / "DHSE_001_RECEIPT_REPAIR_V0_7.json").read_text(encoding="utf-8")
    )["stage_i"]
    current = run_stage_i()

    assert _canonicalize_rational_pairs(persisted) == _canonicalize_rational_pairs(current)
    assert repair["status"] == "LEGACY_NONCANONICAL_RATIONAL_SERIALIZATION"
    assert repair["historical_receipt_overwritten"] is False
    assert repair["scientific_status_changed"] is False
    assert _canonicalize_rational_pairs(repair["example"]["legacy_pair"]) == repair["example"]["canonical_pair"]
