# SOH Prime-Free Interval Rank-3 Certificate v0.1

Status: **CERTIFIED_NONZERO_3x3_MINOR / SCALAR RANK-COLLAPSE REJECTED NEAR FREE POINT / MATRIX-J TRANSFER REQUIRED**

Date: 2026-09-26

Parents:
- research/SOH_SCALARIZATION_RANK_BARRIER_V0_1.md
- research/SOH_LOCALIZED_EXPONENTIAL_WEIL_CROSS_FORM_RANK_WITNESS_V0_1.md
- research/SOH_DE_BRANGES_PONTRYAGIN_COMPLEMENT_V0_1.md

No RH and no zeta-zero list are used.

## 1. Prime-free localization

Choose

\[
\boxed{
a=\frac{69}{200}=0.345.
}
\]

Then

\[
2a=\frac{69}{100}<\log2,
\]

so

\[
e^{2a}<2.
\]

Therefore the localized compactly supported Weil functional contains no
prime-power term:

\[
\boxed{
\sum_{n\le e^{2a}}\frac{\Lambda(n)}{\sqrt n}(\cdots)=0.
}
\]

This removes every prime-threshold and prime-enumeration issue from the rank
certificate. The witness is purely archimedean.

## 2. Rational imaginary sample

Take

\[
\boxed{
z_1=\frac{i}{20},
\qquad
z_2=\frac{i}{4},
\qquad
z_3=\frac{9i}{20}.
}
\]

Write \(z_j=i y_j\). For purely imaginary points the localized vectors are
real exponentials

\[
v_{z_j}(x)=e^{y_jx}\mathbf1_{[-a,a]}(x),
\]

and the first-correction displacement matrix is real symmetric:

\[
\boxed{
M_{jk}
=
2(y_j+y_k)
Q_W^a(v_{z_j},v_{z_k}).
}
\]

## 3. Exact cross-convolution reduction

For \(y,v\in(0,1/2)\), put

\[
c=y+v,
\qquad
T=2a.
\]

The compact cross-convolution is

\[
F_{y,v}(t)
=
(v_{iy}*\widetilde v_{iv})(t).
\]

For \(0\le t\le T\),

\[
F_{y,v}(t)
=
\frac{
e^{ca}e^{-vt}
-
e^{-ca}e^{yt}
}{c},
\]

and for \(-T\le t\le0\),

\[
F_{y,v}(t)
=
\frac{
e^{ca}e^{yt}
-
e^{-ca}e^{-vt}
}{c}.
\]

Thus every elementary Weil integral is a finite linear combination of
elementary exponentials.

## 4. Validated regularization integral

On \(0\le t\le T\), the regularization core reduces to finite linear
combinations of

\[
H(\lambda,T)
=
\int_0^T
\frac{
e^{-\lambda t}-e^{-t}
}{
1-e^{-2t}
}\,dt,
\qquad
0<\lambda<1.
\]

The infinite integral is

\[
\boxed{
H(\lambda,\infty)
=
\frac12
\left[
\psi(1/2)-\psi(\lambda/2)
\right].
}
\]

Every \(\lambda/2\) in the chosen rational sample is rational. The
implementation evaluates these digamma values by Gauss' finite digamma
formula, using only outward-rounded interval operations on
\(\pi,\log,\sin,\cos\).

The finite-\(T\) tail is

\[
H(\lambda,\infty)-H(\lambda,T)
=
\sum_{k\ge0}
\left[
\frac{e^{-(\lambda+2k)T}}{\lambda+2k}
-
\frac{e^{-(1+2k)T}}{1+2k}
\right].
\]

After 60 interval terms, the unsummed positive remainder is bounded by

\[
\boxed{
0\le R_N
\le
\frac{
e^{-(\lambda+2N)T}
}{
(\lambda+2N)(1-e^{-2T})
}.
}
\]

Thus the complete regularization integral has a validated enclosure without
numerical quadrature.

## 5. Interval implementation

The executable certificate is

src/secret_of_a_half/localized_weil_rank_interval.py

and the regression is

tests/test_localized_weil_rank_interval.py.

The implementation uses mpmath.iv outward-rounded interval arithmetic.
Rational endpoints are rounded down/up, and the elementary transcendental
operations are evaluated as intervals.

