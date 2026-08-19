from __future__ import annotations

import mpmath as mp

from secret_of_a_half.jensen_wiener_kernel import (
    G004_STRONG_LOG_CONCAVITY_MARGIN,
    G024_FIRST_ORDER_CM_UNIFORM_FLOOR,
    G024_SHARPENED_FIRST_ORDER_CM_UNIFORM_FLOOR,
    G024_SHARPENED_STRONG_CONVEXITY_MARGIN,
    bridge_even_moment_upper_bound,
    bridge_square_exponential_mgf_upper_bound,
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


def test_conservative_and_sharpened_strong_convexity_constants() -> None:
    assert G004_STRONG_LOG_CONCAVITY_MARGIN == mp.mpf("10")
    assert G024_FIRST_ORDER_CM_UNIFORM_FLOOR == mp.mpf("9.5")
    assert G024_SHARPENED_STRONG_CONVEXITY_MARGIN == mp.mpf("17")
    assert G024_SHARPENED_FIRST_ORDER_CM_UNIFORM_FLOOR == mp.mpf("16.5")


def test_channel_curvature_polynomial_floor_is_positive() -> None:
    # h(r)-19 has numerator 16x^3+20x^2-24x+9 for x=r-3>=0.
    # Its quadratic part has negative discriminant; this numerical fixture only
    # protects the exact polynomial recorded in the proof note.
    discriminant = (-24) ** 2 - 4 * 20 * 9
    assert discriminant == -144
    for x in (mp.mpf("0"), mp.mpf("0.1"), mp.mpf("1"), mp.mpf("10")):
        assert 16 * x**3 + 20 * x**2 - 24 * x + 9 > 0


def test_first_order_sharpened_log_slope_bound_above_thirty_three_halves() -> None:
    mp.mp.dps = 50
    for y in (mp.mpf("0"), mp.mpf("0.25"), mp.mpf("0.49"), mp.mpf("0.499999")):
        for q in (mp.mpf("0"), mp.mpf("1e-8"), mp.mpf("0.1"), mp.mpf("1"), mp.mpf("100")):
            bound = first_order_cm_log_slope_lower_bound(
                q,
                y,
                strong_log_concavity_margin=G024_SHARPENED_STRONG_CONVEXITY_MARGIN,
            )
            assert bound > G024_SHARPENED_FIRST_ORDER_CM_UNIFORM_FLOOR


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


def test_bridge_even_moment_hierarchy_sharpened_bounds() -> None:
    mp.mp.dps = 50
    m = G024_SHARPENED_STRONG_CONVEXITY_MARGIN
    expected = {
        0: mp.mpf("1"),
        1: mp.mpf("3") / 34,
        2: mp.mpf("15") / (34**2),
        3: mp.mpf("105") / (34**3),
        4: mp.mpf("945") / (34**4),
    }
    for order, value in expected.items():
        observed = bridge_even_moment_upper_bound(
            order,
            strong_log_concavity_margin=m,
        )
        assert mp.almosteq(observed, value)
    for order in range(4):
        left = bridge_even_moment_upper_bound(
            order + 1,
            strong_log_concavity_margin=m,
        )
        right = (
            mp.mpf(2 * order + 3)
            / 34
            * bridge_even_moment_upper_bound(
                order,
                strong_log_concavity_margin=m,
            )
        )
        assert mp.almosteq(left, right)


def test_bridge_square_exponential_mgf_sharpened_envelope() -> None:
    mp.mp.dps = 50
    lam = mp.mpf("3")
    observed = bridge_square_exponential_mgf_upper_bound(
        lam,
        strong_log_concavity_margin=G024_SHARPENED_STRONG_CONVEXITY_MARGIN,
    )
    expected = mp.power(mp.mpf("17") / 14, mp.mpf("1.5"))
    assert mp.almosteq(observed, expected)
    assert observed > 1


def test_sharpened_second_order_one_ninth_constants() -> None:
    mp.mp.dps = 80
    e_upper = mp.mpf(87) / 32
    assert mp.e < e_upper
    assert mp.power(mp.mpf("17") / 14, mp.mpf("1.5")) < mp.mpf(47) / 35
    c17 = 42 * mp.exp(mp.mpf("1") / 3) * mp.power(mp.mpf("17") / 14, mp.mpf("1.5"))
    assert c17 < 79

    # Exact integer comparison used for F(1/3)>0 after e<87/32.
    assert 79**3 * 87**2 < 154**3 * 32**2

    u = mp.mpf("1") / 3
    f_boundary = 33 + 1089 * u**2 - 79 * mp.exp(2 * u)
    assert f_boundary > 0

    derivative_floor = 726 - 158 * e_upper
    assert derivative_floor == mp.mpf(4743) / 16
    assert derivative_floor > 0


def test_second_order_bridge_reduction_matches_gaussian_closed_form() -> None:
    mp.mp.dps = 60
    u = mp.mpf("0.37")
    y = mp.mpf("0.23")
    q = u * u

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
