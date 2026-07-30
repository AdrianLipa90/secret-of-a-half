from __future__ import annotations

import math
from pathlib import Path

import mpmath as mp
import numpy as np

from secret_of_a_half.phasenav_weil_hermite_ladder import (
    HermiteLadderProgram,
    arithmetic_matrix,
    hermite_linearization_terms,
    kernel_fourier_closed,
    kernel_value,
    physicists_hermite,
    run_ladder_audit,
    spectral_fixture_matrix,
)

ROOT = Path(__file__).resolve().parents[1]
PROGRAM_PATH = ROOT / "construction" / "phasenav" / "secret_of_half_weil_hermite_ladder.pnv"


def program() -> HermiteLadderProgram:
    return HermiteLadderProgram.load(PROGRAM_PATH)


def test_native_profile_is_zero_list_free() -> None:
    profile = program()
    assert profile.max_basis_size == 6
    assert profile.equations["SPECTRAL_ZERO_INPUT"] == "NONE_FOR_ARITHMETIC_SUM"
    assert profile.equations["BASE_HEAD"].startswith("5c4883d")


def test_physicists_hermite_recurrence_values() -> None:
    x = 0.37
    assert abs(physicists_hermite(0, x) - 1) < 1e-15
    assert abs(physicists_hermite(1, x) - 2 * x) < 1e-15
    assert abs(physicists_hermite(2, x) - (4 * x * x - 2)) < 1e-15
    assert abs(physicists_hermite(3, x) - (8 * x**3 - 12 * x)) < 1e-15


def test_linearization_identity() -> None:
    x = 0.23
    for left in range(5):
        for right in range(5):
            lhs = physicists_hermite(left, x) * physicists_hermite(right, x)
            rhs = sum(
                coefficient * physicists_hermite(order, x)
                for order, coefficient in hermite_linearization_terms(left, right)
            )
            assert abs(lhs - rhs) < 1e-10


def test_fourier_transform_matches_direct_quadrature() -> None:
    profile = program()
    mp.mp.dps = 40
    for left, right, frequency in [(0, 0, 0.17), (1, 2, -0.11), (3, 2, 0.08)]:
        direct = mp.quad(
            lambda r: kernel_value(left, right, r, profile)
            * mp.e ** (-2j * mp.pi * frequency * r),
            [-mp.inf, profile.target_ordinate, mp.inf],
        )
        closed = kernel_fourier_closed(frequency, left, right, profile)
        assert abs(complex(direct) - closed) < profile.fourier_tolerance


def test_fourier_zero_is_orthonormality_matrix() -> None:
    profile = program()
    for left in range(profile.max_basis_size):
        for right in range(profile.max_basis_size):
            expected = 1.0 if left == right else 0.0
            assert abs(kernel_fourier_closed(0.0, left, right, profile) - expected) < 1e-12


def test_arithmetic_matrix_is_hermitian() -> None:
    profile = program()
    matrix, _ = arithmetic_matrix(profile, basis_size=4, prime_cutoff=profile.prime_cutoff)
    assert np.max(np.abs(matrix - matrix.conjugate().T)) < 1e-12


def test_ladder_receipt_is_internally_consistent() -> None:
    receipt = run_ladder_audit(program())
    assert receipt["arithmetic_sum_uses_zero_list"] is False
    assert receipt["orthonormality_error"] < 1e-12
    assert len(receipt["sections"]) == 6
    assert receipt["claim_boundary"]["proof_of_rh"] is False
    for expected_size, section in enumerate(receipt["sections"], start=1):
        assert section["basis_size"] == expected_size
        assert math.isfinite(section["lambda_min"])
        assert math.isfinite(section["lambda_max"])


def test_dense_ladder_detects_synthetic_off_axis_quartet() -> None:
    profile = program()
    on_axis = spectral_fixture_matrix(profile, basis_size=profile.max_basis_size)
    off_axis = spectral_fixture_matrix(
        profile,
        basis_size=profile.max_basis_size,
        off_axis_delta=profile.synthetic_off_axis_delta,
    )
    on_min = float(np.linalg.eigvalsh(on_axis)[0])
    off_min = float(np.linalg.eigvalsh(off_axis)[0])
    assert on_min >= -profile.psd_tolerance
    assert off_min < profile.synthetic_negativity_threshold
