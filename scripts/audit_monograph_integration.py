#!/usr/bin/env python3
"""Fail closed when the publication monograph omits current theorem state."""
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
    if len(includes) != 57:
        fail(f"v0.11 requires exactly 57 numbered chapters, found {len(includes)}")
    if includes[-2:] != [
        "56_g024_complete_monotonicity_route_no_go",
        "57_reciprocal_conjugation_orbit_collapse",
    ]:
        fail(f"unexpected publication terminal chapters: {includes[-2:]}")

    for token in [
        "Version 0.11 Publication Audit",
        r"\include{chapters/56_g024_complete_monotonicity_route_no_go}",
        r"\include{chapters/57_reciprocal_conjugation_orbit_collapse}",
        r"\input{frontmatter/roadmap}",
        r"\input{backmatter/final_synthesis}",
    ]:
        if token not in main_text:
            fail(f"main.tex missing publication token {token!r}")

    title_count = sum(p.read_text(encoding="utf-8").count(r"\begin{titlepage}") for p in MONO.rglob("*.tex"))
    if title_count != 1:
        fail(f"expected exactly one titlepage, found {title_count}")

    ledger = json.loads(CANON_LEDGER.read_text(encoding="utf-8"))
    ids = [item["id"] for item in ledger["claims"]]
    if len(ids) != len(set(ids)):
        fail("duplicate canonical claim IDs")
    if ledger.get("canonical_through") != "SOH-G023":
        fail("canonical_through must remain SOH-G023")
    if ledger.get("proof_of_rh") is not False:
        fail("canonical proof_of_rh firewall must remain false")
    if "SOH-G024" in ids:
        fail("SOH-G024 must not be silently inserted into canonical numbered ledger")

    g024 = json.loads(G024_LEDGER.read_text(encoding="utf-8"))
    if g024.get("promotion_status") != "INTEGRATED_MAINLINE_NOT_CANONICAL":
        fail("G024 integration/canon firewall changed")
    if g024.get("proof_of_rh") is not False:
        fail("G024 ledger proof_of_rh must remain false")

    t = json.loads(G024_T.read_text(encoding="utf-8"))
    if t.get("claim_id") != "SOH-G024-T":
        fail("missing reviewed G024-T claim")
    if t.get("status") != "REPOSITORY_REVIEWED_BRANCH_PROMOTED_THEOREM":
        fail("G024-T reviewed theorem status changed")
    if t.get("proof_of_rh") is not False:
        fail("G024-T must not claim RH")
    if t.get("route_effect", {}).get("closed_route") != "FULL_COMPLETE_MONOTONICITY_TO_GAUSSIAN_MIXTURE":
        fail("G024-T closed-route identity changed")

    required_text = "\n".join(
        p.read_text(encoding="utf-8")
        for p in [
            MONO / "frontmatter" / "title.tex",
            MONO / "frontmatter" / "abstract.tex",
            MONO / "chapters" / "46_current_canon_and_open_frontier.tex",
            MONO / "chapters" / "56_g024_complete_monotonicity_route_no_go.tex",
            MONO / "chapters" / "57_reciprocal_conjugation_orbit_collapse.tex",
            MONO / "appendices" / "D_claim_ledger.tex",
            MONO / "backmatter" / "final_synthesis.tex",
        ]
    )
    for token in [
        "SOH-G024-T",
        "not completely monotone",
        "CLOSED ROUTE / NO-GO",
        "u^{-1}=\\bar u",
        "Delta_{\\mathrm{RC}}",
        "Riemann Hypothesis remains OPEN",
    ]:
        if token not in required_text:
            fail(f"publication synthesis missing token {token!r}")

    print("MONOGRAPH_INTEGRATION_PASS")
    print(f"version=v0.11-publication-audit chapters={len(includes)} canonical_through=SOH-G023 g024_t=reviewed_route_nogo")


if __name__ == "__main__":
    main()
