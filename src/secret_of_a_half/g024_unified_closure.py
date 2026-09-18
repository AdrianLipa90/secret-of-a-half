"""SOH-G024 v0.6: unified radial / Laguerre / quotient-Gram closure.

This module records exact crosswalks between:
  * the first-q radial response of Q_x(q)=1/2|f(x+i sqrt(q))|^2,
  * the generating function of the extended Laguerre hierarchy,
  * the G025 square-quotient dual Gram kernels under f(z)=F(-z^2).

Nothing here proves RH.
"""

from __future__ import annotations

from collections.abc import Callable

import mpmath as mp

ComplexFn = Callable[[mp.mpc], mp.mpc]


def quotient_point(x: float | mp.mpf, q: float | mp.mpf) -> mp.mpc:
    r"""Return ``w=-(x+i sqrt(q))^2`` for ``q>=0``."""
    x = mp.mpf(x)
    q = mp.mpf(q)
    if q < 0:
        raise ValueError("q must be non-negative")
    z = mp.mpc(x, mp.sqrt(q))
    return -(z * z)


def q_from_quotient_point(w: complex | mp.mpf | mp.mpc) -> mp.mpf:
    r"""Recover ``q=y^2`` from ``w=-(x+i y)^2`` with ``y>=0``.

    Exactly ``q=(|w|+Re(w))/2``.
    """
    w = mp.mpc(w)
    return (abs(w) + mp.re(w)) / 2


def q_partition_from_quotient(
    F: ComplexFn, x: float | mp.mpf, q: float | mp.mpf
) -> mp.mpc:
    r"""Return ``Q_x(q)=1/2 F(w)F(conj(w))`` with ``w=-(x+i sqrt(q))^2``."""
    w = quotient_point(x, q)
    return mp.mpf("0.5") * F(w) * F(mp.conj(w))


def radial_response_from_quotient(
    F: ComplexFn, x: float | mp.mpf, q: float | mp.mpf
) -> mp.mpf:
    r"""Return ``dQ_x/dq`` directly in square-quotient coordinates.

    For q>0 and w=-(x+i sqrt(q))^2,

        Q_q = |F(w)|^2 [Re(phi(w)) + x/sqrt(q) Im(phi(w))],

    where phi=F'/F.  The implementation uses the pole-free numerator

        Q_q = Re(F'(w) conj(F(w)))
              + x/sqrt(q) Im(F'(w) conj(F(w))).

    At x=0 this reduces continuously to F(q)F'(q) for a real entire F.
    """
    x = mp.mpf(x)
    q = mp.mpf(q)
    if q <= 0:
        raise ValueError("q must be positive")
    y = mp.sqrt(q)
    w = quotient_point(x, q)
    Fw = F(w)
    Fp = mp.diff(F, w, 1)
    prod = Fp * mp.conj(Fw)
    return mp.re(prod) + (x / y) * mp.im(prod)


def pole_free_dual_gram_diagonals(
    F: ComplexFn, x: float | mp.mpf, q: float | mp.mpf
) -> tuple[mp.mpf, mp.mpf]:
    r"""Return the G025 pole-free diagonal pair ``(K0hat,K1hat)``.

    For non-real ``w``,

        K0hat = [w F'(w) conj(F(w)) - conj(w) F(w) conj(F'(w))]
                / (w-conj(w)),

        K1hat = [F(w) conj(F'(w)) - F'(w) conj(F(w))]
                / (w-conj(w)).

    On the positive real axis (x=0, q>0) the continuous limits are

        K0hat = F F' + w(F F'' - F'^2),
        K1hat = F'^2 - F F''.

    The exact closure identity is

        Q_q = K0hat + |w| K1hat.
    """
    x = mp.mpf(x)
    q = mp.mpf(q)
    if q <= 0:
        raise ValueError("q must be positive")
    w = quotient_point(x, q)
    Fw = F(w)
    Fp = mp.diff(F, w, 1)

    if abs(mp.im(w)) <= mp.eps * max(1, abs(w)):
        Fpp = mp.diff(F, w, 2)
        k1 = Fp * Fp - Fw * Fpp
        k0 = Fw * Fp + w * (Fw * Fpp - Fp * Fp)
        return mp.re(k0), mp.re(k1)

    den = w - mp.conj(w)
    k0 = (
        w * Fp * mp.conj(Fw)
        - mp.conj(w) * Fw * mp.conj(Fp)
    ) / den
    k1 = (
        Fw * mp.conj(Fp)
        - Fp * mp.conj(Fw)
    ) / den
    return mp.re(k0), mp.re(k1)


def dual_gram_radial_response(
    F: ComplexFn, x: float | mp.mpf, q: float | mp.mpf
) -> mp.mpf:
    r"""Return ``K0hat(w,w)+|w|K1hat(w,w)``."""
    w = quotient_point(x, q)
    k0, k1 = pole_free_dual_gram_diagonals(F, x, q)
    return k0 + abs(w) * k1


def laguerre_resummed_radial_response(
    laguerre_values: list[mp.mpf] | tuple[mp.mpf, ...],
    q: float | mp.mpf,
) -> mp.mpf:
    r"""Return ``1/2 sum_{n>=1} n L_n q^(n-1)`` for supplied finite values.

    ``laguerre_values[n]`` is L_n.  This helper is exact for a polynomial
    whose extended-Laguerre q-series terminates at the supplied order.
    """
    q = mp.mpf(q)
    total = mp.mpf("0")
    for n in range(1, len(laguerre_values)):
        total += mp.mpf("0.5") * n * mp.mpf(laguerre_values[n]) * q ** (n - 1)
    return total


def quotient_strip_membership(
    w: complex | mp.mpf | mp.mpc, *, alpha: float | mp.mpf = mp.mpf("0.5")
) -> bool:
    r"""Return whether ``w`` lies in the image of ``0<y<alpha`` under w=-z^2.

    Since q=y^2=(|w|+Re w)/2, the exact condition is

        0 < (|w|+Re w)/2 < alpha^2.
    """
    w = mp.mpc(w)
    alpha = mp.mpf(alpha)
    if alpha <= 0:
        raise ValueError("alpha must be positive")
    q = q_from_quotient_point(w)
    return bool(0 < q < alpha * alpha)
