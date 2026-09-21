#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

from secret_of_a_half.c005_suzuki_localization import localization_crosswalk_receipt

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "artifacts" / "receipts" / "SOH_SUZUKI_LOCALIZATION_UNITARY_CROSSWALK_V0_1.json"


def main() -> int:
    receipt = localization_crosswalk_receipt()
    receipt["status"] = "PASS_COORDINATE_DOMAIN_CROSSWALK_ONLY"
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
