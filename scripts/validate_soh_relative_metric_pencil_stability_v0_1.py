#!/usr/bin/env python3
"""Monte Carlo regression for the relative-metric pencil bound."""
from __future__ import annotations

import numpy as np


def invsqrt(a: np.ndarray) -> np.ndarray:
    w, v = np.linalg.eigh(a)
    if np.min(w) <= 0.0:
        raise ValueError("positive definite matrix required")
    return (v * (w ** -0.5)) @ v.T


def sqrtm(a: np.ndarray) -> np.ndarray:
    w, v = np.linalg.eigh(a)
    if np.min(w) <= 0.0:
        raise ValueError("positive definite matrix required")
    return (v * (w ** 0.5)) @ v.T


def certificate(K0, G0, K, G):
    G0m = invsqrt(G0)
    A0 = G0m @ K0 @ G0m
    E = G0m @ (G - G0) @ G0m
    dG = np.linalg.norm(E, 2)
    if not dG < 1.0:
        raise ValueError("relative metric distortion must be < 1")
    dK = np.linalg.norm(G0m @ (K - K0) @ G0m, 2)
    bound = (dK + dG * np.linalg.norm(A0, 2)) / (1.0 - dG)

    Gm = invsqrt(G)
    A = Gm @ K @ Gm
    e0 = np.linalg.eigvalsh(A0)
    e1 = np.linalg.eigvalsh(A)
    observed = float(np.max(np.abs(e1 - e0)))
    return dG, dK, bound, observed


def main():
    rng = np.random.default_rng(20260926)
    max_ratio = 0.0
    cases = 0

    for n in [2, 3, 5, 8]:
        for _ in range(250):
            q = rng.normal(size=(n, n))
            G0 = q.T @ q + np.eye(n)

            a = rng.normal(size=(n, n))
            K0 = 0.5 * (a + a.T)

            Ghalf = sqrtm(G0)

            e = rng.normal(size=(n, n))
            e = 0.5 * (e + e.T)
            e /= np.linalg.norm(e, 2)
            e *= rng.uniform(0.0, 0.75)
            G = G0 + Ghalf @ e @ Ghalf

            dk = rng.normal(size=(n, n))
            dk = 0.5 * (dk + dk.T)
            dk /= np.linalg.norm(dk, 2)
            dk *= rng.uniform(0.0, 0.75)
            K = K0 + Ghalf @ dk @ Ghalf

            dG, dK, bound, observed = certificate(K0, G0, K, G)
            assert dG < 1.0
            assert observed <= bound + 2e-10
            if bound > 0.0:
                max_ratio = max(max_ratio, observed / bound)
            cases += 1

    print("SOH_RELATIVE_METRIC_PENCIL_STABILITY_V0_1: PASS")
    print("CASES=", cases)
    print("MAX_OBSERVED_TO_BOUND_RATIO=", max_ratio)
    print("FAIL_CLOSED_DELTA_G_GE_1=true")


if __name__ == "__main__":
    main()
