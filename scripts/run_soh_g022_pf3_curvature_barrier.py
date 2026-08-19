#!/usr/bin/env python3
"""Extended finite diagnostic for the SOH-G022 PF3 curvature barrier.

The exact theorem is algebraic.  This script only checks a finite set of
Riemann-kernel coefficients and therefore does not prove the barrier for all
indices, PF3, PF-infinity, real-rootedness, or RH.
"""

from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp

from secret_of_a_half.pf3_curvature_barrier import barrier_certificate
from secret_of_a_half.riemann_kernel import even_moment

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports" / "SOH_G022_PF3_CURVATURE_BARRIER_V0_1.json"


def coefficient(k: int) -> mp.mpf:
    return even_moment(k, n_terms=10, y_cutoff=4) / mp.factorial(2 * k)


def main() -> None:
    mp.mp.dps = 70
    max_k = 12
    a = [coefficient(k) for k in range(max_k + 1)]
    r = [None] + [a[k] / a[k - 1] for k in range(1, len(a))]
    q = [None, None] + [r[k + 1] / r[k] for k in range(1, len(r) - 1)]

    rows = []
    for k in range(2, 10):
        u = q[k]
        v = q[k + 1]
        w = q[k + 2]
        cert = barrier_certificate(u, v, w)
        scale = max(mp.mpf("1"), abs(cert["margin"]), abs(cert["decomposed_margin"]))
        residual_ok = abs(cert["decomposition_residual"]) <= mp.mpf("1e-55") * scale
        if not residual_ok:
            raise RuntimeError(f"G022 decomposition reconstruction failed at k={k}")

        rows.append(
            {
                "k": k,
                "u": mp.nstr(u, 50),
                "v": mp.nstr(v, 50),
                "w": mp.nstr(w, 50),
                "u_le_v_le_w_lt_1": bool(0 < u <= v <= w < 1),
                "barrier_Bk": mp.nstr(cert["barrier"], 50),
                "barrier_positive": bool(cert["barrier"] > 0),
                "order_gap_w_minus_v": mp.nstr(cert["order_gap"], 50),
                "order_gap_nonnegative": bool(cert["order_gap"] >= 0),
                "cubic_floor": mp.nstr(cert["cubic_floor"], 50),
                "margin_Mk": mp.nstr(cert["margin"], 50),
                "margin_minus_cubic_floor": mp.nstr(
                    cert["margin"] - cert["cubic_floor"], 50
                ),
                "certificate_assumptions_hold": bool(cert["assumptions_hold"]),
                "solid_minor_certified_positive": bool(
                    cert["solid_minor_certified_positive"]
                ),
                "decomposition_residual": mp.nstr(
                    cert["decomposition_residual"], 12
                ),
            }
        )

    payload = {
        "certificate": "SOH_G022_PF3_CURVATURE_BARRIER_V0_1",
        "status": "EXACT_SUFFICIENT_CONDITION_PLUS_FINITE_DIAGNOSTIC",
        "exact_identity": (
            "M=(1-v)^3+v(1-w)[1-v(2-u)]+v(1-v)(w-v)"
        ),
        "exact_sufficient_package": [
            "0 < v < 1",
            "v <= w <= 1",
            "1 - v(2-u) >= 0",
        ],
        "exact_consequence": "M >= (1-v)^3 > 0 for the single solid G006 minor",
        "proof_barrier_for_all_riemann_indices": False,
        "proof_all_order_three_toeplitz_minors": False,
        "proof_pf3": False,
        "proof_pf_infinity": False,
        "proof_real_rootedness": False,
        "proof_rh": False,
        "rows": rows,
        "all_sampled_ratio_curvatures_ordered": all(
            row["u_le_v_le_w_lt_1"] for row in rows
        ),
        "all_sampled_barriers_positive": all(row["barrier_positive"] for row in rows),
        "all_sampled_certificates_positive": all(
            row["solid_minor_certified_positive"] for row in rows
        ),
        "open_obligations": [
            "prove q_{k+1} >= q_k for every Riemann coefficient index",
            "prove q_k(2-q_{k-1}) <= 1 for every Riemann coefficient index",
            "upgrade solid-minor control to all order-three Toeplitz minors",
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
