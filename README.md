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
- exact finite computer-assisted theorems with explicitly bounded domains;
- conditional theorems whose hypotheses are explicit;
- numerical or symbolic experiments;
- falsification witnesses and negative results;
- the unresolved bridge required to connect every non-trivial zeta zero to the proposed information-spinor cancellation mechanism.

The central open task is to construct a canonical map or operator for which vanishing is equivalent to a non-trivial zero of the completed zeta function while preserving the required symmetry, positivity and spectral structure.

## Mathematical core

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

## Reciprocal self-duality: exact boundary from DHSE-001 Stage M

The 0.6.1 review line adds an exact finite theorem that sharply separates
**self-duality** from **dynamical extremality**.

In projective odds

\[
q=\frac{p}{1-p},
\]

binary complement is conjugate to reciprocal inversion \(q\mapsto1/q\), and the
unique positive self-dual point is \(q=1\leftrightarrow p=1/2\).

DHSE-001 Stage M exhaustively classifies the forcing-count function \(N_n(q)\)
on all \(q>0\) for the complete primitive positive integer Möbius universe with
\(K=6\), projective radius \(1/10\), and binary word lengths \(n=1,2,3,4\).
The endpoint sweep is exact over reduced rational intervals and the fixed-width
NumPy backend is protected by a pre-run overflow certificate.

The exact maximizers are:

| Word length | \(N_n(1)\) | Global maximum | Exact maximizer set |
|---:|---:|---:|---|
| 1 | 24,752 | 39,984 | \([9/11,11/12]\cup[12/11,11/9]\) |
| 2 | 314,690 | 314,690 | \(\{1\}\) |
| 3 | 943,740 | 943,740 | \(\{1\}\) |
| 4 | 2,219,236 | 2,224,570 | \([9882/9911,341/342]\cup[342/341,9911/9882]\) |

Thus

\[
\boxed{
N_n(q)=N_n(1/q)
\;\not\Rightarrow\;
q=1\text{ is a global maximum}
}.
\]

This is recorded as `SOH-L022` (exact finite computer-assisted theorem) and
`SOH-D001` (exact finite counterexample).  It does not close `SOH-C004` or
`SOH-C005`; any future inference from self-duality to a preferred dynamical
state requires an additional condition such as positivity, convexity,
monotonicity, or a variational principle.

## TIR ↔ Secret-of-a-Half interface

The 7 August 2026 cross-review keeps the logical types of the bridge explicit:

\[
\boxed{
\frac12
\xrightarrow{\;H_2\;}
\ln2
\xrightarrow{\;\text{TIR definition}\;}
\kappa=\frac{\ln2}{24\pi}
\xrightarrow{\;\omega=2\pi f\;}
\Gamma_{\mathcal I}=\frac{\ln2}{12}f
}.
\]

The first arrow is exact information theory.  The TIR normalization is a model
postulate/structural definition.  The phase-rate identity is exact conditional
on that normalization and on `dI = κ dφ`.  The cross-relation is not used as a
circular proof of the TIR normalization and does not constitute a proof of the
Riemann Hypothesis.

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
│   ├── experiments/
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
- Exact results, finite exact results, conditional results, numerical evidence and interpretation remain visibly separated.
- Change history and provenance records are append-only.
- Historical receipts are not silently rewritten merely to satisfy a later serialization convention.
- Existing projects are not treated as dependencies unless an explicit interface is documented.
- This repository is autonomous: its definitions, assumptions and proofs must stand on their own.

## Current milestones

1. Binary-complementarity, entropy, cancellation and involution lemmas: **exact**.
2. Native paired theta construction and closure defect: **implemented with explicit open bridge**.
3. PhaseNav–Weil finite probes and Hermite ladder: **implemented; global positivity remains open**.
4. Prime-tail finite-section certification and adaptive cutoff theorem: **implemented with explicit scope**.
5. Zero/undefined reciprocal-duality geometry: **exact structural lemmas; physical interpretation exploratory**.
6. DHSE-001 Stage M forcing landscape: **exact finite classification on the declared universe**.
7. Canonical zeta-state / positivity bridge: **open**.
8. Riemann Hypothesis proof claim: **not made**.

## Monograph Version 0.6.1-review

The active review monograph is maintained as modular LaTeX in `monograph/` and is dated **7 August 2026**.  It retains the Version 0.6 adaptive-cutoff results and adds the Stage-M exact finite classification, the reciprocal-symmetry counterexample, synchronized claim ledgers, and the receipt-provenance audit.

The strongest global zeta conclusion remains conditional: once a canonical, regular zeta-state or Weil-positivity bridge satisfying the stated zero-equivalence and closure requirements is constructed, the corresponding critical-line theorem can be invoked.  That bridge remains open.

The authoritative build and validation sequence is maintained by the repository workflows rather than duplicated as a drifting command transcript in this README.

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
the Riemann Hypothesis. The open promotion target is `SOH-C005`.

## Native PhaseNav–Weil Arithmetic Operator v0.2

The arithmetic construction is defined in
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

## Author

Adrian Lipa
