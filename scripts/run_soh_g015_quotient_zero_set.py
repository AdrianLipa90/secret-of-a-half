#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp

from secret_of_a_half.quotient_zero_set import (
    quotient_F,
    quotient_F_branch_residual,
    quotient_fixed_w,
    quotient_negative_inversion_w,
    w_from_xi_zero,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports" / "SOH_G015_QUOTIENT_ZERO_SET_NO_GO_RECEIPT_V1.json"


def main() -> None:
    mp.mp.dps = 60
    tol = mp.mpf("1e-45")

    samples = [
        mp.mpc("2.3", "0.4"),
        mp.mpc("-3.7", "1.1"),
        mp.mpc("0.8", "-2.2"),
    ]
    involution_residual = max(
        abs(quotient_negative_inversion_w(quotient_negative_inversion_w(w)) - w)
        for w in samples
    )
    branch_residual = max(quotient_F_branch_residual(w) for w in samples)
    if max(involution_residual, branch_residual) > tol:
        raise RuntimeError("quotient involution or F branch-independence regression failed")

    f0 = quotient_F(0)
    f_plus_quarter = quotient_F(mp.mpf("0.25"))
    if abs(mp.im(f0)) > tol or mp.re(f0) <= 0:
        raise RuntimeError("F(0) positivity regression failed")
    if abs(mp.im(f_plus_quarter)) > tol or mp.re(f_plus_quarter) <= 0:
        raise RuntimeError("F(1/4) positivity regression failed")

    fixed_rows = []
    for w in quotient_fixed_w():
        residual = abs(quotient_negative_inversion_w(w) - w)
        if residual > tol:
            raise RuntimeError("quotient fixed-point regression failed")
        fixed_rows.append(
            {
                "w": mp.nstr(w, 20),
                "fixed_residual": mp.nstr(residual, 8),
                "F_abs": mp.nstr(abs(quotient_F(w)), 20),
            }
        )

    zero_rows = []
    for n in range(1, 4):
        rho = mp.zetazero(n)
        w = w_from_xi_zero(rho)
        image = quotient_negative_inversion_w(w)
        source_F_abs = abs(quotient_F(w))
        image_F_abs = abs(quotient_F(image))
        if source_F_abs > mp.mpf("1e-35"):
            raise RuntimeError(f"source quotient root regression failed at zero {n}")
        if image_F_abs <= mp.mpf("0.1"):
            raise RuntimeError(f"mapped quotient root no-go diagnostic unexpectedly small at zero {n}")
        zero_rows.append(
            {
                "index": n,
                "rho": mp.nstr(rho, 30),
                "w": mp.nstr(w, 30),
                "J_w": mp.nstr(image, 30),
                "source_F_abs": mp.nstr(source_F_abs, 8),
                "mapped_F_abs": mp.nstr(image_F_abs, 20),
            }
        )

    contraction_rows = []
    previous = None
    for radius in [10, 100, 1000, 10000]:
        w = -mp.mpf(radius)
        image_abs = abs(quotient_negative_inversion_w(w))
        if previous is not None and not image_abs < previous:
            raise RuntimeError("quotient contraction diagnostic was not monotone")
        previous = image_abs
        contraction_rows.append({"abs_w": radius, "abs_J_w": mp.nstr(image_abs, 20)})

    payload = {
        "certificate": "SOH_G015_QUOTIENT_ZERO_SET_NO_GO_RECEIPT_V1",
        "status": "THEOREM_STRUCTURE_AND_NUMERIC_REGRESSION_PASS",
        "exact_algebra": {
            "map": "J(w)=1/(16w)",
            "involution_residual": mp.nstr(involution_residual, 8),
            "F_branch_residual": mp.nstr(branch_residual, 8),
            "fixed_values": ["1/4", "-1/4"],
        },
        "center_values": {
            "F_0": mp.nstr(f0, 30),
            "F_plus_quarter": mp.nstr(f_plus_quarter, 30),
            "F_0_positive": True,
            "F_plus_quarter_positive": True,
        },
        "fixed_point_diagnostics": fixed_rows,
        "first_root_diagnostics": zero_rows,
        "large_root_contraction": contraction_rows,
        "theorem_claims": {
            "paired_F_root_set_finite_proved_analytically": True,
            "global_F_root_invariance_ruled_out": True,
            "all_but_finitely_many_F_roots_map_to_nonroots": True,
            "exceptional_orbits_are_two_cycles_plus_possible_minus_quarter": True,
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
