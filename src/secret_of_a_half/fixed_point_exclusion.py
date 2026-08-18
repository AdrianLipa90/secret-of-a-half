"""SOH-G017 fixed-point exclusion for the quotient negative inversion.

The theorem proves F(-1/4)=xi(1/2+i/2)>0 from the positive Riemann kernel,
without using a table of zeta zeros.  The floating-point helpers below evaluate
closed-form analytic bounds; the proof itself is recorded in the theorem note.
"""
from __future__ import annotations

import mpmath as mp

from .quotient_zero_set import quotient_F
from .riemann_kernel import xi_from_kernel


def positive_block_lower_bound() -> mp.mpf:
    r"""Lower bound from y in [0,1/2] and only the n=1 kernel channel.

    For Xi(1/2)=int Phi(y) cos(y/2) dy,

        A = 2*pi*(2*pi-3)*exp(-pi*e)*cos(1/4)

    satisfies int_0^(1/2) Phi(y) cos(y/2) dy >= A.
    """

    return (
        2
        * mp.pi
        * (2 * mp.pi - 3)
        * mp.exp(-mp.pi * mp.e)
        * mp.cos(mp.mpf("0.25"))
    )


def oscillatory_tail_upper_bound() -> mp.mpf:
    r"""Analytic upper bound for int_pi^infinity Phi(y) dy.

    Put X=e^(2*pi), q=e^(-pi*X).  The summand-wise exponential derivative
    estimate yields

        T <= 8*pi*X^(5/4) * q*(1+q)/(1-q)^3.
    """

    X = mp.exp(2 * mp.pi)
    q = mp.exp(-mp.pi * X)
    return 8 * mp.pi * X ** mp.mpf("1.25") * q * (1 + q) / (1 - q) ** 3


def coarse_positive_bound() -> mp.mpf:
    """Elementary theorem-note bound A > 2^-15."""

    return mp.mpf(2) ** -15


def coarse_tail_bound() -> mp.mpf:
    """Elementary theorem-note bound T < 2^-167."""

    return mp.mpf(2) ** -167


def certified_margin() -> mp.mpf:
    """Strict lower bound 2^-15 - 2^-167 for F(-1/4)."""

    return coarse_positive_bound() - coarse_tail_bound()


def quotient_negative_fixed_value() -> mp.mpc:
    """Numerically evaluate F(-1/4)=xi(1/2+i/2)."""

    return quotient_F(mp.mpf("-0.25"))


def kernel_negative_fixed_value(*, n_terms: int = 8, y_cutoff: int = 4) -> mp.mpc:
    """Numerical regression value from the positive-kernel representation."""

    return xi_from_kernel(mp.j / 2, n_terms=n_terms, y_cutoff=y_cutoff)


def elementary_bound_checks() -> dict[str, bool]:
    """Return exact integer checks used by the coarse proof bounds."""

    # A > 18*(31/32)*3^-12 > 2^-15.
    lower_integer_check = 18 * 31 * 2**15 > 32 * 3**12

    # T < 32*3^10*12*2^-192 < 2^-167.
    tail_integer_check = 32 * 3**10 * 12 < 2**25

    return {
        "positive_block_gt_2^-15": lower_integer_check,
        "tail_lt_2^-167": tail_integer_check,
    }
