"""DHSE-001 Stage J: preregistered projective-quotient robustness audit."""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
from functools import lru_cache
from math import gcd

import numpy as np

from .dhse_001_stage_f import CENTRES, PASS_RATIO
from .dhse_001_stage_g import admissible_maps, reciprocal_conjugate_tuple
from .dhse_001_stage_i import (
    LENGTHS,
    RADIUS,
    SCALE,
    _force_counts,
    _pair,
    _word_matrix,
    words_of_length,
)

EXPECTED_FULL_MAP_COUNT = 1073
EXPECTED_PRIMITIVE_MAP_COUNT = 952
TARGET_INDEX = CENTRES.index(Fraction(1))
FULL_TARGET_RATES = {
    1: Fraction(13, 1073),
    2: Fraction(91879, 1151329),
    3: Fraction(562921, 4605316),
    4: Fraction(167131, 1151329),
}


def coefficient_gcd(matrix: tuple[int, int, int, int]) -> int:
    value = 0
    for coefficient in matrix:
        value = gcd(value, coefficient)
    return value


def primitive_maps(scale: int = SCALE) -> np.ndarray:
    maps = admissible_maps(scale)
    primitive = [
        tuple(int(value) for value in row)
        for row in maps.tolist()
        if coefficient_gcd(tuple(int(value) for value in row)) == 1
    ]
    return np.asarray(primitive, dtype=np.int64)


def scalar_multiplicity_distribution(scale: int = SCALE) -> dict[int, int]:
    distribution: Counter[int] = Counter()
    for row in primitive_maps(scale).tolist():
        maximum = max(int(value) for value in row)
        distribution[scale // maximum] += 1
    return dict(sorted(distribution.items()))


def length_census(length: int) -> dict[str, object]:
    maps = primitive_maps(SCALE)
    size = len(maps)
    a, b, c, d = (maps[:, index] for index in range(4))
    left = (a[None, :], b[None, :], c[None, :], d[None, :])
    right = (a[:, None], b[:, None], c[:, None], d[:, None])

    words = words_of_length(length)
    totals = [0] * len(CENTRES)
    word_counts: dict[str, list[int]] = {}
    for word in words:
        counts = _force_counts(_word_matrix(word, left, right, size))
        word_counts[word] = counts
        totals = [a_count + b_count for a_count, b_count in zip(totals, counts)]

    event_count = len(words) * size * size
    controls = sorted(
        totals[index]
        for index in range(len(CENTRES))
        if index != TARGET_INDEX
    )
    median_control = Fraction(controls[3] + controls[4], 2)
    target_count = totals[TARGET_INDEX]
    target_rate = Fraction(target_count, event_count)
    full_rate = FULL_TARGET_RATES[length]
    primitive_to_full = target_rate / full_rate
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
            "forcing_rate": _pair(target_rate),
            "full_representative_rate": _pair(full_rate),
            "primitive_to_full_rate_ratio": _pair(primitive_to_full),
            "median_control_count": _pair(median_control),
            "target_to_control_median_ratio": None if ratio is None else _pair(ratio),
            "strict_first": strict_first,
            "ratio_pass": ratio_pass,
            "anti_collapse_pass": primitive_to_full >= Fraction(1, 2),
            "length_pass": strict_first and ratio_pass and reciprocal_counts_equal,
        },
        "symmetry": {
            "reciprocal_centre_counts_equal": reciprocal_counts_equal,
        },
    }


@lru_cache(maxsize=1)
def run_stage_j() -> dict[str, object]:
    full = admissible_maps(SCALE)
    primitive = primitive_maps(SCALE)
    primitive_tuples = {
        tuple(int(value) for value in row) for row in primitive.tolist()
    }
    reciprocal_closed = all(
        reciprocal_conjugate_tuple(matrix) in primitive_tuples
        for matrix in primitive_tuples
    )
    lengths = [length_census(length) for length in LENGTHS]
    all_length_gates = all(row["target"]["length_pass"] for row in lengths)
    anti_collapse = all(row["target"]["anti_collapse_pass"] for row in lengths)

    if all_length_gates and anti_collapse:
        conclusion = "PROJECTIVE_QUOTIENT_ROBUST_HALF_EXCESS"
    elif all_length_gates:
        conclusion = "PROJECTIVE_QUOTIENT_HALF_EXCESS_WITH_RATE_SHIFT"
    else:
        conclusion = "SCALAR_MULTIPLICITY_DEPENDENT"

    distribution = scalar_multiplicity_distribution(SCALE)
    reconstructed_full_count = sum(
        multiplicity * primitive_count
        for multiplicity, primitive_count in distribution.items()
    )
    technical_pass = (
        len(full) == EXPECTED_FULL_MAP_COUNT
        and len(primitive) == EXPECTED_PRIMITIVE_MAP_COUNT
        and reconstructed_full_count == len(full)
        and reciprocal_closed
        and all(
            row["word_count"] == 2 ** row["length"]
            and row["ordered_pair_count"] == len(primitive) ** 2
            and row["pair_word_event_count"] == (2 ** row["length"]) * len(primitive) ** 2
            and row["symmetry"]["reciprocal_centre_counts_equal"]
            for row in lengths
        )
    )

    return {
        "experiment": "DHSE-001",
        "stage": "J-preregistered-projective-quotient-robustness",
        "parameters": {
            "scale": SCALE,
            "full_map_count": len(full),
            "primitive_map_count": len(primitive),
            "removed_scalar_representatives": len(full) - len(primitive),
            "lengths": list(LENGTHS),
            "radius": _pair(RADIUS),
            "centres_odds": [_pair(centre) for centre in CENTRES],
            "pass_ratio": _pair(PASS_RATIO),
        },
        "scalar_multiplicity_distribution": {
            str(key): value for key, value in distribution.items()
        },
        "length_census": lengths,
        "primary_rule": {
            "all_length_gates_pass": all_length_gates,
            "anti_collapse_all_lengths": anti_collapse,
            "conclusion": conclusion,
        },
        "symmetry": {
            "primitive_universe_reciprocal_closed": reciprocal_closed,
        },
        "technical_status": "PASS" if technical_pass else "FAIL",
        "scientific_status": conclusion,
        "interpretation_boundary": (
            "Scalar multiplicity is removed only inside the bounded primitive K=6 "
            "integer Möbius lattice for word lengths 1..4 and radius 1/10. "
            "No all-map, all-length or measure-independent theorem is claimed."
        ),
    }
