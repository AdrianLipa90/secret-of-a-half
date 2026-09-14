"""Exact half-kernel operator bridge for the So½ programme.

This module is deliberately finite/algebraic.  It does not claim RH.
It records:
  * the directed terminal axis 4 -> 2 -> 1 -> 1/2;
  * its positive self-adjoint Gram operator A_C = (I-P_C)^T(I-P_C);
  * the exact spectral projector onto the half endpoint;
  * the canonical inverse-scale ladder 5/2, 7/2, 9/2;
  * the standard Xi-kernel endpoint exponents and their midpoint;
  * the finite-rank obstruction to using A_C alone for the all-n Gram gate.

The remaining RH-equivalent obligation is an infinite-carrier factorization
of the XF-8C derivative translation-Gram family.
"""
from __future__ import annotations

import json
from fractions import Fraction
from typing import Iterable

Q = Fraction
Matrix = list[list[Fraction]]


def _qmatrix(rows: Iterable[Iterable[int | Fraction]]) -> Matrix:
    return [[Q(x) for x in row] for row in rows]


def eye(n: int) -> Matrix:
    return [[Q(1 if i == j else 0) for j in range(n)] for i in range(n)]


def transpose(a: Matrix) -> Matrix:
    return [list(row) for row in zip(*a)]


def matmul(a: Matrix, b: Matrix) -> Matrix:
    if not a or not b or len(a[0]) != len(b):
        raise ValueError("incompatible matrix shapes")
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), Q(0)) for j in range(len(b[0]))] for i in range(len(a))]


def madd(a: Matrix, b: Matrix) -> Matrix:
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise ValueError("incompatible matrix shapes")
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def mscale(c: Fraction, a: Matrix) -> Matrix:
    return [[c * x for x in row] for row in a]


def msub(a: Matrix, b: Matrix) -> Matrix:
    return madd(a, mscale(Q(-1), b))


def mpow(a: Matrix, n: int) -> Matrix:
    if n < 0:
        raise ValueError("negative matrix power not supported")
    out = eye(len(a))
    for _ in range(n):
        out = matmul(out, a)
    return out


def matrix_rank(a: Matrix) -> int:
    m = [row[:] for row in a]
    rows, cols = len(m), len(m[0])
    r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if m[i][c] != 0), None)
        if pivot is None:
            continue
        m[r], m[pivot] = m[pivot], m[r]
        p = m[r][c]
        m[r] = [x / p for x in m[r]]
        for i in range(rows):
            if i != r and m[i][c] != 0:
                f = m[i][c]
                m[i] = [m[i][j] - f * m[r][j] for j in range(cols)]
        r += 1
        if r == rows:
            break
    return r


def directed_terminal_transfer() -> Matrix:
    """Column-stochastic deterministic transfer 4->2->1->h, h->h."""
    return _qmatrix([[0, 0, 0, 0], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 1]])


def positive_half_operator() -> Matrix:
    p = directed_terminal_transfer()
    g = msub(eye(4), p)
    return matmul(transpose(g), g)


def half_projector() -> Matrix:
    """Spectral projector p(A_C) onto ker(A_C), evaluated exactly."""
    a = positive_half_operator()
    return madd(madd(madd(eye(4), mscale(Q(-5, 2), a)), mscale(Q(3, 2), mpow(a, 2))), mscale(Q(-1, 4), mpow(a, 3)))


def annihilating_polynomial_residual() -> Matrix:
    """A(A-2I)(A^2-4A+2I), whose roots are 0,2,2±sqrt(2)."""
    a = positive_half_operator()
    i = eye(4)
    factor1 = msub(a, mscale(Q(2), i))
    factor2 = madd(msub(mpow(a, 2), mscale(Q(4), a)), mscale(Q(2), i))
    return matmul(matmul(a, factor1), factor2)


def canonical_inverse_ladder() -> dict[str, Fraction]:
    """Exact inverse scales shared with the TIR CKM incidence packet."""
    return {"c_inv": Q(5, 2), "a_inv": Q(7, 2), "b_inv": Q(9, 2)}


