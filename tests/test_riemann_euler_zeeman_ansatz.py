from __future__ import annotations

import cmath
import math
import unittest


SIGMA_X = ((0j, 1 + 0j), (1 + 0j, 0j))
SIGMA_Z = ((1 + 0j, 0j), (0j, -1 + 0j))
IDENTITY = ((1 + 0j, 0j), (0j, 1 + 0j))


def matmul(a, b):
    return (
        (
            a[0][0] * b[0][0] + a[0][1] * b[1][0],
            a[0][0] * b[0][1] + a[0][1] * b[1][1],
        ),
        (
            a[1][0] * b[0][0] + a[1][1] * b[1][0],
            a[1][0] * b[0][1] + a[1][1] * b[1][1],
        ),
    )


def conjugate(a):
    return tuple(tuple(v.conjugate() for v in row) for row in a)


def assert_matrix_close(testcase, a, b, places=12):
    for i in range(2):
        for j in range(2):
            testcase.assertAlmostEqual(a[i][j].real, b[i][j].real, places=places)
            testcase.assertAlmostEqual(a[i][j].imag, b[i][j].imag, places=places)


def omega(s: complex) -> complex:
    return s / (1 - s)


def riemann_K(s: complex) -> complex:
    return 1 - s.conjugate()


def radial_B(s: complex) -> float:
    return math.log(abs(omega(s)))


def h_zeeman(B: float, *, E0: float = 2.0, coupling: float = 3.0):
    return (
        (E0 + coupling * B + 0j, 0j),
        (0j, E0 - coupling * B + 0j),
    )


def euler_lift(theta: float):
    return (
        (cmath.exp(0.5j * theta), 0j),
        (0j, cmath.exp(-0.5j * theta)),
    )


def anti_linear_K_matrix_action(a):
    # K = sigma_x C, hence K A K^{-1} = sigma_x conjugate(A) sigma_x.
    return matmul(SIGMA_X, matmul(conjugate(a), SIGMA_X))


class RiemannEulerZeemanAnsatzTests(unittest.TestCase):
    def test_projective_involution(self):
        for s in (0.2 + 3.0j, 0.4 + 8.0j, 0.7 + 5.0j):
            lhs = omega(riemann_K(s))
            rhs = 1 / omega(s).conjugate()
            self.assertAlmostEqual(lhs.real, rhs.real, places=12)
            self.assertAlmostEqual(lhs.imag, rhs.imag, places=12)

    def test_B_is_odd_under_riemann_involution(self):
        for s in (0.2 + 3.0j, 0.4 + 8.0j, 0.7 + 5.0j):
            self.assertAlmostEqual(radial_B(riemann_K(s)), -radial_B(s), places=12)

    def test_critical_line_is_exact_degeneracy_locus(self):
        coupling = 1.7
        for t in (0.0, 1.0, 14.134725141734693, 50.0):
            B = radial_B(0.5 + 1j * t)
            self.assertAlmostEqual(B, 0.0, places=12)
            H = h_zeeman(B, coupling=coupling)
            self.assertAlmostEqual(H[0][0].real, H[1][1].real, places=12)

    def test_linear_doublet_splitting(self):
        for B in (-1.25, -0.1, 0.0, 0.3, 2.0):
            E0 = 4.0
            coupling = 2.5
            H = h_zeeman(B, E0=E0, coupling=coupling)
            delta = abs(H[0][0].real - H[1][1].real)
            self.assertAlmostEqual(delta, 2 * abs(coupling * B), places=12)

    def test_K_exchanges_split_branches(self):
        for B in (-1.0, -0.25, 0.4, 1.5):
            transformed = anti_linear_K_matrix_action(h_zeeman(B))
            assert_matrix_close(self, transformed, h_zeeman(-B))

    def test_imaginary_potential_euler_layer_is_K_invariant(self):
        for theta in (-2.3, -0.5, 0.0, 1.0, math.pi, 5.0):
            U = euler_lift(theta)
            transformed = anti_linear_K_matrix_action(U)
            assert_matrix_close(self, transformed, U)


if __name__ == "__main__":
    unittest.main()
