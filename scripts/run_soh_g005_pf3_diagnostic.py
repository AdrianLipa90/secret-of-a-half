#!/usr/bin/env python3
"""Finite PF3 diagnostic for the SOH-G005 coefficient hierarchy.

This script does not prove PF3 or PF_infinity.  It evaluates a finite set of
solid order-three Toeplitz minors for the positive coefficient sequence

    a_k = mu_{2k}/(2k)!,

where mu_{2k} are moments of the exact positive Riemann kernel.  The purpose is
falsification: any negative minor would kill this PF3 route immediately.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import mpmath as mp

from secret_of_a_half.riemann_kernel import even_moment

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports" / "SOH_G005_PF3_FINITE_DIAGNOSTIC_V0_1.json"


def coefficient(k: int) -> mp.mpf:
    if k < 0:
        return mp.mpf("0")
    return even_moment(k, n_terms=10, y_cutoff=4) / mp.factorial(2 * k)


def solid_toeplitz_minor(coeffs: list[mp.mpf], offset: int, order: int) -> mp.mpf:
    matrix = mp.matrix(order)
    for i in range(order):
        for j in range(order):
            idx = offset + j - i
            matrix[i, j] = coeffs[idx] if 0 <= idx < len(coeffs) else mp.mpf("0")
    return mp.det(matrix)


def main() -> None:
    mp.mp.dps = 50
    max_k = 9
    coeffs = [coefficient(k) for k in range(max_k + 1)]

    rows = []
    for offset in range(1, 7):
        det = solid_toeplitz_minor(coeffs, offset, 3)
        if not mp.isfinite(det):
            raise RuntimeError(f"non-finite PF3 minor at offset={offset}")
        rows.append({
            "offset": offset,
            "order": 3,
            "determinant": mp.nstr(det, 40),
            "positive": bool(det > 0),
        })

    payload = {
        "certificate": "SOH_G005_PF3_FINITE_DIAGNOSTIC_V0_1",
        "status": "FINITE_DIAGNOSTIC_NOT_PROOF",
        "proof_of_pf3": False,
        "proof_of_pf_infinity": False,
        "proof_of_rh": False,
        "coefficient_definition": "a_k = integral_0^infinity Phi(y) y^(2k) dy / (2k)!",
        "moment_controls": {
            "mp_dps": 50,
            "n_terms": 10,
            "y_cutoff": 4,
            "max_k": max_k,
        },
        "solid_order_three_minors": rows,
        "all_sampled_positive": all(row["positive"] for row in rows),
        "open_obligations": [
            "analytic_PF3_all_minors",
            "PF_order_hierarchy_beyond_3",
            "PF_infinity_or_equivalent_zero_preserving_bridge",
            "SOH_G003_real_rootedness",
            "RH",
        ],
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
