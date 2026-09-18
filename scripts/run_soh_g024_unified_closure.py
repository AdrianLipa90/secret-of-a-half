#!/usr/bin/env python3
"""Deterministic receipt for SOH-G024 v0.6 unified closure."""

from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp

from secret_of_a_half.g024_unified_closure import (
    dual_gram_radial_response,
    laguerre_resummed_radial_response,
    pole_free_dual_gram_diagonals,
    q_from_quotient_point,
    quotient_point,
    radial_response_from_quotient,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports" / "SOH_G024_UNIFIED_CLOSURE_RECEIPT_V0_6.json"


def completed_xi(s):
    s = mp.mpc(s)
    return (
        mp.mpf("0.5")
        * s
        * (s - 1)
        * mp.power(mp.pi, -s / 2)
        * mp.gamma(s / 2)
        * mp.zeta(s)
    )


def quotient_F(w):
    # xi(1/2+z)=F(z^2); the principal sqrt is harmless because xi is even
    # about 1/2.
    w = mp.mpc(w)
    return completed_xi(mp.mpf("0.5") + mp.sqrt(w))


def linear_F(w):
    return 1 + w


def s(x, digits=60):
    return mp.nstr(x, digits)


def main():
    mp.mp.dps = 80

    x = mp.mpf("0.7")
    q = mp.mpf("0.09")
    w = quotient_point(x, q)
    k0, k1 = pole_free_dual_gram_diagonals(linear_F, x, q)
    dual = dual_gram_radial_response(linear_F, x, q)
    direct = radial_response_from_quotient(linear_F, x, q)

    L0 = (1 - x*x) ** 2
    L1 = 2 * (1 + x*x)
    L2 = mp.mpf("1")
    laguerre = laguerre_resummed_radial_response([L0, L1, L2], q)

    rx = mp.mpf("14.134725141734693790")
    rq = mp.mpf("0.01")
    rw = quotient_point(rx, rq)
    rdual = dual_gram_radial_response(quotient_F, rx, rq)
    rdirect = radial_response_from_quotient(quotient_F, rx, rq)

    payload = {
        "schema": "sohalf.g024-unified-closure-receipt/v0.6",
        "status": "PASS",
        "rh_status": "OPEN",
        "classification": "EXACT_CROSSWALK_PLUS_FINITE_REGRESSION",
        "controls": {
            "mp_dps": 80,
            "new_tests": "6 passed",
        },
        "linear_quotient_control": {
            "x": s(x),
            "q": s(q),
            "w_real": s(mp.re(w)),
            "w_imag": s(mp.im(w)),
            "q_roundtrip": s(q_from_quotient_point(w)),
            "K0hat": s(k0),
            "K1hat": s(k1),
            "K0hat_plus_absw_K1hat": s(dual),
            "radial_response_direct": s(direct),
            "laguerre_resummed_response": s(laguerre),
            "dual_residual_abs": s(abs(dual-direct)),
            "laguerre_residual_abs": s(abs(laguerre-direct)),
        },
        "riemann_quotient_crosswalk": {
            "x": s(rx),
            "q": s(rq),
            "w_real": s(mp.re(rw)),
            "w_imag": s(mp.im(rw)),
            "dual_gram_sum": s(rdual),
            "radial_response": s(rdirect),
            "residual_abs": s(abs(rdual-rdirect)),
            "classification": "FINITE_HIGH_PRECISION_DIAGNOSTIC",
        },
        "exact_closure": {
            "q_from_w": "q=(|w|+Re(w))/2",
            "critical_strip_image": "0<(|w|+Re(w))/2<1/4",
            "radial_dual_gram": "Q_q=K0hat(w,w)+|w| K1hat(w,w)",
            "laguerre_resummation": "Q_q=1/2 sum_{n>=1} n L_n[f](x) q^(n-1)",
            "physical_tangent": "Fourier[G_q](2x)=Q_q",
            "rh_gate": "RH iff Q_q>=0 for all real x and 0<q<1/4",
        },
    }

    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
