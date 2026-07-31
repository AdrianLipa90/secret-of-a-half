import json
from pathlib import Path
from fractions import Fraction

from secret_of_a_half.dhse_001_stage_l import dense_centres, run_stage_l


def test_dense_grid_is_exact_and_reciprocal() -> None:
    centres = dense_centres()
    assert len(centres) == 43
    assert centres[0] == Fraction(1, 8)
    assert centres[-1] == Fraction(8)
    assert centres[len(centres) // 2] == Fraction(1)
    assert all(1 / centre in centres for centre in centres)


def test_half_is_unique_maximum_at_both_lengths() -> None:
    receipt = run_stage_l()
    assert receipt["technical_status"] == "PASS"
    assert receipt["scientific_status"] == "DENSE_GRID_UNIQUE_HALF_MAXIMUM"
    assert receipt["primary_rule"]["both_lengths_pass"] is True
    for row in receipt["length_census"]:
        assert row["target"]["strict_first"] is True
        assert row["target"]["ratio_pass"] is True
        assert row["symmetry"]["reciprocal_centre_counts_equal"] is True


def test_exact_runner_up_locations_are_recorded() -> None:
    receipt = run_stage_l()
    length_two = next(row for row in receipt["length_census"] if row["length"] == 2)
    length_four = next(row for row in receipt["length_census"] if row["length"] == 4)
    assert length_two["target"]["runner_up_centres"] == [[6, 7], [7, 6]]
    assert length_two["target"]["runner_up_count"] == 292386
    assert length_four["target"]["runner_up_centres"] == [[5, 6], [6, 5]]
    assert length_four["target"]["runner_up_count"] == 2175168


def test_dense_profiles_are_not_falsely_marked_unimodal() -> None:
    receipt = run_stage_l()
    for row in receipt["length_census"]:
        assert row["secondary"]["globally_unimodal"] is False
        assert len(row["secondary"]["local_maxima"]) > 1


def test_persisted_stage_l_receipt_is_reproducible() -> None:
    root = Path(__file__).resolve().parents[1]
    persisted = json.loads(
        (root / "data" / "processed" / "dhse_001_stage_l_receipt.json").read_text(encoding="utf-8")
    )
    assert persisted == run_stage_l()
