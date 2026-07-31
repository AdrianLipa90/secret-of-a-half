"""DHSE-001 Stage K: preregistered reciprocal-invariant measure audit."""
from __future__ import annotations

from fractions import Fraction
from functools import lru_cache

import numpy as np

from .dhse_001_stage_f import CENTRES, PASS_RATIO
from .dhse_001_stage_i import RADIUS, _pair, _word_matrix, words_of_length
from .dhse_001_stage_j import EXPECTED_PRIMITIVE_MAP_COUNT, primitive_maps

LENGTHS = (2, 4)
TARGET_INDEX = CENTRES.index(Fraction(1))
UNIFORM_REFERENCE_RATES = {
    2: Fraction(157345, 1812608),
    4: Fraction(554809, 3625216),
}
MEASURE_NAMES = (
    "uniform",
    "determinant",
    "determinant_squared",
    "coefficient_sum",
    "boundary_taper",
    "low_determinant_taper",
)


def map_weights(maps: np.ndarray) -> dict[str, np.ndarray]:
    a, b, c, d = (maps[:, index] for index in range(4))
    determinant = a * d - b * c
    return {
        "uniform": np.ones(len(maps), dtype=np.int64),
        "determinant": determinant.astype(np.int64),
        "determinant_squared": (determinant * determinant).astype(np.int64),
        "coefficient_sum": (a + b + c + d).astype(np.int64),
        "boundary_taper": (7 - np.max(maps, axis=1)).astype(np.int64),
        "low_determinant_taper": (37 - determinant).astype(np.int64),
    }


def _forcing_masks(
    matrix: tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray],
) -> list[np.ndarray]:
    A, B, C, D = matrix
    masks = []
    for centre in CENTRES:
        qn, qd = centre.numerator, centre.denominator
        masks.append(
            (B * 11 * qd >= 9 * qn * D)
            & (C > 0)
            & (A * 9 * qd <= 11 * qn * C)
        )
    return masks


def weighted_length_census(length: int) -> dict[str, object]:
    maps = primitive_maps()
    size = len(maps)
    a, b, c, d = (maps[:, index] for index in range(4))
    left = (a[None, :], b[None, :], c[None, :], d[None, :])
    right = (a[:, None], b[:, None], c[:, None], d[:, None])
    weights = map_weights(maps)
    pair_weights = {
        name: values[:, None] * values[None, :]
        for name, values in weights.items()
    }
    words = words_of_length(length)

    accumulators = {
        name: {
            "totals": [0] * len(CENTRES),
            "word_counts": {},
        }
        for name in MEASURE_NAMES
    }

    for word in words:
        masks = _forcing_masks(_word_matrix(word, left, right, size))
        for name in MEASURE_NAMES:
            pair_weight = pair_weights[name]
            counts = [
                int(pair_weight[mask].sum(dtype=np.int64)) for mask in masks
            ]
            accumulators[name]["word_counts"][word] = counts
            accumulators[name]["totals"] = [
                previous + current
                for previous, current in zip(
                    accumulators[name]["totals"], counts
                )
            ]

    measure_rows = []
    for name in MEASURE_NAMES:
        totals = accumulators[name]["totals"]
        map_weight_total = int(weights[name].sum(dtype=np.int64))
        total_mass = len(words) * map_weight_total * map_weight_total
        target_mass = totals[TARGET_INDEX]
        target_rate = Fraction(target_mass, total_mass)
        uniform_rate = UNIFORM_REFERENCE_RATES[length]
        weighted_to_uniform = target_rate / uniform_rate
        controls = sorted(
            totals[index]
            for index in range(len(CENTRES))
            if index != TARGET_INDEX
        )
        median_control = Fraction(controls[3] + controls[4], 2)
        ratio = None if median_control == 0 else Fraction(target_mass, 1) / median_control
        strict_first = all(
            target_mass > totals[index]
            for index in range(len(CENTRES))
            if index != TARGET_INDEX
        )
        ratio_pass = target_mass > 0 if median_control == 0 else ratio is not None and ratio >= PASS_RATIO
        reciprocal_equal = all(
            totals[index] == totals[len(CENTRES) - 1 - index]
            for index in range(len(CENTRES))
        )

        centre_rows = []
        for index, centre in enumerate(CENTRES):
            total = totals[index]
            centre_rows.append(
                {
                    "odds": _pair(centre),
                    "weighted_forcing_mass": total,
                    "weighted_rate": _pair(Fraction(total, total_mass)),
                    "rank": 1 + sum(other > total for other in totals),
                    "word_masses": {
                        word: accumulators[name]["word_counts"][word][index]
                        for word in words
                    },
                }
            )

        measure_rows.append(
            {
                "measure": name,
                "map_weight_total": map_weight_total,
                "pair_word_total_mass": total_mass,
                "centre_scan": centre_rows,
                "target": {
                    "weighted_forcing_mass": target_mass,
                    "weighted_rate": _pair(target_rate),
                    "uniform_reference_rate": _pair(uniform_rate),
                    "weighted_to_uniform_rate_ratio": _pair(weighted_to_uniform),
                    "median_control_mass": _pair(median_control),
                    "target_to_control_median_ratio": None if ratio is None else _pair(ratio),
                    "strict_first": strict_first,
                    "ratio_pass": ratio_pass,
                    "anti_collapse_pass": weighted_to_uniform >= Fraction(1, 4),
                    "cell_pass": strict_first and ratio_pass and reciprocal_equal,
                },
                "symmetry": {
                    "reciprocal_centre_masses_equal": reciprocal_equal,
                },
            }
        )

    return {
        "length": length,
        "word_count": len(words),
        "measures": measure_rows,
    }


