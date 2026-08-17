# The Secret of a Half — SOH-G003 Riemann Kernel Derivation

**Status:** EXACT KERNEL DERIVATION; REAL-ROOTEDNESS REMAINS OPEN  
**Branch:** `proof/soh-g003-riemann-kernel-v1`  
**Date:** 17 August 2026

## 1. Starting point: canonical theta–Mellin representation

Use the already-canonical identity from Chapter 16:

\[
\xi(s)=\frac12+\frac{s(s-1)}2\int_1^\infty
\psi(x)\left(x^{s/2}+x^{(1-s)/2}\right)\frac{dx}{x},
\]

where

\[
\psi(x)=\sum_{n=1}^{\infty}e^{-\pi n^2x}.
\]

Put

\[
s=\frac12+z,\qquad x=e^u.
\]

Then

\[
\xi\!\left(\frac12+z\right)
=\frac12+
\left(z^2-\frac14\right)
\int_0^\infty A(u)\cosh\!\left(\frac{zu}{2}\right)du,
\]

with

\[
A(u)=\psi(e^u)e^{u/4}.
\]

Set \(u=2y\) and

\[
B(y)=2A(2y)=2\psi(e^{2y})e^{y/2}.
\]

Hence

\[
\xi\!\left(\frac12+z\right)
=\frac12+
\left(z^2-\frac14\right)
\int_0^\infty B(y)\cosh(zy)\,dy.
\]

## 2. Transfer of the spectral factor to the kernel

Since

\[
\frac{d^2}{dy^2}\cosh(zy)=z^2\cosh(zy),
\]

we may integrate by parts twice. The decay of \(B\) and its derivatives at \(+\infty\), together with \(\sinh(0)=0\), gives

\[
\left(z^2-\frac14\right)
\int_0^\infty B(y)\cosh(zy)\,dy
=
B'(0)+
\int_0^\infty
\left(B''(y)-\frac14B(y)\right)
\cosh(zy)\,dy.
\]

The theta modular relation gives the boundary identity

\[
B'(0)=-\frac12,
\]

which cancels the explicit \(1/2\). Therefore

\[
\boxed{
\xi\!\left(\frac12+z\right)
=
\int_0^\infty \Phi(y)\cosh(zy)\,dy
}
\]

with

\[
\boxed{
\Phi(y)=B''(y)-\frac14B(y).
}
\]

The boundary identity is part of the same theta modular symmetry used to derive the completed-zeta functional equation; it is not an RH assumption.

## 3. Explicit termwise kernel

For one theta term put \(a=\pi n^2\) and

\[
B_n(y)=2\exp\!\left(\frac y2-ae^{2y}\right).
\]

Then

\[
\frac{B_n''}{B_n}
=\frac14-6ae^{2y}+4a^2e^{4y},
\]

so

\[
B_n''-\frac14B_n
=
4a e^{5y/2}\left(2ae^{2y}-3\right)e^{-ae^{2y}}.
\]

Summing over \(n\ge1\) yields

\[
\boxed{
\Phi(y)
=
4\sum_{n=1}^{\infty}
\pi n^2 e^{5y/2}
\left(2\pi n^2e^{2y}-3\right)
\exp\!\left(-\pi n^2e^{2y}\right).
}
\]

## 4. Exact positivity

For \(y\ge0\) and \(n\ge1\),

\[
2\pi n^2e^{2y}-3
\ge 2\pi-3>0.
\]

Every summand is therefore strictly positive. Hence

\[
\boxed{\Phi(y)>0\qquad(y\ge0).}
\]

This is an exact consequence of the canonical theta representation.

## 5. Quotient function F

Let

\[
\xi\!\left(\frac12+z\right)=F(z^2).
\]

Expanding the hyperbolic cosine gives

\[
F(w)
=
\sum_{k=0}^{\infty}
\frac{\mu_{2k}}{(2k)!}w^k,
\qquad
\mu_{2k}=\int_0^\infty \Phi(y)y^{2k}\,dy.
\]

Since \(\Phi>0\),

\[
\boxed{\mu_{2k}>0}
\]

for every \(k\ge0\). Thus every Taylor coefficient of \(F\) is strictly positive and

\[
\boxed{F(x)>0\quad\text{for every }x\ge0.}
\]

Consequently, any real zero of \(F\) is automatically negative.

## 6. What this does and does not solve

**EXACT:**

1. the theta–Mellin representation;
2. the integration-by-parts kernel transfer;
3. the explicit series for \(\Phi\);
4. strict positivity \(\Phi(y)>0\) on \([0,\infty)\);
5. strict positivity of every Taylor coefficient of \(F\);
6. exclusion of \([0,\infty)\) from the zero set of \(F\).

**OPEN:**

\[
\boxed{
\text{SOH-G003: all zeros of }F\text{ are real.}
}
\]

Since positive real zeros are already excluded, SOH-G003 would force every zero of \(F\) onto \(( -\infty,0)\), which is exactly the compactified self-dual half-layer under the global map.

## 7. Classical no-shortcut gate

De Bruijn's 1950 analysis of trigonometric integrals explicitly separates the Riemann kernel problem from the classes for which the universal-factor machinery directly guarantees real zeros. Therefore no claim is made here that positivity of \(\Phi\), monotonicity, or a generic universal-factor theorem already proves SOH-G003.

The next admissible step must establish a genuinely stronger structural property of this exact \(\Phi\), not merely restate real-rootedness in another equivalent language.
