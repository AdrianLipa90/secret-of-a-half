#!/usr/bin/env python3
"""Emit explicit Yoshida gamma-window certificates for deterministic targets."""
from __future__ import annotations

import json
from pathlib import Path

from secret_of_a_half.c005_yoshida_gamma_window import gamma_window_gate_receipt

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "artifacts" / "receipts" / "SOH_YOSHIDA_GAMMA_WINDOW_V0_1.json"


def main() -> int:
    targets = ("1", "5", "10", "25")
    rows = [gamma_window_gate_receipt(C) for C in targets]
    passed = all(bool(row["tail_gate_pass"]) for row in rows)
    receipt = {
        "schema": "SOH_YOSHIDA_GAMMA_WINDOW_SWEEP_V0_1",
        "status": "PASS_EXPLICIT_GAMMA_WINDOW_ONLY" if passed else "FAIL",
        "rows": rows,
        "claim_boundary": {
            "closed": [
                "DLMF-based explicit t0(C) tail threshold",
                "DLMF-based explicit compact C0 upper envelope",
            ],
            "open": [
                "exact Suzuki (4.11) coefficient extraction in repository normalization",
                "localized form/domain/boundary/Friedrichs join",
                "constant optimization for useful all-scale schedules",
                "uniform effective Schur gap",
                "completion null-mode exclusion",
                "SOH-C005",
                "Riemann Hypothesis",
            ],
            "proof_of_rh": False,
        },
    }
    if not passed:
        raise SystemExit("Yoshida gamma-window gate failed")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
