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
├── construction/
│   └── phasenav/
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

## Monograph Version 0.2

The complete monograph is maintained as modular LaTeX in `monograph/`. GitHub Actions rebuilds the validated 92-page PDF and publishes it as the `secret-of-a-half-monograph-v0.2` workflow artifact. It contains 16 chapters, five appendices, deterministic figures, numerical regression tables, the native PhaseNav construction, and a full claim ledger.

Its strongest result is conditional: once a canonical, regular, equal-gain zeta-state map satisfying the stated zero-equivalence and covariance requirements is constructed, the critical-line conclusion follows. That canonical bridge remains open.

## Native PhaseNav Construction v0.1

The first executable bridge construction is now defined natively in
`construction/phasenav/secret_of_half_theta_bridge.pnv`.

It maps the symmetric theta-Mellin representation of the completed zeta function
to 18 complementary rotor pairs, giving a 36-dimensional PhaseNav state. The
construction proves exactly that its normalized self-dual closure defect is

\[
\mathcal C(s)=\left(\operatorname{Re}(s)-\frac12\right)^2.
\]

The finite detector approximates \(\xi(s)\), while the continuous detector is the
classical theta-Mellin identity. The remaining open statement is explicit:
every non-trivial zero must be shown to close in the canonical self-dual
PhaseNav shell. This is `SOH-C004`; it is not marked as proved.

The Python implementation parses and executes the `.pnv` source. It is an
auditor of the native program, not the source of the construction.

## Native PhaseNav–Weil Positivity Probe v0.1

The second native PhaseNav construction is defined in
`construction/phasenav/secret_of_half_weil_operator.pnv`.

It builds a two-channel, involution-coupled finite Hermitian witness in centred
coordinates \(z=s-1/2\). For an involution-fixed finite zero fixture the matrix
reduces exactly to a positive-semidefinite Gram matrix. Under the declared
Gaussian profile, replacing the first on-axis conjugate pair by a synthetic
off-axis quartet produces a stable negative eigenvalue.

The deterministic receipt is:

```text
on-axis control lambda_min:        +1.304512053935e-13
synthetic off-axis lambda_min:     -1.989005564501e-03
```

This establishes falsification sensitivity of the finite probe. It does not
establish positivity of the complete arithmetic Weil form and does not prove
the Riemann Hypothesis. The new open promotion target is `SOH-C005`.

## Author

Adrian Lipa
