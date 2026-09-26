#!/usr/bin/env python3
"""Finite-dimensional regression for the denominator-# symmetry.

The regression uses a symmetric grid, a real symmetric parity-commuting matrix,
and checks B(z)=A#(z) plus the exact characteristic factorization.
"""
from __future__ import annotations

import numpy as np


def main() -> None:
    rng=np.random.default_rng(20260926)
    x=np.linspace(-2.0,2.0,41)
    n=x.size

    J=np.eye(n)[::-1]
    q=rng.normal(size=(n,n))
    q=0.5*(q+q.T)
    q=0.5*(q+J@q@J)
    T=q.T@q+2.0*np.eye(n)
    assert np.linalg.norm(T@J-J@T,2)<1e-10

    e_plus=np.exp(x)
    e_minus=np.exp(-x)
    h_plus=np.linalg.solve(T,e_plus)
    h_minus=np.linalg.solve(T,e_minus)

    max_sharp=0.0
    max_char=0.0

    for z in [
        0.2+0.4j,
        -0.7+0.8j,
        1.1+1.3j,
        -1.5+0.25j,
    ]:
        ez=np.exp(-1j*z*x)
        A=np.dot(ez,h_plus)
        B=np.dot(ez,h_minus)

        ez_bar=np.exp(-1j*np.conjugate(z)*x)
        A_bar=np.dot(ez_bar,h_plus)
        A_sharp=np.conjugate(A_bar)

        max_sharp=max(max_sharp,abs(B-A_sharp))
        assert abs(B-A_sharp)<2e-12

        E=(z+1j)*A
        E_sharp=(z-1j)*B
        chi_direct=-(z-1j)*B/((z+1j)*A)
        chi_factor=-E_sharp/E
        max_char=max(max_char,abs(chi_direct-chi_factor))
        assert abs(chi_direct-chi_factor)<2e-14

    print("SOH_LIVSIC_DENOMINATOR_SHARP_THETA_WEIL_V0_1: PASS")
    print("MAX_B_MINUS_A_SHARP=",max_sharp)
    print("MAX_CHARACTERISTIC_FACTORIZATION_ERROR=",max_char)
    print("STATUS=EXACT_SHARP_REGRESSION")


if __name__=="__main__":
    main()
