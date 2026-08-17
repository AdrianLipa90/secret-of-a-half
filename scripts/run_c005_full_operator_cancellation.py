#!/usr/bin/env python3
"""Finite-ladder cancellation diagnostic for the full arithmetic Weil block.

This receipt keeps pole, conductor, archimedean and retained-prime components
separate until the final operator sum.  It measures cancellation inside the
finite declared Hermite ladder only.  It is not an infinite-complement bound,
not a localized Suzuki A_a certificate, and not a proof of SOH-C005 or RH.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from secret_of_a_half.phasenav_weil_hermite_core import HermiteLadderProgram
from secret_of_a_half.phasenav_weil_hermite_arithmetic import (
    arithmetic_rectangular_components,
)

ROOT = Path(__file__).resolve().parents[1]
PROGRAM_PATH = ROOT / "construction" / "phasenav" / "secret_of_half_weil_hermite_ladder.pnv"
OUTPUT_PATH = ROOT / "reports" / "SOH_C005_FULL_OPERATOR_CANCELLATION_V0_1.json"


def spectral_norm(matrix: np.ndarray) -> float:
    return float(np.linalg.norm(matrix, ord=2))


def main() -> None:
    program = HermiteLadderProgram.load(PROGRAM_PATH)
    cutoff = program.audit_prime_cutoff
    rows: list[dict[str, object]] = []

    for split in range(1, program.max_basis_size):
        components = arithmetic_rectangular_components(
            program,
            left_orders=range(0, split),
            right_orders=range(split, program.max_basis_size),
            prime_cutoff=cutoff,
        )
        component_norms = {
            "pole": spectral_norm(components.pole),
            "conductor": spectral_norm(components.conductor),
            "archimedean": spectral_norm(components.archimedean),
            "prime": spectral_norm(components.prime),
        }
        full_norm = spectral_norm(components.total)
        absolute_component_envelope = float(sum(component_norms.values()))
        cancellation_ratio = (
            full_norm / absolute_component_envelope
            if absolute_component_envelope > 0.0
            else 0.0
        )
        cancellation_gain = (
            absolute_component_envelope / full_norm
            if full_norm > 0.0
            else None
        )
        triangle_pass = full_norm <= absolute_component_envelope + 1e-12
        rows.append(
            {
                "split": split,
                "left_orders": [0, split - 1],
                "right_orders": [split, program.max_basis_size - 1],
                "component_norms": component_norms,
                "full_operator_norm": full_norm,
                "absolute_component_envelope": absolute_component_envelope,
                "cancellation_ratio": cancellation_ratio,
                "cancellation_gain": cancellation_gain,
                "triangle_inequality_pass": triangle_pass,
            }
        )

    receipt = {
        "program": "SOH_C005_FULL_OPERATOR_CANCELLATION",
        "version": "0.1.0",
        "status": "NUMERICAL_DIAGNOSTIC_FINITE_LADDER_ONLY",
        "basis_size": program.max_basis_size,
        "prime_cutoff": cutoff,
        "spectral_zero_input": False,
        "rows": rows,
        "all_triangle_checks_pass": all(bool(row["triangle_inequality_pass"]) for row in rows),
        "claim_boundary": {
            "exact": [
                "full rectangular block equals pole + conductor + archimedean + retained-prime components",
                "operator triangle inequality bounds full norm by sum of component norms",
            ],
            "numerical": [
                "finite-ladder component spectral norms",
                "finite-ladder cancellation ratios and gains",
            ],
            "open": [
                "uniform cancellation-sensitive control as Hermite window tends to infinity",
                "localized Suzuki A_a off-diagonal bound epsilon_Na",
                "high-index complement lower bound nu_Na",
                "SOH-C005",
                "Riemann Hypothesis",
            ],
            "proof_of_rh": False,
        },
    }
    if not receipt["all_triangle_checks_pass"]:
        raise SystemExit("triangle inequality check failed")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
