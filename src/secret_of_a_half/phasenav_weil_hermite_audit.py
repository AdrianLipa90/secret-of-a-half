"""Spectral validation and receipt layer for the PhaseNav--Weil Hermite ladder."""

from __future__ import annotations

import numpy as np

from .phasenav_weil_hermite_core import (
    HermiteLadderProgram,
    channel_value,
    kernel_fourier_closed,
)
from .phasenav_weil_hermite_arithmetic import REFERENCE_ORDINATES, arithmetic_matrix

def spectral_fixture_matrix(
    program: HermiteLadderProgram,
    *,
    basis_size: int,
    off_axis_delta: float | None = None,
) -> np.ndarray:
    """Build a validation-only spectral fixture matrix.

    The arithmetic computation never calls this function.  With ``off_axis_delta``
    omitted, the fixture contains the first ten on-axis conjugate pairs.  With a
    positive delta, the first pair is replaced by the corresponding symmetric
    off-axis quartet.
    """
    if not 1 <= basis_size <= program.max_basis_size:
        raise ValueError("basis_size is outside the declared ladder")
    r_values: list[complex] = []
    for index, ordinate in enumerate(REFERENCE_ORDINATES):
        if index == 0 and off_axis_delta is not None:
            delta = float(off_axis_delta)
            if delta <= 0.0:
                raise ValueError("off_axis_delta must be positive")
            r_values.extend(
                [
                    ordinate + 1j * delta,
                    ordinate - 1j * delta,
                    -ordinate + 1j * delta,
                    -ordinate - 1j * delta,
                ]
            )
        else:
            r_values.extend([complex(ordinate), complex(-ordinate)])

    matrix = np.zeros((basis_size, basis_size), dtype=complex)
    for r_value in r_values:
        left = np.array(
            [
                np.conjugate(channel_value(order, np.conjugate(r_value), program))
                for order in range(basis_size)
            ],
            dtype=complex,
        )
        right = np.array(
            [channel_value(order, r_value, program) for order in range(basis_size)],
            dtype=complex,
        )
        matrix += np.outer(left, right)
    return 0.5 * (matrix + matrix.conjugate().T)

def max_entry_distance(left: np.ndarray, right: np.ndarray) -> float:
    if left.shape != right.shape:
        raise ValueError("matrix shapes differ")
    return float(np.max(np.abs(left - right)))


def _complex_matrix_json(matrix: np.ndarray) -> list[list[dict[str, float]]]:
    return [
        [
            {"real": float(value.real), "imag": float(value.imag)}
            for value in row
        ]
        for row in matrix
    ]


def run_ladder_audit(program: HermiteLadderProgram) -> dict[str, object]:
    """Run all finite principal sections declared by the native programme."""
    sections: list[dict[str, object]] = []
    all_stable = True
    all_psd = True
    for basis_size in range(1, program.max_basis_size + 1):
        primary, _ = arithmetic_matrix(
            program,
            basis_size=basis_size,
            prime_cutoff=program.prime_cutoff,
        )
        audited, components = arithmetic_matrix(
            program,
            basis_size=basis_size,
            prime_cutoff=program.audit_prime_cutoff,
        )
        stability_error = max_entry_distance(primary, audited)
        eigenvalues = np.linalg.eigvalsh(audited)
        stable = stability_error <= program.stability_tolerance
        psd = float(eigenvalues[0]) >= -program.psd_tolerance
        all_stable &= stable
        all_psd &= psd
        sections.append(
            {
                "basis_size": basis_size,
                "matrix": _complex_matrix_json(audited),
                "lambda_min": float(eigenvalues[0]),
                "lambda_max": float(eigenvalues[-1]),
                "cutoff_max_entry_error": stability_error,
                "cutoff_stable": stable,
                "psd_sample": psd,
                "component_norms": {
                    "pole": float(np.linalg.norm(components.pole, ord=2)),
                    "conductor": float(np.linalg.norm(components.conductor, ord=2)),
                    "archimedean": float(np.linalg.norm(components.archimedean, ord=2)),
                    "prime": float(np.linalg.norm(components.prime, ord=2)),
                },
            }
        )

    orthonormality_error = 0.0
    for left in range(program.max_basis_size):
        for right in range(program.max_basis_size):
            expected = 1.0 if left == right else 0.0
            orthonormality_error = max(
                orthonormality_error,
                abs(kernel_fourier_closed(0.0, left, right, program) - expected),
            )

    on_axis_validation = spectral_fixture_matrix(
        program, basis_size=program.max_basis_size
    )
    off_axis_validation = spectral_fixture_matrix(
        program,
        basis_size=program.max_basis_size,
        off_axis_delta=program.synthetic_off_axis_delta,
    )
    on_axis_eigenvalues = np.linalg.eigvalsh(on_axis_validation)
    off_axis_eigenvalues = np.linalg.eigvalsh(off_axis_validation)

    return {
        "program": program.equations["PROGRAM"],
        "version": program.equations["VERSION"],
        "base_head": program.equations["BASE_HEAD"],
        "status": program.equations["STATUS"],
        "arithmetic_sum_uses_zero_list": False,
        "dense_family": "translated_scaled_hermite_schwartz_core",
        "max_basis_size": program.max_basis_size,
        "prime_cutoff": program.prime_cutoff,
        "audit_prime_cutoff": program.audit_prime_cutoff,
        "orthonormality_error": float(orthonormality_error),
        "all_cutoff_stable": all_stable,
        "all_sampled_sections_psd": all_psd,
        "sections": sections,
        "spectral_falsification_validation": {
            "role": "validation_only_not_arithmetic_input",
            "on_axis_lambda_min": float(on_axis_eigenvalues[0]),
            "synthetic_off_axis_delta": program.synthetic_off_axis_delta,
            "synthetic_off_axis_lambda_min": float(off_axis_eigenvalues[0]),
            "negative_witness_pass": float(off_axis_eigenvalues[0])
            < program.synthetic_negativity_threshold,
        },
        "claim_boundary": {
            "exact": [
                "Hermite product linearization",
                "closed Fourier transform",
                "Schwartz dense-core reduction",
            ],
            "numerical": "finite principal ladder at finite cutoffs",
            "open": [
                "uniform positivity for every basis size",
                "controlled cutoff removal",
                "null-structure implication to native closure",
            ],
            "proof_of_rh": False,
        },
    }
