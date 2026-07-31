# DHSE-001 — Stage E exploratory coefficient-neighbourhood audit

## Status

- Branch: `experiment/dhse-001` only.
- Exploratory exact sensitivity analysis; **not preregistered**.
- No new claim about universal halfway selection is authorized.
- No merge, monograph inclusion or claim promotion is authorized.

## Question

The Stage C/D Möbius mechanism uses

```text
L = [1,1,2,3]
R = [3,1,1,2]
```

and the left-to-right word `LR`. Does whole-line forcing into the frozen Stage B
target ball survive small integer perturbations of these eight coefficients?

## Declared exploratory neighbourhood

Each coefficient is varied independently by `-1`, `0` or `+1`, clipped at
zero. A matrix `[a,b,c,d]` is admitted only when

- `a>0`, `b>=0`, `c>=0`, `d>0`;
- determinant `a*d-b*c>0`.

These conditions keep the map positive and orientation-preserving on `z>0`.
Every admissible left matrix is paired with every admissible right matrix.

The tested composition is always `R(L(z))`. The target ball remains exactly

```text
[9/11,11/9].
```

A pair passes when the image of the entire positive projective line under
`R∘L` lies inside that interval.

## Interpretation boundary

A nonzero passing fraction would show structural persistence inside this local
integer neighbourhood. It would not make the mechanism operator-independent:
the neighbourhood is centred on the already identified Möbius construction
and the scan is explicitly exploratory.
