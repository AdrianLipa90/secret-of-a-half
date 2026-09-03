#!/usr/bin/env python3
"""Fail-closed semantic guard for the v0.11 publication state."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "monograph"


def main() -> int:
    errors: list[str] = []
    files = sorted(MONO.rglob("*.tex"))

    forbidden = {
        "anti-linear involution": "affine map s->1-conj(s) is conjugate-affine/anti-holomorphic",
        "anti-linear reflection": "use conjugate-affine or anti-holomorphic in the affine coordinate",
        "full complete monotonicity remains open": "SOH-G024-T proves this route impossible",
        "prove complete monotonicity of H_y for all derivative orders": "obsolete route after SOH-G024-T",
        "all orders m\\ge3 remain open": "after G024-T some signed inequality is known to fail; only its first failure is unknown",
    }
    for path in files:
        text = path.read_text(encoding="utf-8")
        low = text.lower()
        for phrase, reason in forbidden.items():
            if phrase.lower() in low:
                errors.append(f"{path.relative_to(ROOT)}: forbidden stale phrase {phrase!r} ({reason})")

    interpretive_patterns = [
        r"\bmay be interpreted as\b", r"\bcan be interpreted as\b",
        r"\bsuggests an interpretation\b", r"\bsuggests the interpretation\b",
    ]
    for path in files:
        text = path.read_text(encoding="utf-8")
        for paragraph in re.split(r"\n\s*\n", text):
            if any(re.search(p, paragraph.lower()) for p in interpretive_patterns) and "INTERPRETACJA" not in paragraph:
                errors.append(f"{path.relative_to(ROOT)}: unlabeled interpretive assertion")

    title = (MONO / "frontmatter" / "title.tex").read_text(encoding="utf-8")
    abstract = (MONO / "frontmatter" / "abstract.tex").read_text(encoding="utf-8")
    roadmap = (MONO / "frontmatter" / "roadmap.tex").read_text(encoding="utf-8")
    current = (MONO / "chapters" / "46_current_canon_and_open_frontier.tex").read_text(encoding="utf-8")
    third = (MONO / "chapters" / "55_g024_third_order_cumulant_frontier.tex").read_text(encoding="utf-8")
    nogo = (MONO / "chapters" / "56_g024_complete_monotonicity_route_no_go.tex").read_text(encoding="utf-8")
    orbit = (MONO / "chapters" / "57_reciprocal_conjugation_orbit_collapse.tex").read_text(encoding="utf-8")
    ledger = (MONO / "appendices" / "D_claim_ledger.tex").read_text(encoding="utf-8")
    final = (MONO / "backmatter" / "final_synthesis.tex").read_text(encoding="utf-8")

    required = {
        "title": (title, ["Version 0.11 Publication Audit", "SOH-G024-T", "does not claim a proof of the Riemann Hypothesis"]),
        "abstract": (abstract, ["not completely monotone", "reciprocal--conjugation orbit collapse", "Riemann Hypothesis"]),
        "roadmap": (roadmap, ["Route no-go", "full complete monotonicity", "Projective orbit"]),
        "current": (current, ["CLOSED ROUTE / NO-GO", "Delta_{\\mathrm{RC}}", "u^{-1}=\\bar u", "RH OPEN"]),
        "third": (third, ["SOH-G024-T", "no longer a sufficient route to RH", "direct surviving RH-equivalent G024 target"]),
        "nogo": (nogo, ["SOH-G024-T", "not completely monotone", "Bernstein lower-envelope lemma", "strict external Fourier positivity"]),
        "orbit": (orbit, ["\\mathcal I_u(u)=\\frac1u", "\\mathcal C_u(u)=\\overline u", "Delta_{\\mathrm{RC}}", "No QED for RH is claimed"]),
        "ledger": (ledger, ["SOH-G024-T", "REVIEWED THEOREM-LEVEL ROUTE NO-GO", "EXACT RH-EQUIVALENT REFORMULATION; NOT A PROOF"]),
        "final": (final, ["CLOSED ROUTE / NO-GO", "Delta_{\\mathrm{RC}}", "External Fourier positivity", "Riemann Hypothesis"]),
    }
    for label, (text, tokens) in required.items():
        for token in tokens:
            if token not in text:
                errors.append(f"{label}: missing semantic token {token!r}")

    # Critical map firewall: functional reciprocal must never be identified with Li/Euler negative inversion.
    combined = current + orbit + ledger + abstract
    if "u\\mapsto1/u" not in combined and "u)=1/u" not in combined and "u)=\\frac1u" not in combined:
        errors.append("functional reciprocal u->1/u is not explicitly represented")
    if "-1/u" not in combined and "-\\frac1u" not in combined:
        errors.append("negative-inversion firewall -1/u is not explicitly represented")

    # Publication must preserve the actual proof boundary.
    proof_boundary = title + abstract + current + orbit + final
    if "Riemann Hypothesis" not in proof_boundary or "OPEN" not in proof_boundary:
        errors.append("RH OPEN firewall missing from publication boundary")
    if "X(u)=0" not in orbit or "Delta_{\\mathrm{RC}}(u)=0" not in orbit:
        errors.append("orbit chapter must expose the unproved zerohood-to-defect implication")

    if errors:
        print("SEMANTIC AUDIT: FAIL")
        for error in errors:
            print(f" - {error}")
        return 1

    print("SEMANTIC AUDIT: PASS")
    print(f"Checked {len(files)} LaTeX source files.")
    print("Protected invariants: canon through G023; G024 m=1,2 proved; G024-T closes full CM route; 1/u separated from -1/u; orbit collapse exact RH-equivalence only; direct Fourier positivity and RH open.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
