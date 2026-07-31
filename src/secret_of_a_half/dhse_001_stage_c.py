"""DHSE-001 Stage C: analytic diagnosis of the Möbius-skew Stage B signal."""
from __future__ import annotations

from fractions import Fraction

from .dhse_001 import LEFT, RIGHT, branch_stream, initial_odds
from .dhse_001_stage_b import (
    BASE_SEED,
    BURN_IN,
    ENSEMBLE_SIZE,
    FAMILIES,
    RADIUS,
    STEPS,
    TARGET,
    projective_residual,
    trajectory,
)


def mobius_skew_family():
    return next(family for family in FAMILIES if family.name == "mobius_skew")


def lr_composition(z: Fraction) -> Fraction:
    value = Fraction(z)
    if value <= 0:
        raise ValueError("projective odds must be positive")
    return Fraction(5 * value + 6, 5 * value + 7)


def lr_residual(z: Fraction) -> Fraction:
    value = Fraction(z)
    if value <= 0:
        raise ValueError("projective odds must be positive")
    return Fraction(1, 10 * value + 13)


def run_stage_c() -> dict[str, object]:
    family = mobius_skew_family()
    observed = 0
    target_hits = 0
    lr_words = 0
    equivalence_matches = 0
    counterexamples: list[dict[str, object]] = []

    for index in range(ENSEMBLE_SIZE):
        seed = f"{BASE_SEED}:stage-b:{index:03d}"
        stream = branch_stream(seed)
        branches = tuple(next(stream) for _ in range(STEPS))
        states = trajectory(family, initial_odds(seed), branches)
        for step in range(BURN_IN, STEPS + 1):
            observed += 1
            hit = projective_residual(states[step], TARGET) <= RADIUS
            lr = step >= 2 and branches[step - 2] == LEFT and branches[step - 1] == RIGHT
            target_hits += int(hit)
            lr_words += int(lr)
            equivalence_matches += int(hit == lr)
            if hit != lr and len(counterexamples) < 8:
                counterexamples.append(
                    {
                        "seed_index": index,
                        "step": step,
                        "hit": hit,
                        "lr_word": lr,
                    }
                )

    exact_mechanism = (
        target_hits == lr_words
        and equivalence_matches == observed
        and not counterexamples
    )

    return {
        "experiment": "DHSE-001",
        "stage": "C-analytic-mechanism-diagnosis",
        "operator_family": "mobius_skew",
        "composition": {
            "word": "LR",
            "meaning": "apply L, then R",
            "matrix": [[5, 6], [5, 7]],
            "map": "(5*z+6)/(5*z+7)",
        },
        "theorem": {
            "domain": "z>0",
            "image_interval": "6/7 < R(L(z)) < 1",
            "target_residual": "d_1(R(L(z)))=1/(10*z+13)<1/13<1/10",
            "therefore": "every LR word forces a Stage B target hit",
        },
        "audit": {
            "observed_states": observed,
            "target_hits": target_hits,
            "lr_words": lr_words,
            "hit_iff_lr_matches": equivalence_matches,
            "counterexamples": counterexamples,
        },
        "technical_status": "PASS" if exact_mechanism else "FAIL",
        "scientific_status": (
            "OPERATOR_WORD_ARTIFACT_IDENTIFIED"
            if exact_mechanism
            else "MECHANISM_NOT_CLOSED"
        ),
        "interpretation": (
            "The Stage B mobius_skew signal is completely explained by the LR "
            "two-step composition and the preregistered radius. It is not independent "
            "evidence for a universal halfway attractor."
        ),
    }
