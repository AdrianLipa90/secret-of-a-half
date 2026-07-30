#!/usr/bin/env python3
"""Run the native PhaseNav-Weil finite witness and write a JSON receipt."""

from __future__ import annotations

import json
from pathlib import Path

from secret_of_a_half.phasenav_weil_probe import (
    WeilProbeProgram,
    default_program_path,
    run_probe,
)

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = ROOT / "data" / "processed" / "phasenav_weil_probe_receipt.json"


def main() -> int:
    program = WeilProbeProgram.load(default_program_path())
    receipt = run_probe(program)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(
        json.dumps(receipt, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    print(f"program={receipt['program']} version={receipt['version']}")
    print(f"status={receipt['status']}")
    print(f"receipt={OUTPUT_PATH}")

    for fixture in ("on_axis_control", "synthetic_off_axis"):
        row = receipt[fixture]
        print(
            f"{fixture}: lambda_min={row['lambda_min']:.12e} "
            f"lambda_max={row['lambda_max']:.12e} "
            f"pass={row['pass']}"
        )

    return 0 if (
        receipt["on_axis_control"]["pass"]
        and receipt["synthetic_off_axis"]["pass"]
    ) else 1


if __name__ == "__main__":
    raise SystemExit(main())
