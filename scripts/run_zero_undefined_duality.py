#!/usr/bin/env python3
"""Execute the native Zero--Undefined Reciprocal Duality audit."""

from __future__ import annotations

import json
from pathlib import Path

from secret_of_a_half.zero_undefined_duality import (
    ZeroUndefinedProgram,
    default_program_path,
    run_duality_audit,
)


def main() -> None:
    program = ZeroUndefinedProgram.load(default_program_path())
    receipt = run_duality_audit(program)
    root = Path(__file__).resolve().parents[1]
    output = root / "data" / "processed" / "zero_undefined_duality_receipt.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
