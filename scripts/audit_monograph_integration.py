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

    if not includes or includes[-1] != "52_g024_bridge_moment_tail_second_order":
        fail("G024 candidate terminal chapter must be 52_g024_bridge_moment_tail_second_order")
    for required in [
        "49_reciprocal_deficit_pf3_normal_form",
        "50_jensen_wiener_kernel_frontier",
        "51_g024_second_order_bridge_reduction",
        "52_g024_bridge_moment_tail_second_order",
    ]:
        if required not in includes:
            fail(f"required integrated chapter missing: {required}")

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
    if "Version 0.6.1-review" in frontmatter_text or "Version 0.7 --" in frontmatter_text:
        fail("stale active version marker remains in title/frontmatter")
    if "Version 0.9 Integrated Canon V3" not in frontmatter_text:
        fail("v0.9 Integrated Canon V3 marker missing from active title/frontmatter")
    if "SOH-G023" not in frontmatter_text:
        fail("G023 canonical marker missing from active title/frontmatter")
    if "G024" not in frontmatter_text or "Candidate" not in frontmatter_text:
        fail("G024 must be identified as candidate in active title/frontmatter")

    collision_checks = {
        "18_zero_undefined_reciprocal_duality.tex": ("SOH-L015", "SOH-L016", "SOH-L017", "SOH-L022"),
        "19_phasenav_weil_prime_tail_certificate.tex": ("SOH-L018", "SOH-L019", "SOH-L020"),
        "20_phasenav_weil_adaptive_cutoff.tex": ("SOH-L021",),
    }
    declaration_markers = (r"\textbf{", r"\item[", r"\status{")
    for filename, forbidden in collision_checks.items():
        text = (CHAPTERS / filename).read_text(encoding="utf-8")
        for claim_id in forbidden:
            for line in text.splitlines():
                if claim_id not in line:
                    continue
                if any(marker in line for marker in declaration_markers):
                    fail(f"legacy claim collision {claim_id} remains active in {filename}: {line.strip()}")

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
        fail("SOH-G024 must not be promoted into the canonical ledger on this candidate branch")
    if ledger.get("canonical_through") != "SOH-G023":
        fail("machine claim ledger canonical_through must equal SOH-G023")
    if ledger.get("proof_of_rh") is not False:
        fail("canonical proof_of_rh firewall must remain false")

    candidate = json.loads(G024_LEDGER.read_text(encoding="utf-8"))
    if candidate.get("promotion_status") != "BRANCH_CANDIDATE_NOT_CANONICAL":
        fail("G024 branch ledger must remain explicitly non-canonical")
    if candidate.get("proof_of_rh") is not False:
        fail("G024 proof_of_rh firewall must remain false")
    candidate_ids = {item["id"] for item in candidate.get("claims", [])}
    required_candidate = {
        "SOH-G024-A", "SOH-G024-B", "SOH-G024-C", "SOH-G024-D", "SOH-G024-E",
        "SOH-G024-F", "SOH-G024-G", "SOH-G024-H", "SOH-G024-I", "SOH-G024-J",
        "SOH-G024-K", "SOH-G024-L", "SOH-G024-N1",
    }
    if not required_candidate.issubset(candidate_ids):
        fail(f"G024 branch ledger incomplete: {sorted(required_candidate - candidate_ids)}")

    by_id = {item["id"]: item for item in candidate.get("claims", [])}
    if by_id["SOH-G024-L"].get("status") != "proved_second_order_tail_region":
        fail("G024-L must record proved second-order tail region")
    if "compact core" not in by_id["SOH-G024-L"].get("statement", ""):
        fail("G024-L must keep the compact-core-open firewall")

    print("MONOGRAPH_INTEGRATION_PASS")
    print(
        f"version=V3-G023+G024-candidate chapters={len(chapter_files)} canonical_claims={len(ids)} "
        f"titlepages={title_count} terminal={includes[-1]}"
    )


if __name__ == "__main__":
    main()
