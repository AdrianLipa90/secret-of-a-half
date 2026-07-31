# DHSE-001 — Stage L preregistration: dense rational centre scan

## Status before execution

- Branch: `experiment/dhse-001` only.
- No Stage L centre counts or conclusion are recorded here.
- No merge, pull request, monograph inclusion or claim promotion is authorized.

## Scientific question

Does the half remain the unique maximum when the sparse nine-centre diagnostic
is replaced by a complete, reciprocal and exact rational grid?

## Frozen operator universe and measure

- the `952` primitive `K=6` Möbius representatives from Stage J;
- uniform projective counting measure;
- complete binary word sets of lengths `2` and `4`;
- exact integer arithmetic;
- unchanged whole-positive-line forcing predicate;
- unchanged projective radius `1/10`.

## Frozen centre grid

The centre set is

`Q_8 = {m/n : 1 <= m,n <= 8, gcd(m,n)=1}`.

After reduction and deduplication this contains exactly `43` positive rational
centres, ordered from `1/8` to `8`. It is exactly closed under `q -> 1/q` and
contains the self-dual centre `q=1`.

Every centre is evaluated by the same code path. No centre is added, removed or
reweighted after execution.

## Primary gate at each word length

A declared word length passes when:

1. `q=1` has strictly greater forcing count than all other 42 centres;
2. its count is at least `5/4` of the median count of the 42 controls;
3. every reciprocal pair `q,1/q` has exactly equal counts.

## Frozen conclusion rule

- `DENSE_GRID_UNIQUE_HALF_MAXIMUM` if both lengths 2 and 4 pass;
- `DENSE_GRID_HALF_PLATEAU` if `q=1` is tied for first at either length and no centre exceeds it;
- `DENSE_GRID_OFF_CENTRE_MAXIMUM` if any other centre exceeds `q=1`;
- `DENSE_GRID_RATIO_WEAK` if the half is uniquely first but a median-ratio gate fails.

## Secondary diagnostics

Recorded but unable to alter the primary conclusion:

- complete ordered count profile over all 43 centres;
- second-highest centre and exact half/runner-up ratio;
- monotonicity of counts as centres approach `q=1` from each side;
- number and location of local maxima;
- reciprocal symmetry residuals.

## Interpretation boundary

A positive result would establish a unique maximum only on the complete finite
rational grid `Q_8`, not over every positive real centre. The coefficient bound,
word lengths, radius and uniform primitive measure remain fixed. IEEE `NaN`
remains outside the state space and no Riemann-hypothesis claim is promoted.
