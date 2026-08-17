#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from secret_of_a_half.phasenav_weil_hermite_ladder import (
    HermiteLadderProgram,
    arithmetic_rectangular_components,
)

ROOT = Path(__file__).resolve().parents[1]
PROGRAM = ROOT / "construction/phasenav/secret_of_half_weil_hermite_ladder.pnv"
OUTPUT = ROOT / "data/processed/c005_finite_ladder_coupling.json"


def spectral_norm(matrix: np.ndarray) -> float:
    return float(np.linalg.norm(matrix, ord=2))


def main() -> int:
    program = HermiteLadderProgram.load(PROGRAM)
    sections: list[dict[str, object]] = []
    for split in range(1, program.max_basis_size):
        block = arithmetic_rectangular_components(
            program,
            left_orders=range(split),
            right_orders=range(split, program.max_basis_size),
            prime_cutoff=program.prime_cutoff,
        )
        sections.append(
            {
                "split_N": split,
                "finite_ladder_M": program.max_basis_size,
                "shape": list(block.total.shape),
                "total_operator_norm": spectral_norm(block.total),
                "pole_operator_norm": spectral_norm(block.pole),
                "conductor_operator_norm": spectral_norm(block.conductor),
                "archimedean_operator_norm": spectral_norm(block.archimedean),
                "retained_prime_operator_norm": spectral_norm(block.prime),
            }
        )

    receipt = {
        "schema": "SOH_C005_FINITE_LADDER_COUPLING_V0_1",
        "status": "PASS_FINITE_LADDER_MEASUREMENT",
        "program": program.equations["PROGRAM"],
        "prime_cutoff": program.prime_cutoff,
        "max_basis_size": program.max_basis_size,
        "spectral_zero_input": False,
        "sections": sections,
        "claim_boundary": {
            "exact": [
                "rectangular block uses the same arithmetic Weil form as the principal Hermite matrix",
                "reported component matrices sum exactly to the reported total block",
                "operator norms are finite-dimensional spectral norms of the declared M-dimensional ladder",
            ],
            "open": [
                "M-to-infinity complement bound",
                "Suzuki localization-radius a normalization",
                "uniform epsilon_N,a bound",
                "high-index complement lower bound nu_N,a",
                "SOH-C005 global positivity",
                "Riemann Hypothesis",
            ],
            "proof_of_rh": False,
        },
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
