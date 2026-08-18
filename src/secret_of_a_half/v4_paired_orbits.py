"""SOH-G017 V4 orbit utilities for the negative-inversion paired spectrum.

The theorem note proves the set-theoretic orbit classification.  These helpers
encode the exact projective maps and provide deterministic regression checks;
they are not a numerical proof of any zero claim.
"""
from __future__ import annotations

import mpmath as mp

from .negative_inversion_zero_set import negative_inversion_s


def _finite_complex(value: complex | mp.mpf | mp.mpc, *, name: str) -> mp.mpc:
    value = mp.mpc(value)
    if not mp.isfinite(value):
        raise ValueError(f"{name} must be finite")
    return value


def reflection_s(s: complex | mp.mpf | mp.mpc) -> mp.mpc:
    """R(s)=1-s, the holomorphic xi reflection."""
    s = _finite_complex(s, name="s")
    return 1 - s


def euler_halfturn_s(s: complex | mp.mpf | mp.mpc) -> mp.mpc:
    """E(s)=s/(2s-1), conjugate to u -> -u in the Li coordinate."""
    s = _finite_complex(s, name="s")
    if 2 * s - 1 == 0:
        raise ValueError("Euler half-turn has its affine pole at s=1/2")
    return s / (2 * s - 1)


def v4_images(s: complex | mp.mpf | mp.mpc) -> dict[str, mp.mpc]:
    """Return the four projective V4 images I,R,N,E of s."""
    s = _finite_complex(s, name="s")
    if 2 * s - 1 == 0:
        raise ValueError("V4 affine chart is singular at s=1/2 for N and E")
    return {
        "I": s,
        "R": reflection_s(s),
        "N": negative_inversion_s(s),
        "E": euler_halfturn_s(s),
    }


def v4_algebra_residuals(s: complex | mp.mpf | mp.mpc) -> dict[str, mp.mpf]:
    """Residuals for R^2=N^2=E^2=I and RN=NR=E."""
    s = _finite_complex(s, name="s")
    if 2 * s - 1 == 0:
        raise ValueError("V4 affine chart is singular at s=1/2")
    r = reflection_s
    n = negative_inversion_s
    e = euler_halfturn_s
    return {
        "R2": abs(r(r(s)) - s),
        "N2": abs(n(n(s)) - s),
        "E2": abs(e(e(s)) - s),
        "RN_E": abs(r(n(s)) - e(s)),
        "NR_E": abs(n(r(s)) - e(s)),
    }


def negative_inversion_fixed_pair() -> tuple[mp.mpc, mp.mpc]:
    """The two affine fixed points of N: 1/2 +/- i/2."""
    return mp.mpc("0.5", "0.5"), mp.mpc("0.5", "-0.5")


def reflection_fixed_point() -> mp.mpc:
    """The unique affine fixed point of R."""
    return mp.mpc("0.5")


def euler_halfturn_fixed_pair() -> tuple[mp.mpc, mp.mpc]:
    """The affine fixed points of E: 0 and 1."""
    return mp.mpc(0), mp.mpc(1)


def orbit_cardinality(
    s: complex | mp.mpf | mp.mpc,
    *,
    tolerance: mp.mpf | float | str = "1e-40",
) -> int:
    """Count distinct V4 images numerically with an explicit tolerance."""
    tol = mp.mpf(tolerance)
    if not mp.isfinite(tol) or tol < 0:
        raise ValueError("tolerance must be finite and non-negative")
    values = list(v4_images(s).values())
    representatives: list[mp.mpc] = []
    for value in values:
        if not any(abs(value - rep) <= tol for rep in representatives):
            representatives.append(value)
    return len(representatives)


def paired_set_cardinality(generic_orbits: int, exceptional_pair_present: bool) -> int:
    """Return |P_N|=4a+2 epsilon from the G017 orbit decomposition."""
    if isinstance(generic_orbits, bool) or not isinstance(generic_orbits, int):
        raise TypeError("generic_orbits must be an integer")
    if generic_orbits < 0:
        raise ValueError("generic_orbits must be non-negative")
    return 4 * generic_orbits + (2 if exceptional_pair_present else 0)


def quotient_paired_set_cardinality(
    generic_orbits: int, exceptional_pair_present: bool
) -> int:
    """Return the corresponding |P_J|=2a+epsilon from G016."""
    if isinstance(generic_orbits, bool) or not isinstance(generic_orbits, int):
        raise TypeError("generic_orbits must be an integer")
    if generic_orbits < 0:
        raise ValueError("generic_orbits must be non-negative")
    return 2 * generic_orbits + (1 if exceptional_pair_present else 0)
