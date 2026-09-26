# SOH Pontryagin Shift Spectral Flow and Generalized-Schur Characteristic v0.1

Status: **PROVED_FROM_SUZUKI_PLUS_STANDARD_PONTRYAGIN_REALIZATION / EXACT_FINITE_INDEX / ZERO-SHIFT_LIMIT_OPEN**

Date: 2026-09-26

Parents:
- research/SOH_SUZUKI_LIVSIC_SCHUR_REDUCTION_V0_1.md
- research/SOH_DE_BRANGES_PONTRYAGIN_COMPLEMENT_V0_1.md
- research/SOH_LOCALIZED_WEIL_NEGATIVE_INDEX_MONOTONICITY_V0_1.md
- research/SOH_GENERALIZED_SCHUR_XI_NEVANLINNA_CAYLEY_V0_1.md

External inputs:
- Masatoshi Suzuki, Weil's quadratic form via the screw function,
  arXiv:2606.09096v3.
- Standard realization theory of generalized Schur/Nevanlinna functions in
  Pontryagin spaces.

No RH and no zeta-zero list are used.

## 1. Localized spectral shift

Fix a localization radius \(a>0\).

Suzuki's localized Weil operator

\[
A_a=A_a^*
\]

has discrete lower-bounded spectrum, with \(+\infty\) as its only
accumulation point.

For a real parameter

\[
\eta\in\rho(A_a),
\]

define

\[
\boxed{
T_{a,\eta}=A_a-\eta I.
}
\]

Its closed form is

\[
Q_{a,\eta}[u,v]
=
Q_W^a[u,v]
-
\eta\langle u,v\rangle_{L^2}.
\]

## 2. Pontryagin index

Because the spectrum is discrete and lower bounded, only finitely many
eigenvalues lie below any fixed real \(\eta\).

Define, with multiplicity,

\[
\boxed{
\kappa_a(\eta)
=
\#\{\lambda_j(A_a)<\eta\}.
}
\]

The form space of \(T_{a,\eta}\), equipped with

\[
[u,v]_{a,\eta}
=
\left\langle
\operatorname{sgn}(T_{a,\eta})
|T_{a,\eta}|^{1/2}u,
|T_{a,\eta}|^{1/2}v
\right\rangle,
\]

is a Pontryagin space of negative index

\[
\boxed{
\operatorname{ind}_-\Pi_{a,\eta}
=
\kappa_a(\eta).
}
\]

If

\[
\eta<\lambda_a=\inf\sigma(A_a),
\]

then \(\kappa_a(\eta)=0\) and the construction reduces to Suzuki's positive
Hilbert-space metric.

## 3. The differential operator remains symmetric

On the compact core

\[
C_c^\infty(-a,a),
\]

Suzuki proves symmetry of

\[
\mathscr D_a=i\,d/dx
\]

for the shifted form in the positive regime.

The Green/form identity is algebraic. Replacing the positive shift by an
arbitrary real resolvent shift changes the form only by

\[
-\eta\langle u,v\rangle_{L^2}.
\]

The ordinary first derivative is symmetric for that \(L^2\) term on the same
compact core.

Therefore the same identity gives

\[
\boxed{
[\mathscr D_a u,v]_{a,\eta}
=
[u,\mathscr D_a v]_{a,\eta}
}
\]

for every real

\[
\eta\in\rho(A_a).
\]

Thus \(\mathscr D_a\) is a symmetric operator in the Pontryagin space
\(\Pi_{a,\eta}\).

## 4. Deficiency/evaluation vectors

Since

\[
\eta\in\rho(A_a),
\]

the inverse

\[
T_{a,\eta}^{-1}
\]

is bounded on \(L^2(-a,a)\).

For

\[
e_z(x)=e^{-izx},
\]

define

\[
\boxed{
v_z^{(\eta)}
=
T_{a,\eta}^{-1}e_z.
}
\]

The same adjoint calculation as in Suzuki Section 6 gives

\[
\boxed{
\mathscr D_{a,\eta}^{+}v_z^{(\eta)}
=
zv_z^{(\eta)}.
}
\]

