# SOH-G017 — Fixed-Root Exclusion from Quantitative Kernel Curvature

## Status

**THEOREM-LEVEL ANALYTIC EXCLUSION / PROVED.**

This note removes the final possible fixed exceptional root left by G015–G016. It proves

\[
\boxed{F(-1/4)>0}
\]

without using a zero table, RH, or numerical root exclusion.

Attribution boundary: Gershon (2026) independently proved strict log-concavity of the classical Xi kernel `Phi`. The quantitative curvature constants used below are the explicit SOH-G004 channel/mixture bounds already retained in the monograph. No priority claim is made for strict log-concavity itself.

## 1. Modular evenness of the Xi kernel

Let

\[
\Theta(x)=\sum_{n\in\mathbb Z}e^{-\pi n^2x},\qquad x>0.
\]

Jacobi modularity gives

\[
\Theta(x)=x^{-1/2}\Theta(1/x).
\]

With `x=e^{2y}`, the SOH kernel can be written

\[
\Phi(y)=4x^{9/4}\Theta''(x)+6x^{5/4}\Theta'(x).
\]

Differentiate the modular identity. Writing `t=1/x`, one obtains

\[
\Theta'(t)
=-x^{5/2}\Theta'(x)-\frac12x^{3/2}\Theta(x),
\]

and

\[
\Theta''(t)
=x^{9/2}\Theta''(x)
+3x^{7/2}\Theta'(x)
+\frac34x^{5/2}\Theta(x).
\]

Substitution into the kernel expression at `t=1/x` gives exact cancellation of the `Theta(x)` terms and

\[
4t^{9/4}\Theta''(t)+6t^{5/4}\Theta'(t)
=4x^{9/4}\Theta''(x)+6x^{5/4}\Theta'(x).
\]

Therefore

\[
\boxed{\Phi(-y)=\Phi(y)}
\]

and in particular

\[
\boxed{\Phi'(0)=0.}
\]

## 2. Quantitative strong log-concavity from G004

G004 established for every theta channel

\[
g_n''<-12
\]

and the exact mixture identity

\[
(\log\Phi)''
=\sum_n p_ng_n''+\operatorname{Var}_p(g_n').
\]

Its conservative rational estimate proves

\[
\operatorname{Var}_p(g_n')<2.
\]

Hence

\[
\boxed{(\log\Phi)''<-10.}
\]

Set

\[
V(y)=-\log\Phi(y).
\]

Then

\[
V''(y)>10.
\]

From modular evenness, `V'(0)=0`, so for every `y>0`,

\[
\boxed{V'(y)>10y.}
\]

## 3. Second-moment bound

Define

\[
m_0=\int_0^\infty\Phi(y)\,dy,
\qquad
m_2=\int_0^\infty y^2\Phi(y)\,dy.
\]

Because the explicit Riemann kernel decays super-exponentially, the boundary term `y Phi(y)` vanishes at infinity. Using `V' Phi=-Phi'`,

\[
10m_2
<\int_0^\infty yV'(y)\Phi(y)\,dy
=-\int_0^\infty y\Phi'(y)\,dy
=m_0.
\]

Thus

\[
\boxed{m_2<\frac{m_0}{10}.}
\]

## 4. Exclusion of the negative fixed quotient value

For `w=-1/4`, choose `z=i/2`. The positive-kernel representation gives

\[
F(-1/4)
=\xi\!\left(\frac12+\frac{i}{2}\right)
=\int_0^\infty\Phi(y)\cos(y/2)\,dy.
\]

The elementary global inequality

\[
\cos x\ge1-\frac{x^2}{2}
\]

gives

\[
\cos(y/2)\ge1-\frac{y^2}{8}.
\]

Therefore

\[
F(-1/4)
\ge m_0-\frac{m_2}{8}
>m_0\left(1-\frac1{80}\right).
\]

Since `m0=F(0)=xi(1/2)>0`,

\[
\boxed{
F(-1/4)>\frac{79}{80}F(0)>0.
}
\]

Hence

\[
\boxed{F(-1/4)\ne0.}
\]

## 5. Orbit consequences

G015 showed that the quotient involution

\[
J(w)=\frac1{16w}
\]

has fixed values `w=+/-1/4`, with `+1/4` already excluded by coefficient positivity. G017 now excludes `-1/4` as well.

Therefore the finite paired-root set `P_J` has no fixed points and is a disjoint union of non-fixed two-cycles. Consequently

\[
\boxed{|P_J|\equiv0\pmod2.}
\]

G016 proved

\[
|P_N|=2|P_J|,
\]

so

\[
\boxed{|P_N|\equiv0\pmod4.}
\]

The G012 geometric fixed pair

\[
\left\{\frac12+\frac i2,\frac12-\frac i2\right\}
\]

is therefore not a pair of xi zeros.

## 6. Proof firewall

Proved here:

- modular evenness `Phi(-y)=Phi(y)` and `Phi'(0)=0`;
- the quantitative consequence `(log Phi)''<-10` from the existing G004 bounds;
- `m2<m0/10`;
- `F(-1/4)>(79/80)F(0)>0`;
- no fixed points occur in `P_J`;
- `|P_J|` is even;
- `|P_N|` is divisible by four;
- the G012 fixed pair `1/2 +/- i/2` is not in the xi zero set.

Not proved or claimed here:

- that `P_J` or `P_N` is empty;
- that non-fixed paired two-cycles do not exist;
- real-rootedness of `F`;
- PF-infinity;
- SOH-G003;
- RH.
