# SOH de Branges–Pontryagin Complement of the Localized Weil Flow v0.1

Status: **EXACT_DE_BRANGES_KERNEL_IDENTITY / EXACT_NEGATIVE_SQUARE_INDEX / GENERALIZED_COMPLEMENT_CONSTRUCTED / KREIN_LANGER_SCALAR_TRANSFER_OPEN**

Date: 2026-09-26

Parents:
- \`research/SOH_SUZUKI_LIVSIC_SCHUR_REDUCTION_V0_1.md\`
- \`research/SOH_FREE_SUBTRACTED_RESOLVENT_PONTRYAGIN_FRONTIER_V0_1.md\`
- \`research/SOH_LIVSIC_DENOMINATOR_SHARP_THETA_WEIL_V0_1.md\`

External framework:
- de Branges reproducing-kernel identity;
- reproducing-kernel Pontryagin spaces;
- Kreĭn--Langer generalized Schur theory.

No RH and no zero list are used.

## 1. Positive metric flow

Fix \(a>0\) and write
\[
A=A_a.
\]

For every
\[
t>0
\]
such that
\[
I+tA>0,
\]
define
\[
T_t=I+tA,
\qquad
R_t=T_t^{-1}.
\]

This is equivalent to the large-negative-shift parameter
\[
\lambda=-t^{-1}
\]
up to the irrelevant positive scalar factor \(t^{-1}\) in the Hilbert metric.

Define
\[
v_z^{(t)}=R_t e_z.
\]

The finite Livšic construction applies because \(T_t>0\).

## 2. Canonical denominator entire function

Let
\[
N_t^2
=
\|v_i^{(t)}\|_{T_t}^2
=
\langle e_i,R_t e_i\rangle
>0.
\]

Define
\[
A_t(z)
=
\langle e_z,R_t e_i\rangle
\]
and
\[
E_t(z)
=
(z+i)A_t(z).
\]

By the exact \(\#\)-symmetry theorem,
\[
E_t^\#(z)
=
(z-i)
\langle e_z,R_t e_{-i}\rangle.
\]

Normalize
\[
\boxed{
\mathcal E_t(z)
=
\frac{E_t(z)}{N_t}.
}
\]

The positive scalar normalization does not change the finite characteristic
quotient.

## 3. Polarized boundary-form identity

Suzuki's deficiency decomposition gives, for every \(z,w\),
\[
W(v_z^{(t)},v_w^{(t)})
=
(z-\overline w)
\langle
v_z^{(t)},v_w^{(t)}
\rangle_{T_t}.
\]

In the canonical equal-norm deficiency basis,
\[
\alpha_t(z)
=
\frac{E_t(z)}
{2iN_t^2},
\qquad
\beta_t(z)
=
-\frac{E_t^\#(z)}
{2iN_t^2}.
\]

Polarizing the finite Schur identity yields
\[
W(v_z^{(t)},v_w^{(t)})
=
2iN_t^2
\left[
\alpha_t(z)\overline{\alpha_t(w)}
-
\beta_t(z)\overline{\beta_t(w)}
\right].
\]

Substitution gives
\[
\boxed{
\langle
v_z^{(t)},v_w^{(t)}
\rangle_{T_t}
=
\frac{
\mathcal E_t(z)\overline{\mathcal E_t(w)}
-
\mathcal E_t^\#(z)\overline{\mathcal E_t^\#(w)}
}{
2i(\overline w-z)
}.
}
\]

Since
\[
\langle
v_z^{(t)},v_w^{(t)}
\rangle_{T_t}
=
\langle
e_w,R_t e_z
\rangle,
\]
we obtain the exact de Branges kernel identity
\[
\boxed{
K_t(z,w)
:=
\frac{
\mathcal E_t(z)\overline{\mathcal E_t(w)}
-
\mathcal E_t^\#(z)\overline{\mathcal E_t^\#(w)}
}{
2i(\overline w-z)
}
=
\langle e_w,R_t e_z\rangle.
}
\]

Thus the finite Suzuki RKHS is exactly a de Branges space in the current
normalization.

## 4. Free system

At
\[
t=0,
\]
we have
\[
R_0=I.
\]

Let
\[
\mathcal E_0
\]
denote the corresponding normalized free denominator.

Then
\[
\boxed{
K_0(z,w)
=
\langle e_w,e_z\rangle.
}
\]

The finite free characteristic is
\[
\chi_{0,a}
=
-\mathcal E_0^\#/\mathcal E_0.
\]

## 5. Exact complementary kernel

Subtract the two de Branges kernels:
\[
K_0(z,w)-K_t(z,w)
=
\langle
e_w,
(I-R_t)e_z
\rangle.
\]

Since
\[
I-R_t
=
I-(I+tA)^{-1}
=
tA(I+tA)^{-1},
\]
we have
\[
\boxed{
K_0-K_t
=
\left\langle
e_w,
tA(I+tA)^{-1}e_z
\right\rangle.
}
\]

This is precisely the free-subtracted first-correction kernel before the
additional \(t^{-1}\) scaling.

## 6. Exact negative-square index

For every spectral value \(\lambda\) of \(A\),
\[
\frac{t\lambda}{1+t\lambda}
\]
has the same sign as \(\lambda\), because \(I+tA>0\).

Hence
\[
n_-\!\left(
tA(I+tA)^{-1}
\right)
=
n_-(A)
=
:\kappa_a.
\]

The real exponential family is total in \(L^2(-a,a)\), so the kernel
\[
K_0-K_t
\]
has exactly the same number of negative squares.

Therefore
\[
\boxed{
K_0-K_t
\text{ has exactly }
\kappa_a=n_-(A_a)
\text{ negative squares.}
}
\]

The index is independent of admissible \(t\).

## 7. Exact positive case

The complementary kernel is positive semidefinite if and only if
\[
A_a\ge0.
\]

Thus
\[
\boxed{
K_0-K_t\succeq0
\iff
A_a\succeq0.
}
\]

When this happens, the finite Suzuki de Branges space is contractively embedded
in the free de Branges space through the direct kernel ordering.

Demanding this positive inclusion for every \(a\) is therefore just the
localized Weil-positivity route in different language.

## 8. Indefinite complement

Without assuming C005, the difference
\[
K_0-K_t
\]
is still a completely canonical reproducing kernel with finite negative index
\(\kappa_a\).

It therefore generates a reproducing-kernel Pontryagin space
\[
\boxed{
\mathcal P_{a,t}
=
\mathcal P(K_0-K_t)
}
\]
of negative index
\[
\boxed{
\operatorname{ind}_-(\mathcal P_{a,t})
=
\kappa_a.
}
\]

This is the exact indefinite complement between the free and localized Suzuki
de Branges kernels.

No ordinary positivity claim is required.

## 9. Connection with generalized Schur theory

Classical Kreĭn--Langer theory says that a scalar generalized Schur function of
index \(\kappa\) has a Schur kernel with exactly \(\kappa\) negative squares and
admits a factorization into an ordinary Schur function and the inverse of a
finite Blaschke product of degree \(\kappa\).

The present theorem supplies the negative-square kernel canonically.

What is still missing is the **explicit scalar transfer function** whose
generalized Schur kernel realizes this exact de Branges complement.

That realization is not inserted by definition.

## 10. Refined operator frontier

### LIV-MD2c5P1 — Pontryagin complement
Status: **CLOSED / EXACT**.

\[
K_0-K_t
\]
is a canonical Pontryagin kernel of index
\[
\kappa_a=n_-(A_a).
\]

### LIV-MD2c5P2 — scalar Kreĭn--Langer transfer
Status: **OPEN**.

Construct an explicit scalar or \(2\times2\) \(J\)-contractive transfer object
whose generalized Schur kernel is equivalent to the complement
\[
K_0-K_t.
\]

### LIV-MD2c5P3 — defect escape
Status: **OPEN**.

Show, without proving \(A_a\ge0\) at every finite \(a\), that the finite
Pontryagin/Kreĭn--Langer defect does not survive on compact subsets in the
\(a\to\infty\) theta/Weil normalized limit.

A sufficient form would be:
- the finite Blaschke poles leave every compact subset of the upper half-plane;
  or
- the negative-square transfer contribution tends locally uniformly to zero.

## 11. Why this route is genuinely different from C005

C005 requires
\[
\kappa_a=0
\quad
\text{for every }a.
\]

The Pontryagin-complement route permits
\[
\kappa_a>0
\]
at finite scales.

It asks only that the corresponding indefinite defect disappear from the
relevant limiting characteristic.

Therefore the new frontier is not a restatement of finite-\(a\) positivity.

Whether defect escape is provable is an open analytic question.

## 12. Compact theorem

With
\[
T_t=I+tA_a>0
\]
and normalized finite denominator \(\mathcal E_t\),
\[
\boxed{
K_t(z,w)
=
\frac{
\mathcal E_t(z)\overline{\mathcal E_t(w)}
-
\mathcal E_t^\#(z)\overline{\mathcal E_t^\#(w)}
}{
2i(\overline w-z)
}
=
\langle e_w,(I+tA_a)^{-1}e_z\rangle.
}
\]

Hence
\[
\boxed{
K_0-K_t
=
\langle
e_w,tA_a(I+tA_a)^{-1}e_z
\rangle
}
\]
has exactly
\[
\boxed{
\kappa_a=n_-(A_a)
}
\]
negative squares.

This constructs the canonical finite de Branges--Pontryagin complement and
isolates scalar transfer/defect escape as the next proof-bearing task.
