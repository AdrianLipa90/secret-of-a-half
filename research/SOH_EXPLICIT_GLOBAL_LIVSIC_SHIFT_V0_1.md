# SOH Explicit Global Livšic Shift Schedule v0.1

Status: **LIV-MD1 CLOSED / EXPLICIT UNCONDITIONAL LOWER BOUND / ZERO-LIST-FREE**

Date: 2026-09-26

Parent:
- \`research/SOH_SUZUKI_LIVSIC_SCHUR_REDUCTION_V0_1.md\`
- \`research/SOH_LIVSIC_SCALAR_RESOLVENT_CONDITIONING_V0_1.md\`

Primary source:
- Masatoshi Suzuki, *Weil's quadratic form via the screw function*,
  arXiv:2606.09096v3, especially equations (2.2), (2.5), (4.4), (4.5).

No RH is assumed.

## 1. Source-scaled Rayleigh quotient

Suzuki's scaled formula is

\[
R(a,w)
=
-\log a-(2A+1)
+
\frac{\mathcal L(w)}{\|w\|_2^2}
-
P_a(w)
-
J_a(w),
\]

where

\[
A
=
\frac12(\log(2\pi)+\gamma-1),
\]

\[
\mathcal L(w)
=
\frac14
\int_{-1}^{1}\int_{-1}^{1}
\frac{|w(x)-w(y)|^2}{|x-y|}\,dx\,dy
-
\frac12
\int_{-1}^{1}
|w(x)|^2\log(1-x^2)\,dx,
\]

\(P_a(w)\) is the prime-shift term, and

\[
J_a(w)
=
\frac{a}{\|w\|_2^2}
\int_{-1}^{1}\int_{-1}^{1}
r''(a(x-y))
w(y)\overline{w(x)}\,dx\,dy.
\]

Since \(\log(1-x^2)\le0\) on \((-1,1)\),

\[
\boxed{\mathcal L(w)\ge0.}
\]

Also

\[
\boxed{
2A+1=\log(2\pi)+\gamma.
}
\]

## 2. Prime-shift bound

For \(\tau\ge0\), zero-extend \(w\) outside \([-1,1]\). Then

\[
\left|
\int w(x+\tau)\overline{w(x)}\,dx
\right|
\le
\|w\|_2^2
\]

by Cauchy--Schwarz.

Suzuki's prime term contains two such overlaps for every \(n\), hence

\[
P_a(w)
\le
2\sum_{n\le e^{2a}}
\frac{\Lambda(n)}{\sqrt n}.
\]

Define

\[
\Pi(a)
=
\sum_{n\le e^{2a}}
\frac{\Lambda(n)}{\sqrt n}.
\]

Then

\[
\boxed{
P_a(w)\le2\Pi(a).
}
\]

For a completely elementary closed-form bound, use

\[
\Lambda(n)\le\log n\le2a
\]

and

\[
\sum_{n\le N}n^{-1/2}
\le2\sqrt N.
\]

With \(N=e^{2a}\),

\[
\boxed{
\Pi(a)\le4ae^a.
}
\]

Therefore

\[
\boxed{
P_a(w)\le8ae^a.
}
\]

No prime number theorem is used.

## 3. Exact remainder derivative

Suzuki decomposes

\[
r=r_0+r_1
\]

with

\[
r_0(t)
=
-4(e^{t/2}+e^{-t/2}-2)
\]

and

\[
r_1''(t)
=
\frac{e^{-|t|/2}}{1-e^{-2|t|}}
-
\frac1{2|t|}.
\]

Thus

\[
r_0''(t)
=
-2\cosh(t/2).
\]

For \(t>0\), put \(x=t/2\). Then

\[
r_1''(t)
=
\frac14
\left(
\operatorname{csch}x
+
\operatorname{sech}x
-
\frac1x
\right).
\]

The continuous value at \(t=0\) is

\[
r_1''(0)=\frac14.
\]

## 4. Uniform bound \(|r_1''|\le1/4\)

Because

\[
\sinh x>x
\qquad(x>0),
\]

we have

\[
\operatorname{csch}x-\frac1x<0.
\]

Hence

\[
r_1''(t)
<
\frac14\operatorname{sech}x
\le
\frac14.
\]

For the lower bound, if \(x\ge1\), then

\[
\operatorname{csch}x+\operatorname{sech}x-\frac1x>-1.
\]

If \(0<x<1\), define

\[
F(x)
=
x-(1-x)\sinh x.
\]

Then

\[
F(0)=F'(0)=0
\]

and

\[
F''(x)
=
2\cosh x-(1-x)\sinh x>0.
\]

Therefore \(F(x)>0\), i.e.

\[
\operatorname{csch}x
>
\frac1x-1.
\]

Consequently again

\[
\operatorname{csch}x+\operatorname{sech}x-\frac1x>-1.
\]

Thus for every real \(t\),

\[
\boxed{
|r_1''(t)|\le\frac14.
}
\]

Therefore, for \(|t|\le2a\),

\[
\boxed{
|r''(t)|
\le
2\cosh a+\frac14.
}
\]

## 5. Remainder quadratic-form bound

On \([-1,1]\),

\[
\|w\|_1^2
\le
2\|w\|_2^2.
\]

Hence

\[
\left|
\int_{-1}^{1}\int_{-1}^{1}
r''(a(x-y))
w(y)\overline{w(x)}\,dx\,dy
\right|
\le
\left(2\cosh a+\frac14\right)
\|w\|_1^2
\]

and therefore

\[
\le
2\left(2\cosh a+\frac14\right)\|w\|_2^2.
\]

Thus

\[
\boxed{
|J_a(w)|
\le
4a\cosh a+\frac a2.
}
\]

## 6. Explicit global lower bound

Combining Sections 1--5 gives, for every nonzero admissible \(w\),

\[
R(a,w)
\ge
-\log a
-\log(2\pi)
-\gamma
-8ae^a
-4a\cosh a
-\frac a2.
\]

Define

\[
\boxed{
L_{\rm elem}(a)
=
-\log a
-\log(2\pi)
-\gamma
-8ae^a
-4a\cosh a
-\frac a2.
}
\]

Suzuki's Corollary 1.2 identifies \(\lambda_a\) with the infimum of the
Rayleigh quotient on the compactly supported smooth core. Since the bound above
holds on that core,

\[
\boxed{
\lambda_a\ge L_{\rm elem}(a)
\qquad(a>0).
}
\]

This bound is intentionally crude. Its purpose is admissibility, not spectral
sharpness.

## 7. Explicit Livšic shift schedule

Define

\[
\boxed{
\lambda_{\rm sh}(a)
=
L_{\rm elem}(a)-1.
}
\]

Then for every \(a>0\),

\[
\boxed{
\lambda_{\rm sh}(a)
<
L_{\rm elem}(a)
\le
\lambda_a.
}
\]

Therefore

\[
T_a
=
A_a-\lambda_{\rm sh}(a)I
\]

is strictly positive and invertible for every localization scale \(a>0\),
without RH and without knowing the actual ground-state eigenvalue.

Moreover,

\[
A_a-\lambda_{\rm sh}(a)I
\ge
I,
\]

so

\[
\boxed{
\|T_a^{-1}\|\le1.
}
\]

Thus the admissible-shift problem in the Livšic route is closed globally.

## 8. Stronger arithmetic schedule

If one is willing to evaluate the finite prime-power sum

\[
\Pi(a)
=
\sum_{n\le e^{2a}}
\frac{\Lambda(n)}{\sqrt n},
\]

a less pessimistic lower bound is

\[
\boxed{
L_{\rm pp}(a)
=
-\log a
-\log(2\pi)
-\gamma
-2\Pi(a)
-4a\cosh a
-\frac a2.
}
\]

Then

\[
\lambda_{\rm pp}(a)=L_{\rm pp}(a)-1
\]

is also globally admissible.

The elementary schedule \(L_{\rm elem}\) is preferred as the proof baseline
because it does not require prime enumeration.

## 9. Consequence for the Livšic programme

The previous split was:

- LIV-MD1: construct a computable \(\lambda(a)<\lambda_a\);
- LIV-MD2: prove direct normalized parity-ratio convergence.

This theorem closes LIV-MD1.

The surviving non-circular frontier is therefore

\[
\boxed{
\text{LIV-MD2:
zero-free-axis convergence of }
\frac{C_a(y)-S_a(y)}
{C_a(y)+S_a(y)}.
}
\]

No global Weil positivity is required merely to define the finite Schur family.

## 10. Compact theorem

### Theorem -- explicit unconditional Livšic shift

For every \(a>0\),

\[
\boxed{
\lambda_a
\ge
-\log a-\log(2\pi)-\gamma
-8ae^a
-4a\cosh a
-\frac a2.
}
\]

Hence the explicit zero-list-free schedule

\[
\boxed{
\lambda_{\rm sh}(a)
=
-\log a-\log(2\pi)-\gamma
-8ae^a
-4a\cosh a
-\frac a2-1
}
\]

satisfies

\[
\boxed{
\lambda_{\rm sh}(a)<\lambda_a
}
\]

for all \(a>0\), and

\[
\boxed{
\|(A_a-\lambda_{\rm sh}(a)I)^{-1}\|\le1.
}
\]

Q.E.D.
