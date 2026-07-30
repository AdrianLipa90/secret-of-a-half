# Validation receipt — Version 0.6

Date: 2026-07-30
Base main: `c31969c6fa4d40d9d9bf8effbe78800f77d1204d`

## Technical targets

- Existing regression suite remains mandatory.
- New adaptive-cutoff regression suite: 8 tests.
- Native adaptive-cutoff receipt generation: required.
- Structured and Markdown claim ledgers must contain `SOH-L021` and `SOH-N006`.
- Monograph Chapter 20 must compile without unresolved references or overfull boxes.

## Mathematical PASS

- The elementary tail inequality `integral h <= h(U)/alpha(U)` is proved for positive decay rate.
- A coarse finite-section envelope is derived from explicit Hermite coefficient and row-sum bounds.
- For every `c>0`, the schedule `Q_N=exp(cN)` gives
  `log B_N(cN)=-c^2 N^2/(4w^2)+O(N log N)`.
- Therefore the coarse adaptive envelope tends to zero.

## Numerical PASS

Declared profile:

- Gaussian width: `0.8`;
- base cutoff: `100000`;
- logarithmic slope: `2.0`;
- basis sizes: `1..20`;
- target: `1e-12`.

Results:

- all 20 sharp v0.5 certificates pass;
- maximum: `3.280365246530569e-14` at `N=5`;
- final-window coarse envelope is strictly decreasing;
- arithmetic audit consumes no zeta-zero list.

## Boundary

This closes an adaptive diagonal cutoff schedule, not uniformity at one fixed
cutoff. Positivity of all infinite-cutoff sections, closure of the complete
form, the null-space implication and `SOH-C005` remain open. Version 0.6 does
not claim a proof of the Riemann Hypothesis.
