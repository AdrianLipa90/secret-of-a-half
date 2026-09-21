from __future__ import annotations

import numpy as np
import pytest

from secret_of_a_half.c005_interval_schur import (
    absolute_radius_operator_norm_upper,
    continuation_cell,
    cover_is_strict,
    hermitian_interval_min_eigenvalue,
    interval_gate_map,
    interval_schur_from_matrix_enclosures,
    rectangular_interval_norm_upper,
    scalar_block_gap_lower,
    schur_interval_certificate,
)


def test_absolute_radius_operator_norm_upper_is_safe() -> None:
    radius = np.array([[0.1, 0.2], [0.3, 0.4]])
    bound = absolute_radius_operator_norm_upper(radius)
    # sqrt(max-row-sum * max-column-sum)
    expected = np.sqrt(0.7 * 0.6)
    assert bound == pytest.approx(expected)


def test_hermitian_interval_min_eigenvalue_certifies_perturbation() -> None:
    midpoint = np.array([[3.0, 0.25], [0.25, 2.0]], dtype=complex)
    radius = np.full((2, 2), 0.01)
    cert = hermitian_interval_min_eigenvalue(midpoint, radius)
    assert cert.certified_min_eigenvalue == pytest.approx(
        cert.midpoint_min_eigenvalue - cert.perturbation_norm_upper
    )
    assert cert.positive


def test_rectangular_interval_norm_upper() -> None:
    midpoint = np.array([[0.25, -0.1], [0.0, 0.2]], dtype=complex)
    radius = np.full((2, 2), 0.005)
    cert = rectangular_interval_norm_upper(midpoint, radius)
    assert cert.certified_norm_upper >= cert.midpoint_norm


def test_schur_interval_certificate_strict_case() -> None:
    cert = schur_interval_certificate(2.0, 0.5, 3.0)
    assert cert.effective_floor_lower == pytest.approx(2.0 - 0.25 / 3.0)
    assert cert.scalar_block_gap_lower == pytest.approx(
        scalar_block_gap_lower(2.0, 0.5, 3.0)
    )
    assert cert.strict


def test_end_to_end_matrix_interval_schur_certificate() -> None:
    low_mid = np.array([[3.0, 0.1], [0.1, 2.5]], dtype=complex)
    high_mid = np.array([[4.0, 0.2], [0.2, 3.5]], dtype=complex)
    coupling_mid = np.array([[0.15, 0.05], [0.1, 0.1]], dtype=complex)
    low_rad = np.full((2, 2), 1e-3)
    high_rad = np.full((2, 2), 1e-3)
    coupling_rad = np.full((2, 2), 1e-3)
    low, coupling, high, schur = interval_schur_from_matrix_enclosures(
        low_mid,
        low_rad,
        coupling_mid,
        coupling_rad,
        high_mid,
        high_rad,
    )
    assert low.positive
    assert high.positive
    assert coupling.certified_norm_upper > 0
    assert schur.strict


def test_continuation_cell_and_cover() -> None:
    cells = [
        continuation_cell(0.5, 0.5, 1.0, 0.5),
        continuation_cell(1.5, 0.5, 1.0, 0.5),
        continuation_cell(2.5, 0.5, 1.0, 0.5),
    ]
    assert all(cell.strict for cell in cells)
    assert cover_is_strict(cells, 0.0, 3.0)


def test_cover_rejects_gap_or_nonpositive_cell() -> None:
    gap_cells = [
        continuation_cell(0.25, 0.25, 1.0, 0.1),
        continuation_cell(0.9, 0.1, 1.0, 0.1),
    ]
    assert not cover_is_strict(gap_cells, 0.0, 1.0)

    bad = [continuation_cell(0.5, 0.5, 0.1, 1.0)]
    assert not cover_is_strict(bad, 0.0, 1.0)


def test_gate_map_keeps_physical_interval_inputs_open() -> None:
    gates = interval_gate_map()
    assert gates["proof_of_rh"] is False
    assert (
        "rigorous interval enclosures for localized operator matrix entries as functions of a"
        in gates["open"]
    )


def test_invalid_interval_inputs_fail_closed() -> None:
    with pytest.raises(ValueError):
        hermitian_interval_min_eigenvalue(np.eye(2), np.ones((3, 3)))
    with pytest.raises(ValueError):
        schur_interval_certificate(1.0, 0.1, 0.0)
    with pytest.raises(ValueError):
        continuation_cell(1.0, -0.1, 1.0, 1.0)
