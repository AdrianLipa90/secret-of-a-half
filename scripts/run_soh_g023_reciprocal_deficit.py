#!/usr/bin/env python3
"""Finite Riemann diagnostic for the SOH-G023 reciprocal-deficit frontier.

The exact normal form is algebraic.  This receipt samples only finitely many
Riemann-kernel moments and therefore does not prove the monotone 1-Lipschitz
law globally, PF3, PF-infinity, real-rootedness, or RH.
"""

from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp

from secret_of_a_half.pf3_reciprocal_deficit import (
    lipschitz_certificate,
    reciprocal_deficit,
)
from secret_of_a_half.riemann_kernel import even_moment

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports" / "SOH_G023_RECIPROCAL_DEFICIT_V0_1.json"


def coefficient(k: int) -> mp.mpf:
    return even_moment(k, n_terms=10, y_cutoff=4) / mp.factorial(2 * k)


def main() -> None:
    mp.mp.dps = 70
    max_k = 13
    a = [coefficient(k) for k in range(max_k + 1)]
    r = [None] + [a[k] / a[k - 1] for k in range(1, len(a))]
    q = [None, None] + [r[k + 1] / r[k] for k in range(1, len(r) - 1)]
    E = [None, None] + [reciprocal_deficit(q[k]) for k in range(2, len(q))]

    rows = []
    for k in range(3, 11):
        E_prev = E[k - 1]
        Ek = E[k]
        E_next = E[k + 1]
        cert = lipschitz_certificate(E_prev, Ek, E_next)
        scale = max(mp.mpf("1"), abs(cert["transformed_margin"]))
        if abs(cert["decomposition_residual"]) > mp.mpf("1e-55") * scale:
            raise RuntimeError(f"G023 transformed-margin reconstruction failed at k={k}")
        rows.append(
            {
                "k": k,
                "E_prev": mp.nstr(E_prev, 50),
                "E": mp.nstr(Ek, 50),
                "E_next": mp.nstr(E_next, 50),
                "alpha": mp.nstr(cert["alpha"], 50),
                "beta": mp.nstr(cert["beta"], 50),
                "alpha_in_0_1": bool(0 <= cert["alpha"] <= 1),
                "beta_nonnegative": bool(cert["beta"] >= 0),
                "transformed_margin": mp.nstr(cert["transformed_margin"], 50),
                "decomposition_residual": mp.nstr(cert["decomposition_residual"], 12),
                "certificate_assumptions_hold": bool(cert["assumptions_hold"]),
                "solid_minor_certified_positive": bool(cert["solid_minor_certified_positive"]),
            }
        )

    increments = [E[k + 1] - E[k] for k in range(2, len(E) - 1)]
    payload = {
        "certificate": "SOH_G023_RECIPROCAL_DEFICIT_V0_1",
        "status": "EXACT_NORMAL_FORM_PLUS_FINITE_DIAGNOSTIC",
        "exact_normal_form": (
            "M=[E_{k-1}E_{k+1}-(E_k-1)^2]/"
            "[E_{k-1}E_k^2E_{k+1}]"
        ),
        "exact_increment_decomposition": (
            "Mhat=(E_k-1)+E_k(1-alpha_k)+E_{k-1}beta_k"
        ),
        "global_target": "0 <= E_{k+1}-E_k <= 1",
        "all_sampled_increments_in_0_1": all(0 <= x <= 1 for x in increments),
        "all_sampled_certificates_positive": all(
            row["solid_minor_certified_positive"] for row in rows
        ),
        "sampled_increment_min": mp.nstr(min(increments), 50),
        "sampled_increment_max": mp.nstr(max(increments), 50),
        "rows": rows,
        "proof_global_one_lipschitz_law": False,
        "proof_all_solid_minors": False,
        "proof_all_order_three_toeplitz_minors": False,
        "proof_pf3": False,
        "proof_pf_infinity": False,
        "proof_real_rootedness": False,
        "proof_rh": False,
        "open_obligations": [
            "prove E_{k+1} >= E_k for every actual Riemann coefficient index",
            "prove E_{k+1}-E_k <= 1 for every actual Riemann coefficient index",
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
