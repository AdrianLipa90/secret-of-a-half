#!/usr/bin/env python3
"""Regression for the quantitative operator-domain first-correction bound."""
from __future__ import annotations

import numpy as np


def first_correction(T: np.ndarray, f: np.ndarray, g: np.ndarray, mu: float) -> float:
    Rg = np.linalg.solve(T + mu * np.eye(T.shape[0]), g)
    return -mu * mu * (float(f @ Rg) - float(f @ g) / mu)


def main() -> None:
    rng = np.random.default_rng(20260926)
    max_ratio = 0.0
    cases = 0

    for n in [2, 4, 8, 12]:
        for _ in range(250):
            q = rng.normal(size=(n, n))
            T = q.T @ q + np.eye(n)  # T >= I
            f = rng.normal(size=n)
            g = rng.normal(size=n)

            target = float(f @ T @ g)
            Tf = T @ f
            Tg = T @ g

            for mu in [1.0, 10.0, 100.0, 1000.0]:
                observed = abs(first_correction(T, f, g, mu) - target)
                bound = np.linalg.norm(Tf) * np.linalg.norm(Tg) / (mu + 1.0)
                assert observed <= bound + 2e-10
                if bound > 0:
                    max_ratio = max(max_ratio, observed / bound)
                cases += 1

    print("SOH_QUANTITATIVE_OPERATOR_DOMAIN_RESOLVENT_RATE_V0_1: PASS")
    print("CASES=", cases)
    print("MAX_OBSERVED_TO_BOUND_RATIO=", max_ratio)
    print("RH_USED=false")
    print("ZERO_LIST_USED=false")
    print("STATUS=EFFECTIVE_OPERATOR_DOMAIN_RATE_CLOSED")


if __name__ == "__main__":
    main()
