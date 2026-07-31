# DHSE-001 — Stage F preregistration

## Status before execution

- Branch: `experiment/dhse-001` only.
- Stage: exact centre-blind coefficient-cube census.
- This document contains no Stage F result.
- No merge, monograph inclusion or claim promotion is authorized.

## Scientific question

Is the self-dual odds coordinate `q=1` exceptionally frequent as a whole-line
forcing centre in a finite operator universe that was defined independently of
the successful Stage C Möbius pair?

The scan treats all declared centres identically. IEEE `NaN` remains outside
the mathematical state space.

## Frozen operator universe

Every branch is an increasing positive Möbius map

```text
M(z) = (a*z+b)/(c*z+d)
```

with integer coefficients constrained by

```text
a,d in {1,2,3,4}
b,c in {0,1,2,3,4}
ad-bc > 0
```

No distance from any earlier operator is used. The complete admissible set
contains `256` maps and therefore `65,536` ordered branch pairs `(L,R)`.
No sampling is permitted.

For every ordered pair, all four two-letter words are composed left to right:

```text
LL, LR, RL, RR
```

The full census therefore contains `262,144` pair-word events.

## Frozen centres and metric

The nine odds centres are

```text
1/16, 1/8, 1/4, 1/2, 1, 2, 4, 8, 16
```

with the same projective residual used in Stage B:

```text
d_q(z) = |z-q|/(z+q).
```

The unchanged radius is `1/10`, so the target interval associated with centre
`q` is exactly

```text
[9q/11, 11q/9].
```

Every centre is processed by the same code path before `q=1` is inspected.

## Exact whole-line forcing predicate

For a positive orientation-preserving composition

```text
W(z) = (A*z+B)/(C*z+D),
```

its image of the positive line is the open interval between the exact endpoint
limits `B/D` and `A/C`, with `A/C=+infinity` when `C=0`.

A pair-word event forces centre `q` iff the closure of this image interval is
contained in `[9q/11, 11q/9]`. The decision uses integer and rational
arithmetic only; no grid sampling or floating-point approximation is allowed.

## Frozen primary statistic

For every centre, count the number of the `262,144` pair-word events that
universally force its radius ball.

The self-dual centre passes the Stage F exceptional-frequency gate only if:

1. `q=1` has a strictly greater forcing count than each of the eight controls;
2. its count is at least `5/4` of the median control count.

Conclusion labels are frozen as:

- `CENTRE_BLIND_HALF_EXCESS`: both conditions pass;
- `CENTRE_TIED_OR_MODEST`: at least one forcing event exists at `q=1`, but the
  exceptional-frequency gate fails;
- `NO_HALF_FORCING`: no forcing event exists at `q=1`.

## Frozen symmetry audit

Because reciprocal conjugation maps matrix coefficients
`[a,b,c,d] -> [d,c,b,a]`, the declared map universe is expected to be closed
under this operation. The receipt must verify:

- every reciprocal-conjugate map remains in the universe;
- forcing counts at reciprocal centre pairs are identical:
  `1/16 <-> 16`, `1/8 <-> 8`, `1/4 <-> 4`, `1/2 <-> 2`.

A failure of either audit is a technical FAIL.

## Secondary diagnostics

The receipt will also record, without altering the primary decision:

- forcing counts separated by word `LL/LR/RL/RR`;
- number of distinct branch pairs contributing to each centre;
- exact rank of every centre;
- examples of forcing compositions selected by deterministic lexicographic
  order.

## Technical PASS gates

- exhaustive enumeration of exactly `256` maps;
- exhaustive enumeration of exactly `65,536` ordered branch pairs;
- exactly `262,144` two-letter pair-word events;
- exact rational endpoint decisions;
- reciprocal-universe closure;
- reciprocal-centre count equality;
- byte-identical deterministic receipt regeneration.

## Interpretation boundary

Even a positive Stage F result would concern this declared bounded integer
coefficient universe and the frozen projective radius. It would not establish
an operator-independent law over all deterministic dynamics, would not order
IEEE `NaN` with zero, and would not close any Riemann-hypothesis bridge.
