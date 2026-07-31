# DHSE-001 — Stage B preregistration

## Status before execution

- Branch: `experiment/dhse-001` only.
- Stage: preregistered centre-blind operator-family scan.
- No Stage B result is recorded in this document.
- No merge, monograph inclusion or claim promotion is authorized.

## Scientific question

Does the projective state corresponding to `p=1/2`, namely odds `q=1`,
receive reproducibly exceptional trajectory occupancy under several exact
rational operator families that were **not** constructed by reciprocal
conjugacy?

The experiment does not order IEEE `NaN` with zero. IEEE `NaN` remains outside
the mathematical state space.

## Frozen deterministic parameters

- base seed: `secret-of-a-half:DHSE-001`;
- ensemble size: `64` domain-separated seeds;
- trajectory length: `384` transformations per seed;
- burn-in: first `64` states discarded;
- arithmetic: exact `fractions.Fraction` only;
- branch source: the existing SHA-256 counter stream from Stage A;
- projective residual:

  `d_q(z) = |z-q|/(z+q)`;

- occupancy radius: `1/10`;
- scanned odds centres:

  `1/16, 1/8, 1/4, 1/2, 1, 2, 4, 8, 16`;

- target centre: `q=1`, equivalent to `p=1/2`.

Every centre is evaluated by exactly the same code path. The centre scan is
completed before the target statistic is extracted.

## Frozen operator families

Every map has Möbius form `(a*z+b)/(c*z+d)`.

### Calibration family

This family reproduces Stage A reciprocal conjugacy and is excluded from the
primary robust-effect count.

- `reciprocal_calibration`:
  - `L = [1,0,1,1]`;
  - `R = [1,1,0,1]`.

### Experimental families

These four families must fail exact reciprocal branch conjugacy on the declared
sample audit before their results are admitted.

- `affine_skew`:
  - `L = [2,1,0,3]`;
  - `R = [3,2,0,2]`.
- `mobius_skew`:
  - `L = [1,1,2,3]`;
  - `R = [3,1,1,2]`.
- `scale_translate`:
  - `L = [2,0,0,1]`;
  - `R = [1,3,0,1]`.
- `collatz_stream`:
  - `L = [1,0,0,2]`;
  - `R = [3,1,0,2]`.

The Collatz-derived family uses the deterministic branch stream rather than
parity selection. It is therefore a controlled operator-family probe, not the
ordinary integer Collatz map.

## Frozen primary statistic

For each family and centre, compute the fraction of post-burn-in states whose
projective residual is at most `1/10`.

A family passes only when:

1. target occupancy at `q=1` is strictly greater than occupancy at every one of
   the eight control centres; and
2. target occupancy is at least `5/4` of the median control occupancy.

When the median control occupancy is exactly zero, condition 2 is treated as an
infinite ratio and passes only if target occupancy is strictly positive.

The target rank, crossing rate and median nearest residual are recorded as
secondary diagnostics and cannot alter the primary decision.

## Frozen conclusion rule

- `ROBUST_HALF_EFFECT`: at least 3 of 4 experimental families pass;
- `FAMILY_DEPENDENT`: 1 or 2 experimental families pass;
- `NO_ROBUST_HALF_EFFECT`: no experimental family passes.

The calibration family is reported but never counted toward this rule.

## Technical PASS gates

- deterministic byte-identical receipt regeneration;
- exact rational arithmetic throughout;
- declared state and transition counts for every family;
- all four experimental families fail the complete reciprocal-conjugacy sample
  audit;
- no IEEE `NaN` enters the state space or arithmetic.

## Interpretation boundary

Even `ROBUST_HALF_EFFECT` would establish only a reproducible property of this
declared projective trajectory ensemble. It would not prove that IEEE `NaN` is
a numeric endpoint, that `1/2` is ordered between `NaN` and zero, or that any
Riemann-hypothesis bridge is closed.
