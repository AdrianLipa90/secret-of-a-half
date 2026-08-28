#!/usr/bin/env python3
"""Fail-loud policy audit for retained GitHub Actions artifacts."""

from __future__ import annotations

import re
import sys
from pathlib import Path

MAX_RETENTION_DAYS = 7
HEAVY_MARKERS = ("monograph", "main.pdf", "current-main-repair-pdf")
WORKFLOW_GLOBS = ("*.yml", "*.yaml")


def _indent(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def _step_block(lines: list[str], uses_index: int) -> list[str]:
    uses_indent = _indent(lines[uses_index])
    start = uses_index

    for idx in range(uses_index, -1, -1):
        stripped = lines[idx].lstrip()
        if stripped.startswith("- ") and _indent(lines[idx]) <= uses_indent:
            start = idx
            break

    step_indent = _indent(lines[start])
    end = len(lines)
    for idx in range(start + 1, len(lines)):
        stripped = lines[idx].lstrip()
        indent = _indent(lines[idx])
        if stripped.startswith("- ") and indent == step_indent:
            end = idx
            break
        if stripped and indent < step_indent:
            end = idx
            break
    return lines[start:end]


def audit_workflow(path: Path) -> list[str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    violations: list[str] = []

    for index, line in enumerate(lines):
        if "uses: actions/upload-artifact@" not in line:
            continue

        block_lines = _step_block(lines, index)
        block = "\n".join(block_lines)
        lowered = block.lower()

        retention = re.search(r"(?m)^\s*retention-days:\s*(\d+)\s*$", block)
        if retention is None:
            violations.append(f"{path}:{index + 1}: upload-artifact missing explicit retention-days")
        else:
            days = int(retention.group(1))
            if days < 1 or days > MAX_RETENTION_DAYS:
                violations.append(
                    f"{path}:{index + 1}: retention-days={days} outside 1..{MAX_RETENTION_DAYS}"
                )

        if any(marker in lowered for marker in HEAVY_MARKERS):
            condition = next(
                (entry.strip() for entry in block_lines if entry.strip().startswith("if:")),
                "",
            )
            manual_gate = "github.event_name == 'workflow_dispatch'" in condition
            main_push_gate = (
                "github.event_name == 'push'" in condition
                and "refs/heads/main" in condition
            )
            if not (manual_gate or main_push_gate):
                violations.append(
                    f"{path}:{index + 1}: heavy artifact upload is not gated to manual dispatch or main push"
                )

    return violations


def main() -> int:
    workflow_dir = Path(".github/workflows")
    if not workflow_dir.is_dir():
        print("ARTIFACT_POLICY_FAIL missing .github/workflows", file=sys.stderr)
        return 2

    workflows = sorted(
        {path for pattern in WORKFLOW_GLOBS for path in workflow_dir.glob(pattern)}
    )
    if not workflows:
        print("ARTIFACT_POLICY_FAIL no workflow files found", file=sys.stderr)
        return 2

    violations: list[str] = []
    upload_steps = 0
    for path in workflows:
        text = path.read_text(encoding="utf-8")
        upload_steps += text.count("uses: actions/upload-artifact@")
        violations.extend(audit_workflow(path))

    if violations:
        print("ARTIFACT_POLICY_FAIL", file=sys.stderr)
        for violation in violations:
            print(f"- {violation}", file=sys.stderr)
        return 1

    print(
        f"ARTIFACT_POLICY_PASS workflows={len(workflows)} upload_steps={upload_steps} "
        f"max_retention_days={MAX_RETENTION_DAYS}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
