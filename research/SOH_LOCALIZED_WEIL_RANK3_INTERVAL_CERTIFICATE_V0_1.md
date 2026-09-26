# SOH Localized Weil Rank-3 Interval Certificate v0.1

Status: **MACHINE-INTERVAL CERTIFIED RANK >= 3 / SCALAR C4a CLOSED NEGATIVE / MATRIX-J TRANSFER FORCED**

Date: 2026-09-26

Parent:
- research/SOH_LOCALIZED_EXPONENTIAL_WEIL_CROSS_FORM_RANK_WITNESS_V0_1.md
- research/SOH_SCALARIZATION_RANK_BARRIER_V0_1.md

No RH and no zero list are used.

## 1. Target matrix

Use
\[
a=0.6
\]
and
\[
z_1=0.2+0.7i,\qquad
z_2=-0.6+0.9i,\qquad
z_3=1.1+0.5i.
\]

Define
\[
M_{jk}
=
2i(\overline{z_k}-z_j)
Q_W^a(v_{z_j},v_{z_k}).
\]

If the first-correction de Branges--Pontryagin complement admitted a scalar
generalized-Schur representation, the scalarization-rank theorem would force
\[
\operatorname{rank}M\le2
\]
for every such point set.

Therefore it is enough to certify
\[
\det M\ne0.
\]

## 2. Interval evaluator

The certificate uses the exact compact cross-convolution and Suzuki's explicit
Weil functional.

The only infinite analytic component is
\[
J_T(s)
=
\int_0^T
\frac{e^{-st}-e^{-t}}{1-e^{-2t}}dt.
\]

Expand
\[
\frac1{1-e^{-2t}}
=
\sum_{k\ge0}e^{-2kt}.
\]

After \(K\) terms,
\[
J_T(s)
=
\sum_{k=0}^{K-1}
\left[
\frac{1-e^{-(s+2k)T}}{s+2k}
-
\frac{1-e^{-(1+2k)T}}{1+2k}
\right]
+
R_K.
\]

The rational part of \(R_K\) is accelerated by the geometric expansion
\[
\frac1{2k+s}
=
\sum_{j=0}^{m-1}
\frac{(-s)^j}{(2k)^{j+1}}
+
\mathcal R_{m,k}(s),
\]
with
\[
|\mathcal R_{m,k}(s)|
\le
\frac{|s|^m}{(2k)^{m+1}}
\frac1{1-|s|/(2k)}.
\]

The real p-series tails are enclosed by
\[
\frac{K^{1-p}}{p-1}
\le
\sum_{k=K}^\infty k^{-p}
\le
\frac{K^{1-p}}{p-1}+K^{-p}.
\]

The remaining exponential tail is bounded geometrically.

All finite transcendental arithmetic is evaluated with outward
mpmath.iv interval arithmetic.

## 3. Certified enclosure at K=500

With tail order
\[
m=4
\]
and
\[
K=500,
\]
the determinant enclosure is

\[
\boxed{
\Re\det M
\in
[
0.0010234522869501969681,\;
0.0010460214830344538641
].
}
\]

The imaginary enclosure is

\[
\boxed{
\Im\det M
\in
[
-1.2131681620\times10^{-5},\;
1.2131693091\times10^{-5}
].
}
\]

Since the real interval is strictly positive,

\[
\boxed{
0\notin\det M.
}
\]

Therefore
\[
\boxed{
\operatorname{rank}M=3.
}
\]

## 4. Independent truncation checks

The same certificate remains nonzero for independent series cutoffs.

At \(K=300\),
\[
\Re\det M
\in
[
0.0010033457427969441,\;
0.0010661293968810101
].
\]

At \(K=1000\),
\[
\Re\det M
\in
[
0.0010319187176398247,\;
0.0010375548733737892
].
\]

All three intervals exclude zero.

## 5. Consequence for scalarization

The scalarization-rank theorem gives
\[
\text{scalar generalized-Schur complement}
\Longrightarrow
\operatorname{rank}M\le2.
\]

The certified sample has
\[
\operatorname{rank}M=3.
\]

Hence

\[
\boxed{
\text{the localized first-correction complement is not representable by one scalar generalized-Schur kernel.}
}
\]

Thus

\[
\boxed{
\text{LIV-MD2c5C4a = CLOSED NEGATIVE.}
}
\]

The scalar-complement route is rejected.

## 6. Surviving route

The exact four-channel displacement
\[
\Phi(z)
\operatorname{diag}(1,-1,-1,1)
\Phi(w)^*
\]
does not collapse to scalar rank two.

Therefore the next transfer object must retain matrix or Pontryagin channel
structure.

The surviving gate is

### LIV-MD2c5C4b — matrix/J-contractive transfer
Status: **FORCED OPEN ROUTE**.

Construct the minimal matrix-valued transfer whose kernel realizes the exact
four-channel de Branges--Pontryagin complement, then connect its scalar
compression/Cayley image to the xi target.

## 7. Trust boundary

This is a machine-assisted interval proof.

The proof dependency includes:
- the algebra in the repository implementation;
- Python;
- mpmath.iv outward interval arithmetic.

It is stronger than an arbitrary-precision floating witness but is not a
formally verified Lean/Coq/Isabelle artifact.

No claim about RH follows from the rank obstruction alone.
