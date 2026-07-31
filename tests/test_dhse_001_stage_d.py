from fractions import Fraction
import json
from pathlib import Path

from secret_of_a_half.dhse_001_stage_d import (
    MAX_WORD_LENGTH,
    apply_matrix,
    census_family,
    derivative_at_target,
    fixes_target,
    positive_line_image,
    run_stage_d,
    target_ball,
    universally_forces_target,
    word_matrix,
)


def test_frozen_target_ball_is_exact() -> None:
    assert target_ball() == (Fraction(9, 11), Fraction(11, 9))


def test_affine_left_branch_is_the_minimal_q1_contraction() -> None:
    matrix = word_matrix("affine_skew", "L")
    assert fixes_target(matrix)
    assert derivative_at_target(matrix) == Fraction(2, 3)
    census = census_family("affine_skew")
    assert census["minimal_fixed_q1_words"][0]["word"] == "L"
    assert all(
        count == 1
        for count in census["fixed_q1_counts_by_length"].values()
    )


def test_mobius_lr_word_forces_entire_positive_line_into_target_ball() -> None:
    matrix = word_matrix("mobius_skew", "LR")
    assert matrix == (5, 6, 5, 7)
    assert positive_line_image(matrix) == (Fraction(6, 7), Fraction(1))
    assert universally_forces_target(matrix)
    for z in (Fraction(1, 1000), Fraction(1, 7), Fraction(1), Fraction(1000)):
        assert Fraction(9, 11) <= apply_matrix(matrix, z) <= Fraction(11, 9)


def test_scale_translate_has_no_finite_q1_or_forcing_word_in_census() -> None:
    census = census_family("scale_translate")
    assert census["minimal_fixed_q1_words"] == []
    assert census["minimal_universal_forcing_words"] == []
    assert len(census["fixed_q1_counts_by_length"]) == MAX_WORD_LENGTH
    for word in ("L", "R", "LR", "RLLR"):
        matrix = word_matrix("scale_translate", word)
        for z in (Fraction(1, 7), Fraction(1), Fraction(11, 3)):
            assert apply_matrix(matrix, z) > z


def test_collatz_rl_word_is_the_minimal_q1_contraction() -> None:
    matrix = word_matrix("collatz_stream", "RL")
    assert matrix == (3, 1, 0, 4)
    assert fixes_target(matrix)
    assert derivative_at_target(matrix) == Fraction(3, 4)
    for z in (Fraction(1, 7), Fraction(1), Fraction(13, 4)):
        assert apply_matrix(matrix, z) == 1 + Fraction(3, 4) * (z - 1)


def test_stage_d_conclusion_is_operator_local_not_universal() -> None:
    receipt = run_stage_d()
    assert receipt["technical_status"] == "PASS"
    assert receipt["scientific_status"] == "OPERATOR_LOCAL_MECHANISMS_IDENTIFIED"
    assert receipt["summary"]["shared_mechanism_across_all_families"] is False
    assert receipt["summary"]["conclusion"] == "NO_OPERATOR_INDEPENDENT_HALF_SELECTION"
    assert receipt["summary"]["families_with_finite_q1_fixed_words"] == [
        "affine_skew",
        "collatz_stream",
    ]
    assert receipt["summary"]["families_with_universal_target_forcing_words"] == [
        "mobius_skew"
    ]


def test_persisted_stage_d_receipt_is_reproducible() -> None:
    root = Path(__file__).resolve().parents[1]
    persisted = json.loads(
        (root / "data" / "processed" / "dhse_001_stage_d_receipt.json").read_text(
            encoding="utf-8"
        )
    )
    assert persisted == run_stage_d()
