# 2026-07-30 — PhaseNav–Weil arithmetic operator v0.2

## Scope

Added the first prime-side execution of the two-channel PhaseNav–Weil matrix.

## Source-of-truth rule

The authoritative profile is
`construction/phasenav/secret_of_half_weil_arithmetic.pnv`. The Python module
parses and audits it.

## Exact layer

- centred spectral-coordinate conversion;
- Gaussian channel-product formula;
- closed Fourier transform;
- Guinand–Weil term decomposition with the declared Fourier normalization.

## Numerical layer

- prime-power sums at cutoffs `10000` and `100000`;
- finite-radius archimedean integration;
- cutoff-stability receipt;
- positive-semidefinite sample;
- normalization comparison with the prior low-height spectral fixture.

## Boundary

The arithmetic sum receives no zero list. The target ordinate remains a
declared probe centre. The old zero fixture is used only after arithmetic
evaluation as a validation reference.

`SOH-C005` remains open. No proof of RH is claimed.
