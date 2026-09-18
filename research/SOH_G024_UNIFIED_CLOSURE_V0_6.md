# SOH-G024 v0.6 — Unified closure: radial gate, Laguerre generator, and quotient Gram diagonal

**Status:** EXACT COMMUTING CROSSWALK / SINGLE SCALAR RH-EQUIVALENT FRONTIER / 6/6 NEW TESTS PASS / RH OPEN  
**Branch:** `proof/theta-nbody-hermitian-bilinear-rigidity-v0.1`  
**Date:** 18 September 2026

## 1. Scope

v0.2 corrected the complex continuation to the Hermitian Jensen channel.
v0.3 identified the q-partition with the generating function of the extended
Laguerre hierarchy. v0.4 exposed the relative-moment / positive-definite
physical-space structure and its generic no-go boundary. v0.5 reduced RH to
the sign of the first radial q-response in the critical strip.

v0.6 fits those blocks together and crosswalks them with the independent
SOH-G025 square-quotient / dual-Gram construction.

No new RH claim is made. The output is a single exact scalar gate expressed in
four coordinate systems.

## 2. Common generating object

For a real entire function f define

\[
\mathcal Q_x(q)
=
\frac12f(x+i\sqrt q)f(x-i\sqrt q)
=
\frac12|f(x+i\sqrt q)|^2,
\qquad q\ge0.
\]

For the Riemann function \(f=\Xi\),

\[
\mathcal Q_x(q)=\mathcal Z(-ix,\sqrt q).
\]

The v0.5 Achilles criterion is

\[
\boxed{
RH
\iff
\partial_q\mathcal Q_x(q)\ge0
\quad
\forall x\in\mathbb R,\quad0<q<\frac14.
}
\tag{A}
\]

## 3. Extended-Laguerre resummation

v0.3 gives

\[
2\mathcal Q_x(q)
=
\sum_{n=0}^{\infty}L_n[f](x)q^n.
\]

Therefore

\[
\boxed{
\partial_q\mathcal Q_x(q)
=
\frac12
\sum_{n=1}^{\infty}
nL_n[f](x)q^{n-1}.
}
\tag{B}
\]

Thus the first-q gate is the positive-q resummation of the complete extended
Laguerre hierarchy.

The infinite coefficientwise LP cone is therefore compressed, for Xi, to one
one-parameter radial gate on the critical q-interval.

## 4. Relative-moment / physical-space tangent

v0.4 defines

\[
C_n(u)
=
\int_{\mathbb R}r^{2n}K(u+r)K(u-r)\,dr
\]

and

\[
B_{\sqrt q}(u)
=
\sum_{n=0}^{\infty}
\frac{4^nq^n}{(2n)!}C_n(u).
\]

Differentiate:

\[
\boxed{
G_q(u)
:=
\partial_qB_{\sqrt q}(u)
=
\sum_{n=1}^{\infty}
\frac{n4^nq^{n-1}}{(2n)!}C_n(u).
}
\tag{C}
\]

Using the v0.3 Fourier normalization,

\[
L_n[f](x)
=
\frac{2^{2n+1}}{(2n)!}\widehat C_n(2x),
\]

equations (B) and (C) give

\[
\boxed{
\widehat G_q(2x)
=
\partial_q\mathcal Q_x(q).
}
\tag{D}
\]

Hence (A) is exactly

\[
\boxed{
RH
\iff
G_q\text{ is positive definite for every }0<q<\frac14.
}
\]

## 5. Square quotient

Use the exact square quotient

\[
\Xi(z)=F(-z^2).
\]

Put

\[
z=x+iy,
\qquad
q=y^2,
\qquad
w=-z^2.
\]

Then

\[
w=q-x^2-2ix\sqrt q
\]

and the inverse radial coordinate is

\[
\boxed{
q=\frac{|w|+\Re w}{2}.
}
\tag{E}
\]

Thus the critical strip \(0<|y|<1/2\) maps to

\[
\boxed{
\Omega_{1/2}
=
\left\{
w\in\mathbb C:
0<
\frac{|w|+\Re w}{2}
<
\frac14
\right\}.
}
\tag{F}
\]

The q-partition becomes

\[
\mathcal Q_x(q)
=
\frac12F(w)\overline{F(w)}.
\]

Differentiating at fixed x gives the pole-free formula

