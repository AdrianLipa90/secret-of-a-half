"""DHSE-001 Stage M: exact continuous forcing-count theorem."""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from typing import DefaultDict

import numpy as np

from .dhse_001_stage_i import SCALE, _pair, _word_matrix, words_of_length
from .dhse_001_stage_j import EXPECTED_PRIMITIVE_MAP_COUNT, primitive_maps

LENGTHS = (1, 2, 3, 4)
RADIUS = Fraction(1, 10)
EXPECTED = {
    1: {"interval_count": 188496, "breakpoint_count": 44, "q1_count": 24752, "maximum": 39984},
    2: {"interval_count": 1741094, "breakpoint_count": 3359, "q1_count": 314690, "maximum": 314690},
    3: {"interval_count": 5068044, "breakpoint_count": 150239, "q1_count": 943740, "maximum": 943740},
    4: {"interval_count": 11594096, "breakpoint_count": 1595693, "q1_count": 2219236, "maximum": 2224570},
}

EndpointCounts = DefaultDict[tuple[int, int], int]
INT64_MAX = int(np.iinfo(np.int64).max)


def int64_safety_certificate(length: int, scale: int = SCALE) -> dict[str, int | bool]:
    """Prove that Stage-M fixed-width integer operations cannot overflow.

    Every primitive base matrix has coefficients bounded by ``scale``.  If the
    largest absolute coefficient after ``n`` letters is ``M_n``, one left
    multiplication gives ``M_{n+1} <= 2*scale*M_n``.  Starting from the identity
    therefore gives ``M_n <= (2*scale)**n``.

    Stage M's largest comparison is ``121*B*C``.  Bounding both factors by the
    matrix-entry bound gives a conservative exact upper bound that can be
    checked before allocating the vectorized sweep.  This preserves NumPy's
    fast int64 execution while making the finite-arithmetic premise explicit.
    """
    if length < 1:
        raise ValueError("word length must be positive")
    if scale < 1:
        raise ValueError("scale must be positive")

    matrix_entry_bound = (2 * scale) ** length
    comparison_product_bound = 121 * matrix_entry_bound * matrix_entry_bound
    endpoint_numerator_bound = 11 * matrix_entry_bound
    maximum_required = max(comparison_product_bound, endpoint_numerator_bound)
    return {
        "length": length,
        "scale": scale,
        "matrix_entry_bound": matrix_entry_bound,
        "comparison_product_bound": comparison_product_bound,
        "endpoint_numerator_bound": endpoint_numerator_bound,
        "int64_max": INT64_MAX,
        "safe": maximum_required <= INT64_MAX,
    }


def _reduced_pairs(numerator: np.ndarray, denominator: np.ndarray) -> np.ndarray:
    common = np.gcd(numerator, denominator)
    reduced_n = numerator // common
    reduced_d = denominator // common
    pairs = np.empty(len(reduced_n), dtype=[("n", "<i8"), ("d", "<i8")])
    pairs["n"] = reduced_n
    pairs["d"] = reduced_d
    return pairs


def _accumulate(target: EndpointCounts, pairs: np.ndarray) -> None:
    unique, counts = np.unique(pairs, return_counts=True)
    for numerator, denominator, count in zip(unique["n"], unique["d"], counts):
        target[(int(numerator), int(denominator))] += int(count)


def endpoint_census(
    length: int,
) -> tuple[dict[tuple[int, int], int], dict[tuple[int, int], int], int]:
    safety = int64_safety_certificate(length)
    if not safety["safe"]:
        raise OverflowError(
            "Stage-M vectorized int64 arithmetic is not certified safe for "
            f"length={length}, scale={SCALE}; use an exact wider-integer backend"
        )

    maps = primitive_maps()
    size = len(maps)
    a, b, c, d = (maps[:, index] for index in range(4))
    left = (a[None, :], b[None, :], c[None, :], d[None, :])
    right = (a[:, None], b[:, None], c[:, None], d[:, None])

    starts: EndpointCounts = defaultdict(int)
    ends: EndpointCounts = defaultdict(int)
    interval_count = 0

    for word in words_of_length(length):
        A, B, C, D = _word_matrix(word, left, right, size)
        valid = (B > 0) & (C > 0) & (81 * A * D <= 121 * B * C)
        A = A[valid]
        B = B[valid]
        C = C[valid]
        D = D[valid]

        lower = _reduced_pairs(9 * A, 11 * C)
        upper = _reduced_pairs(11 * B, 9 * D)
        _accumulate(starts, lower)
        _accumulate(ends, upper)
        interval_count += len(lower)

    return dict(starts), dict(ends), interval_count


def _fraction_key(value: Fraction) -> tuple[int, int]:
    return value.numerator, value.denominator


def _maximizer_components(
    point_maximizers: tuple[Fraction, ...],
    open_maximizers: tuple[tuple[Fraction, Fraction], ...],
) -> list[dict[str, object]]:
    point_set = set(point_maximizers)
    components: list[dict[str, object]] = []
    used_points: set[Fraction] = set()

    for left, right in open_maximizers:
        component = {
            "left": _pair(left),
            "right": _pair(right),
            "left_closed": left in point_set,
            "right_closed": right in point_set,
        }
        if (
            components
            and Fraction(*components[-1]["right"]) == left
            and components[-1]["right_closed"]
            and component["left_closed"]
        ):
            components[-1]["right"] = _pair(right)
            components[-1]["right_closed"] = component["right_closed"]
        else:
            components.append(component)
        if left in point_set:
            used_points.add(left)
        if right in point_set:
            used_points.add(right)

    for point in point_maximizers:
        if point not in used_points:
            components.append(
                {
                    "left": _pair(point),
                    "right": _pair(point),
                    "left_closed": True,
                    "right_closed": True,
                }
            )

    components.sort(key=lambda row: Fraction(*row["left"]))
    return components


