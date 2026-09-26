# SOH Minimal 2x2 J-Transfer for the de Branges–Pontryagin Complement v0.1

Status: **EXACT_2x2_TRANSFER_CONSTRUCTED / SCALAR_DIMENSION_REJECTED_PERTURBATIVELY / MINIMAL_TRANSFER_DIMENSION_2 / J-INDEX_AND_XI_LIMIT_OPEN**

Date: 2026-09-26

Parents:
- research/SOH_DE_BRANGES_PONTRYAGIN_COMPLEMENT_V0_1.md
- research/SOH_LOCALIZED_WEIL_RANK3_INTERVAL_CERTIFICATE_V0_1.md
- research/SOH_SCALARIZATION_RANK_BARRIER_V0_1.md

No RH and no zero list are used.

## 1. Free and localized de Branges sections

For the normalized free and localized denominator functions define

\[
u_0(z)
=
\begin{pmatrix}
\mathcal E_0(z)\\
\mathcal E_0^\#(z)
\end{pmatrix},
\qquad
u_t(z)
=
\begin{pmatrix}
\mathcal E_t(z)\\
\mathcal E_t^\#(z)
\end{pmatrix}.
\]

Let

\[
J=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}.
\]

Then the exact de Branges kernels are

\[
2i(\overline w-z)K_j(z,w)
=
u_j(w)^*Ju_j(z),
\qquad
j\in\{0,t\}.
\]

## 2. Relative scalar ratio

Away from zeros of \(\mathcal E_0\), define

\[
\boxed{
r_t(z)
=
\frac{\mathcal E_t(z)}
{\mathcal E_0(z)}.
}
\]

Then automatically

\[
r_t^\#(z)
=
\frac{\mathcal E_t^\#(z)}
{\mathcal E_0^\#(z)}.
\]

Define the diagonal matrix-valued transfer

\[
\boxed{
\Theta_t(z)
=
\begin{pmatrix}
r_t(z)&0\\
0&r_t^\#(z)
\end{pmatrix}.
}
\]

It satisfies

\[
\boxed{
u_t(z)=\Theta_t(z)u_0(z).
}
\]

This identity is meromorphic across free denominator zeros in the usual local
quotient sense.

## 3. Exact J-defect representation

Substitute the relative relation into the kernel difference:

\[
2i(\overline w-z)(K_0-K_t)
=
u_0(w)^*Ju_0(z)
-
u_t(w)^*Ju_t(z).
\]

Hence

\[
\boxed{
2i(\overline w-z)(K_0-K_t)
=
u_0(w)^*
\left[
J-\Theta_t(w)^*J\Theta_t(z)
\right]
u_0(z).
}
\]

Thus the canonical de Branges--Pontryagin complement is an exact compression
of the \(2\times2\) \(J\)-defect kernel of \(\Theta_t\).

No Blaschke data and no spectral zeros are inserted.

## 4. Sharp symmetry of the transfer

Let

\[
\Sigma=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
\]

The diagonal definition gives the exact involution covariance

\[
\boxed{
\Theta_t^\#(z)
=
\Sigma\Theta_t(z)\Sigma.
}
\]

Thus the transfer retains the same numerator/denominator sharp symmetry as the
finite and infinite Livšic systems.

## 5. Why matrix dimension one is insufficient

A scalar generalized-Schur transfer produces a displacement numerator of rank
at most two on every finite sample.

The localized interval certificate proves that the first-correction
displacement at

\[
a=0.6
\]

has a \(3\times3\) sample matrix with

\[
\det M\ne0.
\]

Therefore its rank is three.

If scalar complement representations existed for all sufficiently small
positive \(t\), their displacement matrices would have rank at most two.

But

\[
\frac{K_0-K_t}{t}
\longrightarrow
Q_W^a
\]

in the closed-form first-correction sense. Rank-at-most-two matrices form a
closed algebraic set because all \(3\times3\) minors vanish.

The certified nonzero limiting minor therefore rules out scalar
representability throughout a sufficiently small punctured \(t\)-neighborhood.

Hence:

\[
\boxed{
\text{transfer dimension }1
\text{ is impossible in the perturbative lane.}
}
\]

## 6. Dimension two is sufficient

Section 3 constructs an exact \(2\times2\) transfer for every admissible \(t\).

Therefore, for the localized de Branges--Pontryagin complement,

\[
\boxed{
\text{minimal transfer dimension}=2
}
\]

in the perturbative lane certified by the rank-three first correction.

This is a representation-dimension theorem, not a claim that the full
matrix-valued transfer is already \(J\)-contractive in an ordinary positive
Hilbert sense.

## 7. Relation to the Pontryagin index

The scalar compressed complement

\[
K_0-K_t
\]

has exactly

\[
\kappa_a=n_-(A_a)
\]

negative squares.

The exact matrix \(J\)-defect kernel

\[
\boxed{
\mathbf D_t(z,w)
=
\frac{
J-\Theta_t(w)^*J\Theta_t(z)
}{
2i(\overline w-z)
}
}
\]

is now the natural uncompressed transfer object.

The scalar kernel is its section compression:

\[
\boxed{
K_0(z,w)-K_t(z,w)
=
u_0(w)^*
\mathbf D_t(z,w)
u_0(z).
}
\]

Therefore

\[
\operatorname{ind}_-(K_0-K_t)
\le
\operatorname{ind}_-(\mathbf D_t)
\]

whenever the matrix negative-square index is finite.

Equality has not yet been proved.

## 8. Updated matrix-transfer frontier

### LIV-MD2c5C4a — scalar complement
Status: **CLOSED NEGATIVE / MACHINE-INTERVAL CERTIFIED**.

### LIV-MD2c5C4b1 — exact 2x2 J-transfer
Status: **CLOSED / EXACT**.

\[
\Theta_t
=
\operatorname{diag}(r_t,r_t^\#)
\]

realizes the complement by exact \(J\)-defect compression.

### LIV-MD2c5C4b2 — matrix negative-square index
Status: **OPEN**.

Prove that the full matrix kernel

\[
\mathbf D_t
\]

has finite negative-square index, ideally exactly

\[
\kappa_a.
\]

### LIV-MD2c5C4b3 — matrix-to-xi limit
Status: **OPEN**.

Construct the theta/Weil normalization and Cayley/Potapov transform of
\(\Theta_t\) whose limit contains

\[
Q_\xi(z)
=
i\frac{\xi'}{\xi}
\left(\frac12-iz\right)
\]

as the relevant scalar channel/compression.

## 9. Important firewall

The exact representation

\[
K_0-K_t
=
u_0^*\mathbf D_tu_0
\]

does not imply that the full matrix kernel \(\mathbf D_t\) has the same
negative index as its scalar compression.

Likewise, diagonal form of \(\Theta_t\) does not make it ordinary
\(J\)-contractive.

Those are the next theorems, not assumptions.

## 10. Compact theorem

Let

\[
r_t=\mathcal E_t/\mathcal E_0,
\qquad
\Theta_t=\operatorname{diag}(r_t,r_t^\#).
\]

Then

\[
\boxed{
2i(\overline w-z)(K_0-K_t)
=
u_0(w)^*
[
J-\Theta_t(w)^*J\Theta_t(z)
]
u_0(z).
}
\]

A scalar transfer is excluded in the certified perturbative lane by the
rank-three interval witness, while this \(2\times2\) transfer is exact.

Thus the minimal transfer dimension is two.
