# DHSE-001 — Stage L dense rational centre result

## Decision

- Technical status: **PASS**.
- Scientific status: **DENSE_GRID_UNIQUE_HALF_MAXIMUM**.
- Length-2 gate: **PASS**.
- Length-4 gate: **PASS**.
- Global unimodality diagnostic: **FAIL** — secondary, not a primary gate.
- No merge, pull request, monograph inclusion or claim promotion is authorized.

Stage L replaced the original nine centres with every reduced rational `m/n`
for `1 <= m,n <= 8`. The resulting exact grid contains 43 centres from `1/8`
to `8` and is closed under reciprocal exchange.

## Unique maximum

For word length 2:

```text
target q=1:          314690
runner-up q=6/7,7/6: 292386
exact ratio:          157345/146193 ≈ 1.07628
```

For word length 4:

```text
target q=1:          2219236
runner-up q=5/6,6/5: 2175168
exact ratio:          554809/543792 ≈ 1.02026
```

Thus the half is strictly first at both declared lengths, even after adding 34
non-dyadic and intermediate control centres.

## Median-control gate

The exact target-to-control-median ratios are:

```text
length 2: 157345/64656 ≈ 2.43357
length 4: 554809/295089 ≈ 1.88014
```

Both exceed the frozen threshold `5/4`.

## Local profile near the half

For length 2, selected centres near `q=1` give:

| q | Count |
|---:|---:|
| 3/4 | 275004 |
| 4/5 | 271672 |
| 5/6 | 287916 |
| 6/7 | 292386 |
| 7/8 | 285200 |
| **1** | **314690** |
| 8/7 | 285200 |
| 7/6 | 292386 |
| 6/5 | 287916 |
| 5/4 | 271672 |
| 4/3 | 275004 |

For length 4:

| q | Count |
|---:|---:|
| 3/4 | 2056894 |
| 4/5 | 2002296 |
| 5/6 | 2175168 |
| 6/7 | 2168904 |
| 7/8 | 2141290 |
| **1** | **2219236** |
| 8/7 | 2141290 |
| 7/6 | 2168904 |
| 6/5 | 2175168 |
| 5/4 | 2002296 |
| 4/3 | 2056894 |

Every count is exactly mirrored under `q -> 1/q`.

## Non-unimodality

The dense scan reveals structure hidden by the nine-centre grid. The profile is
not globally monotone toward the half.

At length 2 it has symmetric local maxima at:

```text
1/4, 3/4, 6/7, 1, 7/6, 4/3, 4.
```

At length 4 the local maxima are:

```text
3/4, 5/6, 1, 6/5, 4/3.
```

The half remains the highest maximum, but the landscape contains lower
operator-combinatorial resonances. This matters: the result is not a smooth,
single-peaked distribution whose maximum follows trivially from reciprocal
symmetry.

## Interpretation

Stage L strengthens the positive finite result in one respect and limits it in
another:

- the maximum at the half survives a much denser exact control grid;
- the margin over the nearest rational competitors becomes small, especially
  at length 4;
- reciprocal symmetry alone does not explain the detailed oscillatory profile.

The next mathematical problem is no longer merely another larger census. It is
to characterize the interval-overlap count function over continuous positive
`q` and determine whether `q=1` is a genuine global maximizer or only the
highest sampled point of the finite `Q_8` grid.

IEEE `NaN` remains outside the state space. No ordering of `NaN` with zero and
no Riemann-hypothesis bridge is asserted.

## Reproduction

```bash
python scripts/run_dhse_001_stage_l.py
python -m pytest -q tests/test_dhse_001_stage_l.py
```

The deterministic receipt is stored at
`data/processed/dhse_001_stage_l_receipt.json`.
