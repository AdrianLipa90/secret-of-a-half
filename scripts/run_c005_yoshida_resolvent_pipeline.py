#!/usr/bin/env python3
"""Emit the fail-closed Yoshida Fourier -> resolvent -> Schur pipeline receipt."""
from __future__ import annotations

import json
from pathlib import Path

from secret_of_a_half.c005_yoshida_resolvent import (
    cutoff_for_leakage,
    pipeline_gate_map,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "artifacts" / "receipts" / "SOH_C005_YOSHIDA_RESOLVENT_PIPELINE_V0_1.json"


def main() -> int:
    # Deterministic schedule diagnostics only.  These numbers are not physical
    # constants and are not used as a proof certificate for the Weil operator.
    cases = [
        {"a0": 0.5, "t0": 1.0, "tolerance": 1e-3},
        {"a0": 1.0, "t0": 1.0, "tolerance": 1e-3},
        {"a0": 2.0, "t0": 1.0, "tolerance": 1e-3},
        {"a0": 2.0, "t0": 2.0, "tolerance": 1e-4},
    ]
    rows = []
    for case in cases:
        item = cutoff_for_leakage(**case)
        rows.append(
            {
                "a0": item.a0,
                "t0": item.t0,
                "tolerance": item.tolerance,
                "cutoff_N": item.cutoff,
                "B": item.coefficient,
                "certified_leakage_upper": item.certified_bound,
                "pass": item.pass_bound,
            }
        )

    gate_map = pipeline_gate_map()
    receipt = {
        "schema": gate_map["schema"],
        "status": (
            "PASS_ANALYTIC_PLUMBING_ONLY"
            if all(row["pass"] for row in rows)
            else "FAIL"
        ),
        "rows": rows,
        "pipeline": gate_map,
        "normalization_crosswalk_certified": False,
        "coercivity_nu_instantiated": False,
        "coupling_epsilon_instantiated": False,
        "finite_low_floor_mu_instantiated": False,
        "strict_schur_margin_instantiated": False,
        "spectral_nondegeneracy_proved": False,
        "proof_of_rh": False,
    }

    if receipt["status"] != "PASS_ANALYTIC_PLUMBING_ONLY":
        raise SystemExit("Yoshida Fourier leakage schedule failed")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
