#!/usr/bin/env python3
"""Finite Hermite Schur diagnostic for the natural C005 flow.

This is deliberately a scouting receipt.  It uses the existing finite Hermite
arithmetic matrix, not Suzuki's exact localized Fourier operator, so it cannot
be promoted to a C005 certificate.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from secret_of_a_half.phasenav_weil_hermite_core import (
    HermiteLadderProgram,
    default_program_path,
)
from secret_of_a_half.phasenav_weil_hermite_arithmetic import arithmetic_matrix
from secret_of_a_half.c005_yoshida_resolvent import (
    scalar_block_lower_eigenvalue,
    scalar_schur_certificate,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "artifacts" / "receipts" / "SOH_C005_FINITE_SCHUR_DIAGNOSTIC_V0_1.json"


def eigmin(matrix: np.ndarray) -> float:
    return float(np.min(np.linalg.eigvalsh(matrix)))


def main() -> int:
    program = HermiteLadderProgram.load(default_program_path())
    matrix, _ = arithmetic_matrix(
        program,
        basis_size=program.max_basis_size,
        prime_cutoff=program.audit_prime_cutoff,
    )

    rows: list[dict[str, object]] = []
    for split in range(1, program.max_basis_size):
        low = matrix[:split, :split]
        coupling = matrix[:split, split:]
        high = matrix[split:, split:]

        mu = eigmin(low)
        nu = eigmin(high)
        epsilon = float(np.linalg.norm(coupling, ord=2))
        scalar = scalar_schur_certificate(mu, epsilon, nu)
        scalar_gap = scalar_block_lower_eigenvalue(mu, epsilon, nu)

        row: dict[str, object] = {
            "split_N": split,
            "M": program.max_basis_size,
            "mu_low_eigmin": mu,
            "epsilon_coupling_norm": epsilon,
            "nu_high_eigmin": nu,
            "scalar_determinant_margin": scalar.determinant_margin,
            "scalar_lower_eigenvalue": scalar_gap,
            "high_block_invertible_positive": bool(nu > program.psd_tolerance),
            "schur_available": False,
            "schur_eigmin": None,
        }

        if nu > program.psd_tolerance:
            solved = np.linalg.solve(high, coupling.conjugate().T)
            schur = low - coupling @ solved
            schur = 0.5 * (schur + schur.conjugate().T)
            row["schur_available"] = True
            row["schur_eigmin"] = eigmin(schur)

        rows.append(row)

    receipt = {
        "schema": "SOH_C005_FINITE_SCHUR_DIAGNOSTIC_V0_1",
        "status": "NUMERICAL_DIAGNOSTIC_NOT_PROOF",
        "basis": "translated-scaled Hermite",
        "localized_suzuki_operator": False,
        "basis_size": program.max_basis_size,
        "prime_cutoff": program.audit_prime_cutoff,
        "rows": rows,
        "claim_boundary": {
            "numerical": [
                "finite Hermite principal matrix only",
                "finite high-block inversion only when numerically positive",
                "finite Schur eigenvalues and scalar envelopes",
            ],
            "open": [
                "localized Fourier-domain operator equality",
                "infinite high-mode resolvent",
                "uniform Schur gap in a",
                "completion null-mode exclusion",
                "SOH-C005",
                "Riemann Hypothesis",
            ],
            "proof_of_rh": False,
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
