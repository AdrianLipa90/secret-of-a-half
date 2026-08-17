"""Prime-side arithmetic layer for the PhaseNav--Weil Hermite ladder."""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
import math

import mpmath as mp
import numpy as np
from numpy.polynomial.hermite import hermgauss

from .phasenav_weil_hermite_core import (
    HermiteLadderProgram,
    channel_normalization,
    hermite_values,
    kernel_fourier_closed,
    kernel_value,
)


@lru_cache(maxsize=8)
def prime_power_terms(cutoff: int) -> tuple[tuple[int, float], ...]:
    """Return (p^k, log p) for von Mangoldt support up to cutoff."""
    if cutoff < 2:
        return ()
    sieve = bytearray(b"\x01") * (cutoff + 1)
    sieve[0:2] = b"\x00\x00"
    for prime in range(2, int(math.isqrt(cutoff)) + 1):
        if sieve[prime]:
            start = prime * prime
            sieve[start : cutoff + 1 : prime] = b"\x00" * (
                ((cutoff - start) // prime) + 1
            )
    result: list[tuple[int, float]] = []
    for prime in range(2, cutoff + 1):
        if not sieve[prime]:
            continue
        log_prime = math.log(prime)
        power = prime
        while power <= cutoff:
            result.append((power, log_prime))
            if power > cutoff // prime:
                break
            power *= prime
    result.sort(key=lambda item: item[0])
    return tuple(result)


@dataclass(frozen=True)
class MatrixComponents:
    pole: np.ndarray
    conductor: np.ndarray
    archimedean: np.ndarray
    prime: np.ndarray

    @property
    def total(self) -> np.ndarray:
        return self.pole + self.conductor + self.archimedean + self.prime


def _quadrature_cache(program: HermiteLadderProgram) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    nodes, weights = hermgauss(program.quadrature_order)
    hermites = hermite_values(program.max_basis_size - 1, nodes)
    r_values = program.target_ordinate + nodes / program.gaussian_width
    mp.mp.dps = program.mp_dps
    gamma_values = np.array(
        [float(mp.re(mp.digamma(mp.mpf("0.25") + 0.5j * float(r)))) for r in r_values],
        dtype=float,
    )
    return nodes, weights, hermites, gamma_values


def _component_entry(
    program: HermiteLadderProgram,
    *,
    left: int,
    right: int,
    n_values: np.ndarray,
    mangoldt: np.ndarray,
    weights: np.ndarray,
    hermites: np.ndarray,
    gamma_values: np.ndarray,
) -> tuple[complex, complex, complex, complex]:
    width = program.gaussian_width
    pole_value = kernel_value(left, right, 1 / (2j), program)
    pole_value += kernel_value(left, right, -1 / (2j), program)

    conductor_value = -math.log(math.pi) / (2.0 * math.pi) * kernel_fourier_closed(
        0.0, left, right, program
    )

    left_norm = channel_normalization(left, width)
    right_norm = channel_normalization(right, width)
    arch_integral = (
        left_norm
        * right_norm
        / width
        * np.sum(weights * hermites[left] * hermites[right] * gamma_values)
    )
    arch_value = arch_integral / (2.0 * math.pi)

    if n_values.size:
        x_values = np.log(n_values) / (2.0 * math.pi)
        prime_weights = mangoldt / np.sqrt(n_values)
        transforms = kernel_fourier_closed(x_values, left, right, program)
        transforms += kernel_fourier_closed(-x_values, left, right, program)
        prime_value = -np.sum(prime_weights * transforms) / (2.0 * math.pi)
    else:
        prime_value = 0.0 + 0.0j

    return (
        complex(pole_value),
        complex(conductor_value),
        complex(arch_value),
        complex(prime_value),
    )


def arithmetic_rectangular_components(
    program: HermiteLadderProgram,
    *,
    left_orders: range | tuple[int, ...] | list[int],
    right_orders: range | tuple[int, ...] | list[int],
    prime_cutoff: int,
) -> MatrixComponents:
    """Build a rectangular block of the same arithmetic Weil form.

    The returned block uses exactly the pole, conductor, archimedean and
    retained-prime formulas used by :func:`arithmetic_matrix`.  It is a
    finite-ladder Hermite coupling certificate only; it does not introduce
    Suzuki's localization radius ``a`` and is not, by itself, a certificate
    for the infinite complement.
    """
    left = tuple(int(i) for i in left_orders)
    right = tuple(int(j) for j in right_orders)
    if not left or not right:
        raise ValueError("rectangular order sets must be non-empty")
    if min(left + right) < 0 or max(left + right) >= program.max_basis_size:
        raise ValueError("Hermite order is outside the declared ladder")
    if prime_cutoff < 2:
        raise ValueError("prime_cutoff must be at least 2")

    shape = (len(left), len(right))
    pole = np.zeros(shape, dtype=complex)
    conductor = np.zeros(shape, dtype=complex)
    archimedean = np.zeros(shape, dtype=complex)
    prime = np.zeros(shape, dtype=complex)

    _, weights, hermites, gamma_values = _quadrature_cache(program)
    terms = prime_power_terms(prime_cutoff)
    n_values = np.array([item[0] for item in terms], dtype=float)
    mangoldt = np.array([item[1] for item in terms], dtype=float)

    for row, left_order in enumerate(left):
        for col, right_order in enumerate(right):
            values = _component_entry(
                program,
                left=left_order,
                right=right_order,
                n_values=n_values,
                mangoldt=mangoldt,
                weights=weights,
                hermites=hermites,
                gamma_values=gamma_values,
            )
            pole[row, col], conductor[row, col], archimedean[row, col], prime[row, col] = values

    return MatrixComponents(pole, conductor, archimedean, prime)


def arithmetic_matrix(
    program: HermiteLadderProgram,
    *,
    basis_size: int,
    prime_cutoff: int,
) -> tuple[np.ndarray, MatrixComponents]:
    """Build one N x N prime-side Hermite principal matrix."""
    if not 1 <= basis_size <= program.max_basis_size:
        raise ValueError("basis_size is outside the declared ladder")

    orders = tuple(range(basis_size))
    components = arithmetic_rectangular_components(
        program,
        left_orders=orders,
        right_orders=orders,
        prime_cutoff=prime_cutoff,
    )
    matrix = components.total
    matrix = 0.5 * (matrix + matrix.conjugate().T)
    return matrix, components


REFERENCE_ORDINATES = (
    14.134725141734695,
    21.022039638771555,
    25.01085758014569,
    30.424876125859512,
    32.93506158773919,
    37.586178158825675,
    40.9187190121475,
    43.327073280915,
    48.00515088116716,
    49.7738324776723,
)
