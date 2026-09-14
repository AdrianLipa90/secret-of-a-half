# SOH Half-Kernel Green Carrier v0.2

Status: `EXACT_GREEN_CARRIER / EXACT_COMPLETION_FACTORIZATION / EXACT_RANK2_KREIN_CORRECTION / STRIPPED_HERGLOTZ_ROUTE_FAIL_NUMERICAL / RH_OPEN`

Date: 2026-09-14

## Scope and correction to v0.1

The finite terminal half-kernel of v0.1 remains exact.  This layer corrects one domain interpretation in that candidate: the raw modular seed whose half-operator image is the Riemann kernel has `exp(|u|/2)` tails and is not an ordinary `L^2(R)` vector.  Therefore it must not be used directly as a Hilbert-space positivity witness.

The correct Hilbert-space carrier is obtained by applying the resolvent of the half operator to the positive even Riemann kernel.

No statement here proves RH.

## 1. Half operator and its Green kernel

Let

\[
L_h=-\partial_u^2+h^2,
\qquad h=\frac12.
\]

On the full line the Green kernel is

\[
G_h(u)=\frac{e^{-h|u|}}{2h}.
\]

At the projective half value,

\[
\boxed{G_{1/2}(u)=e^{-|u|/2}.}
\]

Let `Phi_e` denote the standard positive even Riemann Xi kernel.  Define

\[
\boxed{K_{1/2}=L_{1/2}^{-1}\Phi_e=G_{1/2}*\Phi_e.}
\]

Since both factors of the convolution are positive and even,

\[
K_{1/2}(u)>0,
\qquad K_{1/2}(-u)=K_{1/2}(u).
\]

This carrier has the correct decaying half-tail and belongs to the ordinary Hilbert/Sobolev setting, unlike the raw modular seed.

## 2. Exact completion factorization

Fourier transformation gives

\[
\widehat{L_{1/2}K_{1/2}}(z)
=\left(z^2+\frac14\right)\widehat K_{1/2}(z).
\]

Because `L_{1/2}K_{1/2}=Phi_e`,

\[
\boxed{
\Xi(z)=\left(z^2+\frac14\right)\widehat K_{1/2}(z).
}
\]

For `s=1/2+iz`,

\[
s(s-1)=-\left(z^2+\frac14\right).
\]

Thus the half operator is precisely the Fourier-side realization of the standard completion polynomial.  It organizes the known `s(s-1)` factor; it does not by itself localize the nontrivial zeros.

The `e^{-|u|/2}` tail also identifies the natural Fourier-Laplace strip

\[
\boxed{|\operatorname{Im}z|<\frac12.}
\]

The projective half therefore appears both in the completion operator and in the width of the carrier's natural analytic strip.

## 3. Exact rank-two completion correction

Let

\[
p(z)=z^2+h^2,
\qquad h=\frac12,
\qquad g(z)=\widehat K_{1/2}(z),
\]

so that `Xi=pg`.  For the divided-Wronskian/de Branges kernel

\[
K_f(z,w)=2\frac{f'(z)f(\bar w)-f(z)f'(\bar w)}{\bar w-z},
\]

direct substitution gives

\[
\boxed{
K_\Xi(z,w)
=p(z)\overline{p(w)}K_g(z,w)
+4\left(z\bar w-\frac14\right)g(z)\overline{g(w)}.
}
\]

The second term has rank at most two on every finite point set.  It is an indefinite two-channel correction with feature vector

\[
r(z)=2g(z)\binom{z}{1/2}
\]

and signature matrix `diag(+1,-1)`.

On the diagonal,

\[
\boxed{
K_\Xi(z,z)=|p(z)|^2K_g(z,z)
+4\left(|z|^2-\frac14\right)|g(z)|^2.
}
\]

Hence the completion correction changes sign exactly at the half-radius `|z|=1/2`.  This aligns exactly with the existing SOH-G018 theorem that the quotient disk `|z|<=1/2` (equivalently `|w|<=1/4` after `w=z^2`) is zero-free.  The alignment is structural; it is not promoted to an RH proof.

## 4. Stronger stripped-Herglotz route is false

A tempting stronger route is to demand that the stripped logarithmic derivative

\[
m_g(z)=-\frac{g'(z)}{g(z)}
\]

have non-negative imaginary part throughout the upper half-strip.

It does not.  A stable high-precision witness is

\[
z=1+0.2i,
\qquad
\operatorname{Im}m_g(z)\approx-0.1852830234423052672.
\]

Therefore

\[
\boxed{
\operatorname{Im}m_g\ge0\text{ on the whole upper strip}
}
\]

is classified `FAIL_NUMERICAL_COUNTEREXAMPLE` as a stronger sufficient route.  The full completed Xi sector must retain the finite-rank correction; stripped and completion sectors cannot be forced positive independently.

## 5. Relation to current G024 frontier

SOH-G024 already proves globally the first and second complete-monotonicity inequalities for its Dimitrov-Xu correlation family.  The current open frontier is the third-order condition

\[
-H_y'''(q)\ge0,
\]

or equivalently the already-derived bridge-cumulant/logarithmic-growth inequality.  The Green carrier is therefore not a replacement proof route.  Its admissible use is to reorganize the same global correlation problem while preserving the completion defect exactly.

## Proof firewall

Exact here:

- `G_1/2(u)=exp(-|u|/2)`;
- `K_1/2=L_1/2^{-1} Phi_e` as the corrected Hilbert carrier;
- `Xi=(z^2+1/4) Khat_1/2`;
- the rank-two divided-Wronskian correction;
- the half-radius sign change of the completion correction.

Numerical no-go only:

- the explicit negative witness for the stronger stripped-Herglotz route.

Open:

- G024 third-order complete monotonicity;
- global Pick/de Branges positivity;
- RH.
