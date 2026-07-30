"""Analytic integral identities and finite-section envelopes for the prime tail."""
from __future__ import annotations
import math
import mpmath as mp
import numpy as np
from .phasenav_weil_hermite_core import channel_normalization, hermite_linearization_terms
from .phasenav_weil_prime_tail_program import monotonicity_margin

def tail_term_integral_gamma(degree: int, cutoff: int, width: float) -> mp.mpf:
    """Closed upper-incomplete-gamma form of one logarithmic tail integral.

    This returns
        w^-d int_Q^inf (log x)^(d+1) x^-1/2
                 exp(-(log x)^2/(4 w^2)) dx.
    """
    if degree < 0 or cutoff < 3 or width <= 0.0:
        raise ValueError("invalid tail-integral parameters")
    mp_width = mp.mpf(str(width))
    lower_u = mp.log(cutoff)
    if lower_u <= mp_width * mp_width:
        raise ValueError("cutoff must satisfy log(Q) > width^2")
    lower_a = (lower_u - mp_width * mp_width) / (2 * mp_width)
    result = mp.mpf("0")
    for j in range(degree + 2):
        binomial = math.comb(degree + 1, j)
        shift_power = mp_width ** (2 * (degree + 1 - j))
        gaussian_moment = (
            (mp.mpf(2) ** j)
            * (mp_width ** (j + 1))
            * mp.gammainc(mp.mpf(j + 1) / 2, lower_a * lower_a, mp.inf)
        )
        result += binomial * shift_power * gaussian_moment
    return mp.exp(mp_width * mp_width / 4) * result / (mp_width**degree)


def tail_term_integral_log(degree: int, cutoff: int, width: float) -> mp.mpf:
    """Direct half-line quadrature in u=log(x), used as a cross-check."""
    mp_width = mp.mpf(str(width))
    lower_u = mp.log(cutoff)

    def integrand(u: mp.mpf) -> mp.mpf:
        return (
            u ** (degree + 1)
            * mp.exp(-(u * u) / (4 * mp_width * mp_width) + u / 2)
            / (mp_width**degree)
        )

    return mp.quad(integrand, [lower_u, mp.inf])


def reciprocal_tail_integrand(
    z_tail: float | mp.mpf,
    degree: int,
    width: float,
) -> mp.mpf:
    """Tail density after z_tail=1/log(x), with its flat endpoint value."""
    z = mp.mpf(z_tail)
    if z < 0:
        raise ValueError("z_tail must be non-negative")
    if z == 0:
        return mp.mpf("0")
    mp_width = mp.mpf(str(width))
    return (
        z ** (-(degree + 3))
        * mp.exp(-1 / (4 * mp_width * mp_width * z * z) + 1 / (2 * z))
        / (mp_width**degree)
    )


def tail_term_integral_reciprocal(degree: int, cutoff: int, width: float) -> mp.mpf:
    """Compact-interval quadrature after z_tail=1/log(x)."""
    upper = 1 / mp.log(cutoff)

    def integrand(z: mp.mpf) -> mp.mpf:
        return reciprocal_tail_integrand(z, degree, width)

    return mp.quad(integrand, [0, upper / 4, upper / 2, 3 * upper / 4, upper])


def _fourier_prefactor(left_order: int, right_order: int, width: float) -> mp.mpf:
    return (
        mp.mpf(str(channel_normalization(left_order, width)))
        * mp.mpf(str(channel_normalization(right_order, width)))
        * mp.sqrt(mp.pi)
        / mp.mpf(str(width))
    )


def entry_tail_bound(
    left_order: int,
    right_order: int,
    cutoff: int,
    width: float,
) -> mp.mpf:
    """Unconditional entrywise bound for the omitted prime-power tail."""
    if min(left_order, right_order) < 0:
        raise ValueError("Hermite orders must be non-negative")
    max_degree = left_order + right_order
    if monotonicity_margin(max_degree, cutoff, width) < 0.0:
        raise ValueError("cutoff is below the monotone integral-test threshold")
    total = mp.mpf("0")
    for degree, coefficient in hermite_linearization_terms(left_order, right_order):
        total += coefficient * tail_term_integral_gamma(degree, cutoff, width)
    return _fourier_prefactor(left_order, right_order, width) * total / mp.pi


def entry_bound_matrix(
    basis_size: int,
    cutoff: int,
    width: float,
) -> np.ndarray:
    """Return the symmetric matrix of entrywise tail majorants."""
    if basis_size < 1:
        raise ValueError("basis_size must be positive")
    result = np.empty((basis_size, basis_size), dtype=float)
    for left in range(basis_size):
        for right in range(left, basis_size):
            value = float(entry_tail_bound(left, right, cutoff, width))
            result[left, right] = value
            result[right, left] = value
    return result


def operator_norm_tail_bound(
    basis_size: int,
    cutoff: int,
    width: float,
) -> float:
    """Spectral-norm envelope obtained from the symmetric max-row-sum norm."""
    bounds = entry_bound_matrix(basis_size, cutoff, width)
    return float(np.max(np.sum(bounds, axis=1)))
