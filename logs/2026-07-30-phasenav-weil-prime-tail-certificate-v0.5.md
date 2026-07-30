# PhaseNav–Weil prime-tail certificate v0.5

Date: 2026-07-30
Base main: `25061583faece869604cebd63d9933fe67317dfb`
Branch: `agent/prime-tail-certificate-v0.5`

## Scope

- Replace empirical cutoff comparison by an analytic omitted-tail certificate.
- Use the reciprocal coordinate `z_tail=1/log(x)` only for compactifying the logarithmic prime tail.
- Keep the map explicitly separate from zeta-zero coordinates.

## Exact additions

- Monotonicity threshold for each Gaussian-polynomial tail term.
- Reciprocal compactification to a finite interval with a smooth flat endpoint.
- Closed upper-incomplete-gamma representation.
- Entrywise prime-power tail majorant using `Lambda(n)<=log(n)`.
- Finite-section operator-norm and Weyl eigenvalue enclosure.

## Numerical receipt

- Profile: `w=0.8`, `Q=100000`, `N<=6`.
- Maximum entry bound: `6.155991053261891e-13`.
- Maximum finite-section operator-norm bound: `7.717202888999335e-13`.
- Log, reciprocal and gamma integral representations: PASS.
- Finite prime-shell regressions: PASS.

## Boundary

The construction controls cutoff removal for every fixed declared finite section. It does not prove uniform positivity as `N->infinity`, global regularized-form continuity, native zero closure, or the Riemann Hypothesis.
