#!/usr/bin/env python3
"""Growing-M diagnostic for the full arithmetic Weil rectangular block.

This extends only the *diagnostic* Hermite ladder size while preserving every
other parameter from the canonical profile.  It is not a proof of infinite-
complement convergence and does not alter the canonical PhaseNav profile.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from secret_of_a_half.phasenav_weil_hermite_core import HermiteLadderProgram, default_program_path
from secret_of_a_half.phasenav_weil_hermite_arithmetic import arithmetic_rectangular_components

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "artifacts" / "receipts" / "SOH_C005_FULL_OPERATOR_STABILITY_V0_1.json"


def extended_profile(max_basis_size: int) -> HermiteLadderProgram:
    base = HermiteLadderProgram.load(default_program_path())
    equations = dict(base.equations)
    equations["MAX_BASIS_SIZE"] = str(max_basis_size)
    profile = HermiteLadderProgram(base.path, equations)
    profile.validate()
    return profile


def spectral_norm(a: np.ndarray) -> float:
    return float(np.linalg.norm(a, ord=2))


def main() -> None:
    low_size = 2
    windows = (4, 6, 8, 10, 12)
    rows = []
    for stop in windows:
        profile = extended_profile(stop)
        comp = arithmetic_rectangular_components(
            profile,
            left_orders=range(low_size),
            right_orders=range(low_size, stop),
            prime_cutoff=profile.audit_prime_cutoff,
        )
        component_norms = {
            "pole": spectral_norm(comp.pole),
            "conductor": spectral_norm(comp.conductor),
            "archimedean": spectral_norm(comp.archimedean),
            "prime": spectral_norm(comp.prime),
        }
        total = spectral_norm(comp.total)
        triangle = sum(component_norms.values())
        rows.append(
            {
                "M": stop,
                "N": low_size,
                "full_block_norm": total,
                "component_norms": component_norms,
                "component_norm_sum": triangle,
                "cancellation_ratio": total / triangle if triangle else 0.0,
                "cancellation_gain": triangle - total,
                "triangle_pass": total <= triangle + 1e-10,
            }
        )

    receipt = {
        "program": "SOH_C005_FULL_OPERATOR_STABILITY",
        "version": "0.1.0",
        "status": "NUMERICAL_DIAGNOSTIC_NOT_PROOF",
        "basis_center_source": "canonical translated Hermite profile",
        "canonical_profile_mutated": False,
        "fixed_low_block_N": low_size,
        "growing_windows": list(windows),
        "rows": rows,
        "all_triangle_checks_pass": all(r["triangle_pass"] for r in rows),
        "claim_boundary": {
            "exact": [
                "same full arithmetic Weil component formulas are used in every finite window",
                "triangle inequality is checked for every reported rectangular block",
            ],
            "numerical": [
                "finite prime cutoff and finite Hermite windows only",
                "reported cancellation ratios and full-block norms",
            ],
            "open": [
                "M to infinity convergence",
                "cutoff removal uniformly in M",
                "localized Suzuki A_a off-diagonal bound",
                "positive infinite complement lower bound",
                "SOH-C005",
                "Riemann Hypothesis",
            ],
            "proof_of_rh": False,
        },
    }
    if not receipt["all_triangle_checks_pass"]:
        raise SystemExit("full-operator stability triangle gate failed")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
