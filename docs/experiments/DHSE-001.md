# DHSE-001 — Deterministic Halfway Seed Experiment

## Status

- Branch-only experiment.
- Stage A: deterministic calibration.
- Not part of the monograph.
- No merge or claim promotion is authorized.

## Question

Does the existing abstract duality between `DEFINED_ZERO` and
`UNDEFINED_BOTTOM` support a reproducible trajectory-level distinction of the
self-dual state, without allowing IEEE `NaN` to enter arithmetic?

This stage does **not** test whether IEEE `NaN` is numerically ordered with zero.
It is excluded from the state space and may only serve as an implementation
marker for the abstract undefined label.

## Exact state

A state is a positive rational projective odds coordinate

\[
z=\frac{p}{1-p}, \qquad p\in(0,1).
\]

The endpoint labels are recovered as limits: `DEFINED_ZERO` at \(p=0\) and
`UNDEFINED_BOTTOM` at \(p=1\). Reciprocal duality is

\[
J(z)=\frac1z,
\]

which induces \(p\mapsto1-p\). Its unique fixed point is \(z=1\), equivalently
\(p=1/2\).

## Deterministic seed

The literal seed is `secret-of-a-half:DHSE-001`. SHA-256 is used only as a
platform-independent deterministic expander:

1. one domain-separated digest creates the initial positive rational \(z_0\);
2. a counter-mode domain-separated digest creates an infinite `L/R` branch
   stream.

There is no randomness, clock input, machine identifier or floating-point
state.

## Operator pair

\[
L(z)=\frac{z}{1+z}, \qquad R(z)=z+1.
\]

The pair is exactly conjugated by reciprocal duality:

\[
J\circ L=R\circ J, \qquad J\circ R=L\circ J.
\]

The primary trajectory uses the seed branch stream. The dual trajectory starts
at \(J(z_0)\) and complements every branch. The negative control starts at
\(J(z_0)\) but reuses the original branches.

## PASS/FAIL gates

Technical PASS requires:

- byte-for-byte deterministic seed expansion;
- exact rational arithmetic throughout;
- exact reciprocal correspondence at every primary/dual step;
- negative control failure for at least one state;
- explicit exclusion of IEEE `NaN` from arithmetic.

Scientific status remains `CALIBRATION_ONLY` even on technical PASS. The
operator family was selected to obey reciprocal conjugacy, so it structurally
distinguishes \(z=1\). This is not independent evidence for an ordering
`NaN -> 1/2 -> 0`.

## Next falsification stage

Stage B must compare operator families not constructed from reciprocal
conjugacy and must preregister the statistic before execution. Candidate
families include exact affine, modular and Collatz-derived controls. A robust
halfway effect would need to survive representation changes and negative
controls.
