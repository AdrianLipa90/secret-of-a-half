from fractions import Fraction
import json
from pathlib import Path

from secret_of_a_half.dhse_001_stage_h import (
    RADII,
    run_stage_h,
    target_interval,
)


def test_declared_radius_sequence_and_interval_formula() -> None:
    assert RADII == (
        Fraction(1, 40), Fraction(1, 30), Fraction(1, 20), Fraction(1, 15),
        Fraction(1, 10), Fraction(1, 8), Fraction(1, 6), Fraction(1, 5),
    )
    assert target_interval(Fraction(1), Fraction(1, 10)) == (
        Fraction(9, 11), Fraction(11, 9)
    )


def test_stage_h_passes_all_frozen_radius_gates() -> None:
    receipt = run_stage_h()
    primary = receipt["primary_rule"]
    assert receipt["technical_status"] == "PASS"
    assert receipt["scientific_status"] == "RADIUS_ROBUST_HALF_EXCESS"
    assert primary["positive_all_radii"] is True
    assert primary["strict_first_all_radii"] is True
    assert primary["ratio_pass_all_radii"] is True


def test_target_count_sequence_is_exact_and_monotone() -> None:
    receipt = run_stage_h()
    assert receipt["secondary"]["target_count_sequence"] == [
        26544, 43140, 81864, 171608, 367516, 510480, 759680, 1018500
    ]
    assert receipt["secondary"]["target_counts_monotone_with_radius"] is True


def test_reciprocal_symmetry_and_strict_first_hold_at_each_radius() -> None:
    receipt = run_stage_h()
    for row in receipt["radii"]:
        counts = [entry["forcing_count"] for entry in row["centre_scan"]]
        assert counts == list(reversed(counts))
        assert counts[4] > max(counts[:4] + counts[5:])
        assert row["reciprocal_centre_counts_equal"] is True


def test_persisted_stage_h_receipt_is_reproducible() -> None:
    root = Path(__file__).resolve().parents[1]
    persisted = json.loads(
        (root / "data" / "processed" / "dhse_001_stage_h_receipt.json").read_text(
            encoding="utf-8"
        )
    )
    assert persisted == run_stage_h()
