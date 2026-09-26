# SOH Minimal Four-Channel J-Jet Realization v0.1

Status: **EXACT_FIXED-SIGNATURE JET REALIZATION / MINIMAL NEAR FREE POINT / POTAPOV DYNAMICAL TRANSFER OPEN**

Date: 2026-09-26

Parents:
- research/SOH_DE_BRANGES_PONTRYAGIN_COMPLEMENT_V0_1.md
- research/SOH_PRIME_FREE_INTERVAL_RANK4_MINIMAL_CHANNEL_V0_1.md
- research/SOH_LIVSIC_DENOMINATOR_SHARP_THETA_WEIL_V0_1.md

No RH and no zeta-zero list are used.

## 1. Two finite de Branges denominators

Let

\[
\mathcal E_0(z)
\]

be the normalized free finite denominator and

\[
\mathcal E_t(z)
\]

the normalized localized denominator for

\[
I+tA_a>0.
\]

Define the two-by-two denominator matrix

\[
\mathbb E_t(z)
=
\begin{pmatrix}
\mathcal E_0(z)&\mathcal E_t(z)\\
\mathcal E_0^\#(z)&\mathcal E_t^\#(z)
\end{pmatrix}.
\]

Let

\[
J_r
=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix},
\qquad
J_c
=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}.
\]

The exact complement displacement is

\[
\boxed{
D_t(z,w)
:=
2i(\overline w-z)(K_0-K_t)(z,w)
=
\operatorname{tr}
\left[
J_r
\mathbb E_t(z)
J_c
\mathbb E_t(w)^*
\right].
}
\]

This is simply the four-channel identity written as a two-by-two matrix
pairing.

## 2. Midpoint/secant jet frame

Define the exact secant

\[
\boxed{
H_t(z)
=
\frac{
\mathcal E_0(z)-\mathcal E_t(z)
}{t}
}
\]

and midpoint

\[
\boxed{
M_t(z)
=
\frac{
\mathcal E_0(z)+\mathcal E_t(z)
}{2}.
}
\]

Form the jet matrix

\[
\boxed{
\widehat{\mathbb E}_t(z)
=
\begin{pmatrix}
M_t(z)&H_t(z)\\
M_t^\#(z)&H_t^\#(z)
\end{pmatrix}.
}
\]

This is a purely algebraic change of column coordinates.

Indeed, if

\[
\mathbb B_t(z)
=
\begin{pmatrix}
\mathcal E_0(z)&H_t(z)\\
\mathcal E_0^\#(z)&H_t^\#(z)
\end{pmatrix},
\]

then

\[
\mathbb E_t
=
\mathbb B_t
R_t,
\qquad
R_t
=
\begin{pmatrix}
1&1\\
0&-t
\end{pmatrix}.
\]

## 3. Exact column metric after free subtraction

A direct multiplication gives

\[
R_tJ_cR_t^*
=
t
\begin{pmatrix}
0&1\\
1&-t
\end{pmatrix}.
\]

Define

\[
G_t
=
\begin{pmatrix}
0&1\\
1&-t
\end{pmatrix}.
\]

Then

\[
\boxed{
\frac{D_t(z,w)}{t}
=
\operatorname{tr}
\left[
J_r
\mathbb B_t(z)
G_t
\mathbb B_t(w)^*
\right].
}
\]

For every real \(t\),

\[
\det G_t=-1.
\]

Hence \(G_t\) always has signature \((1,1)\).

## 4. Fixed signature by an exact shear

Let

\[
F
=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}
\]

and

\[
S_t
=
\begin{pmatrix}
1&0\\
-t/2&1
\end{pmatrix}.
\]

Then

\[
\boxed{
G_t
=
S_tFS_t^*.
}
\]

Also

\[
\mathbb B_tS_t
=
\begin{pmatrix}
\mathcal E_0-\frac t2H_t&H_t\\
\mathcal E_0^\#-\frac t2H_t^\#&H_t^\#
\end{pmatrix}
=
\widehat{\mathbb E}_t.
\]

Therefore

\[
\boxed{
\frac{D_t(z,w)}{t}
=
\operatorname{tr}
\left[
J_r
\widehat{\mathbb E}_t(z)
F
\widehat{\mathbb E}_t(w)^*
\right].
}
\]

The column metric is now independent of \(t\).

## 5. Standard J22 form

