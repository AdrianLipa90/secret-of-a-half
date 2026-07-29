from __future__ import annotations

import math
from pathlib import Path

from secret_of_a_half.phasenav_theta_bridge import (
    PhaseNavProgram,
    closure_defect,
    covariance_residual,
    native_closed,
    phase_state,
    theta_detector,
    zeta_involution,
)

PROGRAM = PhaseNavProgram.load(
    Path(__file__).resolve().parents[1]
    / "construction"
    / "phasenav"
    / "secret_of_half_theta_bridge.pnv"
)


def test_native_program_is_36d_with_18_pairs() -> None:
    assert PROGRAM.vector_dim == 36
    assert PROGRAM.pair_count == 18
    assert len(PROGRAM.nodes) == 18


def test_involution_is_an_involution() -> None:
    s = 0.31 + 17.25j
    assert abs(zeta_involution(zeta_involution(s)) - s) < 1e-15


def test_phase_state_has_36_rotors() -> None:
    assert len(phase_state(0.5 + 14.0j, PROGRAM).rotors) == 36


def test_exact_phasenav_covariance() -> None:
    assert covariance_residual(0.31 + 17.25j, PROGRAM) < 2e-18


def test_closure_defect_is_exact_half_axis_distance_squared() -> None:
    for sigma in (0.1, 0.25, 0.5, 0.73, 0.9):
        state = phase_state(sigma + 11.0j, PROGRAM)
        expected = (sigma - 0.5) ** 2
        assert math.isclose(closure_defect(state), expected, rel_tol=2e-14, abs_tol=2e-16)


def test_native_closure_holds_only_on_half_axis() -> None:
    assert native_closed(phase_state(0.5 + 14.0j, PROGRAM))
    assert not native_closed(phase_state(0.500001 + 14.0j, PROGRAM))


def test_detector_respects_functional_equation_at_finite_resolution() -> None:
    s = 0.27 + 9.5j
    left = theta_detector(phase_state(s, PROGRAM))
    right = theta_detector(phase_state(1.0 - s, PROGRAM))
    assert abs(left - right) < 1e-14


def test_detector_matches_known_xi_half_value() -> None:
    # xi(1/2) = 0.497120778188314109...; finite 18-pair error is < 4e-10.
    value = theta_detector(phase_state(0.5 + 0.0j, PROGRAM))
    assert abs(value - 0.4971207781883141) < 4e-10


def test_detector_matches_xi_at_two() -> None:
    # xi(2) = pi/6.
    value = theta_detector(phase_state(2.0 + 0.0j, PROGRAM))
    assert abs(value - math.pi / 6.0) < 1e-9


def test_first_known_zero_is_small_for_low_height_profile() -> None:
    first_zero = 0.5 + 14.134725141734693j
    value = theta_detector(phase_state(first_zero, PROGRAM))
    assert abs(value) < 1e-8
