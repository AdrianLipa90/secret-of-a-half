# The Secret of a Half — SOH-G003 Modular Kernel Compactification V2

**Status:** EXACT CHANGE OF VARIABLES + CLASSICAL ROUTE AUDIT; REAL-ROOTEDNESS REMAINS OPEN  
**Date:** 17 August 2026

## 1. Starting point

From the exact positive half-line representation already derived in the project,

\[
\xi\!\left(\frac12+z\right)
=
\int_0^\infty \Phi(y)\cosh(zy)\,dy,
\]

with

\[
\Phi(y)
=
4\sum_{n\ge1}\pi n^2e^{5y/2}
\left(2\pi n^2e^{2y}-3\right)e^{-\pi n^2e^{2y}},
\qquad y\ge0,
\]

and \(\Phi(y)>0\).

## 2. Mellin variable and the reciprocal pair

Set

\[
x=e^{2y},\qquad x\in[1,\infty).
\]

Then \(dy=dx/(2x)\) and

\[
\cosh(zy)=\frac12\left(x^{z/2}+x^{-z/2}\right).
\]

Therefore

\[
\boxed{
\xi\!\left(\frac12+z\right)
=
\int_1^\infty D(x)
\left(x^{z/2}+x^{-z/2}\right)\,dx
}
\]

where

\[
\boxed{
D(x)=\sum_{n\ge1}\pi n^2x^{1/4}
\left(2\pi n^2x-3\right)e^{-\pi n^2x}
}
\]

is strictly positive for \(x\ge1\).

The two Mellin channels are exchanged by the reciprocal map

\[
x\longmapsto x^{-1}.
\]

Thus the quotient representative \(x\ge1\) already carries the complete reciprocal pair.

## 3. Compactified modular radius

Define

\[
\boxed{
\eta=\frac{x-1}{x+1}
}
\]

so that

\[
x=\frac{1+\eta}{1-\eta},
\qquad
\eta=\tanh y.
\]

On the full positive line,

\[
x\mapsto x^{-1}
\quad\Longrightarrow\quad
\boxed{\eta\mapsto-\eta}.
\]

The distinguished locations are

\[
x=1\longleftrightarrow\eta=0,
\qquad
x\to\infty\longleftrightarrow\eta\to1,
\qquad
x\to0^+\longleftrightarrow\eta\to-1.
\]

Hence the modular Mellin variable has exactly the same signed compactification geometry as the inverse-boundary coordinate used elsewhere in the monograph: the reciprocal fixed point is the centre and zero/infinity occupy opposite compactified boundaries.

## 4. Exact compactified kernel

Since

\[
\frac{dx}{d\eta}=\frac{2}{(1-\eta)^2}
\]

and

\[
\frac12\log x=\operatorname{artanh}\eta,
\]

we obtain

\[
\boxed{
\xi\!\left(\frac12+z\right)
=
\int_0^1 W(\eta)
\cosh\!\left(z\operatorname{artanh}\eta\right)\,d\eta
}
\]

with

\[
\boxed{
W(\eta)
=
\frac{4D\!\left((1+\eta)/(1-\eta)\right)}{(1-\eta)^2}
>0.
}
\]

This is an exact change of variables, not an approximation.

## 5. Relation to SOH-G003

Writing

\[
\xi\!\left(\frac12+z\right)=F(z^2),
\]

the real-rootedness target remains

\[
\boxed{
F(w)=0\Longrightarrow w\in\mathbb R.
}
\]

The compactified formula does not prove this. Its role is structural: it places the exact positive Riemann kernel on a compact reciprocal coordinate whose involution is the sign flip \(\eta\mapsto-\eta\), with the modular self-dual point at \(\eta=0\).

## 6. Classical Pólya/de Bruijn route audit

De Bruijn's 1950 paper studies sufficient real-zero mechanisms for trigonometric integrals, including kernels of the form

\[
e^{-\lambda\cosh t} f(\cosh t)
\]

with strong restrictions on \(f\). In the section devoted to the Riemann hypothesis, de Bruijn explicitly notes that the exact Riemann kernel does not admit the global analytic continuation needed to force it into the corresponding analytic-universal-factor approximation class. Therefore this project must not claim that the exact \(\Phi\) already satisfies those sufficient hypotheses.

This is a route audit, not a negative statement about RH.

## 7. Current proof frontier

**EXACT:**

1. positive half-line kernel \(\Phi(y)>0\);
2. Mellin representation with reciprocal channels \(x^{z/2}\) and \(x^{-z/2}\);
3. compactification \(\eta=(x-1)/(x+1)=\tanh y\);
4. reciprocal inversion \(x\mapsto1/x\) becomes \(\eta\mapsto-\eta\);
5. compactified positive weight \(W(\eta)>0\);
6. equality of the \(y\)-, \(x\)- and \(\eta\)-representations.

**OPEN:**

- a kernel property strong enough to imply real-rootedness of \(F\);
- SOH-G003;
- RH.

**DO NOT REOPEN AS PROOF TARGETS:**

- local finite-Hermite cancellation;
- forcing the exact Riemann kernel into de Bruijn's analytic universal-factor class without proving its hypotheses;
- further coordinate changes that do not strengthen the real-zero mechanism.
