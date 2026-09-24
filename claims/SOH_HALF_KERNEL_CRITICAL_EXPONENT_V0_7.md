# SOH Half-Kernel Critical Exponent and Second-Stieltjes Firewall v0.7

Status: `EXACT_CRITICAL_EXPONENT_ALPHA_MAX_2 / CORRECTED_SECOND_STIELTJES_FIREWALL / HIGHER_STIELTJES_OPEN / GLOBAL_SQRT_KERNEL_PF3_OPEN / RH_OPEN`

Date: 2026-09-14

This note extends `SOH_HALF_KERNEL_SQRT_ULC_V0_6.md` without promoting any
higher Stieltjes sign, global `PF3` claim, real-rootedness claim, or RH claim.

Let
\[
L(y)=-\log\Phi(y),\qquad y\ge0,
\]
for the exact even Riemann kernel used throughout SOH.  From v0.6 we already
have
\[
L'''(y)>0\qquad(y>0)
\]
and therefore
\[
yL''(y)-L'(y)>0\qquad(y>0).
\]
The same outward interval engine used in v0.6 gives, at the origin,
\[
\boxed{
18.72690492950325
<
L''(0)
<
18.72690492950340.
}
\]
Hence \(L''(0)>0\).  Since \(L''\) is strictly increasing on \((0,\infty)\),
we also have \(L''(y)>0\) and \(L'(y)>0\) for \(y>0\).

## 1. Exact critical exponent

For \(\alpha>0\), define
\[
H_\alpha(x)=\Phi\!\left(x^{1/\alpha}\right),\qquad x>0,
\]
and put \(y=x^{1/\alpha}\), so \(x=y^\alpha\).  Direct differentiation gives
\[
\boxed{
\frac{d^2}{dx^2}\log H_\alpha(x)
=
-\frac{
yL''(y)-(\alpha-1)L'(y)
}{
\alpha^2 y^{2\alpha-1}
}.
}
\]

For \(0<\alpha\le2\),
\[
yL''-(\alpha-1)L'
=
\underbrace{(yL''-L')}_{>0}
+
\underbrace{(2-\alpha)L'}_{\ge0},
\]
so
\[
\frac{d^2}{dx^2}\log H_\alpha(x)<0
\qquad(x>0).
\]
Thus every \(H_\alpha\) with \(0<\alpha\le2\) is strictly log-concave on
\((0,\infty)\).

For \(\alpha>2\), evenness of \(L\) gives
\[
L'(y)=L''(0)y+O(y^3),
\qquad
L''(y)=L''(0)+O(y^2).
\]
Therefore
\[
yL''(y)-(\alpha-1)L'(y)
=
(2-\alpha)L''(0)y+O(y^3).
\]
Because \(L''(0)>0\) and \(2-\alpha<0\), the numerator is negative for all
sufficiently small \(y>0\).  Hence
\[
\frac{d^2}{dx^2}\log H_\alpha(x)>0
\]
near the origin, so \(H_\alpha\) is not globally log-concave.

Therefore
\[
\boxed{\alpha_{\max}=2.}
\]

Equivalently, the square-root reparametrization
\[
\boxed{y=\sqrt{x}}
\]
is the unique boundary member of the power family \(y=x^{1/\alpha}\) for
which global log-concavity survives.  In root-exponent language the sharp
boundary is exactly
\[
\boxed{\frac12.}
\]

## 2. Corrected second-Stieltjes identity

Let
\[
F(u)>0,\qquad
R(u)=\frac{F'(u)}{F(u)}.
\]
The exact second derivative is
\[
\boxed{
R''(u)
=
\frac{
F(u)^2F'''(u)-3F(u)F'(u)F''(u)+2F'(u)^3
}{
F(u)^3
}.
}
\]

The previously considered determinant
\[
F'(u)^3F'''(u)-F(u)F''(u)^3\ge0
\]
is **not equivalent** to \(R''\ge0\).  It is a stronger derivative-ratio
log-convexity condition and must not be substituted for the actual second
Stieltjes target.

Define
\[
A_j=\frac{F^{(j+1)}}{F^{(j)}},
\qquad
q_j=\frac{A_{j+1}}{A_j}.
\]
Then
\[
\boxed{
\frac{R''}{R}
=
A_0^2\left(2-3q_0+q_0^2q_1\right).
}
\]

If \(q_0,q_1<1\), define the reciprocal deficits
\[
E_j=\frac1{1-q_j}.
\]
A direct algebraic reduction gives
\[
2-3q_0+q_0^2q_1
=
\frac{
(E_0+1)E_1-(E_0-1)^2
}{
E_0^2E_1
}.
\]
Therefore, under \(q_0,q_1<1\),
\[
\boxed{
R''\ge0
\iff
(E_0+1)E_1\ge(E_0-1)^2.
}
\]

This preserves the reciprocal-deficit bridge while correcting the earlier
false equivalence.

## 3. Proof boundary

Closed at the declared repository-certificate level:

- exact power-family differentiation;
- outward interval certificate \(L''(0)>18\);
- exact sharp threshold \(\alpha_{\max}=2\);
- exact critical root exponent \(1/2\);
- exact corrected identity for \(R''\);
- exact derivative-ratio normal form;
- exact reciprocal-deficit equivalence.

Open:

- \(R''(u)\ge0\) globally for the SOH \(F\);
- all higher Stieltjes derivative signs;
- global `PF3` of \(h(x)=\Phi(\sqrt{x})\);
- full Herglotz property of \(-G'/G\);
- SOH-G003 real-rootedness;
- RH.

No higher claim is promoted by this note.
