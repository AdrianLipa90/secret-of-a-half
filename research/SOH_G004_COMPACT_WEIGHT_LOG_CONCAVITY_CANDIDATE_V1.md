# SOH-G004 — Compactified-kernel log-concavity candidate

**Status:** OPEN CANDIDATE — NOT PROMOTED  
**Branch:** `proof/soh-g003-modular-kernel-v2`  
**Date:** 17 August 2026

## 1. Exact setup

Let

\[
\xi\!\left(\frac12+z\right)
=\int_0^\infty \Phi(y)\cosh(zy)\,dy
\]

with the exact positive Riemann kernel \(\Phi(y)>0\) for \(y\ge0\).  Introduce

\[
\eta=\tanh y,\qquad y=\operatorname{artanh}\eta,
\]

and the compactified weight

\[
W(\eta)=\frac{\Phi(\operatorname{artanh}\eta)}{1-\eta^2},
\qquad 0\le \eta<1.
\]

Equivalently,

\[
\xi\!\left(\frac12+z\right)
=\int_0^1 W(\eta)
\cosh\!\bigl(z\operatorname{artanh}\eta\bigr)\,d\eta.
\]

The modular involution is \(\eta\mapsto-\eta\), with the self-dual point at \(\eta=0\).

## 2. Exact curvature reduction

Set

\[
L(y)=\log\Phi(y).
\]

Since

\[
\log W(\eta)
=L(\operatorname{artanh}\eta)-\log(1-\eta^2),
\]

a direct differentiation gives

\[
\boxed{
\frac{d^2}{d\eta^2}\log W(\eta)
=
\frac{
L''(y)+2\tanh y\,L'(y)+2\bigl(1+\tanh^2 y\bigr)
}{
\bigl(1-\tanh^2 y\bigr)^2
},
\qquad y=\operatorname{artanh}\eta.
}
\]

Therefore strict log-concavity of the compactified weight,

\[
\frac{d^2}{d\eta^2}\log W(\eta)<0,
\qquad 0<\eta<1,
\]

is exactly equivalent to the kernel inequality

\[
\boxed{
L''(y)+2\tanh y\,L'(y)
+2\bigl(1+\tanh^2 y\bigr)<0,
\qquad y>0.
}
\]

This is a single explicit analytic inequality for the exact Riemann kernel; no Hermite truncation and no zero input occurs.

## 3. Numerical falsification screen

A high-precision numerical screen of the exact finite kernel evaluation found no sign violation of

\[
\frac{d^2}{d\eta^2}\log W(\eta)<0
\]

on a dense sample of \(\eta\in(0,1)\). Representative values were

\[
\left.\frac{d^2}{d\eta^2}\log W\right|_{\eta=0.01}
\approx -16.7409495,
\]

and

\[
\left.\frac{d^2}{d\eta^2}\log W\right|_{\eta=0.98}
\approx -1.56267195\times10^6.
\]

These values are **diagnostic only**. They do not prove the inequality on the continuum and do not prove real-rootedness.

## 4. Proof target

**SOH-G004 candidate.** Prove

\[
L''(y)+2\tanh y\,L'(y)
+2\bigl(1+\tanh^2 y\bigr)<0
\]

for every \(y>0\), where \(L=\log\Phi\).

If established, this would promote strict log-concavity of the exact compactified Riemann weight from numerical evidence to a theorem.

## 5. Firewall

**EXACT:** the change of variables and the curvature identity above.

**NUMERICAL EVIDENCE ONLY:** sampled negativity of the curvature.

**OPEN:** SOH-G004, any implication from SOH-G004 to total positivity or real-rootedness of the quotient entire function \(F\), SOH-G003, and RH.

Log-concavity must not be advertised as sufficient for RH unless an independent theorem establishing the required implication is supplied and its hypotheses are verified for this exact kernel.
