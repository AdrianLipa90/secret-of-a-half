#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp

from secret_of_a_half.negative_inversion_zero_set import completed_xi
from secret_of_a_half.paired_spectrum_quotient import quotient_map_s_to_w
from secret_of_a_half.v4_paired_orbits import (
    euler_halfturn_fixed_pair,
    negative_inversion_fixed_pair,
    orbit_cardinality,
    paired_set_cardinality,
    quotient_paired_set_cardinality,
    reflection_fixed_point,
    v4_algebra_residuals,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports" / "SOH_G017_V4_PAIRED_SPECTRUM_ORBITS_RECEIPT_V1.json"


def main() -> None:
    mp.mp.dps = 80
    tol = mp.mpf("1e-60")

    samples = [
        mp.mpc("0.37", "2.125"),
        mp.mpc("1.31", "-0.73"),
        mp.mpc("-1.4", "0.91"),
    ]
    residual_rows = []
    max_algebra_residual = mp.mpf(0)
    for s in samples:
        residuals = v4_algebra_residuals(s)
        row_max = max(residuals.values())
        max_algebra_residual = max(max_algebra_residual, row_max)
        residual_rows.append(
            {
                "s": mp.nstr(s, 30),
                "orbit_cardinality": orbit_cardinality(s),
                "residuals": {k: mp.nstr(v, 8) for k, v in residuals.items()},
            }
        )
    if max_algebra_residual > tol:
        raise RuntimeError("V4 algebra regression failed")
    if any(row["orbit_cardinality"] != 4 for row in residual_rows):
        raise RuntimeError("generic V4 orbit cardinality regression failed")

    r_fixed = reflection_fixed_point()
    e_fixed = euler_halfturn_fixed_pair()
    n_fixed = negative_inversion_fixed_pair()

    excluded_fixed_values = {
        "R_fixed_s": mp.nstr(r_fixed, 30),
        "xi_R_fixed_abs": mp.nstr(abs(completed_xi(r_fixed)), 20),
        "E_fixed_s": [mp.nstr(s, 30) for s in e_fixed],
        "xi_E_fixed_abs": [mp.nstr(abs(completed_xi(s)), 20) for s in e_fixed],
    }
    if completed_xi(0) != mp.mpf("0.5") or completed_xi(1) != mp.mpf("0.5"):
        raise RuntimeError("completed xi removable-point normalization regression failed")
    if abs(completed_xi(r_fixed)) <= mp.mpf("0.1"):
        raise RuntimeError("xi(1/2) positivity regression failed")

    n_orbit_sizes = [orbit_cardinality(s) for s in n_fixed]
    n_q_values = [quotient_map_s_to_w(s) for s in n_fixed]
    if n_orbit_sizes != [2, 2]:
        raise RuntimeError("N-fixed exceptional orbit-size regression failed")
    if max(abs(w + mp.mpf("0.25")) for w in n_q_values) > tol:
        raise RuntimeError("N-fixed pair does not map to w=-1/4")

    exceptional_xi_abs = [abs(completed_xi(s)) for s in n_fixed]

    cardinality_rows = []
    for a in range(5):
        for epsilon in (False, True):
            pn = paired_set_cardinality(a, epsilon)
            pj = quotient_paired_set_cardinality(a, epsilon)
            if pn != 2 * pj:
                raise RuntimeError("G016 cardinality cross-check failed")
            cardinality_rows.append(
                {
                    "generic_v4_orbits": a,
                    "epsilon": int(epsilon),
                    "PN": pn,
                    "PJ": pj,
                    "PN_mod_4": pn % 4,
                    "PJ_mod_2": pj % 2,
                }
            )

    payload = {
        "certificate": "SOH_G017_V4_PAIRED_SPECTRUM_ORBITS_RECEIPT_V1",
        "status": "THEOREM_STRUCTURE_AND_NUMERIC_REGRESSION_PASS",
        "v4_algebra": {
            "maps": {
                "R": "R(s)=1-s",
                "N": "N(s)=(s-1)/(2s-1)",
                "E": "E(s)=s/(2s-1)",
            },
            "relations": ["R^2=N^2=E^2=I", "RN=NR=E"],
            "max_residual": mp.nstr(max_algebra_residual, 8),
            "samples": residual_rows,
        },
        "excluded_fixed_loci": excluded_fixed_values,
        "possible_exceptional_orbit": {
            "points": [mp.nstr(s, 30) for s in n_fixed],
            "orbit_cardinalities": n_orbit_sizes,
            "quotient_values": [mp.nstr(w, 30) for w in n_q_values],
            "xi_abs_numeric_diagnostic": [mp.nstr(v, 20) for v in exceptional_xi_abs],
            "zero_status_resolved_analytically_here": False,
        },
        "cardinality_cross_checks": cardinality_rows,
        "theorem_claims": {
            "PN_is_V4_invariant": True,
            "generic_PN_orbits_have_size_four": True,
            "only_possible_size_two_orbit_is_half_plus_minus_i_over_two": True,
            "PN_cardinality_is_4a_plus_2epsilon": True,
            "PJ_cardinality_is_2a_plus_epsilon": True,
            "F_minus_quarter_zero_status_resolved": False,
            "numerics_are_the_proof": False,
            "soh_g003_proved": False,
            "pf_infinity_proved": False,
            "rh_proved": False,
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
