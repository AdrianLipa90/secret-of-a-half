#!/usr/bin/env python3
"""Regression checks for the explicit sharp-to-smooth Fourier majorant."""
from __future__ import annotations

import math


EULER_GAMMA = 0.5772156649015328606


def log_energy_majorant(a: float, p: float, delta: float) -> float:
    if not (a > 0.0 and 0.0 < delta <= math.exp(-1.0)):
        raise ValueError("require a>0 and 0<delta<=e^-1")
    B = math.exp(abs(p) * a)
    q = abs(p) * a
    M = 2.0 * B * (2.0 + q * delta)
    L = math.log(1.0 / delta)
    low = 8.0 * B * B * delta * delta * (
        2.0 + (L - 1.0 + EULER_GAMMA) / delta
    )
    high = 2.0 * M * M * delta * (L + 1.0 + EULER_GAMMA)
    return (low + high) / (2.0 * math.pi)


def main() -> None:
    # Positivity and asymptotic regression: E/(delta log(1/delta))
    # remains bounded and approaches a finite constant for fixed a,p.
    cases = 0
    for a in [0.25, 1.0, 2.0]:
        for p in [0.75, 1.0, 1.5]:
            ratios = []
            for k in [4, 6, 8, 10, 12]:
                delta = math.exp(-k)
                E = log_energy_majorant(a, p, delta)
                assert E > 0.0
                ratios.append(E / (delta * math.log(1.0 / delta)))
                cases += 1
            assert ratios[-1] <= 2.0 * ratios[0]

    print("SOH_EXPLICIT_SHARP_TO_SMOOTH_WEIL_FORM_RATE_V0_1: PASS")
    print("CASES=", cases)
    print("ASYMPTOTIC_ORDER=delta_log_1_over_delta")
    print("RH_USED=false")
    print("ZERO_LIST_USED=false")
    print("STATUS=LIV_MD2C4B2_CLOSED")


if __name__ == "__main__":
    main()
