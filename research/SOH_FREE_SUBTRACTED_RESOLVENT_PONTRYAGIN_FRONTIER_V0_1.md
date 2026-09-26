# SOH Free-Subtracted Resolvent Inertia and Pontryagin Frontier v0.1

Status: **EXACT_INERTIA_THEOREM / DIRECT_POSITIVE_RENORMALIZATION_C005_EQUIVALENT / GENERALIZED_SCHUR_REALIZATION_OPEN**

Date: 2026-09-26

Parents:
- \`research/SOH_LIVSIC_DENOMINATOR_SHARP_THETA_WEIL_V0_1.md\`
- \`research/SOH_NEGATIVE_SHIFT_RESOLVENT_WEIL_FIRST_CORRECTION_V0_1.md\`
- \`research/SOH_C005_SPECTRAL_FLOW_FRONTIER_V0_1.md\`

External framework:
- classical Kreĭn--Langer generalized Schur / reproducing-kernel Pontryagin theory:
  a generalized Schur function of index \(\kappa\) is characterized by a Schur
  kernel with \(\kappa\) negative squares and admits a finite
  Kreĭn--Langer Blaschke factorization.

No RH and no zero list are used.

## 1. The direct free-subtracted operator

Fix \(a>0\). Let
\[
A_a=A_a^*
\]
be the localized Suzuki Weil operator, with lowest spectral value
\[
\lambda_a=\inf\sigma(A_a).
\]

Choose
\[
\mu>-\lambda_a.
\]

Then
\[
A_a+\mu I>0.
\]

Define
\[
\boxed{
C_{a,\mu}
=
I-\mu(A_a+\mu I)^{-1}.
}
\]

The resolvent identity gives
\[
\boxed{
C_{a,\mu}
=
A_a(A_a+\mu I)^{-1}.
}
\]

This is exactly the operator that appears when the free leading resolvent
kernel is subtracted before the first-correction scaling.

## 2. Spectral sign is preserved exactly

By the spectral theorem,
\[
C_{a,\mu}
=
\varphi_\mu(A_a),
\qquad
\varphi_\mu(\lambda)
=
\frac{\lambda}{\lambda+\mu}.
\]

Because
\[
\lambda+\mu>0
\qquad
(\lambda\in\sigma(A_a)),
\]
we have
\[
\boxed{
\operatorname{sgn}\varphi_\mu(\lambda)
=
\operatorname{sgn}\lambda.
}
\]

Therefore:
\[
\boxed{
n_-(C_{a,\mu})
=
n_-(A_a),
}
\]
\[
\boxed{
\ker C_{a,\mu}
=
\ker A_a,
}
\]
and similarly the positive spectral subspaces have the same dimension
(in the appropriate infinite-dimensional sense).

Multiplication by the positive scalar \(\mu\) does not change the inertia.

Hence the renormalized first-correction operator
\[
\mu C_{a,\mu}
\]
has the same negative index as \(A_a\).

## 3. Direct positivity is exactly localized Weil positivity

Because \(\varphi_\mu\) preserves sign,
\[
\boxed{
C_{a,\mu}\succeq0
\iff
A_a\succeq0.
}
\]

Thus the most naive attempt to preserve an ordinary positive reproducing
kernel after subtracting the free term,
\[
K_{\rm free}-\mu K_{\rm resolvent},
\]
is positive if and only if the localized Weil operator itself is positive.

For every \(a\), this is exactly the localized C005 condition.

Therefore:

### No-go — direct positive free subtraction

A proof that the direct free-subtracted first-correction kernel is positive for
all \(a\) would already prove the localized Weil positivity statement one is
trying to avoid.

Ordinary Schur positivity cannot be obtained from this subtraction as a free
by-product.

## 4. Exponential evaluation kernel

Let
\[
e_z(x)=e^{-izx},
\qquad x\in[-a,a].
\]

Define the Hermitian kernel
\[
\boxed{
\mathcal K_{a,\mu}(z,w)
=
\langle e_w,C_{a,\mu}e_z\rangle_{L^2(-a,a)}.
}
\]

For any points \(z_1,\ldots,z_m\) and coefficients \(c_1,\ldots,c_m\),
\[
\sum_{j,k}
\overline{c_j}c_k
\mathcal K_{a,\mu}(z_j,z_k)
=
\left\langle
\sum_j c_j e_{z_j},
C_{a,\mu}
\sum_k c_k e_{z_k}
\right\rangle.
\]

Hence every finite Gram matrix has at most
\[
\kappa_a:=n_-(A_a)
\]
negative eigenvalues.

## 5. Exact number of negative squares

The exponential family
\[
\{e_x:x\in\mathbb R\}
\]
is total in \(L^2(-a,a)\).

Since the localized operator has discrete lower-bounded spectrum and its
high-energy spectrum tends upward, its negative spectral subspace is
finite-dimensional.

Let
\[
\kappa_a=n_-(A_a)<\infty.
\]

Choose a basis of the negative spectral subspace. By totality, each basis vector
can be approximated arbitrarily well by finite linear combinations of
exponentials.

Strict negativity of the quadratic form on the finite-dimensional negative
subspace is stable under sufficiently small perturbations.

Therefore some finite exponential Gram matrix has exactly
\(\kappa_a\) negative eigenvalues.

Thus
\[
\boxed{
\mathcal K_{a,\mu}
\text{ has exactly }
\kappa_a
\text{ negative squares}.
}
\]

The number is independent of the admissible \(\mu\).

## 6. The correct indefinite replacement for ordinary Schur

The direct free-subtracted kernel is therefore naturally a reproducing-kernel
Pontryagin object rather than a Hilbert-space kernel whenever
\[
\kappa_a>0.
\]

Classical generalized Schur theory organizes scalar meromorphic functions by
the number of negative squares of their Schur kernels.

For scalar generalized Schur class \(S_\kappa\), the Kreĭn--Langer
factorization has the form
\[
S=B^{-1}S_0
\]
(or the left-factor analogue), where:
- \(S_0\) is ordinary Schur;
- \(B\) is a finite Blaschke product;
- the degree of \(B\) is \(\kappa\).

The present theorem does **not** yet construct the exact scalar generalized
characteristic whose Schur kernel equals \(\mathcal K_{a,\mu}\).

It establishes the inertia data that such a realization must carry.

## 7. Refined renormalization target

The previous gate
\[
\text{Schur-compatible renormalization}
\]
was too restrictive.

The non-circular version is:

### LIV-MD2c5P — Pontryagin/generalized-Schur renormalization

Construct from the free-subtracted Suzuki resolvent a scalar meromorphic
relative characteristic
\[
S_{a,\mu}
\]
such that:

1. its generalized Schur kernel has exactly
   \[
   \kappa_a=n_-(A_a)
   \]
   negative squares;
2. its denominator/numerator retain the exact \(\#\)-symmetry;
3. the Kreĭn--Langer factorization
   \[
   S_{a,\mu}=B_{a,\mu}^{-1}S_{a,\mu}^{(0)}
   \]
   is explicit or controllable;
4. after the theta/Weil normalization, the ordinary-Schur factor converges to
   the desired Suzuki infinite characteristic;
5. the finite Blaschke/Pontryagin defect either vanishes or its poles escape
   every compact subset relevant to the limit;
6. no statement equivalent to \(A_a\ge0\) is inserted upstream.

## 8. Why this is potentially weaker than C005

C005 asks for
\[
\kappa_a=0
\qquad
\text{for every }a.
\]

The generalized-Schur route may instead allow
\[
\kappa_a>0
\]
at finite localization scales, provided the corresponding indefinite defect
does not survive in the limiting characteristic on compact subsets.

Therefore the limit problem
\[
\text{finite negative squares}
\to
\text{escaping defect}
\to
\text{ordinary Schur limit}
\]
is logically weaker than proving finite-\(a\) positivity at every scale.

Whether the required escape can be proved arithmetically is open.

## 9. Important firewall

One must not silently use the Kreĭn--Langer factorization to set
\[
\kappa_a=0.
\]

The factorization records finite negative index; it does not remove it.

Likewise, numerical observation of no negative eigenvalue in a finite
truncation does not prove
\[
n_-(A_a)=0.
\]

## 10. Compact theorem

For every admissible \(\mu>-\lambda_a\),
\[
\boxed{
C_{a,\mu}
=
I-\mu(A_a+\mu I)^{-1}
=
A_a(A_a+\mu I)^{-1}
}
\]
and
\[
\boxed{
n_-(C_{a,\mu})
=
n_-(A_a).
}
\]

The exponential evaluation kernel
\[
\boxed{
\mathcal K_{a,\mu}(z,w)
=
\langle e_w,C_{a,\mu}e_z\rangle
}
\]
has exactly the same number
\[
\boxed{
\kappa_a=n_-(A_a)
}
\]
of negative squares.

Consequently, direct positive-kernel free subtraction is equivalent to
localized Weil positivity, while the natural non-circular replacement is a
Pontryagin/generalized-Schur realization with finite index \(\kappa_a\).
