# DHSE-001 — Stage K preregistration: reciprocal-invariant measure robustness

## Status before execution

- Branch: `experiment/dhse-001` only.
- No Stage K weighted centre census or conclusion is recorded here.
- No merge, pull request, monograph inclusion or claim promotion is authorized.

## Scientific question

Does the projective half excess survive several exact, reciprocal-invariant
measures on the primitive `K=6` Möbius universe, rather than only the uniform
counting measure?

## Frozen operator universe

- the `952` primitive representatives from Stage J;
- `gcd(a,b,c,d)=1`;
- `1 <= a,d <= 6`, `0 <= b,c <= 6`, `ad-bc>0`;
- exact reciprocal closure under `[a,b,c,d] -> [d,c,b,a]`.

## Frozen map weights

For each primitive matrix `M=[a,b,c,d]`, with `Delta=ad-bc`, declare six
positive integer weights:

1. `uniform(M) = 1`;
2. `determinant(M) = Delta`;
3. `determinant_squared(M) = Delta^2`;
4. `coefficient_sum(M) = a+b+c+d`;
5. `boundary_taper(M) = 7-max(a,b,c,d)`;
6. `low_determinant_taper(M) = 37-Delta`.

Every weight is strictly positive on the declared universe and invariant under
reciprocal conjugation.

For an ordered pair `(L,R)`, the pair weight is `w(L)w(R)`. Every word of a
declared length receives the same unit word weight. No measure is modified or
renormalized after the centre census.

## Frozen word lengths, centres and radius

- complete word sets of lengths `2` and `4`;
- centres `1/16,1/8,1/4,1/2,1,2,4,8,16`;
- target `q=1`, equivalent to `p=1/2`;
- projective radius `1/10`;
- exact whole-positive-line forcing predicate from Stages F–J.

Lengths 2 and 4 test the original finite census and the longest fully audited
word set while limiting only duplicated intermediate computation, not the
operator or centre universe.

## Weighted rate

For each measure and length:

`weighted_rate(q) = weighted_forcing_mass(q) / [2^length * (sum_M w(M))^2]`.

The denominator is independent of the centre.

## Primary gate

A measure-length cell passes when:

1. `q=1` has strictly greatest weighted forcing mass;
2. its mass is at least `5/4` of the median of the eight weighted control masses;
3. reciprocal centre pairs have exactly equal weighted masses.

## Frozen anti-collapse gate

The uniform primitive Stage J target rates are fixed as:

```text
length 2: 157345/1812608
length 4: 554809/3625216
```

For each weighted measure and length, the weighted target rate must be at least
one quarter of the corresponding uniform primitive rate.

## Frozen conclusion rule

- `MEASURE_ROBUST_HALF_EXCESS` if every one of the 12 measure-length cells and every anti-collapse comparison pass;
- `RANK_ROBUST_RATE_SENSITIVE` if all primary cells pass but at least one anti-collapse comparison fails;
- `MEASURE_DEPENDENT_HALF_EXCESS` if any primary cell fails.

## Secondary diagnostics

Recorded but unable to alter the conclusion:

- total map weight and pair-word mass for each measure;
- complete weighted centre profiles;
- weighted target rates and ratios to uniform;
- word-by-word weighted contributions;
- reciprocal-conjugacy weight audit.

## Interpretation boundary

A positive result would establish robustness across the six declared symmetric
integer measures, not across every possible measure on projective operators.
The coefficient bound, word lengths and projective radius remain finite and
fixed. IEEE `NaN` remains outside the state space and no Riemann-hypothesis
claim is promoted.
