from __future__ import annotations

import mpmath as mp
import pytest

from secret_of_a_half.phasenav_weil_arithmetic import (
    ArithmeticWeilProgram,
    default_arithmetic_program_path,
    run_arithmetic_audit,
    spectral_test_fourier,
    spectral_test_value,
)
from secret_of_a_half.phasenav_weil_probe import (
    WeilProbeProgram,
    default_program_path,
    finite_weil_matrix,
    on_axis_fixture,
)


def load_arithmetic_program() -> ArithmeticWeilProgram:
    return ArithmeticWeilProgram.load(default_arithmetic_program_path())


@pytest.fixture(scope="module")
def receipt() -> dict[str, object]:
    arithmetic = load_arithmetic_program()
    witness = WeilProbeProgram.load(default_program_path())
    reference = finite_weil_matrix(on_axis_fixture(witness), witness)
    return run_arithmetic_audit(arithmetic, spectral_reference=reference)


def test_arithmetic_profile_parses_without_zero_list() -> None:
    program = load_arithmetic_program()
    assert program.channel_count == 2
    assert program.audit_prime_cutoff > program.prime_cutoff
    assert program.equations["SPECTRAL_ZERO_INPUT"] == "NONE_FOR_ARITHMETIC_SUM"


def test_closed_fourier_transform() -> None:
    program = load_arithmetic_program()
    mp.mp.dps = 40
    left, right = program.channel_centres
    x = mp.mpf("0.1")
    numerical = mp.quad(
        lambda r: spectral_test_value(r, left, right, program)
        * mp.exp(-2j * mp.pi * x * r),
        [-mp.inf, mp.inf],
    )
    closed = spectral_test_fourier(x, left, right, program)
    assert abs(numerical - closed) < mp.mpf("1e-30")


def test_prime_cutoff_is_stable(receipt: dict[str, object]) -> None:
    assert receipt["cutoff_stability"]["pass"] is True
    assert receipt["cutoff_stability"]["max_entry_error"] < 5e-12


def test_arithmetic_sample_is_psd(receipt: dict[str, object]) -> None:
    assert receipt["psd_sample"]["pass"] is True
    assert receipt["eigenvalues"]["lambda_min"] >= -5e-12


def test_prime_side_matches_low_height_spectral_receipt(receipt: dict[str, object]) -> None:
    assert receipt["arithmetic_sum_uses_zero_list"] is False
    assert receipt["spectral_cross_check"]["pass"] is True
    assert receipt["spectral_cross_check"]["max_entry_error"] < 5e-12
