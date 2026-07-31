"""DHSE-001 Stage F: preregistered centre-blind coefficient-cube census."""
from __future__ import annotations

from fractions import Fraction
from functools import lru_cache

COEFFICIENT_MAX = 4
CENTRES = (
    Fraction(1, 16), Fraction(1, 8), Fraction(1, 4), Fraction(1, 2),
    Fraction(1), Fraction(2), Fraction(4), Fraction(8), Fraction(16),
)
WORDS = ("LL", "LR", "RL", "RR")
RADIUS = Fraction(1, 10)
TARGET = Fraction(1)
PASS_RATIO = Fraction(5, 4)


def admissible_maps() -> tuple[tuple[int, int, int, int], ...]:
    maps = []
    for a in range(1, COEFFICIENT_MAX + 1):
        for b in range(0, COEFFICIENT_MAX + 1):
            for c in range(0, COEFFICIENT_MAX + 1):
                for d in range(1, COEFFICIENT_MAX + 1):
                    if a * d - b * c > 0:
                        maps.append((a, b, c, d))
    return tuple(sorted(maps))


def multiply(
    left: tuple[int, int, int, int],
    right: tuple[int, int, int, int],
) -> tuple[int, int, int, int]:
    """Return the matrix product ``left @ right``."""
    a, b, c, d = left
    e, f, g, h = right
    return (
        a * e + b * g,
        a * f + b * h,
        c * e + d * g,
        c * f + d * h,
    )


def compose_word(
    left_branch: tuple[int, int, int, int],
    right_branch: tuple[int, int, int, int],
    word: str,
) -> tuple[int, int, int, int]:
    if word not in WORDS:
        raise ValueError("word must be one of LL, LR, RL, RR")
    first = left_branch if word[0] == "L" else right_branch
    second = left_branch if word[1] == "L" else right_branch
    return multiply(second, first)


def reciprocal_conjugate(
    matrix: tuple[int, int, int, int],
) -> tuple[int, int, int, int]:
    a, b, c, d = matrix
    return (d, c, b, a)


def target_interval(centre: Fraction) -> tuple[Fraction, Fraction]:
    q = Fraction(centre)
    if q <= 0:
        raise ValueError("centre must be positive")
    return Fraction(9, 11) * q, Fraction(11, 9) * q


def forces_centre(
    matrix: tuple[int, int, int, int],
    centre: Fraction,
) -> bool:
    """Decide exact closure containment of the positive-line image."""
    A, B, C, D = matrix
    q = Fraction(centre)
    qn, qd = q.numerator, q.denominator
    if B * 11 * qd < 9 * qn * D:
        return False
    if C == 0:
        return False
    return A * 9 * qd <= 11 * qn * C


def _pair(value: Fraction) -> list[int]:
    return [value.numerator, value.denominator]


def _matrix_list(matrix: tuple[int, int, int, int]) -> list[int]:
    return list(matrix)


