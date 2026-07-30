from __future__ import annotations

import math
from pathlib import Path

from secret_of_a_half.phasenav_weil_adaptive_cutoff import (
    AdaptiveCutoffProgram,
    adaptive_cutoff,
    adaptive_log_cutoff,
    crude_log_operator_envelope,
    default_adaptive_cutoff_program_path,
    elementary_tail_integral_envelope,
    logarithmic_decay_rate,
    run_adaptive_cutoff_audit,
)
from secret_of_a_half.phasenav_weil_prime_tail_integrals import tail_term_integral_gamma

ROOT = Path(__file__).resolve().parents[1]


def program() -> AdaptiveCutoffProgram:
    return AdaptiveCutoffProgram.load(
        ROOT / "construction/phasenav/secret_of_half_weil_adaptive_cutoff_schedule.pnv"
    )


def test_native_profile_parses_and_declares_no_zero_input() -> None:
    item = program()
    assert item.max_basis_size == 20
    assert item.base_cutoff == 100_000
    assert item.log_cutoff_slope == 2.0
    assert item.equations["SPECTRAL_ZERO_INPUT"] == "NONE"


def test_default_path_matches_declared_native_source() -> None:
    assert default_adaptive_cutoff_program_path().name == "secret_of_half_weil_adaptive_cutoff_schedule.pnv"


def test_schedule_uses_base_cutoff_then_exponential_growth() -> None:
    item = program()
    assert adaptive_cutoff(1, base_cutoff=item.base_cutoff, slope=item.log_cutoff_slope) == item.base_cutoff
    assert adaptive_log_cutoff(20, base_cutoff=item.base_cutoff, slope=item.log_cutoff_slope) == 40.0
    assert adaptive_cutoff(20, base_cutoff=item.base_cutoff, slope=item.log_cutoff_slope) > 10**17


def test_decay_rate_is_positive_for_every_declared_section() -> None:
    item = program()
    for basis_size in range(1, item.max_basis_size + 1):
        degree = 2 * basis_size - 2
        log_cutoff = adaptive_log_cutoff(
            basis_size, base_cutoff=item.base_cutoff, slope=item.log_cutoff_slope
        )
        assert logarithmic_decay_rate(degree, log_cutoff, item.gaussian_width) > 0.0


def test_elementary_envelope_dominates_exact_gamma_integral() -> None:
    item = program()
    degree = 10
    log_cutoff = adaptive_log_cutoff(6, base_cutoff=item.base_cutoff, slope=item.log_cutoff_slope)
    cutoff = adaptive_cutoff(6, base_cutoff=item.base_cutoff, slope=item.log_cutoff_slope)
    exact = tail_term_integral_gamma(degree, cutoff, item.gaussian_width)
    envelope = elementary_tail_integral_envelope(degree, log_cutoff, item.gaussian_width)
    assert exact <= envelope


def test_declared_schedule_passes_through_basis_twenty() -> None:
    receipt = run_adaptive_cutoff_audit(program())
    assert receipt["all_target_pass"] is True
    assert receipt["maximum_bound_basis_size"] == 5
    assert math.isclose(
        receipt["maximum_certified_bound"],
        3.280365246530553e-14,
        rel_tol=2e-12,
        abs_tol=0.0,
    )


def test_coarse_asymptotic_envelope_decreases_on_final_window() -> None:
    item = program()
    values = []
    for basis_size in range(13, 21):
        log_cutoff = adaptive_log_cutoff(
            basis_size, base_cutoff=item.base_cutoff, slope=item.log_cutoff_slope
        )
        values.append(crude_log_operator_envelope(basis_size, log_cutoff, item.gaussian_width))
    assert all(right < left for left, right in zip(values, values[1:]))


def test_claim_boundary_keeps_global_positivity_open() -> None:
    receipt = run_adaptive_cutoff_audit(program())
    assert receipt["spectral_zero_input"] is False
    assert receipt["claim_boundary"]["proof_of_rh"] is False
    assert "fixed-cutoff uniformity in basis size" in receipt["claim_boundary"]["open"]
    assert "global arithmetic positivity" in receipt["claim_boundary"]["open"]
