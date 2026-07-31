"""DHSE-001 Stage L: preregistered dense rational centre scan."""
from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from math import gcd

import numpy as np

from .dhse_001_stage_f import PASS_RATIO
from .dhse_001_stage_i import RADIUS, _pair, _word_matrix, words_of_length
from .dhse_001_stage_j import EXPECTED_PRIMITIVE_MAP_COUNT, primitive_maps

LENGTHS = (2, 4)
TARGET = Fraction(1)
EXPECTED_CENTRE_COUNT = 43


def dense_centres(bound: int = 8) -> tuple[Fraction, ...]:
    if bound < 1:
        raise ValueError("centre bound must be positive")
    return tuple(
        sorted(
            {
                Fraction(numerator, denominator)
                for numerator in range(1, bound + 1)
                for denominator in range(1, bound + 1)
                if gcd(numerator, denominator) == 1
            }
        )
    )


def _force_counts(
    matrix: tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray],
    centres: tuple[Fraction, ...],
) -> list[int]:
    A, B, C, D = matrix
    counts = []
    for centre in centres:
        qn, qd = centre.numerator, centre.denominator
        mask = (
            (B * 11 * qd >= 9 * qn * D)
            & (C > 0)
            & (A * 9 * qd <= 11 * qn * C)
        )
        counts.append(int(np.count_nonzero(mask)))
    return counts


def _local_maxima(
    centres: tuple[Fraction, ...], counts: list[int]
) -> list[dict[str, object]]:
    maxima = []
    for index in range(1, len(counts) - 1):
        current = counts[index]
        if (
            current >= counts[index - 1]
            and current >= counts[index + 1]
            and (current > counts[index - 1] or current > counts[index + 1])
        ):
            maxima.append(
                {
                    "odds": _pair(centres[index]),
                    "forcing_count": current,
                }
            )
    return maxima


def length_census(length: int) -> dict[str, object]:
    centres = dense_centres()
    target_index = centres.index(TARGET)
    maps = primitive_maps()
    size = len(maps)
    a, b, c, d = (maps[:, index] for index in range(4))
    left = (a[None, :], b[None, :], c[None, :], d[None, :])
    right = (a[:, None], b[:, None], c[:, None], d[:, None])
    words = words_of_length(length)

    totals = [0] * len(centres)
    target_word_counts: dict[str, int] = {}
    for word in words:
        counts = _force_counts(_word_matrix(word, left, right, size), centres)
        totals = [previous + current for previous, current in zip(totals, counts)]
        target_word_counts[word] = counts[target_index]

    target_count = totals[target_index]
    control_values = [
        total for index, total in enumerate(totals) if index != target_index
    ]
    sorted_controls = sorted(control_values)
    median_control = Fraction(
        sorted_controls[len(sorted_controls) // 2 - 1]
        + sorted_controls[len(sorted_controls) // 2],
        2,
    )
    runner_count = max(control_values)
    runner_centres = [
        centres[index]
        for index, total in enumerate(totals)
        if index != target_index and total == runner_count
    ]
    target_to_median = Fraction(target_count, 1) / median_control
    target_to_runner = Fraction(target_count, runner_count)
    strict_first = target_count > runner_count
    ratio_pass = target_to_median >= PASS_RATIO
    reciprocal_equal = all(
        totals[index] == totals[len(centres) - 1 - index]
        for index in range(len(centres))
    )

    left_profile = totals[: target_index + 1]
    right_profile = totals[target_index:]
    left_nondecreasing = all(
        left_profile[index] >= left_profile[index - 1]
        for index in range(1, len(left_profile))
    )
    right_nonincreasing = all(
        right_profile[index] <= right_profile[index - 1]
        for index in range(1, len(right_profile))
    )

    return {
        "length": length,
        "word_count": len(words),
        "pair_word_event_count": len(words) * size * size,
        "forcing_counts": totals,
        "target_word_counts": target_word_counts,
        "target": {
            "forcing_count": target_count,
            "median_control_count": _pair(median_control),
            "runner_up_count": runner_count,
            "runner_up_centres": [_pair(centre) for centre in runner_centres],
            "target_to_control_median_ratio": _pair(target_to_median),
            "target_to_runner_up_ratio": _pair(target_to_runner),
            "strict_first": strict_first,
            "ratio_pass": ratio_pass,
            "length_pass": strict_first and ratio_pass and reciprocal_equal,
        },
        "symmetry": {
            "reciprocal_centre_counts_equal": reciprocal_equal,
        },
        "secondary": {
            "left_nondecreasing_to_half": left_nondecreasing,
            "right_nonincreasing_from_half": right_nonincreasing,
            "globally_unimodal": left_nondecreasing and right_nonincreasing,
            "local_maxima": _local_maxima(centres, totals),
        },
    }


@lru_cache(maxsize=1)
def run_stage_l() -> dict[str, object]:
    centres = dense_centres()
    lengths = [length_census(length) for length in LENGTHS]
    any_off_centre = any(
        not row["target"]["strict_first"]
        and any(
            count > row["target"]["forcing_count"]
            for index, count in enumerate(row["forcing_counts"])
            if centres[index] != TARGET
        )
        for row in lengths
    )
    any_tie = any(
        not row["target"]["strict_first"] and not any_off_centre
        for row in lengths
    )
    all_pass = all(row["target"]["length_pass"] for row in lengths)
    all_strict = all(row["target"]["strict_first"] for row in lengths)

    if all_pass:
        conclusion = "DENSE_GRID_UNIQUE_HALF_MAXIMUM"
    elif any_off_centre:
        conclusion = "DENSE_GRID_OFF_CENTRE_MAXIMUM"
    elif any_tie:
        conclusion = "DENSE_GRID_HALF_PLATEAU"
    elif all_strict:
        conclusion = "DENSE_GRID_RATIO_WEAK"
    else:
        conclusion = "DENSE_GRID_INDETERMINATE"

    reciprocal_closed = all(1 / centre in centres for centre in centres)
    technical_pass = (
        len(centres) == EXPECTED_CENTRE_COUNT
        and centres[0] == Fraction(1, 8)
        and centres[-1] == Fraction(8)
        and centres[len(centres) // 2] == TARGET
        and reciprocal_closed
        and len(primitive_maps()) == EXPECTED_PRIMITIVE_MAP_COUNT
        and all(
            row["word_count"] == 2 ** row["length"]
            and row["symmetry"]["reciprocal_centre_counts_equal"]
            for row in lengths
        )
    )

    return {
        "experiment": "DHSE-001",
        "stage": "L-preregistered-dense-rational-centre-scan",
        "parameters": {
            "primitive_map_count": EXPECTED_PRIMITIVE_MAP_COUNT,
            "lengths": list(LENGTHS),
            "radius": _pair(RADIUS),
            "centre_bound": 8,
            "centre_count": len(centres),
            "centres_odds": [_pair(centre) for centre in centres],
            "target_odds": _pair(TARGET),
            "pass_ratio": _pair(PASS_RATIO),
        },
        "length_census": lengths,
        "primary_rule": {
            "both_lengths_pass": all_pass,
            "conclusion": conclusion,
        },
        "symmetry": {
            "centre_grid_reciprocal_closed": reciprocal_closed,
        },
        "technical_status": "PASS" if technical_pass else "FAIL",
        "scientific_status": conclusion,
        "interpretation_boundary": (
            "The unique maximum is established only on the finite 43-point "
            "rational grid Q_8 for the primitive K=6 uniform measure, word "
            "lengths 2 and 4, and projective radius 1/10."
        ),
    }
