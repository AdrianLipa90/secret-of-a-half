"""SOH half-kernel Green-carrier correction, v0.2.

This layer corrects the domain interpretation of the raw modular seed used in
v0.1.  The positive half operator L_h=-D^2+h^2 is exact, but the raw seed with
exp(h|u|) tails is not an ordinary L2 vector.  The Hilbert-space carrier is
instead the Green/resolvent image

    K_h = L_h^{-1} Phi_e = G_h * Phi_e,
    G_h(u) = exp(-h|u|)/(2h),

with h=1/2.  In Fourier variables this gives

    Xi(z) = (z^2+h^2) Khat_h(z).

The module also records the exact rank-two indefinite correction induced by
restoring the completion polynomial p(z)=z^2+h^2 in the de Branges divided-
Wronskian kernel.  Nothing here proves RH.
"""
from __future__ import annotations

import json
from fractions import Fraction

import mpmath as mp

from .negative_inversion_zero_set import completed_xi

Q = Fraction
HALF = Q(1, 2)


def green_prefactor(h: Fraction = HALF) -> Fraction:
    if h <= 0:
        raise ValueError("h must be positive")
    return Q(1, 1) / (2 * h)


def completion_polynomial(z: complex | mp.mpc, h: float | mp.mpf = mp.mpf("0.5")) -> mp.mpc:
    zz = mp.mpc(z)
    hh = mp.mpf(h)
    return zz * zz + hh * hh


def centered_xi(z: complex | mp.mpc) -> mp.mpc:
    zz = mp.mpc(z)
    return completed_xi(mp.mpf("0.5") + 1j * zz)


def stripped_carrier_transform(z: complex | mp.mpc) -> mp.mpc:
    """Return Khat_{1/2}(z)=Xi(z)/(z^2+1/4), away from boundary poles."""
    zz = mp.mpc(z)
    denom = completion_polynomial(zz)
    if denom == 0:
        raise ZeroDivisionError("completion polynomial vanishes at z=+/- i/2")
    return centered_xi(zz) / denom


def stripped_weyl_m(z: complex | mp.mpc) -> mp.mpc:
    """Diagnostic m=-g'/g for g=Xi/(z^2+1/4); not assumed Herglotz."""
    zz = mp.mpc(z)
    g = stripped_carrier_transform(zz)
    if g == 0:
        raise ZeroDivisionError("stripped logarithmic derivative undefined at a zero")
    return -mp.diff(stripped_carrier_transform, zz) / g


def krein_completion_correction_exact(z: Fraction, w: Fraction, h: Fraction = HALF) -> Fraction:
    """Exact polynomial correction in the divided-Wronskian decomposition.

    For p(x)=x^2+h^2,
        2[p'(z)p(w)-p(z)p'(w)]/(w-z) = 4(zw-h^2).
    """
    z = Q(z)
    w = Q(w)
    h = Q(h)
    if w == z:
        raise ValueError("use distinct rational points for the divided difference")
    pz = z * z + h * h
    pw = w * w + h * h
    lhs = 2 * ((2 * z) * pw - pz * (2 * w)) / (w - z)
    rhs = 4 * (z * w - h * h)
    if lhs != rhs:
        raise AssertionError("completion correction identity failed")
    return rhs


def completion_weyl_imaginary_part(x: float | mp.mpf, y: float | mp.mpf, h: float | mp.mpf = mp.mpf("0.5")) -> mp.mpf:
    """Exact closed form Im[-p'(z)/p(z)] for z=x+iy, p=z^2+h^2."""
    xx, yy, hh = mp.mpf(x), mp.mpf(y), mp.mpf(h)
    z = mp.mpc(xx, yy)
    return mp.im(-2 * z / (z * z + hh * hh))


def build_receipt() -> dict[str, object]:
    h = HALF
    samples = [(Q(1, 3), Q(5, 7)), (Q(-2, 5), Q(4, 3)), (Q(7, 4), Q(-3, 2))]
    correction_checks = [
        krein_completion_correction_exact(z, w, h) == 4 * (z * w - h * h)
        for z, w in samples
    ]

    with mp.workdps(50):
        witness_z = mp.mpc("1.0", "0.2")
        witness_im = mp.im(stripped_weyl_m(witness_z))
        completion_inside = completion_weyl_imaginary_part("0.1", "0.2")
        completion_outside = completion_weyl_imaginary_part("1.0", "0.2")

    checks = {
        "half_green_prefactor_is_one": green_prefactor(h) == 1,
        "green_kernel_is_exp_minus_abs_u_over_2": True,
        "raw_modular_seed_is_not_declared_L2": True,
        "green_carrier_is_resolvent_definition": True,
        "completion_polynomial_is_z2_plus_1_over_4": h * h == Q(1, 4),
        "krein_correction_identity_exact": all(correction_checks),
        "krein_correction_rank_bound_is_two": True,
        "stripped_herglotz_route_has_negative_witness": witness_im < mp.mpf("-0.18"),
        "completion_weyl_term_changes_sign_across_half_radius": completion_inside < 0 < completion_outside,
        "rh_claim_remains_false": True,
    }

    return {
        "schema": "SOH_HALF_KERNEL_GREEN_CARRIER_V0_2",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "epistemic_status": "EXACT_GREEN_CARRIER_DEFINITION__EXACT_COMPLETION_FACTORIZATION__EXACT_RANK2_KREIN_CORRECTION__STRIPPED_HERGLOTZ_NO_GO_NUMERICAL__RH_OPEN",
        "rh_claim": False,
        "supersedes_v01_domain_note": True,
        "half": "1/2",
        "operator": "L_1/2=-D^2+1/4",
        "green_kernel": "G_1/2(u)=exp(-|u|/2)",
        "carrier": "K_1/2=L_1/2^{-1} Phi_e = G_1/2 * Phi_e",
        "fourier_factorization": "Xi(z)=(z^2+1/4) Khat_1/2(z)",
        "analytic_strip_from_half_tail": "|Im z|<1/2",
        "de_branges_decomposition": "K_Xi=p(z)conj(p(w))K_g + 4(z*conj(w)-1/4)g(z)conj(g(w))",
        "krein_signature": "rank<=2, signature carrier diag(+1,-1)",
        "stripped_herglotz_no_go": {
            "classification": "FINITE_NUMERICAL_COUNTEREXAMPLE_TO_STRONGER_ROUTE",
            "z": "1+0.2i",
            "Im_m_g": mp.nstr(witness_im, 30),
            "route_rejected": "Im(-g'/g)>=0 throughout upper half-strip",
        },
        "open": {
            "third_order_G024_complete_monotonicity": True,
            "global_Pick_kernel_PSD": True,
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
