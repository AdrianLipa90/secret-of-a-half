from __future__ import annotations

import json
from pathlib import Path

from secret_of_a_half.c005_infinite_complement import schedule_receipt
from secret_of_a_half.phasenav_weil_prime_tail_program import PrimeTailProgram, default_prime_tail_program_path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports" / "SOH_C005_INFINITE_WINDOW_CUTOFF_SCHEDULE_V0_2.json"


def main() -> None:
    program = PrimeTailProgram.load(default_prime_tail_program_path())
    receipt = schedule_receipt(64, program.gaussian_width)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2, sort_keys=True))
    if receipt["status"] != "PASS_VALIDITY_ONLY":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
