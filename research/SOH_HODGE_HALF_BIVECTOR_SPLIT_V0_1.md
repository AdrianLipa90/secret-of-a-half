# Secret-of-a-Half: Hodge Half-Bivector Split v0.1

Status: CANDIDATE_CROSS_REPO_GEOMETRIC_HALF_REALIZATION / EXACT_PROJECTOR_ALGEBRA / RH_NOT_CLAIMED
Date: 2026-09-24

In four dimensions, two-forms form a six-dimensional space. Once an oriented Euclidean metric is fixed, the Hodge star obeys

\[
\star^2=1
\]

on two-forms, and therefore

\[
\boxed{P_+=\frac12(I+\star),\qquad P_-=\frac12(I-\star)}.
\]

The projectors obey

\[
P_\pm^2=P_\pm,\qquad P_+P_-=0,\qquad P_++P_-=I,
\]

and each has rank three:

\[
\Lambda^2=\Lambda^2_+\oplus\Lambda^2_-,
\qquad 6=3+3.
\]

Thus 1/2 is not inserted ad hoc in this geometric sector: it is forced by the spectral projectors of an involution.

Lorentzian firewall: on real Lorentzian two-forms \(\star^2=-1\), so the real formula above is not a real ±1 eigenspace decomposition. After complexification one uses the corresponding ±i eigenspace projectors. Signature must be explicit.

Cross-repo role: TIR/PhaseNav may use this exact half split after a metric has been reconstructed from an admissible bivector B-field. This supplies a standard geometric realization of a half-projector and a 3+3 decomposition. It does not prove the Riemann Hypothesis and does not identify every project occurrence of 1/2 with Hodge duality.

Relation to the existing half-bifurcation candidate:

\[
T(x)=2x+1
\]

and

\[
P_\pm=\frac12(I\pm\star)
\]

are independent exact appearances of a half structure. Their coexistence is recorded as a crosswalk only; no theorem identifying the affine and Hodge mechanisms is asserted.

Promotion ledger:
- projector normalization 1/2: PASS EXACT/STANDARD
- rank 3+3 split in oriented Euclidean 4D: PASS STANDARD
- Lorentzian complexification firewall: PASS
- identification with Stella Octangula dual tetrahedra: CANDIDATE CROSSWALK
- identification with affine half-bifurcation algebra: OPEN CROSSWALK
- RH closure from this split: NOT IMPLIED


## Parity exchanges the half sectors

The antipodal tetrahedral layer acts on the four-vector carrier as spatial parity

\[
P=\operatorname{diag}(1,-1,-1,-1).
\]

Its exterior-square action in the ordered bivector basis
\((01,02,03,23,31,12)\) is

\[
\boxed{
K=C_2(P)=\operatorname{diag}(-I_3,+I_3).
}
\]

For the Euclidean Hodge matrix \(\star\) used by the exact half projectors,

\[
\boxed{
K\star=-\star K.
}
\]

Hence

\[
\boxed{
K P_+=P_-K,
\qquad
K P_-=P_+K.
}
\]

So orientation-reversing spatial parity exchanges the self-dual and anti-self-dual three-dimensional sectors.

This gives a precise project-level phase/antiphase crosswalk:

\[
3_+\leftrightarrow3_-.
\]

It does not identify the two sectors with matter/antimatter, chirality, or any physical field without an additional theorem.

In Lorentzian signature the analogous statement is formulated on the complexified \(\pm i\) Hodge eigenspaces; the real Euclidean projector formula is not silently reused.
