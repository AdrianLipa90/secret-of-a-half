from __future__ import annotations

import mpmath as mp

from secret_of_a_half.half_kernel_green_carrier import (
    HALF,
    build_receipt,
    completion_weyl_imaginary_part,
    green_prefactor,
    krein_completion_correction_exact,
    stripped_weyl_m,
)


def test_half_green_normalization_exact() -> None:
    assert green_prefactor(HALF) == 1


def test_krein_completion_correction_exact_on_rationals() -> None:
    from fractions import Fraction as Q

    assert krein_completion_correction_exact(Q(1, 3), Q(5, 7)) == 4 * (Q(5, 21) - Q(1, 4))
    assert krein_completion_correction_exact(Q(-2, 5), Q(4, 3)) == 4 * (Q(-8, 15) - Q(1, 4))


def test_completion_weyl_term_changes_sign_at_half_radius() -> None:
    with mp.workdps(50):
        assert completion_weyl_imaginary_part("0.1", "0.2") < 0
        assert completion_weyl_imaginary_part("1.0", "0.2") > 0


def test_stripped_herglotz_stronger_route_is_rejected() -> None:
    with mp.workdps(50):
        witness = mp.im(stripped_weyl_m(mp.mpc("1.0", "0.2")))
        assert witness < mp.mpf("-0.18")


def test_receipt_is_fail_closed_and_keeps_rh_open() -> None:
    receipt = build_receipt()
    assert receipt["status"] == "PASS"
    assert receipt["rh_claim"] is False
    assert receipt["supersedes_v01_domain_note"] is True
    assert receipt["open"]["third_order_G024_complete_monotonicity"] is True
    assert receipt["open"]["riemann_hypothesis"] is True
