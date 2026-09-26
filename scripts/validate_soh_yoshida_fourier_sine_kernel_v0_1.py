#!/usr/bin/env python3
"""Validate SOH Yoshida-Fourier projector sine-kernel compatibility."""
import cmath
import math


def kernel_direct(N, a, x, y):
    return sum(
        cmath.exp(1j * math.pi * n * (x-y) / a)
        for n in range(-N, N+1)
    ) / (2*a)


def kernel_closed(N, a, x, y):
    M = 2*N + 1
    d = x-y
    z = math.pi*d/(2*a)
    if abs(math.sin(z)) < 1e-14:
        return M/(2*a)
    return math.sin(M*z)/(2*a*math.sin(z))


def g2_finite(N, s):
    M = 2*N + 1
    if abs(s) < 1e-14:
        return 0.0
    return 1.0 - (
        math.sin(math.pi*s)
        / (M*math.sin(math.pi*s/M))
    )**2


def sine_limit_g2(s):
    if abs(s) < 1e-14:
        return 0.0
    return 1.0 - (
        math.sin(math.pi*s)/(math.pi*s)
    )**2


def main():
    # Exact finite geometric-series kernel across unrelated support scales.
    for N in [1,2,8,31]:
        for a in [0.7,2.0,7.3]:
            for d in [0.13,-0.41,1.2]:
                assert abs(
                    kernel_direct(N,a,d,0.0)
                    - kernel_closed(N,a,d,0.0)
                ) < 2e-12

    # Unfolded formula is independent of support parameter a.
    for N in [2,9,37]:
        M = 2*N+1
        for a in [0.5,3.0,11.0]:
            for s in [-1.8,-0.7,0.0,0.3,1.4]:
                d = 2*a*s/M
                rho = M/(2*a)
                k = kernel_direct(N,a,d,0.0)
                observed = 1.0-abs(k/rho)**2
                assert abs(observed-g2_finite(N,s)) < 3e-12

    # Compact-window convergence to the forced sine-kernel pair law.
    grid = [-3.0+6.0*j/600 for j in range(601)]
    errors=[]
    for N in [8,32,128,512]:
        err=max(
            abs(g2_finite(N,s)-sine_limit_g2(s))
            for s in grid
        )
        errors.append(err)

    assert all(errors[i+1] < errors[i] for i in range(len(errors)-1))
    assert errors[-1] < 4e-7

    print("SOH_YOSHIDA_FOURIER_SINE_KERNEL_COMPATIBILITY_V0_1: PASS")
    print("ZETA_ZERO_LIST_USED=false")
    print("GUE_OR_MONTGOMERY_USED_AS_INPUT=false")
    print("SUPPORT_SCALE_CANCELS_AFTER_UNFOLDING=true")
    print("MAX_ERROR_N512=", errors[-1])
    print("PROJECTOR_GEOMETRY_GATE=CLOSED")
    print("ZETA_CAR_OCCUPANCY_GATE=OPEN_SOH_MD001")


if __name__ == "__main__":
    main()
