#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp

from secret_of_a_half.half_mass_pf2 import (
    canonical_half_mass_weight,
    canonical_radius_numeric,
    pf2_minor_numeric,
    quotient_coefficient_numeric,
    sharpened_coefficient_envelope,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports" / "SOH_G020_CANONICAL_HALF_MASS_PF2_RECEIPT_V1.json"


def main() -> None:
    mp.mp.dps = 70

    radius = canonical_radius_numeric(70)
    weights = [canonical_half_mass_weight(n, dps=70) for n in range(7)]
    minors = [pf2_minor_numeric(n, dps=70) for n in range(1, 6)]

    if weights[0] != mp.mpf("0.5"):
        raise RuntimeError("G020 pi_0 must equal one half exactly")
    if not all(value > 0 for value in weights):
        raise RuntimeError("G020 sampled weights must be positive")
    if not all(weights[n] > weights[n + 1] for n in range(len(weights) - 1)):
        raise RuntimeError("G020 sampled weights must be strictly decreasing")
    if not all(value > 0 for value in minors):
        raise RuntimeError("G020 sampled PF2 minors must be positive")

    for n in range(1, 7):
        coefficient = quotient_coefficient_numeric(n, 70)
        envelope = sharpened_coefficient_envelope(n, dps=70)
        if not coefficient < envelope:
            raise RuntimeError(f"G020 sharpened envelope failed at n={n}")

    positive_partial = sum(weights[1:])
    if not (mp.mpf("0.49") < positive_partial < mp.mpf("0.5")):
        raise RuntimeError("G020 positive-mass partial-sum regression failed")

    payload = {
        "certificate": "SOH_G020_CANONICAL_HALF_MASS_PF2_RECEIPT_V1",
        "status": "ANALYTIC_HALF_MASS_PF2_LAW_PASS",
        "analytic_theorem": {
            "pi_0_exact": "1/2",
            "sum_positive_indices_exact": "1/2",
            "sum_all_indices_exact": "1",
            "pf2_preserved_by_positive_geometric_scaling": True,
            "strictly_decreasing_sequence": True,
            "sharpened_coefficient_envelope": "a_n < F(0)/(n R_star^n), n>=1",
            "numerics_are_the_proof": False,
        },
        "regression": {
            "R_star": mp.nstr(radius, 50),
            "pi_0_to_pi_6": [mp.nstr(value, 40) for value in weights],
            "sampled_pf2_minors_n1_to_n5": [mp.nstr(value, 30) for value in minors],
            "positive_partial_pi_1_to_pi_6": mp.nstr(positive_partial, 40),
        },
        "proof_firewall": {
            "pf3_proved": False,
            "pf_infinity_proved": False,
            "ultra_log_concavity_proved": False,
            "real_rootedness_proved": False,
            "soh_g003_real_rootedness_proved": False,
            "rh_proved": False,
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
