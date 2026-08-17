# SOH-G003 — One-Sided Transform No-Go

**Status:** HIGH-PRECISION NUMERICAL FALSIFICATION OF TWO SUFFICIENT CANDIDATES  
**Claim status:** does not affect SOH-G003 itself; RH remains open.

Let

\[
E(z)=\int_0^\infty \Phi(y)e^{zy}\,dy,
\qquad
\xi\!\left(\frac12+z\right)=\frac{E(z)+E(-z)}2.
\]

A zero of the centered xi function therefore satisfies

\[
E(z)=-E(-z).
\]

Two stronger sufficient conditions were tested because either would have excluded such equality in the open right half-plane.

## Candidate A: strict modulus dominance

Candidate:

\[
|E(z)|>|E(-z)|\qquad(\Re z>0).
\]

This is false. At

\[
z=0.01+16i
\]

high-precision quadrature of the exact positive kernel gives

\[
\frac{|E(z)|}{|E(-z)|}
\approx 0.9999863668276836593<1.
\]

Thus a global Hermite--Biehler-type argument based solely on this strict modulus inequality is not available.

## Candidate B: right-half-plane quotient

Define

\[
Q(z)=\frac{E(z)}{E(-z)}.
\]

Candidate:

\[
\Re Q(z)>0\qquad(\Re z>0).
\]

This is also false. At

\[
z=0.01+5i
\]

high-precision quadrature gives

\[
Q(z)\approx
-0.08487873033294857
+0.99940367048429155\,i,
\]

whose real part is negative.

## Consequence

Neither of these broad one-sided-transform inequalities should be used as a proof route. They are stronger than necessary and are already numerically false for the exact Riemann kernel.

The admissible frontier remains kernel-specific: prove a structural property of the exact \(\Phi\) that forces the cosine/cosh transform to be real-rooted, rather than forcing \(E\) into an incorrect global modulus or half-plane geometry.

These are numerical counterexamples to candidate sufficient conditions, not numerical evidence against RH.
