# SOH-G023 — Reciprocal-deficit normal form and the 1-Lipschitz frontier

**Status:** EXACT REPARAMETRIZATION / EXACT LOCAL SUFFICIENT CONDITION / GLOBAL RIEMANN LAW OPEN.

SOH-G022 rewrites the G006 solid PF3 margin into a positive cubic floor plus a
one-step barrier and a forward curvature-order term.  SOH-G023 introduces a
reciprocal deficit variable in which both nontrivial G022 requirements become
one-sided bounds on consecutive increments, and the G006 margin itself becomes
a shifted multiplicative determinant.

The result does not prove the increment law for all actual Riemann quotient
coefficients, does not control all order-three Toeplitz minors, and does not
prove PF3, PF-infinity, real-rootedness, SOH-G003, SOH-C005, or RH.

## 1. Reciprocal curvature deficit

For the G006 ratio-curvatures

\[
q_k=\frac{r_{k+1}}{r_k},
\qquad
r_k=\frac{a_k}{a_{k-1}},
\]

strict PF2 places the relevant sampled values in \(0<q_k<1\).  Define

\[
\boxed{
E_k:=\frac{1}{1-q_k}>1.
}
\]

Equivalently,

\[
q_k=1-\frac1{E_k}.
\]

For the solid minor at index \(k\), write

\[
u=q_{k-1},\qquad v=q_k,\qquad w=q_{k+1}.
\]

## 2. Exact G006 normal form

The G006 margin is

\[
M_k=(1-v)^2-v^2(1-u)(1-w).
\]

Using

\[
1-u=\frac1{E_{k-1}},
\qquad
1-v=\frac1{E_k},
\qquad
1-w=\frac1{E_{k+1}},
\qquad
v=\frac{E_k-1}{E_k},
\]

gives

\[
\boxed{
M_k=
\frac{E_{k-1}E_{k+1}-(E_k-1)^2}
     {E_{k-1}E_k^2E_{k+1}}.
}
\]

Because the denominator is positive, the sign of the solid PF3 minor is the
sign of

\[
\boxed{
\widehat M_k:=E_{k-1}E_{k+1}-(E_k-1)^2.
}
\]

Thus the G006 solid-minor problem has the exact reciprocal-deficit form

\[
\boxed{
\Delta_k\ge0
\iff
E_{k-1}E_{k+1}\ge(E_k-1)^2.
}
\]

## 3. Increment decomposition

Define consecutive increments

\[
\alpha_k:=E_k-E_{k-1},
\qquad
\beta_k:=E_{k+1}-E_k.
\]

Substitution yields the second exact identity

\[
\boxed{
\widehat M_k
=(E_k-1)+E_k(1-\alpha_k)+E_{k-1}\beta_k.
}
\]

Therefore

\[
E_k>1,
\qquad
\alpha_k\le1,
\qquad
\beta_k\ge0
\]

imply

\[
\boxed{
\widehat M_k>0,
\qquad
M_k>0.
}
\]

## 4. Exact equivalence with the G022 local package

The G022 forward-order condition

\[
q_{k+1}\ge q_k
\]

is equivalent to

\[
E_{k+1}\ge E_k
\]

and hence

\[
\boxed{\beta_k\ge0.}
\]

The G022 one-step barrier

\[
q_k(2-q_{k-1})\le1
\]

is equivalent to

\[
\frac1{1-q_k}-\frac1{1-q_{k-1}}\le1,
\]

that is,

\[
\boxed{\alpha_k\le1.}
\]

Consequently, if the actual reciprocal deficits satisfy the global law

\[
\boxed{
0\le E_{k+1}-E_k\le1
}
\]

for every relevant index, then every solid G006 order-three minor is strictly
positive.

This is a reparametrization of the G022 local sufficient package, not a proof
of the global law.

## 5. Continuous normalized-moment target

Let

\[
L(p)=\log R(p),
\qquad
R(p)=\Gamma(p+1)^{-1}\int_0^\infty y^p\Phi(y)\,dy,
\]

and define the step-two second difference

\[
\delta(p):=L(p+2)-2L(p)+L(p-2).
\]

At the even lattice,

\[
q_k=e^{\delta(2k)}.
\]

Define the continuous reciprocal-deficit transform

\[
\boxed{
\mathcal E(p):=\frac{1}{1-e^{\delta(p)}}
}
\]

where \(\delta(p)<0\).  Then

\[
E_k=\mathcal E(2k).
\]

A sufficient continuous route to the global G023 law is therefore

\[
\boxed{
0\le \mathcal E'(p)\le\frac12
}
\]

on the relevant range.  Indeed, integration over an interval of length two
gives

\[
0\le E_{k+1}-E_k\le1.
\]

Differentiation gives the exact formula

\[
\mathcal E'(p)
=
\frac{e^{\delta(p)}\delta'(p)}{(1-e^{\delta(p)})^2}.
\]

Hence the derivative package is equivalent to

\[
\delta'(p)\ge0
\]

and

\[
\boxed{
\delta'(p)\le\cosh(\delta(p))-1.
}
\]

The latter follows because

\[
\frac{(1-e^{\delta})^2}{2e^{\delta}}
=\cosh\delta-1.
\]

This produces a precise continuous moment-function target for future work.
It is not proved in SOH-G023.

## 6. Finite Riemann diagnostic

The accompanying receipt samples the exact positive Riemann kernel and records
\(E_k\), the increments \(E_{k+1}-E_k\), the transformed margin, and the
increment-decomposition residual.  The previously observed values begin with
approximately

\[
E_1=1.86980,
\quad E_2=2.68317,
\quad E_3=3.46465,
\quad E_4=4.22515,
\]

with consecutive increments approximately

\[
0.81337,
\quad0.78147,
\quad0.76050,
\quad0.74539,
\ldots
\]

inside \((0,1)\) on the sampled range.  This is
**FINITE_DIAGNOSTIC_NOT_PROOF**.

## 7. G021 firewall

For the exact G021 counterexample

\[
u=\frac15,
\qquad
v=\frac9{10},
\qquad
w=\frac15,
\]

the reciprocal deficits satisfy

\[
E_{k-1}=\frac54,
\qquad
E_k=10,
\qquad
E_{k+1}=\frac54.
\]

Thus

\[
\alpha_k=\frac{35}{4}>1,
\qquad
\beta_k=-\frac{35}{4}<0,
\]

so the G021 construction violates both sides of the G023 local law.

## Proof firewall

SOH-G023 proves only the exact normal forms

\[
M_k=
\frac{E_{k-1}E_{k+1}-(E_k-1)^2}
     {E_{k-1}E_k^2E_{k+1}}
\]

and

\[
\widehat M_k=(E_k-1)+E_k(1-\alpha_k)+E_{k-1}\beta_k,
\]

together with the local implication

\[
\alpha_k\le1,
\quad
\beta_k\ge0
\Longrightarrow
M_k>0.
\]

It does **not** prove:

- the global monotone 1-Lipschitz law for the actual Riemann coefficient
  sequence;
- the continuous derivative bounds for \(\mathcal E\);
- all solid order-three minors globally;
- all order-three Toeplitz minors;
- PF3;
- PF-infinity;
- SOH-G003 real-rootedness;
- SOH-C005;
- RH.
