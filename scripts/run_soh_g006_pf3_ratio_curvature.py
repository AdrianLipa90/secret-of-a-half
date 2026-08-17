#!/usr/bin/env python3
"""Finite ratio-curvature diagnostic for SOH-G006.

This script verifies the exact algebraic reconstruction of the sampled solid
order-three Toeplitz minors from adjacent coefficient ratios and records the
PF3 margin M_k. It is a falsification diagnostic only; it does not prove PF3.
"""

from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp

from secret_of_a_half.riemann_kernel import even_moment

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports" / "SOH_G006_PF3_RATIO_CURVATURE_V0_1.json"


def coefficient(k: int) -> mp.mpf:
    return even_moment(k, n_terms=10, y_cutoff=4) / mp.factorial(2 * k)


def main() -> None:
    mp.mp.dps = 60
    max_k = 10
    a = [coefficient(k) for k in range(max_k + 1)]
    r = [None] + [a[k] / a[k - 1] for k in range(1, len(a))]

    rows = []
    for k in range(2, 7):
        u = r[k] / r[k - 1]
        v = r[k + 1] / r[k]
        w = r[k + 2] / r[k + 1]
        margin = 1 - 2 * v + v**2 * (u + w - u * w)

        matrix = mp.matrix([
            [a[k], a[k + 1], a[k + 2]],
            [a[k - 1], a[k], a[k + 1]],
            [a[k - 2], a[k - 1], a[k]],
        ])
        det = mp.det(matrix)

        positive_factor = a[k - 2] ** 3 * r[k - 1] ** 2 * r[k]
        reconstructed = positive_factor * margin
        err = abs(det - reconstructed)
        tol = mp.mpf("1e-45") * max(mp.mpf("1"), abs(det), abs(reconstructed))
        if err > tol:
            raise RuntimeError(f"PF3 ratio reconstruction failed at k={k}: {err}")

        rows.append({
            "k": k,
            "u": mp.nstr(u, 40),
            "v": mp.nstr(v, 40),
            "w": mp.nstr(w, 40),
            "u_lt_v_lt_w_lt_1": bool(u < v < w < 1),
            "margin_Mk": mp.nstr(margin, 40),
            "solid_minor": mp.nstr(det, 40),
            "margin_positive": bool(margin > 0),
            "reconstruction_error": mp.nstr(err, 12),
        })

    payload = {
        "certificate": "SOH_G006_PF3_RATIO_CURVATURE_V0_1",
        "status": "FINITE_DIAGNOSTIC_NOT_PROOF",
        "proof_of_pf3": False,
        "proof_of_pf_infinity": False,
        "proof_of_rh": False,
        "exact_margin_formula": "M_k = 1 - 2 v_k + v_k^2 (u_k + w_k - u_k w_k)",
        "rows": rows,
        "all_sampled_margins_positive": all(row["margin_positive"] for row in rows),
        "all_sampled_ratio_curvature_ordered": all(row["u_lt_v_lt_w_lt_1"] for row in rows),
        "open_obligations": [
            "analytic_ratio_curvature_bound",
            "all_order_three_toeplitz_minors",
            "PF3",
            "PF_infinity",
            "SOH_G003_real_rootedness",
            "RH",
        ],
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
