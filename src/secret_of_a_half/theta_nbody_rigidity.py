"""Theta/N-body rigidity diagnostics for the Secret-of-a-Half project.

This module separates exact identities from finite numerical diagnostics.
Nothing here proves or disproves RH. In particular, the external bilinear
Dimitrov--Xu quantity and the internal Hermitian Jensen quantity are kept
as distinct objects throughout.
"""

from __future__ import annotations

from collections.abc import Callable

import mpmath as mp

ComplexFn = Callable[[mp.mpc], mp.mpc]


def completed_xi(s: complex | mp.mpf | mp.mpc) -> mp.mpc:
    """Completed Riemann xi function."""
    s = mp.mpc(s)
    return (
        mp.mpf("0.5")
        * s
        * (s - 1)
        * mp.power(mp.pi, -s / 2)
        * mp.gamma(s / 2)
        * mp.zeta(s)
    )


def xi_fourier_entire(z: complex | mp.mpf | mp.mpc) -> mp.mpc:
    r"""Return ``Xi(z)=xi(1/2+i z)`` as an entire function of ``z``."""
    z = mp.mpc(z)
    return completed_xi(mp.mpf("0.5") + 1j * z)


def riemann_halfline_kernel(t: float | mp.mpf, *, n_terms: int = 8) -> mp.mpf:
    r"""Canonical positive Riemann half-line kernel ``Phi(t)`` for ``t>=0``.

    This matches the repository normalization

        Xi(z) = int_0^infinity Phi(t) cos(z t) dt.

    ``n_terms`` is a numerical truncation control only.
    """
    if n_terms < 1:
        raise ValueError("n_terms must be positive")
    t = mp.mpf(t)
    if t < 0:
        raise ValueError("t must be non-negative")
    e2 = mp.exp(2 * t)
    e5 = mp.exp(mp.mpf("2.5") * t)
    total = mp.mpf("0")
    for n in range(1, n_terms + 1):
        a = mp.pi * n * n
        total += 4 * a * e5 * (2 * a * e2 - 3) * mp.exp(-a * e2)
    return total


def _breakpoints(cutoff: mp.mpf) -> list[mp.mpf]:
    pts = [mp.mpf("0"), mp.mpf("0.5"), mp.mpf("1"), mp.mpf("2")]
    pts = [p for p in pts if p < cutoff]
    pts.append(cutoff)
    return pts


def kernel_mgf_real(
    lam: float | mp.mpf,
    *,
    n_terms: int = 8,
    cutoff: float | mp.mpf = 4,
) -> mp.mpf:
    r"""Full-line MGF ``M(lam)=int K(t)e^(lam t)dt`` for real ``lam``.

    With ``K(t)=Phi(|t|)/2`` this is

        M(lam) = int_0^infinity Phi(t) cosh(lam t) dt.
    """
    lam = mp.mpf(lam)
    cutoff = mp.mpf(cutoff)
    if cutoff <= 0:
        raise ValueError("cutoff must be positive")
    return mp.quad(
        lambda t: riemann_halfline_kernel(t, n_terms=n_terms) * mp.cosh(lam * t),
        _breakpoints(cutoff),
    )


def kernel_mgf_derivatives_real(
    lam: float | mp.mpf,
    *,
    n_terms: int = 8,
    cutoff: float | mp.mpf = 4,
) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
    r"""Return ``(M,M',M'')`` by differentiating under the kernel integral."""
    lam = mp.mpf(lam)
    cutoff = mp.mpf(cutoff)
    pts = _breakpoints(cutoff)
    M = mp.quad(
        lambda t: riemann_halfline_kernel(t, n_terms=n_terms) * mp.cosh(lam * t),
        pts,
    )
    Mp = mp.quad(
        lambda t: riemann_halfline_kernel(t, n_terms=n_terms) * t * mp.sinh(lam * t),
        pts,
    )
    Mpp = mp.quad(
        lambda t: riemann_halfline_kernel(t, n_terms=n_terms) * t * t * mp.cosh(lam * t),
        pts,
    )
    return M, Mp, Mpp


def log_mgf_curvature_real(
    lam: float | mp.mpf,
    *,
    n_terms: int = 8,
    cutoff: float | mp.mpf = 4,
) -> mp.mpf:
    r"""Return ``d^2/dlam^2 log M(lam)``.

    For the positive non-degenerate kernel this is a variance and is strictly
    positive in exact mathematics. The finite quadrature is diagnostic only.
    """
    M, Mp, Mpp = kernel_mgf_derivatives_real(lam, n_terms=n_terms, cutoff=cutoff)
    return Mpp / M - (Mp / M) ** 2


def theta_transverse_potential(
    y: float | mp.mpf,
    *,
    n_terms: int = 8,
    cutoff: float | mp.mpf = 4,
) -> mp.mpf:
    r"""Canonical even-kernel transverse potential.

        V_Theta(y) = log(M(y)M(-y)/M(0)^2).

    Since the full kernel is even, ``M(-y)=M(y)``. Exact Cauchy--Schwarz
    gives ``V_Theta>=0`` with equality only at ``y=0`` for non-degenerate K.
    """
    y = mp.mpf(y)
    M0 = kernel_mgf_real(0, n_terms=n_terms, cutoff=cutoff)
    Mp = kernel_mgf_real(y, n_terms=n_terms, cutoff=cutoff)
    Mm = kernel_mgf_real(-y, n_terms=n_terms, cutoff=cutoff)
    return mp.log(Mp * Mm / (M0 * M0))


