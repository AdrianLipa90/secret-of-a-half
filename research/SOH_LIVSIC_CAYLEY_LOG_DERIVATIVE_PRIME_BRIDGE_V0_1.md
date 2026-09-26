# SOH Livšic Cayley–Log-Derivative Prime-Side Bridge v0.1

Status: **EXACT_CAYLEY_REDUCTION / ZERO-FREE_PRIME_TARGET / EXPLICIT_EXPONENTIAL_TAIL / FINITE_OPERATOR_MATCH_OPEN**

Date: 2026-09-26

Parents:
- \`research/SOH_SUZUKI_LIVSIC_SCHUR_REDUCTION_V0_1.md\`
- \`research/SOH_LIVSIC_NEAR_ZERO_SHIFT_NOGO_V0_1.md\`

## 1. Infinite characteristic quotient

Write

\[
f(z)=\xi\!\left(\frac12-iz\right),
\]

\[
A=\xi(3/2),
\qquad
B=\xi'(3/2),
\qquad
r_0=\frac BA=\frac{\xi'(3/2)}{\xi(3/2)}.
\]

The normalized infinite characteristic candidate is

\[
\chi_\infty(z)
=
\frac{Bf(z)-iAf'(z)}
{Bf(z)+iAf'(z)}.
\]

Then

\[
1-\chi_\infty
=
\frac{2iAf'}{Bf+iAf'},
\]

\[
1+\chi_\infty
=
\frac{2Bf}{Bf+iAf'}.
\]

Therefore

\[
\boxed{
-i r_0
\frac{1-\chi_\infty(z)}
{1+\chi_\infty(z)}
=
\frac{f'(z)}{f(z)}.
}
\]

This is exact wherever the quotient is defined, with meromorphic continuation
through the standard logarithmic derivative.

## 2. Zero-free imaginary-axis target

Let

\[
z=iy,
\qquad
y>\frac12,
\]

and put

\[
s=\frac12+y>1.
\]

Then

\[
f(iy)=\xi(s),
\qquad
f'(iy)=-i\xi'(s).
\]

Hence

\[
\boxed{
r_0
\frac{1-\chi_\infty(iy)}
{1+\chi_\infty(iy)}
=
\frac{\xi'(s)}{\xi(s)}.
}
\]

Thus the Livšic scalar convergence target is equivalent to convergence of a
Cayley-transformed finite Schur function to the classical logarithmic
derivative on the absolutely convergent half-plane.

## 3. Finite Cayley/Weyl observable

For any finite admissible Schur quotient

\[
\chi_{a,\lambda}(z),
\qquad
|\chi_{a,\lambda}(z)|<1
\quad(\Im z>0),
\]

define

\[
\boxed{
\mathfrak r_{a,\lambda}(y)
=
r_0
\frac{
1-\chi_{a,\lambda}(iy)
}{
1+\chi_{a,\lambda}(iy)
}.
}
\]

Because \(|\chi|<1\), the denominator cannot vanish.

The surviving Livšic target becomes

\[
\boxed{
\mathfrak r_{a,\lambda(a)}(y)
\longrightarrow
\frac{\xi'(1/2+y)}
{\xi(1/2+y)}
}
\]

on any zero-free set \(Y\subset(1/2,\infty)\) with an accumulation point.

This is equivalent to the previous characteristic-ratio target but is
arithmetically more transparent.

## 4. Prime-side formula for \(\xi'/\xi\)

Suzuki uses

\[
\xi(s)
=
s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]

Therefore for \(s>1\),

\[
\boxed{
\frac{\xi'(s)}{\xi(s)}
=
\frac1s
+
\frac1{s-1}
-
\frac12\log\pi
+
\frac12\psi(s/2)
-
\sum_{n=2}^{\infty}
\frac{\Lambda(n)}{n^s}.
}
\]

The Dirichlet series is absolutely convergent.

No zeta zero is used.

## 5. Natural finite-\(a\) arithmetic truncation

The localized Suzuki form sees prime powers only through

\[
\log n\le2a,
\]

equivalently

\[
n\le e^{2a}.
\]

Let

\[
M_a=\lfloor e^{2a}\rfloor.
\]

Define the zero-list-free finite target

\[
\boxed{
r_{\le M_a}(s)
=
\frac1s
+
\frac1{s-1}
-
\frac12\log\pi
+
\frac12\psi(s/2)
-
\sum_{n\le M_a}
\frac{\Lambda(n)}{n^s}.
}
\]

This uses exactly the same prime-power support scale as the finite localized
operator.

## 6. Explicit tail bound

For \(s>1\),

\[
0
\le
\sum_{n>M}
\frac{\Lambda(n)}{n^s}
\le
\sum_{n>M}
\frac{\log n}{n^s}.
\]

For \(M\ge e\), the function

\[
x\mapsto\frac{\log x}{x^s}
\]

is decreasing. Therefore

\[
\sum_{n>M}\frac{\log n}{n^s}
\le
\int_M^\infty
\frac{\log x}{x^s}\,dx.
\]

Direct integration gives

\[
\boxed{
\int_M^\infty
\frac{\log x}{x^s}\,dx
=
M^{1-s}
\left(
\frac{\log M}{s-1}
+
\frac1{(s-1)^2}
\right).
}
\]

Hence, for \(a\ge1/2\),

\[
\boxed{
\left|
\frac{\xi'(s)}{\xi(s)}
-
r_{\le M_a}(s)
\right|
\le
M_a^{1-s}
\left(
\frac{\log M_a}{s-1}
+
\frac1{(s-1)^2}
\right).
}
\]

## 7. Uniform zero-free compact bound

Fix

\[
s\ge1+\eta,
\qquad
\eta>0.
\]

Then

\[
M_a^{1-s}\le M_a^{-\eta}
\]

and

\[
\boxed{
\left|
\frac{\xi'(s)}{\xi(s)}
-
r_{\le M_a}(s)
\right|
\le
M_a^{-\eta}
\left(
\frac{\log M_a}{\eta}
+
\frac1{\eta^2}
\right).
}
\]

Since

\[
M_a=e^{2a+o(1)},
\]

the tail is

\[
\boxed{
O_\eta(ae^{-2a\eta}).
}
\]

Thus on every compact subset of \(s>1\), the exact prime-side target is
approximated exponentially well by the prime powers already visible to the
finite localized Suzuki operator.

## 8. Updated LIV-MD2 decomposition

The old scalar convergence problem now splits into a closed arithmetic part and
one finite-operator comparison.

### LIV-MD2a — Cayley/log-derivative equivalence
Status: **CLOSED / EXACT**.

\[
\mathfrak r_\infty(y)
=
\xi'(1/2+y)/\xi(1/2+y).
\]

### LIV-MD2b — prime truncation
Status: **CLOSED / EXACT + EXPLICIT TAIL**.

The finite arithmetic target \(r_{\le M_a}(s)\) differs from the full target by
\(O_\eta(ae^{-2a\eta})\) on \(s\ge1+\eta\).

### LIV-MD2c — finite operator to finite prime target
Status: **OPEN**.

Prove for a zero-list-free admissible shift/renormalization that

\[
\boxed{
\mathfrak r_{a,\lambda(a)}(y)
-
r_{\le M_a}(1/2+y)
\to0
}
\]

on a zero-free set \(y>1/2\) with an accumulation point.

This is now the only nontrivial analytic comparison in the Livšic lane.

## 9. Why this target is substantially narrower

The full zeta object no longer appears on both sides.

The target is a finite, explicit arithmetic scalar built from:
- the gamma/digamma factor;
- pole terms;
- finitely many von Mangoldt weights \(n\le e^{2a}\).

Those are exactly the structural ingredients already present in the localized
Weil operator.

The remaining task is therefore a finite-interval resolvent/boundary-form
identity or asymptotic, not an independent reconstruction of the zeta zeros.

## 10. Compact theorem

### Theorem — zero-free prime-side Livšic target

For \(s=1/2+y>1\),

\[
\boxed{
r_0
\frac{1-\chi_\infty(iy)}
{1+\chi_\infty(iy)}
=
\frac{\xi'(s)}{\xi(s)}.
}
\]

Let \(M_a=\lfloor e^{2a}\rfloor\). Then for \(s\ge1+\eta\),

\[
\boxed{
\left|
\frac{\xi'(s)}{\xi(s)}
-
r_{\le M_a}(s)
\right|
\le
M_a^{-\eta}
\left(
\frac{\log M_a}{\eta}
+
\frac1{\eta^2}
\right).
}
\]

Therefore proving

\[
\mathfrak r_{a,\lambda(a)}(y)
-
r_{\le M_a}(1/2+y)
\to0
\]

on a zero-free accumulation set is sufficient for the existing
Vitali/identity-theorem RH endgame.

Q.E.D. for the reduction.
