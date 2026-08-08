from fractions import Fraction
import json
from pathlib import Path

from secret_of_a_half.dhse_001_stage_b import (
    CENTRES,
    FAMILIES,
    RADIUS,
    TARGET,
    projective_residual,
    reciprocal_conjugacy_matches,
    run_stage_b,
)
from secret_of_a_half.dhse_001_stage_b_receipt import compact_stage_b_receipt


def test_centres_are_reciprocal_and_target_is_central() -> None:
    assert TARGET == Fraction(1)
    assert CENTRES == tuple(reversed(tuple(1 / value for value in CENTRES)))
    assert CENTRES[len(CENTRES) // 2] == TARGET


def test_projective_residual_is_exact_and_scale_symmetric() -> None:
    assert projective_residual(Fraction(3, 2), Fraction(1)) == Fraction(1, 5)
    assert projective_residual(Fraction(2, 3), Fraction(1)) == Fraction(1, 5)
    assert projective_residual(Fraction(3, 2), Fraction(3, 4)) == Fraction(1, 3)


def test_experimental_families_are_not_reciprocal_conjugate() -> None:
    samples = (Fraction(1, 7), Fraction(2, 3), Fraction(1), Fraction(9, 4), Fraction(31, 5))
    for family in FAMILIES:
        matches = reciprocal_conjugacy_matches(family, samples)
        if family.calibration_only:
            assert matches == 2 * len(samples)
        else:
            assert matches < 2 * len(samples)


def test_stage_b_is_deterministic_and_exactly_parameterized() -> None:
    left = run_stage_b()
    right = run_stage_b()
    assert left == right
    assert left["technical_status"] == "PASS"
    assert left["parameters"]["radius"] == [RADIUS.numerator, RADIUS.denominator]
    assert len(left["families"]) == len(FAMILIES)
    assert left["scientific_status"] in {
        "ROBUST_HALF_EFFECT",
        "FAMILY_DEPENDENT",
        "NO_ROBUST_HALF_EFFECT",
    }


def test_zero_control_median_rule_is_explicit_in_receipt() -> None:
    receipt = run_stage_b()
    mobius = next(row for row in receipt["families"] if row["family"] == "mobius_skew")
    stat = mobius["primary_statistic"]
    if stat["control_median_occupancy"] == [0, 1]:
        assert stat["target_occupancy"] != [0, 1]
        assert stat["family_pass"] is stat["strict_first"]


def test_persisted_stage_b_projection_is_reproducible_with_hash_migration() -> None:
    root = Path(__file__).resolve().parents[1]
    persisted = json.loads(
        (root / "data" / "processed" / "dhse_001_stage_b_receipt.json").read_text(encoding="utf-8")
    )
    repair = json.loads(
        (root / "data" / "processed" / "DHSE_001_RECEIPT_REPAIR_V0_7.json").read_text(encoding="utf-8")
    )["stage_b"]
    current = compact_stage_b_receipt()

    historical_hash = persisted.pop("full_receipt_sha256")
    current_hash = current.pop("full_receipt_sha256")

    # The compact scientific/technical projection is reproducible.  The old
    # full-receipt digest is preserved as historical provenance rather than
    # silently rewritten after the mismatch was discovered.
    assert persisted == current
    assert historical_hash == repair["historical_full_receipt_sha256"]
    assert current_hash == repair["current_recomputed_full_receipt_sha256"]
    assert historical_hash != current_hash
    assert repair["historical_receipt_overwritten"] is False
    assert repair["scientific_status_changed"] is False
