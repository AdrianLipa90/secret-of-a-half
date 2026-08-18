#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp

from secret_of_a_half.fixed_point_exclusion import (
    certified_margin,
    coarse_positive_bound,
    coarse_tail_bound,
    elementary_bound_checks,
    kernel_negative_fixed_value,
    oscillatory_tail_upper_bound,
    positive_block_lower_bound,
    quotient_negative_fixed_value,
)
from secret_of_a_half.quotient_zero_set import quotient_F, quotient_fixed_w

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports" / "SOH_G017_FIXED_POINT_EXCLUSION_RECEIPT_V1.json"


def main() -> None:
    mp.mp.dps = 80

    checks = elementary_bound_checks()
    if not all(checks.values()):
        raise RuntimeError("G017 exact integer bound check failed")

    positive_bound = positive_block_lower_bound()
    tail_bound = oscillatory_tail_upper_bound()
    coarse_positive = coarse_positive_bound()
    coarse_tail = coarse_tail_bound()
    margin = certified_margin()

    if not positive_bound > coarse_positive:
        raise RuntimeError("G017 positive block does not exceed 2^-15")
    if not tail_bound < coarse_tail:
        raise RuntimeError("G017 tail does not lie below 2^-167")
    if not margin > 0:
        raise RuntimeError("G017 certified fixed-point margin is not positive")

    direct = quotient_negative_fixed_value()
    kernel = kernel_negative_fixed_value(n_terms=10, y_cutoff=4)
    kernel_residual = abs(direct - kernel)
    if abs(mp.im(direct)) > mp.mpf("1e-60"):
        raise RuntimeError("G017 F(-1/4) should be real by xi symmetry")
    if mp.re(direct) <= margin:
        raise RuntimeError("G017 numerical F(-1/4) violates analytic lower bound")
    if kernel_residual > mp.mpf("1e-35"):
        raise RuntimeError("G017 kernel regression mismatch")

    plus, minus = quotient_fixed_w()
    plus_value = quotient_F(plus)
    minus_value = quotient_F(minus)
    if mp.re(plus_value) <= 0 or mp.re(minus_value) <= 0:
        raise RuntimeError("G017 fixed-point exclusion regression failed")

    payload = {
        "certificate": "SOH_G017_FIXED_POINT_EXCLUSION_RECEIPT_V1",
        "status": "ANALYTIC_FIXED_POINT_EXCLUSION_PASS",
        "analytic_certificate": {
            "positive_block_closed_form": mp.nstr(positive_bound, 40),
            "coarse_positive_bound": "2^-15",
            "tail_closed_form_upper_bound": mp.nstr(tail_bound, 12),
            "coarse_tail_bound": "2^-167",
            "certified_margin": mp.nstr(margin, 40),
            "exact_integer_checks": checks,
            "numerics_are_the_proof": False,
        },
        "fixed_point_regression": {
            "F_plus_quarter": mp.nstr(plus_value, 40),
            "F_minus_quarter": mp.nstr(minus_value, 40),
            "kernel_F_minus_quarter": mp.nstr(kernel, 40),
            "kernel_residual_abs": mp.nstr(kernel_residual, 8),
        },
        "theorem_claims": {
            "F_minus_quarter_strictly_positive": True,
            "J_has_no_fixed_roots_in_PJ": True,
            "PJ_is_disjoint_union_of_two_cycles": True,
            "PJ_cardinality_even": True,
            "PN_cardinality_divisible_by_four_via_G016": True,
            "every_exceptional_J_two_cycle_lifts_to_four_point_V4_orbit": True,
            "PJ_empty_proved": False,
            "PN_empty_proved": False,
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
