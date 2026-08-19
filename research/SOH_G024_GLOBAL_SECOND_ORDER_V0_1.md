# SOH-G024 — Fourth log-curvature certificate and global second-order closure

**Status:** COMPUTER-ASSISTED INTERVAL LEMMA / EXACT DOWNSTREAM RICCATI PROOF / GLOBAL SECOND ORDER PROVED AT REPOSITORY CERTIFICATE LEVEL / ORDERS >=3 OPEN / RH OPEN  
**Branch:** `proof/soh-g024-jensen-kernel-positive-definite-v1`  
**Date:** 19 August 2026

## 1. Scope

Earlier G024 work proves

\[
H_y'(q)<0
\]

globally and

\[
H_y''(q)>0
\]

for `q>=1/9`, for every external Dimitrov--Xu tilt `0<|y|<1/2`. This note closes the remaining compact second-order core by combining one computer-assisted kernel lemma with an exact Riccati estimate.

The computer-assisted component is explicitly isolated. It uses `mpmath.iv` outward interval arithmetic on a compact interval and an analytic infinite-theta-tail bound. It is not represented as a proof-assistant-verified theorem.

No statement below proves derivative orders `m>=3`, full complete monotonicity, strict external Fourier positivity, SOH-G003, SOH-C005, PF3, PF-infinity, or RH.

## 2. Kernel notation

Let

\[
K(t)=\frac12\Phi(|t|),
\qquad
L(t)=-\log K(t).
\]

The factor `1/2` drops from every logarithmic derivative. Previous G024 work sharpens the canonical G004 estimates to

\[
\boxed{L''(t)>17}
\]

and retains the upper envelope

\[
\boxed{L''(t)<21e^{2|t|}}.
\]

## 3. Fourth log-curvature lemma

The new kernel target is

