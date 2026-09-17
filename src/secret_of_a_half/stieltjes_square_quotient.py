"""SOH-G025 square-quotient / Stieltjes helpers.

This module contains only exact algebraic reductions for a formal power series

    F(w) = sum_{k>=0} a_k w^k,   a_0 != 0,

and its logarithmic derivative phi = F'/F.

If F belongs to the Laguerre--Polya class LP+ then

    phi(w) = sum_{n>=0} (-1)^n mu_n w^n

with (mu_n) a Stieltjes moment sequence. For the secret-of-a-half quotient
F defined by xi(1/2+z)=F(z^2), the converse is a classical external theorem
under the standard entire-function hypotheses. This module does not promote
that theorem, RH, PF3, PF-infinity, or real-rootedness; it only computes the
exact finite algebra exposed by the research note.
"""

from __future__ import annotations

from math import factorial
from typing import Sequence, TypeVar

Scalar = TypeVar("Scalar")


def log_derivative_stieltjes_moments(
    coefficients: Sequence[Scalar],
    *,
    order: int | None = None,
) -> tuple[Scalar, ...]:
    """Return mu_n = (-1)^n [w^n] F'(w)/F(w).

    The recurrence is exact in any scalar type supporting +, -, *, /.
    To obtain moments through order m, coefficients through a_{m+1} are
    required.
    """
    if len(coefficients) < 2:
        raise ValueError("need at least a0 and a1")
    if coefficients[0] == 0:
        raise ValueError("a0 must be nonzero")
    max_order = len(coefficients) - 2
    if order is None:
        order = max_order
    if not isinstance(order, int) or order < 0 or order > max_order:
        raise ValueError("order must satisfy 0 <= order <= len(coefficients)-2")

    a = coefficients
    phi: list[Scalar] = []
    for n in range(order + 1):
        rhs = (n + 1) * a[n + 1]
        for k in range(1, n + 1):
            rhs -= a[k] * phi[n - k]
        phi.append(rhs / a[0])
    return tuple(((-1) ** n) * value for n, value in enumerate(phi))


def hankel_matrix(
    moments: Sequence[Scalar],
    *,
    size: int,
    shift: int = 0,
) -> tuple[tuple[Scalar, ...], ...]:
    """Return [mu_{i+j+shift}]_{i,j=0}^{size-1}."""
    if not isinstance(size, int) or size < 1:
        raise ValueError("size must be a positive integer")
    if not isinstance(shift, int) or shift < 0:
        raise ValueError("shift must be a non-negative integer")
    needed = 2 * size - 2 + shift
    if needed >= len(moments):
        raise ValueError("insufficient moments for requested Hankel matrix")
    return tuple(
        tuple(moments[i + j + shift] for j in range(size))
        for i in range(size)
    )


def determinant_2x2(matrix: Sequence[Sequence[Scalar]]) -> Scalar:
    """Return the exact determinant of a 2x2 matrix."""
    if len(matrix) != 2 or any(len(row) != 2 for row in matrix):
        raise ValueError("matrix must be 2x2")
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def normalized_gamma_ratios(
    coefficients: Sequence[Scalar],
    *,
    through: int = 3,
) -> tuple[Scalar, ...]:
    """Return r_k = gamma_k/gamma_{k-1}, gamma_k=k! a_k."""
    if not isinstance(through, int) or through < 1:
        raise ValueError("through must be a positive integer")
    if len(coefficients) <= through:
        raise ValueError("insufficient coefficients")
    gamma = [factorial(k) * coefficients[k] for k in range(through + 1)]
    if any(gamma[k - 1] == 0 for k in range(1, through + 1)):
        raise ValueError("gamma denominator must be nonzero")
    return tuple(gamma[k] / gamma[k - 1] for k in range(1, through + 1))


def alpha2_ratio_gate(coefficients: Sequence[Scalar]) -> Scalar:
    """Return r1 - 2*r2 + r3, the first open SOH-G025 ratio gate."""
    r1, r2, r3 = normalized_gamma_ratios(coefficients, through=3)
    return r1 - 2 * r2 + r3


def first_s_fraction_coefficients(
    coefficients: Sequence[Scalar],
) -> tuple[Scalar, Scalar, Scalar]:
    """Return alpha0, alpha1, alpha2 for the Stieltjes S-fraction.

    With M(t)=sum mu_n t^n = (F'/F)(-t),

        M(t) = alpha0 / (1 - alpha1 t/(1 - alpha2 t/(1-...))).

    Thus alpha0=mu0, alpha1=mu1/mu0, and
    alpha2=(mu0*mu2-mu1^2)/(mu0*mu1).
    """
    moments = log_derivative_stieltjes_moments(coefficients, order=2)
    mu0, mu1, mu2 = moments
    if mu0 == 0 or mu1 == 0:
        raise ZeroDivisionError("alpha1/alpha2 require mu0 and mu1 nonzero")
    alpha0 = mu0
    alpha1 = mu1 / mu0
    alpha2 = (mu0 * mu2 - mu1 * mu1) / (mu0 * mu1)
    return alpha0, alpha1, alpha2
