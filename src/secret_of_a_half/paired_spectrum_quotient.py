"""SOH-G016 paired-spectrum quotient correspondence utilities.

The exact diagram is
    q(s) = (s-1/2)^2,
    q(N_s(s)) = J(q(s)),
where N_s is the G014 negative inversion and J(w)=1/(16w) is the G015
quotient involution.  Set-theoretic paired-root correspondence is proved in
the accompanying theorem note; numerical helpers are regression checks only.
"""
from __future__ import annotations

import mpmath as mp

from .negative_inversion_zero_set import negative_inversion_s
from .quotient_zero_set import quotient_negative_inversion_w


def _finite_complex(value: complex | mp.mpf | mp.mpc, *, name: str) -> mp.mpc:
    value = mp.mpc(value)
    if not mp.isfinite(value):
        raise ValueError(f"{name} must be finite")
    return value


def quotient_map_s_to_w(s: complex | mp.mpf | mp.mpc) -> mp.mpc:
    """q(s)=(s-1/2)^2."""
    s = _finite_complex(s, name="s")
    z = s - mp.mpf("0.5")
    return z * z


def reflection_s(s: complex | mp.mpf | mp.mpc) -> mp.mpc:
    """Holomorphic xi reflection s -> 1-s."""
    s = _finite_complex(s, name="s")
    return 1 - s


def quotient_fiber(w: complex | mp.mpf | mp.mpc) -> tuple[mp.mpc, mp.mpc]:
    """Return the two s-preimages of w under q, using the principal sqrt."""
    w = _finite_complex(w, name="w")
    z = mp.sqrt(w)
    return mp.mpf("0.5") + z, mp.mpf("0.5") - z


def diagram_residual(s: complex | mp.mpf | mp.mpc) -> mp.mpf:
    """Residual of q∘N_s = J∘q, away from s=1/2."""
    s = _finite_complex(s, name="s")
    w = quotient_map_s_to_w(s)
    if w == 0:
        raise ValueError("the quotient involution is singular over s=1/2")
    return abs(
        quotient_map_s_to_w(negative_inversion_s(s))
        - quotient_negative_inversion_w(w)
    )


def negative_inversion_fiber_action(
    w: complex | mp.mpf | mp.mpc,
) -> tuple[tuple[mp.mpc, mp.mpc], tuple[mp.mpc, mp.mpc]]:
    """Return source fiber and its N_s images over J(w)."""
    w = _finite_complex(w, name="w")
    if w == 0:
        raise ValueError("the quotient involution is singular at w=0")
    source = quotient_fiber(w)
    images = tuple(negative_inversion_s(s) for s in source)
    return source, images
