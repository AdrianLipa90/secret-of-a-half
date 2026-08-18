#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp

from secret_of_a_half.negative_inversion import (
    centered_t_from_u,
    euler_half_turn_t,
    euler_half_turn_u,
    log_negative_inversion,
    negative_inversion_fixed_s,
    negative_inversion_fixed_u,
    negative_inversion_t,
    negative_inversion_u,
    negative_inversion_w,
    negative_inversion_z,
    quotient_fixed_w,
    riemann_reflection_t,
    riemann_reflection_u,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports" / "SOH_G012_NEGATIVE_INVERSION_RECEIPT_V1.json"


def main() -> None:
    mp.mp.dps = 70
    tol = mp.mpf("1e-55")

    samples = [
        mp.mpc("0.7", "0.4"),
        mp.mpc("-0.3", "1.2"),
        mp.mpc("2.1", "-0.8"),
    ]
    max_v4_residual = mp.mpf("0")
    max_t_residual = mp.mpf("0")

    for u in samples:
        r = riemann_reflection_u
        e = euler_half_turn_u
        n = negative_inversion_u
        residuals = [
            abs(r(r(u)) - u),
            abs(e(e(u)) - u),
            abs(n(n(u)) - u),
            abs(r(e(u)) - n(u)),
            abs(e(r(u)) - n(u)),
        ]
        max_v4_residual = max(max_v4_residual, *residuals)

        t = centered_t_from_u(u)
        t_residuals = [
            abs(centered_t_from_u(r(u)) - riemann_reflection_t(t)),
            abs(centered_t_from_u(e(u)) - euler_half_turn_t(t)),
            abs(centered_t_from_u(n(u)) - negative_inversion_t(t)),
        ]
        max_t_residual = max(max_t_residual, *t_residuals)

    if max_v4_residual > tol or max_t_residual > tol:
        raise RuntimeError("operator algebra or centered conjugacy residual exceeded tolerance")

    fixed_rows = []
    for u, s in zip(negative_inversion_fixed_u(), negative_inversion_fixed_s()):
        n_residual = abs(negative_inversion_u(u) - u)
        critical_residual = abs(mp.re(s) - mp.mpf("0.5"))
        euler_square_residual = abs(u * u - mp.e ** (mp.j * mp.pi))
        if max(n_residual, critical_residual, euler_square_residual) > tol:
            raise RuntimeError("negative-inversion fixed-point verification failed")
        fixed_rows.append(
            {
                "u": mp.nstr(u, 30),
                "s": mp.nstr(s, 30),
                "negative_inversion_residual": mp.nstr(n_residual, 8),
                "critical_line_residual": mp.nstr(critical_residual, 8),
                "u_squared_minus_euler_phase_abs": mp.nstr(euler_square_residual, 8),
            }
        )

    w_plus, w_minus = quotient_fixed_w()
    quotient_residuals = {
        "w_plus": abs(negative_inversion_w(w_plus) - w_plus),
        "w_minus": abs(negative_inversion_w(w_minus) - w_minus),
        "genuine_z_fixed_plus_i_over_2": abs(negative_inversion_z(mp.j / 2) - mp.j / 2),
        "quotient_two_cycle_plus_half": abs(negative_inversion_z(mp.mpf("0.5")) + mp.mpf("0.5")),
    }
    if max(quotient_residuals.values()) > tol:
        raise RuntimeError("quotient fixed-point stratification verification failed")

    lam = mp.mpc("0.31", "0.27")
    log_residual = abs(mp.exp(log_negative_inversion(lam)) - negative_inversion_u(mp.exp(lam)))
    if log_residual > tol:
        raise RuntimeError("logarithmic negative-inversion lift verification failed")

    payload = {
        "certificate": "SOH_G012_NEGATIVE_INVERSION_RECEIPT_V1",
        "status": "THEOREM_NUMERIC_REGRESSION_PASS",
        "operator_algebra": {
            "group": "KLEIN_FOUR_V4",
            "max_v4_residual": mp.nstr(max_v4_residual, 8),
            "max_centered_conjugacy_residual": mp.nstr(max_t_residual, 8),
            "log_lift_residual": mp.nstr(log_residual, 8),
        },
        "fixed_pair": fixed_rows,
        "w_quotient": {key: mp.nstr(value, 8) for key, value in quotient_residuals.items()},
        "claims": {
            "negative_inversion_as_riemann_times_euler_proved": True,
            "klein_four_operator_algebra_proved": True,
            "fixed_pair_on_critical_line_proved": True,
            "all_xi_zeros_fixed_by_negative_inversion_proved": False,
            "soh_g003_proved": False,
            "rh_proved": False,
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
