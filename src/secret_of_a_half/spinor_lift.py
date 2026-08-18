"""SOH-G013 Pauli/SU(2) spinor lift of the G012 projective operator algebra.

The projective maps R(u)=1/u, E(u)=-u, and N(u)=-1/u form V4.
Their determinant-one unitary lifts generate the quaternion group Q8.  This is
an exact CP1/SU(2) double-cover statement and makes no claim about xi zero
locations or RH.
"""
from __future__ import annotations

import mpmath as mp


def identity2() -> mp.matrix:
    return mp.matrix([[1, 0], [0, 1]])


def sigma_x() -> mp.matrix:
    return mp.matrix([[0, 1], [1, 0]])


def sigma_y() -> mp.matrix:
    return mp.matrix([[0, -mp.j], [mp.j, 0]])


def sigma_z() -> mp.matrix:
    return mp.matrix([[1, 0], [0, -1]])


def scale_matrix(c: complex | mp.mpc | mp.mpf, a: mp.matrix) -> mp.matrix:
    return mp.matrix([[c * a[0, 0], c * a[0, 1]], [c * a[1, 0], c * a[1, 1]]])


def add_matrix(a: mp.matrix, b: mp.matrix) -> mp.matrix:
    return mp.matrix([[a[0, 0] + b[0, 0], a[0, 1] + b[0, 1]], [a[1, 0] + b[1, 0], a[1, 1] + b[1, 1]]])


def dagger(a: mp.matrix) -> mp.matrix:
    return mp.matrix(
        [
            [mp.conj(a[0, 0]), mp.conj(a[1, 0])],
            [mp.conj(a[0, 1]), mp.conj(a[1, 1])],
        ]
    )


def determinant2(a: mp.matrix) -> mp.mpc:
    return a[0, 0] * a[1, 1] - a[0, 1] * a[1, 0]


def matrix_residual(a: mp.matrix, b: mp.matrix) -> mp.mpf:
    return max(abs(a[r, c] - b[r, c]) for r in range(2) for c in range(2))


def pauli_spinor_lifts() -> dict[str, mp.matrix]:
    """Return the chosen SU(2) lifts of R, E, N.

    R~=i sigma_x, E~=i sigma_z, N~=i sigma_y.  With this convention
    R~ E~=N~, whereas E~ R~=-N~.  The central sign is projectively invisible.
    """
    return {
        "R": scale_matrix(mp.j, sigma_x()),
        "E": scale_matrix(mp.j, sigma_z()),
        "N": scale_matrix(mp.j, sigma_y()),
    }


def q8_elements() -> dict[str, mp.matrix]:
    lifts = pauli_spinor_lifts()
    ident = identity2()
    return {
        "+I": ident,
        "-I": scale_matrix(-1, ident),
        "+R": lifts["R"],
        "-R": scale_matrix(-1, lifts["R"]),
        "+E": lifts["E"],
        "-E": scale_matrix(-1, lifts["E"]),
        "+N": lifts["N"],
        "-N": scale_matrix(-1, lifts["N"]),
    }


def projective_action(matrix: mp.matrix, u: complex | mp.mpf | mp.mpc) -> mp.mpc | mp.mpf:
    """Apply a 2x2 matrix to CP1 using u -> (a u+b)/(c u+d).

    ``mp.inf`` is accepted as the point at infinity and returned when the image
    denominator vanishes.
    """
    if u == mp.inf:
        numerator = matrix[0, 0]
        denominator = matrix[1, 0]
    else:
        u = mp.mpc(u)
        if not mp.isfinite(u):
            raise ValueError("u must be finite or mp.inf")
        numerator = matrix[0, 0] * u + matrix[0, 1]
        denominator = matrix[1, 0] * u + matrix[1, 1]
    if denominator == 0:
        return mp.inf
    return numerator / denominator


def projective_class_label(matrix: mp.matrix, *, tol: float | mp.mpf = mp.mpf("1e-40")) -> str:
    """Return the V4 class I/R/E/N after quotienting the central sign +/-I."""
    tol = mp.mpf(tol)
    lifts = pauli_spinor_lifts()
    candidates = {"I": identity2(), **lifts}
    for label, representative in candidates.items():
        if matrix_residual(matrix, representative) <= tol:
            return label
        if matrix_residual(matrix, scale_matrix(-1, representative)) <= tol:
            return label
    raise ValueError("matrix is not in the Q8 lift subgroup at the requested tolerance")


def pauli_fixed_pairs() -> dict[str, tuple[mp.mpc | mp.mpf, mp.mpc | mp.mpf]]:
    """Return CP1 fixed pairs of the three projective Pauli operators."""
    return {
        "R": (mp.mpf(1), mp.mpf(-1)),
        "E": (mp.mpf(0), mp.inf),
        "N": (mp.j, -mp.j),
    }


def bloch_vector_from_u(u: complex | mp.mpf | mp.mpc) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
    """Bloch vector for the homogeneous spinor (u,1)^T.

    With this chart convention the components are
      x=2 Re(u)/(1+|u|^2), y=-2 Im(u)/(1+|u|^2),
      z=(|u|^2-1)/(1+|u|^2).
    The point u=infinity maps to the north pole (0,0,1).
    """
    if u == mp.inf:
        return mp.mpf(0), mp.mpf(0), mp.mpf(1)
    u = mp.mpc(u)
    if not mp.isfinite(u):
        raise ValueError("u must be finite or mp.inf")
    norm = 1 + abs(u) ** 2
    return (
        2 * mp.re(u) / norm,
        -2 * mp.im(u) / norm,
        (abs(u) ** 2 - 1) / norm,
    )


def pi_rotation_lifts() -> dict[str, mp.matrix]:
    """Return U_j(pi)=exp(-i*pi*sigma_j/2)=-i sigma_j.

    Each differs from the chosen +i*sigma_j lift by the central element -I,
    hence has the same projective CP1 action.
    """
    return {
        "R": scale_matrix(-mp.j, sigma_x()),
        "E": scale_matrix(-mp.j, sigma_z()),
        "N": scale_matrix(-mp.j, sigma_y()),
    }
