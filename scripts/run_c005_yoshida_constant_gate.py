#!/usr/bin/env python3
"""Emit the explicit Yoshida c=2 constant-gate receipt.

This closes only the elementary C1/C2 source constants used in the
Yoshida/Suzuki finite-codimension coercivity argument.  The gamma-window
constants t0 and C0, the operator-domain join, and RH remain open.
"""
from __future__ import annotations

import json
from pathlib import Path

from secret_of_a_half.c005_yoshida_constants import constant_gate_receipt

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "artifacts" / "receipts" / "SOH_YOSHIDA_CONSTANT_GATE_V0_1.json"


def main() -> int:
    cases = [
        {"a1": 0.25, "target_mu": 0.25},
        {"a1": 0.50, "target_mu": 0.50},
        {"a1": 1.00, "target_mu": 1.00},
        {"a1": 2.00, "target_mu": 1.00},
    ]
    rows = [constant_gate_receipt(**case) for case in cases]
    passed = all(row["source_gate_pass"] for row in rows)
    receipt = {
        "schema": "SOH_YOSHIDA_CONSTANT_GATE_SWEEP_V0_1",
        "status": "PASS_SOURCE_CONSTANTS_ONLY" if passed else "FAIL",
        "contour_c": 2.0,
        "rows": rows,
        "closed": [
            "C1 <= 5/6 at contour c=2",
            "C2(a1) <= (exp(4*a1)-1)/(4*a1)",
            "constructive choice C > 3*C1*C2 + mu",
        ],
        "open": [
            "rigorous gamma-tail threshold t0 for every chosen C",
            "rigorous compact gamma maximum C0 on |z|<=t0",
            "exact localized form/domain/boundary join",
            "uniform effective Schur gap",
            "completion null-mode exclusion",
            "SOH-C005",
            "Riemann Hypothesis",
        ],
        "proof_of_rh": False,
    }
    if not passed:
        raise SystemExit("Yoshida source constant gate failed")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
