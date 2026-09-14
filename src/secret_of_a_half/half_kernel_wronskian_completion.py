"""Exact completion decomposition of the G024 Wronskian/Laguerre functional.

For f=p*g and W[f]=f'^2-f*f'',

    W[f] = p^2 W[g] + (p'^2-p p'') g^2.

With p(z)=z^2+1/4 this becomes

    W[Xi] = p(z)^2 W[g] + 2(z^2-1/4) g(z)^2,

where g=Xi/p is the Green-carrier Fourier transform.  The identity is exact;
finite numerical witnesses below reject the stronger requirement that the two
summands be separately nonnegative throughout the Dimitrov-Xu strip.
"""
from __future__ import annotations

import json

import mpmath as mp

from .half_kernel_green_carrier import centered_xi, completion_polynomial, stripped_carrier_transform


def laguerre_wronskian(fun, z: complex | mp.mpc) -> mp.mpc:
    zz = mp.mpc(z)
    value = fun(zz)
    first = mp.diff(fun, zz)
    second = mp.diff(fun, zz, 2)
    return first * first - value * second


def stripped_term(z: complex | mp.mpc) -> mp.mpc:
    zz = mp.mpc(z)
    p = completion_polynomial(zz)
    return p * p * laguerre_wronskian(stripped_carrier_transform, zz)


def completion_defect_term(z: complex | mp.mpc) -> mp.mpc:
    zz = mp.mpc(z)
    g = stripped_carrier_transform(zz)
    return 2 * (zz * zz - mp.mpf("0.25")) * g * g


def decomposition_residual(z: complex | mp.mpc) -> mp.mpf:
    zz = mp.mpc(z)
    lhs = laguerre_wronskian(centered_xi, zz)
    rhs = stripped_term(zz) + completion_defect_term(zz)
    return abs(lhs - rhs)


def build_receipt() -> dict[str, object]:
    with mp.workdps(60):
        z0 = mp.mpc("0", "0.2")
        z1 = mp.mpc("1", "0.2")
        s0, c0 = stripped_term(z0), completion_defect_term(z0)
        s1, c1 = stripped_term(z1), completion_defect_term(z1)
        t0 = s0 + c0
        t1 = s1 + c1
        r0 = decomposition_residual(z0)
        r1 = decomposition_residual(z1)

    checks = {
        "decomposition_residual_z0_small": r0 < mp.mpf("1e-45"),
        "decomposition_residual_z1_small": r1 < mp.mpf("1e-45"),
        "z0_stripped_real_part_positive": mp.re(s0) > 0,
        "z0_completion_real_part_negative": mp.re(c0) < 0,
        "z0_total_real_part_positive": mp.re(t0) > 0,
        "z1_stripped_real_part_negative": mp.re(s1) < 0,
        "z1_completion_real_part_positive": mp.re(c1) > 0,
        "z1_total_real_part_positive": mp.re(t1) > 0,
        "blockwise_same_sign_route_rejected": mp.re(s0) * mp.re(s1) < 0 and mp.re(c0) * mp.re(c1) < 0,
        "rh_claim_remains_false": True,
    }

    def snap(z, a, b):
        return {
            "z": str(z),
            "Re_stripped": mp.nstr(mp.re(a), 30),
            "Re_completion_defect": mp.nstr(mp.re(b), 30),
            "Re_total": mp.nstr(mp.re(a + b), 30),
        }

    return {
        "schema": "SOH_HALF_KERNEL_WRONSKIAN_COMPLETION_V0_3",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "epistemic_status": "EXACT_WRONSKIAN_COMPLETION_IDENTITY__BLOCKWISE_POSITIVITY_FAIL_NUMERICAL__G024_THIRD_ORDER_OPEN__RH_OPEN",
        "rh_claim": False,
        "identity": "W_Xi=p^2 W_g + 2(z^2-1/4)g^2, p=z^2+1/4, g=Xi/p",
        "g024_link": "The external Dimitrov-Xu/Laguerre target uses Re(W_Xi)>0; v0.3 preserves the full coupled sum.",
        "witnesses": [snap(z0, s0, c0), snap(z1, s1, c1)],
        "no_go": "Neither stripped nor completion summand has a global nonnegative real part in the open half-strip; independent block positivity is inadmissible.",
        "open": {
            "coupled_global_Wronskian_sign": True,
            "third_order_G024_complete_monotonicity": True,
            "riemann_hypothesis": True,
        },
        "checks": checks,
    }


def main() -> int:
    receipt = build_receipt()
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0 if receipt["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
