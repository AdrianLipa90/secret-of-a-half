# The Secret of a Half — SOH-G001 Holomorphic Quotient Reduction

**Status:** EXACT ANALYTIC REDUCTION; RH REMAINS OPEN  
**Branch:** `proof/inverse-boundary-global-closure-v1`  
**Date:** 17 August 2026

## 1. Why a second coordinate is needed

The compactified radial coordinate

\[
q(s)=\frac{|\Omega(s)|}{1+|\Omega(s)|},\qquad \Omega(s)=\frac{s}{1-s},
\]

is the exact global geometric coordinate for the reciprocal boundary pair. It sends the inverse-boundary geometry to

\[
0\leftrightarrow 1,\qquad q\mapsto 1-q,
\]

with the unique self-dual layer \(q=1/2\).

Because \(q\) contains an absolute value, it is not holomorphic. The analytic zero problem should therefore be expressed in a holomorphic quotient coordinate that carries the same inversion symmetry.

## 2. Centered entire function and exact quotient

Put

\[
z=s-\frac12,
\qquad
\Xi_c(z):=\xi\!\left(\frac12+z\right).
\]

The functional equation \(\xi(s)=\xi(1-s)\) gives

\[
\Xi_c(z)=\Xi_c(-z).
\]

Hence \(\Xi_c\) is an even entire function. Its Taylor expansion contains only even powers,

\[
\Xi_c(z)=\sum_{n=0}^{\infty} a_{2n}z^{2n}.
\]

Therefore there exists a unique entire function

\[
\boxed{F(w):=\sum_{n=0}^{\infty}a_{2n}w^n}
\]

such that

\[
\boxed{\xi\!\left(\frac12+z\right)=F(z^2).}
\]

This is an exact global factorization through the quotient \(z\sim -z\).

## 3. Relation to the inverse-boundary coordinate

Since

\[
s=\frac{u}{1+u},\qquad u=\Omega(s),
\]

we have

\[
z=s-\frac12
=\frac{u-1}{2(u+1)}.
\]

Thus the quotient coordinate is

\[
\boxed{
w=z^2=\frac{(u-1)^2}{4(u+1)^2}.
}
\]

It is invariant under reciprocal inversion:

\[
w(1/u)
=\frac{(1/u-1)^2}{4(1/u+1)^2}
=\frac{(u-1)^2}{4(u+1)^2}
=w(u).
\]

Therefore the functional involution \(u\leftrightarrow 1/u\) is exactly quotiented out by \(w\).

## 4. Image of the self-dual circle

For \(|u|=1\), write \(u=e^{i\theta}\). Then

\[
\frac{u-1}{u+1}=i\tan\frac{\theta}{2},
\]

so

\[
\boxed{
w=-\frac14\tan^2\frac{\theta}{2}\in(-\infty,0].
}
\]

Conversely, if \(w=z^2\le 0\) is real, then \(z\) is purely imaginary, hence

\[
\Re s=\frac12
\]

and therefore \(|u|=1\) and \(q=1/2\).

Consequently,

\[
\boxed{
q=\frac12
\iff |u|=1
\iff z\in i\mathbb R
\iff w=z^2\in(-\infty,0].
}
\]

## 5. Exact RH reduction

A non-trivial zero \(\rho\) can be written

\[
\rho=\frac12+z_\rho.
\]

Since

\[
\xi(\rho)=F(z_\rho^2),
\]

the Riemann Hypothesis is exactly equivalent to

\[
\boxed{
F(w)=0\Longrightarrow w\in(-\infty,0].
}
\]

for every zero \(w\) corresponding to a non-trivial zero of \(\xi\).

Equivalently, defining

\[
G(x):=F(-x),
\]

RH is exactly the statement

\[
\boxed{
G(x)=0\Longrightarrow x\in[0,\infty).
}
\]

Thus SOH-G001 can be stated without modulus as a real-rootedness problem for a single entire quotient function.

## 6. Relation to the compactified radius

The geometric and analytic reductions are complementary rather than competing:

- \(q\) makes the global projective boundary geometry explicit and has the unique self-dual value \(1/2\);
- \(w=z^2\) is holomorphic and quotients the functional involution exactly;
- the self-dual layer \(q=1/2\) is mapped by \(w\) to the negative real half-axis.

Hence the remaining bridge may be written equivalently as

\[
X(u)=0\Rightarrow q(u)=\frac12,
\]

or

\[
F(w)=0\Rightarrow w\le 0.
\]

The second form is the analytically useful one.

## 7. New proof target

**SOH-G002 — quotient real-rootedness target**

Prove that the entire function \(F\) defined by

\[
\xi\!\left(\frac12+z\right)=F(z^2)
\]

has only non-positive real zeros.

This is exactly equivalent to SOH-G001 and RH; it is not an additional assumption and not a proof by itself.

## 8. Firewall

**EXACT:**

1. \(\Xi_c(z)=\xi(1/2+z)\) is even entire.
2. There is a unique entire \(F\) with \(\Xi_c(z)=F(z^2)\).
3. \(w=(u-1)^2/[4(u+1)^2]\) is invariant under \(u\mapsto1/u\).
4. The unit circle \(|u|=1\) maps exactly to \(( -\infty,0]\) in the \(w\)-coordinate.
5. RH is equivalent to real-rootedness of \(F\) on the non-positive real axis.

**OPEN:** SOH-G002 / SOH-G001 / RH.

No finite-Hermite or moving-boundary condition is required to formulate this target.
