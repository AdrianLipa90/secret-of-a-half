# SOH Collatz Radial Lyapunov Law v0.1

Status: **EXACT ALGEBRA / LEAN TARGET / ZERO-PRESERVATION OPEN**

## 1. Defect

For a projective radius \(q>0\), define

\[
D(q)=\left(q-\frac1q\right)^2.
\]

For \(u\ne0\),

\[
\Delta_{\rm RC}(u)
=
\left|u^{-1}-\overline u\right|^2
=
D(|u|).
\]

Thus \(D\) is exactly the radial reciprocal--conjugation defect.

## 2. Stage-D radial Collatz selector

Use

\[
W(q)=\frac{3q+1}{4}.
\]

The self-dual point is \(q=1\), and

\[
W(q)-1=\frac34(q-1).
\]

The stronger defect identity is

\[
\boxed{
D(W(q))
=
R(q)\,D(q)
}
\]

with

\[
\boxed{
R(q)=
\frac{9q^2(3q+5)^2}
{16(q+1)^2(3q+1)^2}.
}
\]

## 3. Strict contraction

A direct factorization gives

\[
1-R(q)
=
\frac{
(3q+4)(7q+1)(3q^2+q+4)
}{
16(q+1)^2(3q+1)^2
}.
\]

Every factor in the numerator and denominator is positive for \(q>0\).
Therefore

\[
\boxed{0\le R(q)<1\qquad(q>0)}
\]

and hence

\[
\boxed{
q>0,\ q\ne1
\Longrightarrow
D(W(q))<D(q).
}
\]

So the Collatz radial selector is not only a fixed-point map toward the seam:
the exact reciprocal--conjugation defect is a strict global Lyapunov function
for the positive radial dynamics.

## 4. Optional sharp contraction constant

Differentiating \(R\) gives

\[
\frac{d}{dq}\log R(q)
=
-\frac{2(3q^2-6q-5)}
{q(q+1)(3q+1)(3q+5)}.
\]

The unique positive maximizer is

\[
q_* = 1+\frac{2\sqrt6}{3},
\]

and

\[
R(q_*)
=
\frac{657}{64}-\frac{63\sqrt6}{16}
\approx0.6207591378.
\]

This sharp constant is a derived analytic diagnostic and is not required for
the Lean contraction theorem.

## 5. Exact relation to the Riemann seam

For

\[
q=|\Omega(s)|,\qquad
\Omega(s)=\frac{s}{1-s},
\]

one has

\[
D(q)=0
\iff q=1
\iff \Re(s)=\frac12.
\]

Combined with the weighted defect identity,

\[
\Delta_{\rm RC}(\Omega(s))
=
\frac{4(\Re s-\frac12)^2}{|s|^2|1-s|^2},
\]

the radial Collatz word monotonically drives the exact projective seam defect
toward zero.

## 6. Firewall

This is **not** a proof that zeta zeros obey the radial Collatz dynamics.

The missing statement remains an independent bridge from zeta/arithmetic or
the Weil/theta operator to either:

- zero-preserving discrete radial dynamics; or
- direct vanishing/coercivity of the radial defect at every non-trivial zero.

The Lyapunov law says what the declared dynamics does once applied; it does not
show that the zeta zero set is invariant under that dynamics.

Formal file:

\`SecretOfAHalfFormal/RadialContraction.lean\`

\`proof_of_rh = false\`
