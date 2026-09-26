#!/usr/bin/env python3
"""Algebra regression for the fixed-signature midpoint/secant jet frame."""
from __future__ import annotations

import numpy as np


def main() -> None:
    rng=np.random.default_rng(20260926)
    max_metric_error=0.0
    max_frame_error=0.0

    J=np.diag([1.0,-1.0])
    F=np.array([[0.0,1.0],[1.0,0.0]])

    for t in [1e-3,0.05,0.2,0.8,2.0]:
        R=np.array([[1.0,1.0],[0.0,-t]])
        G=R@J@R.T
        expected=t*np.array([[0.0,1.0],[1.0,-t]])
        max_metric_error=max(
            max_metric_error,
            float(np.linalg.norm(G-expected,2)),
        )

        S=np.array([[1.0,0.0],[-t/2.0,1.0]])
        max_metric_error=max(
            max_metric_error,
            float(np.linalg.norm(S@F@S.T-expected/t,2)),
        )

        for _ in range(50):
            e0=rng.normal(size=2)+1j*rng.normal(size=2)
            et=rng.normal(size=2)+1j*rng.normal(size=2)
            E=np.column_stack([e0,et])

            h=(e0-et)/t
            B=np.column_stack([e0,h])
            midpoint=(e0+et)/2.0
            Ehat=np.column_stack([midpoint,h])

            max_frame_error=max(
                max_frame_error,
                float(np.linalg.norm(E-B@R,2)),
                float(np.linalg.norm(Ehat-B@S,2)),
            )

            lhs=E@J@E.conj().T/t
            rhs=Ehat@F@Ehat.conj().T
            assert np.linalg.norm(lhs-rhs,2)<2e-10

    assert max_metric_error<2e-14
    assert max_frame_error<2e-12

    print("SOH_MINIMAL_FOUR_CHANNEL_J_JET_V0_1: PASS")
    print("MAX_METRIC_ERROR=",max_metric_error)
    print("MAX_FRAME_ERROR=",max_frame_error)
    print("STATUS=FIXED_SIGNATURE_JET_IDENTITY")


if __name__=="__main__":
    main()
