"""Exact Riemann-kernel utilities for the SOH-G003 proof frontier.

The formulas here are derived from the canonical theta--Mellin representation
already used by the monograph.  Numerical quadrature is a regression aid only;
real-rootedness of the quotient entire function remains an open theorem target.
"""

from __future__ import annotations

import mpmath as mp


def completed_xi(s: complex | mp.mpf | mp.mpc) -> mp.mpc:
    """Return the completed Riemann xi function."""

    s = mp.mpc(s)
    return (
        mp.mpf("0.5")
        * s
        * (s - 1)
        * mp.power(mp.pi, -s / 2)
        * mp.gamma(s / 2)
        * mp.zeta(s)
    )


def riemann_kernel(y: float | mp.mpf, *, n_terms: int = 8) -> mp.mpf:
    r"""Evaluate the positive half-line kernel

    .. math::

       \Phi(y)=4\sum_{n\ge1}\pi n^2e^{5y/2}
       (2\pi n^2e^{2y}-3)e^{-\pi n^2e^{2y}}.

    ``n_terms`` truncates only the numerical evaluation; every individual term
    is positive for ``y >= 0``.
    """

    if n_terms < 1:
        raise ValueError("n_terms must be positive")
    y = mp.mpf(y)
    if y < 0:
        raise ValueError("riemann_kernel is defined here on y >= 0")

    exp2y = mp.exp(2 * y)
    exp5y2 = mp.exp(mp.mpf("2.5") * y)
    total = mp.mpf("0")
    for n in range(1, n_terms + 1):
        a = mp.pi * n * n
        total += (
            4
            * a
            * exp5y2
            * (2 * a * exp2y - 3)
            * mp.exp(-a * exp2y)
        )
    return total


def xi_from_kernel(
    z: complex | mp.mpf | mp.mpc,
    *,
    n_terms: int = 8,
    y_cutoff: float | mp.mpf = 4,
) -> mp.mpc:
    r"""Numerically evaluate ``xi(1/2 + z)`` from the positive kernel.

    The exact identity is

    .. math::

       \xi(1/2+z)=\int_0^\infty \Phi(y)\cosh(zy)\,dy.

    The finite ``n_terms`` and ``y_cutoff`` are numerical regression controls,
    not part of the analytic statement.
    """

    z = mp.mpc(z)
    cutoff = mp.mpf(y_cutoff)
    if cutoff <= 0:
        raise ValueError("y_cutoff must be positive")

    breakpoints = [mp.mpf("0"), mp.mpf("0.5"), mp.mpf("1"), mp.mpf("2")]
    breakpoints = [point for point in breakpoints if point < cutoff]
    breakpoints.extend([cutoff])
    return mp.quad(
        lambda y: riemann_kernel(y, n_terms=n_terms) * mp.cosh(z * y),
        breakpoints,
    )


def even_moment(order: int, *, n_terms: int = 8, y_cutoff: float = 4) -> mp.mpf:
    r"""Return the numerical even moment ``mu_{2*order}`` of ``Phi``."""

    if not isinstance(order, int) or order < 0:
        raise ValueError("order must be a non-negative integer")
    cutoff = mp.mpf(y_cutoff)
    return mp.quad(
        lambda y: riemann_kernel(y, n_terms=n_terms) * y ** (2 * order),
        [0, mp.mpf("0.5"), mp.mpf("1"), mp.mpf("2"), cutoff],
    )
