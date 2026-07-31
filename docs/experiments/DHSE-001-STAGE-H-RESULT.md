# DHSE-001 — Stage H radius-robustness result

## Decision

- Technical status: **PASS**.
- Scientific status: **RADIUS_ROBUST_HALF_EXCESS**.
- All frozen radius gates: **PASS**.
- No merge, monograph inclusion or claim promotion is authorized.

Stage H used the complete `K=6` coefficient universe, all four two-letter
words and the unchanged nine reciprocal centres. Only the projective radius
was varied, using the eight values committed before execution.

## Exact target results

| Radius | Half forcing count | Half forcing rate | Rank |
|---:|---:|---:|---:|
| `1/40` | 26,544 | `6636/1151329` | 1 |
| `1/30` | 43,140 | `10785/1151329` | 1 |
| `1/20` | 81,864 | `20466/1151329` | 1 |
| `1/15` | 171,608 | `42902/1151329` | 1 |
| `1/10` | 367,516 | `91879/1151329` | 1 |
| `1/8` | 510,480 | `127620/1151329` | 1 |
| `1/6` | 759,680 | `189920/1151329` | 1 |
| `1/5` | 1,018,500 | `254625/1151329` | 1 |

The half count is strictly positive and strictly first at every declared
radius. It increases monotonically as the target interval expands.

## Ratio gate

At every radius, the target count exceeds `5/4` of the median of the eight
control counts. The exact target-to-control-median ratios range from

```text
26544/433 ≈ 61.30  at radius 1/40
```

to

```text
4850/449 ≈ 10.80  at radius 1/5.
```

The effect therefore remains strong even when the projective neighbourhood is
made eight times wider.

## Symmetry

Every radius produced an exactly reciprocal count profile. For example, at
radius `1/40`:

```text
0, 114, 752, 4922, 26544, 4922, 752, 114, 0
```

and at radius `1/5`:

```text
2366, 25820, 162760, 540094, 1018500,
540094, 162760, 25820, 2366.
```

Thus the excess at `q=1` is not caused by directional asymmetry between the
zero-facing and undefined-facing sides.

## Word contributions

At narrow radius `1/40`, the target count decomposes as:

```text
LL = 9,657
LR = 3,615
RL = 3,615
RR = 9,657
```

At broad radius `1/5`:

```text
LL = 216,746
LR = 292,504
RL = 292,504
RR = 216,746
```

The half excess persists in both same-branch and mixed-branch sectors. The
relative contribution changes with radius, but no single word class carries
the entire effect.

## Interpretation

Stage H removes the simple explanation that Stages F–G succeeded only because
of the original radius `1/10`. In the complete `K=6` lattice universe, the
self-dual centre remains uniquely dominant throughout the preregistered radius
range `1/40` to `1/5`.

The remaining major structural dependency is word length and the chosen
uniform lattice measure over integer coefficients. A later stage should vary
one of those without changing the centre set after observing results.

This is still finite exact evidence, not a theorem over all deterministic
operators. IEEE `NaN` remains outside the state space, and no Riemann-hypothesis
claim is promoted.

## Reproduction

```bash
python scripts/run_dhse_001_stage_h.py
python -m pytest -q tests/test_dhse_001_stage_h.py
```

The deterministic receipt is stored at
`data/processed/dhse_001_stage_h_receipt.json`.
