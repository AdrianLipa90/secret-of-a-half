"""DHSE-001: deterministic reciprocal seed dynamics.

This module extends the existing zero--undefined duality with exact rational
trajectories. IEEE NaN never enters the state space. The abstract endpoints
are represented by p=0 (DEFINED_ZERO) and p=1 (UNDEFINED_BOTTOM), while the
projective odds z=p/(1-p) evolve under a reciprocal-conjugate pair of maps.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import hashlib
from typing import Iterator, Sequence

LEFT = 0
RIGHT = 1


@dataclass(frozen=True)
class Step:
    index: int
    branch: int | None
    odds: Fraction

    @property
    def probability(self) -> Fraction:
        return self.odds / (1 + self.odds)

    @property
    def side(self) -> int:
        return (self.odds > 1) - (self.odds < 1)

    @property
    def balance_residual(self) -> Fraction:
        p = self.probability
        return abs(2 * p - 1)

    def as_dict(self) -> dict[str, object]:
        p = self.probability
        residual = self.balance_residual
        return {
            "index": self.index,
            "branch": None if self.branch is None else ("L" if self.branch == LEFT else "R"),
            "odds": [self.odds.numerator, self.odds.denominator],
            "probability": [p.numerator, p.denominator],
            "side": self.side,
            "balance_residual": [residual.numerator, residual.denominator],
        }


def seed_digest(seed: str) -> str:
    return hashlib.sha256(seed.encode("utf-8")).hexdigest()


def initial_odds(seed: str) -> Fraction:
    """Map a text seed to one positive exact projective coordinate."""

    digest = hashlib.sha256(("DHSE-001:init:" + seed).encode("utf-8")).digest()
    numerator = int.from_bytes(digest[:16], "big") + 1
    denominator = int.from_bytes(digest[16:], "big") + 1
    return Fraction(numerator, denominator)


def branch_stream(seed: str) -> Iterator[int]:
    """Yield a deterministic, platform-independent SHA-256 counter stream."""

    counter = 0
    while True:
        payload = b"DHSE-001:stream:" + seed.encode("utf-8") + counter.to_bytes(8, "big")
        block = hashlib.sha256(payload).digest()
        for byte in block:
            for shift in range(7, -1, -1):
                yield (byte >> shift) & 1
        counter += 1


def left_map(z: Fraction) -> Fraction:
    if z <= 0:
        raise ValueError("projective odds must be positive")
    return z / (1 + z)


def right_map(z: Fraction) -> Fraction:
    if z <= 0:
        raise ValueError("projective odds must be positive")
    return z + 1


def reciprocal(z: Fraction) -> Fraction:
    if z <= 0:
        raise ValueError("projective odds must be positive")
    return 1 / z


def apply_branch(z: Fraction, branch: int) -> Fraction:
    if branch == LEFT:
        return left_map(z)
    if branch == RIGHT:
        return right_map(z)
    raise ValueError("branch must be LEFT=0 or RIGHT=1")


def trajectory(z0: Fraction, branches: Sequence[int]) -> tuple[Step, ...]:
    z = Fraction(z0)
    if z <= 0:
        raise ValueError("initial projective odds must be positive")
    result = [Step(index=0, branch=None, odds=z)]
    for index, branch in enumerate(branches, start=1):
        z = apply_branch(z, branch)
        result.append(Step(index=index, branch=branch, odds=z))
    return tuple(result)


def complement_branches(branches: Sequence[int]) -> tuple[int, ...]:
    return tuple(1 - branch for branch in branches)


def crossings(steps: Sequence[Step]) -> int:
    count = 0
    previous = steps[0].side
    for step in steps[1:]:
        current = step.side
        if current == 0 or previous == 0 or current != previous:
            count += 1
        previous = current
    return count


def exact_duality_holds(primary: Sequence[Step], dual: Sequence[Step]) -> bool:
    return len(primary) == len(dual) and all(
        left.odds * right.odds == 1 and left.probability + right.probability == 1
        for left, right in zip(primary, dual, strict=True)
    )


def run_experiment(seed: str = "secret-of-a-half:DHSE-001", steps: int = 256) -> dict[str, object]:
    if steps < 1:
        raise ValueError("steps must be positive")

    z0 = initial_odds(seed)
    stream = branch_stream(seed)
    branches = tuple(next(stream) for _ in range(steps))
    primary = trajectory(z0, branches)
    dual = trajectory(reciprocal(z0), complement_branches(branches))
    same_bits_control = trajectory(reciprocal(z0), branches)

    best = min(primary, key=lambda step: (step.balance_residual, step.index))
    half_hits = [step.index for step in primary if step.odds == 1]
    duality = exact_duality_holds(primary, dual)
    control_matches = sum(
        left.odds * right.odds == 1
        for left, right in zip(primary, same_bits_control, strict=True)
    )

    return {
        "experiment": "DHSE-001",
        "stage": "A-calibration",
        "seed": seed,
        "seed_sha256": seed_digest(seed),
        "steps": steps,
        "state_model": {
            "defined_zero_probability": [0, 1],
            "undefined_bottom_probability": [1, 1],
            "ieee_nan_in_state_space": False,
            "projective_coordinate": "z=p/(1-p)",
        },
        "operator": {
            "L": "z/(1+z)",
            "R": "z+1",
            "duality": "J(z)=1/z; J∘L=R∘J; J∘R=L∘J",
            "uses_explicit_half_constant": False,
        },
        "initial_odds": [z0.numerator, z0.denominator],
        "initial_probability": [
            (z0 / (1 + z0)).numerator,
            (z0 / (1 + z0)).denominator,
        ],
        "branch_prefix": "".join("L" if bit == LEFT else "R" for bit in branches[:64]),
        "results": {
            "exact_duality_all_steps": duality,
            "exact_half_hit_steps": half_hits,
            "crossings_of_self_dual_axis": crossings(primary),
            "closest_step": best.index,
            "closest_balance_residual": [
                best.balance_residual.numerator,
                best.balance_residual.denominator,
            ],
            "same_bits_control_duality_matches": control_matches,
            "same_bits_control_total_states": len(primary),
        },
        "technical_status": "PASS" if duality and control_matches < len(primary) else "FAIL",
        "scientific_status": "CALIBRATION_ONLY",
        "interpretation_boundary": (
            "The reciprocal-conjugate operator family structurally singles out z=1 "
            "(p=1/2). This stage validates deterministic provenance and exact duality; "
            "it is not independent evidence that 1/2 lies between IEEE NaN and zero."
        ),
        "trajectory_preview": [step.as_dict() for step in primary[:12]],
    }
