from __future__ import annotations

import math

from secret_of_a_half.c005_infinite_complement import cutoff_for_window, schedule_receipt
from secret_of_a_half.phasenav_weil_prime_tail_program import monotonicity_margin


def test_schedule_certifies_every_degree_in_window() -> None:
    width = 1.0
    for window_stop in range(1, 33):
        item = cutoff_for_window(window_stop, width)
        assert item.max_degree == 2 * (window_stop - 1)
        assert monotonicity_margin(item.max_degree, item.cutoff, width) >= 0.0
        for degree in range(item.max_degree + 1):
            assert monotonicity_margin(degree, item.cutoff, width) >= 0.0


def test_schedule_is_monotone_and_subexponential_in_window_index() -> None:
    width = 1.0
    cutoffs = [cutoff_for_window(m, width).cutoff for m in range(1, 65)]
    assert cutoffs == sorted(cutoffs)
    # log Q_M = O(sqrt(M)) from the closed threshold formula.
    ratios = [math.log(q) / math.sqrt(m) for m, q in enumerate(cutoffs, start=1)]
    assert max(ratios) < 4.0


def test_receipt_keeps_convergence_and_rh_open() -> None:
    receipt = schedule_receipt(32, 1.0)
    assert receipt["status"] == "PASS_VALIDITY_ONLY"
    assert receipt["all_integral_test_bounds_valid"] is True
    assert receipt["cutoff_schedule_monotone"] is True
    boundary = receipt["claim_boundary"]
    assert boundary["proof_of_convergence"] is False
    assert boundary["proof_of_rh"] is False
    assert "SOH-C005" in boundary["open"]
