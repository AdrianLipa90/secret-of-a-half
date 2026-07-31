from __future__ import annotations

import json
from pathlib import Path

from secret_of_a_half.dhse_001_stage_g import run_stage_g


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "data" / "processed" / "dhse_001_stage_g_receipt.json"


def main() -> None:
    receipt = run_stage_g()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps(receipt, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    primary = receipt["primary_rule"]
    print(f"technical_status={receipt['technical_status']}")
    print(f"scientific_status={receipt['scientific_status']}")
    print(f"rate_K4={primary['rate_K4']}")
    print(f"rate_K6={primary['rate_K6']}")
    print(f"receipt={OUTPUT}")


if __name__ == "__main__":
    main()