def nbody_partition_real(
    alpha: float | mp.mpf,
    beta: float | mp.mpf,
    *,
    n_terms: int = 8,
    cutoff: float | mp.mpf = 4,
) -> mp.mpf:
    r"""Two-body generating function ``Z=1/2 M(a+b)M(a-b)``."""
    alpha = mp.mpf(alpha)
    beta = mp.mpf(beta)
    return mp.mpf("0.5") * kernel_mgf_real(
        alpha + beta, n_terms=n_terms, cutoff=cutoff
    ) * kernel_mgf_real(alpha - beta, n_terms=n_terms, cutoff=cutoff)


def nbody_log_partition_hessian_real(
    alpha: float | mp.mpf,
    beta: float | mp.mpf,
    *,
    n_terms: int = 8,
    cutoff: float | mp.mpf = 4,
) -> tuple[mp.mpf, mp.mpf, mp.mpf, mp.mpf]:
    r"""Return ``(F_aa,F_ab,F_bb,det Hessian)`` for ``F=log Z``.

    Exact identities:

        F_aa = h''(a+b)+h''(a-b)
        F_bb = F_aa
        F_ab = h''(a+b)-h''(a-b)
        det   = 4 h''(a+b) h''(a-b).
    """
    alpha = mp.mpf(alpha)
    beta = mp.mpf(beta)
    hp = log_mgf_curvature_real(alpha + beta, n_terms=n_terms, cutoff=cutoff)
    hm = log_mgf_curvature_real(alpha - beta, n_terms=n_terms, cutoff=cutoff)
    faa = hp + hm
    fab = hp - hm
    fbb = faa
    det = 4 * hp * hm
    return faa, fab, fbb, det


def external_bilinear_value(f: ComplexFn, z: complex | mp.mpc) -> mp.mpf:
    r"""External bilinear Laguerre/Wronskian quantity.

        E(z) = Re(f'(z)^2 - f(z) f''(z)).
    """
    z = mp.mpc(z)
    fv = f(z)
    fp = mp.diff(f, z, 1)
    fpp = mp.diff(f, z, 2)
    return mp.re(fp * fp - fv * fpp)


def hermitian_jensen_value(f: ComplexFn, z: complex | mp.mpc) -> mp.mpf:
    r"""Complex/Hermitian Laguerre--Jensen quantity.

        H(z) = |f'(z)|^2 - Re(f''(z) conjugate(f(z))).
    """
    z = mp.mpc(z)
    fv = f(z)
    fp = mp.diff(f, z, 1)
    fpp = mp.diff(f, z, 2)
    return abs(fp) ** 2 - mp.re(fpp * mp.conj(fv))


def tent_kernel(t: float | mp.mpf) -> mp.mpf:
    r"""Positive tent kernel with transform ``(sin z/z)^2``."""
    t = abs(mp.mpf(t))
    if t > 2:
        return mp.mpf("0")
    return (2 - t) / 4


def tent_transform(z: complex | mp.mpf | mp.mpc) -> mp.mpc:
    r"""Entire transform of :func:`tent_kernel`."""
    z = mp.mpc(z)
    if abs(z) < mp.mpf("1e-30"):
        return mp.mpc(1)
    return (mp.sin(z) / z) ** 2


def tent_nu2(t: float | mp.mpf) -> mp.mpf:
    r"""Exact order-two correlation for the tent kernel.

    For ``a=|t|``:

      * 0 <= a <= 2:
        ``(3a^5-20a^4+80a^3-160a^2+256)/480``;
      * 2 <= a <= 4: ``(4-a)^5/480``;
      * otherwise zero.

    The polynomial was obtained by exact piecewise integration of
    ``int (t-2s)^2 K(t-s)K(s) ds``.
    """
    a = abs(mp.mpf(t))
    if a > 4:
        return mp.mpf("0")
    if a <= 2:
        return (3 * a**5 - 20 * a**4 + 80 * a**3 - 160 * a**2 + 256) / 480
    return (4 - a) ** 5 / 480


def tent_external_tilt_fourier(x: float | mp.mpf, y: float | mp.mpf) -> mp.mpf:
    r"""Fourier transform of ``cosh(y t) nu_2(t)`` for the tent kernel."""
    x = mp.mpf(x)
    y = mp.mpf(y)
    return 2 * (
        mp.quad(lambda t: mp.cosh(y * t) * tent_nu2(t) * mp.cos(x * t), [0, 2])
        + mp.quad(lambda t: mp.cosh(y * t) * tent_nu2(t) * mp.cos(x * t), [2, 4])
    )


def riemann_external_bilinear(x: float | mp.mpf, y: float | mp.mpf) -> mp.mpf:
    return external_bilinear_value(xi_fourier_entire, mp.mpc(x, y))


def riemann_hermitian_jensen(x: float | mp.mpf, y: float | mp.mpf) -> mp.mpf:
    return hermitian_jensen_value(xi_fourier_entire, mp.mpc(x, y))
