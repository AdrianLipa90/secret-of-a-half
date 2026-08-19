from fractions import Fraction

from secret_of_a_half.pf3_reciprocal_deficit import (
    increment_decomposition,
    lipschitz_certificate,
    pf3_margin_from_q,
    q_from_reciprocal_deficit,
    reciprocal_deficit,
    reconstructed_pf3_margin,
    transformed_margin,
)


def test_q_E_transform_is_exact() -> None:
    q = Fraction(3, 5)
    E = reciprocal_deficit(q)
    assert E == Fraction(5, 2)
    assert q_from_reciprocal_deficit(E) == q


def test_reciprocal_deficit_normal_form_exact() -> None:
    u = Fraction(1, 2)
    v = Fraction(3, 5)
    w = Fraction(7, 10)
    E_prev = reciprocal_deficit(u)
    E = reciprocal_deficit(v)
    E_next = reciprocal_deficit(w)
    assert reconstructed_pf3_margin(E_prev, E, E_next) == pf3_margin_from_q(u, v, w)
    assert transformed_margin(E_prev, E, E_next) == increment_decomposition(E_prev, E, E_next)


def test_monotone_one_lipschitz_increment_package_certifies_solid_minor() -> None:
    E_prev = Fraction(2, 1)
    E = Fraction(5, 2)
    E_next = Fraction(3, 1)
    cert = lipschitz_certificate(E_prev, E, E_next)
    assert cert["alpha"] == Fraction(1, 2)
    assert cert["beta"] == Fraction(1, 2)
    assert cert["assumptions_hold"] is True
    assert cert["solid_minor_certified_positive"] is True
    assert cert["transformed_margin"] > 0
    assert cert["decomposition_residual"] == 0


def test_g022_barrier_is_alpha_upper_bound() -> None:
    # q_{k-1}=1/2 and q_k=2/3 are exactly on the G022 barrier.
    u = Fraction(1, 2)
    v = Fraction(2, 3)
    E_prev = reciprocal_deficit(u)
    E = reciprocal_deficit(v)
    assert E - E_prev == 1
    assert v * (2 - u) == 1


def test_g021_counterexample_breaks_reciprocal_deficit_law() -> None:
    u = Fraction(1, 5)
    v = Fraction(9, 10)
    w = Fraction(1, 5)
    E_prev = reciprocal_deficit(u)
    E = reciprocal_deficit(v)
    E_next = reciprocal_deficit(w)
    cert = lipschitz_certificate(E_prev, E, E_next)
    assert cert["alpha"] > 1
    assert cert["beta"] < 0
    assert cert["assumptions_hold"] is False
    assert pf3_margin_from_q(u, v, w) == Fraction(-1271, 2500)


def test_outside_package_is_not_labeled_pf3_failure() -> None:
    cert = lipschitz_certificate(Fraction(2), Fraction(4), Fraction(9, 2))
    assert cert["alpha"] > 1
    assert cert["assumptions_hold"] is False
