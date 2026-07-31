# DHSE-001 — Stage D analytical scope lock

## Status

- Branch: `experiment/dhse-001` only.
- Analytical stage; no new stochastic target statistic is authorized here.
- No merge, monograph inclusion or claim promotion is authorized.

## Purpose

Stage C explained the only positive Stage B family by an exact two-letter
operator word. Stage D generalizes that diagnosis to all four experimental
families before any further numerical test is considered.

The stage asks:

1. Which branch maps or finite branch words fix the self-dual odds coordinate
   `q=1`, equivalent to `p=1/2`?
2. Which such fixed words are locally contracting?
3. Which finite words map the entire positive projective line into the frozen
   Stage B target ball?
4. Which families possess bounded trapping geometry, branch-local attraction,
   word-local attraction or monotone escape?

## Frozen mathematical objects

The positive projective state is `z>0`. Every branch map is represented by an
integer matrix

```text
[a b]
[c d]
```

acting as

```text
z -> (a*z+b)/(c*z+d).
```

Sequential word composition is exact integer matrix multiplication. All
reported derivatives and image endpoints use rational arithmetic.

The frozen Stage B residual ball around `q=1` is

```text
|z-1|/(z+1) <= 1/10,
```

which is exactly the interval

```text
[9/11, 11/9].
```

## Frozen finite-word census

- Alphabet: `L`, `R`.
- Word order: letters are applied from left to right.
- Maximum census length: `8`.
- A `q=1` fixed word satisfies `F(1)=1` exactly.
- It is contracting when `|F'(1)|<1`.
- A universal forcing word maps every `z>0` into `[9/11,11/9]`.
- Minimal words are reported by shortest length, then lexicographic order.

Finite census statements remain explicitly bounded by length 8 unless a
separate algebraic proof removes that bound.

## Interpretation boundary

Finding a fixed or forcing word at `q=1` identifies a mechanism internal to the
chosen operator algebra. It is not independent evidence that unrelated
dynamics prefer one half, and it does not order IEEE `NaN` with zero.
