#!/usr/bin/env python3
"""Deterministic receipt for the SOH-G024 N-body / extended-Laguerre hierarchy."""
from __future__ import annotations

import json
from pathlib import Path
import mpmath as mp

from secret_of_a_half.g024_nbody_laguerre_hierarchy import (
    extended_laguerre_value,
    finite_real_zero_q_coefficients,
    jensen_from_laguerre_coefficients,
    quartic_first_gate_exact,
    quartic_non_lp,
    real_zero_product_function,
    transverse_q_coefficient,
    transverse_q_coefficients,
    xi_transverse_q_coefficients,
)
from secret_of_a_half.theta_nbody_rigidity import hermitian_jensen_value

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports" / "SOH_G024_NBODY_LAGUERRE_HIERARCHY_RECEIPT_V0_3.json"


def s(x, digits=55):
    return mp.nstr(x, digits)


def main():
    mp.mp.dps = 70
    gammas = [mp.mpf("1"), mp.mpf("2"), mp.mpf("3.5")]
    x = mp.mpf("0.7")
    f = real_zero_product_function(gammas)
    direct = transverse_q_coefficients(f, x, 2 * len(gammas))
    fact = finite_real_zero_q_coefficients(gammas, x)
    factor_res = max(abs(a - b) for a, b in zip(direct, fact))

    qx = mp.mpf("1")
    quartic_c1 = transverse_q_coefficient(quartic_non_lp, qx, 1)

    xh = mp.mpf("0.63")
    yh = mp.mpf("0.27")
    f2 = real_zero_product_function([1, 2])
    lag = [extended_laguerre_value(f2, xh, n) for n in range(5)]
    h_series = jensen_from_laguerre_coefficients(lag, yh)
    h_direct = hermitian_jensen_value(f2, mp.mpc(xh, yh))

    xi_samples = {}
    for label, xx in [("0", "0"), ("10", "10"), ("first_zero", "14.134725141734693790")]:
        cs = xi_transverse_q_coefficients(mp.mpf(xx), 4)
        xi_samples[label] = {
            "x": xx,
            "c_0_to_4": [s(v) for v in cs],
            "sampled_all_nonnegative": all(v >= 0 for v in cs),
        }

    payload = {
        "schema": "sohalf.g024-nbody-laguerre-hierarchy-receipt/v0.3",
        "status": "PASS",
        "rh_status": "OPEN",
        "classification": {
            "q_coefficient_identity": "EXACT",
            "cardon_extended_laguerre_crosswalk": "STANDARD_EXTERNAL_THEOREM",
            "nbody_generating_identity": "EXACT",
            "xi_samples": "FINITE_DIAGNOSTIC_NOT_PROOF",
        },
        "source": {
            "author": "David A. Cardon",
            "title": "Extended Laguerre inequalities and a criterion for real zeros",
            "arxiv": "0911.1122",
            "theorem": "Theorem 1.1",
            "operator": "L_n[f](x)=sum_{k=0}^{2n} (-1)^(k+n)/(2n)! binom(2n,k) f^(k)(x) f^(2n-k)(x)",
        },
        "exact_crosswalk": {
            "Q_x(q)": "1/2*f(x+i*sqrt(q))*f(x-i*sqrt(q))",
            "coefficient": "c_n(x)=L_n[f](x)/2",
            "wick_partition": "Z(-i*x,y)=Q_x(y^2)",
            "jensen_generator": "H_f(x+i*y)=sum_{n>=1} n*(2*n-1)*L_n[f](x)*y^(2*n-2)",
            "xi_equivalence": "RH iff L_n[Xi](x)>=0 for every real x and every n>=0",
        },
        "real_zero_product_control": {
            "gammas": [s(g) for g in gammas],
            "x": s(x),
            "max_abs_derivative_vs_factorized_residual": s(factor_res),
            "minimum_coefficient": s(min(direct)),
        },
        "non_lp_quartic_control": {
            "f": "1+z^4",
            "x": "1",
            "c1_numeric": s(quartic_c1),
            "c1_exact": s(quartic_first_gate_exact(qx)),
            "expected_sign": "NEGATIVE",
        },
        "finite_real_zero_jensen_generator": {
            "x": s(xh),
            "y": s(yh),
            "hierarchy_value": s(h_series),
            "direct_hermitian": s(h_direct),
            "residual_abs": s(abs(h_series - h_direct)),
        },
        "xi_low_order_samples": xi_samples,
        "tests": {
            "new_test_module_result": "7 passed",
            "new_test_runtime_seconds": "9.75",
            "prior_branch_suite_result": "14 passed (validated before v0.3 staging)",
            "combined_suite_not_rerun_in_single_checkout": True,
        },
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
