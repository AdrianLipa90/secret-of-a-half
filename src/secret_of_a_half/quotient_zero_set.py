"""SOH-G015 quotient-level negative-inversion zero-set utilities.

The analytic theorem concerns the entire function F defined by
    xi(1/2 + z) = F(z^2)
and the quotient involution J(w)=1/(16w).  Numerical helpers are regression
checks only; the finiteness theorem is proved in the accompanying note.
"""
from __future__ import annotations

import mpmath as mp

from .negative_inversion_zero_set import completed_xi


def _finite_complex(value: complex | mp.mpf | mp.mpc, *, name: str) -> mp.mpc:
    value = mp.mpc(value)
    if not mp.isfinite(value):
        raise ValueError(f"{name} must be finite")
    return value


def quotient_negative_inversion_w(w: complex | mp.mpf | mp.mpc) -> mp.mpc:
    """J(w)=1/(16w), the G012 negative inversion after w=z^2 quotienting."""
    w = _finite_complex(w, name="w")
    if w == 0:
        raise ValueError("quotient negative inversion is singular at w=0")
    return 1 / (16 * w)


def quotient_fixed_w() -> tuple[mp.mpf, mp.mpf]:
    """Fixed values of J(w)=1/(16w): +1/4 and -1/4."""
    return mp.mpf("0.25"), mp.mpf("-0.25")


def quotient_F(w: complex | mp.mpf | mp.mpc) -> mp.mpc:
    r"""Evaluate F(w) from xi(1/2+z)=F(z^2) using a principal square root.

    The value is branch-independent because xi(1/2+z) is even in z.
    """
    w = _finite_complex(w, name="w")
    z = mp.sqrt(w)
    return completed_xi(mp.mpf("0.5") + z)


def quotient_F_branch_residual(w: complex | mp.mpf | mp.mpc) -> mp.mpf:
    """Numerically verify equality of the two square-root branches."""
    w = _finite_complex(w, name="w")
    z = mp.sqrt(w)
    return abs(
        completed_xi(mp.mpf("0.5") + z)
        - completed_xi(mp.mpf("0.5") - z)
    )


def w_from_xi_zero(rho: complex | mp.mpf | mp.mpc) -> mp.mpc:
    """Map an xi zero coordinate rho to the even quotient w=(rho-1/2)^2."""
    rho = _finite_complex(rho, name="rho")
    z = rho - mp.mpf("0.5")
    return z * z
