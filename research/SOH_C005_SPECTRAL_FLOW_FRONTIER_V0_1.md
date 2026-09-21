# SOH-C005 Spectral-Flow Frontier v0.1

Status: **EXACT TOPOLOGICAL REDUCTION / VERIFIED EXTERNAL OPERATOR INPUT / RH OPEN**

## 1. Verified external operator facts

Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096v2
(19 August 2026), states unconditionally:

1. for every \(a>0\), the localized Weil form \(Q_W^a\) is represented by a
   self-adjoint lower-bounded operator \(A_a\);
2. the bottom of the spectrum
   \[
   \lambda_a=\inf_{0\ne v}\frac{Q_W^a(v)}{\|v\|_2^2}
   \]
   is an eigenvalue;
3. \(a\mapsto\lambda_a\) is continuous (Theorem 1.3);
4. \(\lambda_a>0\) for sufficiently small \(a>0\), using Yoshida's local
   positivity;
5. failure of RH is equivalent to \(\lambda_a<0\) for some \(a>0\), hence by
   continuity failure of RH forces a degeneracy \(\lambda_{a_*}=0\) at an
   intermediate scale.

Suzuki explicitly identifies this as another proof of Yoshida's equivalence:
RH is equivalent to nondegeneracy of the localized Weil form for every
positive scale.

These facts are prior art and are not claimed as new project theorems.

## 2. Lean closure of the purely topological step

SecretOfAHalfFormal/SpectralFlow.lean proves, without any zeta-specific
axiom, the generic statement

\[
\operatorname{Continuous}(\lambda)
\land
\lambda(a_0)>0
\land
(\forall a>0,\ \lambda(a)\ne0)
\Longrightarrow
(\forall a>0,\ \lambda(a)>0).
\]

It also proves the corresponding equivalence between positivity and
nondegeneracy under the continuity + positive-anchor hypotheses.

This isolates the spectral-flow logic from the arithmetic content.

## 3. Exact remaining RH edge in this route

After importing Suzuki/Yoshida only as external mathematical input, the
remaining problem is not continuity. It is

\[
\boxed{\lambda_a\ne0\quad\text{for every }a>0.}
\]

Equivalently, there is no nonzero vector \(v\) in the localized form domain
with

\[
Q_W^a(v)=0.
\]

This statement is RH-equivalent. Therefore it cannot be used as an assumed
"gluing condition", gauge constraint, self-duality condition, or hidden
boundary axiom.

## 4. Finite-codimension reduction

Yoshida's finite-codimension coercivity, as restated by Suzuki (2023,
Section 4.2), says that for every fixed \(a_0>0\) and every \(\mu>0\), a
Fourier cutoff \(N\) can be chosen so that the high-mode subspace is
uniformly coercive for all \(0<a\le a_0\).

Thus on every bounded scale interval a possible null direction is forced into
a finite low-frequency sector after a high-mode Schur complement.

Schematically,

\[
A_a=
\begin{pmatrix}
A_{LL}(a) & B(a)\\
B(a)^* & A_{HH}(a)
\end{pmatrix},
\qquad
A_{HH}(a)\ge\nu I,\quad \nu>0.
\]

A zero mode is then controlled by the finite Schur operator

\[
S_a=A_{LL}(a)-B(a)A_{HH}(a)^{-1}B(a)^*.
\]

Therefore an admissible non-circular target is

\[
\boxed{S_a>0\quad\text{for every }a>0.}
\]

The scalar sufficient terminus is already formalized in
SecretOfAHalfFormal/C005Block.lean.

## 5. Explicit high-mode schedule already exposed

The Yoshida/Suzuki integration-by-parts estimate gives, for the Fourier tail,

\[
S_N=\sum_{|n|>N}\frac1{(\pi n)^2}\le\frac{2}{\pi^2N},
\]

and hence the integrated low-frequency leakage is bounded by

\[
R_N(a)\le
\frac{8a}{\pi^2N}
\left(
t_0+a t_0^2+\frac{a^2t_0^3}{3}
\right).
\]

For \(0<a\le a_0\),

\[
R_N(a)\le\frac{B(a_0,t_0)}{N}.
\]

Thus the high-mode leakage schedule is computable once the exact constants of
the localized operator normalization are frozen.

## 6. Gauge/quotient firewall

The representation-invariance principle used elsewhere in the project must
not be used to quotient away a null vector of \(Q_W^a\).

A basis change, phase convention, or coordinate gauge can be quotiented.
A genuine vector \(v\ne0\) satisfying

\[
Q_W^a(v)=0
\]

is a spectral statement. Declaring it "gauge" would assume away the precise
obstruction whose exclusion is equivalent to RH.

## 7. Next proof-bearing target

The next useful target is not another RH-equivalent reformulation.

For each bounded \(0<a\le a_0\):

1. freeze the exact repository-to-Suzuki normalization;
2. make the Yoshida high-mode coercivity constant explicit;
3. construct the finite low-mode Schur matrix \(S_{N,a}\);
4. derive a rigorous lower bound
   \[
   \lambda_{\min}(S_{N,a})>0
   \]
   uniformly over the whole interval in \(a\);
5. provide an all-scale continuation/schedule as \(a_0\to\infty\).

Only Step 4+5 can supply the missing incoming edge.

## 8. Current verdict

\[
\boxed{\text{continuity: CLOSED externally}}
\]

\[
\boxed{\text{small-}a\text{ positivity: CLOSED externally}}
\]

\[
\boxed{\text{high-mode finite-codimension coercivity: CLOSED externally}}
\]

\[
\boxed{\text{spectral-flow topology: LEAN-CLOSED}}
\]

\[
\boxed{\text{global exclusion of }\lambda_a=0: \text{OPEN / RH-EQUIVALENT}}
\]

proof_of_rh = false
