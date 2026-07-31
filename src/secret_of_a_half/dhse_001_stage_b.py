"""DHSE-001 Stage B: preregistered centre-blind operator-family scan.

All dynamics use exact positive rational projective odds. IEEE NaN remains
outside the state space. The target q=1 (equivalently p=1/2) is scored by the
same centre-blind statistic as eight reciprocal control centres.
"""
from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from fractions import Fraction
from statistics import median
from typing import Iterable, Sequence

from .dhse_001 import LEFT, RIGHT, branch_stream, initial_odds

BASE_SEED = "secret-of-a-half:DHSE-001"
ENSEMBLE_SIZE = 64
STEPS = 384
BURN_IN = 64
RADIUS = Fraction(1, 10)
CENTRES = tuple(Fraction(2**k, 1) if k >= 0 else Fraction(1, 2 ** (-k)) for k in range(-4, 5))
TARGET = Fraction(1, 1)
PASS_RATIO = Fraction(5, 4)
REQUIRED_FAMILY_PASSES = 3


@dataclass(frozen=True)
class MobiusMap:
    a: int
    b: int
    c: int
    d: int

    def __call__(self, z: Fraction) -> Fraction:
        value = Fraction(z)
        if value <= 0:
            raise ValueError("projective odds must be positive")
        denominator = self.c * value + self.d
        if denominator <= 0:
            raise ValueError("map left the positive projective line")
        result = (self.a * value + self.b) / denominator
        if result <= 0:
            raise ValueError("map left the positive projective line")
        return result

    def as_list(self) -> list[int]:
        return [self.a, self.b, self.c, self.d]


@dataclass(frozen=True)
class OperatorFamily:
    name: str
    left: MobiusMap
    right: MobiusMap
    calibration_only: bool = False

    def apply(self, z: Fraction, branch: int) -> Fraction:
        if branch == LEFT:
            return self.left(z)
        if branch == RIGHT:
            return self.right(z)
        raise ValueError("branch must be LEFT=0 or RIGHT=1")


FAMILIES = (
    OperatorFamily(
        "reciprocal_calibration",
        MobiusMap(1, 0, 1, 1),
        MobiusMap(1, 1, 0, 1),
        calibration_only=True,
    ),
    OperatorFamily("affine_skew", MobiusMap(2, 1, 0, 3), MobiusMap(3, 2, 0, 2)),
    OperatorFamily("mobius_skew", MobiusMap(1, 1, 2, 3), MobiusMap(3, 1, 1, 2)),
    OperatorFamily("scale_translate", MobiusMap(2, 0, 0, 1), MobiusMap(1, 3, 0, 1)),
    OperatorFamily("collatz_stream", MobiusMap(1, 0, 0, 2), MobiusMap(3, 1, 0, 2)),
)


def projective_residual(z: Fraction, centre: Fraction) -> Fraction:
    value = Fraction(z)
    target = Fraction(centre)
    if value <= 0 or target <= 0:
        raise ValueError("odds and centre must be positive")
    return abs(value - target) / (value + target)


def trajectory(family: OperatorFamily, z0: Fraction, branches: Sequence[int]) -> tuple[Fraction, ...]:
    z = Fraction(z0)
    if z <= 0:
        raise ValueError("initial projective odds must be positive")
    result = [z]
    for branch in branches:
        z = family.apply(z, branch)
        result.append(z)
    return tuple(result)


def reciprocal_conjugacy_matches(family: OperatorFamily, samples: Iterable[Fraction]) -> int:
    matches = 0
    for z in samples:
        if 1 / family.left(z) == family.right(1 / z):
            matches += 1
        if 1 / family.right(z) == family.left(1 / z):
            matches += 1
    return matches


def _crossings(states: Sequence[Fraction], centre: Fraction) -> int:
    previous = (states[0] > centre) - (states[0] < centre)
    total = 0
    for z in states[1:]:
        current = (z > centre) - (z < centre)
        if current == 0 or previous == 0 or current != previous:
            total += 1
        previous = current
    return total


def _fraction_pair(value: Fraction) -> list[int]:
    return [value.numerator, value.denominator]


def _median_fraction(values: Sequence[Fraction]) -> Fraction:
    return Fraction(median(values))


