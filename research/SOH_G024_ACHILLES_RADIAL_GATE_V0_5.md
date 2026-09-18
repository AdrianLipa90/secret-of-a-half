# SOH-G024 v0.5 — Achilles radial gate: zero-touch geometry

**Status:** EXACT RH-EQUIVALENT REDUCTION / PD-TANGENT CROSSWALK EXACT / 7/7 NEW TESTS PASS / RH OPEN  
**Branch:** `proof/theta-nbody-hermitian-bilinear-rigidity-v0.1`  
**Date:** 18 September 2026

## 1. Scope

v0.2 corrected the complex continuation to the Hermitian Jensen channel; v0.3 identified the q-expansion with the extended Laguerre hierarchy; v0.4 showed that generic strong log-concavity, fixed-u Hankel positivity and positivity of the generating mixture are not enough to force coefficientwise Fourier positivity.

v0.5 isolates a smaller exact target. For Riemann Xi,

\[
\boxed{
RH\iff \partial_q\mathcal Q_x(q)\ge0
\quad\forall x\in\mathbb R,\quad0<q<\frac14.
}
\]

This is an RH-equivalent reduction, not a proof of RH.

## 2. q-partition

For a real entire function f define

\[
\boxed{
\mathcal Q_x(q)=\frac12f(x+i\sqrt q)f(x-i\sqrt q)
=\frac12|f(x+i\sqrt q)|^2\ge0,\qquad q\ge0.
}
\]

The product is even in \(\sqrt q\), hence entire in q. For the SOH two-body partition,

\[
\mathcal Q_x(q)=\mathcal Z(-ix,\sqrt q).
\]

Thus q is the square transverse coordinate of the Wick-rotated N-body geometry.

## 3. First-q response

With \(z=x+iy\), \(y=\sqrt q>0\),

