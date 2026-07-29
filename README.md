# Secret of a Half

**Secret of a Half** is an independent research repository devoted to a precise mathematical investigation of why the value

\[
\operatorname{Re}(s)=\frac12
\]

appears as the distinguished symmetry axis in the analytic structure surrounding the Riemann zeta function.

The starting ansatz links four structures:

1. binary complementarity and the Shannon value \(\ln 2\);
2. exact destructive interference of a normalized two-channel state;
3. spinorial phase closure and the sign acquired under a \(2\pi\) rotation;
4. the zeta involution \(s\mapsto 1-\overline{s}\), whose fixed set is \(\operatorname{Re}(s)=1/2\).

## Research status

This repository begins with a **structural ansatz**, not a claimed proof of the Riemann Hypothesis.

The initial programme separates:

- exact lemmas that can already be proved;
- conditional theorems whose hypotheses are explicit;
- numerical or symbolic experiments;
- the unresolved bridge required to connect every non-trivial zeta zero to the proposed information-spinor cancellation mechanism.

The central open task is to construct a canonical map or operator for which vanishing is equivalent to a non-trivial zero of the completed zeta function while preserving the required symmetry, positivity and spectral structure.

## Initial mathematical core

For a normalized complementary state

\[
|\psi\rangle=\sqrt{\sigma}\,|0\rangle+e^{i\phi}\sqrt{1-\sigma}\,|1\rangle,
\qquad 0<\sigma<1,
\]

the squared amplitude of exact channel cancellation is

\[
\left|\sqrt{\sigma}+e^{i\phi}\sqrt{1-\sigma}\right|^2
=1+2\sqrt{\sigma(1-\sigma)}\cos\phi.
\]

It vanishes exactly when

\[
\sigma=\frac12,
\qquad
\phi\equiv\pi\pmod{2\pi}.
\]

Independently, binary Shannon entropy

\[
H(\sigma)=-\sigma\ln\sigma-(1-\sigma)\ln(1-\sigma)
\]

has its unique maximum at \(\sigma=1/2\), where \(H=\ln2\).

These facts identify the half-axis as the unique point of balanced binary distinction and exact complementary cancellation. They do not by themselves prove that every non-trivial zero of \(\zeta(s)\) lies there.

## Repository layout

```text
secret-of-a-half/
├── README.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── pyproject.toml
├── claims/
│   ├── CLAIM_LEDGER.md
│   └── claim_ledger.json
├── data/
│   ├── raw/
│   └── processed/
├── docs/
│   ├── ansatz/
│   ├── derivations/
│   └── open-problems/
├── figures/
├── logs/
├── monograph/
│   ├── chapters/
│   └── figures/
├── notebooks/
├── references/
├── scripts/
├── src/
│   └── secret_of_a_half/
└── tests/
```

## Working principles

- No claim is promoted from conjectural to proved without a written derivation or reproducible verification.
- Exact results, conditional results, numerical evidence and interpretation remain visibly separated.
- Change history is append-only.
- Existing projects are not treated as dependencies unless an explicit future decision introduces them.
- This repository is autonomous: its definitions, assumptions and proofs must stand on their own.

## Planned first milestones

1. Formalize the binary-complementarity axioms.
2. Prove the cancellation, entropy and involution lemmas.
3. State the conditional critical-line theorem with all hypotheses exposed.
4. Construct and test candidate zeta-state maps.
5. Investigate Hilbert–Pólya, de Branges, Weil and positivity routes without conflating analogy with proof.
6. Build the monograph from the claim ledger and verified derivations.

## Author

Adrian Lipa
