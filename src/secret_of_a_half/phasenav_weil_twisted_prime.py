"""Cancellation-sensitive prime-power accumulation for the C005 frontier.

This module keeps the arithmetic phase n^{-it0}.  It provides an exact finite
summation-by-parts identity and numerical diagnostics only; it does not assert
an asymptotic prime-sum estimate or prove SOH-C005/RH.
"""
from __future__ import annotations

from dataclasses import dataclass
import cmath
import math
from typing import Callable, Iterable

from .phasenav_weil_hermite_arithmetic import prime_power_terms


@dataclass(frozen=True)
class TwistedPrimeTerm:
    n: int
    mangoldt: float
    weight: complex


def twisted_prime_terms(cutoff: int, target_ordinate: float) -> tuple[TwistedPrimeTerm, ...]:
    """Return Λ(n)n^(-1/2-it0) on prime-power support up to cutoff."""
    if cutoff < 2:
        return ()
    if not math.isfinite(target_ordinate):
        raise ValueError("target_ordinate must be finite")
    out: list[TwistedPrimeTerm] = []
    for n, mangoldt in prime_power_terms(cutoff):
        phase = cmath.exp(-1j * target_ordinate * math.log(n))
        weight = mangoldt * phase / math.sqrt(n)
        out.append(TwistedPrimeTerm(n=n, mangoldt=mangoldt, weight=weight))
    return tuple(out)


def cumulative_twisted_prime_sum(cutoff: int, target_ordinate: float) -> complex:
    """S_t0(X)=sum_{n<=X} Λ(n)n^(-1/2-it0) over prime powers."""
    return sum((term.weight for term in twisted_prime_terms(cutoff, target_ordinate)), 0j)


def cancellation_ratio(cutoff: int, target_ordinate: float) -> float:
    """|sum w_n| / sum |w_n|, in [0,1] up to floating-point roundoff."""
    terms = twisted_prime_terms(cutoff, target_ordinate)
    denominator = sum(abs(term.weight) for term in terms)
    if denominator == 0.0:
        return 0.0
    return abs(sum((term.weight for term in terms), 0j)) / denominator


def finite_summation_by_parts(
    terms: Iterable[TwistedPrimeTerm],
    kernel: Callable[[int], complex],
) -> complex:
    """Evaluate sum a_j f(n_j) through exact discrete summation by parts.

    For ordered support n_1<...<n_J and A_j=sum_{k<=j}a_k,

        sum_{j=1}^J a_j f(n_j)
        = A_J f(n_J) + sum_{j=1}^{J-1} A_j [f(n_j)-f(n_{j+1})].

    This identity preserves phase/cancellation in the cumulative sums A_j.
    """
    sequence = tuple(terms)
    if not sequence:
        return 0j
    if any(sequence[j].n >= sequence[j + 1].n for j in range(len(sequence) - 1)):
        raise ValueError("terms must be strictly increasing in n")

    cumulative: list[complex] = []
    running = 0j
    for term in sequence:
        running += term.weight
        cumulative.append(running)

    total = cumulative[-1] * complex(kernel(sequence[-1].n))
    for j in range(len(sequence) - 1):
        total += cumulative[j] * (
            complex(kernel(sequence[j].n)) - complex(kernel(sequence[j + 1].n))
        )
    return total


def direct_weighted_sum(
    terms: Iterable[TwistedPrimeTerm],
    kernel: Callable[[int], complex],
) -> complex:
    """Direct reference evaluation of the same finite weighted sum."""
    return sum((term.weight * complex(kernel(term.n)) for term in terms), 0j)
