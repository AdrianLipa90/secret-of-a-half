#!/usr/bin/env python3
"""Run the native PhaseNav theta bridge and write an auditable CSV receipt."""

from __future__ import annotations

import csv
from pathlib import Path

from secret_of_a_half.phasenav_theta_bridge import PhaseNavProgram, scan_points

ROOT = Path(__file__).resolve().parents[1]
PROGRAM_PATH = ROOT / "construction" / "phasenav" / "secret_of_half_theta_bridge.pnv"
OUTPUT_PATH = ROOT / "data" / "processed" / "phasenav_theta_bridge_scan.csv"

POINTS = [0.5 + 0.0j, 2.0 + 0.0j, 0.5 + 14.134725141734693j, 0.3 + 10.0j, 0.7 + 10.0j]


def main() -> None:
    program = PhaseNavProgram.load(PROGRAM_PATH)
    rows = scan_points(POINTS, program)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    print(f"program={program.equations['PROGRAM']} version={program.equations['VERSION']}")
    print(f"vector_dim={program.vector_dim} pairs={program.pair_count}")
    print(f"receipt={OUTPUT_PATH}")
    for row in rows:
        print("sigma={sigma:.6f} t={t:.6f} |D|={detector_abs:.6e} closure={closure_defect:.6e} covariance={covariance_residual:.3e}".format(**row))


if __name__ == "__main__":
    main()
