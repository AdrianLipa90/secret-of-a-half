#!/usr/bin/env python3
"""Deterministic numerical receipt for SOH-G008 scale-defect identities.

The theorem itself is algebraic/analytic.  This script verifies the implemented
xi representation against the predicted antisymmetry at high precision and
fails closed on any regression.
"""
from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp

from secret_of_a_half.uroboros import (
    UROBOROS_SCALE,
    centered_scale_bounds,
    xi_in_u,
    xi_scale_defect,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports" / "SOH_G008_XI_SCALE_DEFECT_RECEIPT_V1.json"


def main() -> None:
    mp.mp.dps = 60
    scale = mp.mpf(UROBOROS_SCALE)
    probes = [mp.mpf("0.05"), mp.mpf("0.2"), mp.mpf("1"), mp.mpf("3")]
    rows = []
    max_residual = mp.mpf("0")

    for u in probes:
        reflected = 1 / (scale * u)
        residual = xi_scale_defect(reflected) + xi_scale_defect(u)
        magnitude = abs(residual)
        max_residual = max(max_residual, magnitude)
        rows.append({
            "u": mp.nstr(u, 20),
            "defect_involution_u": mp.nstr(reflected, 20),
            "antisymmetry_residual": mp.nstr(magnitude, 20),
        })

    tolerance = mp.mpf("1e-45")
    if max_residual >= tolerance:
        raise RuntimeError(f"scale-defect antisymmetry residual {max_residual} exceeds tolerance")

    lower, upper = centered_scale_bounds(UROBOROS_SCALE)
    lower_mp = mp.mpf(lower)
    upper_mp = mp.mpf(upper)
    boundary_residual = abs(xi_in_u(lower_mp) - xi_in_u(upper_mp))
    if boundary_residual >= mp.mpf("1e-14"):
        raise RuntimeError("centered cell boundary xi equality failed")

    nonperiodicity_witness = abs(xi_in_u(mp.mpf("1")) - xi_in_u(scale))
    if nonperiodicity_witness <= mp.mpf("1e-8"):
        raise RuntimeError("sample unexpectedly failed to witness non-periodicity")

    payload = {
        "certificate": "SOH_G008_XI_SCALE_DEFECT_RECEIPT_V1",
        "status": "NUMERICAL_REGRESSION_FOR_PROVED_IDENTITY",
        "scale": UROBOROS_SCALE,
        "centered_cell": [mp.nstr(lower_mp, 20), mp.nstr(upper_mp, 20)],
        "max_antisymmetry_residual": mp.nstr(max_residual, 20),
        "boundary_equality_residual": mp.nstr(boundary_residual, 20),
        "nonperiodicity_sample_difference": mp.nstr(nonperiodicity_witness, 20),
        "rows": rows,
        "claims": {
            "scale_defect_antisymmetry_proved_analytically": True,
            "global_scale_periodicity": False,
            "constant_multiplier_quasiperiodicity": False,
            "zero_location_proved": False,
            "rh_proved": False,
        },
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
