from fractions import Fraction

from secret_of_a_half.half_kernel_operator_bridge import (
    build_receipt,
    canonical_inverse_ladder,
    half_projector,
    positive_half_operator,
)


def test_positive_half_operator_is_exact() -> None:
    assert positive_half_operator() == [
        [Fraction(2), Fraction(-1), Fraction(0), Fraction(0)],
        [Fraction(-1), Fraction(2), Fraction(-1), Fraction(0)],
        [Fraction(0), Fraction(-1), Fraction(2), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(0), Fraction(0)],
    ]


def test_half_projector_is_exact() -> None:
    assert half_projector() == [
        [Fraction(0), Fraction(0), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(0), Fraction(1)],
    ]


def test_inverse_ladder_exact() -> None:
    assert canonical_inverse_ladder() == {
        "c_inv": Fraction(5, 2),
        "a_inv": Fraction(7, 2),
        "b_inv": Fraction(9, 2),
    }


def test_receipt_passes_but_keeps_rh_open() -> None:
    receipt = build_receipt()
    assert receipt["status"] == "PASS"
    assert receipt["rh_claim"] is False
    assert receipt["physical_promotion"] is False
    assert receipt["open"]["construct_explicit_V_y_T_from_theta_translations"] is True
    assert receipt["open"]["close_XF8C_RH_equivalent_gate"] is True
    assert receipt["open"]["riemann_hypothesis"] is True
    assert all(receipt["checks"].values())
