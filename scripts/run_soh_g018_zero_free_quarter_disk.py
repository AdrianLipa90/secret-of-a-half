#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp

from secret_of_a_half.quarter_disk_exclusion import (
    direct_f0,
    direct_f_quarter,
    exact_radical_checks,
    f0_elementary_lower_bound,
    paired_modulus_contradiction,
    quarter_disk_lower_margin,
)
from secret_of_a_half.quotient_zero_set import quotient_F

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports" / "SOH_G018_ZERO_FREE_QUARTER_DISK_RECEIPT_V1.json"


def main() -> None:
    mp.mp.dps = 80

    radical_checks = exact_radical_checks()
    if not all(radical_checks.values()):
        raise RuntimeError("G018 exact radical reduction failed")

    lower = f0_elementary_lower_bound()
    margin = quarter_disk_lower_margin()
    if not lower > mp.mpf("0.25"):
        raise RuntimeError("G018 elementary F(0) bound does not exceed 1/4")
    if not margin > 0:
        raise RuntimeError("G018 zero-free disk margin is not positive")

    f0 = direct_f0()
    f_quarter = direct_f_quarter()
    if abs(mp.im(f0)) > mp.mpf("1e-60") or mp.re(f0) <= lower:
        raise RuntimeError("G018 F(0) regression violates analytic lower bound")
    if abs(f_quarter - mp.mpf("0.5")) > mp.mpf("1e-70"):
        raise RuntimeError("G018 F(1/4)=1/2 regression failed")

    samples = [
        mp.mpf("0"),
        mp.mpf("0.25"),
        mp.mpf("-0.25"),
        mp.mpc("0.1", "0.2"),
        mp.mpc("-0.17", "0.11"),
    ]
    rows = []
    for w in samples:
        value = quotient_F(w)
        if abs(w) > mp.mpf("0.25"):
            raise RuntimeError("G018 internal disk sample lies outside radius 1/4")
        if abs(value) <= margin:
            raise RuntimeError("G018 sampled disk value violates analytic margin")
        rows.append(
            {
                "w": mp.nstr(w, 24),
                "abs_F": mp.nstr(abs(value), 24),
            }
        )

    radii = [mp.mpf("0.01"), mp.mpf("0.249"), mp.mpf("0.25"), mp.mpf("0.251"), mp.mpf("1"), mp.mpf("10")]
    if not all(paired_modulus_contradiction(r) for r in radii):
        raise RuntimeError("G018 J-modulus contradiction regression failed")

    payload = {
        "certificate": "SOH_G018_ZERO_FREE_QUARTER_DISK_RECEIPT_V1",
        "status": "ANALYTIC_ZERO_FREE_DISK_AND_PAIRED_EXCLUSION_PASS",
        "analytic_certificate": {
            "F0_elementary_lower": mp.nstr(lower, 40),
            "target_threshold": "1/4",
            "closed_disk_radius": "1/4",
            "certified_abs_F_margin": mp.nstr(margin, 40),
            "F_one_quarter_exact": "1/2",
            "exact_radical_checks": radical_checks,
            "numerics_are_the_proof": False,
        },
        "numeric_regression": {
            "F0": mp.nstr(f0, 40),
            "F_one_quarter": mp.nstr(f_quarter, 40),
            "disk_samples": rows,
        },
        "theorem_claims": {
            "F0_gt_one_quarter": True,
            "closed_quarter_disk_zero_free": True,
            "all_F_roots_have_modulus_gt_one_quarter": True,
            "PJ_empty": True,
            "PN_empty_via_G016": True,
            "negative_inversion_maps_no_xi_zero_to_xi_zero": True,
            "real_rootedness_proved": False,
            "pf_infinity_proved": False,
            "rh_proved": False,
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