\[
\boxed{L''''(t)<20L''(t)\qquad(t\in\mathbb R).}
\tag{Q}
\]

Because `L` is even, it is enough to cover `t>=0`.

### 3.1 Direct theta derivatives

For

\[
\phi_n(t)=4a_ne^{5t/2}(2r_n-3)e^{-r_n},
\qquad
r_n=a_ne^{2t},\qquad a_n=\pi n^2,
\]

write

\[
\phi_n^{(k)}(t)=4a_ne^{5t/2-r_n}Q_k(r_n).
\]

The required exact polynomials are

\[
Q_0=2r-3,
\]

\[
Q_1=-4r^2+15r-\frac{15}{2},
\]

\[
Q_2=8r^3-56r^2+\frac{165}{2}r-\frac{75}{4},
\]

\[
Q_3=-16r^4+180r^3-529r^2+\frac{1635}{4}r-\frac{375}{8},
\]

and

\[
Q_4=32r^5-528r^4+2588r^3-4256r^2+\frac{15465}{8}r-\frac{1875}{16}.
\]

For `A_k=Phi^(k)/Phi`,

\[
L''=A_1^2-A_2
\]

and

\[
L''''=-A_4+4A_3A_1+3A_2^2-12A_2A_1^2+6A_1^4.
\]

These formulas are evaluated directly by the interval certificate.

## 4. Compact interval certificate: `0<=t<=2/5`

The script

`run_soh_g024_fourth_log_curvature_interval.py`

uses explicit theta terms `n=1,...,4` and analytically encloses all `n>=5` terms.

For every derivative order `k<=4`, the omitted tail is bounded using

\[
|Q_k(r)|\le A_kr^{k+1},
\qquad
\pi<\frac{22}{7},
\qquad
e^3>20.
\]

For `n>=5` the derivative-envelope ratio is less than

\[
\left(\frac65\right)^{12}e^{-33}
<\frac{1}{1001},
\]

so the first omitted term controls the entire tail geometrically. The fixed outward tail enclosures used by the certificate are

\[
4\cdot10^{-28},\quad
2\cdot10^{-25},\quad
8\cdot10^{-23},\quad
5\cdot10^{-20},\quad
3\cdot10^{-17}
\]

for derivative orders zero through four respectively.

Adaptive outward interval subdivision of

\[
0\le t\le\frac25
\]

then certifies

\[
\boxed{20L''(t)-L''''(t)>0}
\]

on every accepted box. The script fails closed if any box remains unresolved at the declared maximum subdivision depth.

## 5. Analytic tail: `t>=2/5`

Write

\[
\Phi=\phi_1(1+\rho),
\qquad
\rho=\sum_{n\ge2}\frac{\phi_n}{\phi_1}.
\]

Since

\[
e^{4/5}>1+\frac45+\frac12\left(\frac45\right)^2>2
\]

and `pi>3`, one has

\[
r_1=\pi e^{2t}>6
\]

for `t>=2/5`.

For the dominant channel define

\[
P_1=20(-g_1'')-(-g_1'''').
\]

Exact algebra gives

\[
P_1-390
=
\frac{1024r^5-12384r^4+52800r^3-106128r^2+92880r-31590}
{(2r-3)^4}.
\]

With `r=x+6`, the numerator becomes

\[
1024x^5+18336x^4+124224x^3+381168x^2+457488x+22842,
\]

so

\[
\boxed{P_1>390\qquad(r>=6).}
\]

For `r>=6`, the channel logarithmic derivatives obey the conservative bounds

\[
|g'|<2r,
\quad
|g''|<5r,
\quad
|g'''|<8r,
\quad
|g''''|<21r.
\]

The corresponding Bell-polynomial bounds for derivatives of `rho_n=phi_n/phi_1` are taken conservatively as

\[
1,\ 4,\ 26,\ 204,\ 1886.
\]

Together with

\[
\frac{\phi_n}{\phi_1}<2n^4e^{-\pi(n^2-1)e^{2t}},
\]

the worst successive envelope ratio is bounded by

\[
\left(\frac32\right)^{12}e^{-30}<\frac1{1001}.
\]

Using `e^18>20^6`, the script proves the uniform tail bounds

\[
|\rho|<10^{-6},
\quad
|\rho'|<\frac1{19000},
\quad
|\rho''|<\frac9{1000},
\quad
|\rho'''|<\frac{17}{10},
\quad
|\rho''''|<378.
\]

For `h=log(1+rho)`, this gives

\[
|h''|<\frac1{100},
\qquad
|h''''|<379,
\]

and hence

\[
|h''''-20h''|<380.
\]

Since

\[
L=-g_1-h+\text{constant},
\]

we conclude

\[
20L''-L''''>390-380=10
\]

for all `t>=2/5`.

Combined with the compact interval certificate and evenness, this proves (Q) on the full real line at the declared computer-assisted interval level.

## 6. Exact bridge trapezoid identity

Let

\[
A_u(r)=L'(u+r)+L'(u-r)
=\int_{r-u}^{r+u}L''(s)\,ds
\]

and

\[
B_u(r)=L''(u+r)+L''(u-r).
\]

The trapezoid error has the exact Peano-kernel form

\[
\boxed{
 uB_u(r)-A_u(r)
 =\frac12\int_{-u}^{u}(u^2-v^2)L''''(r+v)\,dv.
}
\]

Using (Q) and the existing upper curvature envelope,

\[
L''''(s)<20L''(s)<420e^{2|s|},
\]

so

\[
\boxed{
 uB_u(r)-A_u(r)
 <280u^3e^{2u}e^{2|r|}.
}
\]

For the normalized bridge measure,

\[
R=-\frac{C'}C=\mathbb E[A_u],
\qquad
R'=\mathbb E[B_u]-\operatorname{Var}(A_u),
\]

and therefore

\[
\boxed{
 uR'-R
\le\mathbb E[uB_u-A_u].
}
\]

## 7. Uniform compact-core bound for `S_y'`

Put

\[
a=|y|,
\qquad
T=2a\tanh(2au),
\qquad
N=R-T,
\qquad
S_y(q)=\frac{N(u)}{2u},\quad q=u^2.
\]

Then

\[
S_y'(q)=\frac{uN'(u)-N(u)}{4u^3}.
\]

For the bridge part, the sharpened MGF hierarchy and

\[
2|r|\le3r^2+\frac13
\]

give

\[
\mathbb E[e^{2|r|}]
\le e^{1/3}\left(\frac{17}{14}\right)^{3/2}.
\]

Inside the compact core `u<=1/3`, therefore

\[
\frac{uR'-R}{4u^3}
<70e\left(\frac{17}{14}\right)^{3/2}.
\]

For the tilt, with `x=2au`,

\[
\tanh x-x\operatorname{sech}^2x
\le\frac23x^3,
\]

which yields

\[
\frac{T-uT'}{4u^3}\le\frac16.
\]

Thus

\[
\boxed{
S_y'(q)
<70e\left(\frac{17}{14}\right)^{3/2}+\frac16.
}
\]

The exact rational enclosures

\[
e<\frac{87}{32},
\qquad
\left(\frac{17}{14}\right)^{3/2}<\frac{47}{35}
\]

give

\[
\boxed{S_y'(q)<\frac{12275}{48}.}
\]

The sharpened first-order theorem already gives

\[
S_y(q)>\frac{33}{2},
\]

hence

\[
S_y(q)^2>\frac{1089}{4}.
\]

The strict rational gap is

\[
\boxed{
\frac{1089}{4}-\frac{12275}{48}
=\frac{793}{48}>0.
}
\]

Therefore

\[
\boxed{
\frac{H_y''(q)}{H_y(q)}=S_y(q)^2-S_y'(q)>0
}
\]

throughout `0<q<=1/9`. The endpoint `q=0` follows by continuity.

## 8. Global second-order theorem

Chapter 53 already proves

\[
H_y''(q)>0
\qquad(q\ge1/9).
\]

The compact-core argument above proves the same sign on `0<=q<=1/9`. Consequently:

\[
\boxed{
H_y''(q)>0
\qquad
\forall q\ge0,\quad0<|y|<\frac12.
}
\]

This closes the second non-trivial complete-monotonicity inequality globally.

## 9. Proof firewall

**COMPUTER-ASSISTED CERTIFIED:** `L''''<20L''` on `0<=t<=2/5` using outward `mpmath.iv` intervals plus an analytic infinite theta-tail enclosure.

**ANALYTIC EXACT:** `L''''<20L''` for `t>=2/5`; the Peano bridge identity; the bridge MGF reduction; the tilt bound; the rational Riccati gap `793/48`; and the implication from the kernel lemma to compact-core positivity.

**GLOBAL G024 RESULT:** first-order and second-order complete-monotonicity inequalities are proved on their full domains, with the second-order result depending on the declared interval certificate.

**OPEN:** every derivative order `m>=3`, full complete monotonicity, strict external Fourier positivity, Wiener density, SOH-G003, SOH-C005, PF3, PF-infinity, and RH.
