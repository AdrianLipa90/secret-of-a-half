# SOH Explicit Sharp-to-Smooth Weil-Form Rate v0.1

Status: **EXACT_EXPLICIT_FORM_RATE / LIV-MD2c4b2 CLOSED / EFFECTIVE_FIXED-a_SHARP_RESOLVENT_RATE CLOSED / LARGE-a JOINT RATE OPEN**

Date: 2026-09-26

Parents:
- \`research/SOH_EXPLICIT_GLOBAL_LIVSIC_SHIFT_V0_1.md\`
- \`research/SOH_QUANTITATIVE_OPERATOR_DOMAIN_RESOLVENT_RATE_V0_1.md\`
- \`research/SOH_NEGATIVE_SHIFT_RESOLVENT_WEIL_FIRST_CORRECTION_V0_1.md\`
- \`research/SOH_PIECEWISE_EXPONENTIAL_WEIL_CROSS_CONVOLUTION_V0_1.md\`

Primary external source:
- Masatoshi Suzuki, *Weil's quadratic form via the screw function*,
  arXiv:2606.09096v3.
- Section 3.2 proves form-core approximation by boundary cutoffs and uses the
  two Fourier estimates
  \[
  |\widehat w_\delta(z)|\le 2\delta
  \]
  and
  \[
  |\widehat w_\delta(z)|\le M/|z|
  \]
  for the unit-modulus Fourier basis vectors.
- Equation (2.7) gives the exact logarithmic Fourier symbol of the source
  operator \(B_a\).

No RH and no zero list are used.

## 1. Source-scaled boundary layer

Work in Suzuki's scaled interval \([-1,1]\).

For \(a>0\), real \(p\), and

\[
0<\delta\le e^{-1},
\]

define the sharp exponential

\[
h_{a,p}(u)=e^{pa u}.
\]

Let \(\eta_\delta\) be a monotone endpoint cutoff satisfying

\[
\eta_\delta(u)=1
\quad
(|u|\le1-\delta),
\]

\[
\eta_\delta(\pm1)=0,
\]

and on each boundary layer

\[
|\eta_\delta'(u)|\le\delta^{-1}.
\]

Define

\[
u_{a,p,\delta}=h_{a,p}\eta_\delta,
\qquad
w_{a,p,\delta}=h_{a,p}-u_{a,p,\delta}.
\]

Thus \(w_{a,p,\delta}\) is supported on the two endpoint layers of total length
\(2\delta\).

Put

\[
B_{a,p}=e^{|p|a},
\qquad
q_{a,p}=|p|a.
\]

Then

\[
|w_{a,p,\delta}(u)|
\le B_{a,p},
\]

hence

\[
\boxed{
\|w_{a,p,\delta}\|_1
\le
2\delta B_{a,p},
}
\]

and

\[
\boxed{
\|w_{a,p,\delta}\|_2^2
\le
2\delta B_{a,p}^2.
}
\]

## 2. Explicit Fourier bounds

With Suzuki's Fourier convention

\[
\widehat w(z)
=
\int_{-1}^{1}w(u)e^{izu}\,du,
\]

the \(L^1\) bound gives

\[
\boxed{
|\widehat w(z)|
\le
2\delta B_{a,p}.
}
\]

For the high-frequency estimate, integration by parts gives

\[
|\widehat w(z)|
\le
\frac{
|w(1)|+|w(-1)|+\|w'\|_1
}{
|z|
}.
\]

The endpoint term is bounded by

\[
|w(1)|+|w(-1)|
\le
2B_{a,p}.
\]

Moreover,

\[
w'
=
pa\,e^{pau}(1-\eta_\delta)
-
e^{pau}\eta_\delta',
\]

so

\[
\|w'\|_1
\le
2q_{a,p}\delta B_{a,p}
+
2B_{a,p}.
\]

Therefore

\[
\boxed{
|\widehat w(z)|
\le
\frac{
M_{a,p,\delta}
}{
|z|
},
}
\]

where

\[
\boxed{
M_{a,p,\delta}
=
2B_{a,p}
\left(
2+q_{a,p}\delta
\right).
}
\]

This removes the hidden \(O(1)\) constant from the source cutoff argument for
this exponential family.

## 3. Exact logarithmic form identity

Suzuki's exact Fourier formula for \(B_a\), combined with the unitary scaling
used in his equation (4.5), gives for the source-scaled logarithmic form

\[
\boxed{
\mathcal L(w)
=
\frac1{2\pi}
\int_{\mathbb R}
\left(
\log|z|+\gamma
\right)
|\widehat w(z)|^2\,dz.
}
\]

The spatial representation of \(\mathcal L\) also shows

\[
\mathcal L(w)\ge0.
\]

For an upper bound we therefore may use

\[
\mathcal L(w)
\le
\frac1{2\pi}
\int_{\mathbb R}
\left(
|\log|z||+\gamma
\right)
|\widehat w(z)|^2\,dz.
\]

## 4. Closed boundary-layer majorant

Let

\[
L_\delta=\log(1/\delta).
\]

Split the Fourier integral at

\[
|z|=\delta^{-1}.
\]

For the low region use

\[
|\widehat w|
\le
2\delta B_{a,p}.
\]

For the high region use

\[
|\widehat w|
\le
M_{a,p,\delta}/|z|.
\]

The elementary integrals are

\[
\int_0^{1/\delta}
\left(
|\log z|+\gamma
\right)\,dz
=
2+
\frac{
L_\delta-1+\gamma
}{
\delta
},
\]

and

\[
\int_{1/\delta}^{\infty}
\frac{
\log z+\gamma
}{
z^2
}\,dz
=
\delta
\left(
L_\delta+1+\gamma
\right).
\]

Hence

\[
\boxed{
\mathcal L(w_{a,p,\delta})
\le
\mathcal E_{\log}(a,p,\delta),
}
\]

with

\[
\boxed{
\begin{aligned}
\mathcal E_{\log}(a,p,\delta)
:=
\frac1{2\pi}
\Bigg[
&
8B_{a,p}^2\delta^2
\left(
2+
\frac{
L_\delta-1+\gamma
}{
\delta
}
\right)
\\
&+
2M_{a,p,\delta}^2
\delta
\left(
L_\delta+1+\gamma
\right)
\Bigg].
\end{aligned}
}
\]

In particular, for fixed \(a,p\),

\[
\boxed{
\mathcal E_{\log}(a,p,\delta)
=
O_{a,p}
\left(
\delta\log(1/\delta)
\right).
}
\]

This makes Suzuki's qualitative form-core rate explicit for the exponential
family used in the Livšic channel.

## 5. Bounded arithmetic/remainder perturbation

The already-proved source-scaled decomposition gives

\[
R(a,w)
=
-\log a-\log(2\pi)-\gamma
+
\frac{\mathcal L(w)}{\|w\|_2^2}
-
P_a(w)
-
J_a(w),
\]

with the unconditional bounds

\[
|P_a(w)|
\le
8ae^a,
\]

and

\[
|J_a(w)|
\le
4a\cosh a+\frac a2.
\]

Define

\[
C_{\rm pert}(a)
=
\left|
\log a+\log(2\pi)+\gamma
\right|
+
8ae^a
+
4a\cosh a
+
\frac a2.
\]

Then the source-scaled Weil form obeys

\[
\boxed{
|Q_W^{a,\rm sc}(w)|
\le
\mathcal L(w)
+
C_{\rm pert}(a)\|w\|_2^2.
}
\]

## 6. Explicit shifted form-norm rate

Let

\[
\lambda_{\rm sh}(a)
=
-\log a-\log(2\pi)-\gamma
-8ae^a
-4a\cosh a
-\frac a2
-1.
\]

The corresponding shifted form is positive:

\[
T_a=A_a-\lambda_{\rm sh}(a)I\ge I.
\]

In scaled coordinates,

\[
\|w\|_{T_a}^2
=
Q_W^{a,\rm sc}(w)
-
\lambda_{\rm sh}(a)\|w\|_2^2.
\]

Therefore

\[
\boxed{
\|w_{a,p,\delta}\|_{T_a}^2
\le
\mathcal E_T(a,p,\delta),
}
\]

where

\[
\boxed{
\mathcal E_T(a,p,\delta)
=
\mathcal E_{\log}(a,p,\delta)
+
2\delta B_{a,p}^2
\left[
C_{\rm pert}(a)
+
|\lambda_{\rm sh}(a)|
\right].
}
\]

Thus

\[
\boxed{
\|h_{a,p}-u_{a,p,\delta}\|_{T_a}
\le
\sqrt{
\mathcal E_T(a,p,\delta)
}.
}
\]

For every fixed \(a,p\),

\[
\boxed{
\mathcal E_T(a,p,\delta)
=
O_{a,p}
\left(
\delta\log(1/\delta)
\right),
}
\]

and all constants are displayed.

This closes the explicit sharp-to-smooth form-norm gate.

## 7. Uniformity on compact spectral sets

Let

\[
K\Subset\{p\in\mathbb C:\Re p>1/2\}.
\]

The same argument applies after replacing

\[
B_{a,p}
\]

by

\[
B_{a,K}
=
\exp
\left(
a\sup_{p\in K}|p|
\right),
\]

and

\[
q_{a,p}
\]

by

\[
q_{a,K}
=
a\sup_{p\in K}|p|.
\]

Therefore

\[
\boxed{
\sup_{p\in K}
\|h_{a,p}-u_{a,p,\delta}\|_{T_a}
\le
\sqrt{
\mathcal E_T(a,K,\delta)
}
\to0
}
\]

as \(\delta\to0\), with an explicit compact-uniform majorant.

## 8. Resolvent contraction in the form metric

For \(T=T^*\ge I\), define

\[
S_\mu
=
\mu T(T+\mu I)^{-1}.
\]

Spectral calculus gives

\[
0\le S_\mu\le T
\]

in quadratic-form order.

Hence, for form-domain vectors,

\[
\boxed{
|\langle f,S_\mu g\rangle|
\le
\|f\|_T\|g\|_T.
}
\]

Therefore replacing sharp exponential vectors by endpoint-zero cutoffs does
not introduce any factor growing with \(\mu\).

Let

\[
f=h_{a,p},
\qquad
g=h_{a,q},
\]

and

\[
f_\delta=u_{a,p,\delta},
\qquad
g_\delta=u_{a,q,\delta}.
\]

Then

\[
\begin{aligned}
&
|\langle f,S_\mu g\rangle
-
\langle f_\delta,S_\mu g_\delta\rangle|
\\
&\le
\|f-f_\delta\|_T\|g\|_T
+
\|f_\delta\|_T\|g-g_\delta\|_T.
\end{aligned}
\]

The identical estimate holds for the shifted form pairing

\[
\langle T^{1/2}f,T^{1/2}g\rangle.
\]

Thus the sharp-to-smooth approximation error is controlled uniformly in the
negative-shift resolvent parameter.

## 9. Effective fixed-\(a\) sharp-vector resolvent rate

For the endpoint-zero approximants, the previous theorem gives

\[
\left|
\langle f_\delta,S_\mu g_\delta\rangle
-
\langle f_\delta,Tg_\delta\rangle
\right|
\le
\frac{
M_a(f_\delta)M_a(g_\delta)
}{
\mu+1
}.
\]

Combining this with Section 8 and the explicit form errors from Section 6
gives a fully computable fixed-\(a\) bound for the sharp vectors.

Schematically,

\[
\boxed{
E_{\rm sharp}(a,p,q;\delta,\mu)
\le
E_{\rm form}(a,p,q;\delta)
+
\frac{
M_a(u_{a,p,\delta})
M_a(u_{a,q,\delta})
}{
\mu+1
},
}
\]

where every quantity on the right is explicit.

For any fixed \(a,p,q\) and requested tolerance \(\varepsilon>0\), one may:

1. choose explicit \(\delta\) so that
   \[
   E_{\rm form}<\varepsilon/2;
   \]
2. then choose
   \[
   \mu
   \ge
   \frac{
   2M_a(u_{a,p,\delta})
   M_a(u_{a,q,\delta})
   }{\varepsilon}
   -1.
   \]

Therefore the sharp deficiency/evaluation matrix elements admit an effective
fixed-\(a\) first-correction approximation.

## 10. What remains for the large-\(a\) proof lane

The following gates are now closed:

### LIV-MD2c4b1
Effective operator-domain resolvent rate:
**CLOSED**.

### LIV-MD2c4b2
Explicit sharp-to-smooth form-norm rate:
**CLOSED**.

### LIV-MD2c4b2R
Effective fixed-\(a\) sharp-vector resolvent first-correction rate:
**CLOSED**.

The remaining quantitative task is now only the large-\(a\) assembly:

### LIV-MD2c4b3 — OPEN
Choose explicit

\[
\delta(a)\to0,
\qquad
\mu(a)\to\infty
\]

so that:
- the displayed sharp-to-smooth error vanishes;
- the displayed resolvent error vanishes;
- the finite normalized cross-convolution Weil scalar approaches its
  zero-free prime target uniformly on the selected compact \(z\)-set.

The last bullet is the only part not yet equipped with a complete explicit
large-\(a\) rate in this lane.

## 11. Schur numerator firewall

This theorem controls the deficiency/evaluation vectors at the form/resolvent
level.

It does **not** by itself solve the analytic-continuation issue for the
\(e^{-x}\) numerator channel of the limiting Schur quotient. The formal target
is fixed by the functional equation, but a direct absolutely convergent
prime-side representation for that channel is still absent.

Therefore full Schur/characteristic compatibility remains a separate gate.

## 12. Compact theorem

For every fixed \(a>0\), real \(p\), and
\(0<\delta\le e^{-1}\),

\[
\boxed{
\|e^{pau}-e^{pau}\eta_\delta(u)\|_{T_a}^2
\le
\mathcal E_T(a,p,\delta)
}
\]

with the explicit \(\mathcal E_T\) above, and

\[
\boxed{
\mathcal E_T(a,p,\delta)
=
O_{a,p}
\left(
\delta\log(1/\delta)
\right).
}
\]

Combined with the exact operator-domain resolvent rate, this yields a
computable fixed-\(a\) approximation schedule for the sharp Livšic scalar
matrix elements.

The large-\(a\) joint rate and full numerator-channel Schur compatibility
remain open.