@lru_cache(maxsize=1)
def run_stage_k() -> dict[str, object]:
    maps = primitive_maps()
    weights = map_weights(maps)
    index_by_matrix = {
        tuple(int(value) for value in row): index
        for index, row in enumerate(maps.tolist())
    }
    reciprocal_weight_invariance = {}
    for name, values in weights.items():
        reciprocal_weight_invariance[name] = all(
            int(values[index])
            == int(values[index_by_matrix[(matrix[3], matrix[2], matrix[1], matrix[0])]])
            for matrix, index in index_by_matrix.items()
        )

    lengths = [weighted_length_census(length) for length in LENGTHS]
    cells = [
        measure
        for length in lengths
        for measure in length["measures"]
    ]
    all_primary = all(measure["target"]["cell_pass"] for measure in cells)
    all_anti_collapse = all(
        measure["target"]["anti_collapse_pass"] for measure in cells
    )

    if all_primary and all_anti_collapse:
        conclusion = "MEASURE_ROBUST_HALF_EXCESS"
    elif all_primary:
        conclusion = "RANK_ROBUST_RATE_SENSITIVE"
    else:
        conclusion = "MEASURE_DEPENDENT_HALF_EXCESS"

    technical_pass = (
        len(maps) == EXPECTED_PRIMITIVE_MAP_COUNT
        and set(weights) == set(MEASURE_NAMES)
        and all(np.all(values > 0) for values in weights.values())
        and all(reciprocal_weight_invariance.values())
        and all(
            length["word_count"] == 2 ** length["length"]
            and all(
                measure["symmetry"]["reciprocal_centre_masses_equal"]
                for measure in length["measures"]
            )
            for length in lengths
        )
    )

    return {
        "experiment": "DHSE-001",
        "stage": "K-preregistered-reciprocal-invariant-measure-robustness",
        "parameters": {
            "primitive_map_count": len(maps),
            "lengths": list(LENGTHS),
            "measures": list(MEASURE_NAMES),
            "radius": _pair(RADIUS),
            "centres_odds": [_pair(centre) for centre in CENTRES],
            "pass_ratio": _pair(PASS_RATIO),
            "anti_collapse_fraction": [1, 4],
        },
        "weight_ranges": {
            name: {
                "minimum": int(values.min()),
                "maximum": int(values.max()),
                "sum": int(values.sum(dtype=np.int64)),
            }
            for name, values in weights.items()
        },
        "length_census": lengths,
        "primary_rule": {
            "all_measure_length_cells_pass": all_primary,
            "all_anti_collapse_comparisons_pass": all_anti_collapse,
            "conclusion": conclusion,
        },
        "symmetry": {
            "reciprocal_weight_invariance": reciprocal_weight_invariance,
        },
        "technical_status": "PASS" if technical_pass else "FAIL",
        "scientific_status": conclusion,
        "interpretation_boundary": (
            "Robustness is established only for the six declared positive "
            "reciprocal-invariant integer measures on the primitive K=6 universe, "
            "word lengths 2 and 4, and projective radius 1/10."
        ),
    }
