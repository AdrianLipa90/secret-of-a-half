# SOH Livšic Denominator-\(\#\) Symmetry and Theta–Weil Factorization v0.1

Status: **EXACT_FINITE_SHARP_SYMMETRY / EXACT_ZERO-FREE_DENOMINATOR_FACTORIZATION / NUMERATOR_GATE_REMOVED / SCHUR-COMPATIBLE_RENORMALIZATION_OPEN**

Date: 2026-09-26

Parents:
- \`research/SOH_SUZUKI_LIVSIC_SCHUR_REDUCTION_V0_1.md\`
- \`research/SOH_PIECEWISE_EXPONENTIAL_WEIL_CROSS_CONVOLUTION_V0_1.md\`
- \`research/SOH_NEGATIVE_SHIFT_RESOLVENT_WEIL_FIRST_CORRECTION_V0_1.md\`
- \`docs/construction/PHASENAV_NATIVE_THETA_BRIDGE.md\`

No RH and no zeta-zero list are used.

## 1. Finite denominator and numerator channels

Fix \(a>0\) and an admissible real shift
\[
\lambda<\lambda_a.
\]

Let
\[
T_{a,\lambda}=A_a-\lambda I>0
\]
and
\[
e_z(x)=e^{-izx}.
\]

In the canonical parity gauge of the Livšic reduction define
\[
A_{a,\lambda}(z)
=
\langle e_z,T_{a,\lambda}^{-1}e_i\rangle,
\]
\[
B_{a,\lambda}(z)
=
\langle e_z,T_{a,\lambda}^{-1}e_{-i}\rangle.
\]

Let
\[
F^\#(z)=\overline{F(\overline z)}.
\]

The localized Weil operator is real and commutes with parity
\[
(Ju)(x)=u(-x).
\]

Hence \(T_{a,\lambda}^{-1}\) is also real and parity commuting.

## 2. Exact sharp symmetry

Let
\[
h_+=T_{a,\lambda}^{-1}e_i.
\]

Because \(e_i(x)=e^x\) is real, \(h_+\) is real. Therefore
\[
A_{a,\lambda}^\#(z)
=
\left\langle e_z,Jh_+\right\rangle.
\]

Since
\[
Jh_+
=
JT_{a,\lambda}^{-1}e_i
=
T_{a,\lambda}^{-1}Je_i
=
T_{a,\lambda}^{-1}e_{-i},
\]
we obtain the exact identity
\[
\boxed{
B_{a,\lambda}(z)
=
A_{a,\lambda}^\#(z).
}
\]

Thus the numerator channel is not independent data.

## 3. Exact finite de Branges/Livšic form

Define
\[
\boxed{
E_{a,\lambda}(z)
=
(z+i)A_{a,\lambda}(z).
}
\]

Then
\[
E_{a,\lambda}^\#(z)
=
(z-i)B_{a,\lambda}(z).
\]

Suzuki's finite characteristic quotient becomes
\[
\boxed{
\chi_{a,\lambda}(z)
=
-
\frac{E_{a,\lambda}^\#(z)}
{E_{a,\lambda}(z)}.
}
\]

The already-proved finite Schur estimate
\[
|\chi_{a,\lambda}(z)|<1
\qquad(\Im z>0)
\]
is therefore exactly the statement
\[
|E_{a,\lambda}^\#(z)|
<
|E_{a,\lambda}(z)|
\]
on the upper half-plane, modulo the harmless global minus sign in the chosen
characteristic normalization.

Hence every finite admissible system is controlled by one denominator entire
function \(E_{a,\lambda}\).

## 4. The centered xi detector is self-dual

Put
\[
\boxed{
f(z)
=
\xi\!\left(\frac12-iz\right).
}
\]

The continuous PhaseNav theta detector equals this \(f\) identically.

Reality of \(\xi\) under conjugation and the functional equation
\[
\xi(s)=\xi(1-s)
\]
give
\[
\boxed{
f^\#=f.
}
\]

The finite theta-Mellin detector has the same algebraic involution covariance;
the continuous detector is the exact limit.

Thus \(f\) is a canonical self-dual scalar factor.

## 5. The denominator bracket is already prime-side

Let
\[
A=\xi(3/2),
\qquad
B=\xi'(3/2),
\qquad
r_0=\frac BA,
\]
and
\[
r(s)=\frac{\xi'(s)}{\xi(s)}.
\]

For
\[
s=\frac12-iz,
\qquad
\Im z>\frac12,
\]
the piecewise-exponential Weil theorem gives the zero-list-free denominator
bracket
\[
\boxed{
r_0+r(s).
}
\]

Since
\[
f'(z)=-i\xi'(s),
\]
we have
\[
iAf'(z)=A\xi'(s).
\]

Therefore
\[
\boxed{
A\,f(z)\,[r_0+r(s)]
=
Bf(z)+iAf'(z).
}
\]

Define
\[
\boxed{
D(z)=Bf(z)+iAf'(z).
}
\]

The target denominator entire function is thus the product of two already
constructed zero-list-free objects:
- the exact theta-Mellin detector \(f\);
- the zero-free prime/Weil logarithmic-derivative bracket \(r_0+r(s)\).

## 6. The target numerator is forced by \(\#\)

Because
\[
f^\#=f
\]
and \(A,B\in\mathbb R\),
\[
\boxed{
D^\#(z)
=
Bf(z)-iAf'(z).
}
\]

Call
\[
N(z)=D^\#(z).
\]

Then
\[
\boxed{
\chi_\infty(z)
=
\frac{N(z)}{D(z)}
=
\frac{Bf(z)-iAf'(z)}
{Bf(z)+iAf'(z)}.
}
\]

Thus the infinite numerator does not require a separate divergent prime-side
evaluation.

It is the \(\#\)-reflection of the denominator.

On the zero-free axis \(z=iy,\ y>1/2\),
\[
D(iy)
=
A\xi(1/2+y)
\left[
r_0+r(1/2+y)
\right],
\]
while functional symmetry gives the reflected bracket automatically.

## 7. First-correction subtraction preserves \(\#\)

Write
\[
\lambda=-\mu,
\qquad
t=\mu^{-1},
\]
and remove the irrelevant scalar \(\mu^{-1}\) from the resolvent by setting
\[
\widetilde A_{a,t}(z)
=
\left\langle
e_z,
(I+tA_a)^{-1}e_i
\right\rangle.
\]

Let
\[
I_{a,+}(z)=\langle e_z,e_i\rangle.
\]

Define the denominator first-difference quotient
\[
\boxed{
H_{a,t}(z)
=
\frac{
I_{a,+}(z)-\widetilde A_{a,t}(z)
}{t}.
}
\]

Because the exact relation
\[
\widetilde B_{a,t}
=
\widetilde A_{a,t}^{\#}
\]
holds for every admissible \(t\), subtraction and division by the real scalar
\(t\) give
\[
\boxed{
H_{a,t}^{\#}(z)
=
\frac{
I_{a,-}(z)-\widetilde B_{a,t}(z)
}{t}.
}
\]

Hence the negative-shift first-correction procedure preserves the
denominator/numerator \(\#\)-pair **exactly** before any limit is taken.

For fixed \(a\),
\[
H_{a,t}(z)
\to
\langle e_z,A_a e_i\rangle
\]
in the closed-form sense encoded by the previously proved resolvent
first-correction theorem.

## 8. Self-dual common factors do not change the characteristic quotient

Let \(\Theta(z)\) be any entire self-dual factor
\[
\Theta^\#=\Theta.
\]

Where common zeros are removed in the usual analytic sense,
\[
-\frac{(\Theta E)^\#}{\Theta E}
=
-\frac{\Theta E^\#}{\Theta E}
=
-\frac{E^\#}{E}.
\]

Therefore the exact continuous theta detector \(f\), and any finite
theta-Mellin detector with the declared self-dual algebraic covariance, may be
attached as a common numerator/denominator factor without changing the finite
characteristic quotient.

This is a **gauge/common-factor statement only**. It does not assert that the
multiplied function is Hermite--Biehler at common zeros.

## 9. What has been removed from the frontier

The following is no longer an independent gate:

> derive the \(e_{-i}\) numerator from an absolutely convergent prime-side
> series.

That route is unnecessary and, on its face, lies outside the absolute
Dirichlet half-plane.

The exact finite identity
\[
B=A^\#
\]
and the exact infinite identity
\[
N=D^\#
\]
show that one denominator channel is sufficient.

## 10. The surviving structural gate

The negative-shift first correction extracts the correct denominator
logarithmic-derivative information, but subtraction of the free leading term
does not automatically preserve the finite Schur/Hermite--Biehler inequality.

Therefore the remaining structural problem is:

### LIV-MD2c5R — \(\#\)-equivariant Schur-compatible renormalization

Construct a renormalization
\[
\mathcal T_a
\]
of the finite denominator entire functions such that:

1. \(\mathcal T_a\) commutes with \(\#\);
2. it removes the free large-negative-shift term;
3. the resulting denominator converges, after a self-dual theta factor if
   useful, to
   \[
   D(z)=Bf(z)+iAf'(z);
   \]
4. the associated quotient
   \[
   -\frac{
   [\mathcal T_a E_{a,\lambda}]^\#
   }{
   \mathcal T_a E_{a,\lambda}
   }
   \]
   remains Schur, generalized-Schur with a controlled index, or is linked by a
   proved \(J\)-contractive transfer law to the original finite Schur family;
5. no RH-equivalent positivity or zero table is used.

This is sharper than asking separately for numerator and denominator
convergence.

## 11. Useful no-go

A plain affine subtraction
\[
E\mapsto E-E_{\rm free}
\]
does commute with \(\#\), but the difference of two Hermite--Biehler functions
need not be Hermite--Biehler.

Therefore:
\[
\boxed{
\#\text{-equivariance alone is insufficient;}
}
\]
the missing property is a Schur/\(J\)-contractive stability theorem for the
renormalization.

## 12. Compact theorem

For every finite admissible localized Suzuki system,
\[
\boxed{
B_{a,\lambda}=A_{a,\lambda}^{\#}
}
\]
and
\[
\boxed{
\chi_{a,\lambda}
=
-
E_{a,\lambda}^{\#}/E_{a,\lambda},
\qquad
E_{a,\lambda}=(z+i)A_{a,\lambda}.
}
\]

For the infinite target,
\[
\boxed{
D(z)
=
A\,\xi(1/2-iz)
\left[
r_0+
\frac{\xi'(1/2-iz)}{\xi(1/2-iz)}
\right]
=
Bf(z)+iAf'(z),
}
\]
and
\[
\boxed{
N=D^\#.
}
\]

Thus the numerator is exactly forced by the denominator through the same
\(\#\)-symmetry at finite and infinite level. The remaining proof-bearing
problem is Schur-compatible renormalization of the denominator channel.
