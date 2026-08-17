from fractions import Fraction
import math

import pytest

from secret_of_a_half.uroboros import (
    LOG_UROBOROS_SCALE,
    UROBOROS_SCALE,
    collatz_step_s_from_integer,
    collatz_step_x,
    exact_halving_s,
    exact_odd_collatz_s,
    exact_x_to_s,
    halving_s,
    halving_s_inverse,
    inverse_about_half_x,
    invert_u,
    odd_collatz_s,
    riemann_reflection_s,
    s_to_x,
    torus_coordinate,
    x_to_s,
    x_to_u,
)


def test_half_layer_maps_to_riemann_half() -> None:
    assert exact_x_to_s(Fraction(1, 2)) == Fraction(1, 2)
    assert x_to_u(0.5) == pytest.approx(1.0)
    assert x_to_s(0.5) == pytest.approx(0.5)


def test_half_centered_inversion_conjugates_to_riemann_reflection() -> None:
    for x in [0.125, 0.5, 1.0, 2.0, 16.0]:
        lhs = x_to_s(inverse_about_half_x(x))
        rhs = riemann_reflection_s(x_to_s(x))
        assert lhs == pytest.approx(rhs, rel=0, abs=1e-14)
        assert invert_u(x_to_u(x)) == pytest.approx(x_to_u(inverse_about_half_x(x)))


def test_inversion_is_an_involution() -> None:
    for x in [0.125, 0.5, 1.0, 7.0]:
        assert inverse_about_half_x(inverse_about_half_x(x)) == pytest.approx(x)


def test_halving_conjugacy_exact_on_fundamental_chain() -> None:
    chain = [Fraction(16), Fraction(8), Fraction(4), Fraction(2), Fraction(1), Fraction(1, 2)]
    mapped = [exact_x_to_s(x) for x in chain]
    expected = [
        Fraction(32, 33),
        Fraction(16, 17),
        Fraction(8, 9),
        Fraction(4, 5),
        Fraction(2, 3),
        Fraction(1, 2),
    ]
    assert mapped == expected
    for current, nxt in zip(mapped, mapped[1:]):
        assert exact_halving_s(current) == nxt


def test_standard_collatz_branches_are_exactly_conjugated() -> None:
    for n in range(1, 33):
        s = exact_x_to_s(Fraction(n))
        transformed = exact_halving_s(s) if n % 2 == 0 else exact_odd_collatz_s(s)
        expected = exact_x_to_s(Fraction(collatz_step_x(n)))
        assert transformed == expected
        assert collatz_step_s_from_integer(n) == pytest.approx(float(expected))


def test_dihedral_relation_j_h_j_equals_h_inverse() -> None:
    for s in [0.1, 0.25, 0.5, 0.75, 0.9]:
        lhs = riemann_reflection_s(halving_s(riemann_reflection_s(s)))
        rhs = halving_s_inverse(s)
        assert lhs == pytest.approx(rhs, rel=0, abs=1e-14)


def test_round_trip_s_x() -> None:
    for x in [0.125, 0.5, 1.0, 3.0, 16.0]:
        assert s_to_x(x_to_s(x)) == pytest.approx(x, rel=1e-14)


def test_uroboros_scale_is_2_to_fifth() -> None:
    assert UROBOROS_SCALE == 2**5
    assert LOG_UROBOROS_SCALE == pytest.approx(math.log(32.0))


def test_torus_coordinate_identifies_scale_32() -> None:
    for u in [0.3 + 0.7j, 1.0 + 0.2j, -2.0 + 3.0j]:
        a = torus_coordinate(u)
        b = torus_coordinate(32.0 * u)
        assert a.radial == pytest.approx(b.radial, abs=1e-12)
        assert a.phase == pytest.approx(b.phase, abs=1e-12)


def test_torus_coordinate_identifies_full_phase_turn() -> None:
    u = 1.2 + 0.4j
    a = torus_coordinate(u)
    b = torus_coordinate(u * complex(math.cos(2 * math.pi), math.sin(2 * math.pi)))
    assert a.radial == pytest.approx(b.radial, abs=1e-12)
    assert a.phase == pytest.approx(b.phase, abs=1e-12)


@pytest.mark.parametrize("bad", [0, -1, float("inf"), float("nan")])
def test_positive_domain_maps_fail_closed(bad) -> None:
    with pytest.raises(ValueError):
        x_to_s(bad)


def test_torus_coordinate_rejects_zero() -> None:
    with pytest.raises(ValueError):
        torus_coordinate(0)
