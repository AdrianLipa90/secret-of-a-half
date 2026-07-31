# DHSE-001 — Stage H preregistration

## Status before execution

- Branch: `experiment/dhse-001` only.
- Stage: exact radius-robustness audit.
- This document contains no Stage H result.
- No merge, monograph inclusion or claim promotion is authorized.

## Scientific question

Does the scale-persistent excess at the self-dual odds coordinate `q=1`
survive substantial changes of the projective neighbourhood radius, or is it
specific to the Stage B–G value `1/10`?

## Frozen operator universe

Use the complete Stage G coefficient cube at the largest validated scale:

```text
K = 6
a,d in {1,...,6}
b,c in {0,...,6}
ad-bc > 0
```

This gives exactly:

- `1,073` admissible maps;
- `1,151,329` ordered branch pairs;
- words `LL, LR, RL, RR`;
- `4,605,316` pair-word events per radius.

No map or pair sampling is permitted.

## Frozen centres

Use the unchanged reciprocal odds centres:

```text
1/16, 1/8, 1/4, 1/2, 1, 2, 4, 8, 16.
```

Every centre is evaluated by the same code path before `q=1` is inspected.

## Frozen radii

Use the eight exact projective radii:

```text
1/40, 1/30, 1/20, 1/15, 1/10, 1/8, 1/6, 1/5.
```

For residual

```text
d_q(z)=|z-q|/(z+q),
```

the exact target interval at radius `r<1` is

```text
[q(1-r)/(1+r), q(1+r)/(1-r)].
```

No radius may be removed or added after execution.

## Frozen forcing predicate

For each pair-word composition

```text
W(z)=(A*z+B)/(C*z+D),
```

count a forcing event for `(q,r)` only when the closure of the image of the
entire positive line is contained in the exact target interval for centre `q`
and radius `r`.

All decisions use integer/rational endpoint inequalities only. No floating
point or grid sampling is allowed.

## Frozen per-radius statistic

For every radius and centre record:

1. exact forcing count;
2. forcing rate over `4,605,316` events;
3. centre rank;
4. word-separated counts;
5. reciprocal-centre count equality.

For each radius compute

```text
forcing_count(q=1) / median(forcing_count(eight controls)).
```

When the median control count is zero, the ratio gate passes only if the target
count is strictly positive.

## Frozen primary rule

Stage H returns `RADIUS_ROBUST_HALF_EXCESS` only if, at every one of the eight
radii:

1. the target count at `q=1` is strictly positive;
2. `q=1` is strictly first among all nine centres;
3. the target count is at least `5/4` of the median control count, using the
   declared zero-median rule.

Alternative conclusions are frozen as:

- `RADIUS_LOCAL_HALF_EXCESS`: the full gate passes at `1/10` but fails at one
  or more other radii;
- `RADIUS_UNSTABLE`: `q=1` loses strict first place at any radius;
- `NO_HALF_FORCING_AT_RADIUS`: the target count is zero at any radius.

## Frozen technical gates

Technical PASS requires:

- exact map, pair and event counts at every radius;
- reciprocal-conjugation closure of the map universe;
- exact reciprocal-centre count equality at every radius;
- deterministic byte-identical receipt regeneration;
- exact integer/rational forcing decisions.

## Secondary diagnostics

Without altering the primary decision, record:

- target forcing-rate sequence across radii;
- target-to-control-median ratio sequence;
- same-branch versus mixed-branch contributions;
- monotonicity of counts as radius expands;
- no extrapolation beyond the declared radius interval.

## Interpretation boundary

A positive result would show robustness across eight declared radii in the
complete `K=6` coefficient cube and for two-letter words. It would not prove an
all-radius, all-scale or all-dynamics law; it would not order IEEE `NaN` with
zero and would not close an RH bridge.
