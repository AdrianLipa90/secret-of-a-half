# SOH-G020 — Canonical half-mass PF2 law

**Status:** PROVED from SOH-G019 coefficient normalization plus the already proved SOH-G005 PF2 coefficient theorem.

## Setup

Let

\[
F(w)=\sum_{n\ge0}a_nw^n,
\qquad a_n>0,
\]

and let \(R_\star\) be the unique G019 threshold

\[
F(R_\star)=2F(0)=2a_0.
\]

G019 proved

\[
\sum_{n\ge1}a_nR_\star^n=a_0.
\]

Define for every \(n\ge0\)

\[
\boxed{
\pi_n:=\frac{a_nR_\star^n}{2a_0}.
}
\]

## Exact half-mass normalization

At \(n=0\),

\[
\boxed{\pi_0=\frac12.}
\]

For the positive indices,

\[
\sum_{n\ge1}\pi_n
=\frac1{2a_0}\sum_{n\ge1}a_nR_\star^n
=\frac12.
\]

Therefore

\[
\boxed{
\pi_n>0,
\qquad
\sum_{n\ge0}\pi_n=1,
\qquad
\pi_0=\sum_{n\ge1}\pi_n=\frac12.
}
\]

Equivalently,

\[
\boxed{
\frac{F(R_\star\zeta)}{2F(0)}
=\sum_{n\ge0}\pi_n\zeta^n
}
\]

is the probability-generating series of the normalized coefficient law.

## PF2 is preserved exactly

SOH-G005 proved

\[
a_n^2\ge a_{n-1}a_{n+1}\qquad(n\ge1).
\]

Geometric scaling and positive normalization give

\[
\pi_n^2-\pi_{n-1}\pi_{n+1}
=\frac{R_\star^{2n}}{4a_0^2}
\left(a_n^2-a_{n-1}a_{n+1}\right).
\]

Hence

\[
\boxed{
\pi_n^2\ge\pi_{n-1}\pi_{n+1}\qquad(n\ge1).
}
\]

Thus the canonical half-mass law is PF2/log-concave.

## Strict monotone decay

For a positive log-concave sequence, the successive ratios

\[
q_n:=\frac{\pi_n}{\pi_{n-1}}
\]

are nonincreasing.  Since the positive-index mass is exactly \(1/2\),

\[
0<\pi_1<\frac12=\pi_0.
\]

Therefore

\[
q_1<1,
\qquad
q_n\le q_1<1\quad(n\ge1),
\]

and consequently

\[
\boxed{
\pi_0>\pi_1>\pi_2>\cdots>0.
}
\]

## Sharpened global coefficient envelope

Write

\[
b_n:=2\pi_n=\frac{a_nR_\star^n}{a_0}.
\]

Then \(b_n>0\), \(b_1>b_2>\cdots\), and

\[
\sum_{n\ge1}b_n=1.
\]

For any \(n\ge1\), monotonicity gives

\[
nb_n\le\sum_{k=1}^{n}b_k<1,
\]

because the tail after \(n\) is strictly positive.  Thus

\[
\boxed{b_n<\frac1n.}
\]

Returning to \(a_n\),

\[
\boxed{
 a_n<\frac{F(0)}{nR_\star^n},
 \qquad n\ge1.
}
\]

This strictly sharpens the G019 coefficient envelope \(a_n<F(0)R_\star^{-n}\).

## Numerical regression only

Using the numerical G019 radius, the first normalized masses are approximately

\[
\pi_0=0.5,
\quad
\pi_1\approx0.35470477,
\quad
\pi_2\approx0.11705464,
\quad
\pi_3\approx0.02423207,
\]

followed by rapidly smaller positive terms.  These values are regression checks only; the theorem is algebraic.

## Proof firewall

G020 proves:

- an exact probability law from the scaled coefficients;
- exactly half of its mass at index zero and half on positive indices;
- preservation of PF2/log-concavity;
- strict monotone decrease of the full sequence;
- the global envelope \(a_n<F(0)/(nR_\star^n)\).

G020 does **not** prove:

- PF3 or PF\(_\infty\);
- ultra-log-concavity;
- real-rootedness of \(F\);
- SOH-G003 real-rootedness;
- the Riemann Hypothesis.