\[
\boxed{
\partial_q\mathcal Q_x(q)
=
\Re\!\left(F'(w)\overline{F(w)}\right)
+
\frac{x}{\sqrt q}
\Im\!\left(F'(w)\overline{F(w)}\right).
}
\tag{G}
\]

## 6. Exact G024 / G025 dual-Gram crosswalk

G025 defines the pole-free dual kernels

\[
\widehat K_0(w,v)
=
\frac{
wF'(w)\overline{F(v)}
-
\bar vF(w)\overline{F'(v)}
}{
w-\bar v
},
\]

\[
\widehat K_1(w,v)
=
\frac{
F(w)\overline{F'(v)}
-
F'(w)\overline{F(v)}
}{
w-\bar v
}.
\]

On the diagonal, for non-real w,

\[
\widehat K_0(w,w)
=
\frac{
wF'(w)\overline{F(w)}
-
\bar wF(w)\overline{F'(w)}
}{
w-\bar w
},
\]

\[
\widehat K_1(w,w)
=
\frac{
F(w)\overline{F'(w)}
-
F'(w)\overline{F(w)}
}{
w-\bar w
}.
\]

Write \(w=a+ib\) and
\(F'(w)\overline{F(w)}=A+iB\). Then

\[
\widehat K_0=A+\frac{a}{b}B,
\qquad
\widehat K_1=-\frac{B}{b}.
\]

Because

\[
a-|w|=-2x^2,
\qquad
b=-2x\sqrt q,
\]

we have

\[
\frac{a-|w|}{b}=\frac{x}{\sqrt q}.
\]

Substitution into (G) gives the exact identity

\[
\boxed{
\partial_q\mathcal Q_x(q)
=
\widehat K_0(w,w)
+
|w|\widehat K_1(w,w).
}
\tag{H}
\]

For \(x=0\), \(w=q>0\), the continuous diagonal limits are

\[
\widehat K_1(w,w)
=
F'(w)^2-F(w)F''(w),
\]

\[
\widehat K_0(w,w)
=
F(w)F'(w)
+
w\bigl(F(w)F''(w)-F'(w)^2\bigr),
\]

and (H) reduces to

\[
\partial_q\mathcal Q_0(q)=F(q)F'(q).
\]

Therefore the G024 Achilles gate and the G025 dual-Gram geometry are the same
scalar object on the quotient-plane diagonal.

## 7. Single quotient-plane criterion

Combining (A), (E), (F), and (H),

\[
\boxed{
RH
\iff
\widehat K_0(w,w)
+
|w|\widehat K_1(w,w)
\ge0
\quad
\forall w\in\Omega_{1/2}.
}
\tag{RH-Gram}
\]

This is strictly a diagonal weighted-sum requirement on the parabolic image of
the critical strip.

Full G025 Stieltjes positivity makes both Gram kernels positive semidefinite and
therefore implies this diagonal inequality. But full G025 positivity is itself
RH-equivalent. v0.6 does not promote it as an independent proof.

The useful reduction is that the SOH-G024/G025 interface now has one scalar
target, not two unrelated positivity hierarchies.

## 8. Commuting closure diagram

All active representations now meet at the same quantity:

\[
\boxed{
\begin{array}{ccc}
\{C_n(u)\}
&\xrightarrow{\text{q-resum}}&
G_q(u)
\\[4pt]
\downarrow\mathcal F
&&
\downarrow\mathcal F
\\[4pt]
\{L_n[f](x)\}
&\xrightarrow{\text{q-resum}}&
\partial_q\mathcal Q_x(q)
\\[4pt]
&&
\updownarrow
\\[-2pt]
&&
\widehat K_0(w,w)+|w|\widehat K_1(w,w)
\end{array}
}
\]

with

\[
w=-(x+i\sqrt q)^2.
\]

For Xi, non-negativity of the bottom-right scalar throughout
\(\Omega_{1/2}\) is exactly RH.

## 9. Regression

New artifacts:

- `src/secret_of_a_half/g024_unified_closure.py`
- `tests/test_g024_unified_closure.py`
- `scripts/run_soh_g024_unified_closure.py`
- `reports/SOH_G024_UNIFIED_CLOSURE_RECEIPT_V0_6.json`

Fresh staging result:

```text
6 passed
```

The deterministic receipt includes:

1. exact \(q\leftrightarrow w\) roundtrip;
2. exact linear-quotient dual-Gram / radial / Laguerre agreement;
3. the positive-real-axis continuous diagonal limit;
4. critical-strip image checks;
5. an 80-digit Riemann diagnostic at
   \(x=14.134725141734693790,\ q=0.01\), where the quotient-Gram and radial
   formulas agree to approximately \(2\times10^{-87}\).

The Riemann number is a finite diagnostic only.

## 10. Proof firewall

**EXACT**

1. equations (B)–(H);
2. the commuting closure diagram;
3. the quotient-plane image condition (F);
4. the weighted dual-Gram diagonal criterion (RH-Gram), conditional only on the
   already-proved v0.5 RH-q equivalence and the exact square quotient.

**FINITE REGRESSION**

- 6/6 new tests PASS;
- deterministic v0.6 receipt PASS;
- the Xi crosswalk sample is finite high-precision evidence only.

**NOT ENOUGH BY ITSELF**

- positive Taylor coefficients of F;
- generic strong log-concavity;
- fixed-u Hankel positivity of the relative moments;
- positive definiteness of the undifferentiated B-path;
- finite G025 Hankel gates.

**OPEN**

- prove
  \[
  \widehat K_0(w,w)+|w|\widehat K_1(w,w)\ge0
  \]
  throughout \(\Omega_{1/2}\) from Riemann-specific structure;
- equivalently prove the v0.5 radial gate / PD tangent;
- RH.

## 11. Closure verdict

The SOH-G024 algebraic assembly is closed:

\[
\boxed{
\text{theta/N-body}
=
\text{relative-moment tangent}
=
\text{extended-Laguerre resummation}
=
\text{square-quotient weighted Gram diagonal}.
}
\]

There is no remaining coordinate mismatch between those routes.

The remaining problem is one sign theorem for one scalar function on one
explicit quotient-plane domain. That theorem is RH-equivalent and remains
unproved.
