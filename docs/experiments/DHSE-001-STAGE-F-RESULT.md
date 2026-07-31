# DHSE-001 — Stage F centre-blind coefficient-cube result

## Decision

- Technical status: **PASS**.
- Scientific status: **CENTRE_BLIND_HALF_EXCESS**.
- Frozen exceptional-frequency gate: **PASS**.
- The result is restricted to the declared bounded coefficient universe.
- No merge, monograph inclusion or claim promotion is authorized.

The preregistration was committed before implementation and before the receipt.
The complete operator universe was enumerated; no operator sampling or
post-result centre selection was used.

## Exact census

The frozen universe contains:

- `256` positive orientation-preserving integer Möbius maps;
- `65,536` ordered branch pairs `(L,R)`;
- four two-letter words `LL, LR, RL, RR`;
- `262,144` pair-word events;
- nine reciprocal odds centres;
- exact integer/rational endpoint tests only.

An event was counted for centre `q` only when the image of the entire positive
line under the composed word lay within the unchanged projective radius
`1/10` around `q`.

## Primary result

| Odds centre `q` | Probability `p=q/(1+q)` | Forcing events | Distinct pairs | Rank |
|---:|---:|---:|---:|---:|
| `1/16` | `1/17` | 4 | 4 | 8 |
| `1/8` | `1/9` | 104 | 104 | 6 |
| `1/4` | `1/5` | 1,786 | 1,448 | 4 |
| `1/2` | `1/3` | 6,712 | 5,447 | 2 |
| **`1`** | **`1/2`** | **15,104** | **11,148** | **1** |
| `2` | `2/3` | 6,712 | 5,447 | 2 |
| `4` | `4/5` | 1,786 | 1,448 | 4 |
| `8` | `8/9` | 104 | 104 | 6 |
| `16` | `16/17` | 4 | 4 | 8 |

The median of the eight control counts is exactly `945`. Therefore

\[
\frac{N(q=1)}{\operatorname{median}_{q\ne1}N(q)}
=
\frac{15104}{945}
\approx 15.9831.
\]

The target is strictly first and exceeds the frozen `5/4` ratio threshold.
The preregistered Stage F conclusion is therefore
`CENTRE_BLIND_HALF_EXCESS`.

## Word decomposition

| Centre | `LL` | `LR` | `RL` | `RR` |
|---:|---:|---:|---:|---:|
| `1/16` | 0 | 2 | 2 | 0 |
| `1/8` | 0 | 52 | 52 | 0 |
| `1/4` | 512 | 381 | 381 | 512 |
| `1/2` | 1,792 | 1,564 | 1,564 | 1,792 |
| **`1`** | **4,096** | **3,456** | **3,456** | **4,096** |
| `2` | 1,792 | 1,564 | 1,564 | 1,792 |
| `4` | 512 | 381 | 381 | 512 |
| `8` | 0 | 52 | 52 | 0 |
| `16` | 0 | 2 | 2 | 0 |

The excess is not carried by one specially chosen word. It appears in both
same-branch and mixed-branch compositions.

## Symmetry audit

The coefficient universe is exactly closed under reciprocal conjugation

```text
[a,b,c,d] -> [d,c,b,a].
```

All reciprocal centre pairs have identical counts. The count profile is
therefore exactly symmetric around the self-dual centre:

```text
4, 104, 1786, 6712, 15104, 6712, 1786, 104, 4.
```

This rules out an implementation asymmetry between the zero-facing and
undefined-facing directions.

## Interpretation

Stage F is the first DHSE stage in which `q=1` passed a centre-blind gate across
a complete operator universe that was not selected around the previously
successful Möbius pair. This is a genuine positive finite-census result.

It is not yet evidence for an unrestricted operator-independent law. The
coefficient cube itself is bounded and centred on small comparable integer
coefficients. Such a universe may geometrically favour image intervals whose
endpoint ratios are near unity. The next required test is therefore expansion
of the coefficient cube while preserving the same centre set, radius and exact
forcing predicate.

The result also does not make IEEE `NaN` a number or endpoint. The abstract
`UNDEFINED_BOTTOM` label remains separate from implementation `NaN`, and no
Riemann-hypothesis bridge is promoted.

## Reproduction

```bash
python scripts/run_dhse_001_stage_f.py
python -m pytest -q tests/test_dhse_001_stage_f.py
```

The deterministic receipt is stored at
`data/processed/dhse_001_stage_f_receipt.json`.
