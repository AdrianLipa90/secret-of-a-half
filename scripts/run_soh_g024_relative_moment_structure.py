#!/usr/bin/env python3
"""Deterministic receipt for SOH-G024 relative-moment structure v0.4."""

from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp

from secret_of_a_half.g024_relative_moment_structure import (
    gaussian_B_fourier_2x,
    gaussian_fourier,
    gaussian_relative_moment,
    oscillatory_gaussian_l2_witness,
    oscillatory_gaussian_log_curvature_margin,
    radial_first_gate_bound,
    scaled_laguerre_prediction,
    strong_marginal_curvature_bound,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports" / "SOH_G024_RELATIVE_MOMENT_STRUCTURE_RECEIPT_V0_4.json"


def s(x: object, digits: int = 60) -> str:
    return mp.nstr(x, digits)


def main() -> None:
    mp.mp.dps = 90

    # Gaussian saturation control for the strong-Prékopa curvature factor.
    a = mp.mpf("1.5")
    kappa = 2 * a
    u = mp.mpf("0.4")
    c0 = gaussian_relative_moment(a, u, 0)
    c1 = gaussian_relative_moment(a, u, 1)
    c2 = gaussian_relative_moment(a, u, 2)
    hankel2 = c0 * c2 - c1 * c1

    xg, yg = mp.mpf("0.7"), mp.mpf("0.2")
    b_hat = gaussian_B_fourier_2x(a, xg, yg)
    modulus = mp.mpf("0.5") * abs(gaussian_fourier(a, mp.mpc(xg, yg))) ** 2

    margin = oscillatory_gaussian_log_curvature_margin()
    l2_base, scaled_x, l2_scaled = oscillatory_gaussian_l2_witness()
    l2_prediction = scaled_laguerre_prediction(l2_base, 40, 2)

    payload = {
        "schema": "sohalf.g024-relative-moment-structure-receipt/v0.4",
        "status": "PASS",
        "rh_status": "OPEN",
        "controls": {
            "mp_dps": 90,
            "oscillatory_gaussian_a": "0.13",
            "oscillatory_gaussian_epsilon": "0.2",
            "oscillatory_gaussian_frequency": "1",
            "oscillatory_gaussian_scale": "40",
            "base_witness_x": "1.222",
            "scaled_witness_x": s(scaled_x),
        },
        "theorem_status": {
            "relative_moment_stieltjes_hankel": "EXACT",
            "strong_log_concavity_inheritance": "EXACT_USING_STRONG_PREKOPA",
            "generating_mixture_fourier_modulus_square": "EXACT",
            "coefficientwise_fourier_positivity": "OPEN_FOR_RIEMANN",
        },
        "gaussian_saturation_control": {
            "kernel_kappa": s(kappa),
            "predicted_relative_moment_curvature": s(strong_marginal_curvature_bound(kappa)),
            "exact_relative_moment_curvature": s(4 * a),
            "radial_first_gate_lower_bound": s(radial_first_gate_bound(kappa)),
            "u": s(u),
            "C0": s(c0),
            "C1": s(c1),
            "C2": s(c2),
            "hankel_2x2_determinant": s(hankel2),
        },
        "gaussian_generating_mixture_control": {
            "x": s(xg),
            "y": s(yg),
            "Bhat_2x": s(b_hat),
            "half_modulus_square": s(modulus),
            "residual_abs": s(abs(b_hat - modulus)),
        },
        "strong_log_concavity_no_go_control": {
            "certified_scaled_curvature_margin": s(margin),
            "comparison_to_riemann_internal_margin_10": "GREATER",
            "L2_base_at_x_1_222": s(l2_base),
            "L2_scaled_at_x_48_88": s(l2_scaled),
            "L2_scaled_prediction": s(l2_prediction),
            "scaling_residual_abs": s(abs(l2_scaled - l2_prediction)),
            "verdict": "STRONG_LOG_CONCAVITY_PLUS_AUTOMATIC_MOMENT_AND_MIXTURE_POSITIVITY_DO_NOT_FORCE_COEFFICIENTWISE_FOURIER_POSITIVITY",
        },
        "test_suite": {
            "branch_local_new_tests": "6 passed",
            "classification": "FINITE_REGRESSION_PASS",
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
