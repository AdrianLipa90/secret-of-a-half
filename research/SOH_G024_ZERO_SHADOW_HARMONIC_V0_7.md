# SOH-G024 v0.7 — zero-shadow decomposition and 4D harmonic lift

**Status:** EXACT ZERO-SET POTENTIAL DECOMPOSITION / OUTER CRITICAL-STRIP BOUNDARY POSITIVE / 6/6 NEW TESTS PASS / RH OPEN  
**Branch:** `proof/theta-nbody-hermitian-bilinear-rigidity-v0.1`  
**Date:** 18 September 2026

## 1. Scope

v0.6 closed the coordinate assembly

\[
\text{theta/N-body}
=
\text{relative-moment tangent}
=
\text{extended-Laguerre resummation}
=
\text{square-quotient weighted Gram diagonal}
\]

and reduced RH to one scalar radial gate.

v0.7 studies that scalar after dividing by the strictly non-negative partition
away from its zeros. The result is an exact zero-set potential decomposition.

No RH claim is made.

## 2. Normalized radial gate

For a real entire function \(f\), put

\[
\mathcal Q_x(q)
=
\frac12 |f(x+i\sqrt q)|^2,
\qquad q>0.
\]

Away from zeros define

\[
\boxed{
\mathcal R_f(x,q)
:=
\frac{\partial_q\mathcal Q_x(q)}{\mathcal Q_x(q)}
=
\partial_q\log\mathcal Q_x(q).
}
\]

With

\[
z=x+iy,
\qquad y=\sqrt q,
\]

direct differentiation gives

