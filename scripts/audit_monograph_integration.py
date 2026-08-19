#!/usr/bin/env python3
"""Fail closed when the active monograph omits chapters or collapses proof states."""
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

    prefixes = [name.split("_", 1)[0] for name in includes]
    expected = [f"{i:02d}" for i in range(1, len(includes) + 1)]
    if prefixes != expected:
        fail(f"chapter numbering is not contiguous: {prefixes}")

    if not includes or includes[-1] != "55_g024_third_order_cumulant_frontier":
        fail("G024 terminal numbered chapter must be 55_g024_third_order_cumulant_frontier")
    for required in [
        "49_reciprocal_deficit_pf3_normal_form",
        "50_jensen_wiener_kernel_frontier",
        "51_g024_second_order_bridge_reduction",
        "52_g024_bridge_moment_tail_second_order",
        "53_g024_sharpened_curvature_second_order",
        "54_g024_global_second_order_closure",
        "55_g024_third_order_cumulant_frontier",
    ]:
        if required not in includes:
            fail(f"required integrated chapter missing: {required}")

    for required in [r"\input{frontmatter/roadmap}", r"\input{backmatter/final_synthesis}"]:
        if required not in main_text:
            fail(f"v0.10 publication layer missing {required}")

    title_count = sum(
        p.read_text(encoding="utf-8").count(r"\begin{titlepage}")
        for p in MONO.rglob("*.tex")
    )
    if title_count != 1:
        fail(f"expected exactly one titlepage, found {title_count}")
    if r"\maketitle" in main_text:
        fail("main.tex must not create a second title page via \\maketitle")

    frontmatter_text = "\n".join(
        [main_text]
        + [p.read_text(encoding="utf-8") for p in (MONO / "frontmatter").glob("*.tex")]
    )
    if "Streszczenie" in frontmatter_text:
        fail("non-English frontmatter marker Streszczenie remains active")
    for stale in ["Version 0.6.1-review", "Version 0.7 --", "Version 0.9 Integrated Canon V3"]:
        if stale in frontmatter_text:
            fail(f"stale active version marker remains in title/frontmatter: {stale}")
    if "Version 0.10 Mainline Integration" not in frontmatter_text:
        fail("v0.10 Mainline Integration marker missing from active title/frontmatter")
    if "SOH-G023" not in frontmatter_text:
        fail("G023 canonical marker missing from active title/frontmatter")
    if "Integrated G024 Research Line" not in frontmatter_text:
        fail("G024 must be identified as an integrated research line")
    if "Repository integration is not treated as mathematical canonization" not in frontmatter_text:
        fail("mainline-vs-canonization firewall missing from frontmatter")

    ledger = json.loads(CANON_LEDGER.read_text(encoding="utf-8"))
    ids = [item["id"] for item in ledger["claims"]]
    if len(ids) != len(set(ids)):
        dup = sorted({x for x in ids if ids.count(x) > 1})
        fail(f"duplicate canonical claim IDs: {dup}")
    promoted = {f"SOH-L{i:03d}" for i in range(12, 33)}
    if not promoted.issubset(ids):
        fail(f"promoted SOH-L012--SOH-L032 range incomplete: {sorted(promoted - set(ids))}")
    g_line = {f"SOH-G{i:03d}" for i in range(1, 24)}
    if not g_line.issubset(ids):
        fail(f"canonical SOH-G001--SOH-G023 range incomplete: {sorted(g_line - set(ids))}")
    if "SOH-G024" in ids:
        fail("SOH-G024 must not be silently promoted into the canonical numbered ledger")
    if ledger.get("canonical_through") != "SOH-G023":
        fail("machine claim ledger canonical_through must equal SOH-G023")
    if ledger.get("proof_of_rh") is not False:
        fail("canonical proof_of_rh firewall must remain false")

    candidate = json.loads(G024_LEDGER.read_text(encoding="utf-8"))
    # Legacy machine status token is retained as a mathematical-promotion firewall;
    # it no longer describes the Git branch location after G024 was merged to main.
    if candidate.get("promotion_status") != "BRANCH_CANDIDATE_NOT_CANONICAL":
        fail("G024 research-line ledger must remain explicitly non-canonical")
    if candidate.get("proof_of_rh") is not False:
        fail("G024 proof_of_rh firewall must remain false")
    candidate_ids = {item["id"] for item in candidate.get("claims", [])}
    required_candidate = {
        "SOH-G024-A", "SOH-G024-B", "SOH-G024-C", "SOH-G024-D", "SOH-G024-E",
        "SOH-G024-F", "SOH-G024-G", "SOH-G024-H", "SOH-G024-I", "SOH-G024-J",
        "SOH-G024-K", "SOH-G024-L", "SOH-G024-M", "SOH-G024-P", "SOH-G024-Q",
        "SOH-G024-R", "SOH-G024-S", "SOH-G024-N1",
    }
    if not required_candidate.issubset(candidate_ids):
        fail(f"G024 research-line ledger incomplete: {sorted(required_candidate - candidate_ids)}")

    by_id = {item["id"]: item for item in candidate.get("claims", [])}
    if by_id["SOH-G024-M"].get("status") != "proved_sharpened_strong_convexity":
        fail("G024-M must record sharpened strong convexity")
    m_statement = by_id["SOH-G024-M"].get("statement", "")
    if "-(log K)''>17" not in m_statement and "L''>17" not in m_statement:
        fail("G024-M is missing the >17 strong-convexity margin")
    if by_id["SOH-G024-Q"].get("status") != "computer_assisted_fourth_log_curvature_certificate":
        fail("G024-Q must record the computer-assisted fourth-log-curvature certificate")
    if "mpmath.iv" not in by_id["SOH-G024-Q"].get("statement", ""):
        fail("G024-Q must expose the interval-engine trust boundary")
    if by_id["SOH-G024-R"].get("status") != "proved_global_second_order_complete_monotonicity_computer_assisted_dependency":
        fail("G024-R must record global second-order closure")
    if "793/48" not in by_id["SOH-G024-R"].get("statement", ""):
        fail("G024-R is missing the strict Riccati gap")
    if by_id["SOH-G024-S"].get("status") != "exact_third_order_bridge_cumulant_reduction_open_sign":
        fail("G024-S must remain an exact third-order reduction with open sign")

    print("MONOGRAPH_INTEGRATION_PASS")
    print(
        f"version=v0.10-mainline-g024 chapters={len(chapter_files)} canonical_claims={len(ids)} "
        f"titlepages={title_count} terminal={includes[-1]}"
    )


if __name__ == "__main__":
    main()
