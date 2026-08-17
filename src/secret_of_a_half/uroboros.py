"""Exact SOH-G007/G008/G009 Uroboros and Collatz–Riemann maps.

The module separates proved algebraic identities from the optional Uroboros
scale-identification convention.  It does not assume the Collatz conjecture,
assert scale-periodicity of xi, or prove RH.
"""
from __future__ import annotations

import cmath
import math
from dataclasses import dataclass
from fractions import Fraction
from numbers import Real
from typing import Iterable

import mpmath as mp

from .riemann_kernel import completed_xi

UROBOROS_SCALE = 32
LOG_UROBOROS_SCALE = 5.0 * math.log(2.0)


def _positive_real(value: Real, *, name: str) -> float:
    x = float(value)
    if not math.isfinite(x) or x <= 0.0:
        raise ValueError(f"{name} must be finite and strictly positive")
    return x


def _scale(value: Real) -> float:
    scale = _positive_real(value, name="scale")
    if scale <= 1.0:
        raise ValueError("scale must be greater than 1")
    return scale


def x_to_u(x: Real) -> float:
    return 2.0 * _positive_real(x, name="x")


def u_to_x(u: Real) -> float:
    return 0.5 * _positive_real(u, name="u")


def u_to_s(u: Real) -> float:
    u = _positive_real(u, name="u")
    return u / (1.0 + u)


def s_to_u(s: Real) -> float:
    s = float(s)
    if not math.isfinite(s) or not 0.0 < s < 1.0:
        raise ValueError("s must be finite and satisfy 0 < s < 1")
    return s / (1.0 - s)


def x_to_s(x: Real) -> float:
    return u_to_s(x_to_u(x))


def s_to_x(s: Real) -> float:
    return u_to_x(s_to_u(s))


def u_to_t(u: Real) -> float:
    """Centered Bloch/Riemann coordinate ``t=(u-1)/(u+1)``."""
    u = _positive_real(u, name="u")
    return (u - 1.0) / (u + 1.0)


def t_to_u(t: Real) -> float:
    t = float(t)
    if not math.isfinite(t) or not -1.0 < t < 1.0:
        raise ValueError("t must be finite and satisfy -1 < t < 1")
    return (1.0 + t) / (1.0 - t)


def s_to_t(s: Real) -> float:
    s = float(s)
    if not math.isfinite(s):
        raise ValueError("s must be finite")
    return 2.0 * s - 1.0


def t_to_s(t: Real) -> float:
    t = float(t)
    if not math.isfinite(t):
        raise ValueError("t must be finite")
    return 0.5 * (1.0 + t)


def x_to_t(x: Real) -> float:
    return u_to_t(x_to_u(x))


def inverse_about_half_x(x: Real) -> float:
    x = _positive_real(x, name="x")
    return 1.0 / (4.0 * x)


def invert_u(u: Real) -> float:
    u = _positive_real(u, name="u")
    return 1.0 / u


def riemann_reflection_s(s: Real) -> float:
    s = float(s)
    if not math.isfinite(s):
        raise ValueError("s must be finite")
    return 1.0 - s


def halving_s(s: Real) -> float:
    s = float(s)
    if not math.isfinite(s) or s == 2.0:
        raise ValueError("s must be finite and different from 2")
    return s / (2.0 - s)


def halving_s_inverse(s: Real) -> float:
    s = float(s)
    if not math.isfinite(s) or s == -1.0:
        raise ValueError("s must be finite and different from -1")
    return 2.0 * s / (1.0 + s)


def odd_collatz_s(s: Real) -> float:
    s = float(s)
    if not math.isfinite(s):
        raise ValueError("s must be finite")
    return (s + 2.0) / 3.0


def halving_t(t: Real) -> float:
    """Halving branch in the centered coordinate: ``(3t-1)/(3-t)``."""
    t = float(t)
    if not math.isfinite(t) or t == 3.0:
        raise ValueError("t must be finite and different from 3")
    return (3.0 * t - 1.0) / (3.0 - t)


def odd_collatz_t(t: Real) -> float:
    """Odd Collatz branch in the centered coordinate: ``(t+2)/3``."""
    t = float(t)
    if not math.isfinite(t):
        raise ValueError("t must be finite")
    return (t + 2.0) / 3.0


def scale_t(t: Real, scale: Real) -> float:
    """Conjugate ``u -> scale*u`` into the centered coordinate ``t``."""
    a = _positive_real(scale, name="scale")
    t = float(t)
    if not math.isfinite(t):
        raise ValueError("t must be finite")
    numerator = (a - 1.0) + (a + 1.0) * t
    denominator = (a + 1.0) + (a - 1.0) * t
    if denominator == 0.0:
        raise ValueError("scale transform denominator vanished")
    return numerator / denominator


