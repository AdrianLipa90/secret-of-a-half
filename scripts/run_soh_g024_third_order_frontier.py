#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp

from secret_of_a_half.jensen_wiener_kernel import third_order_cm_normalized_margin_from_bridge

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports" / "SOH_G024_THIRD_ORDER_FRONTIER_RECEIPT_V1.json"


def main() -> None:
    mp.mp.dps = 80
    u = mp.mpf("0.37")
    y = mp.mpf("0.23")
    q = u * u

    bridge_margin = third_order_cm_normalized_margin_from_bridge(
        u,
        y,
        mean_a=2 * u,
        mean_b=2,
        var_a=0,
        mean_c=0,
        cov_ab=0,
        third_central_a=0,
    )

    constant = mp.sqrt(mp.pi) / 2
    h = lambda x: constant * mp.exp(-x) * mp.cosh(2 * y * mp.sqrt(x))
    direct_margin = 8 * u**5 * (-mp.diff(h, q, 3) / h(q))
    if abs(bridge_margin - direct_margin) > mp.mpf("1e-55"):
        raise RuntimeError("Gaussian third-order bridge normal-form regression failed")

    a = abs(y)
    x = 2 * a * u
    t = 2 * a * mp.tanh(x)
    tp = 4 * a**2 / mp.cosh(x) ** 2
    tpp = -16 * a**3 / mp.cosh(x) ** 2 * mp.tanh(x)
    n = 2 * u - t
    np = 2 - tp
    npp = -tpp
    m2 = n + u * (n**2 - np)
    m2p = n**2 + u * (2 * n * np - npp)
    recurrence_margin = (u * n + 3) * m2 - u * m2p
    if abs(bridge_margin - recurrence_margin) > mp.mpf("1e-65"):
        raise RuntimeError("G024 third-order recurrence equivalence regression failed")

    payload = {
        "certificate": "SOH_G024_THIRD_ORDER_FRONTIER_RECEIPT_V1",
        "status": "EXACT_THIRD_ORDER_REDUCTION_REGRESSION_PASS_SIGN_OPEN",
        "exact_checks": {
            "complete_monotonicity_recurrence": "F_(m+1)=S*F_m-F_m'",
            "third_order_log_slope_form": "F_3=S^3-3*S*S'+S''",
            "bridge_second_log_derivative": "R''=E[C3]-3*Cov(A,B)+mu_3(A)",
            "radial_third_order_normal_form": "8u^5*(-H'''/H)=u^2*N^3-3u^2*N*N'+u^2*N''+3u*N^2-3u*N'+3N",
            "second_margin_growth_form": "8u^5*(-H'''/H)=(u*N+3)*M2-u*M2'",
            "gaussian_bridge_closed_form_regression": True,
            "gaussian_growth_form_regression": True,
            "gaussian_margin": mp.nstr(bridge_margin, 40),
        },
        "proof_firewall": {
            "first_order_complete_monotonicity_proved": True,
            "second_order_complete_monotonicity_global_proved": True,
            "second_order_compact_dependency": "SOH-G024-Q computer-assisted interval certificate",
            "third_order_reduced_exactly": True,
            "third_order_complete_monotonicity_proved": False,
            "complete_monotonicity_all_orders_proved": False,
            "strict_fourier_positivity_proved": False,
            "wiener_density_proved_for_riemann_family": False,
            "soh_g003_real_rootedness_proved": False,
            "pf3_proved": False,
            "pf_infinity_proved": False,
            "rh_proved": False,
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
