# SOH-G024 v0.3 — N-body partition as the generating function of the extended Laguerre hierarchy

**Status:** EXACT CROSSWALK / CLASSICAL LP CRITERION IDENTIFIED / ADVERSARIAL CONTROLS PASS / RH OPEN  
**Branch:** `proof/theta-nbody-hermitian-bilinear-rigidity-v0.1`  
**Date:** 17 September 2026

## 1. Scope

The v0.2 correction established the exact Wick-rotated two-body identity

\[
\mathcal Z(-ix,y)=\frac12|f(x+iy)|^2,
\]

and

\[
\partial_y^2\mathcal Z(-ix,y)
=H_f(x+iy),
\qquad
H_f(z)=|f'(z)|^2-\Re(f''(z)\overline{f(z)}).
\]

The next question was whether the full Taylor hierarchy of the same partition
contains a stronger positivity structure.

It does. HOUND/source checking also showed that the resulting coefficient
hierarchy is **not a new zero criterion**: it is exactly one half of the
classical extended Laguerre hierarchy of Csordas--Patrick--Varga, in the
normalization recorded explicitly by Cardon.

The SOH contribution in this note is therefore the exact **crosswalk** between
that classical hierarchy and the already constructed theta/N-body partition.
No novelty claim is made for the extended Laguerre criterion itself.

RH remains open.

## 2. Branch-independent q-partition

Let \(f\) be a real entire function and let \(x\in\mathbb R\). Define

\[
\boxed{
\mathcal Q_x(q)
:=\frac12 f(x+i\sqrt q)f(x-i\sqrt q).
}
\]

Although the display contains \(\sqrt q\), the product is even under
\(\sqrt q\mapsto-\sqrt q\). Hence it defines an entire function of \(q\):

\[
\boxed{
\mathcal Q_x(q)=\sum_{n=0}^{\infty}c_n(x)q^n.
}
\]

For real \(q=y^2\ge0\), reality of \(f\) gives

\[
\boxed{
\mathcal Q_x(y^2)
=\frac12|f(x+iy)|^2.
}
\]

For the SOH two-body partition,

\[
\boxed{
\mathcal Q_x(y^2)=\mathcal Z(-ix,y).
}
\]

Thus \(q=y^2\) is the exact square transverse coordinate of the Wick-rotated
N-body geometry.

## 3. Exact coefficient formula

Expand both factors at the real point \(x\). The coefficient of
\(y^{2n}=q^n\) is

\[
\boxed{
c_n(x)=
\frac{(-1)^n}{2(2n)!}
\sum_{k=0}^{2n}(-1)^k
{2n\choose k}
 f^{(k)}(x)f^{(2n-k)}(x).
}
\]

In particular,

\[
c_0(x)=\frac12f(x)^2,
\]

