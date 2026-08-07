from fractions import Fraction
import json
from pathlib import Path

import pytest

from secret_of_a_half.dhse_001_stage_m import (
    LENGTHS,
    endpoint_census,
    exact_sweep,
    int64_safety_certificate,
    reciprocal_endpoint_symmetry,
    run_stage_m,
)


def test_int64_certificate_covers_declared_stage_m_lengths() -> None:
    certificates = [int64_safety_certificate(length) for length in LENGTHS]
    assert all(row["safe"] for row in certificates)

    length_four = int64_safety_certificate(4)
    assert length_four["matrix_entry_bound"] == 20736
    assert length_four["comparison_product_bound"] == 52027785216
    assert length_four["comparison_product_bound"] < length_four["int64_max"]


def test_int64_certificate_rejects_unproved_large_word_length() -> None:
    certificate = int64_safety_certificate(8)
    assert certificate["safe"] is False
    assert certificate["comparison_product_bound"] > certificate["int64_max"]

    # Exercise the actual public census path: refusal must occur before any
    # pair-word enumeration can start on uncertified fixed-width arithmetic.
    with pytest.raises(OverflowError, match="not certified safe"):
        endpoint_census(8)


def test_exact_sweep_distinguishes_symmetry_from_central_maximum() -> None:
    # Two reciprocal intervals, [1/2, 2/3] and [3/2, 2], leave q=1 outside
    # the forcing set while preserving exact endpoint reciprocity.
    starts = {
        (1, 2): 1,
        (3, 2): 1,
    }
    ends = {
        (2, 3): 1,
        (2, 1): 1,
    }
    result = exact_sweep(starts, ends)
    assert result["maximum"] == 1
    assert result["q1_count"] == 0
    assert result["q1_is_global_maximum"] is False
    assert reciprocal_endpoint_symmetry(starts, ends)


def test_exact_sweep_finds_unique_self_dual_point() -> None:
    starts = {(1, 1): 7}
    ends = {(1, 1): 7}
    result = exact_sweep(starts, ends)
    assert result["maximum"] == 7
    assert result["q1_count"] == 7
    assert result["q1_is_unique_global_maximum"] is True
    assert result["maximizer_components"] == [
        {
            "left": [1, 1],
            "right": [1, 1],
            "left_closed": True,
            "right_closed": True,
        }
    ]


def test_stage_m_exact_length_classification() -> None:
    receipt = run_stage_m()
    assert receipt["technical_status"] == "PASS"
    assert receipt["scientific_status"] == (
        "CONTINUOUS_MAXIMUM_CLASSIFIED_WITH_LENGTH_DEPENDENT_SPLITTING"
    )
    assert receipt["summary"]["unique_self_dual_global_maximum_lengths"] == [2, 3]
    assert receipt["summary"]["reciprocal_split_maximum_lengths"] == [1, 4]

    by_length = {row["length"]: row for row in receipt["length_theorems"]}
    assert by_length[2]["sweep"]["maximizer_components"] == [
        {
            "left": [1, 1],
            "right": [1, 1],
            "left_closed": True,
            "right_closed": True,
        }
    ]
    assert by_length[3]["sweep"]["maximizer_components"] == [
        {
            "left": [1, 1],
            "right": [1, 1],
            "left_closed": True,
            "right_closed": True,
        }
    ]
    assert by_length[4]["sweep"]["maximum"] == 2224570
    assert by_length[4]["sweep"]["q1_count"] == 2219236
    assert Fraction(9882, 9911) < Fraction(341, 342) < 1
    assert 1 < Fraction(342, 341) < Fraction(9911, 9882)


def test_persisted_stage_m_receipt_is_reproducible() -> None:
    root = Path(__file__).resolve().parents[1]
    persisted = json.loads(
        (root / "data" / "processed" / "dhse_001_stage_m_receipt.json").read_text(
            encoding="utf-8"
        )
    )
    assert persisted == run_stage_m()
