"""Typed identity-axis and holonomy solver for Secret of a Half v0.7.

The solver is deliberately epistemic: exact and standard rules may close by
default, model rules require explicit opt-in, and OPEN rules are never promoted.
The purpose is to make the logical boundary around the Riemann Hypothesis
machine-checkable rather than merely stated in prose.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import cmath
import math
from typing import Iterable, Mapping

from .core import binary_entropy, complementary_amplitude


HALF = 0.5
LN2 = math.log(2.0)


class ClaimStatus(str, Enum):
    EXACT = "exact"
    STANDARD = "standard"
    MODEL = "model"
    OPEN = "open"


class RelationKind(str, Enum):
    FIXED_POINT = "fixed_point"
    DUAL = "dual"
    IMPLIES = "implies"
    REPRESENTS = "represents"
    HOLONOMIC = "holonomic"
    CROSS_REFERENCE = "cross_reference"


@dataclass(frozen=True)
class Rule:
    premises: tuple[str, ...]
    conclusion: str
    status: ClaimStatus
    kind: RelationKind
    provenance: str
    holonomy_turns: float | None = None


@dataclass(frozen=True)
class ProofStep:
    conclusion: str
    rule: Rule


@dataclass(frozen=True)
class ClosureResult:
    facts: frozenset[str]
    proof: Mapping[str, ProofStep]
    blocked: tuple[Rule, ...]

    def derives(self, claim: str) -> bool:
        return claim in self.facts


@dataclass(frozen=True)
class IdentityAxis:
    """Oriented binary identity axis with fixed point 1/2."""

    value: float = HALF

    def displacement(self, sigma: float) -> float:
        return float(sigma) - self.value

    def orientation(self, sigma: float, *, atol: float = 0.0) -> int:
        x = self.displacement(sigma)
        if math.isclose(x, 0.0, abs_tol=atol, rel_tol=0.0):
            return 0
        return 1 if x > 0.0 else -1

    def complement(self, sigma: float) -> float:
        return 2.0 * self.value - float(sigma)


@dataclass(frozen=True)
class CycleCoordinate:
    """Normalized projective recurrence coordinate on R/Z."""

    turns: float

    @property
    def wrapped(self) -> float:
        return self.turns % 1.0


@dataclass(frozen=True)
class PhaseClosure:
    """Explicit representation map from normalized turns to angular units."""

    period: float

    def __post_init__(self) -> None:
        if self.period <= 0.0:
            raise ValueError("period must be positive")

    def angle(self, turns: float) -> float:
        return self.period * float(turns)

    def turns(self, angle: float) -> float:
        return float(angle) / self.period


class ClaimSolver:
    """Forward-chaining solver over typed multi-premise rules."""

    def __init__(self, rules: Iterable[Rule]) -> None:
        self.rules = tuple(rules)

    @staticmethod
    def _allowed(allow_model: bool) -> set[ClaimStatus]:
        allowed = {ClaimStatus.EXACT, ClaimStatus.STANDARD}
        if allow_model:
            allowed.add(ClaimStatus.MODEL)
        return allowed

    def closure(self, facts: Iterable[str], *, allow_model: bool = False) -> ClosureResult:
        allowed = self._allowed(allow_model)
        known = set(map(str, facts))
        proof: dict[str, ProofStep] = {}
        changed = True
        while changed:
            changed = False
            for rule in self.rules:
                if rule.status not in allowed or rule.conclusion in known:
                    continue
                if all(premise in known for premise in rule.premises):
                    known.add(rule.conclusion)
                    proof[rule.conclusion] = ProofStep(rule.conclusion, rule)
                    changed = True
        blocked = tuple(
            rule for rule in self.rules
            if rule.conclusion not in known
            and (rule.status not in allowed or not all(p in known for p in rule.premises))
        )
        return ClosureResult(frozenset(known), proof, blocked)

    def missing_premises(
        self,
        goal: str,
        facts: Iterable[str],
        *,
        allow_model: bool = False,
    ) -> tuple[tuple[Rule, tuple[str, ...]], ...]:
        result = self.closure(facts, allow_model=allow_model)
        if goal in result.facts:
            return ()
        return tuple(
            (rule, tuple(p for p in rule.premises if p not in result.facts))
            for rule in self.rules
            if rule.conclusion == goal
        )

    def proof_chain(
        self,
        goal: str,
        facts: Iterable[str],
        *,
        allow_model: bool = False,
    ) -> tuple[ProofStep, ...]:
        result = self.closure(facts, allow_model=allow_model)
        if goal not in result.facts:
            return ()
        base = set(map(str, facts))
        ordered: list[ProofStep] = []
        visited: set[str] = set()

        def visit(claim: str) -> None:
            if claim in base or claim in visited:
                return
            visited.add(claim)
            step = result.proof.get(claim)
            if step is None:
                return
            for premise in step.rule.premises:
                visit(premise)
            ordered.append(step)

        visit(goal)
        return tuple(ordered)


HALF_AXIS_RULES = (
    Rule(("sigma_half",), "complement_fixed", ClaimStatus.EXACT, RelationKind.FIXED_POINT, "SOH-L003/binary complement"),
    Rule(("sigma_half",), "centered_zero", ClaimStatus.EXACT, RelationKind.REPRESENTS, "x=sigma-1/2"),
    Rule(("sigma_half",), "entropy_max_ln2", ClaimStatus.EXACT, RelationKind.IMPLIES, "SOH-L001"),
    Rule(("sigma_half", "binary_state"), "bloch_equator", ClaimStatus.STANDARD, RelationKind.REPRESENTS, "SOH-L005/Bloch map"),
    Rule(("bloch_equator", "equatorial_loop"), "berry_minus_one", ClaimStatus.STANDARD, RelationKind.HOLONOMIC, "Berry holonomy", 0.5),
    Rule(("sigma_half", "symmetric_detector", "half_turn_phase"), "exact_cancellation", ClaimStatus.EXACT, RelationKind.IMPLIES, "SOH-L002", 0.5),
    Rule(("zeta_involution",), "zeta_fixed_axis_half", ClaimStatus.STANDARD, RelationKind.FIXED_POINT, "SOH-L003"),
    Rule(("centered_zeta_chart", "reciprocal_chart"), "reciprocal_axis_invariant", ClaimStatus.EXACT, RelationKind.DUAL, "TIR centred reciprocal theorem"),
    Rule(("projective_recurrence", "spin_half"), "spinor_double_cover", ClaimStatus.STANDARD, RelationKind.HOLONOMIC, "SU(2)->SO(3)", 0.5),
    Rule(("binary_information", "twelve_projective_cycles"), "information_per_turn_ln2_over_12", ClaimStatus.MODEL, RelationKind.IMPLIES, "TIR/Metatime cycle assignment"),
    Rule(("information_per_turn_ln2_over_12", "radian_closure"), "kappa_ln2_over_24pi", ClaimStatus.MODEL, RelationKind.IMPLIES, "TIR kappa crosswalk"),
    Rule(("eight_mix_sectors", "three_flavours"), "twenty_four_count", ClaimStatus.MODEL, RelationKind.IMPLIES, "8*3=24 semantic assignment"),
    Rule(("twenty_four_count", "half_turn_phase"), "twenty_four_pi_normalization", ClaimStatus.MODEL, RelationKind.HOLONOMIC, "24 half-turn units = 12 full turns", 0.0),
    Rule(("xi_zero", "canonical_zero_state"), "native_closed", ClaimStatus.OPEN, RelationKind.IMPLIES, "SOH-C004"),
    Rule(("native_closed",), "half_axis", ClaimStatus.EXACT, RelationKind.IMPLIES, "SOH-L009"),
    Rule(("xi_zero", "half_axis"), "zero_on_half_axis", ClaimStatus.EXACT, RelationKind.IMPLIES, "definition within zero state"),
    Rule(("all_nontrivial_zeros_on_half_axis",), "riemann_hypothesis", ClaimStatus.OPEN, RelationKind.IMPLIES, "RH definition / open global bridge"),
)

DEFAULT_SOLVER = ClaimSolver(HALF_AXIS_RULES)


def bisect_root(fn, lo: float, hi: float, *, tol: float = 1e-14, max_iter: int = 256) -> float:
    """Bracketed solver for a sign-changing scalar equation."""
    flo = float(fn(lo))
    fhi = float(fn(hi))
    if flo == 0.0:
        return lo
    if fhi == 0.0:
        return hi
    if flo * fhi > 0.0:
        raise ValueError("root is not bracketed")
    a, b = float(lo), float(hi)
    for _ in range(max_iter):
        mid = 0.5 * (a + b)
        fm = float(fn(mid))
        if abs(fm) <= tol or (b - a) <= tol:
            return mid
        if flo * fm <= 0.0:
            b, fhi = mid, fm
        else:
            a, flo = mid, fm
    return 0.5 * (a + b)


def golden_section_minimum(fn, lo: float, hi: float, *, tol: float = 1e-14, max_iter: int = 256) -> float:
    """Derivative-free minimizer used for non-negative residuals that touch zero."""
    a, b = float(lo), float(hi)
    if not a < b:
        raise ValueError("lo must be less than hi")
    invphi = (math.sqrt(5.0) - 1.0) / 2.0
    c = b - invphi * (b - a)
    d = a + invphi * (b - a)
    fc = float(fn(c))
    fd = float(fn(d))
    for _ in range(max_iter):
        if b - a <= tol:
            break
        if fc <= fd:
            b, d, fd = d, c, fc
            c = b - invphi * (b - a)
            fc = float(fn(c))
        else:
            a, c, fc = c, d, fd
            d = a + invphi * (b - a)
            fd = float(fn(d))
    return 0.5 * (a + b)


def berry_holonomy(sigma: float) -> complex:
    """Holonomy for one azimuthal loop of the binary qubit family."""
    if not 0.0 <= sigma <= 1.0:
        raise ValueError("sigma must lie in [0,1]")
    phase = -2.0 * math.pi * (1.0 - sigma)
    return cmath.exp(1j * phase)


def solve_half_axis_routes() -> dict[str, float]:
    """Solve four independently formulated balance conditions."""
    complement = bisect_root(lambda s: s - (1.0 - s), 0.0, 1.0)
    entropy = bisect_root(lambda s: math.log((1.0 - s) / s), 1e-12, 1.0 - 1e-12)
    cancellation = bisect_root(
        lambda s: complementary_amplitude(s, math.pi).real,
        1e-12,
        1.0 - 1e-12,
    )
    berry = golden_section_minimum(
        lambda s: abs(berry_holonomy(s) + 1.0) ** 2,
        0.25,
        0.75,
    )
    if abs(berry_holonomy(berry) + 1.0) > 1e-10:
        raise RuntimeError("failed to isolate the interior -1 Berry-holonomy solution")
    return {
        "complement": complement,
        "entropy": entropy,
        "cancellation": cancellation,
        "berry_minus_one": berry,
    }


def route_residuals(sigma: float) -> dict[str, float]:
    """Non-negative residuals whose common zero is sigma=1/2."""
    s = float(sigma)
    if not 0.0 < s < 1.0:
        raise ValueError("sigma must lie in (0,1)")
    return {
        "complement": (2.0 * s - 1.0) ** 2,
        "entropy": LN2 - binary_entropy(s),
        "cancellation": abs(complementary_amplitude(s, math.pi)) ** 2,
        "berry_minus_one": abs(berry_holonomy(s) + 1.0) ** 2,
    }


def winding_frequency(delta_winding: float, delta_time: float) -> float:
    if delta_time <= 0.0:
        raise ValueError("delta_time must be positive")
    return float(delta_winding) / float(delta_time)


def spinor_sheet(projective_winding: int) -> int:
    if not isinstance(projective_winding, int):
        raise TypeError("projective_winding must be an integer")
    return -1 if projective_winding % 2 else 1


def information_per_projective_turn() -> float:
    """TIR/Metatime model normalization, not an established theorem."""
    return LN2 / 12.0


def kappa_from_cycle(*, closure_period: float = 2.0 * math.pi) -> float:
    if closure_period <= 0.0:
        raise ValueError("closure_period must be positive")
    return information_per_projective_turn() / closure_period


def cross_factorization_24() -> dict[str, int]:
    return {
        "mixes_x_flavours": 8 * 3,
        "projective_x_halfturns": 12 * 2,
        "spinor_x_halfturns": 6 * 4,
    }
