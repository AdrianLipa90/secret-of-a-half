"""SOH-G024 v0.5: radial q-gate / zero-touch geometry.

For a real entire function f define

    Q_x(q) = 1/2 f(x+i sqrt(q)) f(x-i sqrt(q))
           = 1/2 |f(x+i sqrt(q))|^2,   q >= 0.

The first q-derivative is the complex Laguerre-I radial response.  For the
Riemann Xi function, non-negativity of this response throughout the critical
q-strip is an RH-equivalent criterion.  This module records exact identities
and deterministic diagnostics only; it does not claim RH.
"""

from __future__ import annotations

from collections.abc import Callable

import mpmath as mp

ComplexFn = Callable[[mp.mpc], mp.mpc]


def q_partition(f: ComplexFn, x: float | mp.mpf, q: float | mp.mpf) -> mp.mpc:
    r"""Return ``Q_x(q)=1/2 f(x+i sqrt(q)) f(x-i sqrt(q))`` for ``q>=0``."""
    x = mp.mpf(x)
    q = mp.mpf(q)
    if q < 0:
        raise ValueError("q must be non-negative")
    y = mp.sqrt(q)
    return mp.mpf("0.5") * f(mp.mpc(x, y)) * f(mp.mpc(x, -y))


def radial_response(f: ComplexFn, x: float | mp.mpf, q: float | mp.mpf) -> mp.mpf:
    r"""Return the exact first-q response ``dQ_x/dq``.

    For q>0 and z=x+i sqrt(q),

        Q_q = -Im(f'(z) conjugate(f(z))) / (2 sqrt(q)).

    At q=0 the analytic limit is one half of the first real Laguerre gate,

        Q_q(x,0) = 1/2 (f'(x)^2 - f(x) f''(x)).
    """
    x = mp.mpf(x)
    q = mp.mpf(q)
    if q < 0:
        raise ValueError("q must be non-negative")
    if q == 0:
        z = mp.mpc(x)
        fv = f(z)
        fp = mp.diff(f, z, 1)
        fpp = mp.diff(f, z, 2)
        return mp.re(mp.mpf("0.5") * (fp * fp - fv * fpp))
    y = mp.sqrt(q)
    z = mp.mpc(x, y)
    fv = f(z)
    fp = mp.diff(f, z, 1)
    return -mp.im(fp * mp.conj(fv)) / (2 * y)


def complex_laguerre_I(f: ComplexFn, x: float | mp.mpf, y: float | mp.mpf) -> mp.mpf:
    r"""Return ``Im(-f'(z) conjugate(f(z)))/y`` for y != 0.

    This equals ``2 * radial_response(f, x, y**2)``.
    """
    x = mp.mpf(x)
    y = mp.mpf(y)
    if y == 0:
        raise ValueError("complex Laguerre-I quotient requires y != 0")
    z = mp.mpc(x, y)
    return mp.im(-mp.diff(f, z, 1) * mp.conj(f(z))) / y


def hermitian_jensen(f: ComplexFn, x: float | mp.mpf, y: float | mp.mpf) -> mp.mpf:
    r"""Return ``H=|f'|^2-Re(f'' conjugate(f))`` at ``z=x+i y``."""
    z = mp.mpc(x, y)
    fv = f(z)
    fp = mp.diff(f, z, 1)
    fpp = mp.diff(f, z, 2)
    return abs(fp) ** 2 - mp.re(fpp * mp.conj(fv))


def hermitian_from_q(f: ComplexFn, x: float | mp.mpf, q: float | mp.mpf) -> mp.mpf:
    r"""Return the q-form of the Hermitian curvature.

        H(x+i sqrt(q)) = 2 Q_q + 4 q Q_qq.
    """
    x = mp.mpf(x)
    q = mp.mpf(q)
    if q < 0:
        raise ValueError("q must be non-negative")
    qp = radial_response(f, x, q)
    if q == 0:
        return 2 * qp
    qpp = mp.diff(lambda s: q_partition(f, x, s), q, 2)
    return mp.re(2 * qp + 4 * q * qpp)


def q_laplacian_residual(
    f: ComplexFn, x: float | mp.mpf, q: float | mp.mpf
) -> mp.mpf:
    r"""Residual of the exact subharmonicity identity.

        Q_xx + 2 Q_q + 4 q Q_qq = 2 |f'(x+i sqrt(q))|^2.

    Here Q is one half of |f|^2.
    """
    x = mp.mpf(x)
    q = mp.mpf(q)
    if q <= 0:
        raise ValueError("q must be positive for this numerical residual")
    q_xx = mp.diff(lambda xx: q_partition(f, xx, q), x, 2)
    q_q = radial_response(f, x, q)
    q_qq = mp.diff(lambda s: q_partition(f, x, s), q, 2)
    z = mp.mpc(x, mp.sqrt(q))
    rhs = 2 * abs(mp.diff(f, z, 1)) ** 2
    return mp.re(q_xx + 2 * q_q + 4 * q * q_qq - rhs)


def touchdown_leading_coefficient(
    f: ComplexFn,
    x0: float | mp.mpf,
    y0: float | mp.mpf,
    multiplicity: int,
) -> mp.mpf:
    r"""Leading q-touch coefficient at a declared off-axis zero.

    If z0=x0+i y0, y0!=0, is a zero of multiplicity m and

        a = f^(m)(z0)/m!,

    then along the fixed vertical line x=x0,

        Q_x0(q) =
          |a|^2 / (2 (2|y0|)^(2m)) * (q-y0^2)^(2m)
          + higher order terms.

    This helper returns the displayed positive leading coefficient.  The caller
    is responsible for establishing the zero and its multiplicity.
    """
    if not isinstance(multiplicity, int) or multiplicity < 1:
        raise ValueError("multiplicity must be a positive integer")
    x0 = mp.mpf(x0)
    y0 = mp.mpf(y0)
    if y0 == 0:
        raise ValueError("touchdown formula is for an off-axis zero")
    z0 = mp.mpc(x0, y0)
    a = mp.diff(f, z0, multiplicity) / mp.factorial(multiplicity)
    return abs(a) ** 2 / (2 * (2 * abs(y0)) ** (2 * multiplicity))


def off_axis_control(z: complex | mp.mpf | mp.mpc) -> mp.mpc:
    """Simple real-entire control with zeros at +/-i."""
    z = mp.mpc(z)
    return z * z + 1


def gaussian_control(z: complex | mp.mpf | mp.mpc) -> mp.mpc:
    """Zero-free real entire LP control."""
    z = mp.mpc(z)
    return mp.exp(-(z * z) / 2)
