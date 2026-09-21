# SOH Collatz–Riemann radial selector v0.1

Status: **EXACT ALGEBRA / LEAN-FORMALIZED REDUCTION / RH OPEN**

## 1. Projective coordinate

Use

[
u=Omega(s)=rac{s}{1-s}.
]

The Riemann critical line is exactly

[
Re(s)=rac12
quadLongleftrightarrowquad
|u|=1.
]

Thus the horizontal RH defect becomes a radial projective defect.

## 2. Canonical Collatz conjugacy

The half Möbius branch

[
H(s)=rac{s}{2-s}
]

satisfies

[
Omega(H(s))=rac{Omega(s)}2.
]

If one conjugates the literal Collatz odd map (umapsto3u+1) back through
(Omega), the corresponding (s)-plane Möbius branch is

[
oxed{
O_C(s)=rac{2s+1}{s+2}
}
]

and

[
oxed{
Omega(O_C(s))=3Omega(s)+1.
}
]

Therefore (Omega) is an exact conjugacy between the declared Möbius pair and
the standard affine Collatz pair

[
umapstorac u2,
qquad
umapsto3u+1.
]

This is an algebraic identity, not an empirical analogy.

## 3. Accelerated RL selector

Define the accelerated odd step

[
R(u)=rac{3u+1}{2}
]

and then apply one further halving step

[
L(u)=rac u2.
]

The left-to-right word (RL) is

[
W(u)=L(R(u))=rac{3u+1}{4}.
]

It obeys

[
oxed{
W(u)-1=rac34(u-1)
}
]

and hence has the unique fixed point

[
oxed{u=1}.
]

This is the exact Stage-D Collatz-derived contraction mechanism, now placed in
the Riemann projective coordinate.

## 4. Radial selector

For the physical/projective radius

[
q(s)=|Omega(s)|ge0,
]

use the same real affine selector

[
W_r(q)=rac{3q+1}{4}.
]

Then

[
W_r(q)-1=rac34(q-1)
]

and

[
oxed{
W_r(q)=qiff q=1.
}
]

Combining with the projective critical-line identity gives

[
oxed{
W_r(|Omega(s)|)=|Omega(s)|
iff
Re(s)=rac12.
}
]

## 5. Exact RH-equivalent dynamic condition

Define the statement that every non-trivial zeta zero is radially fixed by
(W_r):

[
zeta(s)=0, s	ext{ non-trivial}
Longrightarrow
W_r(|Omega(s)|)=|Omega(s)|.
]

Lean proves that this statement is equivalent to mathlib's literal
`RiemannHypothesis`.

Therefore the Collatz selector is a valid exact reformulation of the missing
zero-confinement edge, but it is **not yet an independent proof**.

The remaining incoming theorem is:

[
oxed{
	ext{zeta/arithmetic structure}
Longrightarrow
	ext{radial Collatz fixedness of every non-trivial zero}.
}
]

That implication must be derived without importing RH-equivalent positivity,
zero locations, or the fixedness condition itself.

## 6. Why this is still useful

The reduction replaces the geometric target (Re(s)=1/2) by a dynamical
fixed-point target on one positive scalar:

[
qmapstorac{3q+1}{4}.
]

This interfaces naturally with the existing Weil/spectral programme because a
proof may now seek an independently derived contraction, stationarity,
nondegeneracy or variational law for the radial defect (q-1), rather than
re-proving the critical-line geometry.

## 7. Lean provenance

Formal file:

`SecretOfAHalfFormal/CollatzConjugacy.lean`

The formal branch also contains the exact seam equivalence, symmetry-only
no-go witness, C005 scalar Schur certificate, two-channel cancellation no-go
and spectral-flow lemma.

`proof_of_rh = false`
