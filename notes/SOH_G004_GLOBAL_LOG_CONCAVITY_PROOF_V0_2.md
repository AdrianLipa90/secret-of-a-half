# SOH-G004 — Global log-concavity of the compactified Riemann kernel

Status: **PROVED THEOREM (kernel-weight level only); this does not prove SOH-G003 real-rootedness or RH.**

Let

\[
\Phi(y)=\sum_{n\ge1}\phi_n(y),\qquad
\phi_n(y)=4a_n e^{5y/2}(2r_n-3)e^{-r_n},
\]
with

\[
a_n=\pi n^2,\qquad r_n=a_n e^{2y},\qquad y\ge0.
\]

Let

\[
\eta=\tanh y,\qquad
W(\eta)=\frac{\Phi(y)}{1-\eta^2},\qquad 0\le\eta<1.
\]

We prove

\[
\boxed{\frac{d^2}{d\eta^2}\log W(\eta)<0\quad(0\le\eta<1).}
\]

## 1. Channel formulas

Set \(g_n=\log\phi_n\). Then

\[
g_n'(y)=\frac52+\frac{4r_n}{2r_n-3}-2r_n,
\]

\[
g_n''(y)=-4r_n-\frac{24r_n}{(2r_n-3)^2}.
\]

Since \(r_n\ge\pi>3\), the function

\[
h(r)=\frac{4r}{2r-3}
\]

is decreasing on \([3,\infty)\) and satisfies \(2<h(r)\le4\). Therefore

\[
g_n'(y)\le \frac52+4-2r_n\le\frac12,
\]

and

\[
g_n''(y)< -4r_n\le -12.
\]

Writing \(\tau=\tanh y\in[0,1)\), define the compactified channel curvature contribution

\[
A_n(y):=g_n''(y)+2\tau g_n'(y)+2(1+\tau^2).
\]

Using the previous bounds,

\[
A_n(y)< -12+1+4=-7.
\]

Hence

\[
\boxed{A_n(y)<-7\quad\text{for every }n\ge1,\ y\ge0.}
\]

## 2. Mixture identity

Let

\[
p_n(y)=\frac{\phi_n(y)}{\Phi(y)}.
\]

Then

\[
(\log\Phi)''=\sum_n p_n g_n''+\operatorname{Var}_p(g_n'),
\]

and

\[
(\log\Phi)'=\sum_n p_n g_n'.
\]

Therefore

\[
\mathcal M(y):=(\log\Phi)''+2\tau(\log\Phi)'+2(1+\tau^2)
=\sum_n p_n A_n+\operatorname{Var}_p(g_n').
\]

Since every \(A_n<-7\),

\[
\mathcal M(y)<-7+\operatorname{Var}_p(g_n').
\]

Thus it remains only to prove a uniform bound \(\operatorname{Var}_p(g_n')<2\).

## 3. Uniform variance bound

Because variance is no larger than the second moment about any fixed centre,

\[
\operatorname{Var}_p(g_n')\le\sum_{n\ge2}p_n\,|g_n'-g_1'|^2.
\]

Also \(p_n\le\phi_n/\phi_1\). Put \(t=e^{2y}\ge1\) and \(m=n^2-1\ge3\). The exact channel ratio is

\[
\frac{\phi_n}{\phi_1}
=n^2\frac{2\pi n^2t-3}{2\pi t-3}e^{-\pi mt}.
\]

Since \(\pi t>3\),

\[
\frac{2\pi t}{2\pi t-3}<2,
\]

so

\[
\frac{\phi_n}{\phi_1}<2n^4e^{-\pi mt}.
\]

Because \(h(r)=4r/(2r-3)\) decreases from at most \(4\) toward \(2\),

\[
|g_n'-g_1'|
=2\pi mt+h(r_1)-h(r_n)
\le2\pi mt+2.
\]

For fixed \(m\ge3\), the function

\[
e^{-\pi mt}(2\pi mt+2)^2
\]

is strictly decreasing for \(t\ge1\), because

\[
\frac{d}{dt}\log\bigl[e^{-\pi mt}(2\pi mt+2)^2\bigr]
=\pi m\left(\frac{4}{2\pi mt+2}-1\right)<0.
\]

Hence the worst case is \(t=1\). Using the elementary bounds

\[
3<\pi<\frac{22}{7}
\]

and \(m\ge3\),

\[
2\pi m+2
<\frac{44}{7}m+2
\le7m,
\]

and

\[
e^{-\pi m}<e^{-3m}.
\]

Therefore

\[
\operatorname{Var}_p(g_n')
<98\sum_{n\ge2} n^4(n^2-1)^2e^{-3(n^2-1)}.
\]

For \(n=2\),

\[
b_2=98\cdot16\cdot9\,e^{-9}=14112e^{-9}.
\]

The finite Taylor series of \(e^3\) through the \(x^8/8!\) term already exceeds \(20\), so \(e^3>20\) and hence \(e^9>8000\). Thus

\[
b_2<\frac{14112}{8000}=1.764.
\]

For \(n\ge3\), define

\[
b_n:=98n^4(n^2-1)^2e^{-3(n^2-1)}.
\]

At \(n=3\),

\[
b_3<\frac{98\cdot81\cdot64}{20^8}<2\times10^{-5}.
\]

Moreover, for \(n\ge3\),

\[
\frac{(n+1)^4}{n^4}\le\left(\frac43\right)^4,
\]

and

\[
\frac{((n+1)^2-1)^2}{(n^2-1)^2}
\le\left(\frac{15}{8}\right)^2,
\]

so the polynomial ratio is below \(12\). The exponential ratio satisfies

\[
e^{-3((n+1)^2-n^2)}=e^{-3(2n+1)}\le e^{-21}<20^{-7}.
\]

Hence

\[
\frac{b_{n+1}}{b_n}<\frac{12}{20^7}<10^{-8}.
\]

Thus the entire \(n\ge3\) tail is less than \(2.1\times10^{-5}\), and consequently

\[
\boxed{\operatorname{Var}_p(g_n')<1.765<2.}
\]

uniformly for all \(y\ge0\).

## 4. Global compactified log-concavity

Combining the channel margin and the variance bound gives

\[
\mathcal M(y)<-7+2=-5<0.
\]

Finally,

\[
\frac{d^2}{d\eta^2}\log W(\eta)
=
\frac{\mathcal M(y)}{(1-\eta^2)^2}.
\]

Since the denominator is positive for \(0\le\eta<1\),

\[
\boxed{
\frac{d^2}{d\eta^2}\log W(\eta)<0
\quad\text{for every }0\le\eta<1.
}
\]

This proves SOH-G004.

## 5. Epistemic boundary

This theorem establishes a strong global shape property of the exact compactified Riemann kernel: strict positivity and strict log-concavity on the compact radial interval. It does **not** by itself imply that the associated entire function \(F\) has only real zeros. SOH-G003 real-rootedness therefore remains OPEN, and RH is not claimed.