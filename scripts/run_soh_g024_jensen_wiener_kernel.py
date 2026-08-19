#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp

from secret_of_a_half.jensen_wiener_kernel import (
    G024_SHARPENED_FIRST_ORDER_CM_UNIFORM_FLOOR,
    G024_SHARPENED_STRONG_CONVEXITY_MARGIN,
    bridge_even_moment_upper_bound,
    bridge_square_exponential_mgf_upper_bound,
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
    mp.mp.dps = 60

    u = mp.mpf("0.31")
    y = mp.mpf("0.23")
    gaussian_cutoff = mp.mpf("8")
    c_obs = csordas_correlation_from_kernel(u, kernel=gaussian, center_cutoff=gaussian_cutoff)
    c_exp = mp.sqrt(mp.pi) * mp.exp(-u * u) / 2
    if abs(c_obs - c_exp) > mp.mpf("1e-20"):
        raise RuntimeError("Gaussian centered-correlation regression failed")

    d_obs = dimitrov_xu_tilted_from_kernel(u, y, kernel=gaussian, center_cutoff=gaussian_cutoff)
    d_exp = mp.cosh(2 * y * u) * c_exp
    if abs(d_obs - d_exp) > mp.mpf("1e-20"):
        raise RuntimeError("Gaussian external-tilt regression failed")

    j_obs = internal_tilt_jensen_kernel_from_kernel(u, y, kernel=gaussian, center_cutoff=gaussian_cutoff)
    j_exp = mp.sqrt(mp.pi) * mp.exp(y * y - u * u) * (mp.mpf("0.5") + y * y)
    if abs(j_obs - j_exp) > mp.mpf("1e-20"):
        raise RuntimeError("Gaussian internal-tilt regression failed")
    if abs(d_obs - j_obs) <= mp.mpf("1e-6"):
        raise RuntimeError("external and internal y-tilts were incorrectly identified")

    # Sharpened first-order theorem: L''>17 -> -H'/H>33/2.
    exact_margin_rows: list[dict[str, str]] = []
    for yy in (mp.mpf("0"), mp.mpf("0.25"), mp.mpf("0.49"), mp.mpf("0.499999")):
        for qq in (mp.mpf("0"), mp.mpf("1e-8"), mp.mpf("0.1"), mp.mpf("1"), mp.mpf("100")):
            bound = first_order_cm_log_slope_lower_bound(
                qq,
                yy,
                strong_log_concavity_margin=G024_SHARPENED_STRONG_CONVEXITY_MARGIN,
            )
            if not bound > G024_SHARPENED_FIRST_ORDER_CM_UNIFORM_FLOOR:
                raise RuntimeError("sharpened first-order CM margin regression failed")
            exact_margin_rows.append({
                "y": mp.nstr(yy, 8),
                "q": mp.nstr(qq, 8),
                "analytic_lower_bound": mp.nstr(bound, 30),
            })

    # Exact second-order identity regression on Gaussian fixture.
    q_gauss = u * u
    bridge_second_margin = second_order_cm_normalized_margin_from_bridge(
        u, y, mean_a=2 * u, mean_b=2, var_a=0
    )
    h_gauss = lambda q: mp.sqrt(mp.pi) / 2 * mp.exp(-q) * mp.cosh(2 * y * mp.sqrt(q))
    direct_second_margin = 4 * u**3 * mp.diff(h_gauss, q_gauss, 2) / h_gauss(q_gauss)
    if abs(bridge_second_margin - direct_second_margin) > mp.mpf("1e-35"):
        raise RuntimeError("Gaussian second-order bridge regression failed")

    # Sharpened bridge hierarchy from L''>17.
    m = G024_SHARPENED_STRONG_CONVEXITY_MARGIN
    moment_bounds = {
        str(order): mp.nstr(
            bridge_even_moment_upper_bound(order, strong_log_concavity_margin=m), 30
        )
        for order in range(5)
    }
    if bridge_even_moment_upper_bound(1, strong_log_concavity_margin=m) != mp.mpf("3") / 34:
        raise RuntimeError("sharpened bridge second-moment envelope mismatch")
    lam = mp.mpf("3")
    mgf_bound = bridge_square_exponential_mgf_upper_bound(lam, strong_log_concavity_margin=m)
    expected_mgf = mp.power(mp.mpf("17") / 14, mp.mpf("1.5"))
    if not mp.almosteq(mgf_bound, expected_mgf):
        raise RuntimeError("sharpened bridge MGF envelope mismatch")

    # Exact arithmetic gates used in the q>=1/9 theorem.
    if (-24) ** 2 - 4 * 20 * 9 != -144:
        raise RuntimeError("channel curvature polynomial discriminant mismatch")
    e_upper = mp.mpf(87) / 32
    if not mp.e < e_upper:
        raise RuntimeError("declared rational upper bound on e failed")
    if not mp.power(mp.mpf("17") / 14, mp.mpf("1.5")) < mp.mpf(47) / 35:
        raise RuntimeError("declared bridge MGF rational enclosure failed")
    c17 = 42 * mp.exp(mp.mpf("1") / 3) * mp.power(mp.mpf("17") / 14, mp.mpf("1.5"))
    if not c17 < 79:
        raise RuntimeError("C17<79 comparison failed")
    integer_left = 79**3 * 87**2
    integer_right = 154**3 * 32**2
    if not integer_left < integer_right:
        raise RuntimeError("q=1/9 endpoint integer comparison failed")
    derivative_floor = 726 - 158 * e_upper
    if derivative_floor != mp.mpf(4743) / 16 or derivative_floor <= 0:
        raise RuntimeError("q>=1/9 monotonicity derivative floor failed")

    # Numerical diagnostics are still not proof inside q<1/9 or at orders >=3.
    y_grid = [mp.mpf("0"), mp.mpf("0.25"), mp.mpf("0.49")]
    q_grid = [mp.mpf("0.03"), mp.mpf("0.08"), mp.mpf("0.1"), mp.mpf("0.2")]
    h = mp.mpf("0.002")
    rows: list[dict[str, object]] = []
    for yy in y_grid:
        for qq in q_grid:
            values = signed_five_point_derivatives(
                lambda q_value: radial_square_profile(q_value, yy, n_terms=6, center_cutoff=4),
                qq,
                h=h,
            )
            if not all(value > 0 for value in values.values()):
                raise RuntimeError(f"finite G024 sign diagnostic failed at y={yy}, q={qq}")
            rows.append({
                "y": mp.nstr(yy, 8),
                "q": mp.nstr(qq, 8),
                "signed_derivatives": {
                    str(order): mp.nstr(value, 30) for order, value in values.items()
                },
            })

    payload = {
        "certificate": "SOH_G024_JENSEN_WIENER_KERNEL_RECEIPT_V1",
        "status": "EXACT_FIRST_ORDER_GLOBAL_SECOND_ORDER_Q_GE_ONE_NINTH_PLUS_FINITE_CORE_DIAGNOSTIC_PASS",
        "exact_checks": {
            "gaussian_centered_correlation_closed_form": True,
            "gaussian_external_tilt_closed_form": True,
            "gaussian_internal_tilt_closed_form": True,
            "external_internal_tilts_distinct_for_nonzero_y": True,
            "dimitrov_xu_change_of_variables": "nu_2(2u)=4*C(u)",
            "second_order_bridge_identity": "4u^3 H_y''/H_y = N + u[N^2 + Var(A) - E(B) + 4y^2 sech^2(2|y|u)]",
            "gaussian_second_order_bridge_regression": True,
            "sharpened_channel_curvature_floor": "-g_n'' > 19",
            "sharpened_full_kernel_strong_convexity": "L'' > 17",
            "correlation_log_decay": "-C'(u)/C(u) > 34u",
            "first_order_complete_monotonicity_proved": True,
            "uniform_first_order_log_slope_lower_floor": "33/2",
            "analytic_margin_regression_rows": exact_margin_rows,
            "bridge_score_hierarchy": "E[r^(2n+1)D_u]=(2n+3)E[r^(2n)]",
            "bridge_even_moment_bounds_sharpened": moment_bounds,
            "bridge_square_exponential_mgf": "E exp(lambda r^2) <= (1-lambda/17)^(-3/2)",
            "bridge_square_exponential_mgf_lambda": mp.nstr(lam, 8),
            "bridge_square_exponential_mgf_upper_bound": mp.nstr(mgf_bound, 30),
            "full_kernel_curvature_upper_envelope": "L''(s) < 21 exp(2|s|)",
            "mean_bridge_curvature_upper": "E[B_u] < 79 exp(2u)",
            "second_order_proved_region": "q>=1/9",
            "second_order_open_compact_core": "0<=q<1/9",
            "c17_numeric_regression": mp.nstr(c17, 30),
            "endpoint_integer_comparison": f"{integer_left} < {integer_right}",
        },
        "finite_diagnostic": {
            "classification": "FINITE_DIAGNOSTIC_NOT_PROOF_INSIDE_Q_LT_ONE_NINTH_OR_FOR_ORDERS_3_TO_4",
            "n_terms": 6,
            "center_cutoff": "4",
            "finite_difference_h": mp.nstr(h, 8),
            "orders": [1, 2, 3, 4],
            "rows": rows,
        },
        "proof_firewall": {
            "first_order_complete_monotonicity_proved": True,
            "second_order_reduced_exactly": True,
            "second_order_q_ge_one_ninth_proved": True,
            "second_order_q_lt_one_ninth_proved": False,
            "second_order_complete_monotonicity_global_proved": False,
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
