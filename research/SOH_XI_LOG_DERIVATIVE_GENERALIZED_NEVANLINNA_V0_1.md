# SOH Xi Log-Derivative Generalized-Nevanlinna Criterion v0.1

Status: **EXACT_ZERO_TO_POLE_MAP / EXACT_RH_IFF_N0 / CONDITIONAL_NK_OFF-AXIS_COUNT_BOUND / MULTIPLICITY_FIREWALL**

Date: 2026-09-26

Parents:
- \`research/SOH_DE_BRANGES_PONTRYAGIN_COMPLEMENT_V0_1.md\`
- \`research/SOH_FREE_SUBTRACTED_RESOLVENT_PONTRYAGIN_FRONTIER_V0_1.md\`
- \`research/SOH_LOCALIZED_WEIL_NEGATIVE_INDEX_MONOTONICITY_V0_1.md\`

External framework:
- classical scalar generalized Nevanlinna classes \(N_\kappa\);
- classical Laguerre--Pólya / Hadamard product representation.

Primary standard facts used:
- Riemann xi satisfies \(\xi(s)=\xi(1-s)\);
- nontrivial zeta zeros are symmetric about the real axis and the critical
  line;
- \(N_0\) is the ordinary Nevanlinna/Herglotz class;
- a scalar \(N_\kappa\) function has at most \(\kappa\) poles in
  \(\mathbb C^+\).

No RH is assumed unless explicitly stated inside one direction of the
equivalence theorem.

## 1. Centered real-entire xi function

Define

\[
\boxed{
f(z)=\xi\!\left(\frac12-iz\right).
}
\]

The functional equation gives

\[
f(-z)=f(z).
\]

Reality of xi under conjugation together with the functional equation gives

\[
f(\overline z)=\overline{f(z)}.
\]

Thus \(f\) is an even real entire function.

Define its negative logarithmic derivative

\[
\boxed{
Q_\xi(z)
=
-\frac{f'(z)}{f(z)}
=
i\frac{\xi'}{\xi}
\!\left(\frac12-iz\right).
}
\]

Where defined,

\[
Q_\xi(\overline z)=\overline{Q_\xi(z)}.
\]

Therefore \(Q_\xi\) has exactly the symmetry required of a scalar
generalized Nevanlinna candidate.

## 2. Exact zero-to-pole map

Let

\[
\rho=\beta+i\gamma
\]

be a nontrivial zero of \(\xi\).

Solving

\[
\frac12-iz=\rho
\]

gives

\[
\boxed{
z_\rho
=
i\left(\rho-\frac12\right)
=
-\gamma+i\left(\beta-\frac12\right).
}
\]

Hence

\[
\boxed{
\Re\rho>\frac12
\iff
z_\rho\in\mathbb C^+,
}
\]

\[
\boxed{
\Re\rho=\frac12
\iff
z_\rho\in\mathbb R,
}
\]

and

\[
\boxed{
\Re\rho<\frac12
\iff
z_\rho\in\mathbb C^-.
}
\]

If \(\rho\) is a zero of multiplicity \(m\), then the affine substitution
preserves the zero multiplicity of \(f\), and locally

\[
f(z)
=
(z-z_\rho)^m g(z),
\qquad
g(z_\rho)\ne0.
\]

Therefore

\[
\boxed{
Q_\xi(z)
=
-\frac{m}{z-z_\rho}
-\frac{g'(z)}{g(z)}.
}
\]

So every xi zero gives a simple pole of \(Q_\xi\), with residue

\[
\boxed{
\operatorname{Res}_{z=z_\rho}Q_\xi=-m.
}
\]

### Multiplicity firewall

The **order of the pole** of a logarithmic derivative is always one, even when
the underlying zero has multiplicity \(m>1\).

Therefore a theorem bounding the number of poles of an \(N_\kappa\) function
bounds the number of **distinct off-axis zero locations**, not automatically
the sum of their zeta multiplicities.

The zero multiplicity survives in the residue \(-m\), not in the pole order.

## 3. Generalized-Nevanlinna upper bound on off-axis locations

For a scalar generalized Nevanlinna function

\[
Q\in N_\kappa,
\]

the standard Pontryagin-space theory gives at most \(\kappa\) poles in the
open upper half-plane.

Therefore:

### Theorem — conditional right-half zero count

If

\[
\boxed{
Q_\xi\in N_\kappa,
}
\]

then the number of distinct nontrivial xi-zero locations satisfying

\[
\Re\rho>\frac12
\]

is at most \(\kappa\):

\[
\boxed{
\#_{\rm distinct}
\left\{
\rho:
\xi(\rho)=0,\;
\Re\rho>\frac12
\right\}
\le
\kappa.
}
\]

By the functional equation, every left-half off-axis zero has a reflected
right-half partner. Thus a finite \(N_\kappa\) index also implies that the
set of distinct off-critical zero locations is finite.

This implication is one-way. Membership of \(Q_\xi\) in a particular
\(N_\kappa\) class has not been established here for \(\kappa>0\).

## 4. RH implies \(Q_\xi\in N_0\)

Assume RH.

Then every zero of

\[
f(z)=\xi(1/2-iz)
\]

is real.

Because \(f\) is even and of order one, its paired Hadamard product may be
written

\[
\boxed{
f(z)
=
f(0)
\prod_{\gamma>0}
\left(
1-\frac{z^2}{\gamma^2}
\right),
}
\]

where the product ranges over positive real zero ordinates with the usual
multiplicity convention.

The paired product converges because

\[
\sum_{\gamma>0}\frac1{\gamma^2}<\infty.
\]

Taking the logarithmic derivative gives

\[
\boxed{
Q_\xi(z)
=
\sum_{\gamma>0}
\frac{2z}{\gamma^2-z^2}.
}
\]

For each \(\gamma>0\),

\[
\frac{2z}{\gamma^2-z^2}
=
\frac1{\gamma-z}
-
\frac1{\gamma+z}.
\]

If

\[
z=x+iy,
\qquad y>0,
\]

then both terms on the right contribute nonnegative imaginary part, and in
fact their sum has strictly positive imaginary part away from degeneracy.

Therefore

\[
\boxed{
\Im Q_\xi(z)\ge0
\qquad(z\in\mathbb C^+).
}
\]

Hence

\[
\boxed{
Q_\xi\in N_0.
}
\]

Equivalently, under RH the centered xi logarithmic derivative is an ordinary
Nevanlinna/Herglotz function.

## 5. \(Q_\xi\in N_0\) implies RH

Assume

\[
Q_\xi\in N_0.
\]

An \(N_0\) function is holomorphic in \(\mathbb C^+\).

But every xi zero with

\[
\Re\rho>\frac12
\]

would produce a pole of \(Q_\xi\) in \(\mathbb C^+\).

Therefore no such zero exists.

If there were a zero with

\[
\Re\rho<\frac12,
\]

the functional equation would produce the reflected zero

\[
1-\rho
\]

with real part \(>1/2\), contradiction.

Thus every nontrivial zero satisfies

\[
\boxed{
\Re\rho=\frac12.
}
\]

Therefore RH holds.

## 6. Exact criterion

Combining Sections 4 and 5 gives

\[
\boxed{
\mathrm{RH}
\iff
Q_\xi(z)
=
i\frac{\xi'}{\xi}
\!\left(\frac12-iz\right)
\in N_0.
}
\]

Equivalently,

\[
\boxed{
\mathrm{RH}
\iff
-\frac{d}{dz}
\log\xi\!\left(\frac12-iz\right)
\text{ is a Herglotz--Nevanlinna function on }\mathbb C^+.
}
\]

This is a reformulation, not a proof of RH.

## 7. Pontryagin interpretation

The finite localized flow developed in the parent notes produces canonical
kernels with negative-square index

\[
\kappa_a=n_-(A_a).
\]

The theorem above supplies the exact infinite target for a generalized
Nevanlinna transfer:

\[
\boxed{
\text{finite Pontryagin kernel}
\quad\longrightarrow\quad
Q_\xi.
}
\]

If one constructs a scalar transfer family

\[
Q_a\in N_{\kappa_a}
\]

that converges locally meromorphically to \(Q_\xi\), with a uniform finite
index bound

\[
\sup_a\kappa_a\le K<\infty,
\]

and if the generalized-Nevanlinna class is preserved under that limit in the
declared normalization, then

\[
Q_\xi\in N_{\kappa}
\qquad
\text{for some }\kappa\le K,
\]

and consequently there are at most \(K\) distinct right-half off-critical
zero locations.

The special case \(K=0\) would close RH.

No such transfer/limit theorem is asserted here.

## 8. Refined frontier

### LIV-MD2c5N1 — xi zero-to-pole map
Status: **CLOSED / EXACT**.

### LIV-MD2c5N2 — RH iff \(Q_\xi\in N_0\)
Status: **CLOSED / EXACT REFORMULATION**.

### LIV-MD2c5N3 — finite generalized-Nevalinna index bound
Status: **CLOSED CONDITIONALLY ON \(Q_\xi\in N_\kappa\)**.

\[
Q_\xi\in N_\kappa
\Longrightarrow
\#_{\rm distinct}\{\Re\rho>1/2\}\le\kappa.
\]

### LIV-MD2c5N4 — finite-to-infinite transfer
Status: **OPEN / PROOF-BEARING**.

Construct from the localized de Branges--Pontryagin complement a scalar
generalized Nevanlinna transfer

\[
Q_a
\]

whose negative-square index is controlled by \(\kappa_a\), and prove local
meromorphic convergence

\[
Q_a\to Q_\xi.
\]

### LIV-MD2c5N5 — index-zero endgame
Status: **OPEN / RH-EQUIVALENT**.

Prove that the limiting generalized Nevanlinna index is zero without assuming
localized Weil positivity or another RH-equivalent statement upstream.

## 9. Why this is sharper than the previous defect language

The Pontryagin defect now has a direct target meaning.

A nonzero generalized Nevanlinna index allows non-real poles in
\(\mathbb C^+\).

For \(Q_\xi\), those poles are exactly images of distinct xi-zero locations
to the right of the critical line.

Thus the finite negative-square index is not merely an abstract failure of
Hilbert positivity: after a valid transfer theorem it becomes a bound on
off-critical zero locations.

The remaining hard step is the transfer, not the interpretation.

## 10. Compact theorem

Let

\[
f(z)=\xi\!\left(\frac12-iz\right),
\qquad
Q_\xi(z)=-f'(z)/f(z).
\]

Then a zero

\[
\rho=\beta+i\gamma
\]

maps to the pole

\[
\boxed{
z_\rho=-\gamma+i(\beta-1/2).
}
\]

Hence

\[
\boxed{
Q_\xi\in N_\kappa
\Longrightarrow
\#_{\rm distinct}\{\rho:\Re\rho>1/2\}\le\kappa.
}
\]

Moreover,

\[
\boxed{
\mathrm{RH}
\iff
Q_\xi\in N_0.
}
\]

The equivalence is a criterion, not a proof.
