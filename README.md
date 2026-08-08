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

The programme separates:

- exact lemmas that can already be proved;
- conditional theorems whose hypotheses are explicit;
- numerical or symbolic experiments;
- executable PhaseNav/NOEMA dependency state;
- the unresolved bridge required to connect every non-trivial zeta zero to the proposed information-spinor cancellation mechanism.

The central open task is to construct a canonical map or operator for which vanishing is equivalent to a non-trivial zero of the completed zeta function while preserving the required symmetry, positivity and spectral structure.

The current canonical dependency integration is **v0.7**. It introduces a typed PhaseNav routing/provenance boundary without changing the proof status of the mathematical programme. In particular, `SOH-C004` and `SOH-C005` remain OPEN.

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
│   ├── construction/
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
- Change history and corrective receipts are append-only where historical provenance is involved.
- External software projects become executable dependencies only through explicit, versioned contracts with exact commit provenance.
- The mathematical claim ledger remains autonomous: a PhaseNav route, NOEMA memory record, TIR phenomenological relation, or finite numerical sample cannot promote an open mathematical claim.
- Intrinsic scientific state must not be identified with its transport representation.

## Historical monograph baseline: Version 0.2

Version 0.2 was the validated 92-page baseline: 16 chapters, five appendices, deterministic figures, numerical regression tables, the native PhaseNav construction, and a full claim ledger. The 92-page count is historical provenance, not a permanent build invariant.

Its strongest result was conditional: once a canonical, regular, equal-gain zeta-state map satisfying the stated zero-equivalence and covariance requirements is constructed, the critical-line conclusion follows. That canonical bridge remains open.

## Current monograph: Version 0.7

The modular LaTeX monograph in `monograph/` now includes Chapter 21, **Canonical PhaseNav Dependencies and the Proof Firewall**. CI compiles the current PDF and publishes `secret-of-a-half-monograph-v0.7`; the current page count is recorded by the build rather than hard-coded as a scientific gate.

Version 0.7 binds the repository to:

- PhaseNav hard canon `1.2.0` / dependency layer `0.7.0`, commit `54f65f2ca7d35cdd98f0ab8984cc1a8d74444a96`;
- NOEMA dependency/provenance contract, commit `42a0a8916e81ca27f2213bf0f28538f046c2e89a`.

The recovered TIR coefficient state `(h,a,b,c)` remains intrinsically 4D, while PhaseNav uses a separate 36D routing envelope. Vectorization is transport and routing; it is not scientific promotion.

The v0.7 assignment ledger distinguishes:

- `ROLE_ROUTER_HABC = STRUCTURAL_ROLE_ROUTING_PASS`;
- `ORBIT_DIRECTION = IMPLEMENTED_PROJECT_ORBITAL_RULE`;
- `RELATIONAL_GRADIENT = IMPLEMENTED_SOURCE_OPERATOR_CANDIDATE_TIR_BINDING`;
- `TIR_SLOT_BINDING = OPEN`.

Measured masses, measured Yukawa couplings, and coefficient-enriched routing vectors are forbidden as parents of the prospective assignment derivation.

## Native PhaseNav Construction v0.1

The first executable bridge construction is defined natively in
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
the Riemann Hypothesis. The open promotion target remains `SOH-C005`.

## Native PhaseNav–Weil Arithmetic Operator v0.2

The next construction is defined in
`construction/phasenav/secret_of_half_weil_arithmetic.pnv`.

It evaluates the localized two-channel Weil matrix from prime powers, the
archimedean gamma factor, conductor and pole terms. The arithmetic sum does not
consume a zero list. Its deterministic result matches the earlier low-height
spectral receipt within the declared numerical tolerance:

```text
arithmetic lambda_min:        +1.30e-13
arithmetic lambda_max:        +2.00e+00
prime-cutoff stability:       PASS
spectral normalization check: PASS
```

This closes the first executable prime-to-phase-to-spectrum audit loop. It is
one positive localized sample, not a proof of dense Weil positivity; `SOH-C005`
remains open.

## v0.7 receipt hygiene

The v0.7 validation also recovered three historical technical debts without rewriting their original evidence:

- Stage B: an old full-receipt SHA mismatch is recorded append-only while the compact scientific/technical projection remains reproducible;
- Stage I: legacy unreduced rational pairs are compared after exact canonical rational reduction, with the historical JSON retained unchanged;
- Stage M: the reciprocal-interval test fixture was corrected so lower endpoints map to reciprocal upper endpoints; the operator itself was not changed.

The repair ledger is `data/processed/DHSE_001_RECEIPT_REPAIR_V0_7.json`. These corrections do not promote any scientific claim.

## Author

Adrian Lipa
