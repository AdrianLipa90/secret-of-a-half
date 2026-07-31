"""DHSE-001 Stage G: exact coefficient-scale persistence audit."""
from __future__ import annotations

from fractions import Fraction
from functools import lru_cache

import numpy as np

from .dhse_001_stage_f import CENTRES, PASS_RATIO, WORDS

SCALES = (1, 2, 3, 4, 5, 6)
EXPECTED_MAP_COUNTS = {1: 3, 2: 25, 3: 96, 4: 256, 5: 563, 6: 1073}
TARGET_INDEX = CENTRES.index(Fraction(1))


def admissible_maps(scale: int) -> np.ndarray:
    if scale < 1:
        raise ValueError("scale must be positive")
    maps = []
    for a in range(1, scale + 1):
        for b in range(0, scale + 1):
            for c in range(0, scale + 1):
                for d in range(1, scale + 1):
                    if a * d - b * c > 0:
                        maps.append((a, b, c, d))
    return np.asarray(maps, dtype=np.int64)


def reciprocal_conjugate_tuple(
    matrix: tuple[int, int, int, int],
) -> tuple[int, int, int, int]:
    a, b, c, d = matrix
    return (d, c, b, a)


def _force_counts(
    A: np.ndarray,
    B: np.ndarray,
    C: np.ndarray,
    D: np.ndarray,
) -> list[int]:
    counts = []
    for centre in CENTRES:
        qn, qd = centre.numerator, centre.denominator
        mask = (
            (B * 11 * qd >= 9 * qn * D)
            & (C > 0)
            & (A * 9 * qd <= 11 * qn * C)
        )
        counts.append(int(np.count_nonzero(mask)))
    return counts


def _pair(value: Fraction) -> list[int]:
    return [value.numerator, value.denominator]


def scale_census(scale: int) -> dict[str, object]:
    maps = admissible_maps(scale)
    count = len(maps)
    a, b, c, d = (maps[:, index] for index in range(4))

    square_counts = _force_counts(
        a * a + b * c,
        a * b + b * d,
        c * a + d * c,
        c * b + d * d,
    )
    same_branch = [value * count for value in square_counts]

    ar, br, cr, dr = (column[:, None] for column in (a, b, c, d))
    al, bl, cl, dl = (column[None, :] for column in (a, b, c, d))
    mixed = _force_counts(
        ar * al + br * cl,
        ar * bl + br * dl,
        cr * al + dr * cl,
        cr * bl + dr * dl,
    )

    word_counts = {
        "LL": same_branch,
        "LR": mixed,
        "RL": list(mixed),
        "RR": list(same_branch),
    }
    totals = [
        sum(word_counts[word][index] for word in WORDS)
        for index in range(len(CENTRES))
    ]
    event_count = 4 * count * count
    controls = sorted(
        totals[index]
        for index in range(len(CENTRES))
        if index != TARGET_INDEX
    )
    median_control = Fraction(controls[3] + controls[4], 2)
    target_count = totals[TARGET_INDEX]
    target_ratio = (
        None
        if median_control == 0
        else Fraction(target_count, 1) / median_control
    )
    strict_first = all(
        target_count > totals[index]
        for index in range(len(CENTRES))
        if index != TARGET_INDEX
    )

    map_tuples = {
        tuple(int(value) for value in row) for row in maps.tolist()
    }
    reciprocal_closed = all(
        reciprocal_conjugate_tuple(matrix) in map_tuples
        for matrix in map_tuples
    )
    reciprocal_counts_equal = all(
        totals[index] == totals[len(CENTRES) - 1 - index]
        for index in range(len(CENTRES))
    )

    rows = []
    for index, centre in enumerate(CENTRES):
        total = totals[index]
        rows.append(
            {
                "odds": _pair(centre),
                "forcing_count": total,
                "forcing_rate": _pair(Fraction(total, event_count)),
                "rank": 1 + sum(other > total for other in totals),
                "word_counts": {
                    word: word_counts[word][index] for word in WORDS
                },
            }
        )

    return {
        "scale": scale,
        "map_count": count,
        "ordered_pair_count": count * count,
        "pair_word_event_count": event_count,
        "centre_scan": rows,
        "target": {
            "forcing_count": target_count,
            "forcing_rate": _pair(Fraction(target_count, event_count)),
            "median_control_count": _pair(median_control),
            "target_to_control_median_ratio": (
                None if target_ratio is None else _pair(target_ratio)
            ),
            "strict_first": strict_first,
        },
        "symmetry": {
            "reciprocal_universe_closed": reciprocal_closed,
            "reciprocal_centre_counts_equal": reciprocal_counts_equal,
        },
    }


