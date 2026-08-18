#!/usr/bin/env python3
"""Fail closed when the active monograph omits chapters or reintroduces legacy claim collisions."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "monograph"
MAIN = MONO / "main.tex"
CHAPTERS = MONO / "chapters"


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

    # V3 must contain the semantic-audit final synthesis as the terminal numbered chapter.
    if not includes or includes[-1] != "46_current_canon_and_open_frontier":
        fail("V3 terminal chapter must be 46_current_canon_and_open_frontier")

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

    ledger = json.loads((ROOT / "claims" / "claim_ledger.json").read_text(encoding="utf-8"))
    ids = [item["id"] for item in ledger["claims"]]
    if len(ids) != len(set(ids)):
        dup = sorted({x for x in ids if ids.count(x) > 1})
        fail(f"duplicate canonical claim IDs: {dup}")
    promoted = {f"SOH-L{i:03d}" for i in range(12, 33)}
    if not promoted.issubset(ids):
        fail(f"promoted SOH-L012--SOH-L032 range incomplete: {sorted(promoted - set(ids))}")
    if ledger.get("proof_of_rh") is not False:
        fail("proof_of_rh firewall must remain false")

    print("MONOGRAPH_INTEGRATION_PASS")
    print(
        f"version=V3 chapters={len(chapter_files)} canonical_claims={len(ids)} "
        f"titlepages={title_count} terminal={includes[-1]}"
    )


if __name__ == "__main__":
    main()
