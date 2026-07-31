from __future__ import annotations

import json
from pathlib import Path

from secret_of_a_half.dhse_001_stage_k import run_stage_k


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "data" / "processed" / "dhse_001_stage_k_receipt.json"


def main() -> None:
    receipt = run_stage_k()
    rendered = json.dumps(receipt, sort_keys=True, separators=(",", ":"))
    persisted = OUTPUT.read_text(encoding="utf-8").strip()
    if rendered != persisted:
        raise SystemExit("Stage K receipt mismatch")
    print(json.dumps(receipt["primary_rule"], indent=2, sort_keys=True))
    print(f"technical_status={receipt['technical_status']}")
    print(f"scientific_status={receipt['scientific_status']}")


if __name__ == "__main__":
    main()
