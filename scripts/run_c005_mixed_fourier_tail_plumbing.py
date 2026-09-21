#!/usr/bin/env python3
"""Exercise the generic mixed Fourier-tail plumbing on synthetic envelopes."""
from __future__ import annotations

import json
from pathlib import Path

from secret_of_a_half.c005_mixed_fourier_tail import (
    KernelRegularityEnvelope,
    cutoff_for_mixed_norm,
    mixed_tail_gate_map,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "artifacts" / "receipts" / "SOH_C005_MIXED_FOURIER_TAIL_PLUMBING_V0_1.json"


def main() -> int:
    fixtures = [
        KernelRegularityEnvelope(a=0.5, boundary_jump_l2_sq=1.0, du_l2_sq=2.0),
        KernelRegularityEnvelope(a=1.0, boundary_jump_l2_sq=2.0, du_l2_sq=4.0),
    ]
    rows = []
    for env in fixtures:
        cert = cutoff_for_mixed_norm(env, target_epsilon=0.1)
        rows.append(
            {
                "a": env.a,
                "boundary_jump_l2_sq": env.boundary_jump_l2_sq,
                "du_l2_sq": env.du_l2_sq,
                "target_epsilon": 0.1,
                "cutoff_N": cert.cutoff_N,
                "certified_norm_upper": cert.norm_upper,
                "pass": cert.norm_upper <= 0.1,
            }
        )

    receipt = {
        "schema": "SOH_C005_MIXED_FOURIER_TAIL_PLUMBING_V0_1",
        "status": (
            "PASS_SYNTHETIC_PLUMBING_ONLY"
            if all(row["pass"] for row in rows)
            else "FAIL"
        ),
        "synthetic_regularity_envelopes": True,
        "rows": rows,
        "gate_map": mixed_tail_gate_map(),
        "claim_boundary": {
            "not_instantiated": [
                "actual zeta screw-kernel derivative norm",
                "actual boundary-jump norm",
                "uniform a-cell kernel regularity constants",
            ],
            "proof_of_rh": False,
        },
    }

    if receipt["status"] != "PASS_SYNTHETIC_PLUMBING_ONLY":
        raise SystemExit("mixed Fourier-tail plumbing failed")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
