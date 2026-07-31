# DHSE-001 — Stage J projective-quotient robustness result

## Decision

- Technical status: **PASS**.
- Scientific status: **PROJECTIVE_QUOTIENT_ROBUST_HALF_EXCESS**.
- All preregistered length gates: **PASS**.
- Anti-collapse gate: **PASS** at every length.
- No merge, pull request, monograph inclusion or claim promotion is authorized.

Stage J removed scalar multiplicity from the `K=6` coefficient lattice by
retaining only matrices with `gcd(a,b,c,d)=1`.

## Projective normalization

The full coefficient universe contained `1073` admissible matrices. The
primitive quotient contains `952` representatives, so `121` scalar duplicates
were removed.

The primitive representatives have the following numbers of admissible scalar
copies inside the original `K=6` cube:

| Number of copies | Primitive maps |
|---:|---:|
| 1 | 862 |
| 2 | 68 |
| 3 | 19 |
| 6 | 3 |

The reconstruction identity is exact:

```text
862*1 + 68*2 + 19*3 + 3*6 = 1073.
```

The primitive universe remains exactly closed under reciprocal conjugation.

## Exact target results

| Word length | Primitive events | Half count | Primitive half rate | Stage I full rate |
|---:|---:|---:|---:|---:|
| 1 | 1,812,608 | 24,752 | `13/952` | `13/1073` |
| 2 | 3,625,216 | 314,690 | `157345/1812608` | `91879/1151329` |
| 3 | 7,250,432 | 943,740 | `4815/36992` | `562921/4605316` |
| 4 | 14,500,864 | 2,219,236 | `554809/3625216` | `167131/1151329` |

At every length, the primitive-projective target rate is greater than the
corresponding full-representative rate. Scalar multiplicity had therefore been
slightly suppressing, not creating, the observed half concentration.

## Complete centre profiles

Centres are ordered as

```text
1/16, 1/8, 1/4, 1/2, 1, 2, 4, 8, 16.
```

The primitive aggregate profiles are:

```text
length 1: 0, 0, 0, 5712, 24752, 5712, 0, 0, 0
length 2: 284, 3984, 39926, 129312, 314690, 129312, 39926, 3984, 284
length 3: 7698, 28614, 164852, 467234, 943740, 467234, 164852, 28614, 7698
length 4: 38970, 93992, 444322, 1180356, 2219236, 1180356, 444322, 93992, 38970
```

Every profile is exactly reciprocal, and `q=1` is strictly first at every
length.

## Ratio gate

At length 1, the median control count is zero while the target is positive and
strictly first. For lengths 2–4, the exact target-to-control-median ratios are:

```text
length 2: 62938/4391   ≈ 14.3334
length 3: 134820/13819 ≈ 9.75613
length 4: 2219236/269157 ≈ 8.24514
```

All exceed the preregistered threshold `5/4`.

## Primitive/full comparison

The exact primitive-rate/full-rate ratios are:

```text
length 1: 1073/952 ≈ 1.12710
length 2: 181155861505/166540610432 ≈ 1.08776
length 3: 5543649135/5205893408 ≈ 1.06488
length 4: 638767691161/605885975296 ≈ 1.05427
```

Thus all four anti-collapse tests pass with ratios above one.

## Interpretation

Stage J removes a substantial measure-theoretic confound. The half excess does
not depend on counting positive scalar multiples of one Möbius transformation
as separate operators. It survives on the actual finite projective quotient
and becomes modestly stronger in normalized frequency.

This result remains finite and measure-specific. The primitive representatives
are still sampled uniformly inside a bounded coefficient cube; alternative
reciprocal-invariant weights may alter the profile. The next appropriate test
is therefore a preregistered family of symmetric integer weightings on the
primitive projective universe.

IEEE `NaN` remains outside the mathematical state space. No ordering of `NaN`
with zero and no Riemann-hypothesis bridge is asserted.

## Reproduction

```bash
python scripts/run_dhse_001_stage_j.py
python -m pytest -q tests/test_dhse_001_stage_j.py
```

The deterministic receipt is stored at
`data/processed/dhse_001_stage_j_receipt.json`.
