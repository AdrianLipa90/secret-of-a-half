#!/usr/bin/env python3
"""Deterministic semantic guard for the integrated monograph.

This script does not decide mathematical truth. It protects the repository-level
proof-state boundaries through canonical SOH-G023 and the non-canonical G024
candidate: first order global, second order proved for q>=1/9, compact core open,
higher orders and RH open.
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
G024_SECOND = MONOGRAPH / "chapters" / "51_g024_second_order_bridge_reduction.tex"
G024_TAIL = MONOGRAPH / "chapters" / "52_g024_bridge_moment_tail_second_order.tex"
G024_SHARP = MONOGRAPH / "chapters" / "53_g024_sharpened_curvature_second_order.tex"


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
        for paragraph in re.split(r"\n\s*\n", text):
            low = paragraph.lower()
            if any(re.search(pattern, low) for pattern in interpretive_patterns):
                if "INTERPRETACJA" not in paragraph:
                    preview = " ".join(paragraph.split())[:180]
                    fail(f"{path.relative_to(ROOT)}: unlabeled interpretive assertion: {preview}", errors)

    main_text = MAIN.read_text(encoding="utf-8")
    for token in [
        r"\include{chapters/49_reciprocal_deficit_pf3_normal_form}",
        r"\include{chapters/50_jensen_wiener_kernel_frontier}",
        r"\include{chapters/51_g024_second_order_bridge_reduction}",
        r"\include{chapters/52_g024_bridge_moment_tail_second_order}",
        r"\include{chapters/53_g024_sharpened_curvature_second_order}",
        "Version 0.9 Integrated Canon V3",
    ]:
        if token not in main_text:
            fail(f"monograph/main.tex: missing required token {token!r}", errors)

    title_text = TITLE.read_text(encoding="utf-8")
    for token, message in [
        ("Version 0.9 Integrated Canon V3", "title page does not identify Integrated Canon V3"),
        ("SOH-G023", "title page does not identify canonical SOH-G023"),
        ("G024", "title page does not identify G024"),
        ("Candidate", "title page does not mark G024 candidate"),
        ("does not claim a proof of the Riemann Hypothesis", "title page is missing no-RH-proof firewall"),
    ]:
        if token not in title_text:
            fail(message, errors)

    ledger_text = LEDGER.read_text(encoding="utf-8")
    for number in range(1, 24):
        if f"SOH-G{number:03d}" not in ledger_text:
            fail(f"claim ledger is missing SOH-G{number:03d}", errors)
    for token in ["SOH-G003", "SOH-G023", "actual PF$_3$ OPEN", "PF$_\\infty$", "Riemann Hypothesis remains OPEN"]:
        if token not in ledger_text:
            fail(f"claim ledger is missing open-frontier token {token!r}", errors)

    final_text = FINAL.read_text(encoding="utf-8")
    for token in [
        "P_J=\\varnothing", "P_N=\\varnothing", "SOH-G003 OPEN", "SOH-C005 OPEN",
        "SOH-G023", "G024", "RH OPEN", "PF$_2$", "PF$_3$", "PF$_\\infty$",
        "H_y'<0", "H_y''>0", "q\\ge1/9", "0\\le q<1/9",
    ]:
        if token not in final_text:
            fail(f"final synthesis is missing status token {token!r}", errors)

    g024_text = G024.read_text(encoding="utf-8")
    for token in [
        "complete monotonicity", "D_y", "J_y", "0<|y|<\\frac12",
        "Riemann Hypothesis remains open", "SOH-G024 first-order complete-monotonicity theorem",
        "H_y''", "S_y'(q)\\le S_y(q)^2", "f'(x+iy)^2-f(x+iy)f''(x+iy)",
    ]:
        if token not in g024_text:
            fail(f"Chapter 50 is missing theorem/firewall token {token!r}", errors)
    if "D_y(u)=\\cosh(2yu)C(u)" not in g024_text or "D_0=J_0=C" not in g024_text:
        fail("Chapter 50 external/internal tilt firewall incomplete", errors)

    second_text = G024_SECOND.read_text(encoding="utf-8")
    for token in [
        "d\\mu_u", "A_u(r)", "B_u(r)", "R'(u)",
        "\\operatorname{Var}_{\\mu_u}(A_u)", "4u^3H_y''",
        "uD_y''(u)-D_y'(u)", "S_y'\\le S_y^2", "RH remain OPEN",
    ]:
        if token not in second_text:
            fail(f"Chapter 51 is missing bridge/firewall token {token!r}", errors)

    tail_text = G024_TAIL.read_text(encoding="utf-8")
    for token in [
        "Bridge Moment Hierarchy", "\\mathbb E[rD_u(r)]=3", "\\mathbb E[r^2]<\\frac3{20}",
        "(1-\\lambda/10)^{-3/2}", "10<L''(s)<21e^{2|s|}",
        "H_y''(q)>0", "q\\ge\\frac14", "0\\le q<\\frac14", "remains OPEN",
    ]:
        if token not in tail_text:
            fail(f"Chapter 52 is missing historical tail token {token!r}", errors)

    sharp_text = G024_SHARP.read_text(encoding="utf-8")
    for token in [
        "L''(t)>17", "\\frac{33}{2}", "34^n", "(1-\\lambda/17)^{-3/2}",
        "\\mathbb E[B_u]<79e^{2u}", "H_y''(q)>0", "q\\ge1/9",
        "0\\le q<\\frac19", "remains OPEN", "does not claim RH",
    ]:
        if token not in sharp_text:
            fail(f"Chapter 53 is missing sharpened theorem/firewall token {token!r}", errors)

    ch3 = (MONOGRAPH / "chapters" / "03_symmetry_and_the_half_axis.tex").read_text(encoding="utf-8")
    if "conjugate-affine involution" not in ch3 or "not anti-linear" not in ch3:
        fail("Chapter 3 must distinguish affine conjugation from centered anti-linearity", errors)

    if errors:
        print("SEMANTIC AUDIT: FAIL")
        for error in errors:
            print(f" - {error}")
        return 1

    print("SEMANTIC AUDIT: PASS")
    print(f"Checked {len(files)} LaTeX source files.")
    print("Protected invariants: G001-G023 canon; G024 L''>17; first order global; second order q>=1/9; q<1/9 open; higher orders/RH open.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
