#!/usr/bin/env python3
"""Finite-dimensional regression for the semibounded resolvent first correction."""
from __future__ import annotations

import numpy as np


def main() -> None:
    rng = np.random.default_rng(20260926)
    max_last_error = 0.0
    cases = 0

    for n in [2, 4, 8]:
        for _ in range(100):
            x = rng.normal(size=(n, n))
            A = 0.5 * (x + x.T)

            f = rng.normal(size=n)
            g = rng.normal(size=n)

            q = float(f @ A @ g)
            inner = float(f @ g)

            eigen_min = float(np.min(np.linalg.eigvalsh(A)))
            mus = [
                max(100.0, -eigen_min + 100.0),
                max(1_000.0, -eigen_min + 1_000.0),
                max(10_000.0, -eigen_min + 10_000.0),
            ]

            errors = []
            for mu in mus:
                Rg = np.linalg.solve(A + mu * np.eye(n), g)
                first = -mu * mu * (float(f @ Rg) - inner / mu)
                errors.append(abs(first - q))

            assert errors[-1] <= errors[0] + 1e-10
            max_last_error = max(max_last_error, errors[-1])
            cases += 1

    print("SOH_NEGATIVE_SHIFT_RESOLVENT_WEIL_FIRST_CORRECTION_V0_1: PASS")
    print("CASES=", cases)
    print("MAX_ERROR_AT_MU_10000_SCALE=", max_last_error)
    print("FINITE_DIMENSIONAL_REGRESSION_ONLY=true")
    print("STATUS=FIRST_CORRECTION_PASS")


if __name__ == "__main__":
    main()
