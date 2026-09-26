# SOH Scalarization Rank Barrier for the de Branges–Pontryagin Complement v0.1

Status: **EXACT_RANK_NECESSITY / AUTOMATIC_SCALARIZATION_NO-GO / ACTUAL_RANK_COLLAPSE_OPEN**

Date: 2026-09-26

Parents:
- \`research/SOH_DE_BRANGES_PONTRYAGIN_COMPLEMENT_V0_1.md\`
- \`research/SOH_GENERALIZED_SCHUR_XI_NEVANLINNA_CAYLEY_V0_1.md\`

No RH and no zero list are used.

## 1. Scalar generalized-Schur numerator rank

On the upper half-plane, a scalar generalized Schur kernel has the form

\[
K_s(z,w)
=
\frac{
1-s(z)\overline{s(w)}
}{
-i(z-\overline w)
}.
\]

After multiplication by the scalar denominator,

\[
-i(z-\overline w)K_s(z,w)
=
1-s(z)\overline{s(w)}.
\]

The right-hand side is the difference of two rank-one kernels.

Therefore on every finite sample set its matrix rank is at most two.

More generally, after any nonvanishing scalar gauge

\[
g(z)\overline{g(w)},
\]

the numerator is

\[
g(z)\overline{g(w)}
-
g(z)s(z)
\overline{g(w)s(w)},
\]

again of feature rank at most two.

Thus:

\[
\boxed{
\text{scalar generalized-Schur representation}
\Longrightarrow
\text{gauged displacement rank}\le2.
}
\]

## 2. Scalar de Branges numerator rank

Likewise a scalar de Branges kernel has numerator

\[
E(z)\overline{E(w)}
-
E^\#(z)\overline{E^\#(w)},
\]

again a difference of two rank-one kernels.

Therefore any kernel representable by one scalar de Branges entire function has
displacement rank at most two.

## 3. The localized complement has four natural channels

For the normalized finite Suzuki de Branges kernels,

\[
K_j(z,w)
=
\frac{
\mathcal E_j(z)\overline{\mathcal E_j(w)}
-
\mathcal E_j^\#(z)\overline{\mathcal E_j^\#(w)}
}{
2i(\overline w-z)
},
\qquad
j\in\{0,t\}.
\]

The complement is

\[
L_t=K_0-K_t.
\]

Hence

\[
2i(\overline w-z)L_t(z,w)
=
\mathcal E_0(z)\overline{\mathcal E_0(w)}
-
\mathcal E_0^\#(z)\overline{\mathcal E_0^\#(w)}
-
\mathcal E_t(z)\overline{\mathcal E_t(w)}
+
\mathcal E_t^\#(z)\overline{\mathcal E_t^\#(w)}.
\]

Define the four-channel feature row

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

Then

\[
\boxed{
2i(\overline w-z)L_t(z,w)
=
\Phi_t(z)
J_{2,2}
\Phi_t(w)^*.
}
\]

Thus the natural displacement representation has four scalar channels.

## 4. Necessary scalar-collapse condition

If \(L_t\) admits a scalar generalized-Schur or scalar de Branges
representation after a nonvanishing scalar gauge, then for every finite sample

\[
z_1,\ldots,z_m
\]

the displacement matrix

\[
M_{jk}
=
2i(\overline{z_k}-z_j)L_t(z_j,z_k)
\]

must satisfy

\[
\boxed{
\operatorname{rank}M\le2.
}
\]

Equivalently, every \(3\times3\) minor of every such sample matrix must vanish.

Therefore:

### LIV-MD2c5RANK — scalarization test

\[
\boxed{
\text{scalarization}
\Longrightarrow
\text{all displacement }3\times3\text{ minors vanish}.
}
\]

This condition is gauge invariant under multiplication by nonzero scalar
factors, because diagonal left/right multiplication does not change rank.

## 5. What negative-square index does not imply

The Pontryagin theorem proves that

\[
L_t
\]

has exactly

\[
\kappa_a
\]

negative squares.

That statement controls inertia of Gram matrices.

It does **not** imply displacement rank two.

Inertia and displacement rank are independent structural invariants.

Consequently,

\[
\boxed{
\kappa_a<\infty
\not\Longrightarrow
\text{automatic scalar }S_{\kappa_a}\text{ representation of }L_t.
}
\]

A separate scalar-collapse theorem is required.

## 6. Generic counterexample to automatic scalarization

Take four linearly independent scalar analytic functions

\[
u_1,u_2,u_3,u_4
\]

and form

\[
M(z,w)
=
u_1(z)\overline{u_1(w)}
-u_2(z)\overline{u_2(w)}
-u_3(z)\overline{u_3(w)}
+u_4(z)\overline{u_4(w)}.
\]

For a generic four-point sample, the feature matrix has full rank four and so
does the displacement matrix \(M\).

Therefore a difference of two scalar de Branges-type rank-two numerators can
have rank four.

There is no abstract algebraic theorem reducing such a difference to one
scalar Schur numerator.

This is a structural no-go only for **automatic** scalarization. It does not
assert that the special Suzuki pair fails to collapse.

## 7. Refined finite-transfer frontier

The previous gate

\[
\text{construct scalar }\chi_a\in S_{\kappa_a}
\]

splits into two alternatives.

### LIV-MD2c5C4a — special rank collapse
Status: **OPEN / TESTABLE**.

Prove for the actual Suzuki pair that

\[
\operatorname{rank}
\left[
2i(\overline{z_k}-z_j)L_t(z_j,z_k)
\right]_{j,k}
\le2
\]

for all finite samples.

If true, solve the resulting scalar factorization and continue with the scalar
Cayley route.

### LIV-MD2c5C4b — matrix/J-transfer
Status: **OPEN / NATURAL GENERIC ROUTE**.

If a rank-\(>2\) witness exists, abandon scalarization of the complement and
construct the minimal matrix-valued or \(J\)-contractive transfer associated
with the four-channel displacement.

Then seek a scalar compression only after the matrix transfer is connected to
the xi target.

## 8. Implementation consequence

A future localized Suzuki implementation does not need to guess a scalar
Blaschke factor.

It should first evaluate the exact displacement minors.

The fail-closed rule is:

\[
\boxed{
\exists\text{ certified nonzero }3\times3\text{ minor}
\Longrightarrow
\text{scalar complement transfer rejected}.
}
\]

Conversely, finitely many numerical zero minors are not a proof of rank
collapse; an analytic identity or certified all-domain factorization is
required for promotion.

## 9. Compact theorem

The de Branges--Pontryagin complement has the exact four-channel displacement

\[
\boxed{
2i(\overline w-z)(K_0-K_t)
=
\Phi_t(z)J_{2,2}\Phi_t(w)^*.
}
\]

Any scalar generalized-Schur realization, even after a nonvanishing scalar
gauge, would force the corresponding displacement rank to be at most two.

Hence finite negative-square index alone does not provide a scalar transfer.

The next finite-transfer decision is a concrete rank-collapse test.


## 10. Certified closure update

The prime-free interval certificate now supplies a rigorous four-point witness:

\[
a=69/200,
\qquad
z\in\{i/20,\,3i/20,\,3i/10,\,9i/20\},
\]

with no prime-power contribution and an outward-rounded interval enclosure

\[
\det M
\in
[
7.9960256384132330750131598189604317774\times10^{-17},
\;
7.9960256384132330750141020269547584673\times10^{-17}
].
\]

Hence

\[
\boxed{\operatorname{rank}M=4.}
\]

Therefore the special scalar-collapse gate is no longer open:

\[
\boxed{
\text{LIV-MD2c5C4a = CLOSED NEGATIVELY}.
}
\]

By continuity of the resolvent first correction, the actual finite complement
has the same sampled rank four for all sufficiently small positive admissible
\(t\).

The surviving construction is therefore

\[
\boxed{
\text{LIV-MD2c5C4b = matrix/}J\text{-contractive transfer}.
}
\]

See research/SOH_PRIME_FREE_INTERVAL_RANK4_CERTIFICATE_V0_1.md.
