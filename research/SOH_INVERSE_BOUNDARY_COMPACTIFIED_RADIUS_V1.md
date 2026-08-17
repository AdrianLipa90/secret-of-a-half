# The Secret of a Half — Compactified Inverse-Boundary Geometry

**Status:** EXACT GEOMETRIC REDUCTION; RH BRIDGE REMAINS OPEN  
**Scope:** global projective geometry only; no Hermite finite-section assumptions  
**Date:** 17 August 2026

## 1. Canonical inverse-boundary coordinate

Define

\[
\Omega(s)=\frac{s}{1-s},\qquad s\neq 1.
\]

On the Riemann sphere,

\[
\Omega(0)=0,\qquad \Omega(1)=\infty.
\]

Thus the two real strip boundaries are represented by the projective pair

\[
0\longleftrightarrow \infty.
\]

For the anti-linear critical reflection

\[
K(s)=1-\overline{s},
\]

one has the exact conjugacy

\[
\Omega(K(s))=\frac{1}{\overline{\Omega(s)}}.
\]

Hence radial inversion is

\[
R\mapsto R^{-1},\qquad R:=|\Omega(s)|.
\]

## 2. Zero-centred compactification with infinity on the outer boundary

Compactify the projective radius by

\[
q(s):=\frac{R}{1+R}=\frac{|\Omega(s)|}{1+|\Omega(s)|}.
\]

Then

\[
R=0\iff q=0,
\qquad
R=\infty\iff q=1.
\]

Therefore the compactified radial interval is exactly

\[
[0,\infty]\longrightarrow[0,1],
\]

with zero at the centre-side endpoint and infinity at the outer boundary.

Under reciprocal inversion,

\[
R\mapsto R^{-1},
\]

we obtain

\[
q\mapsto\frac{R^{-1}}{1+R^{-1}}=\frac{1}{1+R}=1-q.
\]

So the projective inversion becomes the ordinary complement involution

\[
\boxed{q\mapsto 1-q}.
\]

Its unique fixed point is

\[
\boxed{q=\frac12}.
\]

Since

\[
q=\frac12
\iff R=1
\iff |\Omega(s)|=1
\iff \Re s=\frac12,
\]

we obtain the exact theorem:

> **Compactified inverse-boundary half-axis theorem.**  
> The Möbius coordinate \(\Omega(s)=s/(1-s)\), followed by radial compactification \(q=|\Omega|/(1+|\Omega|)\), sends the reciprocal boundary pair \(0\leftrightarrow\infty\) to \(0\leftrightarrow1\), converts inversion into \(q\mapsto1-q\), and makes the Riemann critical line exactly the unique self-dual radial layer \(q=1/2\).

No zeta-zero assumption is used.

## 3. Signed centred radius

Define

\[
\eta(s):=2q(s)-1=\frac{R-1}{R+1}.
\]

Then

\[
-1\le \eta\le 1,
\]

with

\[
R=0\mapsto\eta=-1,
\qquad
R=1\mapsto\eta=0,
\qquad
R=\infty\mapsto\eta=+1.
\]

Reciprocal inversion gives

\[
\boxed{\eta\mapsto-\eta}.
\]

Moreover, with

\[
B(s)=\log R=\log|\Omega(s)|,
\]

we have the exact identity

\[
\boxed{\eta(s)=\tanh\!\left(\frac{B(s)}{2}\right)}.
\]

Thus the previous logarithmic imbalance \(B\), the compactified radius \(q\), and the centred defect \(\eta\) are equivalent global coordinates:

\[
B=0\iff \eta=0\iff q=\frac12\iff \Re s=\frac12.
\]

## 4. Completed zeta in this geometry

Let

\[
X(u):=\xi\!\left(\frac{u}{1+u}\right),
\qquad u=\Omega(s).
\]

The functional equation and conjugation imply reciprocal-conjugate zero orbits. The Riemann Hypothesis becomes exactly

\[
\boxed{
X(u)=0\Longrightarrow |u|=1
}
\]

or, equivalently,

\[
\boxed{
X(u)=0\Longrightarrow q(u)=\frac12
}
\]

or

\[
\boxed{
X(u)=0\Longrightarrow \eta(u)=0.
}
\]

This is the entire remaining global bridge.

## 5. Proof-target minimisation

The following facts are already exact and must not be re-opened as separate numerical problems:

1. \(0\leftrightarrow\infty\) is the projective boundary pair.
2. Reciprocal inversion is the canonical boundary involution.
3. After compactification, inversion is exactly \(q\mapsto1-q\).
4. The unique self-dual layer is \(q=1/2\).
5. That layer is exactly \(\Re s=1/2\).
6. The Li coordinate is the negative inverse \(z_L=-1/\Omega\), so the same radial self-duality is preserved in Li's criterion.

Therefore the proof frontier is reduced to one analytic statement:

\[
\boxed{
\text{SOH-G001:}\quad X(u)=0\Longrightarrow q(u)=\frac12.
}
\]

Equivalently,

\[
X(u)=0\Longrightarrow B(u)=0,
\]

or

\[
X(u)=0\Longrightarrow \eta(u)=0.
\]

No further finite-Hermite, moving-boundary, or prime-tail condition is logically required to state the target. Such machinery may be retained only as auxiliary evidence if it directly establishes SOH-G001.

## 6. Epistemic boundary

**EXACT:** all coordinate identities and involution/fixed-locus statements above.

**OPEN:** SOH-G001, i.e. the implication from transformed zeta zerohood to the unique self-dual radial layer.

**NOT CLAIMED:** this note alone does not prove RH. It removes avoidable auxiliary subproblems and isolates the single analytic implication that a proof must establish.
