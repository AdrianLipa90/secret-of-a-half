"""Arithmetic zeta screw function g(t) = -Psi(|t|), source-normalized.

This implements Suzuki's explicit 2023 formula

  Psi(t) =
    4(e^(t/2)+e^(-t/2)-2)
    - sum_{n<=e^t} Lambda(n)/sqrt(n) * (t-log n)
    + t/2 * (psi(1/4)-log(pi))
    + 1/4 * (C - e^(-t/2) Phi(e^(-2t),2,1/4))

for t>=0, with C=pi^2+8*Catalan and Phi the Hurwitz--Lerch zeta.
The screw function used in the localized kernel is g(t)=-Psi(|t|).

The implementation is a high-precision numerical evaluator/diagnostic.  It is
NOT interval arithmetic and must not be used as a rigorous C005 certificate
without a separate enclosure layer.
"""
from __future__ import annotations

import math

import mpmath as mp

from .phasenav_weil_hermite_arithmetic import prime_power_terms


_A = mp.mpf("0.25")


def _support_cutoff(x: mp.mpf, max_support: int) -> int:
    if x < 0:
        raise ValueError("x must be non-negative")
    support = int(mp.floor(mp.e**x))
    if support > max_support:
        raise ValueError(
            f"prime support exp(x)={support} exceeds max_support={max_support}"
        )
    return support


def mangoldt_hinge_sum(
    x: float | str | mp.mpf,
    *,
    max_support: int = 2_000_000,
) -> mp.mpf:
    """sum_{n<=exp(x)} Lambda(n)/sqrt(n) * (x-log n)."""
    t = mp.mpf(x)
    cutoff = _support_cutoff(t, max_support)
    total = mp.mpf("0")
    for n, logp in prime_power_terms(cutoff):
        total += mp.mpf(str(logp)) / mp.sqrt(n) * (t - mp.log(n))
    return total


def mangoldt_sqrt_sum(
    x: float | str | mp.mpf,
    *,
    max_support: int = 2_000_000,
) -> mp.mpf:
    """sum_{n<=exp(x)} Lambda(n)/sqrt(n), the a.e. derivative hinge sum."""
    t = mp.mpf(x)
    cutoff = _support_cutoff(t, max_support)
    total = mp.mpf("0")
    for n, logp in prime_power_terms(cutoff):
        total += mp.mpf(str(logp)) / mp.sqrt(n)
    return total


def psi_positive(
    x: float | str | mp.mpf,
    *,
    max_support: int = 2_000_000,
) -> mp.mpf:
    """Suzuki Psi(x) for x>=0."""
    t = mp.mpf(x)
    if t < 0:
        raise ValueError("psi_positive expects x>=0")
    if t == 0:
        return mp.mpf("0")

    q = mp.e ** (-2 * t)
    C = mp.pi**2 + 8 * mp.catalan
    gamma_term = mp.digamma(_A) - mp.log(mp.pi)
    lerch = mp.lerchphi(q, 2, _A)

    return (
        4 * (mp.e ** (t / 2) + mp.e ** (-t / 2) - 2)
        - mangoldt_hinge_sum(t, max_support=max_support)
        + t * gamma_term / 2
        + (C - mp.e ** (-t / 2) * lerch) / 4
    )


def zeta_screw_g(
    t: float | str | mp.mpf,
    *,
    max_support: int = 2_000_000,
) -> mp.mpf:
    """Even real zeta screw function g(t)=-Psi(|t|)."""
    x = abs(mp.mpf(t))
    return -psi_positive(x, max_support=max_support)


def psi_prime_positive(
    x: float | str | mp.mpf,
    *,
    max_support: int = 2_000_000,
) -> mp.mpf:
    """A.e. derivative of Psi(x) for x>0 away from x=log(p^k).

    At prime-power thresholds the hinge derivative has a jump; the formula
    chooses the right-continuous finite sum convention.  This ambiguity is on
    a measure-zero set and is irrelevant for L2 derivative integrals.
    """
    t = mp.mpf(x)
    if t <= 0:
        raise ValueError("psi_prime_positive expects x>0")

    q = mp.e ** (-2 * t)
    gamma_term = mp.digamma(_A) - mp.log(mp.pi)

    # d/dt [ e^(-t/2) Phi(e^(-2t),2,1/4) ]
    #   = -2 e^(-t/2) Phi(e^(-2t),1,1/4).
    arch_derivative = (
        2 * (mp.e ** (t / 2) - mp.e ** (-t / 2))
        + gamma_term / 2
        + mp.e ** (-t / 2) * mp.lerchphi(q, 1, _A) / 2
    )

    return (
        arch_derivative
        - mangoldt_sqrt_sum(t, max_support=max_support)
    )


def zeta_screw_g_prime(
    t: float | str | mp.mpf,
    *,
    max_support: int = 2_000_000,
) -> mp.mpf:
    """A.e. odd derivative g'(t) for t!=0 away from prime-power thresholds."""
    x = mp.mpf(t)
    if x == 0:
        raise ValueError("g' has a logarithmic endpoint singularity at t=0")
    sign = mp.mpf(1) if x > 0 else mp.mpf(-1)
    return -sign * psi_prime_positive(abs(x), max_support=max_support)


def screw_kernel_value(
    t: float | str | mp.mpf,
    u: float | str | mp.mpf,
    *,
    max_support: int = 2_000_000,
) -> mp.mpf:
    """G_g(t,u)=g(t-u)-g(t)-g(-u)+g(0)."""
    tt = mp.mpf(t)
    uu = mp.mpf(u)
    return (
        zeta_screw_g(tt - uu, max_support=max_support)
        - zeta_screw_g(tt, max_support=max_support)
        - zeta_screw_g(-uu, max_support=max_support)
    )


def screw_kernel_du_value(
    t: float | str | mp.mpf,
    u: float | str | mp.mpf,
    *,
    max_support: int = 2_000_000,
) -> mp.mpf:
    """A.e. u-derivative of G_g(t,u), away from singular/jump loci."""
    tt = mp.mpf(t)
    uu = mp.mpf(u)
    return (
        -zeta_screw_g_prime(tt - uu, max_support=max_support)
        + zeta_screw_g_prime(-uu, max_support=max_support)
    )


def screw_formula_receipt() -> dict[str, object]:
    return {
        "schema": "SOH_ZETA_SCREW_FORMULA_V0_1",
        "source_formula": "Suzuki 2023 Psi equation (1.1), g=-Psi",
        "implemented": [
            "finite von-Mangoldt hinge sum",
            "archimedean digamma/Hurwitz-Lerch contribution",
            "even screw function g",
            "a.e. derivative away from threshold/singular loci",
            "two-variable screw kernel G_g",
        ],
        "open": [
            "rigorous interval enclosure of g and g-prime",
            "rigorous L2 norm bounds on [0,2a]",
            "threshold-safe interval arithmetic across log prime powers",
            "localized finite Fourier matrix interval enclosure",
            "SOH-C005",
            "Riemann Hypothesis",
        ],
        "numerical_only": True,
        "proof_of_rh": False,
    }
