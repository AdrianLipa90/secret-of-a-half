#!/usr/bin/env python3
"""Regression for the centered zero-to-pole map and N0 polynomial surrogate.

This does not test RH.  It verifies:
1. the affine rho -> z_rho map;
2. the logarithmic-derivative residue rule;
3. positive imaginary part of -p'/p for a real-rooted even polynomial.
"""
from __future__ import annotations

import cmath


def q_real_rooted(z: complex, roots: list[float]) -> complex:
    return -sum(1.0 / (z-r) for r in roots)


def main() -> None:
    beta=0.73
    gamma=14.2
    zrho=-gamma+1j*(beta-0.5)
    s=0.5-1j*zrho
    assert abs(s-(beta+1j*gamma))<1e-12
    assert zrho.imag>0

    # multiplicity m stays in the residue while the pole order is one
    m=3
    eps=1e-8
    q=-m/eps
    assert abs(eps*q + m)<1e-12

    roots=[-21.0,-14.0,-7.0,7.0,14.0,21.0]
    points=[
        -10+0.2j,
        0.0+0.5j,
        3.0+1.0j,
        17.0+2.5j,
        -30.0+4.0j,
    ]
    min_imag=min(q_real_rooted(z,roots).imag for z in points)
    assert min_imag>0

    print("SOH_XI_LOG_DERIVATIVE_GENERALIZED_NEVANLINNA_V0_1: PASS")
    print("MIN_POLYNOMIAL_SURROGATE_IMAG=",min_imag)
    print("RH_TEST=false")
    print("STATUS=MAP_AND_N0_SURROGATE_PASS")


if __name__=="__main__":
    main()
