#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp

from secret_of_a_half.euler_crossings import (
    complex_scale_defect,
    crossing_quotient_argument,
    euler_half_turn,
    forced_u_crossings,
    log_scale_defect,
    logarithmic_crossing,
    numerical_log_crossing_derivative,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports" / "SOH_G011_EULER_HALF_PERIOD_RECEIPT_V1.json"


def main() -> None:
    mp.mp.dps = 60
    rows = []
    for a in [2, 3, 32]:
        plus, minus = forced_u_crossings(a)
        plus_residual = abs(complex_scale_defect(plus, a))
        minus_residual = abs(complex_scale_defect(minus, a))
        if plus_residual > mp.mpf("1e-45") or minus_residual > mp.mpf("1e-45"):
            raise RuntimeError(f"forced crossing residual failed for a={a}")

        lam0 = logarithmic_crossing(a, 0)
        lam1 = logarithmic_crossing(a, 1)
        euler_residual = abs(mp.exp(lam1) - euler_half_turn(mp.exp(lam0)))
        if euler_residual > mp.mpf("1e-50"):
            raise RuntimeError(f"Euler half-turn residual failed for a={a}")

        d0 = abs(numerical_log_crossing_derivative(a, 0))
        d1 = abs(numerical_log_crossing_derivative(a, 1))
        if d0 <= mp.mpf("1e-30") or d1 <= mp.mpf("1e-30"):
            raise RuntimeError(f"simple-zero regression failed for a={a}")

        w_even = crossing_quotient_argument(a, 0)
        w_odd = crossing_quotient_argument(a, 1)
        if not (w_even > 0 and w_odd > 0):
            raise RuntimeError(f"positive quotient arguments failed for a={a}")

        if abs(log_scale_defect(lam0, a)) > mp.mpf("1e-45"):
            raise RuntimeError(f"log crossing residual failed for a={a}")

        rows.append(
            {
                "a": a,
                "u_plus": mp.nstr(plus, 30),
                "u_minus": mp.nstr(minus, 30),
                "euler_half_turn_residual": mp.nstr(euler_residual, 8),
                "derivative_even_abs": mp.nstr(d0, 16),
                "derivative_odd_abs": mp.nstr(d1, 16),
                "w_even": mp.nstr(w_even, 16),
                "w_odd": mp.nstr(w_odd, 16),
            }
        )

    payload = {
        "certificate": "SOH_G011_EULER_HALF_PERIOD_RECEIPT_V1",
        "status": "THEOREM_NUMERIC_REGRESSION_PASS",
        "rows": rows,
        "claims": {
            "forced_pair_proved_analytically": True,
            "euler_half_period_exchange_proved_analytically": True,
            "forced_pair_simple_proved_analytically": True,
            "no_additional_complex_zeros_proved": False,
            "soh_g003_proved": False,
            "rh_proved": False,
        },
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
