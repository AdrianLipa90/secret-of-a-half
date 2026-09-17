from __future__ import annotations

from fractions import Fraction

from secret_of_a_half.stieltjes_square_quotient import (
    alpha2_ratio_gate,
    determinant_2x2,
    first_s_fraction_coefficients,
    hankel_matrix,
    log_derivative_stieltjes_moments,
    normalized_gamma_ratios,
)


def test_log_derivative_moments_match_closed_forms() -> None:
    a0, a1, a2, a3 = map(Fraction, (2, 3, 5, 7))
    mu0, mu1, mu2 = log_derivative_stieltjes_moments(
        (a0, a1, a2, a3), order=2
    )
    assert mu0 == a1 / a0
    assert mu1 == a1 * a1 / (a0 * a0) - 2 * a2 / a0
    assert mu2 == (
        3 * a3 / a0
        - 3 * a1 * a2 / (a0 * a0)
        + a1**3 / a0**3
    )


def test_first_hankel_gate_equals_ratio_curvature_gate() -> None:
    a = tuple(map(Fraction, (7, 5, 3, 2)))
    mu = log_derivative_stieltjes_moments(a, order=2)
    d1 = determinant_2x2(hankel_matrix(mu, size=2))
    r1, r2, r3 = normalized_gamma_ratios(a, through=3)
    rhs = (r1 * r1 * r2 / 2) * (r1 - 2 * r2 + r3)
    assert d1 == rhs
    assert alpha2_ratio_gate(a) == r1 - 2 * r2 + r3


def test_s_fraction_alpha2_matches_ratio_formula() -> None:
    a = tuple(map(Fraction, (5, 4, 1, 1)))
    alpha0, alpha1, alpha2 = first_s_fraction_coefficients(a)
    r1, r2, r3 = normalized_gamma_ratios(a, through=3)
    assert alpha0 == r1
    assert alpha1 == r1 - r2
    assert alpha2 == r2 * (r1 - 2 * r2 + r3) / (2 * (r1 - r2))


def test_negative_real_root_fixture_is_stieltjes() -> None:
    # F(w)=(1+w)(1+2w)(1+3w)
    # F'/F = 1/(1+w)+2/(1+2w)+3/(1+3w), hence
    # mu_n = 1^(n+1)+2^(n+1)+3^(n+1).
    a = (
        Fraction(1),
        Fraction(6),
        Fraction(11),
        Fraction(6),
    )
    mu = log_derivative_stieltjes_moments(a, order=2)
    expected = tuple(
        Fraction(1 ** (n + 1) + 2 ** (n + 1) + 3 ** (n + 1))
        for n in range(3)
    )
    assert mu == expected
    assert determinant_2x2(hankel_matrix(mu, size=2)) > 0
    alpha0, alpha1, alpha2 = first_s_fraction_coefficients(a)
    assert alpha0 > 0
    assert alpha1 > 0
    assert alpha2 > 0
