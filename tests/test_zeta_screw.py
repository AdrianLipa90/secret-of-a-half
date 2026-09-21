from __future__ import annotations

import mpmath as mp
import pytest

from secret_of_a_half.zeta_screw import (
    mangoldt_hinge_sum,
    mangoldt_sqrt_sum,
    psi_positive,
    psi_prime_positive,
    screw_formula_receipt,
    screw_kernel_value,
    zeta_screw_g,
    zeta_screw_g_prime,
)


def test_psi_and_screw_origin_and_evenness() -> None:
    assert psi_positive(0) == 0
    assert zeta_screw_g(0) == 0
    for t in ("0.1", "0.5", "1.0"):
        assert zeta_screw_g(t) == pytest.approx(float(zeta_screw_g(f"-{t}")))


def test_prime_hinge_is_empty_below_log_two() -> None:
    t = mp.mpf("0.3")
    assert t < mp.log(2)
    assert mangoldt_hinge_sum(t) == 0
    assert mangoldt_sqrt_sum(t) == 0


def test_psi_prime_matches_direct_derivative_of_equation_1_1() -> None:
    # Suzuki 2023, equation (1.1), in the prime-free range 0<t<log 2.
    #
    # Direct differentiation gives
    #   Psi'(t) = 2(e^(t/2)-e^(-t/2))
    #             + 1/2*(digamma(1/4)-log(pi))
    #             + atanh(e^(-t/2)) + atan(e^(-t/2)).
    #
    # The closed formula printed later in the proof of Theorem 4.1 omits
    # exactly -(1/2)log(pi) relative to (1.1).  The implementation follows
    # the source definition (1.1), which is also independently checked below
    # against numerical differentiation.
    t = mp.mpf("0.3")
    r = mp.e ** (-t / 2)
    expected = (
        2 * (mp.e ** (t / 2) - mp.e ** (-t / 2))
        + (mp.digamma(mp.mpf("0.25")) - mp.log(mp.pi)) / 2
        + mp.atanh(r)
        + mp.atan(r)
    )
    actual = psi_prime_positive(t)
    assert actual == pytest.approx(float(expected), rel=1e-11, abs=1e-11)


def test_published_theorem_4_1_derivative_offset_is_half_log_pi() -> None:
    # Regression receipt for the source-text discrepancy noted above.
    t = mp.mpf("0.3")
    c = mp.pi / 4 - (mp.euler + 3 * mp.log(2)) / 2
    printed = (
        2 * (mp.e ** (t / 2) - mp.e ** (-t / 2))
        + c
        - mp.atan(mp.e ** (t / 2))
        + mp.atanh(mp.e ** (-t / 2))
    )
    direct = psi_prime_positive(t)
    assert direct - printed == pytest.approx(float(-mp.log(mp.pi) / 2), rel=1e-11, abs=1e-11)


def test_psi_prime_matches_numerical_derivative_away_from_thresholds() -> None:
    mp.mp.dps = 60
    t = mp.mpf("0.37")
    numeric = mp.diff(lambda x: psi_positive(x), t)
    analytic = psi_prime_positive(t)
    assert analytic == pytest.approx(float(numeric), rel=1e-10, abs=1e-10)


def test_screw_derivative_is_odd_away_from_zero() -> None:
    t = mp.mpf("0.37")
    gp = zeta_screw_g_prime(t)
    gm = zeta_screw_g_prime(-t)
    assert gp == pytest.approx(float(-gm), rel=1e-11, abs=1e-11)


def test_screw_kernel_is_real_symmetric() -> None:
    points = [("0.2", "0.4"), ("0.3", "-0.25"), ("0.7", "0.1")]
    for t, u in points:
        a = screw_kernel_value(t, u)
        b = screw_kernel_value(u, t)
        assert a == pytest.approx(float(b), rel=1e-10, abs=1e-10)
        assert abs(mp.im(a)) == 0


def test_source_formula_receipt_stays_numerical() -> None:
    receipt = screw_formula_receipt()
    assert receipt["numerical_only"] is True
    assert receipt["proof_of_rh"] is False
    assert "rigorous interval enclosure of g and g-prime" in receipt["open"]


def test_derivative_at_origin_fails_closed() -> None:
    with pytest.raises(ValueError):
        zeta_screw_g_prime(0)
