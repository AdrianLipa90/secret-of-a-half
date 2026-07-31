from fractions import Fraction
import json
from pathlib import Path

from secret_of_a_half.dhse_001_stage_j import primitive_maps
from secret_of_a_half.dhse_001_stage_k import (
    MEASURE_NAMES,
    UNIFORM_REFERENCE_RATES,
    map_weights,
    run_stage_k,
)


def test_all_declared_weights_are_positive() -> None:
    weights = map_weights(primitive_maps())
    assert tuple(weights) == MEASURE_NAMES
    assert all((values > 0).all() for values in weights.values())


def test_weight_ranges_are_exact() -> None:
    receipt = run_stage_k()
    assert receipt["weight_ranges"] == {
        "uniform": {"minimum": 1, "maximum": 1, "sum": 952},
        "determinant": {"minimum": 1, "maximum": 36, "sum": 10219},
        "determinant_squared": {"minimum": 1, "maximum": 1296, "sum": 172197},
        "coefficient_sum": {"minimum": 2, "maximum": 23, "sum": 11690},
        "boundary_taper": {"minimum": 1, "maximum": 6, "sum": 1827},
        "low_determinant_taper": {"minimum": 1, "maximum": 36, "sum": 25005},
    }


def test_all_measure_length_cells_pass() -> None:
    receipt = run_stage_k()
    assert receipt["technical_status"] == "PASS"
    assert receipt["scientific_status"] == "MEASURE_ROBUST_HALF_EXCESS"
    assert receipt["primary_rule"]["all_measure_length_cells_pass"] is True
    assert receipt["primary_rule"]["all_anti_collapse_comparisons_pass"] is True
    for length in receipt["length_census"]:
        for measure in length["measures"]:
            assert measure["target"]["strict_first"] is True
            assert measure["target"]["ratio_pass"] is True
            assert measure["target"]["anti_collapse_pass"] is True
            assert measure["symmetry"]["reciprocal_centre_masses_equal"] is True


def test_determinant_squared_length_two_profile_is_exact() -> None:
    receipt = run_stage_k()
    length_two = next(row for row in receipt["length_census"] if row["length"] == 2)
    measure = next(row for row in length_two["measures"] if row["measure"] == "determinant_squared")
    assert measure["centre_masses"] == [
        81260,
        1926286,
        141383378,
        872888370,
        3164153256,
        872888370,
        141383378,
        1926286,
        81260,
    ]


def test_every_weighted_target_rate_clears_anti_collapse_threshold() -> None:
    receipt = run_stage_k()
    for length in receipt["length_census"]:
        reference = UNIFORM_REFERENCE_RATES[length["length"]]
        for measure in length["measures"]:
            weighted = Fraction(*measure["target"]["weighted_rate"])
            assert weighted >= Fraction(1, 4) * reference


def test_persisted_stage_k_receipt_is_reproducible() -> None:
    root = Path(__file__).resolve().parents[1]
    persisted = json.loads(
        (root / "data" / "processed" / "dhse_001_stage_k_receipt.json").read_text(encoding="utf-8")
    )
    assert persisted == run_stage_k()
