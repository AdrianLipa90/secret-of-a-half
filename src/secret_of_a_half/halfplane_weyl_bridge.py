"""SOH v0.5: sin(pi*s) half-plane quotient and conditional Weyl m-function."""
from __future__ import annotations

import json
import mpmath as mp

from .parabolic_disk_compactification import q_of_w


def t_of_s(s: complex | mp.mpc) -> mp.mpc:
    return mp.sin(mp.pi * mp.mpc(s))


def t_of_w(w: complex | mp.mpc) -> mp.mpc:
    return mp.cos(mp.pi * mp.sqrt(mp.mpc(w)))


def t_of_q(q: complex | mp.mpc) -> mp.mpc:
    z = mp.mpc(q)
    if z == 1:
        raise ValueError("Cayley pole at q=1")
    return (1 + z) / (1 - z)


def critical_t(gamma: float | mp.mpf) -> mp.mpf:
    return mp.cosh(mp.pi * abs(mp.mpf(gamma)))


def poincare_distance_critical(gamma: float | mp.mpf) -> mp.mpf:
    q = mp.tanh(mp.pi * abs(mp.mpf(gamma)) / 2) ** 2
    return 2 * mp.atanh(q)


def conditional_weyl_m(x: complex | mp.mpc, positive_t_zeros: list[mp.mpf]) -> mp.mpc:
    """Finite RH-conditional Stieltjes/Weyl diagnostic from positive t zeros."""
    z = mp.mpc(x)
    return mp.fsum(2 * a / (a * a - z) for a in positive_t_zeros)


def build_receipt() -> dict[str, object]:
    with mp.workdps(65):
        samples = [mp.mpc("0.2", "0.7"), mp.mpc("0.49", "1.1"), mp.mpc("0.5", "2")]
        quotient_err = max(abs(t_of_s(mp.mpf("0.5") + z) - t_of_w(z*z)) for z in samples)
        cayley_err = max(abs(t_of_q(q_of_w(z*z)) - t_of_w(z*z)) for z in samples)
        right_halfplane = all(mp.re(t_of_s(mp.mpc(beta, gamma))) > 0
                              for beta in (mp.mpf("0.1"), mp.mpf("0.5"), mp.mpf("0.9"))
                              for gamma in (mp.mpf("0.3"), mp.mpf("2")))
        critical_err = max(abs(t_of_s(mp.mpc("0.5", g)) - critical_t(g))
                           for g in (mp.mpf("0"), mp.mpf("1"), mp.mpf("3")))
        hyperbolic_err = max(abs(poincare_distance_critical(g) - mp.log(critical_t(g)))
                             for g in (mp.mpf("0.5"), mp.mpf("1"), mp.mpf("3")))

        gammas = [mp.im(mp.zetazero(k)) for k in range(1, 6)]
        tzeros = [critical_t(g) for g in gammas]
        xprobe = tzeros[0] ** 2 * mp.mpc("0.5", "0.2")
        mprobe = conditional_weyl_m(xprobe, tzeros)

        beta = mp.mpf("0.4")
        gamma = mp.mpf("2")
        off_t = t_of_s(mp.mpc(beta, gamma))
        off_pole = off_t * off_t
        zeta = mp.mpc(beta - mp.mpf("0.5"), gamma)
        q = q_of_w(zeta*zeta)
        deficit = 1 - abs(q)
        deficit_bound = 4 * mp.e ** (-mp.pi * abs(gamma))

    checks = {
        "sin_cos_quotient_identity": quotient_err < mp.mpf("1e-50"),
        "disk_cayley_parent_identity": cayley_err < mp.mpf("1e-50"),
        "critical_strip_maps_right_halfplane": right_halfplane,
        "critical_line_maps_positive_real": critical_err < mp.mpf("1e-50"),
        "hyperbolic_distance_identity": hyperbolic_err < mp.mpf("1e-50"),
        "finite_RH_conditional_weyl_imag_positive": mp.im(mprobe) > 0,
        "synthetic_offaxis_squared_pole_in_upper_halfplane": mp.im(off_pole) > 0,
        "blaschke_deficit_exponential_bound_sample": deficit > 0 and deficit <= deficit_bound,
        "rh_claim_remains_false": True,
    }
    return {
        "schema": "SOH_HALFPLANE_SIN_QUOTIENT_WEYL_M_V0_5",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "rh_claim": False,
        "epistemic_status": "EXACT_SIN_QUOTIENT_HALFPLANE__STANDARD_ZERO_COUNT_PLUS_EXACT_BLASCHKE__RH_EQUIVALENT_HERGLOTZ_ZEROSET_GATE__RH_OPEN",
        "first_t_zero_numeric": mp.nstr(tzeros[0], 35),
        "first_lambda_zero_numeric": mp.nstr(tzeros[0]**2, 35),
        "open": {"construct_weyl_M_from_Xi_theta_without_zero_input": True, "riemann_hypothesis": True},
        "checks": checks,
    }


def main() -> int:
    receipt = build_receipt()
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0 if receipt["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
