# SOH Relative-Metric Hermitian Pencil Stability v0.1

Status: **EXACT_FINITE_PERTURBATION_CERTIFICATE / MD004D TOOL**

Date: 2026-09-26

Parents:
- \`research/SOH_PRIME_AUTOCORRELATION_WEIL_POSITIVITY_DILEMMA_V0_1.md\`
- \`research/SOH_2026_FINITE_WEIL_POSITIVE_INTERTWINER_CROSSWALK_V0_1.md\`

## 1. Problem

Let

\[
K_0=K_0^*,
\qquad
G_0=G_0^*>0
\]

be a reference Hermitian definite pencil, and let

\[
K=K^*,
\qquad
G=G^*
\]

be a candidate arithmetic pencil on the same finite contrast space.

The generalized eigenvalues of

\[
Kv=\lambda Gv
\]

are the ordinary eigenvalues of

\[
A=G^{-1/2}KG^{-1/2}.
\]

We want a fail-closed certificate that turns relative metric and operator errors
into a spectral error bound.

## 2. Reference normalization

Define

\[
\widehat K_0
=
G_0^{-1/2}K_0G_0^{-1/2},
\]

\[
\Delta\widehat K
=
G_0^{-1/2}(K-K_0)G_0^{-1/2},
\]

and

\[
E
=
G_0^{-1/2}(G-G_0)G_0^{-1/2}.
\]

Put

\[
\epsilon_K=\|\Delta\widehat K\|,
\qquad
\delta_G=\|E\|.
\]

Assume

\[
\boxed{\delta_G<1.}
\]

Then

\[
G
=
G_0^{1/2}(I+E)G_0^{1/2}
\]

is positive definite automatically.

## 3. Candidate standardized operator

Let

\[
S=(I+E)^{-1/2}.
\]

The generalized spectrum of \((K,G)\) is the spectrum of

\[
\widetilde A
=
S(\widehat K_0+\Delta\widehat K)S.
\]

The reference generalized spectrum is the spectrum of

\[
A_0=\widehat K_0.
\]

Since the spectrum of \(I+E\) lies in

\[
[1-\delta_G,1+\delta_G],
\]

we have

\[
\|S\|
\le
(1-\delta_G)^{-1/2}.
\]

Also,

\[
\|S-I\|
\le
(1-\delta_G)^{-1/2}-1.
\]

## 4. Exact perturbation bound

Split

\[
\widetilde A-A_0
=
S\Delta\widehat K S
+
(SA_0S-A_0).
\]

The first term obeys

\[
\|S\Delta\widehat K S\|
\le
\frac{\epsilon_K}{1-\delta_G}.
\]

For the second,

\[
SA_0S-A_0
=
(S-I)A_0S
+
A_0(S-I),
\]

hence

\[
\|SA_0S-A_0\|
\le
\|S-I\|\|A_0\|(\|S\|+1).
\]

Let

\[
r=(1-\delta_G)^{-1/2}.
\]

Then

\[
(r-1)(r+1)=r^2-1
=
\frac{\delta_G}{1-\delta_G}.
\]

Therefore

\[
\boxed{
\|\widetilde A-A_0\|
\le
\frac{
\epsilon_K+\delta_G\|A_0\|
}{
1-\delta_G
}.
}
\]

Define

\[
\boxed{
\mathcal E_{\rm pencil}
=
\frac{
\epsilon_K+\delta_G\|\widehat K_0\|
}{
1-\delta_G
}.
}
\]

## 5. Generalized eigenvalue certificate

Order the generalized eigenvalues increasingly:

\[
\lambda_1^{(0)}\le\cdots\le\lambda_n^{(0)}
\]

for \((K_0,G_0)\), and

\[
\lambda_1\le\cdots\le\lambda_n
\]

for \((K,G)\).

Weyl's Hermitian perturbation theorem gives

\[
\boxed{
|\lambda_j-\lambda_j^{(0)}|
\le
\mathcal E_{\rm pencil}
\qquad
(j=1,\ldots,n).
}
\]

Thus the entire generalized spectrum is certified by two relative quantities:
- operator error \(\epsilon_K\);
- metric error \(\delta_G<1\).

## 6. Gap-preservation corollary

Suppose a reference eigenvalue is isolated by gap

\[
\operatorname{gap}_j
=
\min_{k\ne j}
|\lambda_j^{(0)}-\lambda_k^{(0)}|.
\]

If

\[
\boxed{
2\mathcal E_{\rm pencil}
<
\operatorname{gap}_j,
}
\]

then the corresponding candidate eigenvalue remains uniquely identifiable in
the interval

\[
[
\lambda_j^{(0)}-\mathcal E_{\rm pencil},
\lambda_j^{(0)}+\mathcal E_{\rm pencil}
].
\]

This turns a qualitative "relative perturbation theorem" into an executable
finite certificate.

## 7. Positive-metric firewall

The condition

\[
\delta_G<1
\]

is not cosmetic.

It proves

\[
I+E>0
\]

and hence

\[
G>0.
\]

If \(\delta_G\ge1\), the certificate fails closed. No generalized
positive-metric spectral conclusion is permitted.

Likewise, an absolute matrix difference

\[
\|G-G_0\|
\]

without normalization by \(G_0\) is not enough when the metric is ill
conditioned.

The correct quantity is the relative metric distortion

\[
\boxed{
\|G_0^{-1/2}(G-G_0)G_0^{-1/2}\|.
}
\]

## 8. Relation to MD004D

This theorem does not supply the target pencil.

It supplies the exact certificate a zero-list-free positive intertwiner must
eventually satisfy.

A valid MD004D construction may use a target pencil only if that target is
itself obtained without supplying the zeta ordinates as inputs.

If the target pencil is constructed from a zero table, the theorem is a
validation/reconstruction certificate only, not a proof.

## 9. Prime-to-zero perturbation target

For a zero-list-free target pair

\[
(K_N^\zeta,G_N^\zeta)
\]

and arithmetic pair

\[
(K_N^{\rm p},G_N^{\rm p}),
\]

define

\[
\delta_{G,N}
=
\left\|
(G_N^\zeta)^{-1/2}
(G_N^{\rm p}-G_N^\zeta)
(G_N^\zeta)^{-1/2}
\right\|,
\]

\[
\epsilon_{K,N}
=
\left\|
(G_N^\zeta)^{-1/2}
(K_N^{\rm p}-K_N^\zeta)
(G_N^\zeta)^{-1/2}
\right\|.
\]

A sufficient finite-to-infinite route is

\[
\boxed{
\delta_{G,N}<1
}
\]

eventually and

\[
\boxed{
\frac{
\epsilon_{K,N}
+
\delta_{G,N}
\|
(G_N^\zeta)^{-1/2}
K_N^\zeta
(G_N^\zeta)^{-1/2}
\|
}{
1-\delta_{G,N}
}
\to0.
}
\]

Then the generalized spectra converge uniformly at each finite rank ordering,
subject to the usual compatibility required for the infinite limit.

## 10. Compact theorem

### Theorem — relative-metric pencil stability

For Hermitian \(K_0,K\), positive definite \(G_0\), and Hermitian \(G\), if

\[
\delta_G
=
\|G_0^{-1/2}(G-G_0)G_0^{-1/2}\|
<1
\]

and

\[
\epsilon_K
=
\|G_0^{-1/2}(K-K_0)G_0^{-1/2}\|,
\]

then \(G>0\) and every ordered generalized eigenvalue obeys

\[
\boxed{
|\lambda_j(K,G)-\lambda_j(K_0,G_0)|
\le
\frac{
\epsilon_K+\delta_G
\|G_0^{-1/2}K_0G_0^{-1/2}\|
}{
1-\delta_G
}.
}
\]

Q.E.D.
