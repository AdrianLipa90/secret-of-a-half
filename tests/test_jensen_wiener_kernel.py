from __future__ import annotations

import mpmath as mp

from secret_of_a_half.jensen_wiener_kernel import (
    G004_STRONG_LOG_CONCAVITY_MARGIN,
    G024_FIRST_ORDER_CM_UNIFORM_FLOOR,
    csordas_correlation_from_kernel,
    dimitrov_xu_tilted_from_kernel,
    first_order_cm_log_slope_lower_bound,
    full_xi_kernel,
    internal_tilt_jensen_kernel_from_kernel,
    second_order_cm_normalized_margin_from_bridge,
    signed_five_point_derivatives,
)


def _gaussian(t: mp.mpf) -> mp.mpf:
    return mp.exp(-t * t / 2)


def test_full_xi_kernel_is_even_and_positive() -> None:
    mp.mp.dps = 40
    for t in (mp.mpf("0"), mp.mpf("0.2"), mp.mpf("0.8"), mp.mpf("1.5")):
        left = full_xi_kernel(-t, n_terms=8)
        right = full_xi_kernel(t, n_terms=8)
        assert right > 0
        assert mp.almosteq(left, right)


def test_gaussian_csordas_correlation_closed_form() -> None:
    mp.mp.dps = 40
    u = mp.mpf("0.37")
    observed = csordas_correlation_from_kernel(
        u,
        kernel=_gaussian,
        center_cutoff=8,
    )
    expected = mp.sqrt(mp.pi) * mp.exp(-u * u) / 2
    assert abs(observed - expected) < mp.mpf("1e-20")


def test_gaussian_dimitrov_xu_external_tilt_closed_form() -> None:
    mp.mp.dps = 40
    u = mp.mpf("0.31")
    y = mp.mpf("0.23")
    observed = dimitrov_xu_tilted_from_kernel(
        u,
        y,
        kernel=_gaussian,
        center_cutoff=8,
    )
    expected = (
        mp.cosh(2 * y * u)
        * mp.sqrt(mp.pi)
        * mp.exp(-u * u)
        / 2
    )
    assert abs(observed - expected) < mp.mpf("1e-20")


def test_gaussian_internal_tilt_closed_form_and_not_external_tilt() -> None:
    mp.mp.dps = 40
    u = mp.mpf("0.31")
    y = mp.mpf("0.23")
    internal = internal_tilt_jensen_kernel_from_kernel(
        u,
        y,
        kernel=_gaussian,
        center_cutoff=8,
    )
    expected_internal = (
        mp.sqrt(mp.pi)
        * mp.exp(y * y - u * u)
        * (mp.mpf("0.5") + y * y)
    )
    external = dimitrov_xu_tilted_from_kernel(
        u,
        y,
        kernel=_gaussian,
        center_cutoff=8,
    )
    assert abs(internal - expected_internal) < mp.mpf("1e-20")
    assert abs(internal - external) > mp.mpf("1e-6")


def test_g004_strong_log_concavity_margin_exceeds_first_order_threshold() -> None:
    assert G004_STRONG_LOG_CONCAVITY_MARGIN == mp.mpf("10")
    assert G004_STRONG_LOG_CONCAVITY_MARGIN > mp.mpf("0.5")
    assert G024_FIRST_ORDER_CM_UNIFORM_FLOOR == mp.mpf("9.5")


def test_first_order_cm_log_slope_bound_is_uniformly_above_nineteen_halves() -> None:
    mp.mp.dps = 50
    for y in (mp.mpf("0"), mp.mpf("0.25"), mp.mpf("0.49"), mp.mpf("0.499999")):
        for q in (mp.mpf("0"), mp.mpf("1e-8"), mp.mpf("0.1"), mp.mpf("1"), mp.mpf("100")):
            bound = first_order_cm_log_slope_lower_bound(q, y)
            assert bound > G024_FIRST_ORDER_CM_UNIFORM_FLOOR


def test_first_order_cm_threshold_margin_one_half_is_sufficient() -> None:
    mp.mp.dps = 50
    threshold = mp.mpf("0.5")
    for y in (mp.mpf("0"), mp.mpf("0.25"), mp.mpf("0.49")):
        for q in (mp.mpf("0"), mp.mpf("0.1"), mp.mpf("2")):
            bound = first_order_cm_log_slope_lower_bound(
                q,
                y,
                strong_log_concavity_margin=threshold,
            )
            assert bound > 0


def test_second_order_bridge_reduction_matches_gaussian_closed_form() -> None:
    mp.mp.dps = 60
    u = mp.mpf("0.37")
    y = mp.mpf("0.23")
    q = u * u

    # For K(t)=exp(-t^2/2), L=t^2/2, hence A=2u, B=2, Var(A)=0.
    bridge_margin = second_order_cm_normalized_margin_from_bridge(
        u,
        y,
        mean_a=2 * u,
        mean_b=2,
        var_a=0,
    )

    constant = mp.sqrt(mp.pi) / 2
    h = lambda x: constant * mp.exp(-x) * mp.cosh(2 * y * mp.sqrt(x))
    direct_margin = 4 * u**3 * mp.diff(h, q, 2) / h(q)
    assert abs(bridge_margin - direct_margin) < mp.mpf("1e-45")


def test_signed_five_point_derivatives_on_completely_monotone_exponential() -> None:
    mp.mp.dps = 50
    a = mp.mpf("1.7")
    q = mp.mpf("0.4")
    h = mp.mpf("0.0005")
    values = signed_five_point_derivatives(
        lambda x: mp.exp(-a * x),
        q,
        h=h,
    )
    for order, observed in values.items():
        expected = a**order * mp.exp(-a * q)
        assert observed > 0
        assert abs(observed - expected) / expected < mp.mpf("1e-5")
