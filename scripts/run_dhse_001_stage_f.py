from __future__ import annotations

import json
from pathlib import Path

from secret_of_a_half.dhse_001_stage_f import run_stage_f


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "data" / "processed" / "dhse_001_stage_f_receipt.json"


def main() -> None:
    receipt = run_stage_f()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps(receipt, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    primary = receipt["primary_statistic"]
    print(f"technical_status={receipt['technical_status']}")
    print(f"scientific_status={receipt['scientific_status']}")
    print(f"target_forcing_count={primary['target_forcing_count']}")
    print(f"median_control_count={primary['median_control_count']}")
    print(f"receipt={OUTPUT}")


if __name__ == "__main__":
    main()
