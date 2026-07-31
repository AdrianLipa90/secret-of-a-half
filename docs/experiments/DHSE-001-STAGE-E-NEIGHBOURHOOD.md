# DHSE-001 — Stage E exploratory coefficient-neighbourhood audit

## Decision

- Technical status: **PASS**.
- Scientific status: **EXPLORATORY_SENSITIVITY_ONLY**.
- Conclusion: **LOCALLY_PERSISTENT_BUT_SPARSE**.
- This stage was not preregistered.
- No merge, monograph inclusion or claim promotion is authorized.

## Neighbourhood

The Stage C/D Möbius pair was

\[
L=[1,1,2,3],
\qquad
R=[3,1,1,2],
\]

with matrices interpreted as `(a*z+b)/(c*z+d)`. Each of the eight integer
coefficients was varied independently by `-1`, `0` or `+1`, clipped at zero.
Only positive orientation-preserving maps were retained:

\[
a>0,\quad b\ge0,\quad c\ge0,\quad d>0,\quad ad-bc>0.
\]

This produced:

- `41` admissible left matrices;
- `75` admissible right matrices;
- `3075` admissible ordered pairs.

Every pair was tested by exact rational arithmetic. The composition was always
`R(L(z))`, and passing required the image of the entire positive line to lie in
the unchanged Stage B target interval

\[
\left[\frac9{11},\frac{11}{9}\right].
\]

## Exact result

`145` of the `3075` admissible pairs preserved universal `LR` forcing:

\[
\frac{145}{3075}=\frac{29}{615}\approx0.0471545.
\]

Thus the original pair is not isolated, but the property occupies only about
`4.72%` of this declared local integer neighbourhood.

Counts by total coefficient `L1` distance from the base pair were:

| Distance | Passing pairs |
|---:|---:|
| 0 | 1 |
| 1 | 1 |
| 2 | 7 |
| 3 | 19 |
| 4 | 28 |
| 5 | 39 |
| 6 | 32 |
| 7 | 15 |
| 8 | 3 |

## Nearest non-base persistence

The closest distinct passing pair changes only the leading coefficient of the
right map:

\[
L=[1,1,2,3],
\qquad
R'=[4,1,1,2].
\]

Its composition is

\[
R'(L(z))=\frac{6z+7}{5z+7},
\]

whose positive-line image is

\[
\left(1,\frac65\right)
\subset
\left[\frac9{11},\frac{11}{9}\right].
\]

Therefore the whole-line forcing mechanism survives at coefficient distance
one. It is structurally persistent in a local sense.

## Interpretation

Stage E sharpens, rather than reverses, the Stage C/D diagnosis:

- the Möbius forcing effect is not a single-point numerical accident;
- it persists for a minority of nearby admissible operators;
- it is nevertheless not generic even in a neighbourhood centred on the
  successful construction;
- the neighbourhood itself was selected around the known positive mechanism.

The result supports the description **operator-class-local**, not
operator-independent. It supplies no evidence that arbitrary deterministic
dynamics select one half, and it does not place IEEE `NaN` in the mathematical
state space.

## Reproduction

```bash
python scripts/run_dhse_001_stage_e.py
python -m pytest -q tests/test_dhse_001_stage_e.py
```

The deterministic receipt is stored at
`data/processed/dhse_001_stage_e_receipt.json`.
