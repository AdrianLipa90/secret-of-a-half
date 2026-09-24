"""Relative-moment structure behind the SOH G024 N-body Laguerre hierarchy.

This module records exact structural identities and adversarial controls.
Nothing here proves RH.

For a positive even kernel K define

    C_n(u) = int r^(2n) K(u+r) K(u-r) dr.

If -log K has curvature at least kappa>0, then every C_n is 2*kappa
strongly log-concave by strong Prekopa marginalization. For fixed u the
sequence {C_n(u)} is a Stieltjes moment sequence. The exponential generating
mixture

    B_y(u)=sum (2y)^(2n)/(2n)! C_n(u)

has non-negative Fourier transform

    hat(B_y)(2x)=1/2 |f(x+iy)|^2,

where f is the Fourier transform of K.

These unconditional properties are not sufficient for coefficientwise Fourier
positivity of every C_n. An explicit strongly log-concave oscillatory-Gaussian
control has L_2[f](x)<0.
"""

from __future__ import annotations

from collections.abc import Callable

import mpmath as mp

ComplexFn = Callable[[mp.mpc], mp.mpc]


def strong_marginal_curvature_bound(kappa: float | mp.mpf) -> mp.mpf:
    """Lower bound for ``-(log C_n)''`` from ``-(log K)'' >= kappa``."""
    kappa = mp.mpf(kappa)
    if kappa <= 0:
        raise ValueError("kappa must be positive")
    return 2 * kappa


def radial_first_gate_bound(kappa: float | mp.mpf) -> mp.mpf:
    r"""Lower bound for ``-d/dq log C_n(sqrt(q))`` on q>0.

    If C_n is even and 2*kappa strongly log-concave, integration from u=0 gives

        -(log C_n)'(u) >= 2*kappa*u,

    hence with q=u^2,

        -d/dq log C_n(sqrt(q)) >= kappa.
    """
    kappa = mp.mpf(kappa)
    if kappa <= 0:
        raise ValueError("kappa must be positive")
    return kappa


