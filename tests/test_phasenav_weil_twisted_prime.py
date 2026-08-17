from __future__ import annotations

import cmath
import math

from secret_of_a_half.phasenav_weil_twisted_prime import (
    cancellation_ratio,
    cumulative_twisted_prime_sum,
    direct_weighted_sum,
    finite_summation_by_parts,
    twisted_prime_terms,
)


def test_twisted_terms_are_strictly_ordered_and_finite() -> None:
    terms = twisted_prime_terms(500, 14.134725141734695)
    assert terms
    assert all(terms[j].n < terms[j + 1].n for j in range(len(terms) - 1))
    assert all(math.isfinite(term.weight.real) and math.isfinite(term.weight.imag) for term in terms)


def test_cumulative_sum_matches_explicit_sum() -> None:
    target = 14.134725141734695
    terms = twisted_prime_terms(2000, target)
    expected = sum((term.weight for term in terms), 0j)
    actual = cumulative_twisted_prime_sum(2000, target)
    assert abs(actual - expected) < 1e-12


def test_discrete_summation_by_parts_matches_direct_weighted_sum() -> None:
    target = 14.134725141734695
    terms = twisted_prime_terms(5000, target)

    def kernel(n: int) -> complex:
        u = math.log(n)
        return cmath.exp(-0.013 * u * u) * (1.0 + 0.07j * u)

    direct = direct_weighted_sum(terms, kernel)
    abel = finite_summation_by_parts(terms, kernel)
    scale = max(1.0, abs(direct), abs(abel))
    assert abs(direct - abel) / scale < 1e-12


def test_cancellation_ratio_is_bounded() -> None:
    for cutoff in (100, 1000, 10000):
        ratio = cancellation_ratio(cutoff, 14.134725141734695)
        assert 0.0 <= ratio <= 1.0 + 1e-12
