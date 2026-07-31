from __future__ import annotations

import argparse
import json
from pathlib import Path

from secret_of_a_half.dhse_001 import run_experiment


def main() -> None:
    parser = argparse.ArgumentParser(description="Run DHSE-001 deterministic seed dynamics")
    parser.add_argument("--seed", default="secret-of-a-half:DHSE-001")
    parser.add_argument("--steps", type=int, default=256)
    parser.add_argument("--output", type=Path, default=Path("data/processed/dhse_001_receipt.json"))
    args = parser.parse_args()

    receipt = run_experiment(seed=args.seed, steps=args.steps)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(receipt["results"], indent=2))
    print(f"technical_status={receipt['technical_status']}")
    print(f"scientific_status={receipt['scientific_status']}")


if __name__ == "__main__":
    main()