def gaussian_relative_moment(
    a: float | mp.mpf, u: float | mp.mpf, n: int
) -> mp.mpf:
    r"""Closed ``C_n`` for ``K(t)=exp(-a t^2)``.

    ``C_n(u)=exp(-2 a u^2) Gamma(n+1/2)/(2a)^(n+1/2)``.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")
    a = mp.mpf(a)
    u = mp.mpf(u)
    if a <= 0:
        raise ValueError("a must be positive")
    return mp.e ** (-2 * a * u * u) * mp.gamma(n + mp.mpf("0.5")) / (
        (2 * a) ** (n + mp.mpf("0.5"))
    )


def gaussian_B(
    a: float | mp.mpf, u: float | mp.mpf, y: float | mp.mpf
) -> mp.mpf:
    r"""Closed generating mixture B_y for the Gaussian kernel."""
    a, u, y = mp.mpf(a), mp.mpf(u), mp.mpf(y)
    return (
        mp.e ** (-2 * a * u * u)
        * mp.sqrt(mp.pi / (2 * a))
        * mp.e ** (y * y / (2 * a))
    )


def gaussian_B_fourier_2x(
    a: float | mp.mpf, x: float | mp.mpf, y: float | mp.mpf
) -> mp.mpf:
    r"""Closed ``hat(B_y)(2x)`` for the Gaussian kernel."""
    a, x, y = mp.mpf(a), mp.mpf(x), mp.mpf(y)
    return mp.pi / (2 * a) * mp.e ** ((y * y - x * x) / (2 * a))


def gaussian_fourier(
    a: float | mp.mpf, z: complex | mp.mpf | mp.mpc
) -> mp.mpc:
    """Fourier transform of ``exp(-a t^2)`` under exp(-i z t)."""
    a = mp.mpf(a)
    z = mp.mpc(z)
    return mp.sqrt(mp.pi / a) * mp.e ** (-(z * z) / (4 * a))


def oscillatory_gaussian_log_curvature_margin(
    *,
    a: float | mp.mpf | str = "0.13",
    epsilon: float | mp.mpf | str = "0.2",
    frequency: float | mp.mpf = 1,
    scale: float | mp.mpf = 40,
) -> mp.mpf:
    r"""Certified lower bound for ``-(log K_s)''``.

    Base kernel:
        K_0(t)=exp(-a t^2)(1+epsilon*cos(frequency*t)).

    Since
        d^2 log(1+eps cos(bt))/dt^2 <= eps*b^2/(1-eps),
    the base strong-log-concavity margin is
        2a - eps*b^2/(1-eps).

    ``K_s(t)=K_0(scale*t)`` multiplies this curvature by ``scale^2``.
    """
    a = mp.mpf(a)
    epsilon = mp.mpf(epsilon)
    frequency = mp.mpf(frequency)
    scale = mp.mpf(scale)
    if not (0 < epsilon < 1):
        raise ValueError("epsilon must satisfy 0<epsilon<1")
    base = 2 * a - epsilon * frequency**2 / (1 - epsilon)
    return scale**2 * base


def oscillatory_gaussian_fourier_base(
    z: complex | mp.mpf | mp.mpc,
    *,
    a: float | mp.mpf | str = "0.13",
    epsilon: float | mp.mpf | str = "0.2",
    frequency: float | mp.mpf = 1,
) -> mp.mpc:
    r"""Exact Fourier transform of the base oscillatory-Gaussian control."""
    z = mp.mpc(z)
    a = mp.mpf(a)
    epsilon = mp.mpf(epsilon)
    b = mp.mpf(frequency)
    return (
        mp.sqrt(mp.pi / a)
        * mp.e ** (-(z * z) / (4 * a))
        * (
            1
            + epsilon
            * mp.e ** (-(b * b) / (4 * a))
            * mp.cosh(b * z / (2 * a))
        )
    )


def oscillatory_gaussian_fourier_scaled(
    z: complex | mp.mpf | mp.mpc,
    *,
    scale: float | mp.mpf = 40,
    a: float | mp.mpf | str = "0.13",
    epsilon: float | mp.mpf | str = "0.2",
    frequency: float | mp.mpf = 1,
) -> mp.mpc:
    r"""Fourier transform of ``K_s(t)=K_0(scale*t)``."""
    scale = mp.mpf(scale)
    z = mp.mpc(z)
    return oscillatory_gaussian_fourier_base(
        z / scale, a=a, epsilon=epsilon, frequency=frequency
    ) / scale


def extended_laguerre_value(f: ComplexFn, x: float | mp.mpf, n: int) -> mp.mpf:
    r"""Return the standard extended Laguerre operator L_n[f](x)."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")
    z = mp.mpc(mp.mpf(x))
    derivatives = [mp.diff(f, z, k) for k in range(2 * n + 1)]
    total = mp.mpc(0)
    for k in range(2 * n + 1):
        total += (
            (-1) ** (k + n)
            * mp.binomial(2 * n, k)
            * derivatives[k]
            * derivatives[2 * n - k]
        )
    return mp.re(total / mp.factorial(2 * n))


def oscillatory_gaussian_l2_witness(
    *,
    base_x: float | mp.mpf | str = "1.222",
    scale: float | mp.mpf = 40,
) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
    r"""Return ``(L2_base, scaled_x, L2_scaled)`` for the no-go control."""
    base_x = mp.mpf(base_x)
    scale = mp.mpf(scale)
    f0 = lambda z: oscillatory_gaussian_fourier_base(z)
    fs = lambda z: oscillatory_gaussian_fourier_scaled(z, scale=scale)
    l2_base = extended_laguerre_value(f0, base_x, 2)
    scaled_x = scale * base_x
    l2_scaled = extended_laguerre_value(fs, scaled_x, 2)
    return l2_base, scaled_x, l2_scaled


def scaled_laguerre_prediction(
    base_value: float | mp.mpf, scale: float | mp.mpf, n: int
) -> mp.mpf:
    r"""Scaling law for ``f_s(z)=f_0(z/s)/s``.

    ``L_n[f_s](s*x)=s^(-2n-2)L_n[f_0](x)``.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")
    return mp.mpf(base_value) * mp.mpf(scale) ** (-2 * n - 2)