\[
\partial_y\mathcal Z(-ix,y)
=-\Im\!\left(f'(z)\overline{f(z)}\right),
\]

so

\[
\boxed{
2\partial_q\mathcal Q_x(q)
=\frac1y\Im\!\left[-f'(z)\overline{f(z)}\right].
}
\tag{A}
\]

At q=0,

\[
\boxed{
\partial_q\mathcal Q_x(0)
=\frac12\left(f'(x)^2-f(x)f''(x)\right)
=\frac12L_1[f](x).
}
\]

Csordas--Escassut, *The Laguerre inequality and the distribution of zeros of entire functions*, Ann. Math. Blaise Pascal 12 (2005), DOI `10.5802/ambp.210`, Theorem 2.3, gives for the stated class S(A)

\[
f\in\mathcal{LP}
\iff
\frac1y\Im\!\left[-f'(z)\overline{f(z)}\right]\ge0.
\]

Therefore (A) is exactly the classical complex Laguerre-I criterion expressed as the first radial response of the SOH N-body partition.

## 4. Zero-touch geometry

Suppose \(z_0=x_0+iy_0\), \(y_0\ne0\), is a zero of multiplicity m. Put \(q_0=y_0^2\) and
\[
a=\frac{f^{(m)}(z_0)}{m!}\ne0.
\]

Along x=x0,

\[
\boxed{
\mathcal Q_{x_0}(q)
=
\frac{|a|^2}{2(2|y_0|)^{2m}}
(q-q_0)^{2m}
+O((q-q_0)^{2m+1}).
}
\tag{B}
\]

Thus an off-axis zero is an even-order touchdown of a non-negative surface. Testing \(\mathcal Q\ge0\) cannot reveal it.

## 5. Achilles radial-descent theorem

If a nonzero real entire f has an off-axis zero \(f(x_0+iy_0)=0\), then there exists
\[
q_*\in(0,y_0^2)
\]
such that
\[
\boxed{\partial_q\mathcal Q_{x_0}(q_*)<0.}
\tag{C}
\]

Proof: if \(\mathcal Q_{x_0}(0)>0\), the mean value theorem applied between q=0 and the zero q0 gives a negative derivative. If \(\mathcal Q_{x_0}(0)=0\) and the derivative were non-negative throughout, Q would be nondecreasing with equal zero endpoint values, hence identically zero on an interval; analyticity would force f to vanish identically. Contradiction.

So every off-axis zero must advertise itself by a negative radial response before the touchdown.

## 6. Critical-strip localization

For
\[
f(z)=\Xi(z)=\xi\!\left(\frac12+iz\right),
\]
all Xi zeros correspond to nontrivial zeta zeros. Since those lie in \(0<\Re s<1\), every Xi zero has
\[
|\Im z|<\frac12.
\]
Hence every RH-violating zero has
\[
0<q<\frac14.
\]

If RH holds, Xi belongs to LP, so (A) is non-negative globally. Conversely, if the q-gate is non-negative for all x and \(0<q<1/4\), theorem (C) excludes every possible off-axis Xi zero. Therefore

\[
\boxed{
RH
\iff
\partial_q\mathcal Q_x(q)\ge0
\quad\forall x\in\mathbb R,\ 0<q<\frac14.
}
\tag{RH-q}
\]

Equivalently,

\[
\boxed{
\neg RH
\iff
\exists x\in\mathbb R,\ q\in(0,\tfrac14):
\partial_q\mathcal Q_x(q)<0.
}
\]

## 7. Positive-definite tangent formulation

v0.4 defined

\[
B_y(u)=\int_{\mathbb R}\cosh(2yr)K(u+r)K(u-r)\,dr
\]

with

\[
\widehat B_y(2x)=\frac12|f(x+iy)|^2.
\]

Set \(\widetilde B_q=B_{\sqrt q}\). Then

\[
\widehat{\widetilde B_q}(2x)=\mathcal Q_x(q)\ge0,
\]

so the path q -> \(\widetilde B_q\) lies in the positive-definite cone unconditionally.

For q>0 define its tangent

\[
\boxed{
G_q(u)=\partial_q\widetilde B_q(u)
=
\int_{\mathbb R}
\frac{r\sinh(2\sqrt q\,r)}{\sqrt q}
K(u+r)K(u-r)\,dr.
}
\]

The integrand is pointwise non-negative, and \(G_0=2C_1\). Fourier differentiation gives

\[
\boxed{
\widehat G_q(2x)=\partial_q\mathcal Q_x(q).
}
\]

Hence

\[
\boxed{
RH
\iff
G_q\text{ is positive definite for every }0<q<\frac14.
}
\tag{RH-PD}
\]

Geometrically, RH is equivalent to the positive-definite path \(\widetilde B_q\) having a positive-definite tangent throughout the critical q-interval.

This resums the infinite extended-Laguerre hierarchy into one one-parameter tangent family.

## 8. Hermitian curvature link

The v0.2 Hermitian quantity satisfies

\[
\boxed{
H_f(x+iy)
=2\mathcal Q_q(x,q)+4q\mathcal Q_{qq}(x,q).
}
\]

Also

\[
\boxed{
\mathcal Q_{xx}
+2\mathcal Q_q
+4q\mathcal Q_{qq}
=2|f'(x+i\sqrt q)|^2\ge0.
}
\]

Csordas--Escassut Theorem 2.4 states that the global Hermitian inequality is also LP-equivalent and interprets it as convexity of \(|f(x+iy)|^2\) in y. For Xi, non-negativity of H throughout the critical strip is likewise RH-equivalent.

The first-q gate is the cleaner zero witness: a touchdown necessarily requires radial descent.

## 9. Exact adversarial control

For
\[
f(z)=z^2+1
\]
the off-axis zeros are +/-i and at x=0

\[
\boxed{\mathcal Q_0(q)=\frac12(1-q)^2.}
\]

The zero at q0=1 is a quadratic touchdown with leading coefficient 1/2, while

\[
\boxed{\mathcal Q_0'(q)=q-1<0\quad(0\le q<1).}
\]

At q=1/4:
\[
\mathcal Q_0=9/32,\qquad \mathcal Q_0'=-3/4,\qquad H=-1/2.
\]

This exactly reproduces descent -> touchdown.

## 10. Computation

New artifacts:

- `src/secret_of_a_half/g024_achilles_radial_gate.py`
- `tests/test_g024_achilles_radial_gate.py`
- `scripts/run_soh_g024_achilles_radial_gate.py`
- `reports/SOH_G024_ACHILLES_RADIAL_GATE_RECEIPT_V0_5.json`

The first local run returned 6 PASS / 1 FAIL because one test used strict mpf equality for a value expected to be -0.1. The mathematical value agreed to working precision. The assertion was replaced by an explicit high-precision tolerance and the suite was rerun:

```text
7 passed
```

No failure was suppressed.

The 80-digit receipt also samples Xi. All declared samples have positive radial response, including x=14.134725141734693790, q=0.01 and x=50, q=0.24. These are finite diagnostics only.

## 11. Final frontier

The active proof target is now

\[
\boxed{
\text{prove }G_q\text{ is positive definite for every }0<q<1/4.
}
\]

Equivalently, prove

\[
\boxed{
\partial_q\mathcal Q_x(q)\ge0
\quad\forall x\in\mathbb R,\ 0<q<1/4.
}
\]

v0.4 already excludes a closure based only on generic strong log-concavity, pointwise moment/Hankel positivity, or positivity of the undifferentiated generating path. Any proof still requires Riemann-specific structure, most plausibly the exact theta-channel ordering, modular self-duality, or a q-flow identity coupled to the square-quotient/Stieltjes geometry.

## 12. Proof firewall

**EXACT / PROVED:** q-partition identity; radial-response identity (A); touchdown expansion (B); negative-response witness theorem (C); critical-strip localization; RH-q equivalence; PD-tangent identity and RH-PD equivalence; Hermitian q-identity; q-Laplacian identity.

**STANDARD EXTERNAL ALIGNMENT:** Csordas--Escassut Theorems 2.3 and 2.4 give the complex Laguerre-I and Hermitian LP criteria for the stated class.

**FINITE COMPUTATION:** 7/7 new tests PASS after the disclosed assertion correction; deterministic receipt PASS; Xi samples are diagnostic only.

**OPEN:** a global proof of the radial gate / PD tangent for Xi; RH.
