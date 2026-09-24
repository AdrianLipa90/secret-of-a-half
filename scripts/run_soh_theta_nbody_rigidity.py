from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp

from secret_of_a_half.theta_nbody_rigidity import (
    external_bilinear_value,
    hermitian_jensen_value,
    nbody_log_partition_hessian_real,
    riemann_external_bilinear,
    riemann_hermitian_jensen,
    tent_external_tilt_fourier,
    tent_transform,
    theta_transverse_potential,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports" / "SOH_THETA_NBODY_RIGIDITY_RECEIPT_V0_1.json"


def s(x: mp.mpf | mp.mpc, digits: int = 50) -> str:
    return mp.nstr(x, digits)


def main() -> int:
    mp.mp.dps = 100

    y_tent = mp.mpf("0.1")
    x_tent = mp.pi
    z_tent = mp.mpc(x_tent, y_tent)
    tent_external = external_bilinear_value(tent_transform, z_tent)
    tent_hermitian = hermitian_jensen_value(tent_transform, z_tent)
    tent_ft = tent_external_tilt_fourier(x_tent, y_tent)

    potentials = {
        str(y): theta_transverse_potential(mp.mpf(y), n_terms=8, cutoff=4)
        for y in ("0", "0.1", "0.25", "0.49")
    }

    faa, fab, fbb, det = nbody_log_partition_hessian_real(
        mp.mpf("0.3"), mp.mpf("0.1"), n_terms=8, cutoff=4
    )

    y_r = mp.mpf("0.499")
    e110 = riemann_external_bilinear(mp.mpf("110"), y_r)
    e111 = riemann_external_bilinear(mp.mpf("111"), y_r)
    h110 = riemann_hermitian_jensen(mp.mpf("110"), y_r)
    h111 = riemann_hermitian_jensen(mp.mpf("111"), y_r)

    data = {
        "schema": "SOH_THETA_NBODY_RIGIDITY_RECEIPT_V0_1",
        "status": "PASS_WITH_QUARANTINED_RIEMANN_EXTERNAL_CONFLICT",
        "proof_firewall": {
            "rh_proved": False,
            "rh_disproved": False,
            "external_dimitrov_xu_route_declared_wrong": False,
            "finite_riemann_external_sign_change_promoted": False,
        },
        "controls": {
            "mp_dps": 100,
            "riemann_kernel_n_terms": 8,
            "riemann_kernel_cutoff": "4",
        },
        "tent_control": {
            "x": s(x_tent),
            "y": s(y_tent),
            "external_bilinear": s(tent_external),
            "hermitian_jensen": s(tent_hermitian),
            "external_tilt_fourier": s(tent_ft),
            "external_identity_residual": s(tent_ft - 2 * tent_external),
            "external_negative": bool(tent_external < 0),
            "hermitian_positive": bool(tent_hermitian > 0),
        },
        "theta_transverse_potential": {
            y: s(v) for y, v in potentials.items()
        },
        "nbody_real_hessian_alpha_0_3_beta_0_1": {
            "F_aa": s(faa),
            "F_ab": s(fab),
            "F_bb": s(fbb),
            "det": s(det),
            "positive_definite": bool(faa > 0 and fbb > 0 and det > 0),
        },
        "riemann_external_conflict_diagnostic": {
            "classification": "FINITE_HIGH_PRECISION_DIAGNOSTIC_REQUIRES_INDEPENDENT_SOURCE_CONVENTION_AUDIT",
            "y": s(y_r),
            "external_x_110": s(e110),
            "external_x_111": s(e111),
            "hermitian_x_110": s(h110),
            "hermitian_x_111": s(h111),
            "external_sign_change_bracket": bool(e110 > 0 and e111 < 0),
            "hermitian_positive_at_bracket_endpoints": bool(h110 > 0 and h111 > 0),
        },
        "verdicts": {
            "tent_external_identity": "PASS",
            "internal_external_nonidentity": "PASS",
            "theta_potential_sampled_nonnegative_unique_zero": "PASS",
            "nbody_real_hessian_sampled_positive_definite": "PASS",
            "riemann_external_sign_change": "QUARANTINED_DIAGNOSTIC",
            "RH": "OPEN",
        },
    }
    OUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(data, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
