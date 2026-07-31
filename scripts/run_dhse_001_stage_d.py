from __future__ import annotations

import json
from pathlib import Path

from secret_of_a_half.dhse_001_stage_d import run_stage_d


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "data" / "processed" / "dhse_001_stage_d_receipt.json"


def main() -> None:
    receipt = run_stage_d()
    rendered = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