\[
\boxed{
c_1(x)=\frac12\left(f'(x)^2-f(x)f''(x)\right).}
\]

## 4. Identification with the classical extended Laguerre operators

Cardon records the Csordas--Patrick--Varga operators as

\[
\boxed{
L_n[f](x)
=
\sum_{k=0}^{2n}
\frac{(-1)^{k+n}}{(2n)!}
{2n\choose k}
 f^{(k)}(x)f^{(2n-k)}(x).
}
\]

Therefore

\[
\boxed{c_n(x)=\frac12L_n[f](x).}
\]

Equivalently,

\[
\boxed{
2\mathcal Q_x(q)
=f(x+i\sqrt q)f(x-i\sqrt q)
=\sum_{n=0}^{\infty}L_n[f](x)q^n.
}
\]

External source:

- D. A. Cardon, *Extended Laguerre inequalities and a criterion for real zeros*, arXiv:0911.1122, Theorem 1.1; published in *Progress in Analysis and its Applications*, pp. 143--149, DOI `10.1142/9789814313179_0019`.

Cardon's Theorem 1.1 states, for
\(f(z)=e^{-bz^2}f_1(z)\) with \(b\ge0\) and \(f_1\) real entire of genus 0 or 1,

\[
\boxed{
f\in\mathcal{LP}
\iff
L_n[f](x)\ge0
\quad\forall x\in\mathbb R,\;\forall n\ge0.}
\]

The forward direction is attributed there to Patrick; the reverse direction to
Csordas and Varga.

## 5. Exact RH-equivalent q-cone

For

\[
f(z)=\Xi(z)=\xi\!\left(\frac12+iz\right),
\]

\(\Xi\) is a real entire function of order one. Therefore Cardon's theorem
applies, and the standard equivalence

\[
\mathrm{RH}\iff\Xi\in\mathcal{LP}
\]

gives

\[
\boxed{
\mathrm{RH}
\iff
c_n(x)\ge0
\quad
\forall x\in\mathbb R,\; n\ge0.
}
\]

Equivalently,

\[
\boxed{
\mathrm{RH}
\iff
\mathcal Q_x(q)
\text{ has non-negative Maclaurin coefficients in }q
\quad\forall x\in\mathbb R.
}
\]

Since \(\mathcal Q_x\) is entire, coefficient non-negativity is equivalent to
absolute monotonicity on the positive q-axis:

\[
\boxed{
\mathrm{RH}
\iff
\partial_q^m\mathcal Q_x(q)\ge0
\quad\forall x\in\mathbb R,\ q\ge0,\ m\ge0.
}
\]

This is a reformulation, not a proof of RH.

## 6. Direct zero-set proof of the reverse implication

Assume

\[
c_n(x)\ge0
\]

for every real \(x\) and every \(n\). If \(f\) had a non-real zero

\[
z_0=x_0+iy_0,
\qquad y_0\ne0,
\]

then with \(q_0=y_0^2>0\),

\[
\mathcal Q_{x_0}(q_0)
=\frac12|f(z_0)|^2=0.
\]

But

\[
\mathcal Q_{x_0}(q_0)
=\sum_{n\ge0}c_n(x_0)q_0^n
\]

is a sum of non-negative terms. Hence every coefficient must vanish and
\(\mathcal Q_{x_0}\equiv0\), impossible for a nonzero entire \(f\).
Thus all zeros are real. For \(\Xi\), that conclusion is RH.

## 7. Direct RH-side factorization

Conversely, assume RH. Pair the real zeros of \(\Xi\) as \(\pm\gamma_j\), with
multiplicity. Because \(\Xi\) is even of order one,

\[
\Xi(z)=\Xi(0)
\prod_j\left(1-\frac{z^2}{\gamma_j^2}\right),
\]

with

\[
\sum_j\gamma_j^{-2}<\infty.
\]

For each pair,

\[
\begin{aligned}
&\left(1-\frac{(x+i\sqrt q)^2}{\gamma_j^2}\right)
\left(1-\frac{(x-i\sqrt q)^2}{\gamma_j^2}\right)\\
&=\frac{(\gamma_j^2-x^2)^2
+2(\gamma_j^2+x^2)q+q^2}{\gamma_j^4}.
\end{aligned}
\]

Every coefficient of this quadratic polynomial in \(q\) is non-negative.
Finite products therefore have non-negative q-coefficients. The convergence
\(\sum\gamma_j^{-2}<\infty\) gives locally uniform convergence of the paired
product on compact q-sets, so each limiting Taylor coefficient is a limit of
non-negative coefficients. Hence

\[
c_n(x)\ge0
\]

for all real \(x\) and all \(n\).

## 8. Hermitian Jensen curvature is generated by the entire hierarchy

From

\[
\mathcal Z(-ix,y)
=\frac12\sum_{n\ge0}L_n[f](x)y^{2n},
\]

we obtain

\[
\boxed{
H_f(x+iy)
=\partial_y^2\mathcal Z(-ix,y)
=\sum_{n\ge1}n(2n-1)L_n[f](x)y^{2n-2}.
}
\]

Thus v0.2's Hermitian Jensen quantity is not an isolated second-order object.
It is the weighted generating function of the complete extended-Laguerre
hierarchy. At \(y=0\), only \(n=1\) survives:

\[
H_f(x)=L_1[f](x)=f'(x)^2-f(x)f''(x).
\]

## 9. The theta axis x=0 is unconditionally inside the cone

Write

\[
\xi\!\left(\frac12+z\right)=F(z^2),
\qquad
F(w)=\sum_{k\ge0}a_k w^k.
\]

The positive theta kernel gives

\[
a_k
=\frac1{(2k)!}
\int_0^\infty\Phi(t)t^{2k}\,dt
>0.
\]

At \(x=0\),

\[
\Xi(i\sqrt q)=F(q),
\]

hence

\[
\mathcal Q_0(q)=\frac12F(q)^2.
\]

Comparing coefficients gives

\[
\boxed{
L_n[\Xi](0)
=\sum_{k=0}^{n}a_k a_{n-k}>0.
}
\]

Therefore every extended-Laguerre gate is already positive on the central
transverse axis. The unresolved content is transporting this positivity through
the real phase/translation coordinate \(x\ne0\).

## 10. Two-body kernel representation of every gate

Using

\[
f(x+iy)f(x-iy)
=\iint K(t)K(s)e^{-ix(t+s)}e^{y(t-s)}\,dt\,ds,
\]

the \(y^{2n}\) coefficient gives

\[
\boxed{
L_n[f](x)
=\frac1{(2n)!}
\iint_{\mathbb R^2}
(t-s)^{2n}K(t)K(s)e^{-ix(t+s)}\,dt\,ds.
}
\]

With

\[
t=u+r,\qquad s=u-r,
\]

and Jacobian \(2\), define

\[
C_n(u)
:=\int_{\mathbb R}r^{2n}K(u+r)K(u-r)\,dr>0.
\]

Then

\[
\boxed{
L_n[f](x)
=\frac{2^{2n+1}}{(2n)!}
\int_{\mathbb R}C_n(u)e^{-i2xu}\,du.
}
\]

This exposes the exact remaining sign problem: every \(C_n(u)\) is pointwise
positive, but RH requires the Fourier transform of every member of the whole
relative-moment hierarchy to remain non-negative for every real frequency.
Pointwise positivity alone does not imply Fourier positivity.

## 11. Adversarial controls

For the real-rooted control

\[
f(z)=\prod_j\left(1-\frac{z^2}{\gamma_j^2}\right),
\]

direct differentiation matches coefficientwise convolution of the positive
quadratic q-factors. The deterministic control uses

\[
\gamma=(1,2,3.5),\qquad x=0.7,
\]

with maximum residual below \(2\times10^{-71}\) at 70-digit precision.

For the non-LP control

\[
f(z)=1+z^4,
\]

we get exactly

\[
\boxed{c_1(x)=2x^2(x^4-3),}
\]

so

\[
\boxed{c_1(1)=-4<0.}
\]

The receipt also samples \(c_0,\ldots,c_4\) for \(\Xi\) at
\(x=0\), \(x=10\), and \(x=14.134725141734693790\). All sampled values are
non-negative at 70-digit working precision. This is only
`FINITE_DIAGNOSTIC_NOT_PROOF`.

## 12. Crosswalk with SOH-G025

Current `main` independently contains SOH-G025, which rewrites the square
quotient through

\[
\phi(w)=\frac{F'(w)}{F(w)}
\]

and a Stieltjes/Hankel positivity hierarchy.

Put

\[
w=-x^2,
\qquad
\phi=F'/F.
\]

Since \(\Xi(x)=F(-x^2)\), direct differentiation gives

\[
\boxed{
L_1[\Xi](x)
=2F(w)^2\left(\phi(w)+2w\phi'(w)\right).
}
\]

If

\[
\phi(w)=\sum_{n\ge0}(-1)^n\mu_n w^n,
\]

then formally around the origin

\[
\boxed{
\phi(-x^2)-2x^2\phi'(-x^2)
=\sum_{n\ge0}(2n+1)\mu_n x^{2n}.
}
\]

Thus G024's first extended-Laguerre gate and G025's logarithmic-derivative
moments are two coordinate descriptions of the same quotient geometry. This
crosswalk does not make either positivity proof automatic and is not used as a
dependency of this branch.

## 13. Current proof frontier

The exact partition now generates the classical complete LP positivity
hierarchy:

\[
\boxed{
\text{theta kernel}
\to
\mathcal Z(-ix,y)
\to
\{L_n[\Xi](x)\}_{n\ge0}
\to
\mathcal{LP}
\iff
\mathrm{RH}.
}
\]

The missing theorem is sharply localized:

\[
\boxed{
L_n[\Xi](x)\ge0
\quad
\forall x\in\mathbb R,\; n\ge1.
}
\]

At \(x=0\), it is already proved unconditionally by positive theta moments.
The open problem is global phase-stability in \(x\).

A natural next attack is to study

\[
C_n(u)=\int r^{2n}K(u+r)K(u-r)\,dr
\]

as a family and search for one structural property forcing all of their Fourier
transforms to be non-negative.

## 14. Proof firewall

**EXACT / PROVED FROM THE DISPLAYED DEFINITIONS**

1. \(\mathcal Q_x(q)\) is entire in \(q\).
2. \(c_n(x)=L_n[f](x)/2\).
3. \(\mathcal Z(-ix,y)=\frac12\sum_nL_n[f](x)y^{2n}\).
4. \(H_f(x+iy)=\sum_{n\ge1}n(2n-1)L_n[f](x)y^{2n-2}\).
5. the two-body kernel representation of every \(L_n\).
6. \(L_n[\Xi](0)=\sum_{k=0}^n a_ka_{n-k}>0\).
7. the displayed G024/G025 first-gate algebraic crosswalk.
8. the real-zero-pair q-factor has non-negative coefficients.

**STANDARD EXTERNAL THEOREM**

Cardon / Csordas--Patrick--Varga:

\[
f\in\mathcal{LP}
\iff L_n[f](x)\ge0
\quad\forall x\in\mathbb R,\;n\ge0
\]

under the stated genus/Gaussian-factor hypotheses. These hypotheses include
\(\Xi\).

**FINITE COMPUTATION / PASS**

1. seven new v0.3 tests pass;
2. real-zero finite-product factorization matches derivative coefficients;
3. non-LP quartic negative gate is reproduced exactly;
4. low-order Xi samples are non-negative.

**OPEN**

1. global positivity of all \(L_n[\Xi](x)\);
2. a structural theorem forcing Fourier positivity for the entire \(C_n\) family;
3. an analytic bridge from the positive theta-moment axis \(x=0\) to every real phase \(x\);
4. RH.
