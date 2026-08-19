# SOH-G021 — Half-mass PF2 does not imply PF3

**Status:** PROVED structural no-go. This theorem concerns the sufficiency of the abstract properties established by SOH-G020; it does not decide PF3 for the actual Riemann-xi quotient coefficients.

## Statement

There exists a positive probability sequence \((\pi_n)_{n\ge0}\) such that

\[
\pi_0=\frac12,
\qquad
\sum_{n\ge1}\pi_n=\frac12,
\]

\((\pi_n)\) is strictly decreasing and PF2/log-concave, and the G020 monotone envelope

\[
2\pi_n<\frac1n\qquad(n\ge1)
\]

holds, but its solid order-three Toeplitz minor at \(k=2\) is negative. Therefore the structural package proved in G020, by itself, cannot imply PF3.

## Exact construction

Let \(x\in(0,1)\) be the unique root of

\[
\boxed{36x^3+205x^2+1295x-1250=0.}
\]

Uniqueness on \([0,\infty)\) is immediate because

\[
P'(x)=108x^2+410x+1295>0,
\]

while \(P(0)=-1250<0<P(1)=286\).

Define adjacent mass ratios

\[
q_n:=\frac{\pi_n}{\pi_{n-1}}
\]

by

\[
q_1=x,
\qquad
q_2=\frac{x}{5},
\qquad
q_3=\frac{9x}{50},
\qquad
q_n=\frac{9x}{250}\quad(n\ge4),
\]

and set \(\pi_0=1/2\).

Because \(0<x<1\),

\[
1>q_1>q_2>q_3>q_4=q_5=\cdots>0.
\]

Hence every mass is positive and the masses decrease strictly. Since the adjacent ratios are nonincreasing, the sequence is PF2/log-concave.

## Exact half-mass normalization

Relative to \(\pi_0\), the first products are

\[
\frac{\pi_1}{\pi_0}=x,
\qquad
\frac{\pi_2}{\pi_0}=\frac{x^2}{5},
\qquad
\frac{\pi_3}{\pi_0}=\frac{9x^3}{250},
\qquad
\frac{\pi_4}{\pi_0}=\frac{81x^4}{62500}.
\]

For \(n\ge4\) the remaining products form a geometric tail with ratio \(9x/250\). Therefore

\[
S(x):=\frac{1}{\pi_0}\sum_{n\ge1}\pi_n
=x+\frac{x^2}{5}+\frac{9x^3}{250}
+\frac{81x^4/62500}{1-9x/250}.
\]

Direct simplification gives

\[
S(x)-1
=
\frac{36x^3+205x^2+1295x-1250}{5(250-9x)}.
\]

The defining cubic therefore gives \(S(x)=1\), and hence

\[
\boxed{\sum_{n\ge1}\pi_n=\frac12.}
\]

Thus \((\pi_n)\) has the same exact half-mass normalization as G020.

## The G020 envelope also holds

Set \(b_n=2\pi_n\). Then \(b_n>0\), the sequence is strictly decreasing, and

\[
\sum_{n\ge1}b_n=1.
\]

Consequently, for every \(n\ge1\),

\[
nb_n\le\sum_{j=1}^n b_j<1,
\]

so

\[
\boxed{b_n<\frac1n.}
\]

This is exactly the abstract monotone-envelope property used in G020 after normalization.

## Exact PF3 failure

For the solid G006 minor at \(k=2\), define

\[
u=\frac{q_2}{q_1},
\qquad
v=\frac{q_3}{q_2},
\qquad
w=\frac{q_4}{q_3}.
\]

The construction gives

\[
\boxed{u=\frac15,
\qquad v=\frac9{10},
\qquad w=\frac15.}
\]

Using the exact G006 factorization

\[
M=(1-v)^2-v^2(1-u)(1-w),
\]

we obtain

\[
\begin{aligned}
M
&=\frac1{100}
-\frac{81}{100}\frac45\frac45\\
&=\boxed{-\frac{1271}{2500}}<0.
\end{aligned}
\]

The corresponding solid order-three Toeplitz determinant is therefore negative. Hence this sequence is not PF3.

## Consequence for the active frontier

SOH-G020 proved a canonical half-mass law for the actual scaled coefficients of \(F\). SOH-G021 proves that the following facts, even taken together, are insufficient to deduce PF3:

- positivity;
- probability normalization;
- exactly half the mass at index zero and half on positive indices;
- strict monotone decay of the masses;
- PF2/log-concavity;
- the envelope \(2\pi_n<1/n\).

Therefore any successful proof of PF3 for the actual Riemann-xi quotient coefficients must use additional structure not contained in that abstract package—for example a stronger kernel-specific ratio-curvature or moment inequality.

## Proof firewall

G021 proves only an implication no-go:

\[
\boxed{\text{G020 structural package}\not\Longrightarrow\text{PF3}.}
\]

It does **not** prove:

- that the actual coefficients of \(F\) fail PF3;
- that any actual G006 margin \(M_k\) is negative;
- PF3 or failure of PF3 for \(F\);
- PF\(_\infty\) or failure of PF\(_\infty\) for \(F\);
- SOH-G003;
- the Riemann Hypothesis.

PF3 for the actual quotient coefficient sequence remains OPEN.