def scan_family(family: OperatorFamily) -> dict[str, object]:
    occupancy = {centre: 0 for centre in CENTRES}
    crossing_counts = {centre: 0 for centre in CENTRES}
    minima = {centre: [] for centre in CENTRES}
    observed_states = 0
    observed_transitions = 0

    for index in range(ENSEMBLE_SIZE):
        seed = f"{BASE_SEED}:stage-b:{index:03d}"
        stream = branch_stream(seed)
        branches = tuple(next(stream) for _ in range(STEPS))
        states = trajectory(family, initial_odds(seed), branches)[BURN_IN:]
        observed_states += len(states)
        observed_transitions += len(states) - 1
        for centre in CENTRES:
            residuals = tuple(projective_residual(z, centre) for z in states)
            occupancy[centre] += sum(residual <= RADIUS for residual in residuals)
            crossing_counts[centre] += _crossings(states, centre)
            minima[centre].append(min(residuals))

    occupancy_rates = {
        centre: Fraction(occupancy[centre], observed_states) for centre in CENTRES
    }
    crossing_rates = {
        centre: Fraction(crossing_counts[centre], observed_transitions) for centre in CENTRES
    }
    median_minima = {
        centre: _median_fraction(minima[centre]) for centre in CENTRES
    }

    target_occupancy = occupancy_rates[TARGET]
    control_occupancies = tuple(occupancy_rates[c] for c in CENTRES if c != TARGET)
    control_median = _median_fraction(control_occupancies)
    ratio = target_occupancy / control_median if control_median > 0 else None
    strict_first = all(target_occupancy > value for value in control_occupancies)
    rank = 1 + sum(value > target_occupancy for value in control_occupancies)
    ratio_pass = (
        target_occupancy > 0 if control_median == 0 else ratio is not None and ratio >= PASS_RATIO
    )
    family_pass = bool(strict_first and ratio_pass)

    samples = (Fraction(1, 7), Fraction(2, 3), Fraction(1), Fraction(9, 4), Fraction(31, 5))
    conjugacy_matches = reciprocal_conjugacy_matches(family, samples)

    centre_rows = []
    for centre in CENTRES:
        centre_rows.append(
            {
                "odds": _fraction_pair(centre),
                "probability": _fraction_pair(centre / (1 + centre)),
                "occupancy": _fraction_pair(occupancy_rates[centre]),
                "crossing_rate": _fraction_pair(crossing_rates[centre]),
                "median_nearest_residual": _fraction_pair(median_minima[centre]),
            }
        )

    return {
        "family": family.name,
        "calibration_only": family.calibration_only,
        "maps": {
            "L": family.left.as_list(),
            "R": family.right.as_list(),
            "form": "(a*z+b)/(c*z+d)",
        },
        "reciprocal_conjugacy_sample_matches": conjugacy_matches,
        "reciprocal_conjugacy_sample_comparisons": 2 * len(samples),
        "observed_states": observed_states,
        "observed_transitions": observed_transitions,
        "centre_scan": centre_rows,
        "primary_statistic": {
            "target_odds": _fraction_pair(TARGET),
            "target_occupancy": _fraction_pair(target_occupancy),
            "control_median_occupancy": _fraction_pair(control_median),
            "target_to_control_median_ratio": None if ratio is None else _fraction_pair(ratio),
            "target_rank": rank,
            "strict_first": strict_first,
            "family_pass": family_pass,
        },
    }


@lru_cache(maxsize=1)
def run_stage_b() -> dict[str, object]:
    family_results = [scan_family(family) for family in FAMILIES]
    experimental = [row for row in family_results if not row["calibration_only"]]
    passing = [row["family"] for row in experimental if row["primary_statistic"]["family_pass"]]
    pass_count = len(passing)
    if pass_count >= REQUIRED_FAMILY_PASSES:
        conclusion = "ROBUST_HALF_EFFECT"
    elif pass_count > 0:
        conclusion = "FAMILY_DEPENDENT"
    else:
        conclusion = "NO_ROBUST_HALF_EFFECT"

    technical_pass = (
        all(row["observed_states"] == ENSEMBLE_SIZE * (STEPS + 1 - BURN_IN) for row in family_results)
        and all(
            row["reciprocal_conjugacy_sample_matches"] < row["reciprocal_conjugacy_sample_comparisons"]
            for row in experimental
        )
    )

    return {
        "experiment": "DHSE-001",
        "stage": "B-preregistered-centre-blind-scan",
        "base_seed": BASE_SEED,
        "parameters": {
            "ensemble_size": ENSEMBLE_SIZE,
            "steps": STEPS,
            "burn_in": BURN_IN,
            "radius": _fraction_pair(RADIUS),
            "centres_odds": [_fraction_pair(value) for value in CENTRES],
            "target_odds": _fraction_pair(TARGET),
            "pass_ratio": _fraction_pair(PASS_RATIO),
            "required_experimental_family_passes": REQUIRED_FAMILY_PASSES,
        },
        "primary_rule": (
            "A family passes iff q=1 has strictly greatest occupancy within projective "
            "residual radius 1/10 and occupancy is at least 5/4 of the median of the "
            "eight non-target centres. Robust effect requires at least 3 of 4 "
            "non-calibration families."
        ),
        "families": family_results,
        "summary": {
            "experimental_family_pass_count": pass_count,
            "passing_experimental_families": passing,
            "conclusion": conclusion,
        },
        "technical_status": "PASS" if technical_pass else "FAIL",
        "scientific_status": conclusion,
        "interpretation_boundary": (
            "This scan concerns exact-rational trajectory occupancy around q=1 in a "
            "declared projective coordinate. It neither orders IEEE NaN with zero nor "
            "promotes the abstract undefined label to a numeric endpoint."
        ),
    }
