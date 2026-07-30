# 2026-07-30 — Native PhaseNav–Weil positivity probe v0.1

## Scope

Added a second native PhaseNav construction aimed at the positivity route for
`SOH-C004`. Existing monograph sources were not changed.

## Source of truth

```text
construction/phasenav/secret_of_half_weil_operator.pnv
```

The Python module is an executor and auditor of the `.pnv` profile.

## Technical receipt

```text
on_axis_control:
  lambda_min =  1.304512053935e-13
  lambda_max =  2.000000000000e+00

synthetic_off_axis:
  lambda_min = -1.989005564501e-03
  lambda_max =  4.027671100607e+00

CONTROL_PSD: PASS
OFF_AXIS_NEGATIVE_WITNESS: PASS
```

## Mathematical status

Exact:

- an involution-fixed finite fixture reduces the operator to a Gram matrix;
- the resulting finite matrix is positive semidefinite.

Numerical:

- the declared Gaussian pair detects the synthetic off-axis quartet by a
  negative eigenvalue.

Open:

- prime-side explicit-formula implementation;
- dense admissible test family and regularization;
- positivity-to-native-closure implication;
- `SOH-C005` and therefore `SOH-C004`.

No proof of the Riemann Hypothesis is claimed.
