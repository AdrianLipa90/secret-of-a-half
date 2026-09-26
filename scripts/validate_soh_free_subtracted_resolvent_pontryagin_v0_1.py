#!/usr/bin/env python3
"""Finite-dimensional regression for sign preservation and negative index."""
from __future__ import annotations

import numpy as np


def inertia_negative(a: np.ndarray, tol: float = 1e-10) -> int:
    return int(np.sum(np.linalg.eigvalsh(a) < -tol))


def main() -> None:
    rng=np.random.default_rng(20260926)
    cases=0
    for n in [3,5,8,12]:
        for _ in range(100):
            q,_=np.linalg.qr(rng.normal(size=(n,n)))
            eig=rng.uniform(-4.0,6.0,size=n)
            # Avoid accidental near-zero ambiguity.
            eig[np.abs(eig)<0.25]+=np.where(eig[np.abs(eig)<0.25]>=0,0.5,-0.5)
            A=q@np.diag(eig)@q.T
            lam_min=float(np.min(eig))
            mu=max(1.0,-lam_min+0.75)

            C=A@np.linalg.inv(A+mu*np.eye(n))
            assert inertia_negative(C)==inertia_negative(A)

            ceig=np.linalg.eigvalsh(C)
            for la,lc in zip(np.sort(eig),np.sort(ceig)):
                # The scalar spectral map is strictly increasing on (-mu,infinity).
                expected=la/(la+mu)
                assert abs(lc-expected)<2e-10
                if abs(la)>1e-10:
                    assert np.sign(lc)==np.sign(la)
            cases+=1

    print("SOH_FREE_SUBTRACTED_RESOLVENT_PONTRYAGIN_FRONTIER_V0_1: PASS")
    print("CASES=",cases)
    print("STATUS=INERTIA_PRESERVED")


if __name__=="__main__":
    main()
