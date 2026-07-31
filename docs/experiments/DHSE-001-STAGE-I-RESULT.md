# DHSE-001 — Stage I word-length robustness result

## Decision

- Technical status: **PASS**.
- Scientific status: **WORD_LENGTH_ROBUST_HALF_EXCESS**.
- All preregistered length gates: **PASS**.
- No merge, pull request, monograph inclusion or claim promotion is authorized.

Stage I enumerated every binary word of lengths `1,2,3,4` in the complete
`K=6` positive integer Möbius universe. The coefficient universe, nine centres,
projective radius `1/10` and whole-line forcing predicate were unchanged.

## Exact aggregate results

| Word length | Words | Pair-word events | Half count | Half rate | Half rank |
|---:|---:|---:|---:|---:|---:|
| 1 | 2 | 2,302,658 | 27,898 | `13/1073` | 1 |
| 2 | 4 | 4,605,316 | 367,516 | `91879/1151329` | 1 |
| 3 | 8 | 9,210,632 | 1,125,842 | `562921/4605316` | 1 |
| 4 | 16 | 18,421,264 | 2,674,096 | `167131/1151329` | 1 |

The corresponding approximate target rates are:

```text
length 1: 0.0121156
length 2: 0.0798026
length 3: 0.122233
length 4: 0.145164
```

The rate is nondecreasing throughout the declared range.

## Complete centre profiles

Centres are ordered as

```text
1/16, 1/8, 1/4, 1/2, 1, 2, 4, 8, 16.
```

The aggregate forcing profiles are:

```text
length 1: 0, 0, 0, 6438, 27898, 6438, 0, 0, 0
length 2: 302, 4366, 45644, 156190, 367516, 156190, 45644, 4366, 302
length 3: 9014, 34148, 194042, 572950, 1125842, 572950, 194042, 34148, 9014
length 4: 47484, 117722, 533344, 1456952, 2674096, 1456952, 533344, 117722, 47484
```

Every profile is exactly invariant under `q -> 1/q`. At every length, the
self-dual centre `q=1` is strictly first.

## Ratio gate

At length 1 the median control count is zero while the target count is positive
and strictly greater than every control. Under the preregistered rule this
passes the ratio gate.

For lengths 2–4 the exact target-to-median-control ratios are:

```text
length 2: 367516/25005  ≈ 14.6977
length 3: 1125842/114095 ≈ 9.86758
length 4: 2674096/325533 ≈ 8.21452
```

All exceed the frozen threshold `5/4` by a large margin.

## Individual-word structure

The result is not carried by one word. At length 4, for example, the half
counts range from `133,052` for `LLLL` and `RRRR` to `193,800` for `LRRL` and
`RLLR`. Every one of the sixteen words contributes a positive half-forcing
count.

Complement-reversal partners have identical centre profiles. This follows from
the reciprocal closure of the operator universe and is verified in the stored
receipt.

## Interpretation

Stage I removes the simplest remaining explanation that the Stage F–H excess
was peculiar to two-step words. In the declared complete lattice universe,
the self-dual centre remains uniquely dominant for all complete word sets from
length one through four, and its normalized forcing frequency rises over this
range.

This is stronger finite evidence for a structural concentration around the
self-dual projective coordinate. It is not an all-length theorem. Longer words
may behave differently, and the uniform lattice measure still counts scalar
multiples of a Möbius matrix as separate coefficient representatives.

The next required control is therefore projective normalization: reduce every
matrix to its primitive integer representative and repeat the centre-blind
census without scalar-multiplicity weighting.

IEEE `NaN` remains outside the mathematical state space. No ordering of `NaN`
with zero and no Riemann-hypothesis bridge is asserted.

## Reproduction

```bash
python scripts/run_dhse_001_stage_i.py
python -m pytest -q tests/test_dhse_001_stage_i.py
```

The deterministic receipt is stored at
`data/processed/dhse_001_stage_i_receipt.json`.
