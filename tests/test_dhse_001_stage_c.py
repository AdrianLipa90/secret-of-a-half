from fractions import Fraction
import json
from pathlib import Path

from secret_of_a_half.dhse_001 import LEFT, RIGHT
from secret_of_a_half.dhse_001_stage_b import RADIUS, TARGET, projective_residual
from secret_of_a_half.dhse_001_stage_c import (
    lr_composition,
    lr_residual,
    mobius_skew_family,
    run_stage_c,
)


def test_lr_composition_formula_matches_operator_pair() -> None:
    family = mobius_skew_family()
    for z in (Fraction(1, 17), Fraction(2, 3), Fraction(1), Fraction(9, 4), Fraction(31, 5)):
        direct = family.apply(family.apply(z, LEFT), RIGHT)
        assert direct == lr_composition(z)


def test_lr_word_always_falls_inside_target_radius() -> None:
    for z in (Fraction(1, 1000), Fraction(1, 7), Fraction(1), Fraction(1000)):
        image = lr_composition(z)
        assert Fraction(6, 7) < image < 1
        assert projective_residual(image, TARGET) == lr_residual(z)
        assert lr_residual(z) < Fraction(1, 13) < RADIUS


def test_stage_c_closes_observed_mobius_signal_exactly() -> None:
    receipt = run_stage_c()
    audit = receipt["audit"]
    assert receipt["technical_status"] == "PASS"
    assert receipt["scientific_status"] == "OPERATOR_WORD_ARTIFACT_IDENTIFIED"
    assert audit["target_hits"] == 5147
    assert audit["lr_words"] == 5147
    assert audit["hit_iff_lr_matches"] == audit["observed_states"]
    assert audit["counterexamples"] == []


def test_persisted_stage_c_receipt_is_reproducible() -> None:
    root = Path(__file__).resolve().parents[1]
    persisted = json.loads(
        (root / "data" / "processed" / "dhse_001_stage_c_receipt.json").read_text(encoding="utf-8")
    )
    assert persisted == run_stage_c()
