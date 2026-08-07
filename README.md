# Secret of a Half

**Secret of a Half** is an independent mathematical research repository devoted to the distinguished axis

\[
\operatorname{Re}(s)=\frac12
\]

in the analytic structure surrounding the Riemann zeta function.

**Current research branch:** `agent/sigma-identity-holonomy-v0.7`  
**Monograph:** *The Secret of a Half*, v0.7 — 7 August 2026  
**Research status:** exact and conditional mathematics plus explicitly separated numerical/model layers; **no proof of the Riemann Hypothesis is claimed**.

## Current mathematical core

For the normalized complementary amplitude

\[
\mathcal A(\sigma,\phi)
=\sqrt{\sigma}+e^{i\phi}\sqrt{1-\sigma},
\qquad 0<\sigma<1,
\]

exact equal-gain cancellation occurs iff

\[
\sigma=\frac12,
\qquad
\phi\equiv\pi\pmod{2\pi}.
\]

Independently,

\[
H_2(\sigma)
=-\sigma\ln\sigma-(1-\sigma)\ln(1-\sigma)
\]

has its unique maximum at `sigma=1/2`, with value `ln(2)`, while

\[
\mathcal J(s)=1-\overline{s}
\]

has fixed set `Re(s)=1/2`. In the declared binary qubit representation the same point is the Bloch equator and an equatorial loop carries Berry holonomy `-1`.

These are exact/standard results in their stated domains. They do **not** by themselves imply that every non-trivial zeta zero belongs to the required binary/native state representation.

## v0.7: Sigma as an identity axis

Version 0.7 centers the binary coordinate at

\[
\Sigma_\star=\frac12,
\qquad
x=\sigma-\frac12.
\]

Complement becomes the geometric orientation reversal

\[
x\mapsto-x.
\]

This gives a concrete computational meaning to signed centered coordinates:

- negative = orientation on one side of the selected axis;
- zero = vanishing displacement / fixed axis;
- positive = the opposite orientation.

The broader statement that a system's `Sigma` is an evolving invariant defining its persistent self is a TIR/PhaseNav modelling principle. The binary fixed-axis result above is exact; the universal physical interpretation is not promoted to theorem status.

## Recurrence before radians

A projective cycle is represented first by

\[
q\in\mathbb R/\mathbb Z,
\qquad
f_q=\frac{\Delta N}{\Delta t},
\]

where frequency is winding count per elapsed parameter. Only afterwards is an angular representation chosen:

\[
\phi=Cq.
\]

For radians, `C=2*pi`. Spin-1/2 supplies the projective/spinor double-cover relation before the conventional `2*pi/4*pi` notation is introduced.

The TIR/Metatime information-cycle assignment remains explicitly model-level:

\[
\frac{dI}{dq}=\frac{\ln2}{12}.
\]

Given that assignment,

\[
\frac{dI}{d\phi}=\frac{\ln2}{12C},
\]

and at `C=2*pi`

\[
\kappa=\frac{\ln2}{24\pi}.
\]

The arithmetic identity

\[
24=8\cdot3=12\cdot2=6\cdot4
\]

is exact. Assigning those factors to mixing sectors/flavours, projective cycles, or spinor cycles is model semantics and is not counted as three independent physical derivations.

## Typed identity/holonomy solver

The v0.7 solver is implemented in:

```text
src/secret_of_a_half/identity_holonomy_solver.py
scripts/run_identity_holonomy_solver.py
```

It uses four rule statuses:

```text
EXACT
STANDARD
MODEL
OPEN
```

and typed relations such as fixed point, dual, implication, representation, and holonomic edges. Rules may have multiple premises.

Default closure admits only `EXACT` and `STANDARD`. Explicit model closure additionally admits `MODEL`. `OPEN` is never auto-promoted.

Four independent numerical/symbolic routes are cross-checked:

```text
complement fixed point        -> sigma = 1/2
binary-entropy stationarity   -> sigma = 1/2
equal-gain cancellation       -> sigma = 1/2
Berry -1 holonomy residual    -> sigma = 1/2
```

The executable receipt is written to:

```text
data/processed/identity_holonomy_solver_receipt.json
```

The receipt must retain:

```text
half_axis_consensus = true
riemann_hypothesis_derived = false
canonical_zero_state = OPEN
```

The missing bridge is the canonical zero-state/native-closure implication `SOH-C004`.