def exact_sweep(
    starts: dict[tuple[int, int], int],
    ends: dict[tuple[int, int], int],
) -> dict[str, object]:
    breakpoints = sorted(
        Fraction(numerator, denominator)
        for numerator, denominator in set(starts) | set(ends)
    )
    active = 0
    previous: Fraction | None = None
    maximum = -1
    point_maximizers: list[Fraction] = []
    open_maximizers: list[tuple[Fraction, Fraction]] = []
    q1_count: int | None = None

    def register_point(point: Fraction, count: int) -> None:
        nonlocal maximum, point_maximizers, open_maximizers
        if count > maximum:
            maximum = count
            point_maximizers = [point]
            open_maximizers = []
        elif count == maximum:
            point_maximizers.append(point)

    def register_open(left: Fraction, right: Fraction, count: int) -> None:
        nonlocal maximum, point_maximizers, open_maximizers
        if count > maximum:
            maximum = count
            point_maximizers = []
            open_maximizers = [(left, right)]
        elif count == maximum:
            open_maximizers.append((left, right))

    for point in breakpoints:
        if previous is not None:
            register_open(previous, point, active)
            if previous < 1 < point:
                q1_count = active

        key = _fraction_key(point)
        point_count = active + starts.get(key, 0)
        register_point(point, point_count)
        if point == 1:
            q1_count = point_count
        active = point_count - ends.get(key, 0)
        previous = point

    if active != 0:
        raise AssertionError("endpoint sweep did not close")
    if q1_count is None:
        raise AssertionError("q=1 was not classified")

    points = tuple(point_maximizers)
    opens = tuple(open_maximizers)
    return {
        "maximum": maximum,
        "q1_count": q1_count,
        "q1_is_global_maximum": q1_count == maximum,
        "q1_is_unique_global_maximum": (
            q1_count == maximum
            and points == (Fraction(1),)
            and not opens
        ),
        "point_maximizers": [_pair(value) for value in points],
        "open_interval_maximizers": [
            {"left": _pair(left), "right": _pair(right)}
            for left, right in opens
        ],
        "maximizer_components": _maximizer_components(points, opens),
    }


def reciprocal_endpoint_symmetry(
    starts: dict[tuple[int, int], int],
    ends: dict[tuple[int, int], int],
) -> bool:
    return all(
        ends.get((denominator, numerator), 0) == count
        for (numerator, denominator), count in starts.items()
    ) and all(
        starts.get((denominator, numerator), 0) == count
        for (numerator, denominator), count in ends.items()
    )


def length_theorem(length: int) -> dict[str, object]:
    starts, ends, interval_count = endpoint_census(length)
    sweep = exact_sweep(starts, ends)
    breakpoint_count = len(set(starts) | set(ends))
    expected = EXPECTED[length]
    symmetry = reciprocal_endpoint_symmetry(starts, ends)
    technical_pass = (
        interval_count == expected["interval_count"]
        and breakpoint_count == expected["breakpoint_count"]
        and sweep["q1_count"] == expected["q1_count"]
        and sweep["maximum"] == expected["maximum"]
        and symmetry
    )
    return {
        "length": length,
        "word_count": 2**length,
        "ordered_pair_count": EXPECTED_PRIMITIVE_MAP_COUNT**2,
        "pair_word_event_count": (2**length) * EXPECTED_PRIMITIVE_MAP_COUNT**2,
        "nonempty_forcing_interval_count": interval_count,
        "breakpoint_count": breakpoint_count,
        "reciprocal_endpoint_symmetry": symmetry,
        "sweep": sweep,
        "technical_status": "PASS" if technical_pass else "FAIL",
    }


@lru_cache(maxsize=1)
def run_stage_m() -> dict[str, object]:
    rows = [length_theorem(length) for length in LENGTHS]
    by_length = {row["length"]: row for row in rows}
    exact_central_lengths = [
        length
        for length, row in by_length.items()
        if row["sweep"]["q1_is_unique_global_maximum"]
    ]
    split_lengths = [
        length
        for length, row in by_length.items()
        if not row["sweep"]["q1_is_global_maximum"]
    ]
    technical_pass = (
        len(primitive_maps()) == EXPECTED_PRIMITIVE_MAP_COUNT
        and all(row["technical_status"] == "PASS" for row in rows)
    )
    conclusion = (
        "CONTINUOUS_MAXIMUM_CLASSIFIED_WITH_LENGTH_DEPENDENT_SPLITTING"
        if exact_central_lengths == [2, 3] and split_lengths == [1, 4]
        else "CONTINUOUS_CLASSIFICATION_UNEXPECTED"
    )
    return {
        "experiment": "DHSE-001",
        "stage": "M-exact-continuous-forcing-theorem",
        "parameters": {
            "primitive_map_count": EXPECTED_PRIMITIVE_MAP_COUNT,
            "lengths": list(LENGTHS),
            "radius": _pair(RADIUS),
            "centre_domain": "all positive q classified by exact rational breakpoints",
        },
        "length_theorems": rows,
        "summary": {
            "unique_self_dual_global_maximum_lengths": exact_central_lengths,
            "reciprocal_split_maximum_lengths": split_lengths,
            "conclusion": conclusion,
        },
        "technical_status": "PASS" if technical_pass else "FAIL",
        "scientific_status": conclusion,
        "interpretation_boundary": (
            "This is an exact exhaustive theorem only for the primitive K=6 "
            "positive integer Möbius universe, radius 1/10 and word lengths 1..4. "
            "It proves that reciprocal symmetry alone does not force a central maximum."
        ),
    }
