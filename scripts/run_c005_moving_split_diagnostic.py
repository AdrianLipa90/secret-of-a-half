#!/usr/bin/env python3
"""Moving-split diagnostic for full arithmetic Weil Hermite coupling.

This script keeps the canonical Hermite profile immutable and extends only the
finite diagnostic basis size.  For each finite window M it compares several
splits N(M), including the fixed-low-block baseline and boundary-adjacent
splits.  It is a numerical structural diagnostic, not an asymptotic theorem,
not Suzuki localization, and not a proof of SOH-C005 or RH.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from secret_of_a_half.phasenav_weil_hermite_core import HermiteLadderProgram, default_program_path
from secret_of_a_half.phasenav_weil_hermite_arithmetic import arithmetic_rectangular_components

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "artifacts" / "receipts" / "SOH_C005_MOVING_SPLIT_DIAGNOSTIC_V0_1.json"


def extended_profile(max_basis_size: int) -> HermiteLadderProgram:
    base = HermiteLadderProgram.load(default_program_path())
    equations = dict(base.equations)
    equations["MAX_BASIS_SIZE"] = str(max_basis_size)
    profile = HermiteLadderProgram(base.path, equations)
    profile.validate()
    return profile


def spectral_norm(a: np.ndarray) -> float:
    return float(np.linalg.norm(a, ord=2))


def split_set(M: int) -> tuple[int, ...]:
    candidates = {2, M // 2, M - 2, M - 1}
    return tuple(sorted(n for n in candidates if 1 <= n < M))


def main() -> None:
    windows = (6, 8, 10, 12)
    rows: list[dict[str, object]] = []
    for M in windows:
        profile = extended_profile(M)
        for N in split_set(M):
            comp = arithmetic_rectangular_components(
                profile,
                left_orders=range(N),
                right_orders=range(N, M),
                prime_cutoff=profile.audit_prime_cutoff,
            )
            component_norms = {
                "pole": spectral_norm(comp.pole),
                "conductor": spectral_norm(comp.conductor),
                "archimedean": spectral_norm(comp.archimedean),
                "prime": spectral_norm(comp.prime),
            }
            full = spectral_norm(comp.total)
            envelope = sum(component_norms.values())
            ratio = full / envelope if envelope else 0.0
            difference = envelope - full
            factor = envelope / full if full > 0.0 else float("inf")
            rows.append(
                {
                    "M": M,
                    "N": N,
                    "distance_to_boundary": M - N,
                    "split_fraction": N / M,
                    "shape": [N, M - N],
                    "full_block_norm": full,
                    "component_norms": component_norms,
                    "component_norm_sum": envelope,
                    "cancellation_ratio": ratio,
                    "cancellation_difference": difference,
                    "cancellation_factor": factor,
                    "triangle_pass": full <= envelope + 1e-10,
                }
            )

    boundary_rows = [row for row in rows if row["distance_to_boundary"] == 1]
    receipt = {
        "program": "SOH_C005_MOVING_SPLIT_DIAGNOSTIC",
        "version": "0.1.0",
        "status": "NUMERICAL_DIAGNOSTIC_NOT_PROOF",
        "canonical_profile_mutated": False,
        "windows": list(windows),
        "split_rule_candidates": ["N=2", "N=floor(M/2)", "N=M-2", "N=M-1"],
        "rows": rows,
        "boundary_adjacent_rows": boundary_rows,
        "all_triangle_checks_pass": all(bool(row["triangle_pass"]) for row in rows),
        "metric_semantics": {
            "cancellation_ratio": "full_block_norm / component_norm_sum",
            "cancellation_difference": "component_norm_sum - full_block_norm",
            "cancellation_factor": "component_norm_sum / full_block_norm",
        },
        "claim_boundary": {
            "exact": [
                "all finite blocks use the same pole, conductor, archimedean, and retained-prime formulas",
                "the canonical Hermite execution profile is not mutated",
                "operator triangle inequality is checked for every finite block",
            ],
            "numerical": [
                "split-dependent full-block norms and cancellation metrics for M in {6,8,10,12}",
                "comparison of fixed, bulk, and boundary-adjacent splits at finite prime cutoff",
            ],
            "open": [
                "asymptotic moving-split law",
                "mathematical relation between moving Hermite boundary and Suzuki localization radius a",
                "uniform cutoff removal",
                "localized off-diagonal epsilon_Na bound",
                "positive complement lower bound nu_Na",
                "SOH-C005",
                "Riemann Hypothesis",
            ],
            "proof_of_rh": False,
        },
    }
    if not receipt["all_triangle_checks_pass"]:
        raise SystemExit("moving-split triangle gate failed")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
