"""SOH-G019 PF2 ratio-majorant zero-free disk for the even xi quotient.

Let F(w)=sum_{k>=0} a_k w^k with a_k>0.  G005 proves PF2, hence the
coefficient ratios a_{k+1}/a_k are non-increasing.  Therefore, with
q0=a1/a0,

    a_k <= a0*q0**k.

This yields a zero-free disk of radius R0=a0/(2*a1).  The theorem itself is
analytic; numerical helpers below are regression aids only.
"""
from __future__ import annotations

import mpmath as mp

from .negative_inversion_zero_set import completed_xi
from .quotient_zero_set import quotient_F


def _positive_mpf(value: mp.mpf | float | int, *, name: str) -> mp.mpf:
    value = mp.mpf(value)
    if not mp.isfinite(value) or value <= 0:
        raise ValueError(f"{name} must be finite and positive")
    return value


def pf2_ratio_zero_free_radius(a0: mp.mpf | float, a1: mp.mpf | float) -> mp.mpf:
    """Return R0=a0/(2*a1), the G019 PF2 ratio-majorant radius."""

    a0 = _positive_mpf(a0, name="a0")
    a1 = _positive_mpf(a1, name="a1")
    return a0 / (2 * a1)


def pf2_tail_majorant(a0: mp.mpf | float, a1: mp.mpf | float, radius: mp.mpf | float) -> mp.mpf:
    r"""Return the geometric tail majorant at ``radius``.

    Under PF2, q0=a1/a0 and a_k<=a0*q0^k.  For q0*r<1,

        sum_{k>=1} a_k r^k <= a0*(q0*r)/(1-q0*r).
    """

    a0 = _positive_mpf(a0, name="a0")
    a1 = _positive_mpf(a1, name="a1")
    radius = mp.mpf(radius)
    if not mp.isfinite(radius) or radius < 0:
        raise ValueError("radius must be finite and non-negative")
    q0 = a1 / a0
    qr = q0 * radius
    if qr >= 1:
        raise ValueError("geometric majorant requires (a1/a0)*radius < 1")
    return a0 * qr / (1 - qr)


def first_two_coefficients_numeric() -> tuple[mp.mpf, mp.mpf]:
    r"""Numerically evaluate a0 and a1 for regression purposes.

    From xi(1/2+z)=F(z^2),

        a0 = xi(1/2),
        a1 = (1/2) d^2/dz^2 xi(1/2+z)|_{z=0}.
    """

    a0 = mp.re(completed_xi(mp.mpf("0.5")))
    f = lambda z: completed_xi(mp.mpf("0.5") + z)
    a1 = mp.re(mp.diff(f, mp.mpf("0"), 2) / 2)
    return a0, a1


def canonical_pf2_zero_free_radius_numeric() -> mp.mpf:
    """Numerical regression value for the canonical G019 radius."""

    a0, a1 = first_two_coefficients_numeric()
    return pf2_ratio_zero_free_radius(a0, a1)


def boundary_regression(samples: int = 64) -> mp.mpf:
    """Return the smallest sampled |F(w)| on |w|=R0.

    Sampling is not the proof.  The closed-disk result follows from PF2 plus
    the fact that F is entire; equality in the geometric majorant at R0 would
    force every coefficient ratio to equal q0 and hence a finite convergence
    radius, contradiction.
    """

    if samples < 4:
        raise ValueError("samples must be at least 4")
    radius = canonical_pf2_zero_free_radius_numeric()
    values = []
    for k in range(samples):
        theta = 2 * mp.pi * k / samples
        w = radius * mp.e ** (mp.j * theta)
        values.append(abs(quotient_F(w)))
    return min(values)


def ratio_majorant_certificate(a0: mp.mpf | float, a1: mp.mpf | float) -> dict[str, mp.mpf | bool]:
    """Return the exact algebraic quantities used by the PF2 majorant."""

    a0 = _positive_mpf(a0, name="a0")
    a1 = _positive_mpf(a1, name="a1")
    q0 = a1 / a0
    radius = pf2_ratio_zero_free_radius(a0, a1)
    qr = q0 * radius
    return {
        "q0": q0,
        "radius": radius,
        "q0_times_radius": qr,
        "boundary_qr_is_half": qr == mp.mpf("0.5"),
        "open_disk_tail_lt_a0": True,
        "closed_disk_strictness_uses_entirety": True,
    }
