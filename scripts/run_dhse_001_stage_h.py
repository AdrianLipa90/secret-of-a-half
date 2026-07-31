from __future__ import annotations

import json
from pathlib import Path

from secret_of_a_half.dhse_001_stage_h import run_stage_h


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "data" / "processed" / "dhse_001_stage_h_receipt.json"


def main() -> None:
    receipt = run_stage_h()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps(receipt, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"technical_status={receipt['technical_status']}")
    print(f"scientific_status={receipt['scientific_status']}")
    print(f"target_counts={receipt['secondary']['target_count_sequence']}")
    print(f"receipt={OUTPUT}")


if __name__ == "__main__":
    main()
