"""DHSE-001 Stage I: preregistered word-length robustness audit."""
from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from itertools import product

import numpy as np

from .dhse_001_stage_f import CENTRES, PASS_RATIO
from .dhse_001_stage_g import admissible_maps, reciprocal_conjugate_tuple

SCALE = 6
LENGTHS = (1, 2, 3, 4)
RADIUS = Fraction(1, 10)
EXPECTED_MAP_COUNT = 1073
TARGET_INDEX = CENTRES.index(Fraction(1))


def _pair(value: Fraction) -> list[int]:
    return [value.numerator, value.denominator]


def words_of_length(length: int) -> tuple[str, ...]:
    if length < 1:
        raise ValueError("word length must be positive")
    return tuple("".join(bits) for bits in product("LR", repeat=length))


def _left_multiply(
    matrix: tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray],
    current: tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray],
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    a, b, c, d = matrix
    A, B, C, D = current
    return (
        a * A + b * C,
        a * B + b * D,
        c * A + d * C,
        c * B + d * D,
    )


def _word_matrix(
    word: str,
    left: tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray],
    right: tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray],
    size: int,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    current = (
        np.ones((1, 1), dtype=np.int64),
        np.zeros((1, 1), dtype=np.int64),
        np.zeros((1, 1), dtype=np.int64),
        np.ones((1, 1), dtype=np.int64),
    )
    for letter in word:
        current = _left_multiply(left if letter == "L" else right, current)
    return tuple(np.broadcast_to(entry, (size, size)) for entry in current)


def _force_counts(
    matrix: tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray],
) -> list[int]:
    A, B, C, D = matrix
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


def length_census(length: int) -> dict[str, object]:
    maps = admissible_maps(SCALE)
    size = len(maps)
    a, b, c, d = (maps[:, index] for index in range(4))
    left = (a[None, :], b[None, :], c[None, :], d[None, :])
    right = (a[:, None], b[:, None], c[:, None], d[:, None])

    words = words_of_length(length)
    word_counts: dict[str, list[int]] = {}
    totals = [0] * len(CENTRES)
    for word in words:
        counts = _force_counts(_word_matrix(word, left, right, size))
        word_counts[word] = counts
        totals = [left_count + right_count for left_count, right_count in zip(totals, counts)]

    event_count = len(words) * size * size
    controls = sorted(
        totals[index]
        for index in range(len(CENTRES))
        if index != TARGET_INDEX
    )
    median_control = Fraction(controls[3] + controls[4], 2)
    target_count = totals[TARGET_INDEX]
    ratio = None if median_control == 0 else Fraction(target_count, 1) / median_control
    strict_first = all(
        target_count > totals[index]
        for index in range(len(CENTRES))
        if index != TARGET_INDEX
    )
    ratio_pass = target_count > 0 if median_control == 0 else ratio is not None and ratio >= PASS_RATIO
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
                    word: word_counts[word][index] for word in words
                },
            }
        )

    return {
        "length": length,
        "word_count": len(words),
        "ordered_pair_count": size * size,
        "pair_word_event_count": event_count,
        "centre_scan": rows,
        "target": {
            "forcing_count": target_count,
            "forcing_rate": _pair(Fraction(target_count, event_count)),
            "median_control_count": _pair(median_control),
            "target_to_control_median_ratio": None if ratio is None else _pair(ratio),
            "strict_first": strict_first,
            "ratio_pass": ratio_pass,
            "length_pass": strict_first and ratio_pass and reciprocal_counts_equal,
        },
        "symmetry": {
            "reciprocal_centre_counts_equal": reciprocal_counts_equal,
        },
    }


@lru_cache(maxsize=1)
def run_stage_i() -> dict[str, object]:
    maps = admissible_maps(SCALE)
    map_tuples = {tuple(int(value) for value in row) for row in maps.tolist()}
    reciprocal_closed = all(
        reciprocal_conjugate_tuple(matrix) in map_tuples for matrix in map_tuples
    )
    lengths = [length_census(length) for length in LENGTHS]
    pass_by_length = {
        row["length"]: bool(row["target"]["length_pass"]) for row in lengths
    }

    if all(pass_by_length.values()):
        conclusion = "WORD_LENGTH_ROBUST_HALF_EXCESS"
    elif not pass_by_length[1] and all(pass_by_length[length] for length in (2, 3, 4)):
        conclusion = "MULTISTEP_HALF_EXCESS"
    elif sum(pass_by_length.values()) >= 2:
        conclusion = "PARTIAL_WORD_LENGTH_PERSISTENCE"
    else:
        conclusion = "WORD_LENGTH_UNSTABLE"

    target_rates = [Fraction(*row["target"]["forcing_rate"]) for row in lengths]
    nondecreasing = all(
        target_rates[index] >= target_rates[index - 1]
        for index in range(1, len(target_rates))
    )
    technical_pass = (
        len(maps) == EXPECTED_MAP_COUNT
        and reciprocal_closed
        and all(
            row["word_count"] == 2 ** row["length"]
            and row["ordered_pair_count"] == EXPECTED_MAP_COUNT ** 2
            and row["pair_word_event_count"] == (2 ** row["length"]) * EXPECTED_MAP_COUNT ** 2
            and row["symmetry"]["reciprocal_centre_counts_equal"]
            for row in lengths
        )
    )

    return {
        "experiment": "DHSE-001",
        "stage": "I-preregistered-word-length-robustness",
        "parameters": {
            "scale": SCALE,
            "map_count": len(maps),
            "lengths": list(LENGTHS),
            "radius": _pair(RADIUS),
            "centres_odds": [_pair(centre) for centre in CENTRES],
            "pass_ratio": _pair(PASS_RATIO),
        },
        "length_census": lengths,
        "primary_rule": {
            "pass_by_length": {str(key): value for key, value in pass_by_length.items()},
            "conclusion": conclusion,
        },
        "secondary": {
            "target_rate_sequence": [_pair(rate) for rate in target_rates],
            "target_rate_trend": "NONDECREASING" if nondecreasing else "NON_MONOTONE",
        },
        "symmetry": {
            "reciprocal_universe_closed": reciprocal_closed,
        },
        "technical_status": "PASS" if technical_pass else "FAIL",
        "scientific_status": conclusion,
        "interpretation_boundary": (
            "Persistence is established only for all binary words of lengths 1..4 "
            "in the complete uniform K=6 positive integer Möbius universe at "
            "projective radius 1/10. No all-length or all-operator theorem is claimed."
        ),
    }
