# 2026-07-30 — PhaseNav–Weil Hermite ladder v0.3

Base GitHub HEAD: `5c4883d795ac0556a0d76aed88f50477a4cf1c1c`.

## Scope

- Define a native translated-scaled Hermite channel ladder.
- Replace one `2x2` sample by principal arithmetic matrices of increasing size.
- Prove the dense-core and closed-transform reductions.
- Keep global positivity, cutoff removal and the closure implication open.

## Integrity boundary

- No zero list is consumed by the arithmetic sum.
- Finite numerical positivity is not promoted to global positivity.
- No proof of the Riemann Hypothesis is claimed.
- No GitHub branch or repository was modified during local construction.

## Final receipt

- tests: 8/8 PASS;
- prime cutoffs: 50,000 and 100,000;
- sampled principal sections: N=1..6;
- all sampled sections PSD within tolerance;
- largest cutoff error: 2.5238422463047527e-12 at N=6;
- orthonormality residual: 4.440892098500626e-16;
- on-axis validation lambda_min: -1.319726356320561e-16;
- synthetic off-axis lambda_min: -0.051399255306793665.