def collatz_step_x(n: int) -> int:
    if not isinstance(n, int) or isinstance(n, bool) or n <= 0:
        raise ValueError("n must be a positive integer")
    return n // 2 if n % 2 == 0 else 3 * n + 1


def collatz_step_s_from_integer(n: int) -> float:
    if not isinstance(n, int) or isinstance(n, bool) or n <= 0:
        raise ValueError("n must be a positive integer")
    s = x_to_s(n)
    return halving_s(s) if n % 2 == 0 else odd_collatz_s(s)


def exact_x_to_s(x: Fraction) -> Fraction:
    if x <= 0:
        raise ValueError("x must be strictly positive")
    return (2 * x) / (1 + 2 * x)


def exact_x_to_t(x: Fraction) -> Fraction:
    if x <= 0:
        raise ValueError("x must be strictly positive")
    u = 2 * x
    return (u - 1) / (u + 1)


def exact_halving_s(s: Fraction) -> Fraction:
    if s == 2:
        raise ValueError("s must differ from 2")
    return s / (2 - s)


def exact_odd_collatz_s(s: Fraction) -> Fraction:
    return (s + 2) / 3


def exact_halving_t(t: Fraction) -> Fraction:
    if t == 3:
        raise ValueError("t must differ from 3")
    return (3 * t - 1) / (3 - t)


def exact_odd_collatz_t(t: Fraction) -> Fraction:
    return (t + 2) / 3


def exact_scale_t(t: Fraction, scale: Fraction) -> Fraction:
    if scale <= 0:
        raise ValueError("scale must be strictly positive")
    denominator = (scale + 1) + (scale - 1) * t
    if denominator == 0:
        raise ValueError("scale transform denominator vanished")
    return ((scale - 1) + (scale + 1) * t) / denominator


def compose_boost_parameters(p: Fraction, q: Fraction) -> Fraction:
    """Hyperbolic/Möbius parameter composition ``(p+q)/(1+pq)``."""
    denominator = 1 + p * q
    if denominator == 0:
        raise ValueError("boost composition denominator vanished")
    return (p + q) / denominator


@dataclass(frozen=True)
class TorusCoordinate:
    radial: float
    phase: float


def torus_coordinate(u: complex) -> TorusCoordinate:
    """Reduce nonzero complex ``u`` modulo ``u~32u`` and phase periodicity."""
    u = complex(u)
    if u == 0 or not (math.isfinite(u.real) and math.isfinite(u.imag)):
        raise ValueError("u must be finite and nonzero")
    return TorusCoordinate(
        radial=math.log(abs(u)) % LOG_UROBOROS_SCALE,
        phase=cmath.phase(u) % (2.0 * math.pi),
    )


def centered_scale_bounds(scale: Real = UROBOROS_SCALE) -> tuple[float, float]:
    """Return the reciprocal cell boundaries ``a^-1/2`` and ``a^1/2``."""
    a = _scale(scale)
    root = math.sqrt(a)
    return 1.0 / root, root


def scale_defect_involution_u(u: Real, scale: Real = UROBOROS_SCALE) -> float:
    """Return the involution ``u -> 1/(a u)`` for an ``a``-scale defect."""
    a = _scale(scale)
    u = _positive_real(u, name="u")
    return 1.0 / (a * u)


def xi_in_u(u: Real | mp.mpf) -> mp.mpc:
    """Evaluate ``X(u)=xi(u/(1+u))`` on the positive real ``u`` axis."""
    uu = mp.mpf(u)
    if not mp.isfinite(uu) or uu <= 0:
        raise ValueError("u must be finite and strictly positive")
    return completed_xi(uu / (1 + uu))


def xi_scale_defect(u: Real | mp.mpf, scale: Real = UROBOROS_SCALE) -> mp.mpc:
    """Return ``Delta_a(u)=X(a u)-X(u)`` without assuming scale-periodicity."""
    a = mp.mpf(_scale(scale))
    uu = mp.mpf(u)
    if not mp.isfinite(uu) or uu <= 0:
        raise ValueError("u must be finite and strictly positive")
    return xi_in_u(a * uu) - xi_in_u(uu)


def halving_orbit(values: Iterable[Real]) -> list[float]:
    """Map a supplied positive x-sequence into s without asserting convergence."""
    return [x_to_s(value) for value in values]
