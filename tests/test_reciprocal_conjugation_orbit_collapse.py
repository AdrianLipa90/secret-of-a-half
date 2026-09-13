from __future__ import annotations

import cmath
import math


def omega(s: complex) -> complex:
    return s / (1.0 - s)


def compact_q(u: complex) -> float:
    r = abs(u)
    return r / (1.0 + r)


def delta_rc(u: complex) -> float:
    return abs(1.0 / u - u.conjugate()) ** 2


def delta_radial(u: complex) -> float:
    r = abs(u)
    return (r - 1.0 / r) ** 2


def delta_q(u: complex) -> float:
    q = compact_q(u)
    return (2.0 * q - 1.0) ** 2 / (q * q * (1.0 - q) ** 2)


def test_functional_reflection_is_reciprocal() -> None:
    for s in [0.2 + 3.1j, 0.5 + 14.134725j, 0.73 - 8.2j]:
        u = omega(s)
        assert abs(omega(1.0 - s) - 1.0 / u) < 1e-12


def test_conjugation_commutes_with_projective_coordinate() -> None:
    for s in [0.2 + 3.1j, 0.5 + 14.134725j, 0.73 - 8.2j]:
        assert abs(omega(s.conjugate()) - omega(s).conjugate()) < 1e-12


def test_defect_forms_are_identical() -> None:
    for u in [0.4 + 0.9j, 1.2 - 0.7j, -0.3 + 2.4j]:
        assert math.isclose(delta_rc(u), delta_radial(u), rel_tol=1e-12, abs_tol=1e-12)
        assert math.isclose(delta_rc(u), delta_q(u), rel_tol=1e-12, abs_tol=1e-12)


def test_critical_line_has_zero_defect() -> None:
    for t in [0.1, 1.0, 14.134725, 100.0]:
        s = 0.5 + 1j * t
        u = omega(s)
        assert math.isclose(abs(u), 1.0, rel_tol=1e-12, abs_tol=1e-12)
        assert delta_rc(u) < 1e-24
        assert abs(1.0 / u - u.conjugate()) < 1e-12


def test_off_axis_points_have_positive_defect() -> None:
    for s in [0.2 + 14j, 0.4 + 8j, 0.7 - 9j]:
        assert delta_rc(omega(s)) > 0.0


def test_reciprocal_fixedness_is_not_rh_condition() -> None:
    # I(u)=u would force u^2=1. The RH locus instead requires I(u)=conj(u).
    for theta in [0.3, 1.1, 2.2]:
        u = cmath.exp(1j * theta)
        assert abs(1.0 / u - u.conjugate()) < 1e-12
        assert abs(1.0 / u - u) > 1e-3
