from __future__ import annotations

import mpmath as mp

from secret_of_a_half.jensen_wiener_kernel import (
    csordas_correlation_from_kernel,
    dimitrov_xu_tilted_from_kernel,
    full_xi_kernel,
    internal_tilt_jensen_kernel_from_kernel,
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
        center_cutoff=7,
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
        center_cutoff=7,
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
        center_cutoff=7,
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
        center_cutoff=7,
    )
    assert abs(internal - expected_internal) < mp.mpf("1e-20")
    assert abs(internal - external) > mp.mpf("1e-6")


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
