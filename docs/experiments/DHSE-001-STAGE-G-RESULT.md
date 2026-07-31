# DHSE-001 — Stage G coefficient-scale persistence result

## Decision

- Technical status: **PASS**.
- Scientific status: **SCALE_PERSISTENT_HALF_EXCESS**.
- All frozen persistence gates: **PASS**.
- No merge, monograph inclusion or claim promotion is authorized.

Stage G expanded the complete coefficient universe from `K=1` through `K=6`
without changing the centres, projective radius, word set or whole-line forcing
predicate.

## Exact scale census

| K | Maps | Pair-word events | Half count | Half rate | Half rank |
|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 36 | 0 | 0 | tied calibration |
| 2 | 25 | 2,500 | 8 | `2/625` | 1 |
| 3 | 96 | 36,864 | 1,202 | `601/18432` | 1 |
| 4 | 256 | 262,144 | 15,104 | `59/1024` | 1 |
| 5 | 563 | 1,267,876 | 88,284 | `22071/316969` | 1 |
| 6 | 1,073 | 4,605,316 | 367,516 | `91879/1151329` | 1 |

The self-dual centre is strictly first at every non-degenerate scale
`K=2,...,6`.

## Complete count profiles

The exact forcing-count profiles, ordered by centres

```text
1/16, 1/8, 1/4, 1/2, 1, 2, 4, 8, 16
```

are:

```text
K=1: 0, 0, 0, 0, 0, 0, 0, 0, 0
K=2: 0, 0, 0, 4, 8, 4, 0, 0, 0
K=3: 0, 4, 58, 920, 1202, 920, 58, 4, 0
K=4: 4, 104, 1786, 6712, 15104, 6712, 1786, 104, 4
K=5: 42, 924, 13962, 42008, 88284, 42008, 13962, 924, 42
K=6: 302, 4366, 45644, 156190, 367516, 156190, 45644, 4366, 302
```

Every scale is exactly symmetric under reciprocal centre exchange.

## Frozen ratio gate

The target-to-median-control ratios are:

| K | Median control count | Exact ratio | Approximate ratio |
|---:|---:|---:|---:|
| 3 | 31 | `1202/31` | 38.774 |
| 4 | 945 | `15104/945` | 15.983 |
| 5 | 7,443 | `29428/2481` | 11.861 |
| 6 | 25,005 | `367516/25005` | 14.698 |

All exceed the frozen threshold `5/4`.

## Anti-collapse gate

The normalized target rate increased from

\[
r_4=\frac{59}{1024}\approx0.0576172
\]

to

\[
r_6=\frac{91879}{1151329}\approx0.0798026.
\]

Their ratio is

\[
\frac{r_6}{r_4}
=
\frac{94084096}{67928411}
\approx1.38505.
\]

Thus the Stage F excess did not collapse as the coefficient cube expanded to
`K=6`; it strengthened in normalized frequency over the declared range.

## Word decomposition at K=6

At the largest frozen scale, the half count decomposes as:

```text
LL = 87,986
LR = 95,772
RL = 95,772
RR = 87,986
```

The effect remains distributed across same-branch and mixed-branch words. It
is not the recurrence of one isolated `LR` mechanism.

## Interpretation

Stage G removes the simplest explanation that the Stage F result was only a
small `K=4` boundary anomaly. Across every complete cube from `K=2` to `K=6`,
the self-dual centre is uniquely most frequent, passes the frozen ratio gate,
and its normalized forcing rate increases.

This is stronger finite evidence than Stages B–E supplied. It is still not a
proof of an asymptotic law. The coefficient distribution remains a specific
uniform lattice measure, the word length remains two, and the radius remains
`1/10`. A valid next stage must vary one of those structural choices without
retuning the centre after observing results.

Nothing in Stage G treats IEEE `NaN` as a number or orders it with zero. The
abstract undefined label remains separate. No Riemann-hypothesis bridge is
promoted.

## Reproduction

```bash
python scripts/run_dhse_001_stage_g.py
python -m pytest -q tests/test_dhse_001_stage_g.py
```

The deterministic receipt is stored at
`data/processed/dhse_001_stage_g_receipt.json`.
