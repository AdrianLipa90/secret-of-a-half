"""Finite shell regression and deterministic receipt for the prime-tail certificate."""
from __future__ import annotations
import math
import mpmath as mp
import numpy as np
from .phasenav_weil_hermite_core import HermiteLadderProgram, kernel_fourier_closed
from .phasenav_weil_hermite_arithmetic import prime_power_terms
from .phasenav_weil_prime_tail_program import PrimeTailProgram, monotonicity_margin
from .phasenav_weil_prime_tail_integrals import (
    entry_bound_matrix, entry_tail_bound, tail_term_integral_gamma,
    tail_term_integral_log, tail_term_integral_reciprocal,
)

def prime_shell_entry(
    hermite_program: HermiteLadderProgram,
    left_order: int,
    right_order: int,
    lower_cutoff: int,
    upper_cutoff: int,
) -> complex:
    """Evaluate a finite prime-power shell for regression only."""
    if upper_cutoff <= lower_cutoff:
        raise ValueError("upper_cutoff must exceed lower_cutoff")
    terms = [item for item in prime_power_terms(upper_cutoff) if item[0] > lower_cutoff]
    if not terms:
        return 0.0 + 0.0j
    n_values = np.array([item[0] for item in terms], dtype=float)
    mangoldt = np.array([item[1] for item in terms], dtype=float)
    x_values = np.log(n_values) / (2.0 * math.pi)
    transforms = kernel_fourier_closed(
        x_values, left_order, right_order, hermite_program
    )
    transforms += kernel_fourier_closed(
        -x_values, left_order, right_order, hermite_program
    )
    return complex(-np.sum(mangoldt / np.sqrt(n_values) * transforms) / (2 * math.pi))


def _relative_error(left: mp.mpf, right: mp.mpf) -> mp.mpf:
    scale = max(abs(left), abs(right), mp.mpf("1e-100"))
    return abs(left - right) / scale


def run_prime_tail_certificate(
    tail_program: PrimeTailProgram,
    hermite_program: HermiteLadderProgram,
) -> dict[str, object]:
    """Evaluate analytic identities and the declared finite-section envelope."""
    mp.mp.dps = tail_program.mp_dps
    width = tail_program.gaussian_width
    cutoff = tail_program.tail_cutoff
    max_degree = 2 * (tail_program.max_basis_size - 1)

    integral_checks: list[dict[str, object]] = []
    max_log_error = mp.mpf("0")
    max_reciprocal_error = mp.mpf("0")
    for degree in range(max_degree + 1):
        gamma_value = tail_term_integral_gamma(degree, cutoff, width)
        log_value = tail_term_integral_log(degree, cutoff, width)
        reciprocal_value = tail_term_integral_reciprocal(degree, cutoff, width)
        log_error = _relative_error(gamma_value, log_value)
        reciprocal_error = _relative_error(gamma_value, reciprocal_value)
        max_log_error = max(max_log_error, log_error)
        max_reciprocal_error = max(max_reciprocal_error, reciprocal_error)
        integral_checks.append(
            {
                "degree": degree,
                "monotonicity_margin": monotonicity_margin(degree, cutoff, width),
                "gamma_value": mp.nstr(gamma_value, 25),
                "log_relative_error": float(log_error),
                "reciprocal_relative_error": float(reciprocal_error),
            }
        )

    sections: list[dict[str, object]] = []
    all_targets_pass = True
    for basis_size in range(1, tail_program.max_basis_size + 1):
        matrix = entry_bound_matrix(basis_size, cutoff, width)
        row_sums = np.sum(matrix, axis=1)
        norm_bound = float(np.max(row_sums))
        target_pass = norm_bound <= tail_program.operator_norm_target
        all_targets_pass &= target_pass
        sections.append(
            {
                "basis_size": basis_size,
                "max_entry_bound": float(np.max(matrix)),
                "operator_norm_bound": norm_bound,
                "target_pass": target_pass,
            }
        )

    shell_checks: list[dict[str, object]] = []
    upper_cutoff = 2 * cutoff
    for left, right in ((0, 0), (2, 3), (5, 5)):
        if max(left, right) >= tail_program.max_basis_size:
            continue
        shell = prime_shell_entry(
            hermite_program,
            left,
            right,
            cutoff,
            upper_cutoff,
        )
        bound = float(entry_tail_bound(left, right, cutoff, width))
        shell_checks.append(
            {
                "left_order": left,
                "right_order": right,
                "upper_cutoff": upper_cutoff,
                "shell_abs": abs(shell),
                "full_tail_bound": bound,
                "pass": abs(shell) <= bound,
            }
        )

    tolerance = mp.mpf(str(tail_program.integral_match_tolerance))
    return {
        "program": tail_program.equations["PROGRAM"],
        "version": tail_program.equations["VERSION"],
        "base_head": tail_program.equations["BASE_HEAD"],
        "status": tail_program.equations["STATUS"],
        "map_role": "reciprocal_compactification_of_logarithmic_prime_tail",
        "maps_zeta_zeros": False,
        "spectral_zero_input": False,
        "tail_cutoff": cutoff,
        "gaussian_width": width,
        "max_basis_size": tail_program.max_basis_size,
        "max_degree": max_degree,
        "integral_checks": integral_checks,
        "max_log_relative_error": float(max_log_error),
        "max_reciprocal_relative_error": float(max_reciprocal_error),
        "integral_identity_pass": max(max_log_error, max_reciprocal_error) <= tolerance,
        "sections": sections,
        "all_operator_norm_targets_pass": all_targets_pass,
        "prime_shell_regression": shell_checks,
        "all_shell_checks_pass": all(item["pass"] for item in shell_checks),
        "claim_boundary": {
            "exact": [
                "reciprocal compactification identity",
                "flat endpoint extension",
                "incomplete-gamma tail formula",
                "entrywise von-Mangoldt majorant",
                "finite-section max-row-sum norm envelope",
            ],
            "numerical": "high-precision evaluation for N<=6 at Q=100000",
            "open": [
                "uniform basis-size control",
                "global arithmetic positivity",
                "null-structure implication to native closure",
            ],
            "proof_of_rh": False,
        },
    }
