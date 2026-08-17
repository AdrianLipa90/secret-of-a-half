# SOH-G008 — Xi scale-defect antisymmetry and the centered Uroboros cell

Status: **PROVED as a consequence of the xi functional equation and the explicit scale quotient. No RH claim.**

Let

\[
X(u)=\xi\!\left(\frac{u}{1+u}\right),\qquad u>0.
\]

The completed xi functional equation gives the exact inversion symmetry

\[
X(u)=X(1/u).
\]

For any fixed scale \(a>1\), write

\[
T_a(u)=au,\qquad J(u)=\frac1u.
\]

Then

\[
JT_aJ(u)=\frac{u}{a}=T_a^{-1}(u).
\]

Therefore the inversion normalizes the dilation subgroup \(a^{\mathbb Z}\) and descends to the quotient

\[
\mathbb C^*/a^{\mathbb Z}.
\]

For the Uroboros scale \(a=32\), a reciprocal fundamental annulus is

\[
32^{-1/2}\le |u|\le32^{1/2},
\]

whose two radial boundaries are exchanged by \(J\).

## Scale defect

Define the scale defect

\[
\Delta_a(u)=X(au)-X(u).
\]

Using only \(X(u)=X(1/u)\),

\[
\begin{aligned}
\Delta_a\!\left(\frac1{au}\right)
&=X(1/u)-X(1/(au))\\
&=X(u)-X(au)\\
&=-\Delta_a(u).
\end{aligned}
\]

Hence

\[
\boxed{\Delta_a(1/(au))=-\Delta_a(u).}
\]

The involution \(u\mapsto1/(au)\) has the unique positive fixed point

\[
u=a^{-1/2}.
\]

Therefore

\[
\boxed{\Delta_a(a^{-1/2})=0}
\]

and equivalently

\[
\boxed{X(a^{1/2})=X(a^{-1/2}).}
\]

For \(a=32\),

\[
\boxed{X(\sqrt{32})=X(1/\sqrt{32}).}
\]

This equality is not an assumed scale law; it is forced by the ordinary Riemann inversion symmetry because the two endpoints are reciprocal.

## Logarithmic coordinate

Let

\[
\lambda=\log u,\qquad Y(\lambda)=X(e^\lambda),\qquad L=\log a.
\]

Then \(Y\) is even,

\[
Y(-\lambda)=Y(\lambda),
\]

and the scale defect

\[
d_L(\lambda)=Y(\lambda+L)-Y(\lambda)
\]

satisfies

\[
\boxed{d_L(-L-\lambda)=-d_L(\lambda).}
\]

The reciprocal fundamental interval is

\[
[-L/2,L/2],
\]

centered exactly at the self-dual coordinate \(\lambda=0\), i.e. \(u=1\), corresponding to \(s=1/2\).

## No-go: exact scale periodicity

There is no identity

\[
X(au)=X(u)\qquad\text{for all }u>0
\]

for any \(a>1\).

Indeed, if it held, then for every fixed \(u>0\),

\[
X(u)=X(a^n u).
\]

As \(n\to\infty\),

\[
\frac{a^n u}{1+a^n u}\to1,
\]

so continuity of \(\xi\) gives

\[
X(u)=\xi(1)=\frac12
\]

for every positive \(u\). Thus \(\xi\) would be constant on the real interval \((0,1)\), hence constant everywhere by the identity theorem, contradicting the nonconstancy of the completed xi function.

A constant-multiplier law

\[
X(au)=cX(u)
\]

is also impossible unless \(c=1\): taking \(u\to\infty\) gives \(1/2=c/2\), after which the preceding no-go applies.

## Proof firewall

The theorem establishes:

- compatibility of Riemann inversion with the explicit dilation quotient;
- a centered reciprocal fundamental cell;
- exact antisymmetry of the xi scale defect;
- an exact boundary equality across the centered scale-32 cell;
- impossibility of global scale-32 periodicity or constant-multiplier quasi-periodicity.

It does **not** establish:

- a nontrivial factor of automorphy for xi under \(u\mapsto32u\);
- a zero-location theorem;
- universal Collatz convergence;
- SOH-G003 real-rootedness;
- RH.
