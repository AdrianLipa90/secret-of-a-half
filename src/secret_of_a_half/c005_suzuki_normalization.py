"""Exact coordinate/Fourier scaling between the SOH arithmetic convention and Suzuki's.

SOH arithmetic convention:
    r = (s - 1/2) / i
    Fourier kernel exp(-2*pi*i*x_repo*r)
    prime support x_repo = log(n)/(2*pi)

Suzuki spectral convention:
    z = i (s - 1/2) = -r
    Fourier kernel exp(i*z*x_suzuki)

Therefore x_suzuki = 2*pi*x_repo makes the kernels identical.

This module closes only the coordinate and Fourier normalization.  It does not
identify operator domains, boundary conditions, Friedrichs extensions, or the
full localized form automatically.
"""
from __future__ import annotations

import math


def soh_spectral_r(s: complex) -> complex:
    return (complex(s) - 0.5) / 1j


def suzuki_spectral_z(s: complex) -> complex:
    return 1j * (complex(s) - 0.5)


def suzuki_z_from_soh_r(r: complex) -> complex:
    return -complex(r)


def soh_r_from_suzuki_z(z: complex) -> complex:
    return -complex(z)


def suzuki_x_from_soh_x(x_repo: float) -> float:
    return 2.0 * math.pi * float(x_repo)


def soh_x_from_suzuki_x(x_suzuki: float) -> float:
    return float(x_suzuki) / (2.0 * math.pi)


def soh_prime_shift(n: int) -> float:
    if n < 1:
        raise ValueError("n must be positive")
    return math.log(n) / (2.0 * math.pi)


def suzuki_prime_shift(n: int) -> float:
    if n < 1:
        raise ValueError("n must be positive")
    return math.log(n)


def soh_support_halfwidth(a_suzuki: float) -> float:
    if a_suzuki <= 0.0:
        raise ValueError("a_suzuki must be positive")
    return a_suzuki / (2.0 * math.pi)


def fourier_phase_soh(x_repo: float, r: complex) -> complex:
    return complex(-2.0 * math.pi * 1j * float(x_repo) * complex(r))


def fourier_phase_suzuki(x_suzuki: float, z: complex) -> complex:
    return complex(1j * complex(z) * float(x_suzuki))


def normalization_crosswalk_receipt() -> dict[str, object]:
    return {
        "schema": "SOH_SUZUKI_FOURIER_NORMALIZATION_CROSSWALK_V0_1",
        "exact": {
            "z_suzuki_equals_minus_r_soh": True,
            "x_suzuki_equals_2pi_x_soh": True,
            "prime_shift_log_n_matches": True,
            "fourier_phase_matches_under_crosswalk": True,
            "support_halfwidth_map": "a_suzuki -> a_suzuki/(2*pi) in SOH x-coordinate",
        },
        "open": [
            "localized form equality with all boundary terms",
            "domain/core identification",
            "Friedrichs-extension identification inside repository code",
            "Yoshida coercivity constant in exact repository normalization",
            "SOH-C005",
            "Riemann Hypothesis",
        ],
        "proof_of_rh": False,
    }
