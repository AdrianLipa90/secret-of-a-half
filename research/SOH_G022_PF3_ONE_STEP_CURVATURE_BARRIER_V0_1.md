# SOH-G022 — One-step curvature barrier for the solid PF3 margin

**Status:** EXACT SUFFICIENT-CONDITION THEOREM / FINITE RIEMANN DIAGNOSTIC / PF3 OPEN.

This result sharpens the SOH-G006 solid-minor reduction after the SOH-G021
structural no-go.  It isolates a new local condition that is strong enough to
certify the *single solid order-three minor* at an index.  The theorem does not
prove that the Riemann-xi quotient coefficients satisfy the condition for all
indices, does not control all order-three Toeplitz minors, and does not prove
PF3, PF-infinity, real-rootedness, SOH-G003, or RH.

## 1. G006 variables

For

\[
F(w)=\sum_{k\ge0}a_k w^k,\qquad a_k>0,
\]

write

\[
r_k=\frac{a_k}{a_{k-1}},
\qquad
q_k=\frac{r_{k+1}}{r_k}.
\]

At a solid G006 minor indexed by \(k\ge2\), set

\[
u=q_{k-1},\qquad v=q_k,\qquad w=q_{k+1}.
\]

SOH-G006 proved that the sign of the solid order-three Toeplitz minor is the
sign of

\[
M=(1-v)^2-v^2(1-u)(1-w).
\]

## 2. Exact decomposition

The G006 margin admits the identity

\[
\boxed{
M=(1-v)^3
+v(1-w)\,[1-v(2-u)]
+v(1-v)(w-v).
}
\]

This is a polynomial identity.  Expanding the right-hand side gives exactly

\[
(1-v)^2-v^2(1-u)(1-w).
\]

Define the one-step barrier

\[
\boxed{B:=1-v(2-u)}
\]

and the forward curvature-order gap

\[
\boxed{G:=w-v}.
\]

Then

\[
\boxed{M=(1-v)^3+v(1-w)B+v(1-v)G.}
\]

## 3. Sufficient-condition theorem

Assume

\[
0<v<1,
\qquad
v\le w\le1,
\qquad
B=1-v(2-u)\ge0.
\]

Every term in the decomposition is then non-negative, and the first term is
strictly positive.  Therefore

\[
\boxed{M\ge(1-v)^3>0.}
\]

Hence the corresponding solid G006 order-three Toeplitz minor is strictly
positive.

Equivalently, for \(v>0\), the barrier condition is

\[
\boxed{
1-u\le\frac{1-v}{v}
}
\]

or

\[
\boxed{
v\le\frac{1}{2-u}.}
\]

In deficit variables

\[
d_j:=1-q_j,
\]

the same condition is

\[
\boxed{
d_k\ge\frac{d_{k-1}}{1+d_{k-1}}.}
\]

Thus the barrier prevents the PF2 curvature deficit from collapsing too
rapidly from one step to the next.

## 4. Moment-function form

For the actual Riemann-kernel coefficients, let

\[
L(p)=\log R(p),
\qquad
R(p)=\Gamma(p+1)^{-1}\int_0^\infty y^p\Phi(y)\,dy,
\]

so that \(a_k=R(2k)\).  Define the sampled second difference

\[
\delta_k
:=L(2k+2)-2L(2k)+L(2k-2).
\]

Then

\[
q_k=e^{\delta_k}.
\]

The two G022 hypotheses become the explicit discrete moment targets

\[
\boxed{\delta_{k+1}\ge\delta_k}
\]

and

\[
\boxed{
e^{\delta_k}\bigl(2-e^{\delta_{k-1}}\bigr)\le1.}
\]

Equivalently,

\[
\boxed{
\delta_k\le-\log\!\bigl(2-e^{\delta_{k-1}}\bigr).
}
\]

SOH-G005 supplies only \(\delta_k\le0\).  G022 therefore identifies two
strictly stronger local obligations that are tailored to the exact G006 PF3
margin.

## 5. Relation to G021

The exact G021 counterexample has

\[
u=\frac15,
\qquad
v=\frac9{10},
\qquad
w=\frac15,
\]

for which

\[
B=1-\frac9{10}\left(2-\frac15\right)=-\frac{31}{50}<0,
\]

and

\[
G=w-v=-\frac7{10}<0.
\]

Therefore G021 lies outside the G022 sufficient package in two independent
ways.  There is no conflict between the G021 no-go and the G022 theorem.

## 6. Finite Riemann diagnostic

The accompanying receipt recomputes the positive-kernel coefficients by
numerical quadrature and checks a finite index range.  For every sampled index
it records

- \(u\le v\le w<1\);
- the barrier \(B=1-v(2-u)\);
- the order gap \(w-v\);
- the exact G006 margin \(M\);
- the cubic floor \((1-v)^3\);
- the exact decomposition residual.

Any finite success remains **FINITE_DIAGNOSTIC_NOT_PROOF** for the global
Riemann coefficient sequence.

## 7. Active proof frontier

A proof route from G022 to a global solid-minor theorem now has two explicit
kernel-specific obligations:

1. prove \(q_{k+1}\ge q_k\) for all relevant Riemann coefficient indices;
2. prove \(q_k(2-q_{k-1})\le1\) for all such indices.

Only after those statements are established may one conclude positivity of all
*solid* G006 order-three minors.  A further argument would still be required to
upgrade solid-minor control to full PF3.

## Proof firewall

SOH-G022 proves only

\[
\boxed{
0<v<1,\ v\le w\le1,\ 1-v(2-u)\ge0
\Longrightarrow
M\ge(1-v)^3>0.
}
\]

It does **not** prove:

- that the Riemann coefficient sequence satisfies the G022 hypotheses for all
  indices;
- all solid order-three minors globally;
- all order-three Toeplitz minors;
- PF3;
- PF-infinity;
- real-rootedness / SOH-G003;
- the Riemann Hypothesis.
