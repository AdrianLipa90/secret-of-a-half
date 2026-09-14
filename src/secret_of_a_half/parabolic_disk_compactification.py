"""SOH v0.4: parabolic quotient of the critical strip to the unit disk."""
from __future__ import annotations

import json
import mpmath as mp

from .caratheodory_disk import majorant_threshold_numeric
from .quotient_zero_set import quotient_F


def q_of_w(w: complex | mp.mpc) -> mp.mpc:
    z = mp.mpc(w)
    return -(mp.tan(mp.pi * mp.sqrt(z) / 2) ** 2)


def w_of_q(q: complex | mp.mpc) -> mp.mpc:
    z = mp.mpc(q)
    if abs(z) >= 1:
        raise ValueError("w_of_q requires |q|<1")
    return (2 * mp.atan(mp.sqrt(-z)) / mp.pi) ** 2


def parabolic_level(w: complex | mp.mpc) -> mp.mpf:
    z = mp.mpc(w)
    return abs(z) + mp.re(z)


def critical_line_q(gamma: float | mp.mpf) -> mp.mpf:
    g = abs(mp.mpf(gamma))
    return mp.tanh(mp.pi * g / 2) ** 2


def exponential_cayley_q(zeta: complex | mp.mpc) -> mp.mpc:
    z = mp.mpc(zeta)
    u = mp.exp(1j * mp.pi * z)
    return ((1 - u) / (1 + u)) ** 2


def positive_axis_A(q: float | mp.mpf) -> mp.mpf:
    x = mp.mpf(q)
    if x < 0 or x >= 1:
        raise ValueError("q must lie in [0,1)")
    return (2 * mp.atanh(mp.sqrt(x)) / mp.pi) ** 2


def q18_radius() -> mp.mpf:
    return mp.tanh(mp.pi / 4) ** 2


def transformed_quotient(q: complex | mp.mpc) -> mp.mpc:
    return quotient_F(w_of_q(q))


def build_receipt() -> dict[str, object]:
    with mp.workdps(65):
        zetas = [mp.mpc("0.1", "0.3"), mp.mpc("-0.2", "1.1"), mp.mpc("0.49", "0.7")]
        parabola_err = max(abs(parabolic_level(z*z) - 2*mp.re(z)**2) for z in zetas)
        roundtrip_err = max(abs(w_of_q(q_of_w(z*z)) - z*z) for z in zetas)
        cayley_err = max(abs(q_of_w(z*z) - exponential_cayley_q(z)) for z in zetas)
        boundary_err = max(abs(abs(q_of_w((a+1j*b)**2))-1)
                           for a in (mp.mpf("0.5"), mp.mpf("-0.5"))
                           for b in (mp.mpf("0"), mp.mpf("0.5"), mp.mpf("2")))
        critical_err = max(abs(q_of_w(-(g*g)) - critical_line_q(g))
                           for g in (mp.mpf("0"), mp.mpf("1"), mp.mpf("3")))

        q18 = q18_radius()
        q18_err = abs(positive_axis_A(q18) - mp.mpf("0.25"))
        r_star = majorant_threshold_numeric(dps=65, iterations=220)
        q19 = mp.tanh(mp.pi * mp.sqrt(r_star) / 2) ** 2
        g019_err = abs(mp.re(quotient_F(r_star)) - 2*mp.re(quotient_F(0)))
        probes = [mp.mpc("0"), q19/2, -q19/2, 1j*q19/2]
        min_re = min(mp.re(transformed_quotient(q)) for q in probes)
        gamma1 = mp.im(mp.zetazero(1))
        q1 = critical_line_q(gamma1)

    checks = {
        "parabolic_identity": parabola_err < mp.mpf("1e-55"),
        "roundtrip": roundtrip_err < mp.mpf("1e-50"),
        "exponential_cayley_identity": cayley_err < mp.mpf("1e-50"),
        "outer_boundary_to_unit_circle": boundary_err < mp.mpf("1e-50"),
        "critical_line_to_positive_radius": critical_err < mp.mpf("1e-50"),
        "g018_transfer_radius": q18_err < mp.mpf("1e-50"),
        "g019_radius_regression": g019_err < mp.mpf("1e-50"),
        "g019_sample_real_part_positive": min_re > 0,
        "first_zero_beyond_g019_disk": q1 > q19,
        "rh_claim_remains_false": True,
    }
    return {
        "schema": "SOH_HALF_KERNEL_PARABOLIC_DISK_COMPACTIFICATION_V0_4",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "rh_claim": False,
        "epistemic_status": "EXACT_PARABOLIC_QUOTIENT_BIHOLOMORPHISM__G018_G019_TRANSFER__RH_EQUIVALENT_DISK_REAL_ZERO_FORM__RH_OPEN",
        "q18": mp.nstr(q18, 35),
        "R_star": mp.nstr(r_star, 35),
        "q19": mp.nstr(q19, 35),
        "first_zero_q": mp.nstr(q1, 35),
        "open": {"disk_real_zero_or_inner_factor_closure": True, "G024_order_three_and_higher": True, "riemann_hypothesis": True},
        "checks": checks,
    }


def main() -> int:
    receipt = build_receipt()
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0 if receipt["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
