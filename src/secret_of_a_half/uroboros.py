"""Exact SOH-G007/G008 Uroboros and Collatz–Riemann maps.

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


def exact_halving_s(s: Fraction) -> Fraction:
    if s == 2:
        raise ValueError("s must differ from 2")
    return s / (2 - s)


def exact_odd_collatz_s(s: Fraction) -> Fraction:
    return (s + 2) / 3


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