\[
\boxed{
\mathcal R_f(x,q)
=
-\frac1y
\Im\frac{f'(z)}{f(z)}.
}
\tag{1}
\]

Since \(\mathcal Q_x(q)>0\) away from zeros, \(\mathcal R_f\) and
\(\partial_q\mathcal Q_x\) have exactly the same sign.

For \(f=\Xi\), v0.5 therefore becomes

\[
\boxed{
RH
\iff
\mathcal R_\Xi(x,q)\ge0
\quad
\forall x\in\mathbb R,\quad 0<q<\frac14,
}
\]

with the inequality interpreted through the unnormalized gate at zeros.

## 3. Canonical paired product for Xi

\(\Xi\) is even, real entire, of order one, and \(\Xi(0)\ne0\). Pairing the
zeros under \(z\mapsto-z\) gives an order-zero product in \(z^2\), because

\[
\sum_\lambda \frac1{|\lambda|^2}<\infty.
\]

Thus the paired logarithmic derivative converges locally normally away from
the zero set. Real zeros occur as pairs \(\pm u\). A non-real zero occurs in
a quartet

\[
\pm(u+iv),
\qquad
\pm(u-iv).
\]

This pairing removes the genus-one exponential factors and permits a
term-by-term decomposition of (1).

## 4. Exact conjugate-pair shadow

Consider only a conjugate pair

\[
u+iv,\qquad u-iv,
\qquad v>0.
\]

Its contribution to the normalized radial gate is

\[
\frac{y-v}
{y\big((x-u)^2+(y-v)^2\big)}
+
\frac{y+v}
{y\big((x-u)^2+(y+v)^2\big)}.
\]

Combining the fractions gives the exact shadow kernel

\[
\boxed{
S_{u,v}(x,y)
=
\frac{
2\big((x-u)^2+y^2-v^2\big)
}{
\big((x-u)^2+(y-v)^2\big)
\big((x-u)^2+(y+v)^2\big)
}.
}
\tag{2}
\]

The denominator is positive away from the zero. Therefore

\[
\boxed{
\operatorname{sgn}S_{u,v}(x,y)
=
\operatorname{sgn}\!\left((x-u)^2+y^2-v^2\right).
}
\tag{3}
\]

Hence the pair contributes negatively exactly inside the open disk

\[
\boxed{
D_{u,v}
=
\left\{
(x,y):
(x-u)^2+y^2<v^2,\quad y>0
\right\}.
}
\tag{4}
\]

It vanishes on the circular boundary and is positive outside it.

This disk is the exact radial-q shadow of the off-axis zero.

## 5. Real pairs and complex quartets

A real zero pair \(\pm u\) contributes

\[
\boxed{
P_u(x,y)
=
\frac1{(x-u)^2+y^2}
+
\frac1{(x+u)^2+y^2}
>0.
}
\tag{5}
\]

A complex quartet \(\pm(u\pm iv)\) contributes

\[
\boxed{
P_{u,v}(x,y)
=
S_{u,v}(x,y)+S_{-u,v}(x,y).
}
\tag{6}
\]

Therefore the complete normalized Xi gate is the locally normally convergent
sum

\[
\boxed{
\mathcal R_\Xi(x,y^2)
=
\sum_{\text{real pairs}}P_u(x,y)
+
\sum_{\text{complex quartets}}P_{u,v}(x,y).
}
\tag{7}
\]

No RH assumption enters (7).

## 6. Zero-shadow localization theorem

Every real-pair term is strictly positive. Every conjugate-pair term is
negative only in its disk (4). Consequently

\[
\boxed{
\{\mathcal R_\Xi<0\}
\subseteq
\bigcup_{\text{off-axis zeros }u\pm iv}
D_{u,v}\cup D_{-u,v}.
}
\tag{8}
\]

Conversely, if \(u+iv\) is an off-axis zero, then along \(x=u\) and
\(y\to v^{-}\),

\[
S_{u,v}(u,y)\to-\infty.
\]

All non-coincident zero contributions remain finite there, while multiplicity
only strengthens the same divergence. Hence every off-axis zero produces
negative radial-gate points immediately below its zero shell.

Thus the v0.5 Achilles descent is localized exactly: a hypothetical RH
violation casts a finite-radius negative shadow whose radius is its transverse
distance from the critical line.

## 7. Unconditional positivity on the outer critical-strip boundary

For a nontrivial zeta zero

\[
\rho=\beta+i\gamma,
\qquad 0<\beta<1,
\]

the corresponding Xi zero is

\[
z_\rho
=
\gamma+i\left(\frac12-\beta\right).
\]

Therefore every Xi zero satisfies

\[
|v|<\frac12.
\]

At the outer boundary \(y=1/2\), each non-real conjugate-pair numerator in
(2) is

\[
(x-u)^2+\frac14-v^2>0,
\]

and every real-pair term is also positive. Hence, term by term,

\[
\boxed{
\mathcal R_\Xi\!\left(x,\frac14\right)>0
\qquad
\forall x\in\mathbb R.
}
\tag{9}
\]

This is unconditional and uses only the classical fact that the nontrivial
zeta zeros lie in the open critical strip.

The open RH gate therefore cannot first fail on the outer boundary
\(q=1/4\). Any failure is an interior zero-shadow phenomenon.

## 8. Exact 4D harmonic lift

Let

\[
U(x,q)=\log\mathcal Q_x(q)
\]

away from the zero set. Since

\[
U(x,y^2)
=
\log|f(x+iy)|^2-\log2
\]

is harmonic in the ordinary \((x,y)\)-plane,

\[
\boxed{
U_{xx}+2U_q+4qU_{qq}=0.
}
\tag{10}
\]

Set

\[
\mathcal R=U_q.
\]

Differentiating (10) gives

\[
\boxed{
\mathcal R_{xx}
+
6\mathcal R_q
+
4q\mathcal R_{qq}
=
0.
}
\tag{11}
\]

Now define

\[
W(x,y)=\mathcal R(x,y^2).
\]

A change of variables gives

\[
\boxed{
W_{xx}+W_{yy}+\frac2yW_y=0.
}
\tag{12}
\]

Equation (12) is precisely the Laplace equation in four Euclidean dimensions
for a function that depends on one Cartesian coordinate \(x\) and only on the
radius

\[
y=|\mathbf Y|,
\qquad \mathbf Y\in\mathbb R^3.
\]

Thus the normalized RH gate is an axisymmetric 4D harmonic field away from the
lifted zero set.

Under this lift, a conjugate pair \(u\pm iv\) becomes the singular two-sphere

\[
x=u,
\qquad
|\mathbf Y|=v.
\]

Its shadow disk (4) becomes the interior of the corresponding 4D ball in the
\((x,|\mathbf Y|)\) quotient.

Real zeros correspond to \(v=0\) and contribute positive point-source kernels.

## 9. What this changes

The remaining sign problem is no longer geometrically diffuse.

The exact structure is now:

\[
\boxed{
\text{off-axis zero}
\Longleftrightarrow
\text{interior singular zero shell}
\Longrightarrow
\text{negative radial shadow immediately below it}.
}
\]

Moreover,

\[
\boxed{
q=\frac14
\text{ is strictly positive unconditionally}.
}
\]

So the active theorem can be stated as a source-exclusion problem for an
axisymmetric harmonic field: prove that the Xi field has no interior
off-axis zero shells.

This is still RH-equivalent. The harmonic reformulation does not by itself
exclude such shells.

## 10. Regression

New artifacts:

- `src/secret_of_a_half/g024_zero_shadow_harmonic.py`
- `tests/test_g024_zero_shadow_harmonic.py`
- `scripts/run_soh_g024_zero_shadow_harmonic.py`
- `reports/SOH_G024_ZERO_SHADOW_HARMONIC_RECEIPT_V0_7.json`

Fresh local test result:

```text
6 passed
```

The deterministic receipt checks:

1. exact conjugate-pair shadow identity;
2. exact even-quartet decomposition;
3. inside / boundary / outside shadow signs;
4. strict positivity of a real-zero pair;
5. the 4D harmonic PDE residual;
6. finite high-precision Xi samples on \(q=1/4\).

The Xi samples are diagnostics only. Equation (9) is analytic and does not
depend on those samples.

## 11. Proof firewall

**EXACT / PROVED**

1. normalized gate identity (1);
2. canonical paired-product decomposition for Xi;
3. conjugate-pair shadow formula (2);
4. disk sign law (3)–(4);
5. real-pair and quartet formulas (5)–(7);
6. negative-set containment (8);
7. negative divergence immediately below every off-axis zero;
8. unconditional outer-boundary positivity (9);
9. q-harmonic equation (10), gate equation (11), and 4D lift (12).

**FINITE REGRESSION**

- 6/6 new tests PASS;
- deterministic v0.7 receipt PASS;
- Xi outer-boundary sample values are finite high-precision diagnostics only.

**NOT PROVED**

- that the absence of boundary negativity alone excludes interior zero shells;
- any maximum-principle argument across unknown singular shells;
- RH.

**OPEN**

The remaining theorem is still equivalent to excluding every off-axis Xi zero.
v0.7 localizes the obstruction: any counterexample must create an interior
zero shell and an associated negative shadow strictly below \(q=1/4\).
