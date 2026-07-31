"""DHSE-001 Stage D: exact operator-geometry atlas.

The stage performs no new stochastic target test. It classifies finite words in
the four Stage B experimental operator families by exact integer matrix
composition on the positive projective line.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import product
from typing import Iterable

from .dhse_001_stage_b import FAMILIES, RADIUS, TARGET

Matrix = tuple[int, int, int, int]
MAX_WORD_LENGTH = 8


def compose(outer: Matrix, inner: Matrix) -> Matrix:
    """Return the matrix for outer(inner(z))."""
    a, b, c, d = outer
    e, f, g, h = inner
    return (
        a * e + b * g,
        a * f + b * h,
        c * e + d * g,
        c * f + d * h,
    )


def family_matrices(family_name: str) -> dict[str, Matrix]:
    family = next(
        item for item in FAMILIES
        if item.name == family_name and not item.calibration_only
    )
    return {
        "L": tuple(family.left.as_list()),
        "R": tuple(family.right.as_list()),
    }


def word_matrix(family_name: str, word: str) -> Matrix:
    matrices = family_matrices(family_name)
    result: Matrix = (1, 0, 0, 1)
    for symbol in word:
        if symbol not in matrices:
            raise ValueError("word must contain only L and R")
        result = compose(matrices[symbol], result)
    return result


def apply_matrix(matrix: Matrix, z: Fraction) -> Fraction:
    value = Fraction(z)
    if value <= 0:
        raise ValueError("projective odds must be positive")
    a, b, c, d = matrix
    denominator = c * value + d
    if denominator <= 0:
        raise ValueError("matrix left the positive projective line")
    result = Fraction(a * value + b, denominator)
    if result <= 0:
        raise ValueError("matrix left the positive projective line")
    return result


def determinant(matrix: Matrix) -> int:
    a, b, c, d = matrix
    return a * d - b * c


def fixes_target(matrix: Matrix) -> bool:
    a, b, c, d = matrix
    return a + b == c + d


def derivative_at_target(matrix: Matrix) -> Fraction:
    if not fixes_target(matrix):
        raise ValueError("matrix does not fix q=1")
    a, b, c, d = matrix
    return Fraction(abs(determinant(matrix)), (c + d) ** 2)


def target_ball(radius: Fraction = RADIUS) -> tuple[Fraction, Fraction]:
    r = Fraction(radius)
    if not 0 < r < 1:
        raise ValueError("radius must lie in (0,1)")
    return Fraction(1 - r, 1 + r), Fraction(1 + r, 1 - r)


def positive_line_image(matrix: Matrix) -> tuple[Fraction, Fraction | None]:
    """Return increasing-map endpoint limits for z in (0,+infinity).

    The upper endpoint is ``None`` when the image is unbounded.
    """
    a, b, c, d = matrix
    if min(a, b, c) < 0 or d <= 0 or determinant(matrix) <= 0:
        raise ValueError("Stage D expects positive increasing Möbius maps")
    lower = Fraction(b, d)
    upper = None if c == 0 else Fraction(a, c)
    return lower, upper


def universally_forces_target(matrix: Matrix) -> bool:
    lower, upper = positive_line_image(matrix)
    target_lower, target_upper = target_ball()
    return upper is not None and lower >= target_lower and upper <= target_upper


def words_of_length(length: int) -> Iterable[str]:
    return ("".join(symbols) for symbols in product("LR", repeat=length))


def census_family(family_name: str) -> dict[str, object]:
    fixed_by_length: dict[str, list[dict[str, object]]] = {}
    forcing_by_length: dict[str, list[dict[str, object]]] = {}

    for length in range(1, MAX_WORD_LENGTH + 1):
        fixed_rows: list[dict[str, object]] = []
        forcing_rows: list[dict[str, object]] = []
        for word in words_of_length(length):
            matrix = word_matrix(family_name, word)
            if fixes_target(matrix):
                multiplier = derivative_at_target(matrix)
                fixed_rows.append(
                    {
                        "word": word,
                        "matrix": list(matrix),
                        "multiplier": [multiplier.numerator, multiplier.denominator],
                        "contracting": multiplier < 1,
                    }
                )
            if universally_forces_target(matrix):
                lower, upper = positive_line_image(matrix)
                assert upper is not None
                forcing_rows.append(
                    {
                        "word": word,
                        "matrix": list(matrix),
                        "image": [
                            [lower.numerator, lower.denominator],
                            [upper.numerator, upper.denominator],
                        ],
                    }
                )
        fixed_by_length[str(length)] = fixed_rows
        forcing_by_length[str(length)] = forcing_rows

    minimal_fixed_length = next(
        (int(length) for length, rows in fixed_by_length.items() if rows),
        None,
    )
    minimal_forcing_length = next(
        (int(length) for length, rows in forcing_by_length.items() if rows),
        None,
    )

    return {
        "family": family_name,
        "fixed_q1_counts_by_length": {
            length: len(rows) for length, rows in fixed_by_length.items()
        },
        "minimal_fixed_q1_words": (
            [] if minimal_fixed_length is None
            else fixed_by_length[str(minimal_fixed_length)]
        ),
        "universal_forcing_counts_by_length": {
            length: len(rows) for length, rows in forcing_by_length.items()
        },
        "minimal_universal_forcing_words": (
            [] if minimal_forcing_length is None
            else forcing_by_length[str(minimal_forcing_length)]
        ),
    }


def mechanism_record(family_name: str) -> dict[str, object]:
    if family_name == "affine_skew":
        return {
            "classification": "BRANCH_LOCAL_Q1_ATTRACTION",
            "exact_statement": "L^n(z)=1+(2/3)^n*(z-1)",
            "minimal_mechanism": "L",
            "scope": "Only all-L words fix q=1 through census length 8.",
        }
    if family_name == "mobius_skew":
        return {
            "classification": "UNIVERSAL_TWO_LETTER_TARGET_FORCING",
            "exact_statement": "R(L(z))=(5z+6)/(5z+7) in (6/7,1) for every z>0",
            "minimal_mechanism": "LR",
            "scope": "The whole positive line is forced into the frozen target ball.",
        }
    if family_name == "scale_translate":
        return {
            "classification": "MONOTONE_ESCAPE",
            "exact_statement": "L(z)=2z>z and R(z)=z+3>z for every z>0",
            "minimal_mechanism": None,
            "scope": "Every infinite branch sequence diverges to +infinity.",
        }
    if family_name == "collatz_stream":
        return {
            "classification": "TWO_LETTER_Q1_ATTRACTION",
            "exact_statement": "(L after R)^n(z)=1+(3/4)^n*(z-1)",
            "minimal_mechanism": "RL",
            "scope": "Repeated RL words contract to q=1; no universal forcing word through length 8.",
        }
    raise ValueError(f"unknown experimental family: {family_name}")


def run_stage_d() -> dict[str, object]:
    experimental_names = [
        family.name for family in FAMILIES if not family.calibration_only
    ]
    rows = []
    for name in experimental_names:
        census = census_family(name)
        census["mechanism"] = mechanism_record(name)
        rows.append(census)

    forcing_families = [
        row["family"] for row in rows
        if row["minimal_universal_forcing_words"]
    ]
    fixed_families = [
        row["family"] for row in rows
        if row["minimal_fixed_q1_words"]
    ]

    expected = {
        "affine_skew": ("L", None),
        "mobius_skew": (None, "LR"),
        "scale_translate": (None, None),
        "collatz_stream": ("RL", None),
    }
    technical_pass = True
    for row in rows:
        fixed_word, forcing_word = expected[row["family"]]
        actual_fixed = (
            row["minimal_fixed_q1_words"][0]["word"]
            if row["minimal_fixed_q1_words"] else None
        )
        actual_forcing = (
            row["minimal_universal_forcing_words"][0]["word"]
            if row["minimal_universal_forcing_words"] else None
        )
        technical_pass = technical_pass and (
            actual_fixed == fixed_word and actual_forcing == forcing_word
        )

    lower, upper = target_ball()
    return {
        "experiment": "DHSE-001",
        "stage": "D-exact-operator-geometry-atlas",
        "parameters": {
            "max_word_length": MAX_WORD_LENGTH,
            "word_application_order": "left-to-right",
            "target_odds": [TARGET.numerator, TARGET.denominator],
            "residual_radius": [RADIUS.numerator, RADIUS.denominator],
            "target_ball": [
                [lower.numerator, lower.denominator],
                [upper.numerator, upper.denominator],
            ],
        },
        "families": rows,
        "summary": {
            "families_with_finite_q1_fixed_words": fixed_families,
            "families_with_universal_target_forcing_words": forcing_families,
            "monotone_escape_families": ["scale_translate"],
            "shared_mechanism_across_all_families": False,
            "conclusion": "NO_OPERATOR_INDEPENDENT_HALF_SELECTION",
        },
        "technical_status": "PASS" if technical_pass else "FAIL",
        "scientific_status": "OPERATOR_LOCAL_MECHANISMS_IDENTIFIED",
        "interpretation_boundary": (
            "The self-dual coordinate q=1 is selected by different local algebraic "
            "mechanisms in some families and by no finite mechanism in another. "
            "This atlas does not establish a universal dynamical halfway law and "
            "does not place IEEE NaN in the mathematical state space."
        ),
    }