In particular, the deficiency spaces at \(\pm i\) remain one-dimensional.

The algebraic deficiency indices remain

\[
\boxed{(1,1).}
\]

No positive metric is required for this statement; nondegeneracy of
\(T_{a,\eta}\) is the relevant finite-scale condition.

## 5. Indefinite de Branges kernel

Set

\[
N_{a,\eta}^2
=
[v_i^{(\eta)},v_i^{(\eta)}]_{a,\eta}.
\]

A canonical equal-sign normalization can be chosen away from exceptional
isotropic deficiency normalizations; equivalently one may formulate the result
with a unitary boundary pair.

Define the denominator entire function by the same boundary-form expression as
in the Suzuki construction.

The polarized boundary identity gives, up to a nonzero real scalar gauge,

\[
\boxed{
K_{a,\eta}(z,w)
=
\langle e_w,T_{a,\eta}^{-1}e_z\rangle.
}
\]

This kernel has exactly

\[
\kappa_a(\eta)
\]

negative squares.

Indeed, \(T_{a,\eta}^{-1}\) has exactly the same inertia as
\(T_{a,\eta}\), and the real exponential family is total in
\(L^2(-a,a)\).

## 6. Generalized-Schur characteristic

Let

\[
\chi_{a,\eta}
\]

be the Pontryagin/Livšic characteristic obtained from the two deficiency
channels by the same boundary quotient as in Suzuki's positive construction.

Its generalized Schur kernel is diagonally congruent to
\(K_{a,\eta}\).

Therefore the negative-square count is preserved exactly:

\[
\boxed{
\chi_{a,\eta}\in S_{\kappa_a(\eta)}.
}
\]

This is the indefinite continuation of Suzuki's ordinary finite Schur theorem.

For

\[
\eta<\lambda_a,
\]

one has \(\kappa_a(\eta)=0\), hence

\[
\chi_{a,\eta}\in S_0,
\]

recovering the previously proved finite Hilbert-space result.

## 7. Cayley form

Define

\[
m_{a,\eta}(z)
=
i\frac{1-\chi_{a,\eta}(z)}
{1+\chi_{a,\eta}(z)}.
\]

The scalar Cayley kernel is diagonally congruent to the generalized Schur
kernel.

Hence

\[
\boxed{
m_{a,\eta}\in N_{\kappa_a(\eta)}.
}
\]

Thus every regular real shift produces a finite generalized-Nevanlinna object
whose index is known exactly from the localized Weil spectrum.

## 8. Shift spectral flow

As a function of the real resolvent parameter,

\[
\boxed{
\eta\mapsto\kappa_a(\eta)
}
\]

is an integer-valued nondecreasing step function.

It jumps by exactly the eigenvalue multiplicity whenever \(\eta\) crosses an
eigenvalue of \(A_a\).

Therefore the generalized-Schur index itself is a spectral-flow counter:

\[
\boxed{
\Delta\kappa_a(\eta)
=
\operatorname{mult}_{A_a}(\eta)
}
\]

at spectral crossings.

The positive Suzuki lane

\[
\eta<\lambda_a
\]

is the index-zero beginning of this flow.

## 9. Near-zero Pontryagin lane

Define

\[
\kappa_a=n_-(A_a)
=
\#\{\lambda_j(A_a)<0\}.
\]

Because the negative spectrum is finite and discrete, there exists

\[
\varepsilon_a>0
\]

such that for every

\[
-\varepsilon_a<\eta<0,
\qquad
\eta\in\rho(A_a),
\]

one has

\[
\boxed{
\kappa_a(\eta)=\kappa_a.
}
\]

This remains true even if

\[
0\in\sigma(A_a),
\]

because the negative shift moves any zero mode to the positive side of
\(T_{a,\eta}\).

Hence one may choose a sequence

\[
\eta_{a,n}\uparrow0,
\qquad
\eta_{a,n}<0,
\qquad
\eta_{a,n}\in\rho(A_a),
\]

with

\[
\boxed{
\chi_{a,\eta_{a,n}}\in S_{\kappa_a}
}
\]

