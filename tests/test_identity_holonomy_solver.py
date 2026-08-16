from __future__ import annotations

import math

import pytest

from secret_of_a_half.identity_holonomy_solver import (
    DEFAULT_SOLVER,
    IdentityAxis,
    PhaseClosure,
    ClaimStatus,
    cross_factorization_24,
    information_per_projective_turn,
    kappa_from_cycle,
    route_residuals,
    solve_half_axis_routes,
    spinor_sheet,
    winding_frequency,
)


def test_identity_axis_generates_sign_and_zero() -> None:
    axis = IdentityAxis()
    assert axis.orientation(0.25) == -1
    assert axis.orientation(0.5) == 0
    assert axis.orientation(0.75) == 1
    assert axis.displacement(0.25) == -0.25
    assert axis.displacement(0.5) == 0.0
    assert axis.displacement(0.75) == 0.25
    assert axis.complement(0.2) == pytest.approx(0.8)


def test_normalized_cycle_precedes_radian_representation() -> None:
    closure = PhaseClosure(math.tau)
    assert closure.angle(0.25) == pytest.approx(math.pi / 2.0)
    assert closure.turns(math.pi) == pytest.approx(0.5)
    assert winding_frequency(12, 3) == pytest.approx(4.0)


def test_spinor_sheet_is_double_cover() -> None:
    assert spinor_sheet(0) == 1
    assert spinor_sheet(1) == -1
    assert spinor_sheet(2) == 1
    assert spinor_sheet(3) == -1


def test_four_balance_routes_select_half() -> None:
    routes = solve_half_axis_routes()
    assert set(routes) == {"complement", "entropy", "cancellation", "berry_minus_one"}
    assert all(value == pytest.approx(0.5, abs=1e-12) for value in routes.values())


def test_four_residuals_share_unique_numerical_zero_at_half() -> None:
    half = route_residuals(0.5)
    assert all(value == pytest.approx(0.0, abs=1e-12) for value in half.values())
    for sigma in (0.1, 0.25, 0.49, 0.51, 0.75, 0.9):
        residuals = route_residuals(sigma)
        assert all(value > 0.0 for value in residuals.values())


def test_exact_closure_never_uses_model_or_open_rules() -> None:
    facts = {
        "sigma_half",
        "binary_state",
        "equatorial_loop",
        "symmetric_detector",
        "half_turn_phase",
        "zeta_involution",
        "centered_zeta_chart",
        "reciprocal_chart",
        "projective_recurrence",
        "spin_half",
        "binary_information",
        "twelve_projective_cycles",
        "radian_closure",
    }
    result = DEFAULT_SOLVER.closure(facts)
    assert result.derives("complement_fixed")
    assert result.derives("entropy_max_ln2")
    assert result.derives("bloch_equator")
    assert result.derives("berry_minus_one")
    assert result.derives("exact_cancellation")
    assert result.derives("reciprocal_axis_invariant")
    assert result.derives("spinor_double_cover")
    assert not result.derives("information_per_turn_ln2_over_12")
    assert not result.derives("kappa_ln2_over_24pi")
    assert not result.derives("riemann_hypothesis")


def test_model_closure_can_reconstruct_kappa_but_not_rh() -> None:
    facts = {
        "binary_information",
        "twelve_projective_cycles",
        "radian_closure",
        "eight_mix_sectors",
        "three_flavours",
        "half_turn_phase",
    }
    result = DEFAULT_SOLVER.closure(facts, allow_model=True)
    assert result.derives("information_per_turn_ln2_over_12")
    assert result.derives("kappa_ln2_over_24pi")
    assert result.derives("twenty_four_count")
    assert result.derives("twenty_four_pi_normalization")
    assert not result.derives("riemann_hypothesis")
    assert all(step.rule.status is not ClaimStatus.OPEN for step in result.proof.values())


def test_solver_reports_open_native_closure_bridge() -> None:
    facts = {"xi_zero"}
    missing = DEFAULT_SOLVER.missing_premises("native_closed", facts, allow_model=True)
    assert missing
    assert any("canonical_zero_state" in absent for _, absent in missing)


def test_cross_factorization_and_kappa_are_numerically_consistent() -> None:
    factors = cross_factorization_24()
    assert set(factors.values()) == {24}
    assert information_per_projective_turn() == pytest.approx(math.log(2.0) / 12.0)
    assert kappa_from_cycle() == pytest.approx(math.log(2.0) / (24.0 * math.pi))
