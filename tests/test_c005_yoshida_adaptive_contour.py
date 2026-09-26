from __future__ import annotations

import mpmath as mp
import pytest

from secret_of_a_half.c005_yoshida_adaptive_contour import (
    adaptive_asymptotic_loglog,
    adaptive_contour_envelope,
    adaptive_parameters,
    c1_upper_general,
    c2_upper_general,
    general_contour_envelope,
)
from secret_of_a_half.c005_yoshida_high_mode import (
    c1_upper_c_eq_2_mp,
    c2_upper_c_eq_2_mp,
)


def test_general_c_recovers_c2_formula_at_c2() -> None:
    for a in [mp.mpf("0.1"),mp.mpf("1"),mp.mpf("2")]:
        assert c2_upper_general(a,2)==pytest.approx(
            float(c2_upper_c_eq_2_mp(a))
        )


def test_general_c1_recovers_five_six_at_c2() -> None:
    assert c1_upper_general(2)==mp.mpf(5)/6
    assert c1_upper_general(2)==c1_upper_c_eq_2_mp()


def test_adaptive_parameters_are_source_admissible() -> None:
    for a in [mp.mpf("0.5"),mp.mpf("1"),mp.mpf("3"),mp.mpf("10")]:
        c,a1=adaptive_parameters(a)
        assert c>1
        assert a1>a


def test_adaptive_loglog_tracks_two_a_law() -> None:
    residuals=[]
    for a0 in [3,4,5,6,8,10]:
        cert=adaptive_contour_envelope(a0)
        logN=mp.mpf(cert.log_required_continuous_cutoff)
        observed=mp.log(logN)
        model=adaptive_asymptotic_loglog(a0)
        residuals.append(observed-model)
    assert all(residuals[i+1]<residuals[i] for i in range(len(residuals)-1))
    assert residuals[-1]<mp.mpf("0.5")


def test_fail_closed_bad_contour() -> None:
    with pytest.raises(ValueError):
        general_contour_envelope(1,2,1,1)
