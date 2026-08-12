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
from secret_of_a_half.receipt_provenance import canonicalize_stage_i_receipt


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


def test_persisted_stage_i_receipt_is_exact_after_rational_canonicalization() -> None:
    root = Path(__file__).resolve().parents[1]
    persisted = json.loads(
        (root / "data" / "processed" / "dhse_001_stage_i_receipt.json").read_text(encoding="utf-8")
    )
    current = run_stage_i()

    # The historical JSON contains a few unreduced rational pairs.  The runtime
    # uses Fraction and emits their reduced forms.  Canonicalize only the
    # schema-declared rational fields; all counts, words, gates and statuses must
    # still compare byte-for-byte as JSON values after that exact reduction.
    assert canonicalize_stage_i_receipt(persisted) == canonicalize_stage_i_receipt(current)
