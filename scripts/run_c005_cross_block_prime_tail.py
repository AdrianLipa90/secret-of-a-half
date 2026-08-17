#!/usr/bin/env python3
"""Emit the first SOH-C005 cross-block prime-tail receipt.

This receipt certifies only the omitted prime-power tail in finite Hermite
windows. It is not a certificate for the full localized Weil operator A_a.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from secret_of_a_half.phasenav_weil_prime_tail import (
    PrimeTailProgram,
    high_index_block_tail_bound,
    rectangular_operator_norm_tail_bound,
)

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--program",
        type=Path,
        default=ROOT / "construction/phasenav/secret_of_half_weil_prime_tail_certificate.pnv",
    )
    parser.add_argument("--split", type=int, default=3)
    parser.add_argument("--stop", type=int, default=6)
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "data/processed/c005_cross_block_prime_tail_receipt.json",
    )
    args = parser.parse_args()

    program = PrimeTailProgram.load(args.program)
    if not (0 < args.split < args.stop <= program.max_basis_size):
        raise ValueError("require 0 < split < stop <= declared max basis size")

    coupling = rectangular_operator_norm_tail_bound(
        0,
        args.split,
        args.split,
        args.stop,
        program.tail_cutoff,
        program.gaussian_width,
    )
    high_block = high_index_block_tail_bound(
        args.split,
        args.stop,
        program.tail_cutoff,
        program.gaussian_width,
    )

    receipt = {
        "program": "SOH_C005_CROSS_BLOCK_PRIME_TAIL",
        "version": "0.1.0",
        "split": args.split,
        "stop": args.stop,
        "prime_cutoff": program.tail_cutoff,
        "gaussian_width": program.gaussian_width,
        "spectral_zero_input": False,
        "epsilon_prime_tail_window_bound": coupling,
        "high_index_prime_tail_window_bound": high_block,
        "claim_boundary": {
            "exact": [
                "entrywise omitted-prime-power tail majorants",
                "finite rectangular spectral-norm envelope via sqrt(||A||_1 ||A||_inf)",
                "finite high-index square-block row-sum norm envelope",
            ],
            "open": [
                "retained-prime cross-block coupling",
                "archimedean cross-block coupling",
                "boundary and regularization coupling",
                "tail beyond the finite stop index",
                "full epsilon_N,a bound",
                "non-negative complement lower bound nu_N,a",
                "localization normalization to Q_W^a",
                "SOH-C005",
                "Riemann Hypothesis",
            ],
            "proof_of_rh": False,
        },
        "status": "PRIME_TAIL_CROSS_BLOCK_COMPONENT_ONLY_NOT_GLOBAL_POSITIVITY",
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
