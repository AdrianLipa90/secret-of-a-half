# DHSE-001 — Stage J preregistration: projective-quotient robustness

## Status before execution

- Branch: `experiment/dhse-001` only.
- No Stage J centre census or conclusion is recorded here.
- No merge, pull request, monograph inclusion or claim promotion is authorized.

## Scientific question

Does the Stage I word-length half excess persist after removing scalar
multiplicity from the coefficient lattice?

A Möbius matrix and every positive scalar multiple define the same projective
map. Stages F–I counted each admissible coefficient representative separately.
Stage J replaces that measure with one count per primitive integer
representative.

## Frozen projective normalization

Start from the complete `K=6` universe

`1 <= a,d <= 6`, `0 <= b,c <= 6`, `ad-bc > 0`.

Retain a matrix `[a,b,c,d]` exactly when

`gcd(a,b,c,d)=1`.

Every omitted matrix is a positive integer multiple of one retained primitive
representative. No additional weighting or sampling is allowed.

Expected primitive-map count from the normalization audit: `952`.
The primitive set must remain closed under reciprocal conjugation

`[a,b,c,d] -> [d,c,b,a]`.

## Frozen words, centres and forcing predicate

Unchanged from Stage I:

- every binary word of lengths `1,2,3,4`;
- centres `1/16,1/8,1/4,1/2,1,2,4,8,16`;
- target `q=1`, equivalent to `p=1/2`;
- projective radius `1/10`;
- whole-positive-line image forcing predicate;
- exact integer arithmetic;
- identical code path for all centres.

## Primary length gate

At each length, the primitive census passes when:

1. `q=1` is strictly first among the nine centres;
2. its forcing count is at least `5/4` of the median of the eight controls;
3. reciprocal centre pairs have exactly equal counts.

## Frozen anti-collapse comparison

The Stage I full-representative target rates are fixed as:

```text
length 1: 13/1073
length 2: 91879/1151329
length 3: 562921/4605316
length 4: 167131/1151329
```

For each length, record the primitive-rate/full-rate ratio. The anti-collapse
gate passes when every primitive target rate is at least one half of the
corresponding Stage I rate.

## Frozen conclusion rule

- `PROJECTIVE_QUOTIENT_ROBUST_HALF_EXCESS` if all four length gates and the anti-collapse gate pass;
- `PROJECTIVE_QUOTIENT_HALF_EXCESS_WITH_RATE_SHIFT` if all four length gates pass but anti-collapse fails;
- `SCALAR_MULTIPLICITY_DEPENDENT` if any length gate fails.

## Secondary diagnostics

Recorded but unable to alter the primary conclusion:

- complete centre profiles at each length;
- every individual-word contribution;
- primitive/full target-rate ratios;
- number and distribution of removed scalar representatives;
- reciprocal and complement-reversal symmetry.

## Interpretation boundary

A positive result would remove scalar-representation multiplicity as the simple
cause of the finite half excess. It would remain a result for the bounded
primitive `K=6` projective lattice and lengths 1–4, not an all-map or all-length
theorem. IEEE `NaN` remains outside the state space and no Riemann-hypothesis
claim is promoted.
