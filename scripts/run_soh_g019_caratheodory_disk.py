#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp

from secret_of_a_half.caratheodory_disk import (
    F0_numeric,
    centered_z_radius_numeric,
    coefficient_majorant_margin,
    majorant_threshold_numeric,
    positive_axis_F,
    sampled_min_real_part,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports" / "SOH_G019_CARATHEODORY_DISK_RECEIPT_V1.json"


def main() -> None:
    mp.mp.dps = 80

    f0 = F0_numeric()
    radius = majorant_threshold_numeric(dps=80, iterations=260)
    z_radius = centered_z_radius_numeric(dps=80)
    residual = abs(positive_axis_F(radius) - 2 * f0)

    if not (mp.mpf("30") < radius < mp.mpf("31")):
        raise RuntimeError("G019 R_* numerical regression left expected bracket")
    if residual > mp.mpf("1e-65"):
        raise RuntimeError("G019 F(R_*)=2F(0) numerical residual too large")
    if coefficient_majorant_margin(mp.mpf("30")) <= 0:
        raise RuntimeError("G019 radius 30 should be inside the proved threshold")
    if coefficient_majorant_margin(mp.mpf("31")) >= 0:
        raise RuntimeError("G019 radius 31 should be outside the majorant threshold")

    sample_radius = mp.mpf("30")
    sampled_min_re = sampled_min_real_part(sample_radius, samples=64)
    if sampled_min_re <= 0:
        raise RuntimeError("G019 sampled positive-real-part regression failed")

    payload = {
        "certificate": "SOH_G019_CARATHEODORY_DISK_RECEIPT_V1",
        "status": "ANALYTIC_COEFFICIENT_MAJORANT_CARATHEODORY_DISK_PASS",
        "analytic_theorem": {
            "input": "all Taylor coefficients a_n of F are strictly positive",
            "R_star_definition": "unique positive solution of F(R_star)=2F(0)",
            "closed_disk_positive_real_part": True,
            "closed_disk_zero_free": True,
            "scaled_coefficients_pn_positive_and_sum_to_one": True,
            "coefficient_envelope": "a_n < F(0) * R_star^(-n), n>=1",
            "R_star_claimed_as_maximal_actual_zero_free_radius": False,
            "numerics_are_the_proof": False,
        },
        "regression": {
            "F0": mp.nstr(f0, 60),
            "R_star": mp.nstr(radius, 60),
            "sqrt_R_star": mp.nstr(z_radius, 60),
            "F_R_star_minus_2F0_abs": mp.nstr(residual, 20),
            "R_star_over_quarter": mp.nstr(radius / mp.mpf("0.25"), 30),
            "sample_radius": mp.nstr(sample_radius, 10),
            "sampled_min_real_part_64": mp.nstr(sampled_min_re, 40),
        },
        "proof_firewall": {
            "real_rootedness_proved": False,
            "pf3_proved": False,
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
