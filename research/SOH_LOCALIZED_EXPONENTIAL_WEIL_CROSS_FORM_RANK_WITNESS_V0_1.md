# SOH Localized Exponential Weil Cross-Form Rank Witness v0.1

Status: **EXACT_CROSS_CONVOLUTION / SOURCE-FAITHFUL NUMERICAL WEIL EVALUATOR / STRONG NUMERICAL RANK-3 WITNESS / INTERVAL CERTIFICATE OPEN**

Date: 2026-09-26

Parents:
- research/SOH_SCALARIZATION_RANK_BARRIER_V0_1.md
- research/SOH_PIECEWISE_EXPONENTIAL_WEIL_CROSS_CONVOLUTION_V0_1.md
- research/SOH_SUZUKI_LOCALIZED_OPERATOR_JOIN_V0_1.md

No RH and no zeta-zero list are used.

## 1. Localized exponential family

For fixed \(a>0\), define

\[
v_z^{(a)}(x)=e^{-izx}\mathbf1_{[-a,a]}(x).
\]

For the standard involution
\[
\widetilde v(x)=\overline{v(-x)},
\]
the localized Weil cross form is
\[
\boxed{
Q_W^a(v_z,v_w)=W(v_z*\widetilde v_w).
}
\]

## 2. Exact finite cross-convolution

Put
\[
\alpha=i(\overline w-z).
\]

For \(|t|\le2a\),
\[
(v_z*\widetilde v_w)(t)
=
e^{-i\overline w t}
\int_{I_t}e^{\alpha u}\,du,
\]
where
\[
I_t=
\begin{cases}
[t-a,a],&0\le t\le2a,\\
[-a,t+a],&-2a\le t\le0.
\end{cases}
\]

Hence, for \(\alpha\ne0\),
\[
\boxed{
(v_z*\widetilde v_w)(t)
=
\begin{cases}
e^{-i\overline w t}
\dfrac{e^{\alpha a}-e^{\alpha(t-a)}}{\alpha},
&0\le t\le2a,\\[4mm]
e^{-i\overline w t}
\dfrac{e^{\alpha(t+a)}-e^{-\alpha a}}{\alpha},
&-2a\le t\le0,\\[4mm]
0,&|t|>2a.
\end{cases}
}
\]

At \(\alpha=0\),
\[
\boxed{
(v_z*\widetilde v_w)(t)
=
e^{-i\overline w t}(2a-|t|).
}
\]

This part is exact.

## 3. Source-faithful Weil evaluator

The implementation in
src/secret_of_a_half/localized_weil_cross_form.py
inserts this exact cross-convolution into Suzuki's explicit Weil functional.

Because
\[
\operatorname{supp}F\subset[-2a,2a],
\]
the prime support is exactly finite:
\[
\boxed{
n\le e^{2a}.
}
\]

The regularization tail beyond \(2a\) is integrated analytically:
\[
\boxed{
\int_{2a}^{\infty}
-2F(0)\frac{e^{-t}}{1-e^{-2t}}dt
=
-2F(0)\operatorname{artanh}(e^{-2a}).
}
\]

Only the compact regularization core is evaluated numerically.

## 4. Hermitian regression

For
\[
a=0.6,\quad
z=0.2+0.7i,\quad
w=-0.6+0.9i,
\]
the high-precision evaluator gives Hermitian residual at the \(10^{-60}\) scale.

This is consistent with the exact Hermitian form identity.

It is a regression, not a proof substitute.

## 5. Scalarization displacement test

Scalar generalized-Schur realization would require
\[
\operatorname{rank}
\left[
2i(\overline{z_k}-z_j)
Q_W^a(v_{z_j},v_{z_k})
\right]_{j,k}
\le2
\]
for every finite point set.

Use
\[
z_1=0.2+0.7i,\qquad
z_2=-0.6+0.9i,\qquad
z_3=1.1+0.5i.
\]

At \(a=0.6\),
\[
\boxed{
\det M\approx1.03473679061\times10^{-3}.
}
\]

The sampled singular values are approximately
\[
\boxed{
1.19336408,\quad
8.056982\times10^{-2},\quad
1.076179\times10^{-2}.
}
\]

At \(a=1\),
\[
\boxed{
\det M\approx7.395531492\times10^{-4}.
}
\]

The sampled singular values are approximately
\[
\boxed{
2.12934440,\quad
2.07125322\times10^{-1},\quad
1.67683482\times10^{-3}.
}
\]

Thus the sampled displacement is strongly rank three rather than rank two.

## 6. Current verdict

Numerically:
\[
\boxed{
\text{LIV-MD2c5C4a scalar rank collapse: FAIL witness found.}
}
\]

Rigorously:
\[
\boxed{
\text{LIV-MD2c5C4a: NOT YET CLOSED.}
}
\]

The evaluator uses arbitrary-precision quadrature rather than interval
enclosures. A high-precision nonzero determinant is a strong witness, not a
certified mathematical proof.

## 7. Exact next certificate

The smallest remaining task is to enclose this same \(3\times3\) determinant
rigorously.

An interval certificate must enclose:
1. the compact elementary integral;
2. every finite prime-power term;
3. the compact regularization integral with a certified quadrature bound;
4. the analytic regularization tail;
5. the determinant of the resulting interval matrix.

A single enclosure excluding zero proves
\[
\boxed{\operatorname{rank}M\ge3}
\]
and closes scalar C4a negatively.

Then the matrix/J-transfer route becomes the unique surviving lane.

## 8. Firewall

Not claimed:
- no RH result;
- no certified rank-three theorem yet;
- no global finite Fourier matrix;
- no substitution of the dense global Hermite surrogate for the localized operator;
- no claim that a floating-point determinant is a proof.
