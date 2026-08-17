#!/usr/bin/env python3
"""Emit a cancellation-sensitive prime-sum diagnostic for SOH-C005."""
from __future__ import annotations

import json
from pathlib import Path

from secret_of_a_half.phasenav_weil_hermite_core import HermiteLadderProgram
from secret_of_a_half.phasenav_weil_twisted_prime import (
    cancellation_ratio,
    cumulative_twisted_prime_sum,
)

ROOT = Path(__file__).resolve().parents[1]
PROGRAM = ROOT / "construction" / "phasenav" / "secret_of_half_weil_hermite_ladder.pnv"


def main() -> None:
    profile = HermiteLadderProgram.load(PROGRAM)
    cutoffs = (100, 1000, 10000, 100000)
    rows = []
    for cutoff in cutoffs:
        value = cumulative_twisted_prime_sum(cutoff, profile.target_ordinate)
        rows.append(
            {
                "cutoff": cutoff,
                "cumulative_real": value.real,
                "cumulative_imag": value.imag,
                "cumulative_abs": abs(value),
                "cancellation_ratio": cancellation_ratio(cutoff, profile.target_ordinate),
            }
        )

    payload = {
        "schema": "SOH_C005_TWISTED_PRIME_SUMMATION_V0_1",
        "status": "NUMERICAL_DIAGNOSTIC_NOT_ASYMPTOTIC_THEOREM",
        "target_ordinate": profile.target_ordinate,
        "phase": "n^(-i*t0)",
        "weights": "Lambda(n)*n^(-1/2-i*t0) on prime-power support",
        "rows": rows,
        "exact_identity_tested_elsewhere": "discrete summation by parts",
        "claim_boundary": {
            "exact": [
                "finite cumulative twisted prime sum definition",
                "finite discrete summation-by-parts identity",
            ],
            "numerical": [
                "cancellation ratios at the declared finite cutoffs",
            ],
            "open": [
                "uniform asymptotic twisted-prime bound in the required operator norm",
                "full epsilon_Na bound",
                "complement positivity nu_Na",
                "SOH-C005",
                "RH",
            ],
            "proof_of_rh": False,
        },
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
