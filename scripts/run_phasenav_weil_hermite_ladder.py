#!/usr/bin/env python3
"""Execute the native PhaseNav-Weil Hermite ladder and write a receipt."""

from __future__ import annotations

import json
from pathlib import Path

from secret_of_a_half.phasenav_weil_hermite_ladder import (
    HermiteLadderProgram,
    default_program_path,
    run_ladder_audit,
)


def main() -> int:
    program = HermiteLadderProgram.load(default_program_path())
    receipt = run_ladder_audit(program)
    root = Path(__file__).resolve().parents[1]
    output = root / "data" / "processed" / "phasenav_weil_hermite_ladder_receipt.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    for section in receipt["sections"]:
        print(
            f"N={section['basis_size']}: "
            f"lambda_min={section['lambda_min']:+.12e}, "
            f"cutoff_error={section['cutoff_max_entry_error']:.3e}, "
            f"PSD={'PASS' if section['psd_sample'] else 'FAIL'}"
        )
    print(f"receipt: {output}")
    return 0 if receipt["all_cutoff_stable"] and receipt["all_sampled_sections_psd"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
