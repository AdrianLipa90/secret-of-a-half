#!/usr/bin/env python3
"""Emit explicit source-level Yoshida high-mode coercivity receipts."""
from __future__ import annotations

import json
from pathlib import Path

from secret_of_a_half.c005_yoshida_high_mode import high_mode_gate_receipt

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "artifacts" / "receipts" / "SOH_YOSHIDA_EXPLICIT_HIGH_MODE_COERCIVITY_V0_1.json"


def main() -> int:
    cases = [
        {"a0": "0.05", "a1": "0.06", "target_mu": "0.10"},
        {"a0": "0.10", "a1": "0.11", "target_mu": "0.10"},
        {"a0": "0.25", "a1": "0.26", "target_mu": "0.25"},
        {"a0": "0.50", "a1": "0.51", "target_mu": "0.50"},
    ]
    rows = [high_mode_gate_receipt(**case) for case in cases]
    passed = all(bool(row["source_level_gate_pass"]) for row in rows)
    receipt = {
        "schema": "SOH_YOSHIDA_EXPLICIT_HIGH_MODE_COERCIVITY_SWEEP_V0_1",
        "status": "PASS_SOURCE_LEVEL_HIGH_MODE_ONLY" if passed else "FAIL",
        "rows": rows,
        "claim_boundary": {
            "closed": [
                "source equation (4.11) coefficient bookkeeping",
                "explicit conservative high-mode cutoff on each declared bounded scale",
            ],
            "open": [
                "repository-to-Suzuki localized operator/domain/Friedrichs join",
                "low/high coupling and finite Schur gap",
                "all-scale continuation",
                "completion null-mode exclusion",
                "SOH-C005",
                "Riemann Hypothesis",
            ],
            "proof_of_rh": False,
        },
    }
    if not passed:
        raise SystemExit("explicit Yoshida high-mode gate failed")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
