"""Reciprocal-deficit normal form for the SOH-G006 solid PF3 margin.

The identities here are exact algebra.  They do not prove the required
monotone 1-Lipschitz law for the actual Riemann quotient coefficients, do not
control all order-three Toeplitz minors, and do not prove PF3, PF-infinity,
real-rootedness, or RH.
"""

from __future__ import annotations


def reciprocal_deficit(q):
    """Return ``E = 1/(1-q)`` for ``q < 1``."""

    return 1 / (1 - q)


def q_from_reciprocal_deficit(E):
    """Invert ``E = 1/(1-q)``."""

    return 1 - 1 / E


def pf3_margin_from_q(u, v, w):
    """Return the exact SOH-G006 solid PF3 margin."""

    return (1 - v) ** 2 - v**2 * (1 - u) * (1 - w)


def transformed_margin(E_prev, E, E_next):
    r"""Return the numerator of the G023 reciprocal-deficit normal form.

    .. math::

       \widehat M=E_{k-1}E_{k+1}-(E_k-1)^2.
    """

    return E_prev * E_next - (E - 1) ** 2


def reconstructed_pf3_margin(E_prev, E, E_next):
    r"""Reconstruct the G006 margin from reciprocal deficits.

    .. math::

       M=\frac{\widehat M}{E_{k-1}E_k^2E_{k+1}}.
    """

    return transformed_margin(E_prev, E, E_next) / (E_prev * E**2 * E_next)


def increment_decomposition(E_prev, E, E_next):
    r"""Return the exact increment decomposition of ``widehat M``.

    With ``alpha=E-E_prev`` and ``beta=E_next-E``, the identity is

    .. math::

       \widehat M=(E-1)+E(1-\alpha)+E_{k-1}\beta.
    """

    alpha = E - E_prev
    beta = E_next - E
    return (E - 1) + E * (1 - alpha) + E_prev * beta


def lipschitz_certificate(E_prev, E, E_next) -> dict[str, object]:
    """Certify the single solid minor from the local G023 increment law.

    The exact sufficient package is ``E > 1``, ``E_prev > 0``,
    ``alpha=E-E_prev <= 1``, and ``beta=E_next-E >= 0``.  Under it,
    ``widehat M > 0`` and hence the G006 solid PF3 margin is positive.
    """

    alpha = E - E_prev
    beta = E_next - E
    wide = transformed_margin(E_prev, E, E_next)
    decomp = increment_decomposition(E_prev, E, E_next)
    assumptions = bool(E > 1 and E_prev > 0 and alpha <= 1 and beta >= 0)
    return {
        "alpha": alpha,
        "beta": beta,
        "transformed_margin": wide,
        "increment_decomposition": decomp,
        "decomposition_residual": wide - decomp,
        "assumptions_hold": assumptions,
        "solid_minor_certified_positive": bool(assumptions and wide > 0),
    }
