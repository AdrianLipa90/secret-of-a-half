#!/usr/bin/env python3
"""Run the entire test suite and reject every failure not present on frozen main.

The v0.7 branch adds identity/holonomy functionality on top of a main snapshot
that already contains three reproducible DHSE test debts.  Those debts are not
silently xfailed or rewritten here.  This gate executes the complete suite,
records the result, and passes only when the observed failure set is a subset of
the frozen baseline debt set.  Any new failure is a hard regression.
"""
from __future__ import annotations

import json
from pathlib import Path
import re
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "processed"
OUT.mkdir(parents=True, exist_ok=True)
LOG = OUT / "v0_7_full_regression.log"
RECEIPT = OUT / "v0_7_regression_delta_gate.json"

BASELINE_DEBTS = frozenset({
    "tests/test_dhse_001_stage_b.py::test_persisted_stage_b_receipt_is_reproducible",
    "tests/test_dhse_001_stage_i.py::test_persisted_stage_i_receipt_is_reproducible",
    "tests/test_dhse_001_stage_m.py::test_exact_sweep_distinguishes_symmetry_from_central_maximum",
})

FAIL_RE = re.compile(r"^FAILED\s+(\S+)\s+-", re.MULTILINE)
PASS_RE = re.compile(r"(?P<count>\d+)\s+passed")
FAIL_COUNT_RE = re.compile(r"(?P<count>\d+)\s+failed")
ERROR_RE = re.compile(r"(?P<count>\d+)\s+error(?:s)?")


def _last_count(pattern: re.Pattern[str], text: str) -> int:
    matches = list(pattern.finditer(text))
    return int(matches[-1].group("count")) if matches else 0


def main() -> int:
    started = time.perf_counter()
    proc = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", "--tb=short"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    elapsed = time.perf_counter() - started
    output = proc.stdout
    LOG.write_text(output, encoding="utf-8")

    observed = frozenset(FAIL_RE.findall(output))
    new_failures = observed - BASELINE_DEBTS
    remaining_baseline = observed & BASELINE_DEBTS
    errors = _last_count(ERROR_RE, output)
    passed = _last_count(PASS_RE, output)
    failed = _last_count(FAIL_COUNT_RE, output)

    # pytest exit 0 is clean. Exit 1 means test failures and is acceptable only
    # when every failure belongs to the explicit baseline debt set. Other exit
    # codes indicate collection/infrastructure errors and always fail the gate.
    infrastructure_ok = proc.returncode in {0, 1} and errors == 0
    gate_pass = infrastructure_ok and not new_failures

    receipt = {
        "schema": "SOH_REGRESSION_DELTA_GATE_V1",
        "baseline_debts": sorted(BASELINE_DEBTS),
        "observed_failures": sorted(observed),
        "remaining_baseline_debts": sorted(remaining_baseline),
        "new_failures": sorted(new_failures),
        "passed_count": passed,
        "failed_count": failed,
        "pytest_exit_code": proc.returncode,
        "elapsed_seconds": round(elapsed, 6),
        "infrastructure_ok": infrastructure_ok,
        "gate_status": "PASS_NO_NEW_REGRESSIONS" if gate_pass else "FAIL",
        "scope_note": "DHSE baseline debts are retained unchanged; v0.7 must add no new failures.",
    }
    RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(output, end="")
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0 if gate_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
