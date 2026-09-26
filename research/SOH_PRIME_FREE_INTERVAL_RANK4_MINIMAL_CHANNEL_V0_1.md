# SOH Prime-Free Interval Rank-4 / Minimal Four-Channel Certificate v0.1

Status: **CERTIFIED_RANK4 / FOUR-CHANNEL REALIZATION MINIMAL NEAR FREE POINT / SCALAR-AND-THREE-CHANNEL COMPRESSION REJECTED**

Date: 2026-09-26

Parents:
- research/SOH_PRIME_FREE_INTERVAL_RANK3_CERTIFICATE_V0_1.md
- research/SOH_SCALARIZATION_RANK_BARRIER_V0_1.md
- research/SOH_DE_BRANGES_PONTRYAGIN_COMPLEMENT_V0_1.md

No RH and no zeta-zero list are used.

## 1. Same prime-free localization

Use

\[
a=\frac{69}{200},
\qquad
2a<\log2.
\]

Hence the localized Weil cross form contains no prime-power term.

All arithmetic threshold issues are absent.

## 2. Four-point rational sample

Take

\[
\boxed{
z_1=\frac{i}{20},
\qquad
z_2=\frac{3i}{20},
\qquad
z_3=\frac{3i}{10},
\qquad
z_4=\frac{9i}{20}.
}
\]

Define

\[
M_{jk}
=
2i(\overline z_k-z_j)
Q_W^a(v_{z_j},v_{z_k}).
\]

Because all \(z_j\) are purely imaginary, \(M\) is real symmetric.

The same Gauss-digamma plus outward-rounded interval method from the rank-3
certificate applies entrywise.

## 3. Certified four-by-four determinant

The validated interval computation gives

\[
\boxed{
\det M_4
\in
[
7.9960256384132325188436556635391341466347256412\times10^{-17},
\;
7.9960256384132336311836061823760311174433641068\times10^{-17}
].
}
\]

Therefore

\[
\boxed{
0\notin\det M_4
}
\]

and

\[
\boxed{
\operatorname{rank}M_4=4.
}
\]

This is a validated interval statement, not a floating-point rank estimate.

## 4. Consequence for channel dimension

The exact de Branges--Pontryagin complement has the four-channel displacement

\[
2i(\overline w-z)(K_0-K_t)(z,w)
=
\Phi_t(z)
J_{2,2}
\Phi_t(w)^*,
\]

where

\[
\Phi_t(z)
=
\left(
\mathcal E_0(z),
\mathcal E_0^\#(z),
\mathcal E_t(z),
\mathcal E_t^\#(z)
\right)
\]

and

\[
J_{2,2}
=
\operatorname{diag}(1,-1,-1,1).
\]

Thus four scalar channels are always sufficient.

The certified first-correction sample has rank four, so no feature
representation with fewer than four scalar channels can reproduce that
displacement matrix.

Therefore the canonical four-channel representation is **minimal** for the
first-correction kernel at the certified scale.

## 5. Transfer to the actual finite complement

The resolvent expansion gives, on the chosen form-domain vectors,

\[
\frac{K_0-K_t}{t}
\longrightarrow
Q_W^a
\qquad(t\downarrow0).
\]

For the fixed four-point sample,

\[
\frac1{t^4}
\det
\left[
2i(\overline z_k-z_j)(K_0-K_t)(z_j,z_k)
\right]_{j,k=1}^4
\]

converges to the certified nonzero determinant of the first-correction
matrix.

Hence there exists

\[
t_4>0
\]

such that for every sufficiently small admissible

\[
0<t<t_4,
\]

the actual finite complement has sampled displacement rank four.

Therefore

\[
\boxed{
\text{four channels are minimal for the actual small-}t
\text{ localized complement.}
}
\]

The theorem is existential in \(t_4\); no effective threshold is claimed.

## 6. Architectural consequence

The following routes are closed near the free point:

- scalar generalized-Schur compression;
- scalar de Branges compression;
- any exact three-scalar-channel displacement factorization.

The surviving minimal finite representation is four-channel with signature

\[
\boxed{
J_{2,2}=\operatorname{diag}(1,-1,-1,1).
}
\]

This is stronger than the previous statement that a matrix transfer is merely
natural.

It is now forced by a certified rank invariant.

## 7. Refined gate

### LIV-MD2c5C4a

Scalar rank collapse:
\[
\boxed{\text{CLOSED NEGATIVELY}.}
\]

### LIV-MD2c5C4b

Three-channel compression:
\[
\boxed{\text{CLOSED NEGATIVELY NEAR }t=0.}
\]

### LIV-MD2c5C4c

Minimal four-channel \(J_{2,2}\)-transfer:
\[
\boxed{\text{OPEN / NOW THE UNIQUE MINIMAL SMALL-}t\text{ LANE}.}
\]

The next object should preserve all four channels until an asymptotic
compression is proved rather than assumed.

## 8. Firewall

This theorem does not:
- prove RH;
- determine the sign/inertia split inside the rank-four sample;
- prove four channels remain minimal for every \(t>0\);
- produce the final \(J\)-contractive transfer law.

It proves exact minimality of four channels in a punctured neighborhood of the
free point.

## 9. Compact theorem

At

\[
a=69/200
\]

and sample

\[
\left\{
i/20,\;3i/20,\;3i/10,\;9i/20
\right\},
\]

the prime-free first-correction displacement determinant is strictly positive:

\[
\boxed{
\det M_4
>
7.9960256384132325\times10^{-17}.
}
\]

Therefore

\[
\boxed{
\operatorname{rank}M_4=4.
}
\]

Since the canonical de Branges--Pontryagin realization already uses four
channels, its channel dimension is minimal at this scale and remains minimal
for the actual complement for all sufficiently small positive \(t\).
