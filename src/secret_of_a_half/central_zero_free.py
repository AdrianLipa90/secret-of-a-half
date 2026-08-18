"""SOH-G018 central zero-free interval from the G017 moment bound.

The analytic theorem is
    xi(1/2+i t) > F(0) * (1 - t^2/20)
for |t|<sqrt(20), with strict positivity also at the two endpoints because
G017 gives the strict moment inequality m2 < m0/10.  Equivalently,
F(w)>0 for every real w in [-20,0].  Earlier positive coefficients extend
this to every real w>=-20.
"""
from __future__ import annotations

import mpmath as mp

from .negative_inversion_zero_set import completed_xi
from .quotient_zero_set import quotient_F


def central_radius_squared() -> int:
    """Return the exact safe squared zero-free radius 20."""
    return 20


def central_radius() -> mp.mpf:
    """Return sqrt(20) at current mpmath precision."""
    return mp.sqrt(central_radius_squared())


def normalized_lower_bound(t: complex | mp.mpf | mp.mpc) -> mp.mpf:
    """Return 1-t^2/20 for a finite real t."""
    t = mp.mpc(t)
    if not mp.isfinite(t) or mp.im(t) != 0:
        raise ValueError("t must be finite and real")
    tr = mp.re(t)
    return 1 - tr * tr / central_radius_squared()


def xi_on_critical_line(t: complex | mp.mpf | mp.mpc) -> mp.mpc:
    """Evaluate xi(1/2+i t) for a finite real t."""
    t = mp.mpc(t)
    if not mp.isfinite(t) or mp.im(t) != 0:
        raise ValueError("t must be finite and real")
    return completed_xi(mp.mpf("0.5") + 1j * mp.re(t))


def F_on_negative_axis_from_t(t: complex | mp.mpf | mp.mpc) -> mp.mpc:
    """Evaluate F(-t^2), equal to xi(1/2+i t)."""
    t = mp.mpc(t)
    if not mp.isfinite(t) or mp.im(t) != 0:
        raise ValueError("t must be finite and real")
    tr = mp.re(t)
    return quotient_F(-(tr * tr))
