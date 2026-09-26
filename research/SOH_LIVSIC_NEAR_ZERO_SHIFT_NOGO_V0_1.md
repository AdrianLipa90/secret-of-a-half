# SOH Livšic Near-Zero Shift No-Go and Renormalized Lane v0.1

Status: **EXACT_NEAR_ZERO_SCHEDULE_RH_HARD / EXACT_LAMBDA_SENSITIVITY / RENORMALIZED_NEGATIVE_SHIFT_LANE_OPEN**

Date: 2026-09-26

Parents:
- \`research/SOH_EXPLICIT_GLOBAL_LIVSIC_SHIFT_V0_1.md\`
- \`research/SOH_SUZUKI_LIVSIC_SCHUR_REDUCTION_V0_1.md\`
- \`research/SOH_LIVSIC_SCALAR_RESOLVENT_CONDITIONING_V0_1.md\`

Primary source:
- M. Suzuki, *Weil's quadratic form via the screw function*,
  arXiv:2606.09096v3, especially Corollary 1.6 and the discussion following it.

## 1. Near-zero admissible shifts are already RH-hard

The localized spectral floor satisfies the exact domain-monotonicity relation

\[
a_1<a_2
\quad\Longrightarrow\quad
\lambda_{a_2}\le\lambda_{a_1}.
\]

Suppose there exists a schedule

\[
\lambda_{\rm adm}(a)<\lambda_a
\]

for all sufficiently large \(a\), with

\[
\boxed{
\lambda_{\rm adm}(a)\to0
\qquad(a\to\infty).
}
\]

Then

\[
\lambda_a>\lambda_{\rm adm}(a),
\]

so

\[
\liminf_{a\to\infty}\lambda_a\ge0.
\]

Because \(a\mapsto\lambda_a\) is non-increasing, for every fixed \(a_0\),

\[
\lambda_{a_0}
\ge
\liminf_{a\to\infty}\lambda_a
\ge0.
\]

Hence

\[
\boxed{
\lambda_a\ge0
\qquad\forall a>0.
}
\]

By the standard localized Weil/Yoshida criterion, this is RH.

Therefore:

### Theorem — near-zero admissible-shift no-go

Any independently proved admissible schedule satisfying

\[
\lambda_{\rm adm}(a)<\lambda_a
\quad\text{and}\quad
\lambda_{\rm adm}(a)\to0
\]

already proves RH.

It cannot be treated as a weaker preliminary lemma.

## 2. Agreement with Suzuki v3

Suzuki explicitly notes that the characteristic object depends on the shift
parameter \(\lambda\), and that the conjectural infinite limit is formulated
with \(\lambda=0\) in mind.

The source further states that proving the expected limit may require
\(\lambda=0\) for all sufficiently large \(a\), which is equivalent to RH
through Weil positivity.

The theorem in Section 1 explains this obstruction abstractly from the
spectral-floor monotonicity.

## 3. Exact lambda derivative of the parity ratio

Let

\[
R_\lambda=(A_a-\lambda I)^{-1}
\]

for \(\lambda<\lambda_a\).

On the zero-free imaginary axis, define

\[
C_\lambda(y)
=
\langle c_y,R_\lambda c_1\rangle,
\qquad
S_\lambda(y)
=
\langle s_y,R_\lambda s_1\rangle,
\]

where

\[
c_y(x)=\cosh(yx),
\qquad
s_y(x)=\sinh(yx).
\]

Since

\[
\frac{d}{d\lambda}R_\lambda
=
R_\lambda^2,
\]

we have

\[
C_\lambda'(y)
=
\langle c_y,R_\lambda^2c_1\rangle,
\qquad
S_\lambda'(y)
=
\langle s_y,R_\lambda^2s_1\rangle.
\]

For

\[
Q_\lambda(y)
=
\frac{C_\lambda(y)-S_\lambda(y)}
{C_\lambda(y)+S_\lambda(y)},
\]

direct differentiation gives

\[
\boxed{
Q_\lambda'(y)
=
\frac{
2\left(
S_\lambda C_\lambda'
-
C_\lambda S_\lambda'
\right)
}{
(C_\lambda+S_\lambda)^2
}.
}
\]

Therefore \(\lambda\)-invariance requires the nontrivial identity

\[
\boxed{
S_\lambda C_\lambda'
=
C_\lambda S_\lambda'.
}
\]

Self-adjointness and parity alone do not imply this identity.

Thus the shift parameter cannot be silently removed from the proof graph.

## 4. Fixed-\(a\) very-negative-shift limit

Let

\[
\lambda=-\mu,
\qquad
\mu\to+\infty
\]

with \(a\) fixed.

For a self-adjoint lower-bounded \(A_a\),

\[
\mu(A_a+\mu I)^{-1}
\to I
\]

strongly.

Therefore

\[
\mu
\langle e_{iy},(A_a+\mu I)^{-1}e_{\pm i}\rangle
\to
\langle e_{iy},e_{\pm i}\rangle.
\]

The finite characteristic quotient consequently tends to the free interval
value

\[
\chi_{a,-\infty}(iy)
=
\frac{1-y}{1+y}
\frac{
\langle e^{yx},e^{-x}\rangle
}{
\langle e^{yx},e^{x}\rangle
}.
\]

The elementary integrals give

\[
\boxed{
\chi_{a,-\infty}(iy)
=
-
\frac{
\sinh((y-1)a)
}{
\sinh((y+1)a)
}
}
\]

for \(y\ne1\), with continuous value \(0\) at \(y=1\).

For every fixed \(y>1/2\),

\[
\boxed{
\chi_{a,-\infty}(iy)\to0
\qquad(a\to\infty).
}
\]

The desired infinite zeta target

\[
\chi_\infty(iy)
=
\frac{r_0-r(1/2+y)}
{r_0+r(1/2+y)}
\]

is not identically zero.

Thus an excessively negative shift, without an additional analytic
renormalization mechanism, collapses toward the wrong free characteristic
object in the iterated large-negative-shift / large-\(a\) limit.

This does not by itself determine the joint limit of the explicit schedule
\(\lambda_{\rm sh}(a)\); it is a conditioning/no-go warning, not a claim that
that schedule has already been disproved.

## 5. The only non-circular Livšic lane left

The proof search can no longer rely on either shortcut:

\[
\lambda(a)\to0
\]

because that is RH-hard, or

\[
\lambda(a)\to-\infty
\]

with no renormalization, because the free resolvent dominates at fixed \(a\).

The surviving route is:

### LIV-MD2R — renormalized negative-shift scalar limit

Use a globally admissible zero-list-free schedule, such as the explicit
\(\lambda_{\rm sh}(a)\), and construct an analytic normalization
\(\phi(a,z)\) or equivalent ratio renormalization such that on a zero-free set
\(z=iy,\ y>1/2\),

\[
\boxed{
e^{\phi(a,iy)}
W(a,\lambda_{\rm sh}(a),\theta(a);iy)
\longrightarrow
\frac{
\xi(1/2+y)
}{
\xi(1/2+y)+\xi'(1/2+y)
}.
}
\]

Equivalent normalized parity-ratio formulations are admissible.

The normalization must be derived from arithmetic/operator data and may not
use zeta zeros.

## 6. Stronger preferred target

Because the finite Schur quotient is uniformly bounded in the upper
half-plane, it is enough to prove scalar convergence on any zero-free set
\(Y\subset(1/2,\infty)\) having an interior accumulation point.

Thus the shortest route remains:

\[
\boxed{
\text{explicit admissible negative shift}
+
\text{zero-free renormalized scalar convergence}
}
\]

followed by the already-proved Vitali/identity-theorem endgame.

## 7. Compact status

- explicit global admissible shift: **CLOSED**;
- near-zero admissible shift: **RH-HARD / NO SHORTCUT**;
- generic shift invariance: **NOT DERIVED**;
- fixed-\(a\) very-negative-shift limit: **EXACT FREE-LIMIT**;
- renormalized negative-shift zeta limit: **OPEN**.

This leaves one sharply defined analytic incoming edge rather than an
undifferentiated operator-convergence problem.
