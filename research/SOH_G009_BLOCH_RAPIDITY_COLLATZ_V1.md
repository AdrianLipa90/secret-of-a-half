# SOH-G009 — Centered Bloch rapidity representation of the Collatz branches

Status: **PROVED algebraic conjugacy. No universal Collatz-convergence or RH claim.**

Define

\[
u=2x,\qquad s=\frac{u}{1+u},\qquad t=2s-1=\frac{u-1}{u+1}.
\]

Equivalently, if \(u=e^\lambda\), then

\[
\boxed{t=\tanh(\lambda/2).}
\]

The distinguished half-layer becomes

\[
\boxed{x=\frac12\iff u=1\iff s=\frac12\iff t=0.}
\]

Thus the statement “the half-layer is the centered zero” has an exact coordinate realization; it is not the arithmetic identity \(1/2=0\).

## General dilation

Under

\[
u\mapsto au,\qquad a>0,
\]

the centered coordinate transforms as

\[
\boxed{
T_a(t)=\frac{(a-1)+(a+1)t}{(a+1)+(a-1)t}.
}
\]

Writing

\[
p_a=\frac{a-1}{a+1}=\tanh\!\left(\frac{\log a}{2}\right),
\]
this is

\[
\boxed{T_a(t)=\frac{t+p_a}{1+p_at}.}
\]

Therefore multiplication in \(u\) becomes hyperbolic/Möbius translation in the centered coordinate.  The parameter composition law is

\[
\boxed{p\oplus q=\frac{p+q}{1+pq}},
\]
which is the ordinary addition law for hyperbolic tangent.

## Halving branch

For \(a=1/2\),

\[
p_{1/2}=-\frac13,
\]
so one exact halving step becomes

\[
\boxed{
B(t)=\frac{t-1/3}{1-t/3}=\frac{3t-1}{3-t}.
}
\]

This is a hyperbolic translation of rapidity \(-\log2\).

## Odd branch

The standard odd Collatz branch \(x\mapsto3x+1\) becomes in the \(s\)-coordinate

\[
O_s(s)=\frac{s+2}{3}.
\]

Since \(t=2s-1\), this becomes

\[
\boxed{O_t(t)=\frac{t+2}{3}.}
\]

Thus the two branches in the centered coordinate are

\[
\boxed{
C_t(t)=
\begin{cases}
\dfrac{3t-1}{3-t}, & x\text{ even},\\[0.75em]
\dfrac{t+2}{3}, & x\text{ odd}.
\end{cases}}
\]

## The exact five-halving chain

The finite sequence

\[
16\to8\to4\to2\to1\to\frac12
\]

maps to

\[
\boxed{
\frac{31}{33}
\to\frac{15}{17}
\to\frac79
\to\frac35
\to\frac13
\to0.
}
\]

The first centered coordinate is

\[
\frac{31}{33}=\frac{32-1}{32+1}=\tanh\!\left(\frac{5\log2}{2}\right).
\]

Five halving translations each have parameter \(-1/3\).  Composing them with

\[
p\oplus q=\frac{p+q}{1+pq}
\]

gives exactly

\[
\boxed{p_5=-\frac{31}{33}.}
\]

Equivalently,

\[
T_{1/32}(31/33)=0,
\]
so

\[
\boxed{B^5(31/33)=0.}
\]

This is an exact geometric statement about the selected finite halving chain. It does not assert that every Collatz orbit reaches this chain.

## Relation to the Uroboros quotient

The quotient scale \(32\) is a translation by \(5\log2\) in \(\lambda=\log u\).  In the centered coordinate, that same translation has Möbius parameter

\[
\boxed{p_{32}=\frac{31}{33}.}
\]

Thus the number \(31/33\) is not inserted by hand: it is simultaneously

- the centered coordinate of \(u=32\), i.e. \(x=16\);
- the hyperbolic parameter of the scale-32 translation;
- the point sent to the centered half-layer \(t=0\) by five halving steps.

## Proof firewall

SOH-G009 establishes an exact coordinate conjugacy and an exact finite orbit identity. It does not prove:

- that every Collatz orbit converges;
- that the Uroboros quotient is dynamically forced for arbitrary Collatz trajectories;
- a new functional equation for xi;
- zero localization;
- SOH-G003;
- RH.
