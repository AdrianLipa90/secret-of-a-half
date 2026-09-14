#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

from secret_of_a_half.half_kernel_wronskian_completion import build_receipt

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports" / "SOH_HALF_KERNEL_WRONSKIAN_COMPLETION_V0_3.json"


def main() -> int:
    receipt = build_receipt()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0 if receipt["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
