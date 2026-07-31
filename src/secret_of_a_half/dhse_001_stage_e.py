"""DHSE-001 Stage E: exploratory exact coefficient-neighbourhood audit."""
from __future__ import annotations

from fractions import Fraction
from itertools import product

from .dhse_001_stage_d import (
    Matrix,
    compose,
    positive_line_image,
    target_ball,
    universally_forces_target,
)

BASE_LEFT: Matrix = (1, 1, 2, 3)
BASE_RIGHT: Matrix = (3, 1, 1, 2)
DELTA = 1


def determinant(matrix: Matrix) -> int:
    a, b, c, d = matrix
    return a * d - b * c


def admissible(matrix: Matrix) -> bool:
    a, b, c, d = matrix
    return a > 0 and b >= 0 and c >= 0 and d > 0 and determinant(matrix) > 0


def coefficient_neighbours(base: Matrix, delta: int = DELTA) -> tuple[Matrix, ...]:
    if delta < 0:
        raise ValueError("delta must be non-negative")
    ranges = tuple(
        range(max(0, coefficient - delta), coefficient + delta + 1)
        for coefficient in base
    )
    return tuple(values for values in product(*ranges) if admissible(values))


def l1_distance(left: Matrix, right: Matrix) -> int:
    return sum(abs(a - b) for a, b in zip(left, right, strict=True))


def pair_distance(left: Matrix, right: Matrix) -> int:
    return l1_distance(left, BASE_LEFT) + l1_distance(right, BASE_RIGHT)


def _fraction_pair(value: Fraction) -> list[int]:
    return [value.numerator, value.denominator]


def run_stage_e() -> dict[str, object]:
    left_candidates = coefficient_neighbours(BASE_LEFT)
    right_candidates = coefficient_neighbours(BASE_RIGHT)
    passing: list[dict[str, object]] = []
    by_distance: dict[int, int] = {}

    for left in left_candidates:
        for right in right_candidates:
            composition = compose(right, left)
            if universally_forces_target(composition):
                lower, upper = positive_line_image(composition)
                assert upper is not None
                distance = pair_distance(left, right)
                by_distance[distance] = by_distance.get(distance, 0) + 1
                passing.append(
                    {
                        "left": list(left),
                        "right": list(right),
                        "composition": list(composition),
                        "image": [_fraction_pair(lower), _fraction_pair(upper)],
                        "l1_distance_from_base_pair": distance,
                    }
                )

    total_pairs = len(left_candidates) * len(right_candidates)
    forcing_count = len(passing)
    forcing_fraction = Fraction(forcing_count, total_pairs)
    nonbase = [row for row in passing if row["l1_distance_from_base_pair"] > 0]
    nearest_distance = min(row["l1_distance_from_base_pair"] for row in nonbase)
    nearest_examples = [
        row for row in nonbase
        if row["l1_distance_from_base_pair"] == nearest_distance
    ]

    expected_counts = {
        "left_candidates": 41,
        "right_candidates": 75,
        "total_pairs": 3075,
        "forcing_pairs": 145,
    }
    technical_pass = (
        len(left_candidates) == expected_counts["left_candidates"]
        and len(right_candidates) == expected_counts["right_candidates"]
        and total_pairs == expected_counts["total_pairs"]
        and forcing_count == expected_counts["forcing_pairs"]
    )

    lower, upper = target_ball()
    return {
        "experiment": "DHSE-001",
        "stage": "E-exploratory-coefficient-neighbourhood",
        "status": "EXPLORATORY_NOT_PREREGISTERED",
        "parameters": {
            "base_left": list(BASE_LEFT),
            "base_right": list(BASE_RIGHT),
            "coefficient_delta": DELTA,
            "target_ball": [_fraction_pair(lower), _fraction_pair(upper)],
            "admissibility": "a>0,b>=0,c>=0,d>0,ad-bc>0",
        },
        "counts": {
            "admissible_left_matrices": len(left_candidates),
            "admissible_right_matrices": len(right_candidates),
            "admissible_pairs": total_pairs,
            "universal_lr_forcing_pairs": forcing_count,
            "forcing_fraction": _fraction_pair(forcing_fraction),
            "forcing_counts_by_l1_distance": {
                str(distance): by_distance[distance]
                for distance in sorted(by_distance)
            },
        },
        "nearest_nonbase_persistence": {
            "minimum_l1_distance": nearest_distance,
            "examples": nearest_examples,
        },
        "summary": {
            "base_pair_is_isolated": False,
            "forcing_is_generic_in_local_neighbourhood": False,
            "conclusion": "LOCALLY_PERSISTENT_BUT_SPARSE",
        },
        "technical_status": "PASS" if technical_pass else "FAIL",
        "scientific_status": "EXPLORATORY_SENSITIVITY_ONLY",
        "interpretation_boundary": (
            "The LR whole-line forcing mechanism persists for a minority of "
            "admissible integer coefficient perturbations around the selected "
            "Möbius pair. This is local structural persistence, not an "
            "operator-independent halfway law."
        ),
    }
