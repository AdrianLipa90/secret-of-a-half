from __future__ import annotations

import math
from pathlib import Path

import mpmath as mp
import numpy as np

from secret_of_a_half.phasenav_weil_hermite_core import HermiteLadderProgram
from secret_of_a_half.phasenav_weil_prime_tail import (
    PrimeTailProgram,
    entry_bound_matrix,
    entry_tail_bound,
    monotonicity_margin,
    operator_norm_tail_bound,
    prime_shell_entry,
    reciprocal_tail_integrand,
    run_prime_tail_certificate,
    tail_term_integral_gamma,
    tail_term_integral_log,
    tail_term_integral_reciprocal,
)

ROOT = Path(__file__).resolve().parents[1]
TAIL_PATH = ROOT / "construction/phasenav/secret_of_half_weil_prime_tail_certificate.pnv"
HERMITE_PATH = ROOT / "construction/phasenav/secret_of_half_weil_hermite_ladder.pnv"


def programs() -> tuple[PrimeTailProgram, HermiteLadderProgram]:
    return PrimeTailProgram.load(TAIL_PATH), HermiteLadderProgram.load(HERMITE_PATH)


def test_native_profile_parses_and_declares_reciprocal_log_map() -> None:
    tail, _ = programs()
    assert tail.max_basis_size == 6
    assert tail.tail_cutoff == 100_000
    assert tail.gaussian_width == 0.8
    assert "1 / LOG_X" in tail.equations["RECIPROCAL_MAP"]
    assert tail.equations["SPECTRAL_ZERO_INPUT"] == "NONE"


def test_integral_test_is_monotone_for_every_declared_degree() -> None:
    tail, _ = programs()
    max_degree = 2 * (tail.max_basis_size - 1)
    margins = [
        monotonicity_margin(d, tail.tail_cutoff, tail.gaussian_width)
        for d in range(max_degree + 1)
    ]
    assert min(margins) > 8.0


def test_gamma_log_and_reciprocal_integrals_agree() -> None:
    tail, _ = programs()
    mp.mp.dps = tail.mp_dps
    for degree in (0, 4, 10):
        gamma = tail_term_integral_gamma(degree, tail.tail_cutoff, tail.gaussian_width)
        direct = tail_term_integral_log(degree, tail.tail_cutoff, tail.gaussian_width)
        reciprocal = tail_term_integral_reciprocal(
            degree, tail.tail_cutoff, tail.gaussian_width
        )
        assert abs(gamma - direct) / abs(gamma) < mp.mpf("1e-35")
        assert abs(gamma - reciprocal) / abs(gamma) < mp.mpf("1e-35")


def test_reciprocal_integrand_has_flat_zero_endpoint() -> None:
    tail, _ = programs()
    assert reciprocal_tail_integrand(0, 10, tail.gaussian_width) == 0
    values = [
        reciprocal_tail_integrand(mp.mpf(10) ** (-power), 10, tail.gaussian_width)
        for power in (1, 2, 3)
    ]
    assert all(value >= 0 for value in values)
    assert values[2] < values[1] < values[0]


def test_entry_bound_matrix_is_symmetric_and_positive() -> None:
    tail, _ = programs()
    bounds = entry_bound_matrix(
        tail.max_basis_size, tail.tail_cutoff, tail.gaussian_width
    )
    assert np.all(bounds >= 0.0)
    assert np.allclose(bounds, bounds.T, rtol=0.0, atol=0.0)
    assert bounds[5, 5] == np.max(bounds)


def test_declared_operator_norm_certificate_is_below_target() -> None:
    tail, _ = programs()
    bound = operator_norm_tail_bound(
        tail.max_basis_size, tail.tail_cutoff, tail.gaussian_width
    )
    assert 7.0e-13 < bound < 8.0e-13
    assert bound < tail.operator_norm_target


def test_finite_prime_shell_is_below_full_tail_majorant() -> None:
    tail, hermite = programs()
    for left, right in ((0, 0), (2, 3), (5, 5)):
        shell = prime_shell_entry(
            hermite,
            left,
            right,
            tail.tail_cutoff,
            2 * tail.tail_cutoff,
        )
        bound = entry_tail_bound(
            left,
            right,
            tail.tail_cutoff,
            tail.gaussian_width,
        )
        assert abs(shell) <= bound


def test_certificate_receipt_separates_exact_numerical_and_open_layers() -> None:
    tail, hermite = programs()
    receipt = run_prime_tail_certificate(tail, hermite)
    assert receipt["integral_identity_pass"] is True
    assert receipt["all_operator_norm_targets_pass"] is True
    assert receipt["all_shell_checks_pass"] is True
    assert receipt["maps_zeta_zeros"] is False
    assert receipt["claim_boundary"]["proof_of_rh"] is False
    assert "uniform basis-size control" in receipt["claim_boundary"]["open"]
