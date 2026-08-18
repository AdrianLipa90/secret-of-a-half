#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp

from secret_of_a_half.negative_inversion_zero_set import (
    completed_xi,
    mapped_critical_height,
    negative_inversion_defect_from_half,
    negative_inversion_s,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports" / "SOH_G014_NEGATIVE_INVERSION_ZERO_SET_NO_GO_RECEIPT_V1.json"


def main() -> None:
    mp.mp.dps = 60
    tol = mp.mpf("1e-45")

    samples = [
        mp.mpc("0.2", "0.7"),
        mp.mpc("1.3", "-0.4"),
        mp.mpc("-2.1", "1.2"),
    ]
    involution_residual = max(abs(negative_inversion_s(negative_inversion_s(s)) - s) for s in samples)
    defect_residual = max(
        abs(
            (negative_inversion_s(s) - mp.mpf("0.5"))
            - negative_inversion_defect_from_half(s)
        )
        for s in samples
    )
    if max(involution_residual, defect_residual) > tol:
        raise RuntimeError("exact negative-inversion algebra regression failed")

    xi_half = completed_xi(mp.mpf("0.5"))
    if abs(mp.im(xi_half)) > tol or mp.re(xi_half) <= 0:
        raise RuntimeError("xi(1/2) positivity regression failed")

    zero_rows = []
    for n in range(1, 4):
        rho = mp.zetazero(n)
        image = negative_inversion_s(rho)
        expected = mapped_critical_height(mp.im(rho))
        map_residual = abs(image - expected)
        image_xi_abs = abs(completed_xi(image))
        source_zeta_abs = abs(mp.zeta(rho))
        if map_residual > tol:
            raise RuntimeError(f"critical-line height map failed at zero {n}")
        if source_zeta_abs > mp.mpf("1e-40"):
            raise RuntimeError(f"source zero regression failed at zero {n}")
        if image_xi_abs <= mp.mpf("0.1"):
            raise RuntimeError(f"mapped-zero no-go diagnostic unexpectedly small at zero {n}")
        zero_rows.append(
            {
                "index": n,
                "rho": mp.nstr(rho, 30),
                "mapped_rho": mp.nstr(image, 30),
                "mapped_height": mp.nstr(mp.im(image), 20),
                "source_zeta_abs": mp.nstr(source_zeta_abs, 8),
                "mapped_xi_abs": mp.nstr(image_xi_abs, 20),
                "height_map_residual": mp.nstr(map_residual, 8),
            }
        )

    contraction_rows = []
    previous = None
    for radius in [10, 100, 1000, 10000]:
        s = mp.mpc(radius, mp.mpf(radius) / 3)
        defect = abs(negative_inversion_s(s) - mp.mpf("0.5"))
        if previous is not None and not defect < previous:
            raise RuntimeError("half-contraction diagnostic was not monotone")
        previous = defect
        contraction_rows.append({"radius": radius, "defect_from_half": mp.nstr(defect, 20)})

    payload = {
        "certificate": "SOH_G014_NEGATIVE_INVERSION_ZERO_SET_NO_GO_RECEIPT_V1",
        "status": "THEOREM_STRUCTURE_AND_NUMERIC_REGRESSION_PASS",
        "exact_algebra": {
            "map": "N_s(s)=(s-1)/(2s-1)",
            "half_defect": "N_s(s)-1/2=-1/(4s-2)",
            "critical_line_height_map": "t -> 1/(4t)",
            "involution_residual": mp.nstr(involution_residual, 8),
            "defect_identity_residual": mp.nstr(defect_residual, 8),
        },
        "xi_half": {
            "value": mp.nstr(xi_half, 30),
            "strictly_positive": True,
        },
        "first_zero_diagnostics": zero_rows,
        "unbounded_input_contraction": contraction_rows,
        "theorem_claims": {
            "paired_zero_set_finite_proved_analytically": True,
            "global_zero_set_invariance_ruled_out": True,
            "all_but_finitely_many_zeros_map_to_nonzeros": True,
            "numerics_are_the_proof": False,
            "rh_proved": False,
            "soh_g003_proved": False,
            "pf_infinity_proved": False,
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
