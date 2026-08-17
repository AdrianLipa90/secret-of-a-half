#!/usr/bin/env python3
"""Diagnose terminal Hermite-column cancellation in the arithmetic Weil block.

This is a finite-cutoff numerical structural diagnostic.  It tests consecutive
ladder sizes, including odd and even sizes, and records the geometry between
the archimedean and retained-prime terminal-column vectors.  It does not
identify the terminal Hermite column with Suzuki localization and is not a
proof of an infinite-complement estimate.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from secret_of_a_half.phasenav_weil_hermite_core import HermiteLadderProgram, default_program_path
from secret_of_a_half.phasenav_weil_hermite_arithmetic import arithmetic_rectangular_components

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "artifacts" / "receipts" / "SOH_C005_BOUNDARY_COLUMN_STRUCTURE_V0_1.json"


def extended_profile(max_basis_size: int) -> HermiteLadderProgram:
    base = HermiteLadderProgram.load(default_program_path())
    equations = dict(base.equations)
    equations["MAX_BASIS_SIZE"] = str(max_basis_size)
    profile = HermiteLadderProgram(base.path, equations)
    profile.validate()
    return profile


def spectral_norm(a: np.ndarray) -> float:
    return float(np.linalg.norm(a, ord=2))


def vector_norm(a: np.ndarray) -> float:
    return float(np.linalg.norm(a.reshape(-1), ord=2))


def main() -> None:
    windows = tuple(range(5, 15))
    rows = []
    for stop in windows:
        split = stop - 1
        profile = extended_profile(stop)
        comp = arithmetic_rectangular_components(
            profile,
            left_orders=range(split),
            right_orders=range(split, stop),
            prime_cutoff=profile.audit_prime_cutoff,
        )

        arch = comp.archimedean.reshape(-1)
        prime = comp.prime.reshape(-1)
        arch_norm = vector_norm(arch)
        prime_norm = vector_norm(prime)
        inner = np.vdot(arch, prime)
        denom = arch_norm * prime_norm
        cosine_real = float(np.real(inner) / denom) if denom else 0.0
        phase_angle = float(np.angle(inner)) if denom else 0.0

        total_norm = spectral_norm(comp.total)
        arch_prime_norm = vector_norm(arch + prime)
        pole_norm = vector_norm(comp.pole)
        conductor_norm = vector_norm(comp.conductor)
        component_sum = pole_norm + conductor_norm + arch_norm + prime_norm

        row = {
            "M": stop,
            "N": split,
            "parity": "even" if stop % 2 == 0 else "odd",
            "distance_to_boundary": 1,
            "shape": list(comp.total.shape),
            "full_block_norm": total_norm,
            "archimedean_norm": arch_norm,
            "prime_norm": prime_norm,
            "arch_plus_prime_residual_norm": arch_prime_norm,
            "pole_norm": pole_norm,
            "conductor_norm": conductor_norm,
            "arch_prime_inner_real": float(np.real(inner)),
            "arch_prime_inner_imag": float(np.imag(inner)),
            "arch_prime_cosine_real": cosine_real,
            "arch_prime_phase_angle_rad": phase_angle,
            "anti_alignment_defect": 1.0 + cosine_real,
            "norm_mismatch": abs(arch_norm - prime_norm),
            "component_norm_sum": component_sum,
            "cancellation_ratio": total_norm / component_sum if component_sum else 0.0,
            "cancellation_factor": component_sum / total_norm if total_norm else None,
            "triangle_pass": total_norm <= component_sum + 1e-10,
        }
        rows.append(row)

    even = [r for r in rows if r["parity"] == "even"]
    odd = [r for r in rows if r["parity"] == "odd"]
    receipt = {
        "program": "SOH_C005_BOUNDARY_COLUMN_STRUCTURE",
        "version": "0.1.0",
        "status": "NUMERICAL_DIAGNOSTIC_NOT_PROOF",
        "canonical_profile_mutated": False,
        "windows": list(windows),
        "terminal_split_rule": "N=M-1",
        "rows": rows,
        "parity_summary": {
            "even_count": len(even),
            "odd_count": len(odd),
            "even_max_full_block_norm": max(r["full_block_norm"] for r in even),
            "odd_max_full_block_norm": max(r["full_block_norm"] for r in odd),
            "even_max_anti_alignment_defect": max(r["anti_alignment_defect"] for r in even),
            "odd_max_anti_alignment_defect": max(r["anti_alignment_defect"] for r in odd),
        },
        "all_triangle_checks_pass": all(r["triangle_pass"] for r in rows),
        "metric_semantics": {
            "arch_prime_cosine_real": "Re(<arch,prime>)/(||arch|| ||prime||)",
            "anti_alignment_defect": "1 + arch_prime_cosine_real; zero is exact antiparallel alignment in the real inner-product sense",
            "norm_mismatch": "abs(||arch||-||prime||)",
            "arch_plus_prime_residual_norm": "||arch+prime||_2 for the terminal column",
        },
        "claim_boundary": {
            "exact": [
                "all rows use the same pole, conductor, archimedean, and retained-prime formulas",
                "odd and even ladder sizes are both sampled",
                "operator triangle inequality is checked for every terminal-column block",
            ],
            "numerical": [
                "finite prime cutoff and finite Hermite ladders M=5,...,14",
                "terminal-column archimedean/prime anti-alignment diagnostics",
            ],
            "open": [
                "analytic identity or bound explaining terminal-column anti-alignment",
                "uniform cutoff removal",
                "asymptotic M to infinity behavior",
                "relation to Suzuki localization radius a",
                "localized epsilon_Na bound",
                "positive complement lower bound nu_Na",
                "SOH-C005",
                "Riemann Hypothesis",
            ],
            "proof_of_rh": False,
        },
    }
    if not receipt["all_triangle_checks_pass"]:
        raise SystemExit("boundary-column triangle gate failed")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
