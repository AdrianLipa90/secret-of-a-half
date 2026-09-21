#!/usr/bin/env python3
"""Emit unconditional zeta-screw L2 and mixed-tail envelope receipts."""
from __future__ import annotations

import json
from pathlib import Path

from secret_of_a_half.c005_screw_analytic_bounds import screw_analytic_gate_receipt

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "artifacts" / "receipts" / "SOH_ZETA_SCREW_ANALYTIC_ENVELOPES_V0_1.json"


def main() -> int:
    cases = [
        {"a0": 0.10, "target_epsilon": 0.10},
        {"a0": 0.25, "target_epsilon": 0.10},
        {"a0": 0.50, "target_epsilon": 0.10},
    ]
    rows = [screw_analytic_gate_receipt(**case) for case in cases]
    passed = all(bool(row["mixed_gate_pass"]) for row in rows)
    receipt = {
        "schema": "SOH_ZETA_SCREW_ANALYTIC_ENVELOPES_SWEEP_V0_1",
        "status": "PASS_ANALYTIC_MIXED_TAIL_ONLY" if passed else "FAIL",
        "rows": rows,
        "claim_boundary": {
            "closed": [
                "closed-form unconditional screw-function L2 envelope",
                "closed-form unconditional a.e.-derivative L2 envelope",
                "uniform mixed Fourier-tail cutoff on each declared bounded scale",
            ],
            "open": [
                "finite localized low Fourier block interval enclosure",
                "uniform low-block/Schur continuation",
                "SOH-C005",
                "Riemann Hypothesis",
            ],
            "proof_of_rh": False,
        },
    }
    if not passed:
        raise SystemExit("zeta screw analytic envelope gate failed")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
