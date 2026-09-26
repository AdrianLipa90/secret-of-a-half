"""Localized exponential Weil cross-form evaluator.

This module evaluates
    Q_W^a(v_z, v_w) = W(v_z * tilde(v_w))
for
    v_z(x)=exp(-i z x) 1_{[-a,a]}(x),
directly from Suzuki's explicit Weil functional.

Important:
- the cross-convolution formula is exact;
- prime support is finite: n <= exp(2a);
- the current integral evaluation uses high-precision mpmath quadrature and is
  diagnostic, not interval arithmetic;
- therefore nonzero determinant/rank witnesses produced by this module are
  NUMERICAL until a separate enclosure layer certifies them.
"""
from __future__ import annotations

import mpmath as mp

from .phasenav_weil_hermite_arithmetic import prime_power_terms


mp.mp.dps=max(mp.mp.dps,80)


def localized_cross_convolution(t,a,z,w):
    aa=mp.mpf(a)
    tt=mp.mpf(t)
    zz=mp.mpc(z)
    ww=mp.mpc(w)
    if aa<=0:
        raise ValueError("a must be positive")
    if abs(tt)>2*aa:
        return mp.mpc(0)
    alpha=1j*(mp.conj(ww)-zz)
    phase=mp.e**(-1j*mp.conj(ww)*tt)
    if abs(alpha)<mp.mpf("1e-50"):
        return phase*(2*aa-abs(tt))
    if tt>=0:
        return phase*(mp.e**(alpha*aa)-mp.e**(alpha*(tt-aa)))/alpha
    return phase*(mp.e**(alpha*(tt+aa))-mp.e**(-alpha*aa))/alpha


def localized_overlap(a,z,w):
    return localized_cross_convolution(0,a,z,w)


def _regularization_kernel(t):
    tt=mp.mpf(t)
    return mp.e**(tt/2)/(mp.e**tt-mp.e**(-tt))


def localized_weil_cross_form(
    a,z,w,*,max_support=2_000_000,near_zero_eps="1e-8"
):
    aa=mp.mpf(a)
    if aa<=0:
        raise ValueError("a must be positive")
    T=2*aa
    f0=localized_cross_convolution(0,aa,z,w)

    elementary=mp.quad(
        lambda t:
            localized_cross_convolution(t,aa,z,w)
            *(mp.e**(t/2)+mp.e**(-t/2)),
        [-T,0,T],
    )

    cutoff=int(mp.floor(mp.e**T))
    if cutoff>max_support:
        raise ValueError(
            f"prime support exp(2a)={cutoff} exceeds max_support={max_support}"
        )

    prime=mp.mpc(0)
    for n,logp in prime_power_terms(cutoff):
        ln=mp.log(n)
        prime -= (
            mp.mpf(str(logp))/mp.sqrt(n)
            *(
                localized_cross_convolution(ln,aa,z,w)
                +localized_cross_convolution(-ln,aa,z,w)
            )
        )

    constant=-(mp.log(4*mp.pi)+mp.euler)*f0

    eps=mp.mpf(near_zero_eps)
    if not 0<eps<T:
        raise ValueError("near_zero_eps must lie in (0,2a)")

    def reg_integrand(t):
        tt=mp.mpf(t)
        bracket=(
            localized_cross_convolution(tt,aa,z,w)
            +localized_cross_convolution(-tt,aa,z,w)
            -2*f0*mp.e**(-tt/2)
        )
        return bracket*_regularization_kernel(tt)

    near=reg_integrand(eps/2)*eps
    regularization_core=near+mp.quad(reg_integrand,[eps,T])

    regularization_tail=-2*f0*mp.atanh(mp.e**(-T))

    return elementary+prime+constant-(regularization_core+regularization_tail)


def displacement_matrix(a,points,**kwargs):
    pts=[mp.mpc(z) for z in points]
    m=mp.matrix(len(pts))
    for j,z in enumerate(pts):
        for k,w in enumerate(pts):
            q=localized_weil_cross_form(a,z,w,**kwargs)
            m[j,k]=2j*(mp.conj(w)-z)*q
    return m


def displacement_determinant(a,points,**kwargs):
    return mp.det(displacement_matrix(a,points,**kwargs))
