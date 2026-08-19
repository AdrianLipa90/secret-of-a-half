"""SOH-G024 Jensen--Wiener correlation-kernel utilities.

Exact identities are separated from numerical regression helpers. Nothing in
this module promotes RH, SOH-G003, PF3, or PF-infinity.
"""

from __future__ import annotations

from collections.abc import Callable

import mpmath as mp

from .riemann_kernel import riemann_kernel

EvenKernel = Callable[[mp.mpf], mp.mpf]

# SOH-G004 proves, with explicit rational estimates, that every theta-channel
# logarithmic curvature is below -12 while the mixture slope variance is below
# 2. Therefore (log Phi)'' < -10 on the half-line. The even full-line kernel
# K(t)=Phi(|t|)/2 inherits the strong log-concavity margin m=10.
G004_STRONG_LOG_CONCAVITY_MARGIN = mp.mpf("10")
G024_FIRST_ORDER_CM_UNIFORM_FLOOR = mp.mpf("9.5")


def full_xi_kernel(t: float | mp.mpf, *, n_terms: int = 8) -> mp.mpf:
    r"""Return the even full-line kernel whose Fourier transform is Xi.

    The repository normalization is

        xi(1/2+z) = int_0^infty Phi(t) cosh(z t) dt.

    Hence K(t)=Phi(|t|)/2 satisfies

        Xi(x)=xi(1/2+i x)=int_R K(t) exp(-i x t) dt.

    ``n_terms`` affects numerical evaluation only.
    """

    return mp.mpf("0.5") * riemann_kernel(abs(mp.mpf(t)), n_terms=n_terms)


def csordas_correlation_from_kernel(
    u: float | mp.mpf,
    *,
    kernel: EvenKernel,
    center_cutoff: float | mp.mpf = 4,
) -> mp.mpf:
    r"""Numerically evaluate

        C(u) = int_R r^2 K(u+r) K(u-r) dr.

    For an even kernel the integrand is even in ``r``. The finite cutoff is a
    regression control, not part of the analytic definition.
    """

    u = mp.mpf(u)
    cutoff = mp.mpf(center_cutoff)
    if cutoff <= 0:
        raise ValueError("center_cutoff must be positive")
    return 2 * mp.quad(
        lambda r: r * r * kernel(u + r) * kernel(u - r),
        [0, cutoff],
    )


def csordas_correlation(
    u: float | mp.mpf,
    *,
    n_terms: int = 8,
    center_cutoff: float | mp.mpf = 4,
) -> mp.mpf:
    """Riemann-kernel specialization of :func:`csordas_correlation_from_kernel`."""

    return csordas_correlation_from_kernel(
        u,
        kernel=lambda t: full_xi_kernel(t, n_terms=n_terms),
        center_cutoff=center_cutoff,
    )


def dimitrov_xu_tilted_from_kernel(
    u: float | mp.mpf,
    y: float | mp.mpf,
    *,
    kernel: EvenKernel,
    center_cutoff: float | mp.mpf = 4,
) -> mp.mpf:
    r"""Return the reparametrized Dimitrov--Xu order-two kernel.

    If

        nu_2(t)=int_R (t-2s)^2 K(t-s)K(s) ds,

    then the exact substitution ``t=2u, s=u-r`` gives

        nu_2(2u)=4 C(u).

    Therefore their tilted kernel ``cosh(t y) nu_2(t)`` is, up to the positive
    factor four and the harmless dilation ``t=2u``,

        D_y(u)=cosh(2 y u) C(u).
    """

    u = mp.mpf(u)
    y = mp.mpf(y)
    return mp.cosh(2 * y * u) * csordas_correlation_from_kernel(
        u,
        kernel=kernel,
        center_cutoff=center_cutoff,
    )


def dimitrov_xu_tilted(
    u: float | mp.mpf,
    y: float | mp.mpf,
    *,
    n_terms: int = 8,
    center_cutoff: float | mp.mpf = 4,
) -> mp.mpf:
    """Riemann-kernel specialization of :func:`dimitrov_xu_tilted_from_kernel`."""

    return dimitrov_xu_tilted_from_kernel(
        u,
        y,
        kernel=lambda t: full_xi_kernel(t, n_terms=n_terms),
        center_cutoff=center_cutoff,
    )


