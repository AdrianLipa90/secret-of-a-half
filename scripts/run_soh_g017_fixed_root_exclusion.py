#!/usr/bin/env python3
from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

import mpmath as mp

from secret_of_a_half.fixed_root_exclusion import (
    fixed_root_lower_ratio,
    fixed_root_numeric_values,
    g004_variance_upper,
    log_phi_curvature_upper,
    safe_strong_concavity_kappa,
    second_moment_ratio_upper,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports" / "SOH_G017_FIXED_ROOT_EXCLUSION_RECEIPT_V1.json"


def main() -> None:
    variance = g004_variance_upper()
    curvature = log_phi_curvature_upper()
    kappa = safe_strong_concavity_kappa()
    moment_ratio = second_moment_ratio_upper()
    lower_ratio = fixed_root_lower_ratio()

    if not variance < Fraction(2, 1):
        raise RuntimeError("G004 variance bound no longer below 2")
    if not curvature < Fraction(-10, 1):
        raise RuntimeError("G004 constants no longer certify (log Phi)'' < -10")
    if kappa != Fraction(10, 1):
        raise RuntimeError("unexpected strong-concavity kappa")
    if moment_ratio != Fraction(1, 10):
        raise RuntimeError("unexpected second-moment ratio bound")
    if lower_ratio != Fraction(79, 80):
        raise RuntimeError("unexpected fixed-root lower ratio")

    mp.mp.dps = 60
    values = fixed_root_numeric_values(60)
    numeric_ratio = mp.re(values["ratio"])
    if not numeric_ratio > mp.mpf(79) / 80:
        raise RuntimeError("numeric regression violates analytic lower ratio")
    if not mp.re(values["F_minus_quarter"]) > 0:
        raise RuntimeError("numeric regression does not show positive fixed-root value")

    payload = {
        "certificate": "SOH_G017_FIXED_ROOT_EXCLUSION_RECEIPT_V1",
        "status": "ANALYTIC_FIXED_ROOT_EXCLUSION_PASS",
        "attribution": {
            "gershon_2026": "prior strict log-concavity of the classical Xi kernel Phi",
            "soh_g004": "explicit channel curvature and mixture-variance constants used quantitatively here",
        },
        "rational_bounds": {
            "g004_variance_upper": str(variance),
            "log_phi_curvature_upper": str(curvature),
            "safe_kappa": str(kappa),
            "m2_over_m0_upper": str(moment_ratio),
            "F_minus_quarter_over_F0_lower": str(lower_ratio),
        },
        "analytic_chain": [
            "Jacobi modularity => Phi(-y)=Phi(y) => Phi'(0)=0",
            "G004: g_n''<-12 and Var_p(g_n')<2 => (log Phi)''<-10",
            "V=-log Phi => V'(y)>10y for y>0",
            "integration by parts => m2<m0/10",
            "cos(y/2)>=1-y^2/8 => F(-1/4)>(79/80)F(0)>0",
        ],
        "numeric_regression_not_proof": {
            "F0": mp.nstr(values["F0"], 30),
            "F_minus_quarter": mp.nstr(values["F_minus_quarter"], 30),
            "ratio": mp.nstr(values["ratio"], 30),
            "xi_half_plus_i_half": mp.nstr(values["xi_half_plus_i_half"], 30),
        },
        "consequences": {
            "F_minus_quarter_nonzero": True,
            "PJ_has_fixed_points": False,
            "PJ_cardinality_even": True,
            "PN_cardinality_divisible_by_four": True,
            "g012_fixed_pair_are_xi_zeros": False,
        },
        "proof_firewall": {
            "paired_sets_empty_proved": False,
            "nonfixed_two_cycles_excluded": False,
            "real_rootedness_proved": False,
            "pf_infinity_proved": False,
            "soh_g003_proved": False,
            "rh_proved": False,
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
