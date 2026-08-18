# SOH-G011 — Forced Complex Crossings and Euler Half-Period Structure

## Status

**THEOREM-LEVEL REDUCTION / PROVED FOR THE FORCED PAIR.**

This note proves the existence and simplicity of the reciprocal fixed-point pair of the xi scale defect. It does **not** prove that these are the only complex zeros of the scale defect and does **not** prove SOH-G003 or RH.

## Definitions

Let

\[
X(u)=\xi\!\left(\frac{u}{1+u}\right),
\qquad
\Delta_a(u)=X(au)-X(u),
\qquad a>1.
\]

Write

\[
u=e^\lambda,\qquad L=\log a,
\qquad
D_a(\lambda)=\Delta_a(e^\lambda).
\]

From the functional equation of completed xi,

\[
X(u)=X(1/u).
\]

Hence

\[
D_a(-L-\lambda)=-D_a(\lambda),
\]

and exponential uniformization gives

\[
D_a(\lambda+2\pi i)=D_a(\lambda).
\]

## Theorem 1 — forced logarithmic crossing family

The fixed points of the defect involution modulo the logarithmic period solve

\[
\lambda=-L-\lambda+2\pi i k.
\]

Therefore

\[
\boxed{\lambda_k=-\frac{L}{2}+\pi i k},\qquad k\in\mathbb Z,
\]

and every such point satisfies

\[
D_a(\lambda_k)=0.
\]

Exponentiation collapses the infinite logarithmic family to two classes:

\[
\boxed{u_+=a^{-1/2}},
\qquad
\boxed{u_-=-a^{-1/2}}.
\]

Equivalently, these are exactly the two fixed points of

\[
I_a(u)=\frac{1}{au}.
\]

## Theorem 2 — Euler half-turn exchanges the two classes

Successive logarithmic representatives obey

\[
\lambda_{k+1}=\lambda_k+\pi i.
\]

Euler's identity gives

\[
e^{i\pi}=-1,
\]

so

\[
\boxed{e^{\lambda_{k+1}}=-e^{\lambda_k}}.
\]

Thus the half-period \(\pi i\) exchanges the positive and negative forced crossing classes, while the full period \(2\pi i\) returns to the same \(u\)-point.

This is an exact use of Euler phase, not an analogy.

## Theorem 3 — both forced zeros are simple

Use the already established centered entire factorization

\[
\xi\!\left(\frac12+z\right)=F(z^2),
\]

with strictly positive Taylor coefficients

\[
F(w)=\sum_{n\ge0}a_n w^n,
\qquad a_n>0.
\]

Under \(u=e^\lambda\),

\[
X(e^\lambda)
=F\!\left(\frac14\tanh^2\frac\lambda2\right).
\]

Set

\[
w(\lambda)=\frac14\tanh^2\frac\lambda2.
\]

Because \(a_n>0\),

\[
F'(w)>0\qquad(w>0).
\]

Differentiating the defect and using evenness plus \(2\pi i\)-periodicity gives

\[
D_a'(\lambda_k)
=2\,\frac{d}{d\lambda}X(e^\lambda)
\Big|_{\lambda=L/2+\pi i k}.
\]

For even \(k\),

\[
w=\frac14\tanh^2\frac{L}{4}>0.
\]

For odd \(k\), the Euler half-period shifts the hyperbolic coordinate by \(i\pi/2\), so

\[
\tanh\!\left(z+\frac{i\pi}{2}\right)=\coth z
\]

and therefore

\[
w=\frac14\coth^2\frac{L}{4}>0.
\]

In both parity classes, \(w'(\lambda)\neq0\) because \(L>0\). Consequently

\[
F'(w)w'(\lambda)\neq0
\]

and hence

\[
\boxed{D_a'(\lambda_k)\neq0}.
\]

Therefore both \(u=+a^{-1/2}\) and \(u=-a^{-1/2}\) are simple forced zeros of \(\Delta_a\).

## Specialization to the Uroboros scale

For \(a=32=2^5\),

\[
L=5\log2,
\qquad
\lambda_k=-\frac52\log2+\pi i k,
\]

and

\[
\boxed{u_\pm=\pm\frac1{\sqrt{32}}}.
\]

The Euler half-turn exchanges these two classes exactly.

## Proof firewall

Proved here:

- reciprocal scale-defect antisymmetry;
- logarithmic half-period crossing family;
- Euler sign exchange between the two forced classes;
- simplicity of the two forced zeros.

Not proved here:

- absence of additional complex zeros of \(\Delta_a\);
- injectivity or global value-separation of \(F\);
- PF-infinity;
- SOH-G003 real-rootedness;
- the Riemann hypothesis.
