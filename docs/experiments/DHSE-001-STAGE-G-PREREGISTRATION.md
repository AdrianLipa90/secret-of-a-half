# DHSE-001 — Stage G preregistration

## Status before execution

- Branch: `experiment/dhse-001` only.
- Stage: exact coefficient-scale persistence audit.
- This document contains no Stage G forcing result.
- No merge, monograph inclusion or claim promotion is authorized.

## Scientific question

Does the centre-blind excess at the self-dual odds coordinate `q=1` persist
when the bounded integer coefficient universe is expanded, or is Stage F mainly
a small-cube boundary effect?

## Frozen scale sequence

For each coefficient maximum

```text
K in {1,2,3,4,5,6}
```

construct the complete map universe

```text
M_K(z) = (a*z+b)/(c*z+d)
a,d in {1,...,K}
b,c in {0,...,K}
ad-bc > 0.
```

The expected exact map counts, determined solely by the frozen enumeration
rule, are:

| K | maps | ordered pairs | pair-word events |
|---:|---:|---:|---:|
| 1 | 3 | 9 | 36 |
| 2 | 25 | 625 | 2,500 |
| 3 | 96 | 9,216 | 36,864 |
| 4 | 256 | 65,536 | 262,144 |
| 5 | 563 | 316,969 | 1,267,876 |
| 6 | 1,073 | 1,151,329 | 4,605,316 |

Every universe is exhaustively enumerated. No sampling is permitted.

## Frozen words, centres and predicate

At every scale use exactly:

- words: `LL, LR, RL, RR`, applied left to right;
- centres: `1/16, 1/8, 1/4, 1/2, 1, 2, 4, 8, 16`;
- projective residual: `d_q(z)=|z-q|/(z+q)`;
- radius: `1/10`;
- exact whole-positive-line forcing predicate from Stage F.

All centres are evaluated by the same code path before the `q=1` statistic is
extracted.

## Frozen per-scale statistics

For every `K` and centre record:

1. exact universal forcing count;
2. forcing rate = count / pair-word event count;
3. centre rank by forcing count;
4. word-separated counts;
5. exact reciprocal-centre equality audit.

For each `K`, compute the exact ratio

```text
forcing_count(q=1) / median(forcing_count(eight controls)).
```

Because all centres at a fixed `K` share the same denominator, the count ratio
is also the forcing-rate ratio.

## Frozen primary persistence rule

Stage G returns `SCALE_PERSISTENT_HALF_EXCESS` only if all conditions hold:

1. `q=1` is strictly first at every non-degenerate scale `K=2,...,6`;
2. the target-to-control-median ratio is at least `5/4` at every scale
   `K=3,...,6`;
3. the normalized target forcing rate at `K=6` is at least one half of its
   Stage F value at `K=4`.

The third condition is the frozen anti-collapse gate:

```text
rate_6(q=1) >= (1/2) * rate_4(q=1).
```

Alternative conclusions are frozen as:

- `FINITE_CUBE_DECAY`: conditions 1 and 2 pass, but the anti-collapse gate
  fails;
- `SCALE_UNSTABLE`: condition 1 or 2 fails;
- `NO_HALF_FORCING_AT_SCALE`: the target count becomes zero at any `K>=2`.

`K=1` is reported as a degenerate calibration and does not enter the primary
persistence decision.

## Frozen symmetry and technical gates

Technical PASS requires at every scale:

- exact expected map, pair and event counts;
- reciprocal-conjugation closure of the map universe;
- exact equality of forcing counts for reciprocal centre pairs;
- deterministic byte-identical receipt regeneration;
- integer/rational arithmetic only in all forcing decisions.

## Secondary diagnostics

Without altering the primary decision, report:

- exact target forcing rates at all scales;
- ratios between successive target rates;
- word contributions to the target count;
- the scale at which each non-target centre first receives a forcing event;
- a descriptive trend label, with no extrapolation beyond `K=6`.

## Interpretation boundary

A positive Stage G result would show persistence across six declared bounded
coefficient universes, not over all Möbius maps or all deterministic dynamics.
It would not make IEEE `NaN` a mathematical endpoint, would not establish the
ordering `NaN -> 1/2 -> 0`, and would not close an RH bridge.
