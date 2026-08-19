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
    r"""Return the even full-line kernel whose Fourier transform is Xi."""

    return mp.mpf("0.5") * riemann_kernel(abs(mp.mpf(t)), n_terms=n_terms)


def csordas_correlation_from_kernel(
    u: float | mp.mpf,
    *,
    kernel: EvenKernel,
    center_cutoff: float | mp.mpf = 4,
) -> mp.mpf:
    r"""Numerically evaluate ``C(u)=int r^2 K(u+r)K(u-r)dr``.

    The finite cutoff is a regression control, not part of the analytic
    definition.
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
    r"""Return ``D_y(u)=cosh(2yu)C(u)`` for a supplied even kernel."""

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
    r"""Return ``H_y(q)=D_y(sqrt(q))`` for ``q>=0``."""

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
    r"""Return the exact lower bound for ``-H_y'(q)/H_y(q)``."""

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


def bridge_even_moment_upper_bound(
    order: int,
    *,
    strong_log_concavity_margin: float | mp.mpf = G004_STRONG_LOG_CONCAVITY_MARGIN,
) -> mp.mpf:
    r"""Return the analytic upper bound for ``E_mu[r^(2*order)]``.

    Under ``L'' >= m`` the bridge score identity gives

        E[r^(2j+1) D_u(r)] = (2j+3) E[r^(2j)],

    while strong monotonicity gives ``r D_u(r) >= 2m r^2``. Therefore

        E[r^(2j+2)] <= (2j+3)/(2m) E[r^(2j)]

    and hence

        E[r^(2n)] <= (2n+1)!! / (2m)^n.

    For the strict G004 margin the corresponding inequalities are strict for
    positive orders. The returned value is the conservative closed upper
    envelope, not a numerical estimate of an actual bridge moment.
    """

    if not isinstance(order, int) or order < 0:
        raise ValueError("order must be a non-negative integer")
    margin = mp.mpf(strong_log_concavity_margin)
    if margin <= 0:
        raise ValueError("strong_log_concavity_margin must be positive")
    bound = mp.mpf("1")
    for j in range(order):
        bound *= mp.mpf(2 * j + 3) / (2 * margin)
    return bound


def bridge_square_exponential_mgf_upper_bound(
    lam: float | mp.mpf,
    *,
    strong_log_concavity_margin: float | mp.mpf = G004_STRONG_LOG_CONCAVITY_MARGIN,
) -> mp.mpf:
    r"""Return the analytic bridge bound ``E[exp(lam*r^2)]``.

    The even-moment hierarchy sums to the radial-Gaussian envelope

        E exp(lam r^2) <= (1-lam/m)^(-3/2),  0<=lam<m.
    """

    lam = mp.mpf(lam)
    margin = mp.mpf(strong_log_concavity_margin)
    if margin <= 0:
        raise ValueError("strong_log_concavity_margin must be positive")
    if not (0 <= lam < margin):
        raise ValueError("require 0 <= lam < strong_log_concavity_margin")
    return mp.power(1 - lam / margin, mp.mpf("-1.5"))


def second_order_cm_normalized_margin_from_bridge(
    u: float | mp.mpf,
    y: float | mp.mpf,
    *,
    mean_a: float | mp.mpf,
    mean_b: float | mp.mpf,
    var_a: float | mp.mpf,
) -> mp.mpf:
    r"""Return the exact normalized second-order CM bridge margin.

    With the normalized bridge measure, ``A=L'(u+r)+L'(u-r)``,
    ``B=L''(u+r)+L''(u-r)``, ``R=E[A]``, ``R'=E[B]-Var(A)``,
    ``a=|y|``, ``T=2a*tanh(2au)``, and ``N=R-T``, the result is

        4u^3 H_y''(u^2)/H_y(u^2)
        = N + u[N^2 + Var(A) - E[B] + 4a^2 sech^2(2au)].
    """

    u = mp.mpf(u)
    a = abs(mp.mpf(y))
    mean_a = mp.mpf(mean_a)
    mean_b = mp.mpf(mean_b)
    var_a = mp.mpf(var_a)
    if u <= 0:
        raise ValueError("require u>0")
    if not (0 <= a < mp.mpf("0.5")):
        raise ValueError("require |y| < 1/2")
    if var_a < 0:
        raise ValueError("var_a must be non-negative")
    tanh_term = mp.tanh(2 * a * u)
    sech_sq = 1 / mp.cosh(2 * a * u) ** 2
    tilt = 2 * a * tanh_term
    n_value = mean_a - tilt
    return n_value + u * (
        n_value * n_value + var_a - mean_b + 4 * a * a * sech_sq
    )


def internal_tilt_jensen_kernel_from_kernel(
    u: float | mp.mpf,
    y: float | mp.mpf,
    *,
    kernel: EvenKernel,
    center_cutoff: float | mp.mpf = 4,
) -> mp.mpf:
    r"""Numerically evaluate the distinct internal-tilt Jensen kernel."""

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
    r"""Return finite-difference diagnostics for ``(-1)^m f^(m)(q)``, m=1..4."""

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