No midpoint quadrature is used in this certificate.

## 6. Certified matrix entries

The interval matrix is enclosed by

\[
M_{11}\in
[0.0251522236721613084593126342514594302,\;
 0.0251522236721613084593126342515408307],
\]

\[
M_{12}\in
[0.0757589750449328396770996448440124663,\;
 0.0757589750449328396770996448440940665],
\]

\[
M_{13}\in
[0.1273432904393610797584216804052222110,\;
 0.1273432904393610797584216804053044110],
\]

\[
M_{22}\in
[0.1270689871447410609209686971868597334,\;
 0.1270689871447410609209686971869411344],
\]

\[
M_{23}\in
[0.1798318885600296191453837541413418661,\;
 0.1798318885600296191453837541414234670],
\]

\[
M_{33}\in
[0.2342596586173064171770187022514689823,\;
 0.2342596586173064171770187022515503844].
\]

Symmetry supplies the transposed entries.

## 7. Certified determinant

Direct interval evaluation of the \(3\times3\) determinant gives

\[
\boxed{
\det M
\in
[
1.2806783879766273009640491866108210462830380456\times10^{-8},
\;
1.2806783879766273009640503312753879790992031402\times10^{-8}
].
}
\]

In particular,

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

This is no longer a floating-point witness.

## 8. Consequence for scalar rank collapse

The scalarization barrier proved

\[
\text{scalar generalized-Schur/de Branges realization}
\Longrightarrow
\text{displacement rank}\le2.
\]

The certified first-correction displacement has rank three.

Moreover,

\[
\frac{K_0-K_t}{t}
\longrightarrow
Q_W^a
\]

on the chosen form-domain vectors as \(t\downarrow0\).

For the fixed three-point sample, the determinant of the corresponding
displacement matrix is a continuous polynomial in its matrix entries.
Because the limiting determinant is strictly nonzero, there exists

\[
t_*>0
\]

such that for every sufficiently small admissible

\[
0<t<t_*,
\]

the actual finite complement \(K_0-K_t\) also has sampled displacement rank
three.

Therefore

\[
\boxed{
\text{the actual localized Suzuki complement is not scalarizable near }t=0.
}
\]

The existence of \(t_*\) is proved; this certificate does not yet compute an
effective value of \(t_*\).

## 9. Gate closure

### LIV-MD2c5C4a — special scalar rank collapse

Status:

\[
\boxed{\text{CLOSED NEGATIVELY}.}
\]

A certified rank-three witness excludes universal scalar collapse for the
localized Suzuki complement near the free point.

### LIV-MD2c5C4b — matrix/J-contractive transfer

Status:

\[
\boxed{\text{REQUIRED FOR THE SMALL-}t\text{ RENORMALIZATION LANE}.}
\]

The natural exact displacement already has four channels

\[
(\mathcal E_0,\mathcal E_0^\#,\mathcal E_t,\mathcal E_t^\#)
\]

with signature matrix

\[
J_{2,2}=\operatorname{diag}(1,-1,-1,1).
\]

The next construction should therefore remain matrix/J-valued until a later,
proved compression.

## 10. Firewall

This theorem does not:
- prove RH;
- determine the Pontryagin index \(\kappa_a\);
- produce the final matrix transfer;
- prove scalarization is impossible at every isolated \(t>0\).

It proves the statement needed to reject the universal scalar-renormalization
lane: scalar rank collapse fails throughout a punctured neighborhood of the
free point.

## 11. Compact theorem

At

\[
a=69/200,
\quad
z_1=i/20,
\quad
z_2=i/4,
\quad
z_3=9i/20,
\]

the prime-free localized Weil first-correction displacement matrix satisfies

\[
\boxed{
\det M>1.2806783879766273\times10^{-8}>0.
}
\]

Hence

\[
\boxed{
\operatorname{rank}M=3.
}
\]

By continuity of the resolvent first correction, the sampled displacement of
\(K_0-K_t\) has rank three for all sufficiently small positive admissible
\(t\). Therefore no scalar generalized-Schur/de Branges representation of the
localized complement can exist throughout that small-\(t\) regime.
