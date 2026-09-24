#!/usr/bin/env python3
"""Fail closed when The Zero Axis v1.1 Proof Edition publication omits current theorem state."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "monograph"
MAIN = MONO / "main.tex"
CHAPTERS = MONO / "chapters"
CANON_LEDGER = ROOT / "claims" / "claim_ledger.json"
G024_LEDGER = ROOT / "claims" / "SOH_G024_BRANCH_CLAIM_LEDGER_V1.json"
G024_T = ROOT / "claims" / "SOH_G024_T_COMPLETE_MONOTONICITY_ROUTE_NOGO_V0_1.json"


def fail(message: str) -> None:
    raise SystemExit(f"MONOGRAPH_INTEGRATION_FAIL: {message}")


def main() -> None:
    main_text = MAIN.read_text(encoding="utf-8")
    includes = re.findall(r"\\include\{chapters/([^}]+)\}", main_text)
    chapter_files = sorted(p.stem for p in CHAPTERS.glob("*.tex"))

    if len(includes) != len(set(includes)):
        fail("duplicate chapter include in main.tex")
    missing = sorted(set(chapter_files) - set(includes))
    extra = sorted(set(includes) - set(chapter_files))
    if missing or extra:
        fail(f"chapter completeness mismatch missing={missing} extra={extra}")

    expected = [f"{i:02d}" for i in range(1, len(includes) + 1)]
    prefixes = [name.split("_", 1)[0] for name in includes]
    if prefixes != expected:
        fail(f"chapter numbering is not contiguous: {prefixes}")
    if len(includes) != 59:
        fail(f"The Zero Axis v1.0 requires exactly 59 numbered chapters, found {len(includes)}")
    if includes[-4:] != [
        "56_g024_complete_monotonicity_route_no_go",
        "57_reciprocal_conjugation_orbit_collapse",
        "58_occam_relational_zero_triad",
        "59_zero_critical_relational_axis",
    ]:
        fail(f"unexpected terminal chapters: {includes[-4:]}")

    for token in [
        r"\textbf{The Zero Axis}",
        "Version 1.1 -- Proof Edition",
        r"\include{chapters/58_occam_relational_zero_triad}",
        r"\include{chapters/59_zero_critical_relational_axis}",
        r"\input{frontmatter/roadmap}",
        r"\input{backmatter/final_synthesis}",
    ]:
        if token not in main_text:
            fail(f"main.tex missing v1.0 token {token!r}")

    title_count = sum(
        p.read_text(encoding="utf-8").count(r"\begin{titlepage}")
        for p in MONO.rglob("*.tex")
    )
    if title_count != 1:
        fail(f"expected exactly one titlepage, found {title_count}")

    ledger = json.loads(CANON_LEDGER.read_text(encoding="utf-8"))
    ids = [item["id"] for item in ledger["claims"]]
    if len(ids) != len(set(ids)):
        fail("duplicate canonical claim IDs")
    if ledger.get("canonical_through") != "SOH-G023":
        fail("canonical_through must remain SOH-G023")
    if "SOH-G024" in ids:
        fail("SOH-G024 must not be silently inserted into canonical numbered ledger")

    g024 = json.loads(G024_LEDGER.read_text(encoding="utf-8"))
    if g024.get("promotion_status") != "INTEGRATED_MAINLINE_NOT_CANONICAL":
        fail("G024 integration/canon firewall changed")
    t = json.loads(G024_T.read_text(encoding="utf-8"))
    if t.get("claim_id") != "SOH-G024-T":
        fail("missing reviewed G024-T claim")
    if t.get("route_effect", {}).get("closed_route") != "FULL_COMPLETE_MONOTONICITY_TO_GAUSSIAN_MIXTURE":
        fail("G024-T closed-route identity changed")

    current_files = [
        MONO / "frontmatter" / "title.tex",
        MONO / "frontmatter" / "abstract.tex",
        MONO / "frontmatter" / "preface.tex",
        MONO / "frontmatter" / "roadmap.tex",
        MONO / "chapters" / "58_occam_relational_zero_triad.tex",
        MONO / "chapters" / "59_zero_critical_relational_axis.tex",
        MONO / "appendices" / "D_claim_ledger.tex",
        MONO / "backmatter" / "final_synthesis.tex",
    ]
    required_text = "\n".join(p.read_text(encoding="utf-8") for p in current_files)

    for token in [
        "The Zero Axis",
        "A0",
        "zero has no independent realization",
        "SOH-RZ001",
        "SOH-RZ002",
        "SOH-RZ003",
        "SOH-RZ006",
        "Relational Lagrange--Zero Theorem",
        "Delta_{\\rm RC}",
        "GREMLIN",
        "A0}\\Longrightarrow\\mathrm{RH}",
        "presents and claims",
        "Q.E.D.",
    ]:
        if token not in required_text:
            fail(f"v1.0 publication synthesis missing token {token!r}")

    print("MONOGRAPH_INTEGRATION_PASS")
    print(
        f"version=the-zero-axis-v1.1-proof-edition chapters={len(includes)} "
        "axioms=1 terminal_theorem=A0=>RH canonical_through=SOH-G023"
    )


if __name__ == "__main__":
    main()
