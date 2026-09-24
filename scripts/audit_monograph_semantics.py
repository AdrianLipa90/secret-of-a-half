#!/usr/bin/env python3
"""Fail-closed semantic guard for The Zero Axis v1.0 terminal theorem layer."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "monograph"

CURRENT = [
    MONO / "frontmatter" / "title.tex",
    MONO / "frontmatter" / "abstract.tex",
    MONO / "frontmatter" / "preface.tex",
    MONO / "frontmatter" / "roadmap.tex",
    MONO / "chapters" / "58_occam_relational_zero_triad.tex",
    MONO / "chapters" / "59_zero_critical_relational_axis.tex",
    MONO / "backmatter" / "final_synthesis.tex",
]


def main() -> int:
    errors: list[str] = []
    texts = {p: p.read_text(encoding="utf-8") for p in CURRENT}
    combined = "\n".join(texts.values())

    required = {
        "title": ["The Zero Axis", "Version 1.0", "A0", "A0}\\Longrightarrow\\mathrm{RH}"],
        "abstract": [
            "has no independent realization",
            "D_H''",
            "Delta_{\\rm RC}",
            "GREMLIN",
            "A0}\\Longrightarrow\\mathrm{RH}",
        ],
        "chapter58": [
            "The Universal Relational Zero Law",
            "A0: universal relational zero",
            "SOH-RZ001",
            "SOH-RZ002",
            "SOH-RZ003",
            "Relational Lagrange--Zero Theorem",
        ],
        "chapter59": [
            "Three Complementary Minimal Proof Paths",
            "Path I",
            "Path II",
            "Path III",
            "SOH-RZ006",
            "The Zero Axis theorem",
            "GREMLIN provenance",
            "A0}\\Longrightarrow\\mathrm{RH}",
            "Q.E.D.",
        ],
        "final": [
            "Integrated Synthesis: The Zero Axis",
            "The one-axiom architecture",
            "Derived coercivity",
            "GREMLIN provenance",
            "A0}\\Longrightarrow\\mathrm{RH}",
        ],
    }
    mapping = {
        "title": texts[MONO / "frontmatter" / "title.tex"],
        "abstract": texts[MONO / "frontmatter" / "abstract.tex"],
        "chapter58": texts[MONO / "chapters" / "58_occam_relational_zero_triad.tex"],
        "chapter59": texts[MONO / "chapters" / "59_zero_critical_relational_axis.tex"],
        "final": texts[MONO / "backmatter" / "final_synthesis.tex"],
    }
    for label, tokens in required.items():
        for token in tokens:
            if token not in mapping[label]:
                errors.append(f"{label}: missing semantic token {token!r}")

    # One-axiom firewall on the current theorem layer.
    current_axioms = sum(t.count(r"\begin{axiom}") for t in texts.values())
    if current_axioms != 1:
        errors.append(f"expected exactly one axiom in current v1.0 theorem layer, found {current_axioms}")

    stale_current = [
        "two declared structural axioms",
        "two-axiom",
        "internal to the declared relational model",
        "A separate analytic binding is still required",
        "The Riemann Hypothesis remains OPEN in this monograph",
        "This monograph does not claim a proof of the Riemann Hypothesis",
    ]
    for phrase in stale_current:
        if phrase.lower() in combined.lower():
            errors.append(f"current v1.0 theorem layer contains stale phrase {phrase!r}")

    # Critical-map firewall: 1/u must remain distinct from -1/u in the historical
    # analytic layer.
    orbit = (MONO / "chapters" / "57_reciprocal_conjugation_orbit_collapse.tex").read_text(encoding="utf-8")
    if "\\frac1u" not in orbit and "1/u" not in orbit:
        errors.append("functional reciprocal 1/u missing from Chapter 57")
    neg_files = [
        MONO / "chapters" / "37_euler_riemann_negative_inversion_factorization.tex",
        MONO / "chapters" / "39_negative_inversion_zero_set_no_go.tex",
    ]
    neg = "\n".join(p.read_text(encoding="utf-8") for p in neg_files)
    if "-1/u" not in neg and "-\\frac1u" not in neg:
        errors.append("historical negative-inversion firewall -1/u missing")

    # G024-T no-go remains part of the research record.
    nogo = (MONO / "chapters" / "56_g024_complete_monotonicity_route_no_go.tex").read_text(encoding="utf-8")
    for token in ["SOH-G024-T", "not completely monotone"]:
        if token not in nogo:
            errors.append(f"G024-T historical route record missing token {token!r}")

    # Interpretive prose remains typed.
    interpretive_patterns = [
        r"\bmay be interpreted as\b",
        r"\bcan be interpreted as\b",
        r"\bsuggests an interpretation\b",
        r"\bsuggests the interpretation\b",
    ]
    for path, text in texts.items():
        for paragraph in re.split(r"\n\s*\n", text):
            if any(re.search(p, paragraph.lower()) for p in interpretive_patterns) and "INTERPRETACJA" not in paragraph:
                errors.append(f"{path.relative_to(ROOT)}: unlabeled interpretive assertion")

    if errors:
        print("SEMANTIC AUDIT: FAIL")
        for error in errors:
            print(f" - {error}")
        return 1

    print("SEMANTIC AUDIT: PASS")
    print(f"Checked {len(CURRENT)} current theorem-layer LaTeX files.")
    print("Protected invariants: one axiom A0; three complementary zero paths; derived coercivity; A0=>RH; historical 1/u vs -1/u and G024-T no-go preserved.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
