"""Exact Riemann-kernel utilities for the SOH-G003 proof frontier.

The formulas here are derived from the canonical theta--Mellin representation
already used by the monograph. Numerical quadrature is a regression aid only;
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


def modular_density(x: float | mp.mpf, *, n_terms: int = 8) -> mp.mpf:
    r"""Return the positive density after the exact substitution ``x=e^(2y)``.

    For ``x >= 1`` define

    .. math::

       D(x)=\sum_{n\ge1}\pi n^2 x^{1/4}
       (2\pi n^2x-3)e^{-\pi n^2x}.

    Then

    .. math::

       \xi(1/2+z)=\int_1^\infty D(x)
       \left(x^{z/2}+x^{-z/2}\right)\,dx.

    The two Mellin channels are exchanged by ``x -> 1/x``.  The implementation
    is restricted to the quotient representative ``x >= 1``.
    """

    if n_terms < 1:
        raise ValueError("n_terms must be positive")
    x = mp.mpf(x)
    if x < 1:
        raise ValueError("modular_density uses the quotient representative x >= 1")

    total = mp.mpf("0")
    x_quarter = mp.power(x, mp.mpf("0.25"))
    for n in range(1, n_terms + 1):
        a = mp.pi * n * n
        total += a * x_quarter * (2 * a * x - 3) * mp.exp(-a * x)
    return total


def compactified_radius_from_x(x: float | mp.mpf) -> mp.mpf:
    r"""Map ``x in [1, infinity)`` to the compact radius ``eta in [0, 1)``.

    The full positive-line involution ``x -> 1/x`` becomes ``eta -> -eta`` for
    ``eta=(x-1)/(x+1)``.  On the quotient ``x >= 1`` only ``eta >= 0`` is needed.
    """

    x = mp.mpf(x)
    if x <= 0:
        raise ValueError("x must be positive")
    return (x - 1) / (x + 1)


def x_from_compactified_radius(eta: float | mp.mpf) -> mp.mpf:
    """Inverse ``eta -> x`` for ``-1 < eta < 1``."""

    eta = mp.mpf(eta)
    if not (-1 < eta < 1):
        raise ValueError("eta must satisfy -1 < eta < 1")
    return (1 + eta) / (1 - eta)


def compactified_kernel_weight(
    eta: float | mp.mpf, *, n_terms: int = 8
) -> mp.mpf:
    r"""Positive compactified kernel weight on ``0 <= eta < 1``.

    With

    .. math::

       x=\frac{1+\eta}{1-\eta},\qquad y=\operatorname{artanh}\eta,

    the exact kernel representation becomes

    .. math::

       \xi(1/2+z)=\int_0^1 W(\eta)
       \cosh\!\left(z\operatorname{artanh}\eta\right)d\eta,

    where

    .. math::

       W(\eta)=\frac{4D(x(\eta))}{(1-\eta)^2}>0.

    Thus ``eta=0`` is the modular self-dual point ``x=1`` and ``eta -> 1`` is
    the compactified ``x -> infinity`` boundary.
    """

    eta = mp.mpf(eta)
    if not (0 <= eta < 1):
        raise ValueError("compactified kernel uses 0 <= eta < 1")
    x = x_from_compactified_radius(eta)
    return 4 * modular_density(x, n_terms=n_terms) / (1 - eta) ** 2


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


def xi_from_compactified_kernel(
    z: complex | mp.mpf | mp.mpc,
    *,
    n_terms: int = 8,
    y_cutoff: float | mp.mpf = 4,
) -> mp.mpc:
    r"""Evaluate the same finite numerical kernel integral in compact radius.

    ``eta=tanh(y)`` maps the finite regression cutoff ``y_cutoff`` to
    ``eta_cutoff=tanh(y_cutoff)``.  Equality with :func:`xi_from_kernel` is an
    exact change of variables; the finite controls remain numerical only.
    """

    z = mp.mpc(z)
    cutoff = mp.mpf(y_cutoff)
    if cutoff <= 0:
        raise ValueError("y_cutoff must be positive")
    eta_cutoff = mp.tanh(cutoff)
    breakpoints = [mp.mpf("0"), mp.tanh(mp.mpf("0.5")), mp.tanh(mp.mpf("1")), mp.tanh(mp.mpf("2"))]
    breakpoints = [point for point in breakpoints if point < eta_cutoff]
    breakpoints.append(eta_cutoff)
    return mp.quad(
        lambda eta: compactified_kernel_weight(eta, n_terms=n_terms)
        * mp.cosh(z * mp.atanh(eta)),
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
