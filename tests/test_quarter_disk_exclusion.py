from __future__ import annotations

import mpmath as mp
import pytest

from secret_of_a_half.quarter_disk_exclusion import (
    direct_f0,
    direct_f_quarter,
    eta_half_four_term_lower,
    exact_radical_checks,
    f0_elementary_lower_bound,
    paired_modulus_contradiction,
    quarter_disk_lower_margin,
    quotient_image_modulus,
)
from secret_of_a_half.quotient_zero_set import quotient_F


def test_eta_four_term_bound_is_positive() -> None:
    mp.mp.dps = 80
    assert eta_half_four_term_lower() > 0


def test_elementary_f0_lower_bound_exceeds_quarter() -> None:
    mp.mp.dps = 80
    assert all(exact_radical_checks().values())
    assert f0_elementary_lower_bound() > mp.mpf("0.25")
    assert quarter_disk_lower_margin() > 0


def test_direct_f0_respects_analytic_lower_bound() -> None:
    mp.mp.dps = 80
    value = direct_f0()
    assert abs(mp.im(value)) < mp.mpf("1e-60")
    assert mp.re(value) > f0_elementary_lower_bound()


def test_f_quarter_is_exactly_one_half_numerically() -> None:
    mp.mp.dps = 80
    assert abs(direct_f_quarter() - mp.mpf("0.5")) < mp.mpf("1e-70")


@pytest.mark.parametrize(
    "w",
    [
        mp.mpf("0"),
        mp.mpf("0.25"),
        mp.mpf("-0.25"),
        mp.mpc("0.1", "0.2"),
        mp.mpc("-0.17", "0.11"),
    ],
)
def test_sampled_closed_quarter_disk_respects_certified_margin(w: mp.mpc) -> None:
    mp.mp.dps = 70
    assert abs(w) <= mp.mpf("0.25")
    assert abs(quotient_F(w)) > quarter_disk_lower_margin()


@pytest.mark.parametrize("radius", ["0.01", "0.249", "0.25", "0.251", "1", "10"])
def test_source_and_image_cannot_both_lie_outside_quarter_disk(radius: str) -> None:
    assert paired_modulus_contradiction(mp.mpf(radius))


def test_j_modulus_formula() -> None:
    mp.mp.dps = 60
    r = mp.mpf("3.75")
    assert quotient_image_modulus(r) == 1 / (16 * r)
