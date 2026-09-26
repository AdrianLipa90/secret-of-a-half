#!/usr/bin/env python3
"""Regression for the Cayley xi-target algebra.

Numerical values are implementation checks only.  No RH test is performed.
"""
from __future__ import annotations

import mpmath as mp


mp.mp.dps=60


def xi(s):
    return (
        mp.mpf("0.5")
        * s*(s-1)
        * mp.pi**(-s/2)
        * mp.gamma(s/2)
        * mp.zeta(s)
    )


def main() -> None:
    A=xi(mp.mpf("1.5"))
    B=mp.diff(xi,mp.mpf("1.5"))
    assert A>0
    assert B>0

    for z in [
        mp.mpc("0.2","0.8"),
        mp.mpc("-1.1","1.2"),
        mp.mpc("2.0","0.7"),
    ]:
        s=mp.mpf("0.5")-1j*z
        f=xi(s)
        fp=-1j*mp.diff(xi,s)
        D=B*f+1j*A*fp
        N=B*f-1j*A*fp
        chi=N/D
        cayley=1j*(1-chi)/(1+chi)
        qxi=-fp/f
        assert abs(cayley-(A/B)*qxi)<mp.mpf("1e-45")

    print("SOH_GENERALIZED_SCHUR_XI_NEVANLINNA_CAYLEY_V0_1: PASS")
    print("A=",mp.nstr(A,30))
    print("B=",mp.nstr(B,30))
    print("A_OVER_B=",mp.nstr(A/B,30))
    print("RH_TEST=false")
    print("STATUS=CAYLEY_TARGET_PASS")


if __name__=="__main__":
    main()
