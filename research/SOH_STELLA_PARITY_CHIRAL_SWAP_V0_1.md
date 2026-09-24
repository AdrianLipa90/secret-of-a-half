# Secret-of-a-Half: Stella Parity / Chiral Half-Sector Swap v0.1

Status: CANDIDATE_EXACT_GEOMETRIC_CROSSWALK / RH_NOT_CLAIMED
Date: 2026-09-24

## 1. Input from the tetrahedral null-frame bridge

For the exact TIR Stella parity seed, the 4D relative frame is

\[
P=\operatorname{diag}(1,-1,-1,-1).
\]

On the ordered two-form basis

\[
(01,02,03,23,31,12),
\]

its exterior-square image is

\[
\boxed{
D=\Lambda^2 P
=
\operatorname{diag}(-1,-1,-1,+1,+1,+1).
}
\]

Thus parity separates the six bivector channels into an exact \(3+3\) sign split.

## 2. Euclidean Hodge half-projectors

On an oriented Euclidean 4D two-form carrier, use

\[
\star^2=I.
\]

In the same pair basis the standard Hodge matrix may be written

\[
\star=
\begin{pmatrix}
0&I_3\\
I_3&0
\end{pmatrix}.
\]

Then

\[
\boxed{
P_+=\frac12(I+\star),
\qquad
P_-=\frac12(I-\star).
}
\]

Each projector has rank three.

## 3. Exact parity swap

The Stella parity bivector operator anticommutes with the Hodge star:

\[
\boxed{
D\star D=-\star.
}
\]

Therefore

\[
\boxed{
DP_+D=P_-,
\qquad
DP_-D=P_+.
}
\]

So the two half-projector sectors are exchanged exactly by orientation reversal.

The factor \(1/2\) is forced by projector algebra. It is not fitted.

## 4. Lorentzian firewall

For Lorentzian signature on real two-forms,

\[
\star^2=-I.
\]

The real Euclidean \(\pm1\) split must not be copied unchanged. After complexification one uses the \(\star=\pm i\) chiral sectors. Spatial parity reverses orientation and exchanges those two complex chiral sectors.

## 5. Relation to other half structures

This gives an independent exact geometric occurrence of a half decomposition:

\[
6=3+3,
\qquad
P_\pm=\frac12(I\pm\star).
\]

It is distinct from:

- the affine half-bifurcation seed \(x=\pm1/2\) under \(T(x)=2x+1\);
- the exchange-fixed probability coordinate \(u=1/2\);
- the tetrahedral face holonomy fraction \(q_3=1/2\);
- the Riemann critical-line coordinate \(\Re s=1/2\).

Any theorem identifying these mechanisms must be proved separately.

## 6. Promotion ledger

- Stella parity bivector sign split \(3+3\): PASS EXACT
- Euclidean Hodge half-projectors: PASS STANDARD/EXACT
- parity anticommutes with Hodge star: PASS EXACT
- parity swaps \(P_+\leftrightarrow P_-\): PASS EXACT
- Lorentzian complex chiral swap: PASS STANDARD CROSSWALK
- identification with affine half-bifurcation: OPEN
- identification with zeta functional-equation half axis: OPEN
- RH proof from this result: NOT IMPLIED
