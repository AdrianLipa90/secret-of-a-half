#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp

from secret_of_a_half.negative_inversion_zero_set import completed_xi, negative_inversion_s
from secret_of_a_half.paired_spectrum_quotient import (
    diagram_residual,
    quotient_fiber,
    quotient_map_s_to_w,
    reflection_s,
)
from secret_of_a_half.quotient_zero_set import quotient_F, quotient_negative_inversion_w, w_from_xi_zero

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports" / "SOH_G016_PAIRED_SPECTRUM_QUOTIENT_RECEIPT_V1.json"


def main() -> None:
    mp.mp.dps = 60
    tol = mp.mpf("1e-45")

    samples = [mp.mpc("0.3", "1.1"), mp.mpc("1.2", "-0.7"), mp.mpc("-2.4", "0.9")]
    max_diagram_residual = max(diagram_residual(s) for s in samples)
    max_reflection_residual = max(
        abs(quotient_map_s_to_w(s) - quotient_map_s_to_w(reflection_s(s)))
        for s in samples
    )
    if max(max_diagram_residual, max_reflection_residual) > tol:
        raise RuntimeError("paired-spectrum quotient diagram regression failed")

    root_rows = []
    for n in range(1, 4):
        rho = mp.zetazero(n)
        w = w_from_xi_zero(rho)
        fiber = quotient_fiber(w)
        source_root_abs = max(abs(completed_xi(s)) for s in fiber)
        q_residual = abs(quotient_map_s_to_w(rho) - w)
        if source_root_abs > mp.mpf("1e-35") or q_residual > tol:
            raise RuntimeError(f"quotient root fiber regression failed at zero {n}")

        target_w = quotient_negative_inversion_w(w)
        target_fiber = quotient_fiber(target_w)
        image_fiber = tuple(negative_inversion_s(s) for s in fiber)
        target_match = max(
            min(abs(image - target) for target in target_fiber)
            for image in image_fiber
        )
        if target_match > tol:
            raise RuntimeError(f"negative-inversion fiber lift failed at zero {n}")

        root_rows.append(
            {
                "index": n,
                "w": mp.nstr(w, 30),
                "source_F_abs": mp.nstr(abs(quotient_F(w)), 8),
                "source_fiber_max_xi_abs": mp.nstr(source_root_abs, 8),
                "q_rho_minus_w_abs": mp.nstr(q_residual, 8),
                "image_fiber_target_match_abs": mp.nstr(target_match, 8),
            }
        )

    fixed_w = mp.mpf("-0.25")
    fixed_fiber = quotient_fiber(fixed_w)
    fixed_residual = max(abs(negative_inversion_s(s) - s) for s in fixed_fiber)
    if fixed_residual > tol:
        raise RuntimeError("minus-quarter fixed fiber regression failed")

    payload = {
        "certificate": "SOH_G016_PAIRED_SPECTRUM_QUOTIENT_RECEIPT_V1",
        "status": "THEOREM_STRUCTURE_AND_NUMERIC_REGRESSION_PASS",
        "exact_diagram": {
            "q": "q(s)=(s-1/2)^2",
            "identity": "q(N_s(s))=J(q(s))",
            "max_diagram_residual": mp.nstr(max_diagram_residual, 8),
            "max_reflection_quotient_residual": mp.nstr(max_reflection_residual, 8),
        },
        "root_fiber_diagnostics": root_rows,
        "minus_quarter_fixed_fiber": {
            "fiber": [mp.nstr(s, 30) for s in fixed_fiber],
            "max_Ns_fixed_residual": mp.nstr(fixed_residual, 8),
        },
        "theorem_claims": {
            "q_of_PN_equals_PJ_proved_analytically": True,
            "restricted_q_is_exactly_two_to_one": True,
            "cardinality_PN_equals_two_times_PJ": True,
            "PN_cardinality_even": True,
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
