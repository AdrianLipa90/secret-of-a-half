from __future__ import annotations

import mpmath as mp

from secret_of_a_half.localized_weil_cross_form import (
    displacement_determinant,
    localized_cross_convolution,
    localized_weil_cross_form,
)


mp.mp.dps=70


def _direct_cross(t,a,z,w):
    lo=max(-a,t-a)
    hi=min(a,t+a)
    if lo>hi:
        return mp.mpc(0)
    return mp.quad(
        lambda u:
            mp.e**(-1j*z*u)
            *mp.e**(1j*mp.conj(w)*(u-t)),
        [lo,hi],
    )


def test_closed_cross_convolution_matches_direct_integral():
    a=mp.mpf("0.8")
    z=mp.mpc("0.2","0.7")
    w=mp.mpc("-0.4","0.9")
    for t in [
        mp.mpf("-1.2"),
        mp.mpf("-0.3"),
        mp.mpf("0"),
        mp.mpf("0.4"),
        mp.mpf("1.3"),
    ]:
        got=localized_cross_convolution(t,a,z,w)
        expected=_direct_cross(t,a,z,w)
        assert abs(got-expected)<mp.mpf("1e-55")


def test_cross_form_is_hermitian_to_high_precision():
    a=mp.mpf("0.6")
    z=mp.mpc("0.2","0.7")
    w=mp.mpc("-0.6","0.9")
    qzw=localized_weil_cross_form(a,z,w)
    qwz=localized_weil_cross_form(a,w,z)
    assert abs(qzw-mp.conj(qwz))<mp.mpf("1e-45")


def test_scalar_rank_collapse_has_strong_numerical_counter_witness():
    points=[
        mp.mpc("0.2","0.7"),
        mp.mpc("-0.6","0.9"),
        mp.mpc("1.1","0.5"),
    ]
    det06=displacement_determinant(mp.mpf("0.6"),points)
    det10=displacement_determinant(mp.mpf("1.0"),points)
    assert abs(det06)>mp.mpf("1e-4")
    assert abs(det10)>mp.mpf("1e-4")
