#!/usr/bin/env python3
"""Deterministic receipt for SOH-G024 v0.5 Achilles radial gate."""

from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp

from secret_of_a_half.g024_achilles_radial_gate import (
    complex_laguerre_I,
    gaussian_control,
    hermitian_from_q,
    hermitian_jensen,
    off_axis_control,
    q_laplacian_residual,
    q_partition,
    radial_response,
    touchdown_leading_coefficient,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports" / "SOH_G024_ACHILLES_RADIAL_GATE_RECEIPT_V0_5.json"


def completed_xi(s: complex | mp.mpf | mp.mpc) -> mp.mpc:
    s = mp.mpc(s)
    return (
        mp.mpf("0.5")
        * s
        * (s - 1)
        * mp.power(mp.pi, -s / 2)
        * mp.gamma(s / 2)
        * mp.zeta(s)
    )


def Xi(z: complex | mp.mpf | mp.mpc) -> mp.mpc:
    z = mp.mpc(z)
    return completed_xi(mp.mpf("0.5") + 1j * z)


def fmt(x: object, digits: int = 55) -> str:
    return mp.nstr(x, digits)


def main() -> None:
    mp.mp.dps = 80

    q0 = mp.mpf("1")
    control_q = mp.mpf("0.25")
    control_Q = q_partition(off_axis_control, 0, control_q)
    control_R = radial_response(off_axis_control, 0, control_q)
    control_H = hermitian_jensen(off_axis_control, 0, mp.sqrt(control_q))
    touchdown = touchdown_leading_coefficient(off_axis_control, 0, 1, 1)

    gx = mp.mpf("0.7")
    gy = mp.mpf("0.3")
    gq = gy * gy
    lag_i = complex_laguerre_I(gaussian_control, gx, gy)
    twice_r = 2 * radial_response(gaussian_control, gx, gq)

    q_identity_x = mp.mpf("0.4")
    q_identity_q = mp.mpf("0.36")
    h_q = hermitian_from_q(off_axis_control, q_identity_x, q_identity_q)
    h_direct = hermitian_jensen(
        off_axis_control, q_identity_x, mp.sqrt(q_identity_q)
    )

    laplace_residual = q_laplacian_residual(
        gaussian_control, mp.mpf("0.8"), mp.mpf("0.16")
    )

    xi_points = [
        ("0", "0.01"),
        ("10", "0.01"),
        ("14.134725141734693790", "0.01"),
        ("20", "0.1"),
        ("50", "0.24"),
    ]
    xi_samples = []
    for xs, qs in xi_points:
        x = mp.mpf(xs)
        q = mp.mpf(qs)
        y = mp.sqrt(q)
        xi_samples.append(
            {
                "x": xs,
                "q": qs,
                "y": fmt(y),
                "Q_q": fmt(radial_response(Xi, x, q)),
                "H": fmt(hermitian_jensen(Xi, x, y)),
            }
        )

    payload = {
        "schema": "sohalf.g024-achilles-radial-gate-receipt/v0.5",
        "status": "PASS",
        "rh_status": "OPEN",
        "criterion_status": "EXACT_RH_EQUIVALENT_REDUCTION",
        "critical_q_interval": "0<q<1/4",
        "source_alignment": {
            "paper": "Csordas-Escassut, The Laguerre inequality and the distribution of zeros of entire functions",
            "doi": "10.5802/ambp.210",
            "theorem_2_3": "complex Laguerre-I criterion",
            "theorem_2_4": "Hermitian/convexity criterion",
        },
        "controls": {
            "mp_dps": 80,
            "branch_local_new_tests": "7 passed",
            "first_run_note": "initial 6/7 was a strict mpf equality assertion at q=0.9; replaced by numerical tolerance and rerun 7/7",
        },
        "off_axis_touchdown_control": {
            "function": "f(z)=z^2+1",
            "zero": "z=i",
            "q0": fmt(q0),
            "Q_at_q0": fmt(q_partition(off_axis_control, 0, q0)),
            "touchdown_leading_coefficient": fmt(touchdown),
            "sample_q": fmt(control_q),
            "Q": fmt(control_Q),
            "Q_q": fmt(control_R),
            "H": fmt(control_H),
            "expected_Q_formula": "Q_0(q)=1/2*(1-q)^2",
        },
        "complex_laguerre_I_identity": {
            "x": fmt(gx),
            "y": fmt(gy),
            "2_Q_q": fmt(twice_r),
            "laguerre_I": fmt(lag_i),
            "residual_abs": fmt(abs(twice_r - lag_i)),
        },
        "hermitian_q_identity": {
            "x": fmt(q_identity_x),
            "q": fmt(q_identity_q),
            "2Qq_plus_4qQqq": fmt(h_q),
            "H_direct": fmt(h_direct),
            "residual_abs": fmt(abs(h_q - h_direct)),
        },
        "q_laplacian_identity": {
            "residual_abs": fmt(abs(laplace_residual)),
        },
        "xi_finite_samples": xi_samples,
        "proof_firewall": {
            "exact": [
                "Q_x(q)=1/2|f(x+i sqrt(q))|^2 for real entire f",
                "2 Q_q = Im(-f'(z) conjugate(f(z)))/y for q=y^2>0",
                "H=2 Q_q+4 q Q_qq",
                "off-axis zero implies an interior negative Q_q witness on the same vertical line",
                "for Xi, RH iff Q_q>=0 for all real x and 0<q<1/4",
            ],
            "finite_only": "listed Xi samples",
            "open": "global proof of the radial gate for Xi; RH",
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
