#!/usr/bin/env python3
"""Run the prime-side PhaseNav--Weil arithmetic audit and write a JSON receipt."""

from __future__ import annotations

import json
from pathlib import Path

from secret_of_a_half.phasenav_weil_arithmetic import (
    ArithmeticWeilProgram,
    default_arithmetic_program_path,
    run_arithmetic_audit,
)
from secret_of_a_half.phasenav_weil_probe import (
    WeilProbeProgram,
    default_program_path,
    finite_weil_matrix,
    on_axis_fixture,
)

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = ROOT / "data" / "processed" / "phasenav_weil_arithmetic_receipt.json"


def main() -> int:
    arithmetic_program = ArithmeticWeilProgram.load(default_arithmetic_program_path())

    # The finite zero fixture is used only to validate normalization.  It is not
    # passed to the arithmetic explicit-formula calculation.
    witness_program = WeilProbeProgram.load(default_program_path())
    spectral_reference = finite_weil_matrix(on_axis_fixture(witness_program), witness_program)

    receipt = run_arithmetic_audit(
        arithmetic_program,
        spectral_reference=spectral_reference,
    )
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(
        json.dumps(receipt, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    print(f"program={receipt['program']} version={receipt['version']}")
    print(f"status={receipt['status']}")
    print(f"arithmetic_sum_uses_zero_list={receipt['arithmetic_sum_uses_zero_list']}")
    print(f"receipt={OUTPUT_PATH}")
    print(
        "matrix: "
        f"a={receipt['matrix']['a']:.15e} "
        f"b=({receipt['matrix']['b']['real']:.15e},"
        f"{receipt['matrix']['b']['imag']:.15e}) "
        f"d={receipt['matrix']['d']:.15e}"
    )
    print(
        "eigenvalues: "
        f"lambda_min={receipt['eigenvalues']['lambda_min']:.15e} "
        f"lambda_max={receipt['eigenvalues']['lambda_max']:.15e}"
    )
    print(
        "cutoff_stability: "
        f"error={receipt['cutoff_stability']['max_entry_error']:.3e} "
        f"pass={receipt['cutoff_stability']['pass']}"
    )
    cross = receipt["spectral_cross_check"]
    print(
        "spectral_cross_check: "
        f"error={cross['max_entry_error']:.3e} pass={cross['pass']}"
    )

    passed = (
        receipt["cutoff_stability"]["pass"]
        and receipt["psd_sample"]["pass"]
        and cross["pass"]
    )
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
