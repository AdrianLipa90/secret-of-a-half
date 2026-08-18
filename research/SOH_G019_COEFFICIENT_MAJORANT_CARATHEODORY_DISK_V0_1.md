# SOH-G019 — Coefficient-majorant Carathéodory disk

**Status:** PROVED from the previously established strict positivity of every Taylor coefficient of the even xi quotient.

## Setup

Let

\[
\xi\!\left(\frac12+z\right)=F(z^2),\qquad
F(w)=\sum_{n\ge0}a_n w^n,
\]

with the already proved coefficient theorem

\[
a_n>0\qquad(n\ge0).
\]

Write \(a_0=F(0)=\xi(1/2)>0\).

## The coefficient-majorant threshold

On the nonnegative real axis,

\[
F'(r)=\sum_{n\ge1}n a_n r^{n-1}>0\qquad(r\ge0),
\]

so \(F(r)\) is strictly increasing.  Since \(a_1>0\),

\[
F(r)\ge a_0+a_1r\to\infty.
\]

Therefore there is a unique \(R_\star>0\) satisfying

\[
\boxed{F(R_\star)=2F(0).}
\]

This definition is exact.  A numerical evaluation of \(R_\star\) is used only as a regression diagnostic.

## Positive-real-part disk

For \(|w|\le r\), coefficient positivity gives

\[
|F(w)-a_0|
\le \sum_{n\ge1}a_n|w|^n
\le F(r)-a_0.
\]

Hence for every \(|w|<R_\star\),

\[
\Re F(w)
\ge a_0-|F(w)-a_0|
\ge 2a_0-F(|w|)>0.
\]

On the boundary \(|w|=R_\star\), equality in the triangle inequality would require all nonconstant terms \(a_nw^n\) to have the same argument.  Since \(a_1,a_2>0\), this can happen only for \(w=R_\star>0\), where

\[
F(R_\star)=2a_0>0.
\]

For every other boundary point the triangle inequality is strict.  Therefore

\[
\boxed{\Re F(w)>0\quad\text{for all }|w|\le R_\star.}
\]

In particular,

\[
\boxed{F(w)\ne0\quad\text{for all }|w|\le R_\star.}
\]

The corresponding centered xi disk is

\[
\boxed{\left|s-\frac12\right|\le\sqrt{R_\star}\Longrightarrow \xi(s)\ne0.}
\]

No table of zeta zeros is used.

## Canonically normalized coefficient law

The defining equation for \(R_\star\) is equivalent to

\[
\sum_{n\ge1}a_nR_\star^n=a_0.
\]

Define

\[
p_n:=\frac{a_nR_\star^n}{a_0}\qquad(n\ge1).
\]

Then

\[
\boxed{p_n>0,\qquad \sum_{n\ge1}p_n=1.}
\]

Thus the exact normalized representation is

\[
\boxed{
\frac{F(R_\star\zeta)}{F(0)}
=1+\sum_{n\ge1}p_n\zeta^n.
}
\]

Since every \(p_n\in(0,1)\), one obtains the global coefficient envelope

\[
\boxed{a_n<F(0)R_\star^{-n}\qquad(n\ge1).}
\]

This coefficient normalization is exact and is separate from PF\(_\infty\) or real-rootedness.

## Numerical regression only

High-precision bisection gives approximately

\[
R_\star\approx30.7037329843450643,
\qquad
\sqrt{R_\star}\approx5.54109492648746.
\]

The old G018 disk \(|w|\le1/4\) is therefore strictly contained in the G019 coefficient-majorant disk.  The numerical values are not used to prove the theorem.

## Proof firewall

G019 proves:

- existence and uniqueness of the coefficient-majorant threshold \(R_\star\);
- \(\Re F(w)>0\) on the closed disk \(|w|\le R_\star\);
- zero-freeness of that closed disk;
- the exact normalized coefficient law \(p_n>0\), \(\sum p_n=1\);
- the coefficient envelope \(a_n<F(0)R_\star^{-n}\).

G019 does **not** prove:

- that \(R_\star\) is the largest actual zero-free radius of \(F\);
- real-rootedness of \(F\);
- PF\(_3\), PF\(_\infty\), or total positivity of all coefficient Toeplitz minors;
- SOH-G003 real-rootedness;
- the Riemann Hypothesis.
