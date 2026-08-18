"""SOH-G011 forced complex crossings and Euler half-period utilities.

The theorem-level statements implemented here follow from the reciprocal
symmetry X(u)=X(1/u), logarithmic periodicity, and the previously proved
positive Taylor coefficients of the centered xi quotient. Additional complex
zeros of the scale defect are not excluded here.
"""
from __future__ import annotations

import mpmath as mp

from .riemann_kernel import completed_xi


def _scale(a: float | mp.mpf) -> mp.mpf:
    a = mp.mpf(a)
    if not mp.isfinite(a) or a <= 1:
        raise ValueError("a must be finite and greater than one")
    return a


def xi_u_complex(u: complex | mp.mpf | mp.mpc) -> mp.mpc:
    """Return X(u)=xi(u/(1+u)) away from the Möbius pole u=-1."""
    u = mp.mpc(u)
    if not mp.isfinite(u):
        raise ValueError("u must be finite")
    if u == -1:
        raise ValueError("u=-1 is the Möbius pole")
    return completed_xi(u / (1 + u))


def complex_scale_defect(
    u: complex | mp.mpf | mp.mpc,
    a: float | mp.mpf,
) -> mp.mpc:
    """Return Delta_a(u)=X(a*u)-X(u) on its natural complex domain."""
    a = _scale(a)
    u = mp.mpc(u)
    if not mp.isfinite(u):
        raise ValueError("u must be finite")
    if u == -1 or a * u == -1:
        raise ValueError("scale defect hits a Möbius pole")
    return xi_u_complex(a * u) - xi_u_complex(u)


def log_scale_defect(
    lam: complex | mp.mpf | mp.mpc,
    a: float | mp.mpf,
) -> mp.mpc:
    """Return D_a(lambda)=Delta_a(exp(lambda))."""
    a = _scale(a)
    lam = mp.mpc(lam)
    if not mp.isfinite(lam):
        raise ValueError("lambda must be finite")
    return complex_scale_defect(mp.exp(lam), a)


def forced_u_crossings(a: float | mp.mpf) -> tuple[mp.mpf, mp.mpf]:
    """Return the reciprocal fixed-point pair (+a^-1/2, -a^-1/2)."""
    a = _scale(a)
    r = 1 / mp.sqrt(a)
    return r, -r


def logarithmic_crossing(a: float | mp.mpf, k: int) -> mp.mpc:
    """Return lambda_k=-log(a)/2 + pi*i*k."""
    if not isinstance(k, int):
        raise TypeError("k must be an integer")
    a = _scale(a)
    return mp.mpc(-mp.log(a) / 2, mp.pi * k)


def logarithmic_reflection(
    lam: complex | mp.mpf | mp.mpc,
    a: float | mp.mpf,
) -> mp.mpc:
    """Return the scale-defect involution lambda -> -log(a)-lambda."""
    a = _scale(a)
    lam = mp.mpc(lam)
    if not mp.isfinite(lam):
        raise ValueError("lambda must be finite")
    return -mp.log(a) - lam


def euler_half_turn(u: complex | mp.mpf | mp.mpc) -> mp.mpc:
    """Apply the Euler half-turn exp(i*pi), numerically equal to a sign flip."""
    u = mp.mpc(u)
    if not mp.isfinite(u):
        raise ValueError("u must be finite")
    return mp.exp(mp.j * mp.pi) * u


def crossing_quotient_argument(a: float | mp.mpf, k: int) -> mp.mpf:
    r"""Return w at the kth logarithmic forced crossing.

    For even k, w=1/4*tanh^2(log(a)/4). For odd k, the Euler half-turn
    shifts tanh by i*pi/2 and gives w=1/4*coth^2(log(a)/4).
    Both values are strictly positive for a>1.
    """
    if not isinstance(k, int):
        raise TypeError("k must be an integer")
    a = _scale(a)
    q = mp.log(a) / 4
    if k % 2 == 0:
        return mp.mpf("0.25") * mp.tanh(q) ** 2
    return mp.mpf("0.25") * mp.coth(q) ** 2


def numerical_log_crossing_derivative(a: float | mp.mpf, k: int) -> mp.mpc:
    """Numerical regression value for D_a'(lambda_k), not the analytic proof."""
    lam = logarithmic_crossing(a, k)
    return mp.diff(lambda z: log_scale_defect(z, a), lam)
