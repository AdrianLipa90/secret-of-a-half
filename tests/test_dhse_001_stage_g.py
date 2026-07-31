from fractions import Fraction
import json
from pathlib import Path

from secret_of_a_half.dhse_001_stage_g import (
    EXPECTED_MAP_COUNTS,
    SCALES,
    admissible_maps,
    run_stage_g,
)


def test_declared_scale_map_counts_are_exact() -> None:
    assert tuple(EXPECTED_MAP_COUNTS) == SCALES
    for scale in SCALES:
        assert len(admissible_maps(scale)) == EXPECTED_MAP_COUNTS[scale]


def test_stage_g_reproduces_stage_f_at_scale_four() -> None:
    receipt = run_stage_g()
    scale_four = next(row for row in receipt["scales"] if row["scale"] == 4)
    counts = [row["forcing_count"] for row in scale_four["centre_scan"]]
    assert counts == [4, 104, 1786, 6712, 15104, 6712, 1786, 104, 4]
    assert scale_four["target"]["forcing_rate"] == [59, 1024]


def test_stage_g_passes_all_frozen_persistence_gates() -> None:
    receipt = run_stage_g()
    primary = receipt["primary_rule"]
    assert receipt["technical_status"] == "PASS"
    assert receipt["scientific_status"] == "SCALE_PERSISTENT_HALF_EXCESS"
    assert primary["strict_first_K2_to_K6"] is True
    assert primary["ratio_at_least_5_over_4_K3_to_K6"] is True
    assert primary["rate_K6_at_least_half_rate_K4"] is True
    assert primary["rate_K4"] == [59, 1024]
    assert primary["rate_K6"] == [91879, 1151329]
    assert Fraction(*primary["rate_K6_to_K4"]) > 1


def test_target_is_strictly_first_and_symmetry_holds_at_each_scale() -> None:
    receipt = run_stage_g()
    for row in receipt["scales"]:
        counts = [entry["forcing_count"] for entry in row["centre_scan"]]
        assert counts == list(reversed(counts))
        assert row["symmetry"]["reciprocal_universe_closed"] is True
        assert row["symmetry"]["reciprocal_centre_counts_equal"] is True
        if row["scale"] >= 2:
            assert counts[4] > max(counts[:4] + counts[5:])


def test_persisted_stage_g_receipt_is_reproducible() -> None:
    root = Path(__file__).resolve().parents[1]
    persisted = json.loads(
        (root / "data" / "processed" / "dhse_001_stage_g_receipt.json").read_text(
            encoding="utf-8"
        )
    )
    assert persisted == run_stage_g()
