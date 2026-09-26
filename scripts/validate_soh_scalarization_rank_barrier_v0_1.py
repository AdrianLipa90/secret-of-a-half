#!/usr/bin/env python3
"""Generic rank-4 witness: difference of two rank-2 de Branges-type numerators.

This is a structural regression only. It does not evaluate the actual Suzuki
operator pair.
"""
from __future__ import annotations

import numpy as np


def main() -> None:
    pts=np.array([
        0.2+0.4j,
        -0.7+0.8j,
        1.1+0.3j,
        -1.4+1.2j,
    ],dtype=complex)

    # Four independent analytic feature columns on the sample.
    F=np.column_stack([
        np.ones_like(pts),
        pts,
        pts**2,
        np.exp(0.37*pts),
    ])
    J=np.diag([1.0,-1.0,-1.0,1.0])
    M=F@J@F.conj().T

    rank=np.linalg.matrix_rank(M,tol=1e-10)
    assert rank==4

    # A scalar Schur numerator 1-s(z)s(w)* has rank <=2.
    s=0.2+0.1*pts
    scalar=np.ones((len(pts),len(pts)),dtype=complex)-np.outer(s,s.conj())
    scalar_rank=np.linalg.matrix_rank(scalar,tol=1e-10)
    assert scalar_rank<=2

    print("SOH_SCALARIZATION_RANK_BARRIER_V0_1: PASS")
    print("GENERIC_FOUR_CHANNEL_RANK=",rank)
    print("SCALAR_SCHUR_NUMERATOR_RANK=",scalar_rank)
    print("ACTUAL_SUZUKI_RANK_TEST=false")
    print("STATUS=AUTOMATIC_SCALARIZATION_NO_GO")


if __name__=="__main__":
    main()
