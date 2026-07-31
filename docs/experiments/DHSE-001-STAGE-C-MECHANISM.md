# DHSE-001 — Stage C mechanism diagnosis

## Result

The only Stage B family that passed the target-occupancy gate,
`mobius_skew`, is completely explained by a two-step operator word. The signal
is an operator-family artifact, not independent evidence for a universal
halfway attractor.

Technical status: **PASS**.
Scientific status: **OPERATOR_WORD_ARTIFACT_IDENTIFIED**.

## Operator pair

The Stage B Möbius-skew maps are

\[
L(z)=\frac{z+1}{2z+3},
\qquad
R(z)=\frac{3z+1}{z+2}.
\]

Applying `L` and then `R` gives

\[
R(L(z))
=
\frac{5z+6}{5z+7}.
\]

For every positive projective odds coordinate `z>0`,

\[
\frac67 < R(L(z)) < 1.
\]

The Stage B target residual around `q=1` was

\[
d_1(w)=\frac{|w-1|}{w+1}.
\]

Since `R(L(z))<1`, direct substitution gives

\[
d_1(R(L(z)))
=
\frac{1}{10z+13}
<
\frac1{13}
<
\frac1{10}.
\]

Therefore every `LR` word necessarily produces a Stage B target hit,
independently of the incoming positive state.

## Exact audit

Across the frozen Stage B ensemble:

- observed post-burn-in states: `20,544`;
- target hits around `q=1`: `5,147`;
- preceding `LR` words: `5,147`;
- states satisfying `target_hit iff preceding_word_is_LR`: `20,544`;
- counterexamples: `0`.

Thus the observed target occupancy is exactly the frequency of the deterministic
branch word `LR` in the declared window.

## Consequence

Stage B already failed the robust-family criterion. Stage C strengthens that
negative interpretation: the one apparent positive family is not unexplained.
Its signal follows algebraically from the chosen pair of Möbius maps and the
preregistered radius.

This leaves the exact geometric role of `1/2` intact as the complement fixed
point, reciprocal self-dual point and Fisher–Rao midpoint. It removes the
present evidence for the stronger claim that unrelated deterministic dynamics
spontaneously select the half.

## Reproduction

```bash
python scripts/run_dhse_001_stage_c.py
python -m pytest -q tests/test_dhse_001_stage_c.py
```

No merge, monograph promotion or claim promotion is authorized.
