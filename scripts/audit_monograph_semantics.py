#!/usr/bin/env python3
"""Deterministic semantic guard for the integrated monograph.

This script does not attempt to decide mathematical truth. It protects the
repository-level semantic invariants through canonical SOH-G023 and checks that
SOH-G024 remains an explicitly non-canonical candidate with an open-RH firewall.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "monograph"
MAIN = MONOGRAPH / "main.tex"
LEDGER = MONOGRAPH / "appendices" / "D_claim_ledger.tex"
FINAL = MONOGRAPH / "chapters" / "46_current_canon_and_open_frontier.tex"
TITLE = MONOGRAPH / "frontmatter" / "title.tex"
G024 = MONOGRAPH / "chapters" / "50_jensen_wiener_kernel_frontier.tex"


def tex_files() -> list[Path]:
    return sorted(MONOGRAPH.rglob("*.tex"))


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def main() -> int:
    errors: list[str] = []
    files = tex_files()

    forbidden = {
        "anti-linear involution": "K(s)=1-conj(s) is conjugate-affine, not anti-linear in the affine s coordinate",
        "anti-linear reflection": "use conjugate-affine/anti-holomorphic reflection; anti-linearity applies only after centering",
        "anti-linear pair": "a pair involving complex conjugation is not itself an anti-linear map",
        "current terminal obstruction remains": "the integrated monograph now has multiple explicitly separated open frontiers",
        "The next progress will not come from": "Chapter 15 is an interim historical conclusion, not the current endpoint",
    }
    for path in files:
        text = path.read_text(encoding="utf-8")
        for phrase, reason in forbidden.items():
            if phrase.lower() in text.lower():
                fail(f"{path.relative_to(ROOT)}: forbidden phrase {phrase!r} ({reason})", errors)

    interpretive_patterns = [
        r"\bmay be interpreted as\b",
        r"\bmay then be interpreted as\b",
        r"\bsuggests an interpretation\b",
        r"\bsuggests the interpretation\b",
        r"\bcan be interpreted as\b",
        r"\bas interpretation rather than\b",
    ]
    for path in files:
        text = path.read_text(encoding="utf-8")
        paragraphs = re.split(r"\n\s*\n", text)
        for paragraph in paragraphs:
            low = paragraph.lower()
            if any(re.search(pattern, low) for pattern in interpretive_patterns):
                if "INTERPRETACJA" not in paragraph:
                    preview = " ".join(paragraph.split())[:180]
                    fail(f"{path.relative_to(ROOT)}: unlabeled interpretive assertion: {preview}", errors)

    main_text = MAIN.read_text(encoding="utf-8")
    required_main_tokens = [
        r"\include{chapters/46_current_canon_and_open_frontier}",
        r"\include{chapters/47_half_mass_pf2_does_not_imply_pf3}",
        r"\include{chapters/48_pf3_one_step_curvature_barrier}",
        r"\include{chapters/49_reciprocal_deficit_pf3_normal_form}",
        r"\include{chapters/50_jensen_wiener_kernel_frontier}",
        "Version 0.9 Integrated Canon V3",
    ]
    for token in required_main_tokens:
        if token not in main_text:
            fail(f"monograph/main.tex: missing required V3 token {token!r}", errors)

    title_text = TITLE.read_text(encoding="utf-8")
    if "Version 0.9 Integrated Canon V3" not in title_text:
        fail("title page does not identify Integrated Canon V3", errors)
    if "SOH-G023" not in title_text:
        fail("title page does not identify canonical SOH-G023", errors)
    if "G024" not in title_text or "Candidate" not in title_text:
        fail("title page must identify G024 as candidate", errors)
    if "does not claim a proof of the Riemann Hypothesis" not in title_text:
        fail("title page is missing the explicit no-RH-proof firewall", errors)

    ledger_text = LEDGER.read_text(encoding="utf-8")
    for number in range(1, 24):
        claim = f"SOH-G{number:03d}"
        if claim not in ledger_text:
            fail(f"claim ledger is missing {claim}", errors)
    if "SOH-G002" in ledger_text and "Inactive / not promoted" not in ledger_text:
        fail("SOH-G002 must remain explicitly inactive/not promoted unless a standalone theorem is canonized", errors)
    for token in [
        "SOH-G003",
        "SOH-G021",
        "SOH-G022",
        "SOH-G023",
        "actual PF$_3$ OPEN",
        "PF$_3$",
        "PF$_\\infty$",
        "Riemann Hypothesis remains OPEN",
    ]:
        if token not in ledger_text:
            fail(f"claim ledger is missing open-frontier token {token!r}", errors)

    final_text = FINAL.read_text(encoding="utf-8")
    required_final = [
        "P_J=\\varnothing",
        "P_N=\\varnothing",
        "SOH-G003 OPEN",
        "SOH-C005 OPEN",
        "SOH-G021",
        "SOH-G022",
        "SOH-G023",
        "G024",
        "RH OPEN",
        "PF$_2$",
        "PF$_3$",
        "PF$_\\infty$",
    ]
    for token in required_final:
        if token not in final_text:
            fail(f"final synthesis is missing required status token {token!r}", errors)

    g024_text = G024.read_text(encoding="utf-8")
    for token in [
        "complete monotonicity",
        "D_y",
        "J_y",
        "0<|y|<\\frac12",
        "Riemann Hypothesis remains open",
    ]:
        if token not in g024_text:
            fail(f"G024 candidate chapter is missing firewall token {token!r}", errors)
    if "D_y(u)=\\cosh(2yu)C(u)" not in g024_text:
        fail("G024 external Dimitrov-Xu tilt is not recorded")
    if "J_y(u)" not in g024_text or "D_0=J_0=C" not in g024_text:
        fail("G024 external/internal tilt distinction is incomplete", errors)

    ch3 = (MONOGRAPH / "chapters" / "03_symmetry_and_the_half_axis.tex").read_text(encoding="utf-8")
    if "conjugate-affine involution" not in ch3 or "not anti-linear" not in ch3:
        fail("Chapter 3 must explicitly distinguish affine conjugation from centered anti-linearity", errors)

    if errors:
        print("SEMANTIC AUDIT: FAIL")
        for error in errors:
            print(f" - {error}")
        return 1

    print("SEMANTIC AUDIT: PASS")
    print(f"Checked {len(files)} LaTeX source files.")
    print("Protected invariants: affine involution terminology, interpretation labels, G001-G023 canonical ledger, G024 candidate firewall, and RH/PF3/PF-infinity firewalls.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
