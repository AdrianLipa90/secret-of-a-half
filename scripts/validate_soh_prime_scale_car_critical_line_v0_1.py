#!/usr/bin/env python3
"""Finite algebra checks for the prime-scale CAR critical-line criterion."""
from __future__ import annotations

import cmath
import math


def normalized_channel(q: float, beta: float, gamma: float) -> complex:
    return cmath.exp(((beta - 0.5) + 1j * gamma) * math.log(q))


def occupation(q: float, beta: float) -> float:
    return q ** (2.0 * beta - 1.0)


def main() -> None:
    max_modulus_error = 0.0
    for q in [2.0, 3.0, 5.0, 11.0, 97.0]:
        for beta in [0.1, 0.25, 0.5, 0.75, 0.9]:
            for gamma in [0.0, 1.0, 14.134725141734693, 100.0]:
                z = normalized_channel(q, beta, gamma)
                expected = q ** (beta - 0.5)
                err = abs(abs(z) - expected)
                max_modulus_error = max(max_modulus_error, err)
                assert err < 2e-13

            lam = occupation(q, beta)
            assert abs(lam - q ** (2.0 * beta - 1.0)) < 1e-15

            if beta == 0.5:
                assert abs(lam - 1.0) < 1e-15
            elif beta > 0.5:
                assert lam > 1.0
            else:
                assert 0.0 < lam < 1.0

            reflected = occupation(q, 1.0 - beta)
            assert abs(lam * reflected - 1.0) < 2e-13

            if beta != 0.5:
                assert max(lam, reflected) > 1.0

    print("SOH_PRIME_SCALE_CAR_CRITICAL_LINE_CRITERION_V0_1: PASS")
    print("MAX_MODULUS_ERROR=", max_modulus_error)
    print("UNIT_MODULUS_IFF_BETA_HALF=true")
    print("OFF_AXIS_REFLECTION_ORBIT_VIOLATES_CAR_CONTRACTION=true")
    print("ZETA_TO_CAR_BINDING_PROVED=false")


if __name__ == "__main__":
    main()
