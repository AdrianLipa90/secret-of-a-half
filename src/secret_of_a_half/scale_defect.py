"""SOH-G010 scale-defect crossing utilities.

Exact theorem support on the positive real u-axis. No RH claim.
"""
from __future__ import annotations

import math
import mpmath as mp

from .riemann_kernel import completed_xi


def xi_u(u: float | mp.mpf) -> mp.mpf:
    u = mp.mpf(u)
    if not mp.isfinite(u) or u <= 0:
        raise ValueError("u must be finite and strictly positive")
    s = u / (1 + u)
    return mp.re(completed_xi(s))


def xi_log_coordinate(lam: float | mp.mpf) -> mp.mpf:
    lam = mp.mpf(lam)
    if not mp.isfinite(lam):
        raise ValueError("lambda must be finite")
    return xi_u(mp.e**lam)


def scale_defect(u: float | mp.mpf, a: float | mp.mpf) -> mp.mpf:
    u = mp.mpf(u)
    a = mp.mpf(a)
    if not mp.isfinite(u) or u <= 0:
        raise ValueError("u must be finite and strictly positive")
    if not mp.isfinite(a) or a <= 1:
        raise ValueError("a must be finite and greater than one")
    return xi_u(a * u) - xi_u(u)


def scale_defect_crossing(a: float | mp.mpf) -> mp.mpf:
    """Return the exact positive crossing a^(-1/2) at current mp precision."""
    a = mp.mpf(a)
    if not mp.isfinite(a) or a <= 1:
        raise ValueError("a must be finite and greater than one")
    return 1 / mp.sqrt(a)


def scale_defect_sign_region(u: float, a: float) -> int:
    """Return theorem sign: -1 below a^-1/2, 0 at it, +1 above it."""
    u = float(u)
    a = float(a)
    if not math.isfinite(u) or u <= 0.0:
        raise ValueError("u must be finite and strictly positive")
    if not math.isfinite(a) or a <= 1.0:
        raise ValueError("a must be finite and greater than one")
    c = 1.0 / math.sqrt(a)
    if math.isclose(u, c, rel_tol=1e-14, abs_tol=1e-15):
        return 0
    return -1 if u < c else 1


def quotient_argument_from_lambda(lam: float | mp.mpf) -> mp.mpf:
    """w(lambda)=1/4 tanh^2(lambda/2), so X(e^lambda)=F(w(lambda))."""
    lam = mp.mpf(lam)
    if not mp.isfinite(lam):
        raise ValueError("lambda must be finite")
    return mp.mpf("0.25") * mp.tanh(lam / 2) ** 2
