from __future__ import annotations

import json
from pathlib import Path

from secret_of_a_half.phasenav_weil_adaptive_cutoff import (
    AdaptiveCutoffProgram,
    default_adaptive_cutoff_program_path,
    run_adaptive_cutoff_audit,
)

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "data/processed/phasenav_weil_adaptive_cutoff_schedule.json"


def main() -> None:
    program = AdaptiveCutoffProgram.load(default_adaptive_cutoff_program_path())
    receipt = run_adaptive_cutoff_audit(program)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "program": receipt["program"],
        "all_target_pass": receipt["all_target_pass"],
        "maximum_certified_bound": receipt["maximum_certified_bound"],
        "maximum_bound_basis_size": receipt["maximum_bound_basis_size"],
        "output": str(OUTPUT),
    }, indent=2))


if __name__ == "__main__":
    main()
