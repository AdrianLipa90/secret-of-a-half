# SOH Explicit Large-a Finite-Cross Weil Error and Effective Denominator Schedule v0.1

Status: **EXPLICIT_LARGE-a_RATE / EFFECTIVE_DENOMINATOR_CHANNEL_CLOSED / FULL_SCHUR_NUMERATOR_OPEN**

Date: 2026-09-26

Parents:
- \`research/SOH_PIECEWISE_EXPONENTIAL_WEIL_CROSS_CONVOLUTION_V0_1.md\`
- \`research/SOH_EXPLICIT_SHARP_TO_SMOOTH_WEIL_FORM_RATE_V0_1.md\`
- \`research/SOH_QUANTITATIVE_OPERATOR_DOMAIN_RESOLVENT_RATE_V0_1.md\`
- \`research/SOH_LIVSIC_CAYLEY_LOG_DERIVATIVE_PRIME_BRIDGE_V0_1.md\`

No RH and no zero list are used.

## 1. Finite normalized cross weight

For

\[
a>0,
\qquad
y>\frac12,
\]

put

\[
c=y+1,
\qquad
d=e^{-2ca},
\qquad
D=1-d.
\]

The normalized finite cross-convolution already proved in the repository is

\[
f_{a,y}(t)
=
\begin{cases}
0,&|t|>2a,\\[1mm]
e^{-t}\dfrac{1-e^{-c(2a-t)}}{D},
&0\le t\le2a,\\[3mm]
e^{yt}\dfrac{1-e^{-c(2a+t)}}{D},
&-2a\le t\le0.
\end{cases}
\]

Its infinite target is

\[
F_{1,y}(t)
=
\begin{cases}
e^{-t},&t\ge0,\\
e^{yt},&t\le0.
\end{cases}
\]

Define the one-sided nonnegative defects for \(x\ge0\),

\[
g_+(x)
=
F_{1,y}(x)-f_{a,y}(x),
\]

\[
g_-(x)
=
F_{1,y}(-x)-f_{a,y}(-x).
\]

For \(0\le x\le2a\),

\[
\boxed{
g_+(x)
=
e^{-x}
\frac{
d(e^{cx}-1)
}{D},
}
\]

\[
\boxed{
g_-(x)
=
e^{-yx}
\frac{
d(e^{cx}-1)
}{D}.
}
\]

For \(x>2a\),

\[
g_+(x)=e^{-x},
\qquad
g_-(x)=e^{-yx}.
\]

## 2. Elementary-term error

The elementary part of Suzuki's Weil functional is bounded by

\[
E_{\rm el}(a,y)
=
\int_0^\infty
[g_+(x)+g_-(x)]
(e^{x/2}+e^{-x/2})\,dx.
\]

Define

\[
\Phi(k,a)
=
\begin{cases}
\dfrac{e^{2ak}-1}{k},&k\ne0,\\
2a,&k=0.
\end{cases}
\]

Using

\[
e^{cx}-1\le e^{cx}
\]

on the finite interval gives

\[
\boxed{
\begin{aligned}
E_{\rm el}(a,y)
\le{}&
\frac dD
\Big[
\Phi(y+1/2,a)
+
\Phi(y-1/2,a)
\\
&\qquad\qquad
+
\Phi(3/2,a)
+
\Phi(1/2,a)
\Big]
\\
&+
2e^{-a}
+\frac23e^{-3a}
\\
&+
\frac{
e^{-2a(y-1/2)}
}{
y-1/2
}
+
\frac{
e^{-2a(y+1/2)}
}{
y+1/2
}.
\end{aligned}
}
\]

## 3. Prime-term error

The prime contribution to the difference satisfies

\[
E_{\rm p}(a,y)
\le
\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}
\left[
g_+(\log n)+g_-(\log n)
\right].
\]

For

\[
n\le e^{2a},
\]

we use

\[
g_+(\log n)
\le
\frac dD n^y,
\]

\[
g_-(\log n)
\le
\frac dD n.
\]

With

\[
\Lambda(n)\le2a
\]

on this finite range,

\[
\boxed{
E_{\rm p}^{\rm in}(a,y)
\le
\frac{2a}{D}
\left[
e^{-a}
+
e^{-a(2y-1)}
\right].
}
\]

For the omitted tail \(n>e^{2a}\),

\[
\boxed{
E_{\rm p}^{\rm out}(a,y)
\le
(4a+4)e^{-a}
+
e^{-2a(y-1/2)}
\left[
\frac{2a}{y-1/2}
+
\frac1{(y-1/2)^2}
\right].
}
\]

Therefore

\[
\boxed{
E_{\rm p}
\le
E_{\rm p}^{\rm in}
+
E_{\rm p}^{\rm out}.
}
\]

## 4. Regularization-term error

The regularization kernel is

\[
k(x)
=
\frac{e^{x/2}}{e^x-e^{-x}}
=
\frac{e^{-x/2}}{1-e^{-2x}}.
\]

For \(0<x\le2a\),

\[
e^{cx}-1
\le
cx e^{cx},
\]

and the elementary inequality

\[
\frac{x}{1-e^{-2x}}
\le
\frac{1+2x}{2}
\]

gives

\[
\boxed{
E_{\rm reg}^{\rm in}(a,y)
\le
\frac{
dc(1+4a)
}{
2D
}
\left[
\Phi(y-1/2,a)
+
\Phi(1/2,a)
\right].
}
\]

For \(a\ge1/2\) and \(x>2a\ge1\),

\[
k(x)
\le
\frac{
e^{-x/2}
}{
1-e^{-2}
}.
\]

Hence

\[
\boxed{
E_{\rm reg}^{\rm out}(a,y)
\le
\frac1{1-e^{-2}}
\left[
\frac23e^{-3a}
+
\frac{
e^{-2a(y+1/2)}
}{
y+1/2
}
\right].
}
\]

Therefore

\[
\boxed{
E_{\rm reg}
\le
E_{\rm reg}^{\rm in}
+
E_{\rm reg}^{\rm out}.
}
\]

The constant term of the Weil functional cancels exactly because

\[
f_{a,y}(0)=F_{1,y}(0)=1.
\]

## 5. Explicit full Weil-functional error

Define

\[
\boxed{
E_W(a,y)
=
E_{\rm el}(a,y)
+
E_{\rm p}(a,y)
+
E_{\rm reg}(a,y).
}
\]

Then

\[
\boxed{
\left|
W(f_{a,y})
-
W(F_{1,y})
\right|
\le
E_W(a,y).
}
\]

Since

\[
W(F_{1,y})
=
r_0+
r(1/2+y),
\]

where

\[
r(s)=\xi'(s)/\xi(s),
\]

we obtain

\[
\boxed{
\left|
W(f_{a,y})
-
r_0
-
r(1/2+y)
\right|
\le
E_W(a,y).
}
\]

All terms on the right are elementary.

## 6. Uniform zero-free interval \(1\le y\le2\)

For the Vitali endgame it is enough to use any zero-free set with an interior
accumulation point. Fix

\[
\boxed{
1\le y\le2.
}
\]

Then

\[
D
\ge
D_a:=1-e^{-4a}.
\]

The preceding bounds simplify to

\[
\boxed{
E_{\rm el}(a,y)
\le
\left(
4+\frac{4}{3D_a}
\right)e^{-a}
+
\left(
\frac43+\frac4{D_a}
\right)e^{-3a}.
}
\]

Also

\[
\boxed{
E_{\rm p}(a,y)
\le
\left[
\frac{4a}{D_a}
+
8(a+1)
\right]e^{-a}.
}
\]

Finally,

\[
\boxed{
E_{\rm reg}(a,y)
\le
\left[
\frac{
6(1+4a)
}{
D_a
}
+
\frac{
4
}{
3(1-e^{-2})
}
\right]
e^{-3a}.
}
\]

Define the uniform envelope

\[
\boxed{
E_W^\ast(a)
}
\]

as the sum of these three displayed right-hand sides.

Then for every \(a\ge1\),

\[
\boxed{
\sup_{1\le y\le2}
\left|
W(f_{a,y})
-
r_0
-
r(1/2+y)
\right|
\le
E_W^\ast(a).
}
\]

Moreover,

\[
\boxed{
E_W^\ast(a)
=
O(ae^{-a}).
}
\]

This is an explicit uniform large-\(a\) rate.

## 7. Effective sharp resolvent schedule on the same interval

Let

\[
h_{a,y}(u)=e^{ayu},
\qquad
h_{a,1}(u)=e^{au}
\]

in source-scaled coordinates.

The preceding sharp-to-smooth theorem gives an explicit form error

\[
\epsilon_T(a,p,\delta)
=
\sqrt{
\mathcal E_T(a,p,\delta)
}.
\]

For \(1\le p\le2\),

\[
\epsilon_T(a,p,\delta)
\le
\epsilon_T^\ast(a,\delta)
:=
\sqrt{
\mathcal E_T(a,2,\delta)
},
\]

because the displayed majorant increases with the envelope parameters
\(B=e^{|p|a}\) and \(q=|p|a\).

Let

\[
H_a(p)
=
\|h_{a,p}\|_{T_a}.
\]

This is a finite zero-list-free arithmetic quantity:

\[
H_a(p)^2
=
Q_W^{a,\rm sc}(h_{a,p})
-
\lambda_{\rm sh}(a)
\|h_{a,p}\|_2^2,
\]

and \(Q_W^{a,\rm sc}(h_{a,p})\) is evaluated by the finite explicit Weil
functional with prime support \(n\le e^{2a}\).

Define

\[
H_a^\ast
=
\max_{1\le p\le2}H_a(p).
\]

It is enough, and computationally simpler, to replace this maximum by any
rigorous interval upper enclosure.

For the smoothed vectors

\[
u_{a,p,\delta}
=
h_{a,p}\eta_\delta,
\]

the form contraction theorem gives a sharp-to-smooth error bounded by

\[
\boxed{
E_{\rm repl}(a,\delta)
\le
4\epsilon_T^\ast(a,\delta)
\left[
H_a^\ast+\epsilon_T^\ast(a,\delta)
\right].
}
\]

## 8. Constructive choice of \(\delta_a\)

For integer

\[
a=n\ge1,
\]

define \(m_n\) to be the first integer \(m\ge1\) such that, with

\[
\delta=e^{-m},
\]

\[
\boxed{
E_{\rm repl}(n,e^{-m})
\le
e^{-n}.
}
\]

Set

\[
\boxed{
\delta_n=e^{-m_n}.
}
\]

Existence follows from the explicit

\[
\delta\log(1/\delta)
\]

form rate.

Every quantity tested in this finite search is zero-list-free and explicitly
computable.

Thus \(\delta_n\) is a constructive schedule, not a non-effective diagonal
choice.

## 9. Constructive choice of \(\mu_n\)

For the endpoint-zero approximants, define the explicit operator bounds

\[
M_n(p)
=
M_n(u_{n,p,\delta_n})
\]

from the quantitative operator-domain theorem, and let

\[
M_n^\ast
=
\max_{1\le p\le2}M_n(p).
\]

Again, a rigorous interval upper enclosure is sufficient.

Choose

\[
\boxed{
\mu_n
=
e^n(M_n^\ast)^2+1.
}
\]

Then the operator-domain first-correction error obeys

\[
\boxed{
\frac{
M_n(p)M_n(1)
}{
\mu_n+1
}
\le
e^{-n}
}
\]

uniformly for

\[
1\le p\le2.
\]

Combining Sections 8 and 9 gives an explicit sharp-vector resolvent error

\[
\boxed{
E_{\rm res}^\ast(n)
\le
2e^{-n}.
}
\]

## 10. Effective denominator-channel theorem

Let

\[
\mathcal D_n(y)
\]

denote the renormalized negative-shift first-correction scalar built from the
sharp pair

\[
e^{nyu},
\qquad
e^{nu},
\]

with:
- \(a=n\);
- cutoff schedule \(\delta_n\);
- negative-shift resolvent parameter \(\mu_n\);
- the explicit recovery of the \(\lambda_{\rm sh}(n)\) form term.

Then

\[
\boxed{
\sup_{1\le y\le2}
\left|
\mathcal D_n(y)
-
r_0
-
r(1/2+y)
\right|
\le
2e^{-n}
+
E_W^\ast(n).
}
\]

Therefore

\[
\boxed{
\mathcal D_n(y)
\longrightarrow
r_0+
\frac{\xi'(1/2+y)}{\xi(1/2+y)}
}
\]

uniformly for

\[
1\le y\le2.
\]

This is a fully effective zero-list-free convergence theorem for the
**denominator deficiency channel**.

## 11. Why this is enough analytically, but not yet enough for RH

The interval

\[
1\le y\le2
\]

lies wholly in the absolutely convergent region

\[
s=1/2+y>1
\]

and has interior accumulation points.

Therefore, if the corresponding **numerator** deficiency channel is put under
the same effective control and the ratio is shown to be the finite Schur
quotient, the existing Montel/Vitali argument is already sufficient to extend
the identity through the upper half-plane and force the RH conclusion.

The denominator channel no longer carries an asymptotic or effectiveness gap.

## 12. True remaining Schur gate

The unresolved second channel uses

\[
e^{-x}
\]

rather than

\[
e^{x}.
\]

Its formal infinite target is fixed by the functional equation:

\[
\frac{\xi'(-1/2)}{\xi(-1/2)}
=
-
\frac{\xi'(3/2)}{\xi(3/2)}
=
-r_0.
\]

Accordingly the desired numerator combination is proportional to

\[
r(s)-r_0.
\]

However the naive piecewise-exponential Weil test corresponding directly to
that channel lies outside the absolutely convergent half-plane for the prime
series.

Therefore the following remains open:

### LIV-MD2c5N — numerator finite-part / boundary-triple transport

Construct a zero-list-free, source-compatible renormalization or boundary
identity that yields the finite-\(a\) numerator channel and converges to

\[
r(s)-r_0
\]

without importing zeta zeros or RH.

This is now the unique structural obstruction in the Livšic Schur lane.

## 13. Updated gate status

- LIV-MD2c4b1 effective operator-domain rate: **CLOSED**.
- LIV-MD2c4b2 explicit sharp-to-smooth rate: **CLOSED**.
- LIV-MD2c4b3 explicit large-\(a\) cross-Weil rate: **CLOSED**.
- LIV-MD2c4E effective denominator schedule: **CLOSED**.
- LIV-MD2c5N numerator finite-part/boundary transport: **OPEN**.
- RH: **OPEN**.

## 14. Compact theorem

There is an explicit zero-list-free sequence

\[
a_n=n,
\qquad
\delta_n>0,
\qquad
\mu_n>0
\]

constructed from the displayed finite arithmetic/form bounds such that the
renormalized negative-shift denominator scalar satisfies

\[
\boxed{
\sup_{1\le y\le2}
\left|
\mathcal D_n(y)
-
\frac{\xi'(3/2)}{\xi(3/2)}
-
\frac{\xi'(1/2+y)}{\xi(1/2+y)}
\right|
\le
2e^{-n}+E_W^\ast(n)
\to0.
}
\]

No RH and no zeta-zero table are used.

The remaining Livšic proof gate is the second deficiency/numerator channel.
