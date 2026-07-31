import json
from pathlib import Path

from secret_of_a_half.dhse_001_stage_e import (
    BASE_LEFT,
    BASE_RIGHT,
    admissible,
    coefficient_neighbours,
    run_stage_e,
)


def test_base_pair_is_admissible_and_neighbourhood_counts_are_exact() -> None:
    assert admissible(BASE_LEFT)
    assert admissible(BASE_RIGHT)
    assert len(coefficient_neighbours(BASE_LEFT)) == 41
    assert len(coefficient_neighbours(BASE_RIGHT)) == 75


def test_stage_e_exact_counts_and_fraction() -> None:
    receipt = run_stage_e()
    counts = receipt["counts"]
    assert receipt["technical_status"] == "PASS"
    assert receipt["status"] == "EXPLORATORY_NOT_PREREGISTERED"
    assert counts["admissible_pairs"] == 3075
    assert counts["universal_lr_forcing_pairs"] == 145
    assert counts["forcing_fraction"] == [29, 615]
    assert counts["forcing_counts_by_l1_distance"] == {
        "0": 1,
        "1": 1,
        "2": 7,
        "3": 19,
        "4": 28,
        "5": 39,
        "6": 32,
        "7": 15,
        "8": 3,
    }


def test_nearest_nonbase_persistence_is_one_coefficient_step() -> None:
    receipt = run_stage_e()
    nearest = receipt["nearest_nonbase_persistence"]
    assert nearest["minimum_l1_distance"] == 1
    assert nearest["examples"] == [
        {
            "left": [1, 1, 2, 3],
            "right": [4, 1, 1, 2],
            "composition": [6, 7, 5, 7],
            "image": [[1, 1], [6, 5]],
            "l1_distance_from_base_pair": 1,
        }
    ]


def test_stage_e_conclusion_is_sparse_local_persistence() -> None:
    receipt = run_stage_e()
    assert receipt["summary"] == {
        "base_pair_is_isolated": False,
        "forcing_is_generic_in_local_neighbourhood": False,
        "conclusion": "LOCALLY_PERSISTENT_BUT_SPARSE",
    }
    assert receipt["scientific_status"] == "EXPLORATORY_SENSITIVITY_ONLY"


def test_persisted_stage_e_receipt_is_reproducible() -> None:
    root = Path(__file__).resolve().parents[1]
    persisted = json.loads(
        (root / "data" / "processed" / "dhse_001_stage_e_receipt.json").read_text(
            encoding="utf-8"
        )
    )
    assert persisted == run_stage_e()
