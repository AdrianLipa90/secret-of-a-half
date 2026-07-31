from fractions import Fraction
import json
from pathlib import Path

from secret_of_a_half.dhse_001 import (
    LEFT,
    RIGHT,
    apply_branch,
    branch_stream,
    complement_branches,
    exact_duality_holds,
    initial_odds,
    reciprocal,
    run_experiment,
    trajectory,
)


def test_seed_is_deterministic_and_positive() -> None:
    assert initial_odds("alpha") == initial_odds("alpha")
    assert initial_odds("alpha") > 0
    assert initial_odds("alpha") != initial_odds("beta")


def test_branch_stream_is_deterministic() -> None:
    left = branch_stream("alpha")
    right = branch_stream("alpha")
    assert [next(left) for _ in range(512)] == [next(right) for _ in range(512)]


def test_reciprocal_conjugates_the_branch_pair() -> None:
    for z in (Fraction(1, 7), Fraction(2, 3), Fraction(1), Fraction(9, 4), Fraction(31, 5)):
        assert reciprocal(apply_branch(z, LEFT)) == apply_branch(reciprocal(z), RIGHT)
        assert reciprocal(apply_branch(z, RIGHT)) == apply_branch(reciprocal(z), LEFT)


def test_dual_trajectory_is_exact_at_every_step() -> None:
    branches = (LEFT, RIGHT, RIGHT, LEFT, LEFT, RIGHT) * 10
    z0 = Fraction(17, 29)
    primary = trajectory(z0, branches)
    dual = trajectory(reciprocal(z0), complement_branches(branches))
    assert exact_duality_holds(primary, dual)


def test_half_is_not_inserted_as_an_operator_constant() -> None:
    assert apply_branch(Fraction(2, 5), LEFT) == Fraction(2, 7)
    assert apply_branch(Fraction(2, 5), RIGHT) == Fraction(7, 5)


def test_declared_experiment_receipt_passes_technical_calibration() -> None:
    receipt = run_experiment()
    assert receipt["technical_status"] == "PASS"
    assert receipt["scientific_status"] == "CALIBRATION_ONLY"
    assert receipt["state_model"]["ieee_nan_in_state_space"] is False
    assert receipt["operator"]["uses_explicit_half_constant"] is False
    assert receipt["results"]["exact_duality_all_steps"] is True
    assert receipt["results"]["same_bits_control_duality_matches"] < receipt["results"]["same_bits_control_total_states"]


def test_persisted_receipt_is_reproducible() -> None:
    root = Path(__file__).resolve().parents[1]
    persisted = json.loads(
        (root / "data" / "processed" / "dhse_001_receipt.json").read_text(encoding="utf-8")
    )
    assert persisted == run_experiment()
