from __future__ import annotations

import mpmath as mp
import pytest

from secret_of_a_half.quotient_zero_set import quotient_F
from secret_of_a_half.reciprocal_paired_polynomial import (
    conjugation_closure_residual,
    evaluate_polynomial,
    expected_normalized_cardinality,
    monic_polynomial_coefficients,
    normalize_w_to_lambda,
    palindromic_coefficient_residual,
    real_coefficient_residual,
    reciprocal_closure_residual,
    reciprocal_lambda,
    reciprocal_pair_factor,
    self_reciprocal_identity_residual,
)


mp.mp.dps = 80


def _complex_closed_root_set(include_minus_one: bool) -> list[mp.mpc]:
    lam = mp.mpc("2.0", "1.0")
    roots = [lam, 1 / lam, mp.conj(lam), 1 / mp.conj(lam)]
    if include_minus_one:
        roots.append(mp.mpc(-1))
    return roots


def test_normalization_conjugates_J_to_reciprocal() -> None:
    w = mp.mpc("0.37", "0.19")
    lam = normalize_w_to_lambda(w)
    j_w = 1 / (16 * w)
    assert abs(normalize_w_to_lambda(j_w) - reciprocal_lambda(lam)) < mp.mpf("1e-70")


def test_reciprocal_and_conjugation_closure() -> None:
    roots = _complex_closed_root_set(False)
    assert reciprocal_closure_residual(roots) < mp.mpf("1e-70")
    assert conjugation_closure_residual(roots) < mp.mpf("1e-70")


def test_orbit_polynomial_is_real_palindromic_with_constant_one() -> None:
    roots = _complex_closed_root_set(False)
    coefficients = monic_polynomial_coefficients(roots)
    assert abs(coefficients[0] - 1) < mp.mpf("1e-70")
    assert abs(coefficients[-1] - 1) < mp.mpf("1e-70")
    assert palindromic_coefficient_residual(coefficients) < mp.mpf("1e-70")
    assert real_coefficient_residual(coefficients) < mp.mpf("1e-70")


def test_self_reciprocal_identity() -> None:
    coefficients = monic_polynomial_coefficients(_complex_closed_root_set(True))
    for x in (mp.mpc("0.7", "0.2"), mp.mpc("-1.3", "0.4"), mp.mpf(2)):
        assert self_reciprocal_identity_residual(coefficients, x) < mp.mpf("1e-68")


def test_minus_one_exception_controls_odd_degree_and_factor() -> None:
    without_exception = monic_polynomial_coefficients(_complex_closed_root_set(False))
    with_exception = monic_polynomial_coefficients(_complex_closed_root_set(True))

    assert (len(without_exception) - 1) % 2 == 0
    assert abs(evaluate_polynomial(without_exception, -1)) > mp.mpf("1e-6")

    assert (len(with_exception) - 1) % 2 == 1
    assert abs(evaluate_polynomial(with_exception, -1)) < mp.mpf("1e-70")


def test_plus_one_is_excluded_for_actual_F_by_positive_coefficients() -> None:
    assert abs(quotient_F(mp.mpf("0.25"))) > mp.mpf("0.1")


def test_pair_factor_has_unit_constant_and_palindromic_ends() -> None:
    factor = reciprocal_pair_factor(mp.mpc("2", "1"))
    assert factor[0] == 1
    assert factor[-1] == 1


def test_expected_cardinality_formula() -> None:
    for a in range(6):
        assert expected_normalized_cardinality(a, False) == 2 * a
        assert expected_normalized_cardinality(a, True) == 2 * a + 1


def test_fail_closed_inputs() -> None:
    with pytest.raises(ValueError):
        reciprocal_lambda(0)
    with pytest.raises(ValueError):
        reciprocal_pair_factor(0)
    with pytest.raises(ValueError):
        self_reciprocal_identity_residual((1, 1), 0)
    with pytest.raises(ValueError):
        expected_normalized_cardinality(-1, False)
