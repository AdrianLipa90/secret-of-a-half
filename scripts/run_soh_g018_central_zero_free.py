#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp

from secret_of_a_half.central_zero_free import (
    central_radius,
    central_radius_squared,
    normalized_lower_bound,
    xi_on_critical_line,
)
from secret_of_a_half.quotient_zero_set import quotient_F

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports" / "SOH_G018_CENTRAL_ZERO_FREE_RECEIPT_V1.json"


def main() -> None:
    if central_radius_squared() != 20:
        raise RuntimeError("unexpected G018 safe squared radius")

    mp.mp.dps = 60
    r = central_radius()
    samples = [mp.mpf("0"), mp.mpf("1"), mp.mpf("2"), mp.mpf("4"), r]
    rows = []
    for t in samples:
        value = xi_on_critical_line(t)
        lower = normalized_lower_bound(t)
        if not mp.re(value) > 0:
            raise RuntimeError(f"critical-line positivity regression failed at t={t}")
        rows.append(
            {
                "t": mp.nstr(t, 30),
                "xi": mp.nstr(value, 30),
                "normalized_weak_lower_bound": mp.nstr(lower, 30),
            }
        )

    real_w_samples = [-20, -10, -1, 0, 1, 10]
    w_rows = []
    for w in real_w_samples:
        value = quotient_F(w)
        if not mp.re(value) > 0:
            raise RuntimeError(f"real-axis F positivity regression failed at w={w}")
        w_rows.append({"w": w, "F": mp.nstr(value, 30)})

    payload = {
        "certificate": "SOH_G018_CENTRAL_ZERO_FREE_RECEIPT_V1",
        "status": "ANALYTIC_CENTRAL_ZERO_FREE_INTERVAL_PASS",
        "analytic_chain": [
            "G017: m2 < m0/10",
            "cos(t y) >= 1 - t^2 y^2/2",
            "Xi(t) >= m0 - t^2 m2/2",
            "Xi(t)>0 for |t|<=sqrt(20), including endpoints by strict moment inequality",
            "F(-t^2)=Xi(t) => F(w)>0 on [-20,0]",
            "prior positive coefficients => F(w)>0 on [0,infinity)",
            "therefore F(w)>0 for every real w>=-20",
        ],
        "exact_bounds": {
            "critical_line_radius_squared": 20,
            "critical_line_radius": "sqrt(20)",
            "real_F_zero_free_interval": "[-20,infinity)",
        },
        "numeric_regression_not_proof": {
            "critical_line_samples": rows,
            "real_w_samples": w_rows,
        },
        "consequences": {
            "critical_line_xi_zero_requires_abs_imag_gt_sqrt20": True,
            "real_F_zero_requires_w_lt_minus20": True,
        },
        "proof_firewall": {
            "all_xi_zeros_on_critical_line_proved": False,
            "F_real_rootedness_proved": False,
            "pf_infinity_proved": False,
            "soh_g003_proved": False,
            "rh_proved": False,
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
