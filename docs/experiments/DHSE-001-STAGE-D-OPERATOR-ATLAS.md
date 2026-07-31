# DHSE-001 — Stage D exact operator-geometry atlas

## Decision

- Technical status: **PASS**.
- Scientific status: **OPERATOR_LOCAL_MECHANISMS_IDENTIFIED**.
- Global conclusion: **NO_OPERATOR_INDEPENDENT_HALF_SELECTION**.
- No new stochastic target statistic was introduced.
- No merge, monograph inclusion or claim promotion is authorized.

Stage D classifies the four non-calibration Stage B families by exact integer
matrix composition. The finite word census covers every `L/R` word through
length 8. Separate algebraic arguments are stated when they apply beyond that
finite census.

## Frozen target ball

The Stage B residual around the self-dual odds coordinate `q=1` was

\[
d_1(z)=\frac{|z-1|}{z+1}.
\]

The frozen condition `d_1(z) <= 1/10` is exactly

\[
\frac9{11}\le z\le\frac{11}{9}.
\]

This interval, not a newly selected radius, is used throughout Stage D.

## 1. Affine-skew family

\[
L(z)=\frac{2z+1}{3},
\qquad
R(z)=\frac{3z+2}{2}.
\]

The left branch fixes `q=1` and contracts deviations by `2/3`:

\[
L(z)-1=\frac23(z-1),
\qquad
L^n(z)=1+\left(\frac23\right)^n(z-1).
\]

Moreover, `R(z)>1` for every `z>0`, while both `L` and `R` preserve the strict
half-line `z>1`. Therefore any word containing `R` cannot map `q=1` back to
itself. The only finite fixed words are the powers `L^n`.

This is branch-local attraction, not universal forcing: every finite affine
word has positive slope and an unbounded image, so no word maps the entire
positive line into the bounded target interval.

## 2. Möbius-skew family

\[
L(z)=\frac{z+1}{2z+3},
\qquad
R(z)=\frac{3z+1}{z+2}.
\]

The individual branches map the positive line into bounded intervals:

\[
L((0,\infty))=\left(\frac13,\frac12\right),
\qquad
R((0,\infty))=\left(\frac12,3\right).
\]

The minimal forcing word is `LR`, applied left to right:

\[
R(L(z))=\frac{5z+6}{5z+7}
\in\left(\frac67,1\right)
\subset\left[\frac9{11},\frac{11}{9}\right].
\]

Consequently every word whose final two letters are `LR` forces the target
ball, regardless of the incoming positive state. The exact finite census gives
`2^(n-2)` forcing words at every length `n=2,...,8`, precisely the words ending
in `LR`.

No word through length 8 fixes `q=1`; the Stage B signal was produced by a
forcing image interval, not by a fixed point.

## 3. Scale–translate family

\[
L(z)=2z,
\qquad
R(z)=z+3.
\]

Both branches strictly increase every positive state. Any infinite branch
sequence diverges to `+infinity`: if `R` occurs infinitely often, its additive
increments are unbounded; if it occurs only finitely often, the tail consists
of repeated doublings.

There is no finite `q=1` fixed word and no universal target-forcing word. This
explains the absence of post-burn-in target occupancy in Stage B as monotone
escape rather than a failed numerical detector.

## 4. Collatz-derived stream family

\[
L(z)=\frac z2,
\qquad
R(z)=\frac{3z+1}{2}.
\]

The minimal fixed word is `RL`, meaning first `R`, then `L`:

\[
L(R(z))=\frac{3z+1}{4}
=1+\frac34(z-1).
\]

Thus repeated `RL` blocks contract to the self-dual coordinate:

\[
(L\circ R)^n(z)
=1+\left(\frac34\right)^n(z-1).
\]

This mechanism is weaker than Möbius forcing. Every finite Collatz-derived word
has positive affine slope and hence unbounded image, so no finite word can map
the entire positive line into the bounded target interval. The census through
length 8 finds only `(RL)^k` as fixed words at even lengths and no universal
forcing word.

This explains why Stage B showed enhanced but non-dominant occupancy near
`q=1`: the stream contains contracting `RL` motifs, but they do not erase the
incoming-state scale in one finite step.

## Mechanism table

| Family | Minimal mechanism at `q=1` | Type | Universal target forcing? |
|---|---|---|---|
| affine skew | `L` | branch fixed point, multiplier `2/3` | no |
| Möbius skew | `LR` | whole-line image forcing | yes |
| scale–translate | none | monotone escape | no |
| Collatz-derived | `RL` | word fixed point, multiplier `3/4` | no |

## Scientific consequence

The four families do not share a common halfway-selection mechanism. Three
qualitatively different local structures appear:

1. branch-local contraction;
2. finite-word whole-line forcing;
3. finite-word contraction;

and the fourth family escapes every finite centre.

Therefore the Stage B family dependence is now explained by operator algebra.
The experiment preserves the exact geometric facts that `p=1/2` is the
complement fixed point, reciprocal self-dual point and Fisher–Rao midpoint, but
it supplies no evidence for an operator-independent dynamical law selecting
one half.

## Reproduction

```bash
python scripts/run_dhse_001_stage_d.py
python -m pytest -q tests/test_dhse_001_stage_d.py
```

The deterministic receipt is stored at
`data/processed/dhse_001_stage_d_receipt.json`.
