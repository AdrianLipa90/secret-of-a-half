# SOH C005 Completion / Weyl-Sequence Funnel v0.1

Status: **FRONTIER SHARPENING / PRIOR-ART CONSISTENT / RH OPEN**

## 1. Why finite nondegeneracy is not enough

Yoshida's framework distinguishes the smooth finite-energy space \(K(a)\)
from its completion \(\widehat{K(a)}\) in the Weil-form geometry.

The key prior-art facts are:

- the Weil Hermitian form is unconditionally nondegenerate on \(K(a)\) for
  every finite \(a>0\);
- RH is equivalent to nondegeneracy on the completed space
  \(\widehat{K(a)}\) for every \(a>0\).

Therefore no amount of checking only finitely represented vectors in
\(K(a)\) can by itself close RH.  The dangerous object is a completion mode:
a sequence of ordinary vectors whose limiting state exists in the completed
form space and becomes degenerate there.

This explains why repeated finite PSD/nondegeneracy tests can remain green
without resolving the theorem.

## 2. Correct obstruction language

The proof-bearing obstruction should be treated as an approximate-null or
Weyl-type sequence.

Schematic form:

\[
\|v_m\|=1,
\qquad
Q_W^a(v_m)\to0,
\]

with no strongly convergent nonzero limit available in the original finite
test-function space.

The task is therefore not merely

\[
Q_W^a(v)\ne0
\quad\text{for every explicitly represented }v.
\]

It is

\[
\boxed{
\inf_{\|v\|=1}Q_W^a(v)>0
}
\]

at the relevant scale, or another estimate strong enough to rule out a
completion null mode.

## 3. Yoshida high-mode coercivity funnels the obstruction

For every bounded scale interval \(0<a\le a_0\) and every requested
\(\nu>0\), Yoshida's finite-codimension argument, in Suzuki's formulation,
provides a sufficiently large Fourier cutoff so that the high-mode sector is
coercive.

Thus an approximate null sequence cannot escape freely to arbitrarily high
Fourier modes.

Write

\[
v=p+q,
\qquad
p=P_Nv,
\qquad
q=Q_Nv.
\]

On the high sector,

\[
A_{HH}\ge\nu I.
\]

If the low/high coupling is bounded, minimization over \(q\) gives the
effective finite Schur form

\[
\boxed{
S_a
=
A_{LL}-B A_{HH}^{-1}B^*.
}
\]

The infinite completion obstruction is thereby funneled into a finite
effective operator, but only after the infinite high block has been
eliminated with a genuine resolvent bound.

## 4. The real bottleneck

The missing statement is not "all finite matrices are nondegenerate."

It is the uniform effective gap

\[
\boxed{
\lambda_{\min}(S_a)>0
}
\]

with enough quantitative control that the bound survives:

- removal of the Fourier cutoff;
- the exact localized operator normalization;
- variation in \(a\);
- passage through bounded intervals;
- ultimately the all-scale continuation.

A scalar envelope is

\[
M=
\begin{pmatrix}
\mu&-\varepsilon\\
-\varepsilon&\nu
\end{pmatrix}.
\]

Its exact lower eigenvalue is

\[
\boxed{
\lambda_-
=
\frac{
\mu+\nu-
\sqrt{(\mu-\nu)^2+4\varepsilon^2}
}{2}.
}
\]

Strict Schur positivity

\[
\mu\nu-\varepsilon^2>0
\]

with \(\mu,\nu>0\) is equivalent to \(\lambda_->0\).

The code now computes this quantitative gap rather than recording only the
determinant margin.

## 5. Natural flow

The corrected pipeline is

\[
\text{Fourier scaling}
\to
\text{localized form join}
\to
\text{high-mode coercivity}
\to
\text{resolvent}
\to
\text{Schur operator}
\to
\boxed{\text{uniform effective gap}}
\to
\text{no completion null mode}.
\]

Only after this step should the pipeline branch to:

1. C005 spectral nondegeneracy / spectral-flow closure;
2. Suzuki deficiency-vector stability / zero attraction.

## 6. Practical implication

The next numerical or interval-arithmetic work should target the **effective
Schur gap as a function of \(a\)**, not raw principal-matrix eigenvalues.

A useful diagnostic is therefore

\[
a\mapsto
\lambda_{\min}\!\left(
A_{LL}(a)-B(a)A_{HH}(a)^{-1}B(a)^*
\right)
\]

with rigorously bounded high-mode inverse.

If this quantity approaches zero, the pipeline must expose where and why.
If it stays uniformly separated from zero on a certified interval, that
interval is genuinely closed for the nondegeneracy route.

## 7. Firewall

The existence of a positive finite-dimensional Schur diagnostic on sampled
values of \(a\) is not a proof.

Promotion requires interval/all-scale control and the exact operator-domain
crosswalk.

\`proof_of_rh = false\`
