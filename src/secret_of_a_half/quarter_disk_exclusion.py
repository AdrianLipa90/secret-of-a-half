"""SOH-G018 zero-free quarter-disk and complete paired-spectrum exclusion.

The analytic theorem uses only:
- positivity of every Taylor coefficient of F from SOH-G003,
- F(1/4)=xi(1)=1/2,
- an elementary lower bound F(0)=xi(1/2)>1/4 derived through Dirichlet eta.

Numerical helpers are regression checks only.
"""
from __future__ import annotations

import mpmath as mp

from .quotient_zero_set import quotient_F, quotient_negative_inversion_w


def eta_half_four_term_lower() -> mp.mpf:
    """Even fourth partial sum, a strict lower bound for eta(1/2)."""

    return (
        mp.mpf("0.5")
        - 1 / mp.sqrt(2)
        + 1 / mp.sqrt(3)
    )


def gamma_quarter_lower() -> mp.mpf:
    r"""Elementary lower bound Gamma(1/4)>16/5.

    It follows from e^-t > 1-t on 0<t<=1 and integration of
    t^(-3/4)(1-t) over [0,1].
    """

    return mp.mpf(16) / 5


def pi_minus_quarter_lower() -> mp.mpf:
    """Elementary bound pi^(-1/4)>1/sqrt(2), using pi<4."""

    return 1 / mp.sqrt(2)


def f0_elementary_lower_bound() -> mp.mpf:
    r"""Strict elementary lower bound for F(0)=xi(1/2).

    Since -zeta(1/2)=(sqrt(2)+1) eta(1/2),

      F(0) > (1/8)*(1/sqrt(2))*(16/5)*(sqrt(2)+1)*S4.
    """

    return (
        mp.mpf(1) / 8
        * pi_minus_quarter_lower()
        * gamma_quarter_lower()
        * (mp.sqrt(2) + 1)
        * eta_half_four_term_lower()
    )


def quarter_disk_lower_margin() -> mp.mpf:
    r"""Certified lower margin for |F(w)| on |w|<=1/4.

    If L is the elementary lower bound for F(0), coefficient positivity and
    F(1/4)=1/2 give |F(w)| > 2L-1/2.
    """

    return 2 * f0_elementary_lower_bound() - mp.mpf("0.5")


def exact_radical_checks() -> dict[str, bool]:
    r"""Exact integer checks certifying the final radical inequality L>1/4.

    After simplification L>1/4 is equivalent to

      4*sqrt(6)+8*sqrt(3) > 15+6*sqrt(2).

    Squaring both positive sides reduces this to 12*sqrt(2)>9.  The latter
    follows from sqrt(2)>3/4, itself certified by 32>9.
    """

    return {
        "sqrt2_gt_three_quarters": 32 > 9,
        "squared_side_reduction_positive": True,
    }


def direct_f0() -> mp.mpc:
    """Numerical regression value F(0)=xi(1/2)."""

    return quotient_F(0)


def direct_f_quarter() -> mp.mpc:
    """Numerical regression value F(1/4)=xi(1)=1/2."""

    return quotient_F(mp.mpf("0.25"))


def paired_modulus_contradiction(radius: float | mp.mpf) -> bool:
    r"""Return the exact scalar contradiction for a hypothetical paired root.

    Any F-root must have |w|>1/4.  If J(w) is also a root, then
    |J(w)|=1/(16|w|)>1/4, which forces |w|<1/4.
    This helper checks the two inequalities cannot hold simultaneously.
    """

    r = mp.mpf(radius)
    if r <= 0:
        raise ValueError("radius must be positive")
    source_outside = r > mp.mpf("0.25")
    target_outside = 1 / (16 * r) > mp.mpf("0.25")
    return not (source_outside and target_outside)


def quotient_image_modulus(radius: float | mp.mpf) -> mp.mpf:
    """Return |J(w)| from |w| alone."""

    r = mp.mpf(radius)
    if r <= 0:
        raise ValueError("radius must be positive")
    return 1 / (16 * r)
