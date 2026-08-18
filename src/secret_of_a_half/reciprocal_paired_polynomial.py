"""SOH-G018 reciprocal polynomial utilities for the finite paired quotient spectrum.

For the normalized quotient coordinate lambda=4w, the G015 involution
J(w)=1/(16w) becomes lambda -> 1/lambda.  The theorem note proves that the
monic polynomial of the finite normalized paired set is self-reciprocal with
constant coefficient one.  Helpers here provide exact-form constructions and
numerical regression checks; they do not establish that the paired set is
nonempty.
"""
from __future__ import annotations

from collections.abc import Iterable, Sequence

import mpmath as mp


def _finite_complex(value: complex | mp.mpf | mp.mpc, *, name: str) -> mp.mpc:
    value = mp.mpc(value)
    if not mp.isfinite(value):
        raise ValueError(f"{name} must be finite")
    return value


def normalize_w_to_lambda(w: complex | mp.mpf | mp.mpc) -> mp.mpc:
    """Return the normalized quotient coordinate lambda=4w."""
    return 4 * _finite_complex(w, name="w")


def reciprocal_lambda(lam: complex | mp.mpf | mp.mpc) -> mp.mpc:
    """Normalized G015 involution lambda -> 1/lambda."""
    lam = _finite_complex(lam, name="lambda")
    if lam == 0:
        raise ValueError("reciprocal involution is singular at lambda=0")
    return 1 / lam


def monic_polynomial_coefficients(
    roots: Iterable[complex | mp.mpf | mp.mpc],
) -> tuple[mp.mpc, ...]:
    """Return descending coefficients of prod(x-root) with leading one."""
    coeffs: list[mp.mpc] = [mp.mpc(1)]
    for index, root in enumerate(roots):
        root = _finite_complex(root, name=f"roots[{index}]")
        next_coeffs = [mp.mpc(0)] * (len(coeffs) + 1)
        for i, coefficient in enumerate(coeffs):
            next_coeffs[i] += coefficient
            next_coeffs[i + 1] -= coefficient * root
        coeffs = next_coeffs
    return tuple(coeffs)


def evaluate_polynomial(
    coefficients: Sequence[complex | mp.mpf | mp.mpc],
    x: complex | mp.mpf | mp.mpc,
) -> mp.mpc:
    """Evaluate descending polynomial coefficients by Horner's rule."""
    x = _finite_complex(x, name="x")
    if not coefficients:
        raise ValueError("coefficients must be non-empty")
    value = mp.mpc(0)
    for index, coefficient in enumerate(coefficients):
        coefficient = _finite_complex(coefficient, name=f"coefficients[{index}]")
        value = value * x + coefficient
    return value


def reciprocal_closure_residual(
    roots: Sequence[complex | mp.mpf | mp.mpc],
) -> mp.mpf:
    """Maximum distance from 1/lambda to the supplied finite root set."""
    values = [_finite_complex(root, name=f"roots[{i}]") for i, root in enumerate(roots)]
    if not values:
        return mp.mpf(0)
    if any(value == 0 for value in values):
        raise ValueError("reciprocal root set cannot contain zero")
    return max(min(abs(1 / value - target) for target in values) for value in values)


def conjugation_closure_residual(
    roots: Sequence[complex | mp.mpf | mp.mpc],
) -> mp.mpf:
    """Maximum distance from conjugate(lambda) to the supplied root set."""
    values = [_finite_complex(root, name=f"roots[{i}]") for i, root in enumerate(roots)]
    if not values:
        return mp.mpf(0)
    return max(min(abs(mp.conj(value) - target) for target in values) for value in values)


def palindromic_coefficient_residual(
    coefficients: Sequence[complex | mp.mpf | mp.mpc],
) -> mp.mpf:
    """Maximum |c_k-c_{n-k}| for descending coefficients."""
    values = [
        _finite_complex(coefficient, name=f"coefficients[{i}]")
        for i, coefficient in enumerate(coefficients)
    ]
    if not values:
        raise ValueError("coefficients must be non-empty")
    return max(abs(values[i] - values[-1 - i]) for i in range(len(values)))


def real_coefficient_residual(
    coefficients: Sequence[complex | mp.mpf | mp.mpc],
) -> mp.mpf:
    """Maximum absolute imaginary part of the coefficients."""
    values = [
        _finite_complex(coefficient, name=f"coefficients[{i}]")
        for i, coefficient in enumerate(coefficients)
    ]
    if not values:
        raise ValueError("coefficients must be non-empty")
    return max(abs(mp.im(value)) for value in values)


def self_reciprocal_identity_residual(
    coefficients: Sequence[complex | mp.mpf | mp.mpc],
    x: complex | mp.mpf | mp.mpc,
) -> mp.mpf:
    """Residual of Q(x)=x^n Q(1/x), away from x=0."""
    x = _finite_complex(x, name="x")
    if x == 0:
        raise ValueError("self-reciprocal identity check requires x != 0")
    n = len(coefficients) - 1
    return abs(
        evaluate_polynomial(coefficients, x)
        - mp.power(x, n) * evaluate_polynomial(coefficients, 1 / x)
    )


def reciprocal_pair_factor(lam: complex | mp.mpf | mp.mpc) -> tuple[mp.mpc, mp.mpc, mp.mpc]:
    """Return coefficients of (x-lambda)(x-1/lambda)."""
    lam = _finite_complex(lam, name="lambda")
    if lam == 0:
        raise ValueError("lambda must be non-zero")
    return mp.mpc(1), -(lam + 1 / lam), mp.mpc(1)


def expected_normalized_cardinality(generic_pairs: int, exceptional_minus_one: bool) -> int:
    """Return n=2a+epsilon for an inversion-invariant normalized paired set."""
    if isinstance(generic_pairs, bool) or not isinstance(generic_pairs, int):
        raise TypeError("generic_pairs must be an integer")
    if generic_pairs < 0:
        raise ValueError("generic_pairs must be non-negative")
    return 2 * generic_pairs + (1 if exceptional_minus_one else 0)
