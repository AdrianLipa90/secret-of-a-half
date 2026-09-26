from __future__ import annotations

from secret_of_a_half.localized_weil_cross_form_interval import (
    displacement_determinant_interval,
    interval_excludes_zero,
)


POINTS=[
    ("0.2","0.7"),
    ("-0.6","0.9"),
    ("1.1","0.5"),
]


def test_rank_three_interval_certificate_excludes_zero():
    det=displacement_determinant_interval(
        "0.6",
        POINTS,
        K=500,
        tail_order=4,
    )
    assert interval_excludes_zero(det)
    assert det.real.a > 0


def test_independent_series_truncations_are_consistent_and_nonzero():
    det300=displacement_determinant_interval(
        "0.6",POINTS,K=300,tail_order=4
    )
    det500=displacement_determinant_interval(
        "0.6",POINTS,K=500,tail_order=4
    )
    assert interval_excludes_zero(det300)
    assert interval_excludes_zero(det500)
    assert det300.real.a > 0
    assert det500.real.a > 0
