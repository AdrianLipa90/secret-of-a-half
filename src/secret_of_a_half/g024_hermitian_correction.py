"""SOH-G024 source-convention correction and Hermitian N-body bridge.

This module is additive.  It does not alter the historical G024 implementation.
It records the corrected Fourier/Jensen channel under the convention

    F[g](x) = int_R g(t) exp(-i x t) dt.

For a real entire Fourier transform f and z=x+i y, the real odd tilted channel
has Fourier transform i*Im(f(z)), not Im(f(z)).  Consequently the Jensen
correlation uses a *difference* of the even/odd order-two correlations.  In
center/relative variables this is the internal kernel J_y, and the resulting
Hermitian Jensen quantity is the Wick-rotated relative susceptibility of the
same two-body partition function used by the theta potential.

Nothing in this module proves or disproves RH.
"""

from __future__ import annotations

from collections.abc import Callable

import mpmath as mp

from .theta_nbody_rigidity import (
    hermitian_jensen_value,
    nbody_partition_real,
    tent_kernel,
    theta_transverse_potential,
    xi_fourier_entire,
)

ComplexFn = Callable[[mp.mpc], mp.mpc]


def odd_tilt_fourier_from_entire(
    f: ComplexFn, x: float | mp.mpf, y: float | mp.mpf
) -> mp.mpc:
    r"""Return the Fourier transform of the real odd tilted channel.

    If ``f(z)=F[K](z)`` with real even ``K`` and ``z=x+i y``, then

        F[sinh(y t) K(t)](x)
            = (f(x+i y)-f(x-i y))/2
            = i Im f(x+i y).

    This exact factor ``i`` is the source-convention correction relevant to
    the historical external G024 route.
    """
    x = mp.mpf(x)
    y = mp.mpf(y)
    return (f(mp.mpc(x, y)) - f(mp.mpc(x, -y))) / 2


def gaussian_fourier_entire(z: complex | mp.mpf | mp.mpc) -> mp.mpc:
    r"""Fourier transform of ``exp(-t^2/2)`` under the repository convention."""
    z = mp.mpc(z)
    return mp.sqrt(2 * mp.pi) * mp.exp(-(z * z) / 2)


def tent_internal_j(u: float | mp.mpf, y: float | mp.mpf) -> mp.mpf:
    r"""Direct internal centered Jensen kernel for the tent control.

        J_y(u)=int r^2 cosh(2 y r) K(u+r) K(u-r) dr.

    The tent support makes the integration interval finite.
    """
    u = mp.mpf(u)
    y = mp.mpf(y)
    lo = max(-2 - u, u - 2)
    hi = min(2 - u, u + 2)
    if lo >= hi:
        return mp.mpf("0")
    points = [mp.mpf(lo)]
    for p in (mp.mpf("0"), -u, u):
        if lo < p < hi:
            points.append(p)
    points.append(mp.mpf(hi))
    points = sorted(set(points))
    return mp.quad(
        lambda r: r**2
        * mp.cosh(2 * y * r)
        * tent_kernel(u + r)
        * tent_kernel(u - r),
        points,
    )


def tent_internal_jensen_transform(
    x: float | mp.mpf, y: float | mp.mpf
) -> mp.mpf:
    r"""Return ``4 * hat(J_y)(2x)`` by direct kernel quadrature.

    Exact mathematics gives

        4 hat(J_y)(2x) = |f'(x+i y)|^2
                         - Re(f''(x+i y) conj(f(x+i y))).
    """
    x = mp.mpf(x)
    y = mp.mpf(y)
    integral = mp.quad(
        lambda u: tent_internal_j(u, y) * mp.cos(2 * x * u),
        [0, 1, 2],
    )
    return 8 * integral


def wick_rotated_partition(
    f: ComplexFn, x: float | mp.mpf, beta: float | mp.mpf
) -> mp.mpc:
    r"""Two-body partition after center-channel Wick rotation.

    For a real entire ``f`` this is

        Z(-i x,beta)=1/2 f(x+i beta)f(x-i beta)
                    =1/2 |f(x+i beta)|^2.
    """
    x = mp.mpf(x)
    beta = mp.mpf(beta)
    return mp.mpf("0.5") * f(mp.mpc(x, beta)) * f(mp.mpc(x, -beta))


def wick_rotated_relative_susceptibility(
    f: ComplexFn, x: float | mp.mpf, y: float | mp.mpf
) -> mp.mpc:
    r"""Return ``d^2/d beta^2 Z(-i x,beta)`` at ``beta=y``.

    For a real entire ``f`` the exact identity is

        d_beta^2 Z(-i x,beta)|_{beta=y}
          = |f'(x+i y)|^2-Re(f''(x+i y)conj(f(x+i y))).
    """
    x = mp.mpf(x)
    y = mp.mpf(y)
    return mp.diff(lambda beta: wick_rotated_partition(f, x, beta), y, 2)


def riemann_relative_susceptibility(
    x: float | mp.mpf, y: float | mp.mpf
) -> mp.mpc:
    """Wick-rotated relative susceptibility for the Riemann Xi entire function."""
    return wick_rotated_relative_susceptibility(xi_fourier_entire, x, y)


def theta_potential_from_partition(
    y: float | mp.mpf,
    *,
    n_terms: int = 8,
    cutoff: float | mp.mpf = 4,
) -> mp.mpf:
    r"""Return the theta potential as a two-body free-energy displacement.

        V_Theta(y)=log(Z(0,y)/Z(0,0)).
    """
    y = mp.mpf(y)
    z0 = nbody_partition_real(0, 0, n_terms=n_terms, cutoff=cutoff)
    zy = nbody_partition_real(0, y, n_terms=n_terms, cutoff=cutoff)
    return mp.log(zy / z0)


def dyadic_sinc_product_truncated(
    z: complex | mp.mpf | mp.mpc, *, n_terms: int = 80
) -> mp.mpc:
    r"""Finite numerical approximant to ``prod_{n>=1} sinc(2^-n z)``.

    The infinite product is used analytically in the research note as a smooth
    positive-kernel LP control with a double zero at ``4*pi``.  This routine is
    only a finite high-precision witness and is not the proof of those facts.
    """
    if n_terms < 1:
        raise ValueError("n_terms must be positive")
    z = mp.mpc(z)
    out = mp.mpc(1)
    for n in range(1, n_terms + 1):
        w = mp.power(2, -n) * z
        out *= mp.sin(w) / w if w != 0 else 1
    return out


def dyadic_external_and_hermitian_witness(
    x: float | mp.mpf = mp.mpf("12.38"),
    y: float | mp.mpf = mp.mpf("0.5"),
    *,
    n_terms: int = 80,
) -> tuple[mp.mpf, mp.mpf]:
    """Return finite-product external and Hermitian values at a declared witness."""
    from .theta_nbody_rigidity import external_bilinear_value

    x = mp.mpf(x)
    y = mp.mpf(y)
    f = lambda z: dyadic_sinc_product_truncated(z, n_terms=n_terms)
    z = mp.mpc(x, y)
    return external_bilinear_value(f, z), hermitian_jensen_value(f, z)


def theta_partition_identity_residual(
    y: float | mp.mpf,
    *,
    n_terms: int = 8,
    cutoff: float | mp.mpf = 4,
) -> mp.mpf:
    """Numerical residual between the two exact theta-potential expressions."""
    return theta_potential_from_partition(
        y, n_terms=n_terms, cutoff=cutoff
    ) - theta_transverse_potential(y, n_terms=n_terms, cutoff=cutoff)