for all sufficiently large \(n\).

## 10. Correction to the earlier near-zero firewall

The earlier statement

\[
\lambda(a)\to0
\Longrightarrow
\text{RH-hard}
\]

was made for the **Hilbert-admissible condition**

\[
\lambda(a)<\lambda_a,
\]

which forces

\[
A_a-\lambda(a)I>0.
\]

That statement remains correct.

The present construction is different.

A Pontryagin shift near zero is only required to satisfy

\[
\eta\in\rho(A_a).
\]

It is allowed to lie above negative eigenvalues, so the metric is indefinite.

Therefore:

\[
\boxed{
\text{Hilbert near-zero shift}
\neq
\text{Pontryagin near-zero shift}.
}
\]

The latter does not assume localized Weil positivity and is not, by itself,
an RH proof.

## 11. Dual-lane structure

The active finite-to-infinite programme now has two complementary routes.

### Tangent lane

The infinitesimal generator

\[
q_a=iH_a
\]

already satisfies

\[
q_a\to Q_\xi
\]

locally uniformly on the zero-free half-plane.

Its finite \(N_\kappa\) index is not yet controlled.

### Pontryagin shift lane

For every regular near-zero real shift,

\[
m_{a,\eta}\in N_{\kappa_a}.
\]

Its finite negative-square index is therefore closed exactly.

The missing theorem is convergence:

\[
\boxed{
m_{a,\eta(a)}
\longrightarrow
(A/B)Q_\xi
}
\]

or equivalently

\[
\boxed{
\chi_{a,\eta(a)}
\longrightarrow
\chi_\infty
}
\]

under a zero-list-free joint \(a\to\infty\), \(\eta(a)\to0\) normalization.

Thus one lane has the limit and lacks the index theorem; the other has the
index theorem and lacks the limit theorem.

## 12. Refined frontier

### LIV-MD2c5SF1 — shifted Pontryagin realization
Status: **CLOSED / PROVED FROM STANDARD REALIZATION THEORY**.

### LIV-MD2c5SF2 — exact finite index
Status: **CLOSED**.

\[
\chi_{a,\eta}\in S_{\kappa_a(\eta)},
\qquad
m_{a,\eta}\in N_{\kappa_a(\eta)}.
\]

### LIV-MD2c5SF3 — near-zero index stabilization
Status: **CLOSED / EXISTENTIAL FINITE-SCALE**.

\[
\eta\uparrow0^-
\Longrightarrow
\kappa_a(\eta)=\kappa_a
\]

after the last negative eigenvalue has been crossed.

### LIV-MD2c5SF4 — Pontryagin characteristic target convergence
Status: **OPEN / PROOF-BEARING**.

Construct a zero-list-free shift schedule and normalization giving

\[
\chi_{a,\eta(a)}\to\chi_\infty.
\]

### LIV-MD2c5SF5 — kernel-at-zero relation case
Status: **OPEN / TECHNICAL**.

Either:
- pass through \(\eta\uparrow0^-\) as above; or
- formulate the exact \(0\)-shift object as a self-adjoint linear relation /
  Pontryagin quotient when \(\ker A_a\ne0\).

The first option already avoids any need to assume invertibility of \(A_a\).

## 13. Compact theorem

For every

\[
\eta\in\rho(A_a)\cap\mathbb R,
\]

the shifted localized Weil metric defines a Pontryagin space with negative
index

\[
\boxed{
\kappa_a(\eta)
=
\#\{\lambda_j(A_a)<\eta\}.
}
\]

The indefinite continuation of Suzuki's finite characteristic satisfies

\[
\boxed{
\chi_{a,\eta}\in S_{\kappa_a(\eta)}
}
\]

and its Cayley transform satisfies

\[
\boxed{
m_{a,\eta}\in N_{\kappa_a(\eta)}.
}
\]

For shifts approaching zero from below after the last negative eigenvalue,

\[
\boxed{
\kappa_a(\eta)=n_-(A_a).
}
\]

This closes the finite-index half of the Pontryagin route without assuming
localized Weil positivity.
