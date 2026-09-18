"""SOH-G024 v0.7: zero-shadow decomposition and harmonic lift.

Exact identities for the normalized radial q-gate

    R_f(x,q) = d_q log(1/2 |f(x+i sqrt(q))|^2).

Nothing here proves RH.
"""
from __future__ import annotations

from collections.abc import Callable
import mpmath as mp

ComplexFn = Callable[[mp.mpc], mp.mpc]


def normalized_radial_gate(
    f: ComplexFn, x: float | mp.mpf, q: float | mp.mpf
) -> mp.mpf:
    r"""Return ``d_q log Q_x(q)`` for ``Q=|f(x+i sqrt(q))|^2/2``.

    Away from zeros and for q>0,

        R_f(x,q) = -Im(f'(z)/f(z))/sqrt(q), z=x+i sqrt(q).
    """
    x = mp.mpf(x)
    q = mp.mpf(q)
    if q <= 0:
        raise ValueError("q must be positive")
    y = mp.sqrt(q)
    z = mp.mpc(x, y)
    fv = f(z)
    if fv == 0:
        raise ZeroDivisionError("normalized radial gate is singular at a zero")
    fp = mp.diff(f, z, 1)
    return -mp.im(fp / fv) / y


def conjugate_pair_shadow(
    x: float | mp.mpf,
    q: float | mp.mpf,
    u: float | mp.mpf,
    v: float | mp.mpf,
) -> mp.mpf:
    r"""Contribution of zeros ``u±iv`` to the normalized radial gate.

    For y=sqrt(q),

        S_{u,v}(x,y)
        = 2((x-u)^2+y^2-v^2)
          / [((x-u)^2+(y-v)^2)((x-u)^2+(y+v)^2)].

    Its sign is the sign of ``(x-u)^2+q-v^2`` away from the zero shell.
    """
    x = mp.mpf(x)
    q = mp.mpf(q)
    u = mp.mpf(u)
    v = abs(mp.mpf(v))
    if q <= 0:
        raise ValueError("q must be positive")
    y = mp.sqrt(q)
    dx = x - u
    dminus = dx * dx + (y - v) ** 2
    dplus = dx * dx + (y + v) ** 2
    if dminus == 0:
        raise ZeroDivisionError("shadow kernel is singular on the zero shell")
    return 2 * (dx * dx + q - v * v) / (dminus * dplus)


def real_pair_shadow(
    x: float | mp.mpf,
    q: float | mp.mpf,
    u: float | mp.mpf,
) -> mp.mpf:
    r"""Contribution of real zeros ``±u`` to the normalized radial gate."""
    x = mp.mpf(x)
    q = mp.mpf(q)
    u = abs(mp.mpf(u))
    if q <= 0:
        raise ValueError("q must be positive")
    return 1 / ((x - u) ** 2 + q) + 1 / ((x + u) ** 2 + q)


def quartet_shadow(
    x: float | mp.mpf,
    q: float | mp.mpf,
    u: float | mp.mpf,
    v: float | mp.mpf,
) -> mp.mpf:
    r"""Contribution of the quartet ``±(u±iv)``."""
    return conjugate_pair_shadow(x, q, u, v) + conjugate_pair_shadow(x, q, -mp.mpf(u), v)


def quartet_control_entire(
    u: float | mp.mpf, v: float | mp.mpf
) -> ComplexFn:
    r"""Return the real-even quartic with zeros ``±(u±iv)``."""
    a = mp.mpc(u, v)
    aa = a * a
    cc = mp.conj(a) * mp.conj(a)

    def f(z: mp.mpc) -> mp.mpc:
        z = mp.mpc(z)
        return (1 - z * z / aa) * (1 - z * z / cc)

    return f


def pair_control_entire(
    u: float | mp.mpf, v: float | mp.mpf
) -> ComplexFn:
    r"""Return the real quadratic with zeros ``u±iv``."""
    u = mp.mpf(u)
    v = mp.mpf(v)

    def f(z: mp.mpc) -> mp.mpc:
        z = mp.mpc(z)
        return (z - mp.mpc(u, v)) * (z - mp.mpc(u, -v))

    return f


def harmonic_lift_residual(
    f: ComplexFn, x: float | mp.mpf, q: float | mp.mpf
) -> mp.mpf:
    r"""Numerically evaluate the exact PDE residual

        R_xx + 6 R_q + 4 q R_qq = 0,

    valid away from zeros for ``R=d_q log Q``.
    """
    x = mp.mpf(x)
    q = mp.mpf(q)
    R = lambda xx, qq: normalized_radial_gate(f, xx, qq)
    rxx = mp.diff(lambda xx: R(xx, q), x, 2)
    rq = mp.diff(lambda qq: R(x, qq), q, 1)
    rqq = mp.diff(lambda qq: R(x, qq), q, 2)
    return rxx + 6 * rq + 4 * q * rqq


def completed_xi(s: complex | mp.mpf | mp.mpc) -> mp.mpc:
    """Completed Riemann xi function, with removable endpoints handled."""
    s = mp.mpc(s)
    if abs(s) < mp.mpf("1e-40"):
        return mp.mpc(mp.mpf("0.5"))
    if abs(s - 1) < mp.mpf("1e-40"):
        return mp.mpc(mp.mpf("0.5"))
    return (
        mp.mpf("0.5")
        * s
        * (s - 1)
        * mp.power(mp.pi, -s / 2)
        * mp.gamma(s / 2)
        * mp.zeta(s)
    )


def xi_fourier_entire(z: complex | mp.mpf | mp.mpc) -> mp.mpc:
    """Xi(z)=xi(1/2+i z)."""
    z = mp.mpc(z)
    return completed_xi(mp.mpf("0.5") + 1j * z)
