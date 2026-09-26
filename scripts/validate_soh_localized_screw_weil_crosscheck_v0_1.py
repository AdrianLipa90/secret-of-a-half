#!/usr/bin/env python3
"""Independent screw-kernel versus explicit-Weil localized cross-check.

The test uses the first normalized Dirichlet mode on [-a,a]:
    phi_1(x)=a^(-1/2) sin(pi(x+a)/(2a)).

Two independent implementations are compared:
1. Q=<G D phi,D phi> using the source-normalized screw function g;
2. Q=W(phi * tilde(phi)) assembled from the localized exponential Weil
   cross-form evaluator.

The sample a=0.345 lies below the first prime threshold, which makes the
normalization cross-check especially clean.
"""
from __future__ import annotations

import mpmath as mp

from secret_of_a_half.localized_weil_cross_form import (
    localized_weil_cross_form,
)
from secret_of_a_half.zeta_screw import zeta_screw_g


mp.mp.dps=max(mp.mp.dps,30)


def derivative_correlation_diag(a,n,t):
    """Integral phi_n'(x) phi_n'(x+t) dx for t in [0,2a]."""
    aa=mp.mpf(a)
    tt=mp.mpf(t)
    k=mp.pi*n/(2*aa)
    return (
        k*k/(2*aa)
        *((2*aa-tt)*mp.cos(k*tt)-mp.sin(k*tt)/k)
    )


def screw_quadratic_diag(a,n=1):
    aa=mp.mpf(a)
    T=2*aa

    def integrand(t):
        return (
            2
            *zeta_screw_g(t)
            *derivative_correlation_diag(aa,n,t)
        )

    # Resolve the logarithmic endpoint structure explicitly.
    cuts=[
        mp.mpf("0"),
        T*mp.mpf("1e-5"),
        T*mp.mpf("1e-4"),
        T*mp.mpf("1e-3"),
        T*mp.mpf("1e-2"),
        T*mp.mpf("0.1"),
        T,
    ]
    return mp.quad(integrand,cuts)


def arithmetic_quadratic_diag(a,n=1):
    aa=mp.mpf(a)
    k=mp.pi*n/(2*aa)

    # phi_n = c_- v_{-k} + c_+ v_{+k}
    coeff=[
        (-k, mp.e**(1j*k*aa)/(2j*mp.sqrt(aa))),
        ( k,-mp.e**(-1j*k*aa)/(2j*mp.sqrt(aa))),
    ]

    out=mp.mpc(0)
    for z,c in coeff:
        for w,d in coeff:
            out += (
                c*mp.conj(d)
                *localized_weil_cross_form(
                    aa,z,w,near_zero_eps="2e-7"
                )
            )
    return out


def main():
    a=mp.mpf("0.345")
    q_screw=screw_quadratic_diag(a,1)
    q_weil=arithmetic_quadratic_diag(a,1)
    error=abs(q_screw-q_weil)

    assert error < mp.mpf("1e-18")

    print("SOH_LOCALIZED_SCREW_WEIL_CROSSCHECK_V0_1: PASS")
    print("A=",mp.nstr(a,20))
    print("Q_SCREW=",mp.nstr(q_screw,30))
    print("Q_WEIL=",mp.nstr(q_weil,30))
    print("ABS_ERROR=",mp.nstr(error,15))
    print("INTERVAL_PROOF=false")
    print("STATUS=NUMERICAL_SOURCE_NORMALIZATION_CROSSCHECK")


if __name__=="__main__":
    main()
