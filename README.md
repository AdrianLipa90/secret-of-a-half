# Secret of a Half

**Secret of a Half** is an independent research repository devoted to a precise mathematical investigation of why

\[
\operatorname{Re}(s)=\frac12
\]

is the distinguished symmetry axis in the analytic structure surrounding the Riemann zeta function.

The programme links binary complementarity, exact two-channel cancellation, spinorial phase closure, the zeta involution, PhaseNav theta states, Weil positivity, Hermite dense-core analysis, reciprocal self-duality, and explicit prime-tail control.

## Research status

This repository develops a **structural ansatz and executable research programme**, not a claimed proof of the Riemann Hypothesis.

Exact lemmas, conditional theorems, numerical certificates, falsification witnesses, and exploratory interpretations are kept visibly separate. The central open task remains construction of a complete arithmetic operator whose positivity and null structure canonically force every non-trivial completed-zeta zero into the self-dual half-axis state.

## Initial mathematical core

For

\[
|\psi\rangle=\sqrt{\sigma}\,|0\rangle+e^{i\phi}\sqrt{1-\sigma}\,|1\rangle,
\]

exact equal-gain cancellation occurs only at

\[
\sigma=\frac12,
\qquad
\phi\equiv\pi\pmod{2\pi}.
\]

Binary Shannon entropy is also uniquely maximal at \(\sigma=1/2\), where it equals \(\ln2\). These facts identify the half as the balanced binary state, but do not by themselves constrain all zeta zeros.

## Working principles

- No claim is promoted without a written proof or reproducible construction.
- Exact, conditional, numerical, and exploratory layers remain separate.
- Change history is append-only.
- Python executors audit native `.pnv` constructions; they are not declared as the source of those constructions.
- No arithmetic receipt consumes a list of zeta zeros unless explicitly marked as a validation-only fixture.
- The project remains autonomous and does not claim RH before the complete bridge is closed.

## Monograph Version 0.5

The modular LaTeX monograph in `monograph/` now contains 19 chapters and five appendices. GitHub Actions rebuilds the validated **103-page A4 PDF** and publishes it as the `secret-of-a-half-monograph-v0.5` artifact.

The newest chapters are:

- Chapter 17 — PhaseNav–Weil Hermite dense-core ladder;
- Chapter 18 — zero–undefined reciprocal self-duality;
- Chapter 19 — reciprocal compactification and the prime-tail certificate.

## Native PhaseNav theta construction v0.1

`construction/phasenav/secret_of_half_theta_bridge.pnv` maps the symmetric theta–Mellin representation to 18 complementary rotor pairs in 36 dimensions. Its exact normalized closure defect is

\[
\mathcal C(s)=\left(\operatorname{Re}(s)-\frac12\right)^2.
\]

The continuous detector equals the classical completed-zeta theta–Mellin expression. The statement that every non-trivial zero closes in the canonical self-dual shell remains open as `SOH-C004`.

## PhaseNav–Weil programme

### Finite positivity probe v0.1

The two-channel finite witness is PSD for an involution-fixed on-axis fixture and develops a stable negative eigenvalue for a declared synthetic off-axis quartet. This establishes falsification sensitivity, not global positivity.

### Prime-side arithmetic operator v0.2

The explicit-formula calculation uses pole, conductor, archimedean gamma, and prime-power terms without consuming a zero list. It closes the first executable primes-to-phase-to-spectrum audit loop.

### Hermite dense-core ladder v0.3

Translated-scaled Hermite channels give an explicit Schwartz dense core. Principal arithmetic matrices through basis size six are cutoff-audited and PSD-tested, while an off-axis validation fixture retains a negative mode.

### Zero–undefined reciprocal duality v0.4

Binary complement is conjugate to reciprocal inversion in projective odds coordinates. The unique positive reciprocal fixed point, the positive swap-fixed spinor, the Fisher–Rao midpoint, and the entropy maximum all occur at \(p=1/2\). `UNDEFINED_BOTTOM` is an abstract label; IEEE `NaN` never enters arithmetic.

### Prime-tail certificate v0.5

The omitted prime-power tail is controlled analytically. With

\[
u=\log x,
\qquad
z_{\rm t}=\frac1u,
\]

the logarithmic half-line is compactified to a finite interval with a flat endpoint. The tail majorant has a closed upper-incomplete-gamma form.

For the declared profile \(w=0.8\), \(Q=100000\), and \(N\le6\),

\[
\|E_N(Q)\|_2\le7.717202888999335\times10^{-13}.
\]

This closes controlled cutoff removal for every fixed declared finite section. A useful bound uniform as the basis size tends to infinity, global positivity, and the null-space implication to native closure remain open.

## Repository layout

```text
secret-of-a-half/
├── construction/phasenav/   # authoritative native programmes
├── claims/                   # Markdown and structured claim ledgers
├── data/processed/           # deterministic receipts
├── docs/construction/        # mathematical derivations
├── logs/                     # append-only process records
├── monograph/                # modular LaTeX monograph
├── scripts/                  # receipt generators
├── src/secret_of_a_half/     # parsers and auditors
└── tests/                    # regression and boundary tests
```

## Author

Adrian Lipa
