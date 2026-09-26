# SOH Infinitesimal J-Transfer Generator to Xi Log-Derivative v0.1

Status: **EXACT_FINITE_GENERATOR_FORMULA / ZERO-LIST-FREE_LOCAL-UNIFORM_XI_TARGET / NEGATIVE-SQUARE_CLASSIFICATION_OPEN**

Date: 2026-09-26

Parents:
- research/SOH_MINIMAL_2X2_J_TRANSFER_V0_1.md
- research/SOH_PIECEWISE_EXPONENTIAL_WEIL_CROSS_CONVOLUTION_V0_1.md
- research/SOH_GENERALIZED_SCHUR_XI_NEVANLINNA_CAYLEY_V0_1.md

No RH and no zero list are used.

## 1. Relative transfer

Let
\[
R_t=(I+tA_a)^{-1}
\]
for admissible \(t>0\).

Define
\[
A_t(z)
=
\langle e_z,R_t e_i\rangle,
\]
and
\[
N_t^2
=
\langle e_i,R_t e_i\rangle.
\]

The normalized de Branges denominator is
\[
\mathcal E_t(z)
=
\frac{(z+i)A_t(z)}{N_t}.
\]

Relative to the free system,
\[
\boxed{
r_{a,t}(z)
=
\frac{\mathcal E_t(z)}
{\mathcal E_0(z)}.
}
\]

