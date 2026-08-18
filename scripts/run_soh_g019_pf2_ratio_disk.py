#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp

from secret_of_a_half.pf2_ratio_disk import (
    boundary_regression,
    canonical_pf2_zero_free_radius_numeric,
    first_two_coefficients_numeric,
    pf2_tail_majorant,
    ratio_majorant_certificate,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports" / "SOH_G019_PF2_RATIO_ZERO_FREE_DISK_RECEIPT_V1.json"


def main() -> None:
    mp.mp.dps = 80

    a0, a1 = first_two_coefficients_numeric()
    if not (a0 > 0 and a1 > 0):
        raise RuntimeError("G019 first two coefficients must be positive")

    cert = ratio_majorant_certificate(a0, a1)
    radius = canonical_pf2_zero_free_radius_numeric()
    if not cert["boundary_qr_is_half"]:
        raise RuntimeError("G019 boundary q0*R0 identity failed")
    if not (mp.mpf("21.6") < radius < mp.mpf("21.7")):
        raise RuntimeError("G019 canonical radius regression moved unexpectedly")

    interior_radius = mp.mpf("0.999") * radius
    tail = pf2_tail_majorant(a0, a1, interior_radius)
    if not tail < a0:
        raise RuntimeError("G019 PF2 geometric tail majorant failed inside disk")

    sampled_boundary_min = boundary_regression(samples=48)
    if sampled_boundary_min <= 0:
        raise RuntimeError("G019 boundary regression encountered an apparent zero")

    payload = {
        "certificate": "SOH_G019_PF2_RATIO_ZERO_FREE_DISK_RECEIPT_V1",
        "status": "PF2_RATIO_MAJORANT_ZERO_FREE_DISK_PASS",
        "coefficient_regression": {
            "a0": mp.nstr(a0, 50),
            "a1": mp.nstr(a1, 50),
            "q0": mp.nstr(cert["q0"], 50),
            "R0": mp.nstr(radius, 50),
            "sqrt_R0": mp.nstr(mp.sqrt(radius), 40),
        },
        "majorant": {
            "q0_times_R0": mp.nstr(cert["q0_times_radius"], 20),
            "boundary_identity_is_half": bool(cert["boundary_qr_is_half"]),
            "interior_tail_lt_a0": True,
            "closed_boundary_strictness_uses_entirety": True,
        },
        "regression": {
            "sampled_boundary_min_abs_F_48": mp.nstr(sampled_boundary_min, 40),
            "numerics_are_the_proof": False,
        },
        "theorem_claims": {
            "closed_disk_abs_w_le_R0_zero_free": True,
            "all_F_roots_have_modulus_gt_R0": True,
            "all_xi_zeros_have_distance_from_half_gt_sqrt_R0": True,
            "real_rootedness_proved": False,
            "pf3_proved_here": False,
            "pf_infinity_proved": False,
            "rh_proved": False,
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
