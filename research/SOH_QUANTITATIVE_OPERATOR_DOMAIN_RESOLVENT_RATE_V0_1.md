# SOH Quantitative Operator-Domain Resolvent First-Correction Bound v0.1

Status: **EXACT_OPERATOR_DOMAIN_RATE / EXPLICIT_SCREW_ENVELOPE / SHARP-TO-SMOOTH_JOIN_OPEN**

Date: 2026-09-26

Parents:
- \`research/SOH_SUZUKI_LOCALIZED_OPERATOR_JOIN_V0_1.md\`
- \`research/SOH_EXPLICIT_GLOBAL_LIVSIC_SHIFT_V0_1.md\`
- \`research/SOH_NEGATIVE_SHIFT_RESOLVENT_WEIL_FIRST_CORRECTION_V0_1.md\`
- \`src/secret_of_a_half/c005_screw_analytic_bounds.py\`

Primary source:
- Suzuki's localized operator identity
  \[
  B_a=D^*G_aD,\qquad \mathfrak D(B_a)=H_0^1(-a,a),
  \]
  with \(A_a\) the Friedrichs extension of \(B_a\).

No RH is used.

## 1. Localized derivative-convolution bound

Let

\[
v\in H_0^1(-a,a).
\]

Since \(v(\pm a)=0\),

\[
\int_{-a}^{a}v'(u)\,du=0,
\]

so

\[
Dv=i v'
\]

already belongs to the zero-mean subspace used by the localized projection.

For

\[
G_a=P_aGP_a
\]

the derivative of the projection's constant subtraction vanishes. Therefore,
on the source core and then by closure,

\[
B_av
=
D^*G_aDv
\]

has the same \(L^2\) norm as the derivative of the convolution

\[
g*(Dv).
\]

Only differences \(x-u\in[-2a,2a]\) occur. Extending \(Dv\) by zero outside
\([-a,a]\), Young's convolution inequality gives

\[
\|B_av\|_{L^2(-a,a)}
\le
\|g'\|_{L^2(-2a,2a)}
\|v'\|_{L^1(-a,a)}.
\]

Because \(g\) is even,

\[
\|g'\|_{L^2(-2a,2a)}^2
=
2\int_0^{2a}|g'(t)|^2\,dt.
\]

Hence

\[
\boxed{
\|A_av\|_2
=
\|B_av\|_2
\le
\sqrt{
2G_1(a)
}
\,
\|v'\|_1,
}
\]

where

\[
G_1(a)
=
\int_0^{2a}|g'(t)|^2\,dt.
\]

The equality \(A_av=B_av\) holds because \(B_a\subset A_a\).

## 2. Repository-explicit envelope

The existing unconditional screw envelope supplies a computable number

\[
G_{1,\rm up}(a)
\ge
\int_0^{2a}|g'(t)|^2\,dt.
\]

Therefore

\[
\boxed{
\|A_av\|_2
\le
\sqrt{2G_{1,\rm up}(a)}
\,
\|v'\|_1.
}
\]

This uses only the source screw function and elementary prime/Lerch majorants.

## 3. Shifted positive operator

Let

\[
\lambda_{\rm sh}(a)
=
L_{\rm elem}(a)-1
\]

be the explicit unconditional Livšic schedule already proved in the
repository.

Then

\[
T_a
=
A_a-\lambda_{\rm sh}(a)I
\ge I.
\]

For \(v\in H_0^1(-a,a)\),

\[
\boxed{
\|T_av\|_2
\le
\sqrt{2G_{1,\rm up}(a)}
\,
\|v'\|_1
+
|\lambda_{\rm sh}(a)|\,\|v\|_2.
}
\]

Define this explicit right side by

\[
M_a(v).
\]

## 4. Quantitative first-correction identity

Let \(T=T^*\ge I\), \(f,g\in\mathfrak D(T)\), and \(\mu>0\).

Put

\[
R_\mu=(T+\mu I)^{-1}.
\]

Define

\[
\mathcal F_\mu(f,g)
=
-\mu^2
\left[
\langle f,R_\mu g\rangle
-
\frac{\langle f,g\rangle}{\mu}
\right].
\]

Functional calculus gives

\[
\mathcal F_\mu(f,g)
=
\langle f,\mu T(T+\mu I)^{-1}g\rangle.
\]

Therefore

\[
\mathcal F_\mu(f,g)-\langle f,Tg\rangle
=
-
\langle
Tf,
(T+\mu I)^{-1}
Tg
\rangle.
\]

Since

\[
\|(T+\mu I)^{-1}\|
\le
\frac1{\mu+1},
\]

we obtain the exact rate

\[
\boxed{
\left|
\mathcal F_\mu(f,g)-\langle f,Tg\rangle
\right|
\le
\frac{
\|Tf\|_2\|Tg\|_2
}{
\mu+1
}.
}
\]

## 5. Fully explicit localized certificate

For

\[
f,g\in H_0^1(-a,a),
\]

the preceding sections give

\[
\boxed{
\left|
\mathcal F_{a,\mu}(f,g)
-
\left[
Q_W^a(f,g)
-
\lambda_{\rm sh}(a)\langle f,g\rangle
\right]
\right|
\le
\frac{
M_a(f)M_a(g)
}{
\mu+1
}.
}
\]

Hence any desired scalar tolerance \(\varepsilon>0\) is guaranteed by

\[
\boxed{
\mu
\ge
\frac{M_a(f)M_a(g)}{\varepsilon}-1.
}
\]

This is a genuinely computable negative-shift schedule at fixed \(a\) for
operator-domain test vectors.

## 6. Explicit endpoint-zero exponential approximants

Let \(0<\delta<a\) and define the piecewise-linear cutoff

\[
\eta_{a,\delta}(x)
=
\begin{cases}
1,&|x|\le a-\delta,\\
(a-|x|)/\delta,&a-\delta<|x|<a,\\
0,&|x|\ge a.
\end{cases}
\]

For real \(p\), define

\[
u_{p,a,\delta}(x)
=
e^{px}\eta_{a,\delta}(x).
\]

Then

\[
u_{p,a,\delta}\in H_0^1(-a,a)
\subset\mathfrak D(A_a).
\]

The derivative obeys

\[
|u'|
\le
|p|e^{px}\eta
+
e^{px}|\eta'|.
\]

Therefore

\[
\boxed{
\|u'_{p,a,\delta}\|_1
\le
|p|
\int_{-a}^{a}e^{px}\,dx
+
\frac1\delta
\left[
\int_{a-\delta}^{a}e^{px}\,dx
+
\int_{-a}^{-a+\delta}e^{px}\,dx
\right].
}
\]

The \(L^2\) norm satisfies the simple upper bound

\[
\boxed{
\|u_{p,a,\delta}\|_2
\le
\left(
\int_{-a}^{a}e^{2px}\,dx
\right)^{1/2}.
}
\]

Thus \(M_a(u_{p,a,\delta})\) is elementary and explicit.

## 7. What this closes

The previous diagonal theorem left an effective-rate problem for the
resolvent first correction.

For endpoint-zero test vectors, that rate is now closed:

\[
\boxed{
\text{operator-domain test}
+
\text{explicit screw }G_1
\Longrightarrow
\text{explicit }\mu(a,\varepsilon).
}
\]

No spectral truncation and no zeta-zero list is needed.

## 8. Remaining sharp-vector join

The actual Livšic deficiency/evaluation vectors use sharp exponentials

\[
e^{-izx}\mathbf1_{[-a,a]},
\]

which belong to the closed form domain but not to \(H_0^1(-a,a)\).

The remaining effective step is therefore no longer an abstract resolvent
rate. It is the concrete approximation problem:

\[
\boxed{
u_{p,a,\delta}
\to
e^{px}\mathbf1_{[-a,a]}
}
\]

in the localized Weil form norm, with an explicit error bound that can be
balanced against the explicit \(1/(\mu+1)\) resolvent error above.

Suzuki's form-core proof gives qualitative convergence. The next task is to
extract a quantitative \(\delta\)-rate in the repository normalization.

## 9. Updated gate split

### LIV-MD2c4b1 — effective operator-domain resolvent rate
Status: **CLOSED**.

### LIV-MD2c4b2 — explicit sharp-to-smooth form-norm rate
Status: **OPEN**.

### LIV-MD2c4b3 — combine \(\delta(a)\) and \(\mu(a)\) with the prime-side
large-\(a\) tail
Status: **OPEN**, but now purely quantitative.

## 10. Compact theorem

For every \(a>0\), every \(f,g\in H_0^1(-a,a)\), and every \(\mu>0\),

\[
\boxed{
\left|
-\mu^2
\left[
\langle f,(T_a+\mu I)^{-1}g\rangle
-
\frac{\langle f,g\rangle}{\mu}
\right]
-
\langle f,T_ag\rangle
\right|
\le
\frac{
M_a(f)M_a(g)
}{
\mu+1
},
}
\]

where \(T_a=A_a-\lambda_{\rm sh}(a)I\ge I\) and

\[
M_a(v)
=
\sqrt{2G_{1,\rm up}(a)}\,\|v'\|_1
+
|\lambda_{\rm sh}(a)|\,\|v\|_2.
\]

All quantities on the right are zero-list-free and explicitly computable.
