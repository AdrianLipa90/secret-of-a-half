#!/usr/bin/env python3
"""Independent screw-kernel versus explicit-Weil localized modal cross-check.

For normalized Dirichlet modes
    phi_n(x)=a^(-1/2) sin(n*pi*(x+a)/(2a))
on [-a,a], compare:

1. screw side:
   Q_n = 2[-g'(2a) + integral_0^(2a) g''(t) F_n(t) dt],
   obtained by integrating the derivative autocorrelation twice by parts;

2. arithmetic side:
   the same mode expanded into the two exponential frequencies +/-k_n and
   evaluated with the localized explicit-Weil cross-form module.

At a=0.345 the prime support is empty.  This is a high-precision normalization
cross-check, not interval arithmetic and not an RH test.
"""
from __future__ import annotations

import mpmath as mp

from secret_of_a_half.localized_weil_cross_form import (
    localized_weil_cross_form,
)


mp.mp.dps=max(mp.mp.dps,40)


A=mp.mpf("0.345")
T=2*A
GAMMA_TERM=mp.digamma(mp.mpf("0.25"))-mp.log(mp.pi)


def g_prime_prime_free(t):
    """g'(t) for 0<t<=2a below the first prime threshold."""
    t=mp.mpf(t)
    q=mp.e**(-2*t)
    psi_prime=(
        2*(mp.e**(t/2)-mp.e**(-t/2))
        +GAMMA_TERM/2
        +mp.e**(-t/2)*mp.lerchphi(q,1,mp.mpf("0.25"))/2
    )
    return -psi_prime


def g_second_prime_free(t):
    """g''(t), evaluated stably for t>0."""
    t=mp.mpf(t)
    if t<=0:
        raise ValueError("g_second_prime_free requires t>0")
    return (
        -2*mp.cosh(t/2)
        +mp.e**(-t/2)/(-mp.expm1(-2*t))
    )


def second_primitive_F(t,n):
    """F_n'' equals the derivative autocorrelation C_n.

    Boundary data:
        F_n(0)=F_n'(0)=0,
        F_n(2a)=1,
        F_n'(2a)=0.
    """
    t=mp.mpf(t)
    k=mp.pi*n/(2*A)
    return (
        1
        +(t-T)/T*mp.cos(k*t)
        -mp.sin(k*t)/(T*k)
    )


def screw_quadratic_diag(n):
    k=mp.pi*n/(2*A)

    def integrand(t):
        t=mp.mpf(t)
        # g''~1/(2t), F_n~k^2 t^2/2, so the product tends to 0.
        if abs(t)<mp.mpf("1e-18"):
            return k*k*t/4
        return g_second_prime_free(t)*second_primitive_F(t,n)

    cuts=[
        mp.mpf("0"),
        T*mp.mpf("1e-6"),
        T*mp.mpf("1e-5"),
        T*mp.mpf("1e-4"),
        T*mp.mpf("1e-3"),
        T*mp.mpf("1e-2"),
        T*mp.mpf("0.1"),
        T,
    ]
    integral=mp.quad(integrand,cuts)
    return 2*(-g_prime_prime_free(T)+integral)


def arithmetic_quadratic_diag(n):
    k=mp.pi*n/(2*A)
    coeff=[
        (-k, mp.e**(1j*k*A)/(2j*mp.sqrt(A))),
        ( k,-mp.e**(-1j*k*A)/(2j*mp.sqrt(A))),
    ]
    out=mp.mpc(0)
    for z,c in coeff:
        for w,d in coeff:
            out += (
                c*mp.conj(d)
                *localized_weil_cross_form(
                    A,z,w,near_zero_eps="2e-8"
                )
            )
    return out


def main():
    expected={
        1:mp.mpf("0.00262569081058866498516318025485"),
        2:mp.mpf("0.157045650889994298960677934719"),
        3:mp.mpf("0.700976786436366215066158696726"),
    }

    max_error=mp.mpf("0")
    for n in [1,2,3]:
        q_screw=screw_quadratic_diag(n)
        q_weil=arithmetic_quadratic_diag(n)
        error=abs(q_screw-q_weil)
        max_error=max(max_error,error)

        assert error<mp.mpf("1e-28")
        assert abs(q_screw-expected[n])<mp.mpf("1e-28")

        print(
            "MODE",n,
            "Q_SCREW=",mp.nstr(q_screw,32),
            "Q_WEIL=",mp.nstr(q_weil,32),
            "ABS_ERROR=",mp.nstr(error,10),
        )

    print("SOH_LOCALIZED_SCREW_WEIL_CROSSCHECK_V0_2: PASS")
    print("MAX_ERROR=",mp.nstr(max_error,12))
    print("INTERVAL_PROOF=false")
    print("RH_USED=false")
    print("STATUS=THREE_MODE_NUMERICAL_SOURCE_NORMALIZATION_CROSSCHECK")


if __name__=="__main__":
    main()
