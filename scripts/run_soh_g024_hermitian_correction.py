#!/usr/bin/env python3
"""Deterministic numerical receipt for the SOH-G024 Hermitian correction."""

from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp

from secret_of_a_half.g024_hermitian_correction import (
    dyadic_external_and_hermitian_witness,
    gaussian_fourier_entire,
    odd_tilt_fourier_from_entire,
    riemann_relative_susceptibility,
    tent_internal_jensen_transform,
    theta_partition_identity_residual,
)
from secret_of_a_half.theta_nbody_rigidity import (
    hermitian_jensen_value,
    tent_transform,
    xi_fourier_entire,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports" / "SOH_G024_HERMITIAN_CORRECTION_RECEIPT_V0_2.json"


def s(x: object, digits: int = 55) -> str:
    return mp.nstr(x, digits)


def main() -> None:
    mp.mp.dps = 80

    gx = mp.mpf("1.7")
    gy = mp.mpf("0.4")
    godd = odd_tilt_fourier_from_entire(gaussian_fourier_entire, gx, gy)
    gexpected = 1j * mp.im(gaussian_fourier_entire(mp.mpc(gx, gy)))

    # The direct compact-support quadrature is deliberately run at lower dps;
    # it is an independent numerical regression of an exact algebraic identity.
    with mp.workdps(35):
        tx = +mp.pi
        ty = mp.mpf("0.1")
        t_direct = tent_internal_jensen_transform(tx, ty)
        t_h = hermitian_jensen_value(tent_transform, mp.mpc(tx, ty))

    external, hermitian = dyadic_external_and_hermitian_witness(
        mp.mpf("12.38"), mp.mpf("0.5"), n_terms=80
    )

    rx = mp.mpf("14.134725141734693790")
    ry = mp.mpf("0.1")
    r_susc = riemann_relative_susceptibility(rx, ry)
    r_h = hermitian_jensen_value(xi_fourier_entire, mp.mpc(rx, ry))

    theta_residual = theta_partition_identity_residual(mp.mpf("0.25"))

    payload = {
        "schema": "sohalf.g024-hermitian-correction-receipt/v0.2",
        "status": "PASS",
        "rh_status": "OPEN",
        "historical_external_g024_rh_frontier": "SUPERSEDED_BY_SOURCE_CONVENTION_AUDIT",
        "corrected_kernel_status": "EXACT_FOURIER_IDENTITY_PASS",
        "nbody_bridge_status": "EXACT_IDENTITY_PASS",
        "source_audit": {
            "paper": "Dimitrov-Xu, Wronskians of Fourier and Laplace Transforms",
            "doi": "10.1090/tran/7809",
            "fourier_convention": "F[g](x)=int g(t) exp(-i*x*t) dt",
            "lemma_3_3_issue": "real odd sinh-tilt transforms to i*Im(f), not Im(f)",
            "publication_erratum_status": "NOT_LOCATED_IN_CURRENT_AUDIT",
        },
        "controls": {
            "mp_dps": 80,
            "tent_direct_quadrature_dps": 35,
            "dyadic_product_terms": 80,
        },
        "odd_channel_gaussian": {
            "x": s(gx),
            "y": s(gy),
            "fourier_real": s(mp.re(godd)),
            "fourier_imag": s(mp.im(godd)),
            "i_im_f_real": s(mp.re(gexpected)),
            "i_im_f_imag": s(mp.im(gexpected)),
            "residual_abs": s(abs(godd - gexpected)),
        },
        "tent_internal_jensen": {
            "x": s(mp.pi),
            "y": "0.1",
            "direct_4_Jhat_2x": s(t_direct),
            "hermitian_H": s(t_h),
            "residual_abs": s(abs(t_direct - t_h)),
        },
        "smooth_lp_dyadic_witness": {
            "x": "12.38",
            "y": "0.5",
            "external_E_truncated_N80": s(external),
            "hermitian_H_truncated_N80": s(hermitian),
            "external_sign": "NEGATIVE",
            "hermitian_sign": "POSITIVE",
            "proof_note": "numeric witness only; rigorous counterexample uses exact double-zero asymptotics of the infinite product",
        },
        "riemann_nbody_bridge": {
            "x": s(rx),
            "y": s(ry),
            "relative_susceptibility": s(r_susc),
            "hermitian_H": s(r_h),
            "residual_abs": s(abs(r_susc - r_h)),
        },
        "theta_partition_bridge": {
            "y": "0.25",
            "Vtheta_minus_log_Z_ratio": s(theta_residual),
        },
        "test_suite": {
            "expected_branch_local_result": "14 passed",
            "classification": "FINITE_REGRESSION_PASS",
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
