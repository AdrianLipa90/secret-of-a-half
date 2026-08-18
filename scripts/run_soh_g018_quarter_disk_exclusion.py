#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp

from secret_of_a_half.quarter_disk_exclusion import (
    XI_HALF_LOWER,
    ZERO_FREE_MARGIN,
    boundary_regression,
    exact_certificate_checks,
    maps_root_modulus_into_zero_free_disk,
    positive_boundary_numeric,
    xi_half_numeric,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports" / "SOH_G018_QUARTER_DISK_ZERO_EXCLUSION_RECEIPT_V1.json"


def as_mpf_fraction(value):
    return mp.mpf(value.numerator) / value.denominator


def main() -> None:
    mp.mp.dps = 80

    checks = exact_certificate_checks()
    if not all(checks.values()):
        raise RuntimeError("G018 exact rational certificate failed")

    xi_half = xi_half_numeric()
    xi_lower = as_mpf_fraction(XI_HALF_LOWER)
    margin = as_mpf_fraction(ZERO_FREE_MARGIN)
    if abs(mp.im(xi_half)) > mp.mpf("1e-70"):
        raise RuntimeError("G018 xi(1/2) should be real")
    if mp.re(xi_half) <= xi_lower:
        raise RuntimeError("G018 xi(1/2) violates rational lower bound")

    boundary = positive_boundary_numeric()
    if abs(boundary - mp.mpf("0.5")) > mp.mpf("1e-60"):
        raise RuntimeError("G018 F(1/4)=xi(1)=1/2 regression failed")

    sampled_min = boundary_regression(samples=48)
    if sampled_min <= margin:
        raise RuntimeError("G018 sampled boundary fell below proved margin")

    for radius in [mp.mpf("0.250001"), mp.mpf("1"), mp.mpf("100")]:
        if not maps_root_modulus_into_zero_free_disk(radius):
            raise RuntimeError("G018 inversion modulus regression failed")

    payload = {
        "certificate": "SOH_G018_QUARTER_DISK_ZERO_EXCLUSION_RECEIPT_V1",
        "status": "ANALYTIC_QUARTER_DISK_AND_SPECTRAL_NO_GO_PASS",
        "analytic_certificate": {
            "xi_half_rational_lower": f"{XI_HALF_LOWER.numerator}/{XI_HALF_LOWER.denominator}",
            "xi_half_numeric_regression": mp.nstr(xi_half, 50),
            "xi_half_gt_one_quarter": True,
            "F_plus_quarter_exact_target": "1/2",
            "quarter_disk_uniform_margin_lower": f"{ZERO_FREE_MARGIN.numerator}/{ZERO_FREE_MARGIN.denominator}",
            "exact_checks": checks,
            "numerics_are_the_proof": False,
        },
        "regression": {
            "sampled_boundary_min_abs_F_48": mp.nstr(sampled_min, 40),
            "sampled_boundary_above_proved_margin": True,
        },
        "theorem_claims": {
            "closed_quarter_disk_zero_free": True,
            "all_F_roots_have_modulus_gt_quarter": True,
            "PJ_empty": True,
            "PN_empty_via_G016": True,
            "negative_inversion_maps_no_xi_zero_to_xi_zero": True,
            "real_rootedness_proved": False,
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
