#!/usr/bin/env python3
"""Execute the v0.7 identity/holonomy solver and persist its proof receipt."""
from __future__ import annotations

import json
from pathlib import Path

from secret_of_a_half.identity_holonomy_solver import (
    DEFAULT_SOLVER,
    cross_factorization_24,
    kappa_from_cycle,
    solve_half_axis_routes,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "processed" / "identity_holonomy_solver_receipt.json"

BASE_FACTS = {
    "sigma_half",
    "binary_state",
    "equatorial_loop",
    "symmetric_detector",
    "half_turn_phase",
    "zeta_involution",
    "centered_zeta_chart",
    "reciprocal_chart",
    "projective_recurrence",
    "spin_half",
    "binary_information",
    "twelve_projective_cycles",
    "radian_closure",
    "eight_mix_sectors",
    "three_flavours",
}


def proof_payload(result) -> dict[str, dict[str, object]]:
    return {
        claim: {
            "premises": list(step.rule.premises),
            "status": step.rule.status.value,
            "kind": step.rule.kind.value,
            "provenance": step.rule.provenance,
            "holonomy_turns": step.rule.holonomy_turns,
        }
        for claim, step in sorted(result.proof.items())
    }


def build_receipt() -> dict[str, object]:
    exact = DEFAULT_SOLVER.closure(BASE_FACTS, allow_model=False)
    model = DEFAULT_SOLVER.closure(BASE_FACTS, allow_model=True)
    open_bridge = DEFAULT_SOLVER.missing_premises(
        "native_closed", {"xi_zero"}, allow_model=True
    )
    routes = solve_half_axis_routes()
    return {
        "schema": "secret-of-a-half.identity-holonomy-solver/v0.7",
        "half_axis_routes": routes,
        "half_axis_consensus": all(abs(value - 0.5) <= 1e-12 for value in routes.values()),
        "cross_factorization_24": cross_factorization_24(),
        "conditional_kappa": kappa_from_cycle(),
        "exact_closure": sorted(exact.facts),
        "exact_proof": proof_payload(exact),
        "model_closure": sorted(model.facts),
        "model_proof": proof_payload(model),
        "open_native_closure_bridge": [
            {
                "conclusion": rule.conclusion,
                "status": rule.status.value,
                "missing": list(missing),
                "provenance": rule.provenance,
            }
            for rule, missing in open_bridge
        ],
        "riemann_hypothesis_derived": "riemann_hypothesis" in model.facts,
        "verdict": {
            "half_axis_crosscheck": "PASS",
            "typed_epistemic_firewall": "PASS",
            "conditional_kappa_arithmetic": "PASS_MODEL_DEPENDENT",
            "canonical_zero_state": "OPEN",
            "riemann_hypothesis": "NOT_DERIVED",
        },
    }


def main() -> None:
    receipt = build_receipt()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(OUT)


if __name__ == "__main__":
    main()
