"""Exact one-step curvature barrier for the SOH-G006 solid PF3 margin.

This module contains algebraic identities and finite diagnostics only.  It does
not prove that the Riemann-xi quotient coefficient sequence satisfies the
barrier at every index, nor does it prove PF3, PF-infinity, real-rootedness, or
RH.
"""

from __future__ import annotations


def pf3_margin(u, v, w):
    """Return the exact G006 solid PF3 ratio-curvature margin."""

    return (1 - v) ** 2 - v**2 * (1 - u) * (1 - w)


def one_step_barrier(u, v):
    r"""Return ``B = 1 - v(2-u)``.

    ``B >= 0`` is equivalent to

    .. math::

       1-u \le \frac{1-v}{v}

    for ``v > 0``.
    """

    return 1 - v * (2 - u)


def curvature_order_gap(v, w):
    """Return the forward curvature-order gap ``w-v``."""

    return w - v


def cubic_floor(v):
    """Return the non-negative cubic floor ``(1-v)^3``."""

    return (1 - v) ** 3


def decomposed_margin(u, v, w):
    r"""Return the G022 exact decomposition of the G006 margin.

    .. math::

       M=(1-v)^3
       +v(1-w)[1-v(2-u)]
       +v(1-v)(w-v).

    The expression is identically equal to :func:`pf3_margin`.
    """

    return (
        cubic_floor(v)
        + v * (1 - w) * one_step_barrier(u, v)
        + v * (1 - v) * curvature_order_gap(v, w)
    )


def barrier_certificate(u, v, w) -> dict[str, object]:
    """Evaluate the exact sufficient-condition certificate.

    The certificate proves the *single solid G006 minor* positive when
    ``0 < v < 1``, ``v <= w <= 1``, and ``1-v(2-u) >= 0``.  No assertion about
    all indices or all order-three Toeplitz minors is made here.
    """

    margin = pf3_margin(u, v, w)
    decomposed = decomposed_margin(u, v, w)
    barrier = one_step_barrier(u, v)
    order_gap = curvature_order_gap(v, w)
    floor = cubic_floor(v)
    assumptions = bool(0 < v < 1 and v <= w <= 1 and barrier >= 0)
    return {
        "margin": margin,
        "decomposed_margin": decomposed,
        "decomposition_residual": margin - decomposed,
        "barrier": barrier,
        "order_gap": order_gap,
        "cubic_floor": floor,
        "assumptions_hold": assumptions,
        "solid_minor_certified_positive": bool(assumptions and margin >= floor > 0),
    }
