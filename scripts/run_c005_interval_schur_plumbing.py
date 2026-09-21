#!/usr/bin/env python3
"""Exercise interval-Schur plumbing without making a physics claim."""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from secret_of_a_half.c005_interval_schur import (
    continuation_cell,
    cover_is_strict,
    interval_gate_map,
    interval_schur_from_matrix_enclosures,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "artifacts" / "receipts" / "SOH_C005_INTERVAL_SCHUR_PLUMBING_V0_1.json"


def main() -> int:
    # Synthetic deterministic fixture: validates propagation logic only.
    low_mid = np.array([[3.0, 0.10], [0.10, 2.50]], dtype=complex)
    high_mid = np.array([[4.0, 0.20], [0.20, 3.50]], dtype=complex)
    coupling_mid = np.array([[0.15, 0.05], [0.10, 0.10]], dtype=complex)

    low_rad = np.full((2, 2), 1e-3)
    high_rad = np.full((2, 2), 1e-3)
    coupling_rad = np.full((2, 2), 1e-3)

    low, coupling, high, schur = interval_schur_from_matrix_enclosures(
        low_mid,
        low_rad,
        coupling_mid,
        coupling_rad,
        high_mid,
        high_rad,
    )

    cells = [
        continuation_cell(center=0.5, halfwidth=0.5, center_gap_lower=0.8, lipschitz_upper=0.2),
        continuation_cell(center=1.5, halfwidth=0.5, center_gap_lower=0.7, lipschitz_upper=0.2),
        continuation_cell(center=2.5, halfwidth=0.5, center_gap_lower=0.6, lipschitz_upper=0.2),
    ]

    plumbing_pass = (
        low.positive
        and high.positive
        and schur.strict
        and cover_is_strict(cells, 0.0, 3.0)
    )

    receipt = {
        "schema": "SOH_C005_INTERVAL_SCHUR_PLUMBING_V0_1",
        "status": "PASS_SYNTHETIC_PLUMBING_ONLY" if plumbing_pass else "FAIL",
        "synthetic_fixture": True,
        "low": low.__dict__,
        "coupling": coupling.__dict__,
        "high": high.__dict__,
        "schur": schur.__dict__,
        "continuation_cells": [
            {
                **cell.__dict__,
                "interval": list(cell.interval),
                "strict": cell.strict,
            }
            for cell in cells
        ],
        "gate_map": interval_gate_map(),
        "claim_boundary": {
            "exact": [
                "matrix perturbation inequalities used by the plumbing",
                "scalar Schur propagation",
                "continuation-cover logic",
            ],
            "not_instantiated": [
                "localized Suzuki matrix entries",
                "entrywise interval radii from analytic/interval evaluation",
                "physical a-dependent Lipschitz constants",
            ],
            "proof_of_rh": False,
        },
    }

    if not plumbing_pass:
        raise SystemExit("interval Schur plumbing fixture failed")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
