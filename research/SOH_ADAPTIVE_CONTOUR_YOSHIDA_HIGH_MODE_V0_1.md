# SOH Adaptive-Contour Yoshida High-Mode Certificate v0.1

Status: **GENERAL-c SOURCE ENVELOPE / ADAPTIVE RATE 2a / ASYMPTOTICALLY OPTIMAL RATE WITHIN CURRENT CERTIFICATE ARCHITECTURE / MINIMAL OPERATOR CUTOFF OPEN**

Date: 2026-09-26

Primary external source:
- M. Suzuki, *Aspects of the screw function corresponding to the Riemann
  zeta-function*, proof of Theorem 4.3, especially equations (4.4),
  (4.11)--(4.13).

The source explicitly fixes an arbitrary contour height
\[
c>1.
\]

No RH and no zero list are used.

## 1. General contour \(C_1(c)\)

On
\[
\Re s=1+c,
\]
the rational source term satisfies
\[
\left|
\frac1{s-1}+\frac1s
\right|
\le
\frac1c+\frac1{1+c}.
\]

Also
\[
\left|
\frac{\zeta'}{\zeta}(1+c+it)
\right|
\le
\sum_{n\ge2}\frac{\Lambda(n)}{n^{1+c}}
\le
\sum_{n\ge2}\frac{\log n}{n^{1+c}}.
\]

For \(c>1\), the function
\[
x\mapsto\frac{\log x}{x^{1+c}}
\]
is decreasing on \(x\ge2\). Therefore
\[
\sum_{n\ge2}\frac{\log n}{n^{1+c}}
\le
\frac{\log2}{2^{1+c}}
+
\int_2^\infty\frac{\log x}{x^{1+c}}dx.
\]

The integral is
\[
2^{-c}
\left(
\frac{\log2}{c}+\frac1{c^2}
\right).
\]

Hence a completely elementary source constant is
\[
\boxed{
C_1(c)
\le
\max\left\{
\frac1c+\frac1{1+c},
\frac{\log2}{2^{1+c}}
+
2^{-c}
\left(
\frac{\log2}{c}+\frac1{c^2}
\right)
\right\}.
}
\]

At \(c=2\), the rational branch is \(5/6\), recovering the existing
repository certificate.

## 2. General contour \(C_2(a_1,c)\)

Suzuki's exact shifted kernel is
\[
K(t,u;y)
=
\frac1{2y}
\left(
-e^{-y(t+|t|)}
-e^{-y(u+|u|)}
+e^{-y(t+u+|t-u|)}
+1
\right).
\]

For same-sign \(t,u\), let
\[
m=\min(|t|,|u|).
\]

Then
\[
K(t,u)=m.
\]

For \(y=+c\),
\[
\frac{K(t,u;c)}{K(t,u)}
=
\frac{1-e^{-2cm}}{2cm}
\le1.
\]

For \(y=-c\),
\[
\frac{K(t,u;-c)}{K(t,u)}
=
\frac{e^{2cm}-1}{2cm}.
\]

The function
\[
x\mapsto\frac{e^x-1}{x}
\]
is increasing on \(x>0\). Thus for \(|t|,|u|\le a_1\),
\[
\boxed{
C_2(a_1,c)
\le
\frac{e^{2ca_1}-1}{2ca_1}.
}
\]

For \(c=2\), this is exactly
\[
\frac{e^{4a_1}-1}{4a_1},
\]
the previous hard-coded envelope.

## 3. General source certificate

Let
\[
p=C_1(c)C_2(a_1,c).
\]

For fixed requested raw-integral floor \(\mu>0\) and margin
\(\delta_C>0\), take
\[
C=3p+\pi\mu+\delta_C.
\]

Keep the same certified gamma rule
\[
t_0=2\sqrt\pi\,e^{C+1}
\]
and the same explicit \(C_0\) and leakage coefficient
\[
B(a,t_0)
=
\frac{8a}{\pi^2}
\left(
t_0+at_0^2+\frac{a^2t_0^3}{3}
\right).
\]

Then the Suzuki (4.11) floor
\[
\nu_N
=
\frac{
C-2p-(C+C_0)B/N
}{\pi}
\]
is at least \(\mu\) whenever
\[
\boxed{
N
\ge
\frac{
(C+C_0)B
}{
C-2p-\pi\mu
}.
}
\]

This is the same theorem architecture as the existing \(c=2\) implementation,
with no new hypothesis.

## 4. Adaptive contour

For large \(a\), choose
\[
\boxed{
c(a)=1+a^{-2},
\qquad
a_1(a)=a+a^{-2}.
}
\]

Then
\[
c(a)>1,
\qquad
a_1(a)>a.
\]

Moreover
\[
c(a)a_1(a)
=
a+o(1).
\]

The elementary \(C_1\) envelope satisfies
\[
\boxed{
C_1(c(a))\to\frac32.
}
\]

The \(C_2\) envelope satisfies
\[
\boxed{
C_2(a_1(a),c(a))
\sim
\frac{e^{2a}}{2a}.
}
\]

Therefore
\[
p(a)
\sim
\frac34\frac{e^{2a}}a
\]
and
\[
\boxed{
C(a)
\sim
\frac94\frac{e^{2a}}a.
}
\]

## 5. Adaptive cutoff asymptotic

As in the fixed-\(c\) analysis,
\[
C_0=C+O(1),
\]
\[
B
\sim
\frac{8}{3\pi^2}a^3t_0^3,
\]
and
\[
\frac{C+C_0}{C-2p-\pi\mu}
=
\frac{C+C_0}{p+\delta_C}
\to6.
\]

Hence the continuous required cutoff \(N_*(a)\) satisfies
\[
\log N_*(a)
=
3C(a)+3\log a+O(1).
\]

Thus
\[
\boxed{
\log N_*(a)
\sim
\frac{27}{4}\frac{e^{2a}}a.
}
\]

Taking one more logarithm,
\[
\boxed{
\log\log N_*(a)
=
2a-\log a+\log\frac{27}{4}+o(1).
}
\]

The integer ceiling has the same asymptotic.

Compared with the previous \(c=2\) schedule,
\[
4a-\log a+O(1),
\]
the adaptive contour cuts the leading \(\log\log N\) slope exactly in half.

## 6. Rate-optimality inside this certificate architecture

This statement is only about the present proof envelope.

The source requires
\[
c>1,\qquad a_1>a.
\]

Put
\[
x=ca_1>a.
\]

The exact \(C_1\) definition contains the rational source term, so
\[
C_1(c)\ge\frac1c.
\]

Also
\[
C_2(a_1,c)
\ge
\frac{e^{2x}-1}{2x}.
\]

Since
\[
c=\frac{x}{a_1}<\frac xa,
\]
we get
\[
C_1C_2
>
\frac{a(e^{2x}-1)}{2x^2}.
\]

For \(x>a\to\infty\), this forces the exponential rate
\[
\boxed{
\liminf_{a\to\infty}
\frac1a\log[C_1(c)C_2(a_1,c)]
\ge2
}
\]
for every admissible contour/radius schedule inside this source comparison.

Since the gamma threshold necessarily has
\[
\log t_0=C+O(1)
\]
in the current architecture, the corresponding sufficient cutoff cannot have
a \(\log\log N\) leading slope below \(2\).

The adaptive schedule above achieves slope \(2\).

Therefore
\[
\boxed{
2
}
\]
is asymptotically optimal at the leading-rate level **within the current
Suzuki \(C_1C_2\) + gamma-window + Fourier-leakage certificate architecture**.

This is not a lower bound for the true minimal high-mode cutoff of \(A_a\).

## 7. Negative-index consequence

If the source high-tail coercivity is transported to the localized
Friedrichs form, then
\[
\boxed{
\kappa_a=n_-(A_a)
\le
2N_{\rm cert}^{\rm adaptive}(a)+1.
}
\]

This remains only an index envelope. It is not a literal Fourier-support
statement for the negative eigenvectors.

## 8. What must change to do better than slope 2

Optimizing constants inside the same architecture can improve the
\(o(a)\)/constant terms, but not the leading slope \(2\).

To beat it one must change at least one structural input:
- replace the vertical-contour \(C_2\) comparison;
- exploit cancellation instead of absolute \(C_1C_2\) control;
- derive high-mode coercivity directly from the localized operator symbol;
- or use a different positive/indefinite transfer adapted to the
  de Branges--Pontryagin complement.

This sharply identifies the next useful analytic innovation.
