from __future__ import annotations

from pathlib import Path

import numpy as np

from secret_of_a_half.phasenav_weil_hermite_core import HermiteLadderProgram
from secret_of_a_half.phasenav_weil_hermite_arithmetic import (
    arithmetic_rectangular_components,
)

ROOT = Path(__file__).resolve().parents[1]
PROGRAM_PATH = ROOT / "construction" / "phasenav" / "secret_of_half_weil_hermite_ladder.pnv"


def program() -> HermiteLadderProgram:
    return HermiteLadderProgram.load(PROGRAM_PATH)


def norm2(matrix: np.ndarray) -> float:
    return float(np.linalg.norm(matrix, ord=2))


def test_full_rectangular_block_is_component_sum() -> None:
    profile = program()
    parts = arithmetic_rectangular_components(
        profile,
        left_orders=range(0, 3),
        right_orders=range(3, profile.max_basis_size),
        prime_cutoff=profile.audit_prime_cutoff,
    )
    explicit = parts.pole + parts.conductor + parts.archimedean + parts.prime
    assert np.max(np.abs(parts.total - explicit)) < 1e-14


def test_full_block_obeys_operator_triangle_inequality_for_all_splits() -> None:
    profile = program()
    for split in range(1, profile.max_basis_size):
        parts = arithmetic_rectangular_components(
            profile,
            left_orders=range(0, split),
            right_orders=range(split, profile.max_basis_size),
            prime_cutoff=profile.audit_prime_cutoff,
        )
        full = norm2(parts.total)
        envelope = sum(
            norm2(component)
            for component in (parts.pole, parts.conductor, parts.archimedean, parts.prime)
        )
        assert full <= envelope + 1e-12


def test_cancellation_diagnostic_does_not_consume_zero_list() -> None:
    profile = program()
    assert profile.equations["SPECTRAL_ZERO_INPUT"] == "NONE_FOR_ARITHMETIC_SUM"