@lru_cache(maxsize=1)
def run_stage_f() -> dict[str, object]:
    maps = admissible_maps()
    map_set = set(maps)
    reciprocal_closed = all(
        reciprocal_conjugate(matrix) in map_set for matrix in maps
    )

    counts = {centre: 0 for centre in CENTRES}
    word_counts = {
        centre: {word: 0 for word in WORDS} for centre in CENTRES
    }
    pair_indices: dict[Fraction, set[tuple[int, int]]] = {
        centre: set() for centre in CENTRES
    }
    examples: dict[Fraction, list[dict[str, object]]] = {
        centre: [] for centre in CENTRES
    }

    for left_index, left_branch in enumerate(maps):
        for right_index, right_branch in enumerate(maps):
            for word in WORDS:
                composition = compose_word(left_branch, right_branch, word)
                for centre in CENTRES:
                    if not forces_centre(composition, centre):
                        continue
                    counts[centre] += 1
                    word_counts[centre][word] += 1
                    pair_indices[centre].add((left_index, right_index))
                    if len(examples[centre]) < 3:
                        examples[centre].append(
                            {
                                "L": _matrix_list(left_branch),
                                "R": _matrix_list(right_branch),
                                "word": word,
                                "composition": _matrix_list(composition),
                            }
                        )

    control_counts = sorted(
        counts[centre] for centre in CENTRES if centre != TARGET
    )
    control_median = Fraction(control_counts[3] + control_counts[4], 2)
    target_count = counts[TARGET]
    target_ratio = (
        Fraction(target_count, 1) / control_median
        if control_median
        else None
    )
    strict_first = all(
        target_count > counts[centre]
        for centre in CENTRES
        if centre != TARGET
    )
    ratio_pass = (
        target_count > 0
        if control_median == 0
        else target_ratio is not None and target_ratio >= PASS_RATIO
    )

    reciprocal_equalities = []
    symmetry_pass = True
    for centre in CENTRES:
        dual = 1 / centre
        equal = counts[centre] == counts[dual]
        reciprocal_equalities.append(
            {
                "left": _pair(centre),
                "right": _pair(dual),
                "left_count": counts[centre],
                "right_count": counts[dual],
                "equal": equal,
            }
        )
        symmetry_pass = symmetry_pass and equal

    if target_count == 0:
        conclusion = "NO_HALF_FORCING"
    elif strict_first and ratio_pass:
        conclusion = "CENTRE_BLIND_HALF_EXCESS"
    else:
        conclusion = "CENTRE_TIED_OR_MODEST"

    rows = []
    event_count = len(maps) ** 2 * len(WORDS)
    for centre in CENTRES:
        count = counts[centre]
        rank = 1 + sum(other > count for other in counts.values())
        interval = target_interval(centre)
        rows.append(
            {
                "odds": _pair(centre),
                "probability": _pair(centre / (1 + centre)),
                "target_interval": [
                    _pair(interval[0]),
                    _pair(interval[1]),
                ],
                "forcing_count": count,
                "forcing_rate": _pair(Fraction(count, event_count)),
                "distinct_branch_pairs": len(pair_indices[centre]),
                "word_counts": word_counts[centre],
                "rank": rank,
                "examples": examples[centre],
            }
        )

    technical_pass = (
        len(maps) == 256
        and len(maps) ** 2 == 65536
        and event_count == 262144
        and reciprocal_closed
        and symmetry_pass
    )

    return {
        "experiment": "DHSE-001",
        "stage": "F-preregistered-centre-blind-coefficient-census",
        "universe": {
            "coefficient_max": COEFFICIENT_MAX,
            "map_count": len(maps),
            "ordered_pair_count": len(maps) ** 2,
            "words": list(WORDS),
            "pair_word_event_count": event_count,
            "map_constraints": "a,d in 1..4; b,c in 0..4; ad-bc>0",
        },
        "metric": {
            "residual": "d_q(z)=|z-q|/(z+q)",
            "radius": _pair(RADIUS),
            "centres": [_pair(centre) for centre in CENTRES],
        },
        "centre_scan": rows,
        "primary_statistic": {
            "target_odds": _pair(TARGET),
            "target_forcing_count": target_count,
            "median_control_count": _pair(control_median),
            "target_to_control_median_ratio": (
                None if target_ratio is None else _pair(target_ratio)
            ),
            "strict_first": strict_first,
            "ratio_pass": ratio_pass,
            "pass_ratio": _pair(PASS_RATIO),
            "conclusion": conclusion,
        },
        "symmetry_audit": {
            "reciprocal_universe_closed": reciprocal_closed,
            "reciprocal_centre_count_equalities": reciprocal_equalities,
            "pass": symmetry_pass,
        },
        "technical_status": "PASS" if technical_pass else "FAIL",
        "scientific_status": conclusion,
        "interpretation_boundary": (
            "The result concerns the complete bounded coefficient universe "
            "a,d in 1..4 and b,c in 0..4 at projective radius 1/10. "
            "It is not an operator-independent law over all deterministic "
            "dynamics, does not order IEEE NaN with zero, and does not close "
            "an RH bridge."
        ),
    }
