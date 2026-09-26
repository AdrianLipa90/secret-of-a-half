# SOH Generalized-Schur / Xi-Nevanlinna Cayley Crosswalk v0.1

Status: **EXACT_CAYLEY_INDEX_PRESERVATION / EXACT_XI_TARGET_IDENTIFICATION / BOUNDED-INDEX_LIMIT_CLOSURE / FINITE-TO-INFINITE_CONSTRUCTION_OPEN**

Date: 2026-09-26

Parents:
- \`research/SOH_LIVSIC_DENOMINATOR_SHARP_THETA_WEIL_V0_1.md\`
- \`research/SOH_DE_BRANGES_PONTRYAGIN_COMPLEMENT_V0_1.md\`
- \`research/SOH_XI_LOG_DERIVATIVE_GENERALIZED_NEVANLINNA_V0_1.md\`

External standard input:
- scalar generalized Schur and generalized Nevanlinna classes are defined by
  kernels with finitely many negative squares;
- \(\Re[\xi'/\xi](s)>0\) for \(\Re s>1\), so at \(s=3/2\) the constants below
  have positive sign.

No RH and no zero list are used.

## 1. Infinite Livšic target

Let

\[
f(z)=\xi\!\left(\frac12-iz\right).
\]

Put

\[
A=\xi(3/2),
\qquad
B=\xi'(3/2).
\]

The infinite characteristic target already isolated in the Suzuki reduction is

\[
\boxed{
\chi_\infty(z)
=
\frac{
Bf(z)-iAf'(z)
}{
Bf(z)+iAf'(z)
}.
}
\]

The denominator is

\[
D(z)=Bf(z)+iAf'(z),
\]

and the numerator is

\[
D^\#(z)=Bf(z)-iAf'(z).
\]

## 2. Positivity of the normalization constants

For real \(s>1\),

\[
\xi(s)>0
\]

directly from the defining product of positive real factors

\[
\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]

Also the classical zero-free-half-plane positivity gives

\[
\Re\frac{\xi'}{\xi}(s)>0
\qquad
(\Re s>1).
\]

At the real point \(s=3/2\),

\[
\frac{\xi'(3/2)}{\xi(3/2)}>0.
\]

Therefore

\[
\boxed{
A>0,
\qquad
B>0,
\qquad
\frac AB>0.
}
\]

Numerically, only as a regression datum,

\[
A\approx0.5087310387,
\qquad
B\approx0.02347077860,
\qquad
A/B\approx21.67508148.
\]

No numerical sign assumption is used in the proof.

## 3. Cayley transform

For a scalar meromorphic function \(\chi\), define

\[
\boxed{
\mathcal C[\chi](z)
=
i\frac{1-\chi(z)}{1+\chi(z)}.
}
\]

This is the upper-half-plane Cayley transform with the orientation
\(\chi=0\mapsto i\).

Let the generalized Schur kernel be

\[
K_\chi(z,w)
=
\frac{
1-\chi(z)\overline{\chi(w)}
}{
-i(z-\overline w)
}.
\]

Let

\[
q=\mathcal C[\chi].
\]

Then its Nevanlinna kernel is

\[
N_q(z,w)
=
\frac{
q(z)-\overline{q(w)}
}{
z-\overline w
}.
\]

A direct calculation gives

\[
\boxed{
N_q(z,w)
=
\frac{
2
}{
(1+\chi(z))
(1+\overline{\chi(w)})
}
K_\chi(z,w).
}
\]

On every finite point set avoiding poles and \(\chi=-1\), the two Gram matrices
are related by diagonal congruence.

Therefore they have exactly the same inertia.

Hence

\[
\boxed{
\chi\in S_\kappa
\iff
\mathcal C[\chi]\in N_\kappa
}
\]

in the scalar upper-half-plane normalization, with the same number of negative
squares.

This is an algebraic kernel identity, not an appeal to analogy.

## 4. Exact xi target under Cayley

Using

\[
\chi_\infty
=
\frac{Bf-iAf'}{Bf+iAf'},
\]

we obtain

\[
1-\chi_\infty
=
\frac{2iAf'}{Bf+iAf'},
\]

and

\[
1+\chi_\infty
=
\frac{2Bf}{Bf+iAf'}.
\]

Therefore

\[
\mathcal C[\chi_\infty]
=
i
\frac{1-\chi_\infty}{1+\chi_\infty}
=
-\frac AB\frac{f'}f.
\]

Since

\[
Q_\xi=-\frac{f'}f,
\]

we get the exact crosswalk

\[
\boxed{
\mathcal C[\chi_\infty]
=
\frac AB Q_\xi.
}
\]

Because

\[
A/B>0,
\]

multiplication by \(A/B\) does not change the number of negative squares of
the Nevanlinna kernel.

Thus

\[
\boxed{
\chi_\infty\in S_\kappa
\iff
Q_\xi\in N_\kappa.
}
\]

In particular,

\[
\boxed{
\chi_\infty\in S_0
\iff
Q_\xi\in N_0
\iff
\mathrm{RH}.
}
\]

The last equivalence is the exact criterion proved in the parent note; it is
not a proof of RH.

## 5. Bounded-index closure under meromorphic limits

Let

\[
q_n\in N_{\kappa_n},
\qquad
\kappa_n\le K
\]

for one fixed finite integer \(K\).

Assume \(q_n\) converges locally meromorphically on
\(\mathbb C\setminus\mathbb R\) to a nonconstant meromorphic function \(q\),
and the reflection symmetry passes to the limit.

Fix any finite set of points

\[
z_1,\ldots,z_m\in\mathbb C^+
\]

away from poles of \(q\).

For all sufficiently large \(n\), the points avoid poles of \(q_n\), and the
Nevanlinna Gram matrices

\[
G_n
=
\left[
\frac{
q_n(z_j)-\overline{q_n(z_k)}
}{
z_j-\overline{z_k}
}
\right]_{j,k}
\]

converge entrywise to

\[
G
=
\left[
\frac{
q(z_j)-\overline{q(z_k)}
}{
z_j-\overline{z_k}
}
\right]_{j,k}.
\]

Every \(G_n\) has at most \(K\) negative eigenvalues.

Eigenvalues of finite Hermitian matrices are continuous in the matrix entries.
Therefore \(G\) also has at most \(K\) negative eigenvalues.

Since the finite point set was arbitrary,

\[
\boxed{
q\in N_\kappa
\quad
\text{for some }
\kappa\le K.
}
\]

Thus generalized Nevanlinna classes with a uniform finite index bound are
closed downward under the declared local meromorphic limit.

The same statement follows for generalized Schur functions through the Cayley
identity in Section 3.

## 6. Consequence for the localized Pontryagin programme

Suppose a finite-scale scalar characteristic family

\[
\chi_a
\]

is constructed from the de Branges--Pontryagin complement with

\[
\chi_a\in S_{\kappa_a},
\qquad
\kappa_a=n_-(A_a),
\]

and suppose

\[
\chi_a\to\chi_\infty
\]

locally meromorphically on the upper half-plane.

Then

\[
q_a:=\mathcal C[\chi_a]
\in N_{\kappa_a}.
\]

If

\[
\sup_a\kappa_a\le K<\infty,
\]

the closure theorem gives

\[
\frac AB Q_\xi
=
\mathcal C[\chi_\infty]
\in N_\kappa
\]

for some

\[
\kappa\le K.
\]

Therefore

\[
\boxed{
\#_{\rm distinct}
\{\rho:\Re\rho>1/2\}
\le K.
}
\]

This is a genuine consequence of a bounded-index transfer theorem.

It is weaker than RH unless \(K=0\).

## 7. Monotone-index dichotomy

The parent theorem proves

\[
a_1<a_2
\Longrightarrow
\kappa_{a_1}\le\kappa_{a_2}.
\]

Hence \(a\mapsto\kappa_a\) is integer-valued and non-decreasing.

Therefore exactly one of the following happens:

1. \(\kappa_a\) is unbounded as \(a\to\infty\); or
2. \(\kappa_a\) is bounded and hence eventually constant:
   \[
   \kappa_a=K
   \quad
   \text{for all sufficiently large }a.
   \]

If the scalar transfer/convergence theorem is completed, case 2 implies at
most \(K\) distinct right-half off-critical xi-zero locations.

If \(K=0\), RH follows.

If \(K>0\), the result is only a finite-defect theorem; no standard theorem
used here rules out finitely many off-critical zero locations.

## 8. Refined frontier

### LIV-MD2c5C1 — Cayley index preservation
Status: **CLOSED / EXACT**.

\[
S_\kappa
\leftrightarrow
N_\kappa.
\]

### LIV-MD2c5C2 — xi target identification
Status: **CLOSED / EXACT**.

\[
\mathcal C[\chi_\infty]
=
(A/B)Q_\xi,
\qquad
A/B>0.
\]

### LIV-MD2c5C3 — bounded-index limit closure
Status: **CLOSED / EXACT ABSTRACT THEOREM**.

Uniform finite negative-square index survives local meromorphic limits as an
upper bound.

### LIV-MD2c5C4 — finite scalar transfer
Status: **OPEN / STRUCTURAL**.

Construct

\[
\chi_a\in S_{\kappa_a}
\]

from the canonical de Branges--Pontryagin complement, with no inserted
Blaschke data and no zero list.

### LIV-MD2c5C5 — target convergence
Status: **OPEN / ANALYTIC**.

Prove

\[
\chi_a\to\chi_\infty
\]

locally meromorphically under the theta/Weil normalization.

These are now the two proof-bearing gates between the finite localized
negative-square theorem and the xi zero geometry.

## 9. Compact theorem

The infinite Suzuki characteristic and the xi logarithmic derivative satisfy

\[
\boxed{
i\frac{1-\chi_\infty}{1+\chi_\infty}
=
\frac{\xi(3/2)}{\xi'(3/2)}
\,i\frac{\xi'}{\xi}
\left(\frac12-iz\right),
}
\]

with strictly positive scalar prefactor.

The Cayley transform preserves the negative-square index exactly.

Therefore a locally meromorphically convergent finite family

\[
\chi_a\in S_{\kappa_a}
\]

with

\[
\sup_a\kappa_a\le K
\]

would imply

\[
Q_\xi\in N_{\le K}
\]

and hence at most \(K\) distinct right-half off-critical xi-zero locations.

For \(K=0\), this is RH.
