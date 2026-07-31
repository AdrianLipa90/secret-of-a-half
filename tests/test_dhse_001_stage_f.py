from fractions import Fraction
import json
from pathlib import Path

from secret_of_a_half.dhse_001_stage_f import (
    CENTRES,
    TARGET,
    admissible_maps,
    compose_word,
    forces_centre,
    reciprocal_conjugate,
    run_stage_f,
    target_interval,
)


def test_frozen_universe_has_declared_size_and_reciprocal_closure() -> None:
    maps = admissible_maps()
    assert len(maps) == 256
    map_set = set(maps)
    assert all(reciprocal_conjugate(matrix) in map_set for matrix in maps)


def test_word_order_matches_left_to_right_application() -> None:
    left = (1, 1, 2, 3)
    right = (3, 1, 1, 2)
    assert compose_word(left, right, "LR") == (5, 6, 5, 7)


def test_target_interval_and_exact_forcing_boundary() -> None:
    assert target_interval(Fraction(1)) == (Fraction(9, 11), Fraction(11, 9))
    assert forces_centre((9, 9, 11, 11), Fraction(1))
    assert not forces_centre((1, 0, 0, 1), Fraction(1))


def test_stage_f_passes_frozen_primary_gate() -> None:
    receipt = run_stage_f()
    primary = receipt["primary_statistic"]
    assert receipt["technical_status"] == "PASS"
    assert receipt["scientific_status"] == "CENTRE_BLIND_HALF_EXCESS"
    assert primary["target_odds"] == [TARGET.numerator, TARGET.denominator]
    assert primary["target_forcing_count"] == 15104
    assert primary["median_control_count"] == [945, 1]
    assert primary["target_to_control_median_ratio"] == [15104, 945]
    assert primary["strict_first"] is True
    assert primary["ratio_pass"] is True


def test_reciprocal_centre_counts_are_exactly_symmetric() -> None:
    receipt = run_stage_f()
    rows = {
        Fraction(*row["odds"]): row["forcing_count"]
        for row in receipt["centre_scan"]
    }
    assert tuple(rows) == CENTRES
    for centre in CENTRES:
        assert rows[centre] == rows[1 / centre]
    assert rows[Fraction(1)] == 15104
    assert rows[Fraction(1, 2)] == rows[Fraction(2)] == 6712


def test_persisted_stage_f_receipt_is_reproducible() -> None:
    root = Path(__file__).resolve().parents[1]
    persisted = json.loads(
        (root / "data" / "processed" / "dhse_001_stage_f_receipt.json").read_text(
            encoding="utf-8"
        )
    )
    assert persisted == run_stage_f()
