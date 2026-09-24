# Secret-of-a-Half: Tetrahedral Parity Half-Projectors v0.1

Status: EXACT_PROJECTOR_CROSSWALK / CANDIDATE_INTERPRETATION / RH_NOT_CLAIMED  
Date: 2026-09-24

The TIR tetrahedral null-frame construction supplies two antipodal four-frames

\[
E_-=PE_+,
\qquad
P=\operatorname{diag}(1,-1,-1,-1).
\]

On the six-dimensional bivector carrier,

\[
\Pi=C_2(P)
=
\operatorname{diag}(-1,-1,-1,+1,+1,+1),
\]

so

\[
\boxed{\Pi^2=I}.
\]

The spectral projectors of this involution are forced to be

\[
\boxed{
Q_+=\frac12(I+\Pi),
\qquad
Q_-=\frac12(I-\Pi).
}
\]

They obey

\[
Q_\pm^2=Q_\pm,
\qquad
Q_+Q_-=0,
\qquad
Q_++Q_-=I,
\]

with

\[
\operatorname{rank}Q_+
=
\operatorname{rank}Q_-
=
3.
\]

Thus

\[
\boxed{6=3+3}
\]

and the factor \(1/2\) is theorem-level projector normalization, not a fitted coefficient.

For the two nonzero antipodal bivector frames

\[
B_-=\Pi B_+,
\]

one gets

\[
\boxed{
\frac{B_++B_-}{2}=Q_+B_+,
}
\]

\[
\boxed{
\frac{B_+-B_-}{2}=Q_-B_+.
}
\]

Therefore each half-overlay annihilates one complete rank-three sector while retaining the complementary sector.

This is an exact instance of

\[
\text{nonzero parents}
\to
\text{half-sum / half-difference}
\to
\text{sector-selective zero}.
\]

It is distinct from the Hodge half-projectors and from the affine generator \(T(x)=2x+1\). The three mechanisms share an exact \(1/2\) normalization in different typed algebras but are not identified.

No Riemann-Hypothesis implication follows from this projector identity alone.


## Vector-level precursor: exact 1+3 split

Before taking the exterior square, the same parity involution acts on the four-dimensional tetrahedral null frame:

\[
P=\operatorname{diag}(1,-1,-1,-1),
\qquad P^2=I.
\]

Hence

\[
P_t=\frac12(I+P),
\qquad
P_s=\frac12(I-P)
\]

are exact complementary projectors with ranks one and three.

For the antipodal frames \(E_-=PE_+\),

\[
\boxed{
\frac{E_++E_-}{2}=P_tE_+
}
\]

has rank one, while

\[
\boxed{
\frac{E_+-E_-}{2}=P_sE_+
}
\]

has rank three.

Thus the parity construction gives the hierarchy

\[
\boxed{
4=1+3
\xrightarrow{\Lambda^2}
6=3+3.
}
\]

The half factor is forced twice by spectral projection. The physical reading of the 1D/3D sectors as time/space uses the separate TIR x IDT carrier binding and is not asserted by projector algebra alone.
