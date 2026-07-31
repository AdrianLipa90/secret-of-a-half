"""DHSE-001 Stage H: exact radius-robustness audit at coefficient scale K=6."""
from __future__ import annotations

from fractions import Fraction
from functools import lru_cache

import numpy as np

from .dhse_001_stage_f import CENTRES, PASS_RATIO, WORDS
from .dhse_001_stage_g import admissible_maps, reciprocal_conjugate_tuple

SCALE = 6
RADII = (
    Fraction(1, 40), Fraction(1, 30), Fraction(1, 20), Fraction(1, 15),
    Fraction(1, 10), Fraction(1, 8), Fraction(1, 6), Fraction(1, 5),
)
TARGET_INDEX = CENTRES.index(Fraction(1))
EXPECTED_MAP_COUNT = 1073
EXPECTED_EVENT_COUNT = 4605316


def _pair(value: Fraction) -> list[int]:
    return [value.numerator, value.denominator]


def target_interval(
    centre: Fraction,
    radius: Fraction,
) -> tuple[Fraction, Fraction]:
    q = Fraction(centre)
    r = Fraction(radius)
    if q <= 0 or not 0 < r < 1:
        raise ValueError("centre must be positive and radius must lie in (0,1)")
    return q * (1 - r) / (1 + r), q * (1 + r) / (1 - r)


def _force_counts(
    A: np.ndarray,
    B: np.ndarray,
    C: np.ndarray,
    D: np.ndarray,
    radius: Fraction,
) -> list[int]:
    rn, rd = radius.numerator, radius.denominator
    counts = []
    for centre in CENTRES:
        qn, qd = centre.numerator, centre.denominator
        mask = (
            (B * qd * (rd + rn) >= qn * (rd - rn) * D)
            & (C > 0)
            & (A * qd * (rd - rn) <= qn * (rd + rn) * C)
        )
        counts.append(int(np.count_nonzero(mask)))
    return counts


@lru_cache(maxsize=1)
def run_stage_h() -> dict[str, object]:
    maps = admissible_maps(SCALE)
    map_count = len(maps)
    a, b, c, d = (maps[:, index] for index in range(4))

    square = (
        a * a + b * c,
        a * b + b * d,
        c * a + d * c,
        c * b + d * d,
    )
    ar, br, cr, dr = (column[:, None] for column in (a, b, c, d))
    al, bl, cl, dl = (column[None, :] for column in (a, b, c, d))
    mixed = (
        ar * al + br * cl,
        ar * bl + br * dl,
        cr * al + dr * cl,
        cr * bl + dr * dl,
    )

    map_tuples = {
        tuple(int(value) for value in row) for row in maps.tolist()
    }
    reciprocal_closed = all(
        reciprocal_conjugate_tuple(matrix) in map_tuples
        for matrix in map_tuples
    )

    radius_rows = []
    all_positive = True
    all_strict_first = True
    all_ratio_pass = True
    all_symmetry = True

    for radius in RADII:
        square_counts = _force_counts(*square, radius)
        same_branch = [value * map_count for value in square_counts]
        mixed_counts = _force_counts(*mixed, radius)
        word_counts = {
            "LL": same_branch,
            "LR": mixed_counts,
            "RL": list(mixed_counts),
            "RR": list(same_branch),
        }
        totals = [
            sum(word_counts[word][index] for word in WORDS)
            for index in range(len(CENTRES))
        ]
        controls = sorted(
            totals[index]
            for index in range(len(CENTRES))
            if index != TARGET_INDEX
        )
        median_control = Fraction(controls[3] + controls[4], 2)
        target_count = totals[TARGET_INDEX]
        ratio = (
            None
            if median_control == 0
            else Fraction(target_count, 1) / median_control
        )
        strict_first = all(
            target_count > totals[index]
            for index in range(len(CENTRES))
            if index != TARGET_INDEX
        )
        ratio_pass = (
            target_count > 0
            if median_control == 0
            else ratio is not None and ratio >= PASS_RATIO
        )
        symmetry = totals == list(reversed(totals))

        centre_rows = []
        for index, centre in enumerate(CENTRES):
            interval = target_interval(centre, radius)
            total = totals[index]
            centre_rows.append(
                {
                    "odds": _pair(centre),
                    "target_interval": [
                        _pair(interval[0]),
                        _pair(interval[1]),
                    ],
                    "forcing_count": total,
                    "forcing_rate": _pair(
                        Fraction(total, EXPECTED_EVENT_COUNT)
                    ),
                    "rank": 1 + sum(other > total for other in totals),
                    "word_counts": {
                        word: word_counts[word][index] for word in WORDS
                    },
                }
            )

        radius_rows.append(
            {
                "radius": _pair(radius),
                "centre_scan": centre_rows,
                "target": {
                    "forcing_count": target_count,
                    "forcing_rate": _pair(
                        Fraction(target_count, EXPECTED_EVENT_COUNT)
                    ),
                    "median_control_count": _pair(median_control),
                    "target_to_control_median_ratio": (
                        None if ratio is None else _pair(ratio)
                    ),
                    "positive": target_count > 0,
                    "strict_first": strict_first,
                    "ratio_pass": ratio_pass,
                },
                "reciprocal_centre_counts_equal": symmetry,
            }
        )
        all_positive = all_positive and target_count > 0
        all_strict_first = all_strict_first and strict_first
        all_ratio_pass = all_ratio_pass and ratio_pass
        all_symmetry = all_symmetry and symmetry

    if not all_positive:
        conclusion = "NO_HALF_FORCING_AT_RADIUS"
    elif all_positive and all_strict_first and all_ratio_pass:
        conclusion = "RADIUS_ROBUST_HALF_EXCESS"
    elif not all_strict_first:
        conclusion = "RADIUS_UNSTABLE"
    else:
        conclusion = "RADIUS_LOCAL_HALF_EXCESS"

    target_counts = [row["target"]["forcing_count"] for row in radius_rows]
    monotone = all(
        target_counts[index] >= target_counts[index - 1]
        for index in range(1, len(target_counts))
    )
    technical_pass = (
        map_count == EXPECTED_MAP_COUNT
        and 4 * map_count * map_count == EXPECTED_EVENT_COUNT
        and reciprocal_closed
        and all_symmetry
    )

    return {
        "experiment": "DHSE-001",
        "stage": "H-preregistered-radius-robustness",
        "universe": {
            "scale": SCALE,
            "map_count": map_count,
            "ordered_pair_count": map_count * map_count,
            "pair_word_event_count_per_radius": EXPECTED_EVENT_COUNT,
            "words": list(WORDS),
        },
        "radii": radius_rows,
        "primary_rule": {
            "positive_all_radii": all_positive,
            "strict_first_all_radii": all_strict_first,
            "ratio_pass_all_radii": all_ratio_pass,
            "conclusion": conclusion,
        },
        "secondary": {
            "target_counts_monotone_with_radius": monotone,
            "target_count_sequence": target_counts,
        },
        "symmetry_audit": {
            "reciprocal_universe_closed": reciprocal_closed,
            "reciprocal_centre_counts_equal_all_radii": all_symmetry,
        },
        "technical_status": "PASS" if technical_pass else "FAIL",
        "scientific_status": conclusion,
        "interpretation_boundary": (
            "Radius robustness is established only for the eight declared "
            "radii, the complete K=6 coefficient cube and two-letter words."
        ),
    }
