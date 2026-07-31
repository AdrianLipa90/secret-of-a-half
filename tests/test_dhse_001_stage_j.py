from fractions import Fraction
import json
from pathlib import Path

from secret_of_a_half.dhse_001_stage_j import (
    EXPECTED_FULL_MAP_COUNT,
    EXPECTED_PRIMITIVE_MAP_COUNT,
    FULL_TARGET_RATES,
    coefficient_gcd,
    primitive_maps,
    run_stage_j,
    scalar_multiplicity_distribution,
)


def test_projective_normalization_counts() -> None:
    maps = primitive_maps()
    assert len(maps) == EXPECTED_PRIMITIVE_MAP_COUNT == 952
    assert EXPECTED_FULL_MAP_COUNT == 1073
    assert all(coefficient_gcd(tuple(int(value) for value in row)) == 1 for row in maps.tolist())


def test_scalar_multiplicity_reconstructs_full_universe() -> None:
    distribution = scalar_multiplicity_distribution()
    assert distribution == {1: 862, 2: 68, 3: 19, 6: 3}
    assert sum(multiplicity * count for multiplicity, count in distribution.items()) == 1073


def test_every_primitive_length_passes() -> None:
    receipt = run_stage_j()
    assert receipt["technical_status"] == "PASS"
    assert receipt["scientific_status"] == "PROJECTIVE_QUOTIENT_ROBUST_HALF_EXCESS"
    assert receipt["primary_rule"]["all_length_gates_pass"] is True
    assert receipt["primary_rule"]["anti_collapse_all_lengths"] is True
    for row in receipt["length_census"]:
        assert row["target"]["strict_first"] is True
        assert row["target"]["ratio_pass"] is True
        assert row["target"]["anti_collapse_pass"] is True
        assert row["symmetry"]["reciprocal_centre_counts_equal"] is True


def test_primitive_rates_do_not_collapse_against_stage_i() -> None:
    receipt = run_stage_j()
    for row in receipt["length_census"]:
        length = row["length"]
        primitive_rate = Fraction(*row["target"]["forcing_rate"])
        assert primitive_rate >= FULL_TARGET_RATES[length]


def test_length_two_primitive_profile_is_exact() -> None:
    receipt = run_stage_j()
    length_two = next(row for row in receipt["length_census"] if row["length"] == 2)
    assert [row["forcing_count"] for row in length_two["centre_scan"]] == [
        284,
        3984,
        39926,
        129312,
        314690,
        129312,
        39926,
        3984,
        284,
    ]


def test_persisted_stage_j_receipt_is_reproducible() -> None:
    root = Path(__file__).resolve().parents[1]
    persisted = json.loads(
        (root / "data" / "processed" / "dhse_001_stage_j_receipt.json").read_text(encoding="utf-8")
    )
    assert persisted == run_stage_j()