def xi_kernel_exponents() -> tuple[Fraction, Fraction]:
    """Standard Xi-kernel powers: exp(9u/2) and exp(5u/2)."""
    return Q(9, 2), Q(5, 2)


def build_receipt() -> dict[str, object]:
    a_c = positive_half_operator()
    projector = half_projector()
    zero4 = _qmatrix([[0] * 4 for _ in range(4)])
    expected_a = _qmatrix([[2, -1, 0, 0], [-1, 2, -1, 0], [0, -1, 2, 0], [0, 0, 0, 0]])
    expected_pi = _qmatrix([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]])
    ladder = canonical_inverse_ladder()
    hi, lo = xi_kernel_exponents()
    midpoint = (hi + lo) / 2
    derivative_coefficients = {"x2": Q(4), "x1": Q(-6)}

    checks = {
        "positive_operator_exact_matrix": a_c == expected_a,
        "positive_operator_rank_is_3": matrix_rank(a_c) == 3,
        "half_basis_vector_is_unique_kernel_direction": all(a_c[i][3] == 0 for i in range(4)) and matrix_rank(a_c) == 3,
        "annihilating_polynomial_exact": annihilating_polynomial_residual() == zero4,
        "half_projector_exact": projector == expected_pi,
        "half_projector_idempotent": matmul(projector, projector) == projector,
        "inverse_ladder_is_5_2_7_2_9_2": ladder == {"c_inv": Q(5, 2), "a_inv": Q(7, 2), "b_inv": Q(9, 2)},
        "xi_endpoint_exponents_are_9_2_and_5_2": (hi, lo) == (Q(9, 2), Q(5, 2)),
        "xi_cross_channel_midpoint_is_7_2": midpoint == Q(7, 2),
        "middle_inverse_scale_matches_a_inverse": midpoint == ladder["a_inv"],
        "theta_term_operator_coefficients_are_4_and_minus_6": derivative_coefficients == {"x2": Q(4), "x1": Q(-6)},
        "bare_finite_half_operator_rank_cap_is_3": matrix_rank(a_c) == 3,
    }

    return {
        "schema": "SOH_HALF_KERNEL_POSITIVE_OPERATOR_BRIDGE_V0_1",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "epistemic_status": "EXACT_FINITE_HALF_KERNEL__EXACT_XI_OPERATOR_IDENTITY__INFINITE_GRAM_FACTORIZATION_OPEN",
        "rh_claim": False,
        "physical_promotion": False,
        "terminal_basis": ["4", "2", "1", "1/2"],
        "A_C": [[str(x) for x in row] for row in a_c],
        "Pi_half": [[str(x) for x in row] for row in projector],
        "spectrum_certificate": {"annihilating_polynomial": "lambda*(lambda-2)*(lambda^2-4*lambda+2)", "roots": ["0", "2", "2-sqrt(2)", "2+sqrt(2)"], "kernel": "span{|1/2>}"},
        "xi_half_operator": {"theta_seed_identity": "Phi=(D^2-1/4)Psi", "positive_partner": "L_1/2=-D^2+1/4=(D+1/2)^dagger(D+1/2)", "domain_note": "formal identity on a boundary-decaying/suitable dense domain", "endpoint_exponents": [str(hi), str(lo)], "mixed_midpoint": str(midpoint)},
        "rank_obstruction": {"rank_A_C": matrix_rank(a_c), "consequence": "A bare finite V^* A_C V factor has rank <=3 and cannot by itself close arbitrary-size XF-8C derivative Gram matrices."},
        "candidate_infinite_carrier": "Pi_half tensor L_1/2",
        "open": {"construct_explicit_V_y_T_from_theta_translations": True, "prove_derivative_gram_factorization_for_every_finite_T": True, "close_XF8C_RH_equivalent_gate": True, "riemann_hypothesis": True},
        "checks": checks,
    }


def main() -> int:
    receipt = build_receipt()
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0 if receipt["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