@lru_cache(maxsize=1)
def run_stage_g() -> dict[str, object]:
    scales = [scale_census(scale) for scale in SCALES]
    by_scale = {row["scale"]: row for row in scales}

    strict_first_all = all(
        by_scale[scale]["target"]["strict_first"]
        for scale in range(2, 7)
    )
    ratio_pass_all = all(
        Fraction(
            *by_scale[scale]["target"][
                "target_to_control_median_ratio"
            ]
        )
        >= PASS_RATIO
        for scale in range(3, 7)
    )
    rate_4 = Fraction(*by_scale[4]["target"]["forcing_rate"])
    rate_6 = Fraction(*by_scale[6]["target"]["forcing_rate"])
    anti_collapse = rate_6 >= Fraction(1, 2) * rate_4
    zero_at_scale = any(
        by_scale[scale]["target"]["forcing_count"] == 0
        for scale in range(2, 7)
    )

    if zero_at_scale:
        conclusion = "NO_HALF_FORCING_AT_SCALE"
    elif strict_first_all and ratio_pass_all and anti_collapse:
        conclusion = "SCALE_PERSISTENT_HALF_EXCESS"
    elif strict_first_all and ratio_pass_all:
        conclusion = "FINITE_CUBE_DECAY"
    else:
        conclusion = "SCALE_UNSTABLE"

    technical_pass = all(
        row["map_count"] == EXPECTED_MAP_COUNTS[row["scale"]]
        and row["ordered_pair_count"] == row["map_count"] ** 2
        and row["pair_word_event_count"] == 4 * row["map_count"] ** 2
        and row["symmetry"]["reciprocal_universe_closed"]
        and row["symmetry"]["reciprocal_centre_counts_equal"]
        for row in scales
    )

    successive = []
    previous = None
    for row in scales:
        current = Fraction(*row["target"]["forcing_rate"])
        successive.append(
            {
                "scale": row["scale"],
                "rate": _pair(current),
                "ratio_to_previous": (
                    None
                    if previous in (None, 0)
                    else _pair(current / previous)
                ),
            }
        )
        previous = current

    increasing = all(
        Fraction(*successive[index]["rate"])
        >= Fraction(*successive[index - 1]["rate"])
        for index in range(1, len(successive))
    )

    return {
        "experiment": "DHSE-001",
        "stage": "G-preregistered-coefficient-scale-persistence",
        "scales": scales,
        "primary_rule": {
            "strict_first_K2_to_K6": strict_first_all,
            "ratio_at_least_5_over_4_K3_to_K6": ratio_pass_all,
            "rate_K6_at_least_half_rate_K4": anti_collapse,
            "rate_K4": _pair(rate_4),
            "rate_K6": _pair(rate_6),
            "rate_K6_to_K4": _pair(rate_6 / rate_4),
            "conclusion": conclusion,
        },
        "secondary": {
            "target_rate_sequence": successive,
            "trend": (
                "INCREASING_OVER_DECLARED_SCALES"
                if increasing
                else "NON_MONOTONE"
            ),
        },
        "technical_status": "PASS" if technical_pass else "FAIL",
        "scientific_status": conclusion,
        "interpretation_boundary": (
            "Persistence is established only for complete coefficient cubes "
            "K=1..6, the four two-letter words and projective radius 1/10. "
            "No extrapolation to all coefficients, all word lengths or all "
            "deterministic dynamics is made."
        ),
    }
