"""SOH-G012 Euler--Riemann negative-inversion operator algebra.

All identities here are exact coordinate conjugacies. They do not assert
anything about the location of nontrivial zeros of xi or prove RH.
"""
from __future__ import annotations

import mpmath as mp


def _finite_complex(value: complex | mp.mpf | mp.mpc, *, name: str) -> mp.mpc:
    value = mp.mpc(value)
    if not mp.isfinite(value):
        raise ValueError(f"{name} must be finite")
    return value


def riemann_reflection_u(u: complex | mp.mpf | mp.mpc) -> mp.mpc:
    """R(u)=1/u, conjugate to s -> 1-s."""
    u = _finite_complex(u, name="u")
    if u == 0:
        raise ValueError("R is singular at u=0 in the affine chart")
    return 1 / u


def euler_half_turn_u(u: complex | mp.mpf | mp.mpc) -> mp.mpc:
    """E(u)=exp(i*pi)u=-u."""
    u = _finite_complex(u, name="u")
    return -u


def negative_inversion_u(u: complex | mp.mpf | mp.mpc) -> mp.mpc:
    """N(u)=R(E(u))=E(R(u))=-1/u."""
    u = _finite_complex(u, name="u")
    if u == 0:
        raise ValueError("negative inversion is singular at u=0 in the affine chart")
    return -1 / u


def s_from_u(u: complex | mp.mpf | mp.mpc) -> mp.mpc:
    """Inverse Möbius map s=u/(1+u), away from u=-1."""
    u = _finite_complex(u, name="u")
    if u == -1:
        raise ValueError("u=-1 is the Möbius pole")
    return u / (1 + u)


def u_from_s(s: complex | mp.mpf | mp.mpc) -> mp.mpc:
    """Möbius map u=s/(1-s), away from s=1."""
    s = _finite_complex(s, name="s")
    if s == 1:
        raise ValueError("s=1 is the affine Möbius pole")
    return s / (1 - s)


def centered_t_from_u(u: complex | mp.mpf | mp.mpc) -> mp.mpc:
    """t=(u-1)/(u+1)=2s-1, away from u=-1."""
    u = _finite_complex(u, name="u")
    if u == -1:
        raise ValueError("u=-1 is the centered-chart pole")
    return (u - 1) / (u + 1)


def riemann_reflection_t(t: complex | mp.mpf | mp.mpc) -> mp.mpc:
    """R_t(t)=-t."""
    t = _finite_complex(t, name="t")
    return -t


def euler_half_turn_t(t: complex | mp.mpf | mp.mpc) -> mp.mpc:
    """E_t(t)=1/t, the centered conjugate of u -> -u."""
    t = _finite_complex(t, name="t")
    if t == 0:
        raise ValueError("Euler centered inversion is singular at t=0")
    return 1 / t


def negative_inversion_t(t: complex | mp.mpf | mp.mpc) -> mp.mpc:
    """N_t(t)=-1/t."""
    t = _finite_complex(t, name="t")
    if t == 0:
        raise ValueError("negative inversion is singular at t=0")
    return -1 / t


def riemann_reflection_z(z: complex | mp.mpf | mp.mpc) -> mp.mpc:
    """For z=s-1/2=t/2, R_z(z)=-z."""
    z = _finite_complex(z, name="z")
    return -z


def euler_half_turn_z(z: complex | mp.mpf | mp.mpc) -> mp.mpc:
    """For z=s-1/2=t/2, E_z(z)=1/(4z)."""
    z = _finite_complex(z, name="z")
    if z == 0:
        raise ValueError("Euler z-chart inversion is singular at z=0")
    return 1 / (4 * z)


def negative_inversion_z(z: complex | mp.mpf | mp.mpc) -> mp.mpc:
    """For z=s-1/2=t/2, N_z(z)=-1/(4z)."""
    z = _finite_complex(z, name="z")
    if z == 0:
        raise ValueError("negative inversion is singular at z=0")
    return -1 / (4 * z)


def riemann_reflection_w(w: complex | mp.mpf | mp.mpc) -> mp.mpc:
    """For w=z^2, R_z is quotiented out: R_w(w)=w."""
    return _finite_complex(w, name="w")


def euler_half_turn_w(w: complex | mp.mpf | mp.mpc) -> mp.mpc:
    """For w=z^2, E_w(w)=1/(16w)."""
    w = _finite_complex(w, name="w")
    if w == 0:
        raise ValueError("Euler quotient inversion is singular at w=0")
    return 1 / (16 * w)


def negative_inversion_w(w: complex | mp.mpf | mp.mpc) -> mp.mpc:
    """For w=z^2, N_w(w)=1/(16w), equal to E_w after quotienting R."""
    w = _finite_complex(w, name="w")
    if w == 0:
        raise ValueError("negative inversion is singular at w=0")
    return 1 / (16 * w)


def negative_inversion_fixed_u() -> tuple[mp.mpc, mp.mpc]:
    """Return the two affine fixed points of N(u)=-1/u: +i and -i."""
    return mp.j, -mp.j


def negative_inversion_fixed_s() -> tuple[mp.mpc, mp.mpc]:
    """Return their s-plane images: 1/2 +/- i/2."""
    return mp.mpc("0.5", "0.5"), mp.mpc("0.5", "-0.5")


def negative_inversion_fixed_z() -> tuple[mp.mpc, mp.mpc]:
    """Return z=s-1/2 fixed points: +/- i/2."""
    return mp.mpc(0, "0.5"), mp.mpc(0, "-0.5")


def quotient_fixed_w() -> tuple[mp.mpf, mp.mpf]:
    """Fixed points of w -> 1/(16w): +1/4 and -1/4."""
    return mp.mpf("0.25"), mp.mpf("-0.25")


def log_negative_inversion(lam: complex | mp.mpf | mp.mpc) -> mp.mpc:
    r"""Principal lift of N on the log cylinder: lambda -> i*pi-lambda.

    Equality in u holds modulo the full logarithmic period 2*pi*i.
    """
    lam = _finite_complex(lam, name="lambda")
    return mp.j * mp.pi - lam


def log_negative_inversion_fixed(k: int = 0) -> mp.mpc:
    """Fixed lift lambda=i*pi/2 + pi*i*k, k integer."""
    if not isinstance(k, int):
        raise TypeError("k must be an integer")
    return mp.j * (mp.pi / 2 + mp.pi * k)