The Hadamard matrix

\[
U
=
\frac1{\sqrt2}
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix}
\]

satisfies

\[
U^*FU
=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}.
\]

Define

\[
\widetilde{\mathbb E}_t
=
\widehat{\mathbb E}_tU.
\]

Then vectorization of the two-by-two matrix gives a four-component feature
vector with fixed signature

\[
\boxed{
J_{2,2}
=
\operatorname{diag}(1,-1,-1,1)
}
\]

up to a harmless permutation of coordinates.

Thus the renormalized complement has an exact fixed-signature four-channel
Kolmogorov realization.

## 6. First-jet limit

If the finite denominator is differentiable in \(t\) at the free point in the
declared form/resolvent sense, then

\[
M_t(z)\to\mathcal E_0(z)
\]

and

\[
H_t(z)
\to
-\left.
\frac{\partial}{\partial t}
\mathcal E_t(z)
\right|_{t=0}.
\]

Therefore the fixed-signature realization has a finite first-jet limit.

This is exactly the level at which the Weil first-correction and
theta/log-derivative bridge enter.

## 7. Minimality

The prime-free interval theorem certifies a four-by-four displacement matrix
of rank four for the first correction at

\[
a=69/200.
\]

Hence no exact feature representation using fewer than four scalar channels
can realize that kernel.

The present realization uses exactly four scalar entries:

\[
M_t,\quad M_t^\#,\quad H_t,\quad H_t^\#.
\]

Therefore

\[
\boxed{
\text{the fixed-signature J-jet realization is minimal near }t=0.
}
\]

By continuity, the same minimal channel count holds for the actual complement
for all sufficiently small positive admissible \(t\).

## 8. What this closes

### LIV-MD2c5C4c — minimal four-channel J realization

Status:

\[
\boxed{\text{CLOSED AT KERNEL/JET LEVEL}.}
\]

We now have:
- exact two-by-two matrix frame;
- exact fixed row signature \(J_r\);
- exact fixed column flip signature \(F\);
- equivalent four-channel \(J_{2,2}\) vector realization;
- certified minimality near the free point.

No arbitrary Blaschke factors are inserted.

## 9. What remains open

The jet frame is a minimal indefinite Kolmogorov realization, but it is not yet
a Potapov transfer matrix with a composition law in \(a\) or \(t\).

The next gate is:

### LIV-MD2c5C4d — Potapov/J-contractive dynamical transfer

Construct from

\[
\widetilde{\mathbb E}_t(z)
\]

a matrix-valued meromorphic transfer

\[
\Theta_{a,t}(z)
\]

such that:

1. its \(J\)-kernel carries the same finite negative-square index;
2. composition in localization/flow parameters is explicit or controlled;
3. the theta/Weil normalized jet converges to the xi target frame;
4. a justified scalar compression, if any, occurs only in the limit;
5. no finite-scale scalar rank collapse is assumed.

## 10. Target-frame direction

The infinite denominator has the exact factorization

\[
D(z)
=
A\,f(z)
\left[
r_0+\frac{\xi'}{\xi}\!\left(\frac12-iz\right)
\right],
\]

with

\[
f(z)=\xi\!\left(\frac12-iz\right),
\qquad
f^\#=f.
\]

Thus the natural limiting jet coordinates are:
- a self-dual carrier \(f\);
- a response/log-derivative channel;
- their \(\#\)-partners.

At the infinite target the self-duality may reduce the effective scalar rank,
but the finite rank-four theorem forbids imposing that collapse before the
limit.

## 11. Compact theorem

Let

\[
M_t=\frac{\mathcal E_0+\mathcal E_t}{2},
\qquad
H_t=\frac{\mathcal E_0-\mathcal E_t}{t}.
\]

Then

\[
\boxed{
\frac{
2i(\overline w-z)(K_0-K_t)(z,w)
}{t}
=
\operatorname{tr}
\left[
J_r
\begin{pmatrix}
M_t&H_t\\
M_t^\#&H_t^\#
\end{pmatrix}_{\!z}
F
\begin{pmatrix}
M_t&H_t\\
M_t^\#&H_t^\#
\end{pmatrix}_{\!w}^{*}
\right].
}
\]

After a fixed Hadamard change of column basis this is a \(J_{2,2}\)
four-channel realization.

The certified rank-four witness shows that this channel dimension is minimal
near the free point.