## Geometry-first CIEL/PhaseNav dependencies

The companion `noema-phasenav-core` branch `canon/sigma-identity-cycle-v1` contains the low-level package:

```text
ciel_geometry.phasenav.dependencies
```

with dependency direction:

```text
identity axes / centered coordinates
        -> normalized cycles and winding
        -> phase crystal (R/Z)^N
        -> typed relations + optional normalized holonomy
        -> tangent/log-map vectorization
        -> higher PhaseNav operators
```

On the phase crystal, vector signs arise from shortest oriented tangent displacement and zero from vanishing displacement. Opaque stable IDs may still provide deterministic computational embeddings, but generated proximity is not semantic evidence by itself.

Holonomy is attached only to eligible paths with a declared connection/transport law. A semantic pair does not automatically receive a phase.

The native v0.7 declaration is:

```text
construction/phasenav/secret_of_half_identity_holonomy_v0_7.pnv
```

## Native PhaseNav theta bridge

The original native bridge remains:

```text
construction/phasenav/secret_of_half_theta_bridge.pnv
```

It maps the symmetric theta-Mellin representation to complementary PhaseNav rotor pairs and proves for the declared native state that the normalized self-dual closure defect is

\[
\mathcal C(s)=\left(\operatorname{Re}(s)-\frac12\right)^2.
\]

The continuous detector is the classical theta-Mellin representation of `xi(s)`. The open statement is still that every non-trivial zero must be forced into the canonical self-dual PhaseNav shell. That is `SOH-C004` and remains **OPEN**.

## PhaseNav–Weil programme

Existing PhaseNav–Weil, Hermite, reciprocal-duality, prime-tail and adaptive-cutoff constructions remain intact. Their finite-section receipts retain their original claim status. Version 0.7 does not reinterpret finite PSD checks as a proof of dense Weil positivity.

Likewise, **DHSE-001 remains separate**. v0.7 does not modify its sources, receipts, thresholds, branch policy, or promotion rules.

## TIR cross-reference boundary

The parent TIR programme is cross-referenced for:

- `kappa = ln(2)/(24*pi)` and its claim boundary;
- Poincare/phase geometry;
- flavour/mixing architecture;
- broader holonomic relation semantics;
- the model-level split `information arithmetic -> energy/matter` and `phase geometry -> time/space`.

The derivation of physical `t` from `tau` is explicitly deferred. The broader TIR object `W_[ij]` is referenced only; its dynamics are not imported into the Secret-of-a-Half proof chain.

## Monograph v0.7

The monograph source is modular LaTeX under `monograph/`. The v0.7 branch adds three chapters:

```text
21_identity_axis_and_normalized_recurrence.tex
22_holonomic_relation_graph_and_geometry_dependencies.tex
23_typed_solver_and_tir_crosswalk.tex
```

and three deterministic generated figures. The local verified build is over 100 pages; CI enforces a floor of 125 pages together with no unresolved references/citations, no overfull boxes, and no Type 3 fonts in the compiled PDF.

## Reproduce v0.7

```bash
python -m pip install -e . pytest numpy matplotlib mpmath
python -m pytest tests/test_identity_holonomy_solver.py -q
python scripts/run_identity_holonomy_solver.py
python scripts/generate_monograph_assets.py
python scripts/generate_identity_holonomy_assets.py
python -m pytest -q

cd monograph
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

## Claim discipline

The authoritative claim ledger is `claims/CLAIM_LEDGER.md`. Current v0.7 additions include:

- `SOH-L022`: normalized recurrence / winding frequency;
- `SOH-L023`: four-route half-axis cross-check;
- `SOH-L024`: exact integer cross-factorization of 24;
- `SOH-C006`: twelve-cycle information assignment — MODEL;
- `SOH-T005`: conditional `kappa` reconstruction;
- `SOH-L025`: typed solver firewall;
- `SOH-H002`: geometry-first sign/zero implementation model;
- `SOH-L026`: normalized-turn holonomy composition.

No claim may be promoted from OPEN/MODEL to exact without an explicit proof or reproducible construction whose dependencies are themselves established.

## Repository layout

```text
secret-of-a-half/
├── claims/
├── construction/phasenav/
├── data/processed/
├── docs/
├── monograph/
│   ├── chapters/
│   └── figures/
├── references/
├── scripts/
├── src/secret_of_a_half/
└── tests/
```

## Author

Adrian Lipa
