#!/usr/bin/env python3
"""Regenerate the DHSE-001 Stage M exact continuous certificate."""
from __future__ import annotations

import json
from pathlib import Path

from secret_of_a_half.dhse_001_stage_m import run_stage_m

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "data" / "processed" / "dhse_001_stage_m_receipt.json"


def main() -> None:
    receipt = run_stage_m()
    rendered = json.dumps(receipt, indent=2, ensure_ascii=False) + "\n"
    persisted = OUTPUT.read_text(encoding="utf-8")
    if persisted != rendered:
        raise SystemExit("Stage M receipt mismatch; regenerate and review the diff")
    print(rendered, end="")


if __name__ == "__main__":
    main()
