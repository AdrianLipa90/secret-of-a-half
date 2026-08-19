from fractions import Fraction

from secret_of_a_half.pf3_curvature_barrier import (
    barrier_certificate,
    cubic_floor,
    decomposed_margin,
    one_step_barrier,
    pf3_margin,
)


def test_exact_decomposition_with_rational_inputs() -> None:
    u = Fraction(1, 2)
    v = Fraction(3, 5)
    w = Fraction(7, 10)
    assert pf3_margin(u, v, w) == decomposed_margin(u, v, w)


def test_barrier_certificate_gives_cubic_floor() -> None:
    u = Fraction(1, 2)
    v = Fraction(3, 5)
    w = Fraction(7, 10)
    cert = barrier_certificate(u, v, w)
    assert one_step_barrier(u, v) == Fraction(1, 10)
    assert cert["assumptions_hold"] is True
    assert cert["solid_minor_certified_positive"] is True
    assert cert["margin"] >= cubic_floor(v) > 0
    assert cert["decomposition_residual"] == 0


def test_barrier_equivalent_one_step_ratio_bound() -> None:
    u = Fraction(3, 4)
    v = Fraction(4, 5)
    barrier = one_step_barrier(u, v)
    assert barrier == 0
    assert v == Fraction(1, 2 - u)


def test_g021_counterexample_is_not_covered_by_g022() -> None:
    u = Fraction(1, 5)
    v = Fraction(9, 10)
    w = Fraction(1, 5)
    cert = barrier_certificate(u, v, w)
    assert pf3_margin(u, v, w) == Fraction(-1271, 2500)
    assert cert["barrier"] < 0
    assert cert["order_gap"] < 0
    assert cert["assumptions_hold"] is False
    assert cert["solid_minor_certified_positive"] is False


def test_forward_order_and_barrier_are_sufficient_not_claimed_necessary() -> None:
    # The API only certifies the stated sufficient package.  It deliberately
    # does not label a point outside the package as a PF3 failure.
    cert = barrier_certificate(Fraction(9, 10), Fraction(4, 5), Fraction(3, 4))
    assert cert["assumptions_hold"] is False
