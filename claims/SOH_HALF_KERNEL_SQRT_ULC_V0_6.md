# SOH Half-Kernel Sqrt-ULC Closure v0.6

Status: `COMPUTER_ASSISTED_L4_CORE_PLUS_ANALYTIC_L3_TAIL / SQRT_KERNEL_LOG_CONCAVITY / ULC / SUB_POISSON / FIRST_STIELTJES_SIGN / RH_OPEN`

Date: 2026-09-14

Let
\[
L(y)=-\log\Phi(y),\qquad y\ge0,
\]
for the exact even Riemann kernel used throughout SOH.

The missing coefficient-strengthening gate reduces to the log-concavity of
\[
h(x)=\Phi(\sqrt x),\qquad x\ge0.
\]
Indeed, for `x=y^2`,
\[
\frac{d^2}{dx^2}\log h(x)
=-\frac{yL''(y)-L'(y)}{4y^3}.
\]
Thus it is enough to prove
\[
\boxed{yL''(y)-L'(y)\ge0.}
\]

## 1. Increasing curvature

On `0<=y<=2/5`, outward interval arithmetic with the same four explicit theta channels and analytic derivative-tail bounds used by SOH-G024 certifies
\[
\boxed{L''''(y)>0.}
\]
Because `L` is even, `L'''(0)=0`, hence `L'''(y)>0` on the compact core away from zero.

For `y>=2/5`, write
\[
\Phi=\phi_1(1+\rho),\qquad g_1=\log\phi_1.
\]
The existing G024 tail machinery gives `r_1>6` and
\[
|\rho'|<\frac1{19000},\qquad
|\rho''|<\frac9{1000},\qquad
|\rho'''|<\frac{17}{10}.
\]
The exact dominant-channel identity gives
\[
-g_1'''(y)>40,
\]
because after clearing the positive denominator and writing `r=x+6`, the numerator is
\[
64x^4+928x^3+4656x^2+8424x+1512>0.
\]
Also
\[
\left|(\log(1+\rho))'''\right|
<\frac{17}{10}+3\frac1{19000}\frac9{1000}+2\left(\frac1{19000}\right)^3
<2.
\]
Therefore
\[
\boxed{L'''(y)>38\qquad(y\ge2/5).}
\]
Combining core and tail yields
\[
\boxed{L'''(y)>0\qquad(y>0).}
\]
Hence `L''` is increasing and, since `L'(0)=0`,
\[
yL''(y)-L'(y)
=\int_0^y\bigl(L''(y)-L''(t)\bigr)dt
\ge0.
\]
So `h(x)=Phi(sqrt(x))` is log-concave on `[0,infinity)`.

## 2. ULC coefficient theorem

With
\[
m_k=\int_0^\infty y^{2k}\Phi(y)dy
=\frac12\int_0^\infty x^{k-1/2}h(x)dx,
\]
the standard normalized-moment log-concavity theorem applied to `h` gives
\[
\boxed{
\frac{m_k^2}{m_{k-1}m_{k+1}}
\ge\frac{2k-1}{2k+1}
\qquad(k\ge1).
}
\]
For
\[
a_k=\frac{m_k}{(2k)!},
\]
this is exactly
\[
\boxed{
a_k^2\ge\frac{k+1}{k}a_{k-1}a_{k+1}.
}
\]
Equivalently, `(k! a_k)` is log-concave: the quotient coefficients are ultra-log-concave.

## 3. First Stieltjes sign

For `u>0`, define the tilted coefficient law
\[
p_n(u)=\frac{a_nu^n}{F(u)}
\]
and the birth-rate sequence
\[
\lambda_n=u(n+1)\frac{a_{n+1}}{a_n}.
\]
ULC is exactly the statement that `lambda_n` is nonincreasing in `n`. Since
\[
(n+1)p_{n+1}=\lambda_np_n,
\]
one obtains
\[
\operatorname{Var}(N)
=\mathbb E[N]+\operatorname{Cov}(N,\lambda_N)
\le\mathbb E[N].
\]
Therefore
\[
\boxed{
\left(\frac{F'}F\right)'(u)
=\frac{\operatorname{Var}(N)-\mathbb E[N]}{u^2}
\le0
\qquad(u>0).
}
\]
This closes the first global Stieltjes sign for the direct Weyl target `G(x)=F(-x)`.

## 4. PF2 firewall

PF2 alone is insufficient. The polynomial
\[
P(u)=1+u+\frac34u^2
\]
has positive log-concave/PF2 coefficients, but
\[
\left.\frac{d}{du}\frac{P'}P\right|_{u=0}
=\frac12>0.
\]
Thus the v0.6 strengthening genuinely uses the sqrt-kernel log-concavity/ULC step rather than recycling PF2.

## 5. Proof boundary

Closed at the declared repository-certificate level:

- compact `L''''>0` interval certificate;
- analytic tail `L'''>38`;
- global `L'''>0` and sqrt-kernel log-concavity;
- moment ULC and coefficient ULC;
- sub-Poisson tilted law;
- first Stieltjes sign `(F'/F)'<=0` on `u>0`.

Open:

- higher Stieltjes derivative signs;
- full Herglotz property of `-G'/G`;
- SOH-G003 real-rootedness;
- RH.
