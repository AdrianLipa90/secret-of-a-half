#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp

from secret_of_a_half.jensen_wiener_kernel import (
    G004_STRONG_LOG_CONCAVITY_MARGIN,
    G024_FIRST_ORDER_CM_UNIFORM_FLOOR,
    csordas_correlation_from_kernel,
    dimitrov_xu_tilted_from_kernel,
    first_order_cm_log_slope_lower_bound,
    internal_tilt_jensen_kernel_from_kernel,
    radial_square_profile,
    second_order_cm_normalized_margin_from_bridge,
    signed_five_point_derivatives,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports" / "SOH_G024_JENSEN_WIENER_KERNEL_RECEIPT_V1.json"


def gaussian(t: mp.mpf) -> mp.mpf:
    return mp.exp(-t * t / 2)


def main() -> None:
    mp.mp.dps = 50

    # Closed-form regression for the exact centered correlation identities.
    # The numerical integral is deliberately evaluated farther into the Gaussian
    # tail than the Riemann-kernel finite diagnostic below.
    u = mp.mpf("0.31")
    y = mp.mpf("0.23")
    gaussian_cutoff = mp.mpf("8")
    c_obs = csordas_correlation_from_kernel(
        u,
        kernel=gaussian,
        center_cutoff=gaussian_cutoff,
    )
    c_exp = mp.sqrt(mp.pi) * mp.exp(-u * u) / 2
    if abs(c_obs - c_exp) > mp.mpf("1e-20"):
        raise RuntimeError("Gaussian centered-correlation regression failed")

    d_obs = dimitrov_xu_tilted_from_kernel(
        u,
        y,
        kernel=gaussian,
        center_cutoff=gaussian_cutoff,
    )
    d_exp = mp.cosh(2 * y * u) * c_exp
    if abs(d_obs - d_exp) > mp.mpf("1e-20"):
        raise RuntimeError("Gaussian Dimitrov-Xu external-tilt regression failed")

    j_obs = internal_tilt_jensen_kernel_from_kernel(
        u,
        y,
        kernel=gaussian,
        center_cutoff=gaussian_cutoff,
    )
    j_exp = (
        mp.sqrt(mp.pi)
        * mp.exp(y * y - u * u)
        * (mp.mpf("0.5") + y * y)
    )
    if abs(j_obs - j_exp) > mp.mpf("1e-20"):
        raise RuntimeError("Gaussian internal-tilt regression failed")
    if abs(d_obs - j_obs) <= mp.mpf("1e-6"):
        raise RuntimeError("external and internal y-tilts were incorrectly identified")

    # Exact first-order complete-monotonicity theorem. SOH-G004 supplies
    # (log Phi)'' < -10. Therefore L=-log K has L'' > 10 and the centered
    # correlation satisfies -C'/C > 20u. This implies the declared global
    # lower bound for -H_y'/H_y on the full Dimitrov-Xu strip.
    exact_margin_rows: list[dict[str, str]] = []
    for yy in (mp.mpf("0"), mp.mpf("0.25"), mp.mpf("0.49"), mp.mpf("0.499999")):
        for qq in (mp.mpf("0"), mp.mpf("0.1"), mp.mpf("1"), mp.mpf("100")):
            bound = first_order_cm_log_slope_lower_bound(qq, yy)
            if not bound > G024_FIRST_ORDER_CM_UNIFORM_FLOOR:
                raise RuntimeError("exact G024 first-order CM margin regression failed")
            exact_margin_rows.append(
                {
                    "y": mp.nstr(yy, 8),
                    "q": mp.nstr(qq, 8),
                    "analytic_lower_bound": mp.nstr(bound, 30),
                }
            )

    # Exact second-order reduction regression on the Gaussian fixture. For
    # K=exp(-t^2/2), L=t^2/2, hence A=2u, B=2 and Var(A)=0 exactly.
    q_gauss = u * u
    bridge_second_margin = second_order_cm_normalized_margin_from_bridge(
        u,
        y,
        mean_a=2 * u,
        mean_b=2,
        var_a=0,
    )
    h_gauss = lambda q: (
        mp.sqrt(mp.pi)
        / 2
        * mp.exp(-q)
        * mp.cosh(2 * y * mp.sqrt(q))
    )
    direct_second_margin = 4 * u**3 * mp.diff(h_gauss, q_gauss, 2) / h_gauss(q_gauss)
    if abs(bridge_second_margin - direct_second_margin) > mp.mpf("1e-35"):
        raise RuntimeError("Gaussian second-order bridge reduction regression failed")

    # Finite numerical diagnostic for the actual Riemann kernel. Passing signs
    # here is deliberately not promoted to complete monotonicity beyond the
    # independently proved first-order inequality above.
    y_grid = [mp.mpf("0"), mp.mpf("0.25"), mp.mpf("0.49")]
    q_grid = [mp.mpf("0.1"), mp.mpf("0.2")]
    h = mp.mpf("0.002")
    rows: list[dict[str, object]] = []

    for yy in y_grid:
        for qq in q_grid:
            values = signed_five_point_derivatives(
                lambda q_value: radial_square_profile(
                    q_value,
                    yy,
                    n_terms=6,
                    center_cutoff=4,
                ),
                qq,
                h=h,
            )
            if not all(value > 0 for value in values.values()):
                raise RuntimeError(
                    f"finite G024 sign diagnostic failed at y={yy}, q={qq}"
                )
            rows.append(
                {
                    "y": mp.nstr(yy, 8),
                    "q": mp.nstr(qq, 8),
                    "signed_derivatives": {
                        str(order): mp.nstr(value, 30)
                        for order, value in values.items()
                    },
                }
            )

    payload = {
        "certificate": "SOH_G024_JENSEN_WIENER_KERNEL_RECEIPT_V1",
        "status": "EXACT_FIRST_ORDER_CM_AND_SECOND_ORDER_REDUCTION_PLUS_FINITE_HIGHER_ORDER_DIAGNOSTIC_PASS",
        "exact_checks": {
            "gaussian_centered_correlation_closed_form": True,
            "gaussian_external_tilt_closed_form": True,
            "gaussian_internal_tilt_closed_form": True,
            "gaussian_regression_cutoff": mp.nstr(gaussian_cutoff, 8),
            "external_internal_tilts_distinct_for_nonzero_y": True,
            "dimitrov_xu_change_of_variables": "nu_2(2u)=4*C(u)",
            "dimitrov_xu_rescaled_kernel": "Psi_y(2u)=4*cosh(2yu)*C(u)",
            "g004_per_channel_log_curvature_upper": "-12",
            "g004_mixture_slope_variance_upper": "2",
            "full_kernel_strong_log_concavity_margin": mp.nstr(
                G004_STRONG_LOG_CONCAVITY_MARGIN, 8
            ),
            "correlation_log_decay": "-C'(u)/C(u) > 20u for u>0",
            "first_order_complete_monotonicity_proved": True,
            "uniform_first_order_log_slope_lower_floor": "19/2",
            "analytic_margin_regression_rows": exact_margin_rows,
            "second_order_bridge_identity": "4u^3 H_y''/H_y = N + u[N^2 + Var(A) - E(B) + 4y^2 sech^2(2|y|u)]",
            "gaussian_second_order_bridge_regression": True,
        },
        "finite_diagnostic": {
            "classification": "FINITE_DIAGNOSTIC_NOT_PROOF_FOR_ORDERS_2_TO_4",
            "n_terms": 6,
            "center_cutoff": "4",
            "finite_difference_h": mp.nstr(h, 8),
            "orders": [1, 2, 3, 4],
            "rows": rows,
        },
        "proof_firewall": {
            "first_order_complete_monotonicity_proved": True,
            "second_order_reduced_exactly": True,
            "second_order_complete_monotonicity_proved": False,
            "higher_order_complete_monotonicity_proved": False,
            "complete_monotonicity_all_orders_proved": False,
            "strict_fourier_positivity_proved": False,
            "wiener_density_proved_for_riemann_family": False,
            "soh_g003_real_rootedness_proved": False,
            "pf3_proved": False,
            "pf_infinity_proved": False,
            "rh_proved": False,
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
