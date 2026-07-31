# DHSE-001 — Stage B result

## Decision

- Technical status: **PASS**.
- Scientific status: **FAMILY_DEPENDENT**.
- Robust-effect gate: **FAIL**.
- Passing experimental families: `1/4`.
- No merge or monograph promotion is authorized.

The preregistration was committed before the implementation receipt. The
frozen robust criterion required at least three of four non-calibration
operator families to pass.

## Declared sample size

Each operator family used:

- 64 domain-separated deterministic seeds;
- 384 transformations per seed;
- 64-state burn-in;
- 20,544 observed post-burn-in states;
- 20,480 observed post-burn-in transitions;
- exact rational arithmetic.

## Primary results

| Family | Reciprocal-conjugacy audit | Target occupancy at `q=1` | Target rank | Family gate |
|---|---:|---:|---:|---:|
| reciprocal calibration | 10/10 matches | 5/107 | 5 | calibration only |
| affine skew | 0/10 matches | 7/20544 | 5 | FAIL |
| Möbius skew | 0/10 matches | 5147/20544 | 1 | PASS |
| scale–translate | 0/10 matches | 0 | tied rank 1 | FAIL |
| Collatz-derived stream | 2/10 matches | 1903/20544 | 3 | FAIL |

Only the Möbius-skew family placed `q=1` strictly first. Its median control
occupancy was zero while target occupancy was positive, so it passed the frozen
zero-median rule. This is a family-specific attractor effect, not a result that
survived operator-family changes.

The Collatz-derived stream produced a target-to-control-median occupancy ratio
of `3806/1977`, approximately `1.925`, but `q=1` ranked third rather than first;
it therefore failed the preregistered primary rule.

## Interpretation

Stage B rejects the strongest version of the present dynamical hypothesis:
with the declared seed ensemble, metric, radius and operator families, the half
was **not** a robustly dominant trajectory centre.

It does not reject the exact structural statements already established in the
repository:

- complement has the unique fixed probability `p=1/2`;
- reciprocal odds duality has the unique fixed coordinate `q=1`;
- `p=1/2` is the Fisher–Rao midpoint of the Bernoulli interval.

Those are geometric facts. Stage B tested the additional claim that unrelated
deterministic dynamics would independently prefer that point. The present
answer is: **not generally; one family did, three did not**.

## Reproducibility

Run:

```bash
python scripts/run_dhse_001_stage_b.py
python -m pytest -q tests/test_dhse_001_stage_b.py
```

The compact receipt stores the primary statistics and SHA-256 of the full
centre-scan receipt:

`d0457d72fedf988bf79287fdbc8d45cd80b266c45d160f5a60d4b5f0827c5ca3`

## Next admissible stage

A Stage C may investigate why the Möbius-skew family concentrates near `q=1`
and whether that is simply its invariant measure or fixed-point geometry. It
must not reuse Stage B as evidence of a universal halfway law. Stage C should
analytically derive each family's invariant or stationary measure before any
new target statistic is evaluated.
