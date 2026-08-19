#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp

from secret_of_a_half.half_mass_pf3_no_go import (
    adjacent_ratio_numeric,
    counterexample_weight_numeric,
    normalization_cubic,
    normalizing_ratio_numeric,
    pf2_minor_numeric,
    positive_mass_closed_form_numeric,
    solid_pf3_margin_exact,
    solid_pf3_minor_k2_numeric,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports" / "SOH_G021_HALF_MASS_PF2_NOT_PF3_RECEIPT_V1.json"


def main() -> None:
    mp.mp.dps = 80
    x = normalizing_ratio_numeric(80)
    weights = [counterexample_weight_numeric(n, dps=80) for n in range(12)]
    ratios = [adjacent_ratio_numeric(n, dps=80) for n in range(1, 12)]
    pf2_minors = [pf2_minor_numeric(n, dps=80) for n in range(1, 10)]
    positive_mass = positive_mass_closed_form_numeric(dps=80)
    margin = solid_pf3_margin_exact()
    determinant = solid_pf3_minor_k2_numeric(dps=80)

    if not (0 < x < 1):
        raise RuntimeError("G021 normalization root must lie in (0,1)")
    if abs(normalization_cubic(x)) >= mp.mpf("1e-60"):
        raise RuntimeError("G021 normalization cubic residual too large")
    if abs(positive_mass - mp.mpf("0.5")) >= mp.mpf("1e-60"):
        raise RuntimeError("G021 positive-index mass must equal one half")
    if weights[0] != mp.mpf("0.5"):
        raise RuntimeError("G021 pi_0 must equal one half")
    if not all(value > 0 for value in weights):
        raise RuntimeError("G021 sampled weights must be positive")
    if not all(weights[n] > weights[n + 1] for n in range(len(weights) - 1)):
        raise RuntimeError("G021 sampled weights must decrease strictly")
    if not all(ratios[n] >= ratios[n + 1] for n in range(len(ratios) - 1)):
        raise RuntimeError("G021 adjacent ratios must be nonincreasing")
    if not all(value >= -mp.mpf("1e-70") for value in pf2_minors):
        raise RuntimeError("G021 sampled PF2 minors must be nonnegative")
    for n in range(1, 12):
        if not 2 * weights[n] < mp.mpf(1) / n:
            raise RuntimeError(f"G021 monotone envelope failed at n={n}")
    if str(margin) != "-1271/2500":
        raise RuntimeError("G021 exact PF3 margin changed")
    if not determinant < 0:
        raise RuntimeError("G021 k=2 solid PF3 determinant must be negative")

    payload = {
        "certificate": "SOH_G021_HALF_MASS_PF2_NOT_PF3_RECEIPT_V1",
        "status": "EXACT_STRUCTURAL_NO_GO_PASS",
        "analytic_theorem": {
            "normalization_cubic": "36*x^3 + 205*x^2 + 1295*x - 1250 = 0",
            "unique_root_interval": "0 < x < 1",
            "pi_0_exact": "1/2",
            "sum_positive_indices_exact": "1/2",
            "positive_probability_sequence": True,
            "strictly_decreasing_masses": True,
            "pf2_log_concavity": True,
            "g020_monotone_envelope": "2*pi_n < 1/n, n>=1",
            "g006_margin_k2_exact": "-1271/2500",
            "pf3_implication_from_g020_package": False,
            "numerics_are_the_proof": False,
        },
        "regression": {
            "x": mp.nstr(x, 60),
            "cubic_residual": mp.nstr(normalization_cubic(x), 20),
            "positive_mass": mp.nstr(positive_mass, 60),
            "pi_0_to_pi_11": [mp.nstr(value, 35) for value in weights],
            "q_1_to_q_11": [mp.nstr(value, 35) for value in ratios],
            "pf2_minors_n1_to_n9": [mp.nstr(value, 25) for value in pf2_minors],
            "solid_pf3_minor_k2": mp.nstr(determinant, 40),
        },
        "proof_firewall": {
            "actual_F_pf3_proved": False,
            "actual_F_pf3_disproved": False,
            "actual_G006_negative_margin_proved": False,
            "pf_infinity_proved": False,
            "soh_g003_real_rootedness_proved": False,
            "rh_proved": False,
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
