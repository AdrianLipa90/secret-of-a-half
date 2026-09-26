# SOH Prime-Free Interval Rank-4 Certificate v0.1

Status: **CERTIFIED_FULL_FOUR_CHANNEL_RANK / SCALAR COLLAPSE CLOSED NEGATIVELY / MATRIX-J TRANSFER REQUIRED**

Date: 2026-09-26

Parents:
- research/SOH_PRIME_FREE_INTERVAL_RANK3_CERTIFICATE_V0_1.md
- research/SOH_SCALARIZATION_RANK_BARRIER_V0_1.md
- research/SOH_DE_BRANGES_PONTRYAGIN_COMPLEMENT_V0_1.md

No RH and no zeta-zero list are used.

## 1. Prime-free localization

Use the same certified localization

\[
a=\frac{69}{200},
\qquad
2a=\frac{69}{100}<\log 2.
\]

Hence

\[
e^{2a}<2
\]

and the localized Weil functional contains no prime-power contribution.

## 2. Four-point sample

Take

\[
z_1=\frac{i}{20},
\qquad
z_2=\frac{3i}{20},
\qquad
z_3=\frac{3i}{10},
\qquad
z_4=\frac{9i}{20}.
\]

For \(z_j=iy_j\), define

\[
M_{jk}
=
2(y_j+y_k)
Q_W^a(v_{z_j},v_{z_k}).
\]

The same outward-rounded interval implementation used in the rank-3
certificate evaluates every matrix entry without numerical quadrature.

## 3. Certified determinant

Direct interval evaluation of the \(4\times4\) Leibniz determinant gives

\[
\boxed{
\det M
\in
[
7.9960256384132330750131598189604317774020397658504\times10^{-17},
\;
7.9960256384132330750141020269547584672851695359059\times10^{-17}
].
}
\]

Therefore

\[
\boxed{0\notin\det M}
\]

and hence

\[
\boxed{\operatorname{rank}M=4.}
\]

This is a validated interval result.

## 4. Structural consequence

The exact first-correction displacement has the natural four-channel form

\[
\Phi(z)J_{2,2}\Phi(w)^*,
\qquad
J_{2,2}=\operatorname{diag}(1,-1,-1,1).
\]

A scalar generalized-Schur or scalar de Branges numerator has displacement
rank at most two after any nonvanishing scalar gauge.

The certified rank-four sample therefore excludes scalar collapse even more
strongly than the rank-three certificate:

\[
\boxed{
\text{localized first-correction displacement is genuinely four-channel.}
}
\]

Thus the scalar transfer lane is closed negatively.

## 5. Actual finite complement near the free point

For the localized resolvent flow,

\[
\frac{K_0-K_t}{t}
\longrightarrow
Q_W^a
\]

on the chosen form-domain vectors as \(t\downarrow0\).

For this fixed four-point sample, the determinant is a continuous polynomial
of the matrix entries. Since the limiting determinant is strictly positive,
there exists \(t_*>0\) such that for every sufficiently small admissible

\[
0<t<t_*,
\]

the sampled displacement matrix of the actual complement \(K_0-K_t\) also has

\[
\boxed{\operatorname{rank}=4.}
\]

Therefore the full finite Suzuki complement is genuinely matrix-valued in a
punctured neighborhood of the free point.

The theorem proves existence of \(t_*\); it does not yet provide an effective
numerical value.

## 6. Gate closure

### LIV-MD2c5C4a

\[
\boxed{\text{CLOSED NEGATIVELY, CERTIFIED}.}
\]

Scalar generalized-Schur/de Branges collapse is excluded near the free point.

### LIV-MD2c5C4b

\[
\boxed{\text{REQUIRED}.}
\]

The next proof-bearing construction is a matrix or \(J\)-contractive transfer
retaining the four-channel signature structure until a later justified
compression.

## 7. Compact theorem

At

\[
a=69/200
\]

and the four imaginary sample points above, the prime-free localized Weil
first-correction displacement has a rigorously certified nonzero \(4\times4\)
determinant. Hence its displacement rank is exactly four.

By continuity, the actual localized resolvent complement has sampled
displacement rank four for all sufficiently small positive admissible \(t\).

Thus the scalar lane is finished; the surviving route is the matrix
\(J_{2,2}\)-transfer.
