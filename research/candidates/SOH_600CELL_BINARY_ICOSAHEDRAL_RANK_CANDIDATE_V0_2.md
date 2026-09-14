# SOH 600-cell / Binary-Icosahedral Rank Candidate v0.2

Status: `CANDIDATE / ACTIVE_WORKING_DEPENDENCY / RIEMANN_CLAIMS_UNCHANGED`

Date: 2026-09-11

The 600-cell candidate provides an active finite `S^3` carrier whose 120 unit vertices are the natural binary-icosahedral / spin-lift research surface. This candidate may be used in SOH spinorial, half-orbit, phase and representation experiments.

Validated finite-rank inputs:

```text
ell=0..5 : sampled ranks 1,4,9,16,25,36 (full continuum dimensions)
ell=6    : 49 continuum directions -> 25 sampled directions
ell=7    : sampled rank 40; contributes 4 new directions beyond ell<=6
H_0+...+H_7 sampled cumulative rank = 120
```

The GREMLIN working route lowers the relations

```text
DOUBLE_COVER_LIFT_OF
EXACT_KERNEL_ISOMORPHISM
COORDINATE_ISOMORPHIC_TO
```

to the already admitted `COMPOSITION` primitive. No new PNV opcode is introduced.

Candidate use is allowed for:

- finite spin-lift / `SU(2)` representation experiments;
- binary-icosahedral phase and half-orbit diagnostics;
- comparisons between lower `S^3` harmonic sectors and finite 600-cell representations;
- downstream candidate-only GREMLIN relational compilation.

This surface does not promote a Riemann-hypothesis proof, repair a historical SOH no-go result, or identify the rank-collapse boundary with a physical horizon. Those require independent evidence and promotion gates.
