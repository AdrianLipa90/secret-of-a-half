from __future__ import annotations

from secret_of_a_half.localized_weil_rank_interval import (
    certified_rank_witness,
    determinant_3x3,
    displacement_matrix,
)


def test_prime_free_interval_matrix_is_symmetric():
    M = displacement_matrix()
    for j in range(3):
        for k in range(3):
            # Intervals overlap pairwise; exact symmetry is analytic.
            assert not (M[j][k] < M[k][j])
            assert not (M[j][k] > M[k][j])


def test_certified_determinant_excludes_zero():
    M = displacement_matrix()
    det = determinant_3x3(M)
    assert det > 0


def test_receipt_reports_rank_at_least_three():
    receipt = certified_rank_witness()
    assert receipt["prime_free"] is True
    assert receipt["rank_lower_bound"] == 3