def radial_square_profile(
    q: float | mp.mpf,
    y: float | mp.mpf,
    *,
    n_terms: int = 8,
    center_cutoff: float | mp.mpf = 4,
) -> mp.mpf:
    r"""Return H_y(q)=D_y(sqrt(q)) for q>=0.

    SOH-G024 proves the first complete-monotonicity inequality ``H_y' < 0``
    globally for the actual Riemann kernel and every ``0<|y|<1/2``. Higher
    derivative orders remain open.
    """

    q = mp.mpf(q)
    if q < 0:
        raise ValueError("q must be non-negative")
    return dimitrov_xu_tilted(
        mp.sqrt(q),
        y,
        n_terms=n_terms,
        center_cutoff=center_cutoff,
    )


def first_order_cm_log_slope_lower_bound(
    q: float | mp.mpf,
    y: float | mp.mpf,
    *,
    strong_log_concavity_margin: float | mp.mpf = G004_STRONG_LOG_CONCAVITY_MARGIN,
) -> mp.mpf:
    r"""Return the exact lower bound for ``-H_y'(q)/H_y(q)``.

    If ``L=-log K`` satisfies ``L'' >= m`` on the even full-line kernel, then
    strong monotonicity of ``L'`` gives

        -C'(u)/C(u) >= 2 m u,  u>0.

    Since ``H_y(q)=cosh(2 y sqrt(q)) C(sqrt(q))``, this yields

        -H_y'(q)/H_y(q)
        >= m - |y| tanh(2 |y| sqrt(q))/sqrt(q).

    The value at ``q=0`` is the continuous limit ``m-2 y^2``. For the G004
    margin ``m=10`` and ``0<|y|<1/2`` this is strictly above 19/2, proving the
    first complete-monotonicity inequality globally. This does not prove any
    higher derivative inequality.
    """

    q = mp.mpf(q)
    y_abs = abs(mp.mpf(y))
    margin = mp.mpf(strong_log_concavity_margin)
    if q < 0:
        raise ValueError("q must be non-negative")
    if not (0 <= y_abs < mp.mpf("0.5")):
        raise ValueError("require |y| < 1/2")
    if margin <= 0:
        raise ValueError("strong_log_concavity_margin must be positive")
    if q == 0:
        return margin - 2 * y_abs * y_abs
    u = mp.sqrt(q)
    return margin - y_abs * mp.tanh(2 * y_abs * u) / u


def internal_tilt_jensen_kernel_from_kernel(
    u: float | mp.mpf,
    y: float | mp.mpf,
    *,
    kernel: EvenKernel,
    center_cutoff: float | mp.mpf = 4,
) -> mp.mpf:
    r"""Numerically evaluate the distinct internal-tilt Jensen kernel

        J_y(u)=int_R r^2 cosh(2 y r) K(u+r)K(u-r) dr.

    This must not be conflated with the Dimitrov--Xu external tilt
    ``D_y(u)=cosh(2yu) C(u)``. They coincide only at ``y=0``.
    """

    u = mp.mpf(u)
    y = mp.mpf(y)
    cutoff = mp.mpf(center_cutoff)
    if cutoff <= 0:
        raise ValueError("center_cutoff must be positive")
    return 2 * mp.quad(
        lambda r: r * r * mp.cosh(2 * y * r) * kernel(u + r) * kernel(u - r),
        [0, cutoff],
    )


def signed_five_point_derivatives(
    func: Callable[[mp.mpf], mp.mpf],
    q: float | mp.mpf,
    *,
    h: float | mp.mpf = mp.mpf("0.002"),
) -> dict[int, mp.mpf]:
    r"""Return finite-difference diagnostics for ``(-1)^m f^(m)(q)``, m=1..4.

    These values are numerical diagnostics only. They are not certificates of
    complete monotonicity beyond the separately proved first-order G024 bound.
    """

    q = mp.mpf(q)
    h = mp.mpf(h)
    if h <= 0 or q <= 2 * h:
        raise ValueError("require h>0 and q>2h")

    fm2 = func(q - 2 * h)
    fm1 = func(q - h)
    f0 = func(q)
    fp1 = func(q + h)
    fp2 = func(q + 2 * h)

    d1 = (fm2 - 8 * fm1 + 8 * fp1 - fp2) / (12 * h)
    d2 = (-fp2 + 16 * fp1 - 30 * f0 + 16 * fm1 - fm2) / (12 * h**2)
    d3 = (-fm2 + 2 * fm1 - 2 * fp1 + fp2) / (2 * h**3)
    d4 = (fm2 - 4 * fm1 + 6 * f0 - 4 * fp1 + fp2) / h**4

    return {1: -d1, 2: d2, 3: -d3, 4: d4}
