# SOH Half-Kernel Global Second-Stieltjes Sign v0.8

Status: `COMPUTER_ASSISTED_COMPACT_PLUS_ANALYTIC_TAIL_PASS / SECOND_STIELTJES_GLOBAL_CLOSED / HIGHER_STIELTJES_OPEN / HERGLOTZ_OPEN / RH_OPEN`

Date: 2026-09-15

Let

\[
\xi\!\left(\frac12+z\right)=F(z^2),\qquad F(u)>0\quad(u\ge0),
\]

and define

\[
R(u)=\frac{F'(u)}{F(u)}.
\]

v0.6 proved the first global Stieltjes sign

\[
R'(u)\le0.
\]

v0.7 corrected the exact second derivative identity to

\[
\boxed{
R''(u)=
\frac{F(u)^2F'''(u)-3F(u)F'(u)F''(u)+2F'(u)^3}{F(u)^3}.
}
\]

This v0.8 certificate closes the next sign:

\[
\boxed{R''(u)>0\qquad\text{for every }u\ge0.}
\]

No zero table is used.

## 1. Compact region: `0 <= u <= 121`

Write

\[
F(u)=\sum_{n\ge0}a_nu^n,
\qquad
a_n=\frac{m_n}{(2n)!},
\qquad
m_n=\int_0^\infty y^{2n}\Phi(y)\,dy.
\]

The validator reconstructs `m_0,...,m_10` directly from the positive Riemann
kernel.  On `0<=y<=3` it uses outward interval composite Simpson bounds with an
explicit fourth-derivative remainder.  The derivatives of `Phi` are enclosed by
the same four explicit theta channels and analytic theta-tail bounds already
used by v0.6/G024.

For `y>=3`, the elementary estimates `pi>3`, `e>8/3`, and

\[
\sum_{n\ge1} n^4e^{-rn^2}<2e^{-r}\qquad(r>1000)
\]

give, uniformly for `0<=k<=10`,

\[
\int_3^\infty y^{2k}\Phi(y)\,dy<10^{-40}.
\]

From v0.6, the sequence

\[
b_n=n!a_n
\]

is log-concave.  Hence the ratios `b_{n+1}/b_n` decrease.  The certified moments
give

\[
\boxed{\frac{b_{10}}{b_9}<0.015288.}
\]

Therefore every coefficient tail `n>=11` of `F,F',F'',F'''` has an explicit
geometric-factorial upper bound.

The interval validator then covers `0<=u<=121` by exactly 2420 boxes of width
`1/20` and certifies

\[
\boxed{
F^2F'''-3FF'F''+2F'^3>0
}

on every box.  The exact-head receipt records the minimum outward lower margin.

## 2. Analytic tail: `z=sqrt(u) >= 11`

Put

\[
\ell(z)=\log\xi\!\left(\frac12+z\right).
\]

Direct differentiation of `ell(z)=log F(z^2)` gives

\[
\boxed{
8z^5R''(z^2)=Q(z)
:=z^2\ell'''(z)-3z\ell''(z)+3\ell'(z).
}
\]

The rational contribution from `s(s-1)` is

\[
Q_{\rm rat}(z)
=
\frac{1024z^5}{64z^6-48z^4+12z^2-1}>0.
\]

For `x=(2z+1)/4`, the standard Stieltjes-remainder bounds

\[
\psi(x) > \log x-\frac1{2x}-\frac1{12x^2},
\]

\[
\psi_1(x) < \frac1x+\frac1{2x^2}+\frac1{6x^3},
\]

\[
\psi_2(x) > -\frac1{x^2}-\frac1{x^3}-\frac1{2x^4}
\]

give the gamma-sector lower bound

\[
Q_\Gamma(z)\ge
\frac32\log\frac{2z+1}{4\pi}
-
\frac{32z^4+108z^3+128z^2+43z+5}{(2z+1)^4}.
\]

The derivative numerator of `Q_rat + Q_Gamma,lower` is, up to a positive
factor/denominator,

\[
384z^7-3392z^6-2336z^5-7056z^4-568z^3-636z^2+26z+13.
\]

After `z=t+11` its coefficients are

\[
993584055,
1275452842,
517546988,
103342408,
11596624,
749536,
26176,
384,
\]

all positive.  Thus this lower baseline is strictly increasing for `z>=11`.

For the zeta part, `Lambda(n)<=log n` gives

\[
|Q_\zeta(z)|
\le z^2S_3(s)+3zS_2(s)+3S_1(s),
\qquad
s=z+\frac12,
\]

where

\[
S_m(s)=\sum_{n\ge2}(\log n)^m n^{-s}
\]

is bounded by its first term plus the elementary integral test.  Moreover every
term `z^p n^{-z-1/2}`, `p<=2`, decreases on `z>=11`, because

\[
\frac{p}{z}-\log n\le\frac2{11}-\log2<0.
\]

Therefore the negative zeta majorant decreases while the positive baseline
increases; it is enough to check the boundary point `z=11`.  The validator
certifies there a strict positive margin greater than `0.09`.

Hence

\[
\boxed{Q(z)>0\quad(z\ge11)}
\]

and therefore

\[
\boxed{R''(u)>0\quad(u\ge121).}
\]

Together with the compact interval certificate:

\[
\boxed{
\left(\frac{F'}F\right)''(u)>0
\qquad\forall u\ge0.
}
\]

## 3. Proof firewall

Closed at the repository-certificate level:

- exact second-Stieltjes algebra;
- interval reconstruction of `m_0,...,m_10` from `Phi`;
- analytic `y>3` moment tail;
- v0.6 ULC coefficient-tail transfer;
- 2420-box compact positivity certificate on `0<=u<=121`;
- analytic `z>=11` gamma/rational/von-Mangoldt tail;
- global second Stieltjes sign `R''>0`.

Still open:

- `-R'''(u)>=0` and all higher Stieltjes signs;
- full Herglotz/Stieltjes property of `-G'/G`;
- global `PF3` of `Phi(sqrt(x))`;
- SOH-G003 real-rootedness;
- the Riemann Hypothesis.

No claim in this note promotes any of those open gates.
