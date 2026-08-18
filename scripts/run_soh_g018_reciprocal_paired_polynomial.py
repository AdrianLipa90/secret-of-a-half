#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp

from secret_of_a_half.quotient_zero_set import quotient_F
from secret_of_a_half.reciprocal_paired_polynomial import (
    conjugation_closure_residual,
    evaluate_polynomial,
    monic_polynomial_coefficients,
    palindromic_coefficient_residual,
    real_coefficient_residual,
    reciprocal_closure_residual,
    self_reciprocal_identity_residual,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports" / "SOH_G018_RECIPROCAL_PAIRED_POLYNOMIAL_RECEIPT_V1.json"


def _synthetic_closed_roots(include_minus_one: bool) -> list[mp.mpc]:
    lam = mp.mpc("2.0", "1.0")
    roots = [lam, 1 / lam, mp.conj(lam), 1 / mp.conj(lam)]
    if include_minus_one:
        roots.append(mp.mpc(-1))
    return roots


def main() -> None:
    mp.mp.dps = 80
    tol = mp.mpf("1e-60")

    rows = []
    for include_minus_one in (False, True):
        roots = _synthetic_closed_roots(include_minus_one)
        coeffs = monic_polynomial_coefficients(roots)
        reciprocal_residual = reciprocal_closure_residual(roots)
        conjugation_residual = conjugation_closure_residual(roots)
        palindromic_residual = palindromic_coefficient_residual(coeffs)
        real_residual = real_coefficient_residual(coeffs)
        identity_residual = max(
            self_reciprocal_identity_residual(coeffs, x)
            for x in (mp.mpc("0.7", "0.2"), mp.mpc("-1.3", "0.4"), mp.mpf(2))
        )
        if max(
            reciprocal_residual,
            conjugation_residual,
            palindromic_residual,
            real_residual,
            identity_residual,
        ) > tol:
            raise RuntimeError("reciprocal paired-polynomial regression failed")
        if abs(coeffs[-1] - 1) > tol:
            raise RuntimeError("unit constant coefficient regression failed")

        q_minus_one = abs(evaluate_polynomial(coeffs, -1))
        if include_minus_one and q_minus_one > tol:
            raise RuntimeError("minus-one exceptional factor regression failed")
        if not include_minus_one and q_minus_one <= mp.mpf("1e-10"):
            raise RuntimeError("unexpected minus-one factor in generic synthetic set")

        rows.append(
            {
                "include_minus_one": include_minus_one,
                "degree": len(coeffs) - 1,
                "coefficients": [mp.nstr(c, 25) for c in coeffs],
                "constant": mp.nstr(coeffs[-1], 12),
                "Q_minus_one_abs": mp.nstr(q_minus_one, 12),
                "reciprocal_closure_residual": mp.nstr(reciprocal_residual, 8),
                "conjugation_closure_residual": mp.nstr(conjugation_residual, 8),
                "palindromic_residual": mp.nstr(palindromic_residual, 8),
                "real_coefficient_residual": mp.nstr(real_residual, 8),
                "self_reciprocal_identity_residual": mp.nstr(identity_residual, 8),
            }
        )

    f_plus_quarter = quotient_F(mp.mpf("0.25"))
    f_minus_quarter = quotient_F(mp.mpf("-0.25"))
    if abs(f_plus_quarter) <= mp.mpf("0.1"):
        raise RuntimeError("F(1/4) positive-axis exclusion regression failed")

    payload = {
        "certificate": "SOH_G018_RECIPROCAL_PAIRED_POLYNOMIAL_RECEIPT_V1",
        "status": "THEOREM_STRUCTURE_AND_SYNTHETIC_REGRESSION_PASS",
        "normalized_coordinate": "lambda=4w",
        "normalized_involution": "lambda -> 1/lambda",
        "synthetic_closed_set_regressions": rows,
        "actual_F_fixed_point_diagnostics": {
            "F_plus_quarter": mp.nstr(f_plus_quarter, 30),
            "F_plus_quarter_nonzero": abs(f_plus_quarter) > mp.mpf("0.1"),
            "F_minus_quarter": mp.nstr(f_minus_quarter, 30),
            "F_minus_quarter_zero_status_resolved_analytically_here": False,
        },
        "theorem_claims": {
            "normalized_paired_polynomial_is_self_reciprocal": True,
            "constant_coefficient_is_one": True,
            "coefficients_are_palindromic": True,
            "coefficients_are_real": True,
            "Q_plus_one_nonzero": True,
            "Q_minus_one_zero_iff_F_minus_quarter_zero": True,
            "paired_set_nonempty_proved": False,
            "F_minus_quarter_zero_status_resolved": False,
            "synthetic_regression_is_the_proof": False,
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