The exact \(2\times2\) transfer is
\[
\Theta_t
=
\operatorname{diag}(r_{a,t},r_{a,t}^\#).
\]

## 2. First derivative at the free point

The resolvent derivative is
\[
\partial_tR_t
=
-R_tA_aR_t.
\]

At \(t=0\),
\[
\partial_tA_t(z)\big|_0
=
-Q_W^a(v_z,v_i).
\]

Also
\[
\partial_tN_t^2\big|_0
=
-Q_W^a(v_i,v_i).
\]

Therefore
\[
\partial_t\log N_t\big|_0
=
-\frac12
\frac{Q_W^a(v_i,v_i)}
{\|v_i\|^2}.
\]

Since the factor \(z+i\) cancels in the relative ratio,

\[
\boxed{
H_a(z)
:=
-\partial_t
\log r_{a,t}(z)
\big|_{t=0}
=
\frac{
Q_W^a(v_z,v_i)
}{
\langle v_z,v_i\rangle
}
-
\frac12
\frac{
Q_W^a(v_i,v_i)
}{
\|v_i\|^2
}.
}
\]

This is an exact finite localized formula.

## 3. Why the deficiency normalization removes \(r_0\)

For
\[
z\in\mathbb C,
\qquad
\Im z>\frac12,
\]
put
\[
s=\frac12-iz.
\]

The finite cross-convolution theorem gives locally uniformly on compact subsets
of this half-plane

\[
\frac{
Q_W^a(v_z,v_i)
}{
\langle v_z,v_i\rangle
}
\longrightarrow
r_0+
\frac{\xi'(s)}{\xi(s)},
\]
where
\[
r_0=\frac{\xi'(3/2)}{\xi(3/2)}.
\]

At the deficiency point \(z=i\),
\[
s=\frac32.
\]

Hence
\[
\frac{
Q_W^a(v_i,v_i)
}{
\|v_i\|^2
}
\longrightarrow
2r_0.
\]

Therefore the factor \(1/2\) in the norm derivative removes exactly one copy of
\(r_0\).

Thus

\[
\boxed{
H_a(z)
\longrightarrow
\frac{\xi'(1/2-iz)}
{\xi(1/2-iz)}
}
\]

locally uniformly on

\[
\Im z>\frac12.
\]

## 4. Direct Nevanlinna target

Define
\[
\boxed{
q_a(z)=iH_a(z).
}
\]

The xi target is
\[
Q_\xi(z)
=
i\frac{\xi'}{\xi}
\left(\frac12-iz\right).
\]

Hence

\[
\boxed{
q_a(z)\longrightarrow Q_\xi(z)
}
\]

locally uniformly on the zero-free half-plane
\[
\Im z>\frac12.
\]

This limit uses only the finite localized Weil form and the explicit
prime/archimedean formula.

No zeta zero table occurs.

## 5. Relation to the matrix J-defect

Write
\[
r_{a,t}(z)
=
1-tH_a(z)+O(t^2)
\]
locally in \(z\).

The top-left entry of the matrix \(J\)-defect satisfies

\[
\frac{
1-r_{a,t}(z)\overline{r_{a,t}(w)}
}{
2i(\overline w-z)t
}
\longrightarrow
\frac{
H_a(z)+\overline{H_a(w)}
}{
2i(\overline w-z)
}.
\]

Because
\[
q_a=iH_a,
\]
its Nevanlinna kernel is

\[
N_{q_a}(z,w)
=
\frac{
q_a(z)-\overline{q_a(w)}
}{
z-\overline w
}
=
2
\frac{
H_a(z)+\overline{H_a(w)}
}{
2i(\overline w-z)
}.
\]

Therefore

\[
\boxed{
\text{top-left first-order J-defect}
=
\frac12N_{q_a}.
}
\]

So the generalized-Nevanlinna target is not added externally: it is the scalar
infinitesimal channel of the exact minimal \(2\times2\) transfer.

## 6. New finite-to-infinite route

The previous matrix-to-xi gate now splits sharply.

### LIV-MD2c5G1 — finite generator formula
Status: **CLOSED / EXACT**.

### LIV-MD2c5G2 — xi target convergence
Status: **CLOSED / ZERO-LIST-FREE ON Im z > 1/2**.

\[
q_a\to Q_\xi.
\]

### LIV-MD2c5G3 — finite negative-square classification
Status: **OPEN / PROOF-BEARING**.

Prove a bound
\[
\boxed{
q_a\in N_{\nu_a},
\qquad
\nu_a\le F(\kappa_a)
}
\]
with a controlled function \(F\), ideally
\[
F(\kappa)=\kappa.
\]

If such a uniform finite-index bound is established and survives the
large-\(a\) continuation/limit, the generalized-Nevanlinna closure theorem
transfers it to \(Q_\xi\).

## 7. Why this is narrower than full matrix convergence

One no longer needs to prove convergence of the entire matrix transfer
\[
\Theta_t
\]
at finite nonzero \(t\).

It is sufficient to classify the negative squares of its scalar infinitesimal
generator
\[
q_a=iH_a
\]
and combine that classification with the already-proved local-uniform target
limit.

Thus the hard structural problem has been reduced to one scalar kernel:

\[
\boxed{
N_{q_a}(z,w)
=
\frac{
q_a(z)-\overline{q_a(w)}
}{
z-\overline w
}.
}
\]

## 8. Firewall

The convergence
\[
q_a\to Q_\xi
\]
is established only first on the already zero-free half-plane
\[
\Im z>1/2.
\]

It does not prove that \(Q_\xi\) belongs to any finite \(N_\kappa\) class on the
whole upper half-plane.

That requires the finite negative-square classification and a continuation
theorem not yet supplied.

Likewise no statement
\[
\nu_a\le\kappa_a
\]
is assumed.

## 9. Compact theorem

For every localized scale \(a\),

\[
\boxed{
H_a(z)
=
\frac{
Q_W^a(v_z,v_i)
}{
\langle v_z,v_i\rangle
}
-
\frac12
\frac{
Q_W^a(v_i,v_i)
}{
\|v_i\|^2
}
=
-\partial_t\log r_{a,t}(z)\big|_{t=0}.
}
\]

On compact subsets of
\[
\Im z>\frac12,
\]
\[
\boxed{
iH_a(z)
\longrightarrow
i\frac{\xi'}{\xi}
\left(\frac12-iz\right)
=
Q_\xi(z).
}
\]

The remaining proof-bearing gate is the generalized-Nevanlinna index of
\(iH_a\).
