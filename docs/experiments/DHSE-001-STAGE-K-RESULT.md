# DHSE-001 — Stage K reciprocal-invariant measure result

## Decision

- Technical status: **PASS**.
- Scientific status: **MEASURE_ROBUST_HALF_EXCESS**.
- Primary measure-length cells: **12/12 PASS**.
- Anti-collapse comparisons: **12/12 PASS**.
- No merge, pull request, monograph inclusion or claim promotion is authorized.

Stage K replaced the uniform primitive-map measure with six preregistered,
positive and reciprocal-invariant integer weights. The primitive `K=6`
universe, centres, projective radius and whole-line forcing predicate were
unchanged.

## Declared measures

For a primitive matrix `M=[a,b,c,d]` and `Delta=ad-bc`:

```text
uniform                 = 1
determinant             = Delta
determinant_squared     = Delta^2
coefficient_sum         = a+b+c+d
boundary_taper          = 7-max(a,b,c,d)
low_determinant_taper   = 37-Delta
```

Their total map weights were respectively:

```text
952, 10219, 172197, 11690, 1827, 25005.
```

All six weights are exactly invariant under reciprocal conjugation.

## Primary results

| Measure | Length-2 half rate | Length-2 target/control median | Length-4 half rate | Length-4 target/control median |
|---|---:|---:|---:|---:|
| uniform | 0.086806 | 14.333 | 0.153042 | 8.245 |
| determinant | 0.051365 | 27.708 | 0.132303 | 12.089 |
| determinant squared | 0.026678 | 44.158 | 0.104747 | 16.583 |
| coefficient sum | 0.113293 | 19.589 | 0.185056 | 10.875 |
| boundary taper | 0.076620 | 13.869 | 0.141774 | 8.132 |
| low-determinant taper | 0.100307 | 12.486 | 0.159147 | 7.397 |

For every measure and both word lengths:

- `q=1` is strictly first;
- its weighted mass exceeds `5/4` of the median control mass;
- reciprocal centre pairs have exactly equal weighted masses.

## Strongest deformation

The most aggressive declared high-determinant weighting is `Delta^2`. At
length 2 its profile is

```text
81260,
1926286,
141383378,
872888370,
3164153256,
872888370,
141383378,
1926286,
81260.
```

The exact half rate is

```text
87893146/3294645201 ≈ 0.0266776,
```

and the exact target-to-control-median ratio is

```text
43946573/995206 ≈ 44.1583.
```

Although this measure suppresses the absolute half rate relative to uniform,
it sharpens the centre ranking.

## Anti-collapse result

Every weighted target rate remains at least one quarter of the corresponding
uniform primitive Stage J rate. The smallest weighted/uniform ratio occurs for
`determinant_squared` at length 2 and is approximately `0.3073`, still above
the preregistered `0.25` boundary.

Several measures increase the target rate. At length 4, for example,
`coefficient_sum` produces approximately `0.1851` and
`low_determinant_taper` approximately `0.1591`, compared with the uniform
primitive rate `0.1530`.

## Word contributions

The half excess remains distributed across all declared words. For example,
under determinant-squared weighting at length 4, all sixteen target word masses
are positive, ranging from about `2.45e9` to `3.86e9`. Complement-reversal word
partners have equal masses, as required by reciprocal closure.

## Interpretation

Stage K removes uniform counting measure as the simplest explanation of the
finite half concentration. The ranking survives weightings that favour:

- large determinants;
- very large determinants quadratically;
- large coefficient sums;
- interior coefficient points;
- small determinants.

This is substantial finite robustness, but not measure independence in the
mathematical sense. The six measures were selected to span several natural,
reciprocal-invariant integer weightings; an adversarial or singular measure can
always concentrate on another subset. A theorem would require explicit
conditions on a class of measures and a proof that those conditions force a
maximum at the self-dual centre.

IEEE `NaN` remains outside the state space. No ordering of `NaN` with zero and
no Riemann-hypothesis bridge is asserted.

## Reproduction

```bash
python scripts/run_dhse_001_stage_k.py
python -m pytest -q tests/test_dhse_001_stage_k.py
```

The deterministic receipt is stored at
`data/processed/dhse_001_stage_k_receipt.json`.
