"""SOH-G018 quarter-disk zero exclusion for the even xi quotient.

The proof uses only exact rational lower bounds plus the previously proved
positivity of the Taylor coefficients of F, where

    xi(1/2 + z) = F(z**2).

It does not use a table of zeta zeros.
"""
from __future__ import annotations

from fractions import Fraction

import mpmath as mp

from .quotient_zero_set import quotient_F, quotient_negative_inversion_w


QUARTER = Fraction(1, 4)
XI_HALF_LOWER = Fraction(54723, 203125)
ZERO_FREE_MARGIN = Fraction(15767, 406250)


def eta_half_lower_bound() -> Fraction:
    """Elementary lower bound eta(1/2) > 9/25 from the fourth partial sum."""

    return Fraction(9, 25)


def minus_zeta_half_lower_bound() -> Fraction:
    """Elementary lower bound -zeta(1/2) > 108/125."""

    return Fraction(108, 125)


def gamma_quarter_lower_bound() -> Fraction:
    r"""Lower bound Gamma(1/4) > 1972/585.

    Integrate t^(-3/4) times the cubic lower Taylor polynomial
    1-t+t^2/2-t^3/6 for exp(-t) on [0,1].
    """

    return Fraction(1972, 585)


def pi_inverse_quarter_lower_bound() -> Fraction:
    """Elementary lower bound pi^(-1/4) > 37/50."""

    return Fraction(37, 50)


def xi_half_rational_lower_bound() -> Fraction:
    r"""Return the exact rational certificate xi(1/2) > 54723/203125."""

    return (
        Fraction(1, 8)
        * pi_inverse_quarter_lower_bound()
        * gamma_quarter_lower_bound()
        * minus_zeta_half_lower_bound()
    )


def zero_free_margin_lower_bound() -> Fraction:
    r"""Lower bound for |F(w)| on |w| <= 1/4.

    Positive Taylor coefficients give

        |F(w)| >= 2 F(0) - F(1/4).

    Since F(1/4)=xi(1)=1/2 and F(0)=xi(1/2), the rational certificate is

        |F(w)| > 2*(54723/203125) - 1/2
               = 15767/406250.
    """

    return 2 * xi_half_rational_lower_bound() - Fraction(1, 2)


def exact_certificate_checks() -> dict[str, bool]:
    """Exact integer/rational checks used by the analytic proof."""

    # sqrt(2) > 7/5 and 1/sqrt(2) < 71/100.
    sqrt2_gt_7_over_5 = 2 * 5**2 > 7**2
    inv_sqrt2_lt_71_over_100 = 2 * 71**2 > 100**2

    # 1/sqrt(3) > 57/100.
    inv_sqrt3_gt_57_over_100 = 3 * 57**2 < 100**2

    # pi < 22/7 < (50/37)^4 implies pi^(-1/4) > 37/50.
    pi_chain_integer = 22 * 37**4 < 7 * 50**4

    xi_bound_identity = xi_half_rational_lower_bound() == XI_HALF_LOWER
    xi_bound_gt_quarter = XI_HALF_LOWER > QUARTER
    margin_identity = zero_free_margin_lower_bound() == ZERO_FREE_MARGIN
    margin_positive = ZERO_FREE_MARGIN > 0

    return {
        "sqrt2_gt_7_over_5": sqrt2_gt_7_over_5,
        "inv_sqrt2_lt_71_over_100": inv_sqrt2_lt_71_over_100,
        "inv_sqrt3_gt_57_over_100": inv_sqrt3_gt_57_over_100,
        "pi_chain_integer": pi_chain_integer,
        "xi_bound_identity": xi_bound_identity,
        "xi_bound_gt_quarter": xi_bound_gt_quarter,
        "margin_identity": margin_identity,
        "margin_positive": margin_positive,
    }


def xi_half_numeric() -> mp.mpc:
    """Numerical regression value F(0)=xi(1/2)."""

    return quotient_F(mp.mpf("0"))


def positive_boundary_numeric() -> mp.mpc:
    """Numerical regression value F(1/4)=xi(1)=1/2."""

    return quotient_F(mp.mpf("0.25"))


def inversion_modulus(radius: mp.mpf) -> mp.mpf:
    """Return |J(w)| from |w|=radius for J(w)=1/(16w)."""

    if radius <= 0:
        raise ValueError("radius must be positive")
    return 1 / (16 * radius)


def maps_root_modulus_into_zero_free_disk(radius: mp.mpf) -> bool:
    """For a root radius >1/4, certify that its J-image has radius <1/4."""

    return radius > mp.mpf("0.25") and inversion_modulus(radius) < mp.mpf("0.25")


def boundary_regression(samples: int = 32) -> mp.mpf:
    """Return the smallest sampled |F(w)| on |w|=1/4.

    This is a regression diagnostic only.  The zero-free disk is proved by the
    analytic coefficient bound above, not by sampling.
    """

    if samples < 4:
        raise ValueError("samples must be at least 4")
    values = []
    for k in range(samples):
        theta = 2 * mp.pi * k / samples
        w = mp.mpf("0.25") * mp.e ** (mp.j * theta)
        values.append(abs(quotient_F(w)))
    return min(values)
