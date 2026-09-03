# The Secret of a Half — Publication Audit v0.11

Date: 2026-09-03

Source main audited: `b82c33132f6fd9d578f9fc34fc877d3f716a066f`

Publication branch: `publication/soh-v0.11-orbit-fourier-frontier`

## Verdict

The v0.10 PDF was build-clean but mathematically stale relative to the source tree. The primary publication blocker was the mismatch between the monograph's live G024 narrative and the reviewed SOH-G024-T theorem already present on `main`.

## Blocker A — stale complete-monotonicity frontier

v0.10 described the next G024 programme as proving the third and all higher signed derivatives of `H_y`, with full complete monotonicity retained as an open sufficient route.

Current source contains the reviewed theorem-level claim SOH-G024-T:

- for every fixed `0<|y|<1/2`, `H_y(q)=D_y(sqrt(q))` decays faster than every exponential in `q`;
- every nonzero completely monotone function with finite value at zero has a positive exponential lower envelope by Hausdorff–Bernstein–Widder;
- therefore `H_y` is **not** completely monotone;
- the already proved signs `H_y'<0` and `H_y''>0` remain valid;
- at least one signed derivative inequality fails at some order `m>=3`;
- the direct external Fourier/Wronskian criterion remains open and RH-equivalent.

Publication action: add Chapter 56 and rewrite frontmatter, current-status synthesis, ledger, and final synthesis so the all-order complete-monotonicity route is recorded as `CLOSED ROUTE / NO-GO`.

## Blocker B — reciprocal map ambiguity

The functional-equation map and Li/Euler negative inversion must not be conflated:

- functional reflection: `s -> 1-s` gives `u -> 1/u`;
- Euler/Li negative inversion: `u -> -1/u`.

The latter is excluded as a global zero-to-zero spectral mechanism by the existing G014–G018 line. This does not affect the former, which is an exact symmetry of the transformed xi zero set.

Publication action: Chapter 57 gives the exact reciprocal–conjugation theorem

`1/u = conjugate(u)  <=>  |u|=1  <=>  Re(s)=1/2`

and the orbit-separating defect

`Delta_RC(u) = |1/u-conjugate(u)|^2 = (|u|-1/|u|)^2`.

For transformed xi zeros this gives the exact reformulation

`RH <=> for every u in Z_X, 1/u = conjugate(u)`.

The chapter explicitly leaves `X(u)=0 -> Delta_RC(u)=0` OPEN. No proof of RH is claimed.

## GREMLIN provenance

GREMLIN/OCTOPUS was used as a candidate-only audit layer. Its half-orbit closure scan independently flags the same failure mode: quotient/barycentric `1/2` does not distinguish an off-self-dual reciprocal two-cycle from a fixed layer. GREMLIN has no canon-promotion authority.

## Q28 provenance

The live Q28 backend was used only as computational support / validation. Runtime capacity reported 28 logical qubits (6 address + 22 workspace) in a numerical hybrid statevector backend. No physical-QPU claim is made. The publication proof status does not depend on Q28 output.

## Publication invariants added

1. Exactly 57 numbered chapters in v0.11.
2. Chapter 56 must expose SOH-G024-T and the closed complete-monotonicity route.
3. Chapter 57 must expose `1/u` versus conjugation and the zero-orbit defect.
4. `1/u` must remain separated from `-1/u`.
5. Canonical numbered status remains through SOH-G023.
6. G024 integration is not automatic canon promotion.
7. Direct external Fourier positivity remains OPEN / RH-equivalent.
8. RH remains OPEN.

## Publication target

The publication-ready PDF is to be accepted only after:

- full regression suite PASS;
- integration audit PASS;
- semantic audit PASS;
- LaTeX build PASS with no overfull boxes, undefined references, undefined citations, or multiply defined labels;
- visual PDF preflight PASS;
- artifact digest recorded.
