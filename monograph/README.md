# Monograph build

The monograph is modular LaTeX. Its entry point is `main.tex`.

## Review version

The active review branch is **Version 0.6.1-review — 7 August 2026**.  It retains
the Version 0.6 adaptive-cutoff results and adds the DHSE-001 Stage-M exact
finite classification, reciprocal-symmetry counterexample, fixed-width
arithmetic certificate, and synchronized claim ledgers.  The review line does
not promote the open zeta/RH bridges.

## Reproducible build

From the repository root, generate the deterministic assets and validation
receipts used by the monograph, then compile `monograph/main.tex` with the
LaTeX/BibTeX sequence declared by the repository workflow.

The current build pipeline regenerates:

- monograph figures and tables;
- PhaseNav-Weil Hermite-ladder receipt;
- zero/undefined reciprocal-duality receipt;
- prime-tail certificate;
- adaptive-cutoff schedule;
- DHSE regression receipts through Stage M.

The authoritative executable commands remain in `.github/workflows/build-and-test.yml`.
This avoids duplicating a shell command sequence here that can drift from CI.

## Outputs

- `main.pdf` — compiled Version 0.6.1-review monograph on the review branch;
- `figures/` — deterministic PDF and PNG figures;
- `generated/` — generated LaTeX tables;
- `main.log` — TeX build log.

## Version 0.6 baseline additions

- Chapter 20: basis-adaptive prime cutoffs;
- elementary `h(U)/alpha(U)` tail envelope;
- coarse Hermite finite-section majorant;
- exact asymptotic collapse for every schedule `Q_N=exp(cN)`, `c>0`;
- deterministic sharp-certificate audit through `N=20`.

## Version 0.6.1 review additions

- Stage M exact rational endpoint classification over all `q>0` for the declared
  primitive `K=6`, radius `1/10`, word-length `1..4` universe;
- explicit conservative `int64` overflow certificate before vectorized Stage-M
  arithmetic;
- exact finite result that `q=1` is the unique global forcing maximum at lengths
  2 and 3 but not at lengths 1 and 4;
- explicit counterexample to the inference
  `reciprocal symmetry => central maximum`;
- Stage-B and Stage-I historical receipt-provenance compatibility audit without
  rewriting historical receipts;
- synchronized JSON, Markdown, and LaTeX claim ledgers;
- explicit retention of `SOH-C004` and `SOH-C005` as open bridges.

## Claim boundary

The adaptive diagonal tail is controlled when the cutoff grows exponentially
with the basis size. One fixed cutoff uniform in all basis sizes, positivity of
all infinite-cutoff sections, continuity of the full regularized Weil form and
the null-space implication to native closure remain open.

DHSE Stage M is an exact finite computer-assisted theorem only on its declared
operator universe and lengths.  It establishes that reciprocal self-duality
alone does not force dynamical extremality; it does not establish an all-length
or all-operator theorem and does not close a canonical zeta-state bridge.

Version 0.6.1-review does not claim a proof of the Riemann Hypothesis.
