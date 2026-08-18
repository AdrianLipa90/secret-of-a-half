#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp

from secret_of_a_half.negative_inversion import (
    euler_half_turn_u,
    negative_inversion_u,
    riemann_reflection_u,
)
from secret_of_a_half.spinor_lift import (
    bloch_vector_from_u,
    dagger,
    determinant2,
    identity2,
    matrix_residual,
    pauli_fixed_pairs,
    pauli_spinor_lifts,
    pi_rotation_lifts,
    projective_action,
    projective_class_label,
    q8_elements,
    scale_matrix,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports" / "SOH_G013_PAULI_SPINOR_LIFT_RECEIPT_V1.json"


def main() -> None:
    mp.mp.dps = 70
    tol = mp.mpf("1e-55")
    ident = identity2()
    minus_ident = scale_matrix(-1, ident)
    lifts = pauli_spinor_lifts()
    r, e, n = lifts["R"], lifts["E"], lifts["N"]

    su2_residuals = {}
    order_residuals = {}
    for label, lift in lifts.items():
        su2_residuals[label] = max(
            abs(determinant2(lift) - 1),
            matrix_residual(dagger(lift) * lift, ident),
        )
        order_residuals[label] = max(
            matrix_residual(lift * lift, minus_ident),
            matrix_residual(lift * lift * lift * lift, ident),
        )
    if max(su2_residuals.values()) > tol or max(order_residuals.values()) > tol:
        raise RuntimeError("SU2 or order-four verification failed")

    quaternion_residuals = {
        "RE_minus_N": matrix_residual(r * e, n),
        "ER_plus_N": matrix_residual(e * r, scale_matrix(-1, n)),
        "EN_minus_R": matrix_residual(e * n, r),
        "NE_plus_R": matrix_residual(n * e, scale_matrix(-1, r)),
        "NR_minus_E": matrix_residual(n * r, e),
        "RN_plus_E": matrix_residual(r * n, scale_matrix(-1, e)),
    }
    if max(quaternion_residuals.values()) > tol:
        raise RuntimeError("quaternion multiplication verification failed")

    elements = q8_elements()
    closure_residual = mp.mpf("0")
    values = list(elements.values())
    for a in values:
        for b in values:
            product = a * b
            best = min(matrix_residual(product, c) for c in values)
            closure_residual = max(closure_residual, best)
            projective_class_label(product, tol=tol)
    if closure_residual > tol:
        raise RuntimeError("Q8 closure verification failed")

    samples = [mp.mpc("0.7", "0.2"), mp.mpc("-0.3", "0.8"), mp.mpc("1.2", "-0.5")]
    projective_residual = mp.mpf("0")
    for u in samples:
        projective_residual = max(
            projective_residual,
            abs(projective_action(r, u) - riemann_reflection_u(u)),
            abs(projective_action(e, u) - euler_half_turn_u(u)),
            abs(projective_action(n, u) - negative_inversion_u(u)),
        )
    if projective_residual > tol:
        raise RuntimeError("projective G012 crosswalk failed")

    rotation_residual = mp.mpf("0")
    for label, rotation in pi_rotation_lifts().items():
        rotation_residual = max(
            rotation_residual,
            matrix_residual(rotation, scale_matrix(-1, lifts[label])),
        )
    if rotation_residual > tol:
        raise RuntimeError("pi-rotation central-sign verification failed")

    fixed_rows = []
    for label, pair in pauli_fixed_pairs().items():
        vectors = []
        for u in pair:
            image = projective_action(lifts[label], u)
            if u == mp.inf:
                fixed_residual = mp.mpf("0") if image == mp.inf else mp.inf
            else:
                fixed_residual = abs(image - u)
            if fixed_residual > tol:
                raise RuntimeError(f"projective fixed pair failed for {label}")
            vectors.append(tuple(mp.nstr(x, 16) for x in bloch_vector_from_u(u)))
        fixed_rows.append({"operator": label, "bloch_vectors": vectors})

    payload = {
        "certificate": "SOH_G013_PAULI_SPINOR_LIFT_RECEIPT_V1",
        "status": "THEOREM_NUMERIC_REGRESSION_PASS",
        "su2_residuals": {k: mp.nstr(v, 8) for k, v in su2_residuals.items()},
        "order_four_residuals": {k: mp.nstr(v, 8) for k, v in order_residuals.items()},
        "quaternion_residuals": {k: mp.nstr(v, 8) for k, v in quaternion_residuals.items()},
        "q8_closure_residual": mp.nstr(closure_residual, 8),
        "projective_g012_crosswalk_residual": mp.nstr(projective_residual, 8),
        "pi_rotation_central_sign_residual": mp.nstr(rotation_residual, 8),
        "fixed_axes": fixed_rows,
        "claims": {
            "pauli_su2_lift_proved": True,
            "q8_group_proved": True,
            "q8_mod_center_equals_v4_proved": True,
            "spinorial_order_doubling_proved": True,
            "bloch_axis_fixed_pairs_proved": True,
            "new_xi_symmetry_proved": False,
            "rh_proved": False,
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
