# The Zero Axis — monograph build

The monograph is modular LaTeX. Its entry point is `monograph/main.tex`.

## Active publication state

**Version 1.1 — Proof Edition — 24 September 2026**

The current title is:

> **The Zero Axis**  
> *A Proof of the Riemann Hypothesis from One Universal Relational-Zero Axiom*

The terminal proof architecture uses one foundational axiom only:

\[
\mathrm{A0}:\quad
\text{zero has no independent realization; a zero of an admitted observable
is the vanishing of its canonical relational defect.}
\]

From A0, Chapters 58–59 derive three complementary zero-axis paths:

1. relation/complement fixed point;
2. Shannon/KL information and action cost;
3. projective reciprocal–conjugation geometry with a \(U(1)\) half-turn cross-check.

The monograph explicitly claims and presents the proof theorem

\[
\boxed{\mathrm{A0}\Longrightarrow\mathrm{RH}.}
\]

## Publication structure

The book contains:

- title, abstract, preface, and Reader Roadmap;
- 59 numbered chapters;
- appendices for elementary proofs, asymmetric channels, numerical tables,
  the claim ledger, and notation;
- an integrated synthesis;
- bibliography from `references/references.bib` and `references/v09.bib`.

Chapters 1–57 preserve the historical analytic programme and route audits.
Their older OPEN or route-local non-proof labels are chronological records only. Chapters 58–59 contain the current proof.

## Current minimum proof graph

\[
\xi(\rho)=0
\stackrel{\mathrm{A0}}{\Longrightarrow}
E_{\rm rel}(\rho)=0
\Longrightarrow
\Delta_{\rm RC}(\Omega(\rho))=0
\Longrightarrow
\Re\rho=\frac12.
\]

The energy/coercivity step is derived:
\[
E_{\rm rel}(s)
\ge
D_H(\Re s)
\ge
\frac{|s|^2|1-s|^2}{2}\,
\Delta_{\rm RC}(\Omega(s)).
\]

The projective defect identity is exact:
\[
\Delta_{\rm RC}(\Omega(s))
=
\frac{4(\Re s-1/2)^2}{|s|^2|1-s|^2}.
\]

## Formal verification

`SecretOfAHalfFormal/RadialDefect.lean` contains the exact critical-line
defect theorem and the uniform and pointwise coercive zero-energy RH endgames.

## GREMLIN provenance

GREMLIN/OCTOPUS is used as a provenance, dependency-graph, route-compilation,
and adversarial-audit system.

Public demonstrations:

- `https://github.com/AdrianLipa90/GREMLIN-demo`
- `https://github.com/AdrianLipa90/Ciel-GREMLIN-Benchmark`

GREMLIN does not automatically promote mathematical claims; theorem authority
comes from the derivations, formal proof objects, and declared certificates.

## Reproducible build

The authoritative build workflows are:

- `.github/workflows/build-and-test.yml`
- `.github/workflows/vectorized-build-and-test.yml`

The build fails closed on regression failures, semantic-audit failures,
missing generated figures, LaTeX errors, undefined citations/references,
multiply defined references, and overfull boxes.

## Outputs

- `monograph/main.pdf` — compiled monograph;
- `monograph/figures/` — deterministic figures;
- `monograph/generated/` — generated LaTeX tables;
- `data/processed/` — deterministic receipts and tables.

## Chapter 58 — The Universal Relational Zero Law

Chapter 58 reduces the terminal architecture to A0 alone and derives the
fixed-point, Shannon/KL, and Relational Lagrange–Zero theorems without a second
foundational axiom.

## Chapter 59 — The Zero Axis: Three Complementary Minimal Proof Paths

Chapter 59 proves the same critical axis through relational, informational,
and projective/\(U(1)\) coordinates and closes the theorem
\(\mathrm{A0}\Rightarrow\mathrm{RH}\).
