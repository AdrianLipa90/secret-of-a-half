"""SOH-G014 negative-inversion zero-set no-go utilities.

The theorem proved in the accompanying note is analytic: the canonical
negative inversion cannot preserve the complete xi zero set, and only
finitely many xi zeros can be paired with another xi zero by this map.
The numerical helpers below are regression checks, not the proof.
"""
from __future__ import annotations

import mpmath as mp


def _finite_complex(value: complex | mp.mpf | mp.mpc, *, name: str) -> mp.mpc:
    value = mp.mpc(value)
    if not mp.isfinite(value):
        raise ValueError(f"{name} must be finite")
    return value


def negative_inversion_s(s: complex | mp.mpf | mp.mpc) -> mp.mpc:
    """Canonical G012 negative inversion in the s-plane.

    If u=s/(1-s) and N_u(u)=-1/u, then
        N_s(s)=(s-1)/(2s-1).
    The affine chart has a pole at s=1/2.
    """
    s = _finite_complex(s, name="s")
    if 2 * s - 1 == 0:
        raise ValueError("negative inversion has its affine pole at s=1/2")
    return (s - 1) / (2 * s - 1)


def negative_inversion_defect_from_half(s: complex | mp.mpf | mp.mpc) -> mp.mpc:
    """Return N_s(s)-1/2 using its exact closed form -1/(4s-2)."""
    s = _finite_complex(s, name="s")
    if 2 * s - 1 == 0:
        raise ValueError("negative inversion has its affine pole at s=1/2")
    return -1 / (4 * s - 2)


def negative_inversion_fixed_s() -> tuple[mp.mpc, mp.mpc]:
    """Affine fixed pair of N_s: 1/2 +/- i/2."""
    return mp.mpc("0.5", "0.5"), mp.mpc("0.5", "-0.5")


def completed_xi(s: complex | mp.mpf | mp.mpc) -> mp.mpc:
    """Completed Riemann xi away from the removable points 0 and 1."""
    s = _finite_complex(s, name="s")
    if s == 0 or s == 1:
        return mp.mpf("0.5")
    return (
        mp.mpf("0.5")
        * s
        * (s - 1)
        * mp.power(mp.pi, -s / 2)
        * mp.gamma(s / 2)
        * mp.zeta(s)
    )


def mapped_critical_height(t: mp.mpf | float | str) -> mp.mpc:
    """For s=1/2+i t, return N_s(s)=1/2+i/(4t)."""
    t = mp.mpf(t)
    if not mp.isfinite(t) or t == 0:
        raise ValueError("t must be finite and non-zero")
    return mp.mpc(mp.mpf("0.5"), 1 / (4 * t))
