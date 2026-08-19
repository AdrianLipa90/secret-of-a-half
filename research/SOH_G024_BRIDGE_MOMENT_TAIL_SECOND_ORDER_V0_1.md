# SOH-G024 — Bridge moment hierarchy and second-order tail theorem

**Status:** EXACT MOMENT HIERARCHY / SECOND ORDER PROVED FOR q >= 1/4 / COMPACT CORE OPEN / RH OPEN  
**Branch:** `proof/soh-g024-jensen-kernel-positive-definite-v1`  
**Date:** 19 August 2026

## 1. Scope

The preceding G024 bridge reduction gives

\[
\frac{4u^3H_y''(u^2)}{H_y(u^2)}
=N_y+u\left[N_y^2+\operatorname{Var}(A_u)-\mathbb E(B_u)
+4a^2\operatorname{sech}^2(2au)\right],
\]

where `a=|y|`, `0<a<1/2`, and the first-order theorem already proves

\[
N_y(u)>19u.
\]

This note adds two exact results:

1. a full moment / exponential-moment hierarchy for the normalized bridge measure;
2. a proof that the second complete-monotonicity inequality holds for the entire tail region `u>=1/2`, equivalently `q>=1/4`.

The compact core `0<=q<1/4` remains open.

## 2. Bridge score identity

Recall

\[
d\mu_u(r)=\frac{r^2K(u+r)K(u-r)}{C(u)}\,dr,
\qquad
L=-\log K.
\]

Define the transverse bridge slope

\[
\boxed{D_u(r)=L'(u+r)-L'(u-r).}
\]

The logarithmic derivative of the bridge density with respect to `r` is

\[
\partial_r\log\mu_u(r)=\frac2r-D_u(r).
\]

For every integer `n>=0`, integrate the derivative of `r^(2n+1)` against the bridge density. Boundary terms vanish because of the factor `r^2` at the origin and the super-exponential Riemann-kernel decay at infinity. This gives

\[
0=(2n+1)\mathbb E[r^{2n}]+2\mathbb E[r^{2n}]
-\mathbb E[r^{2n+1}D_u(r)],
\]

hence the exact score hierarchy

\[
\boxed{
\mathbb E_{\mu_u}[r^{2n+1}D_u(r)]
=(2n+3)\mathbb E_{\mu_u}[r^{2n}].
}
\]

In particular,

\[
\boxed{\mathbb E[rD_u(r)]=3.}
\]

## 3. Strong-convexity moment hierarchy

Canonical SOH-G004 gives

\[
\boxed{L''(t)>10\qquad(t\in\mathbb R).}
\]

For `r>0`,

\[
D_u(r)=\int_{u-r}^{u+r}L''(s)\,ds>20r.
\]

Therefore

\[
r^{2n+1}D_u(r)>20r^{2n+2}
\]

away from the null point `r=0`. Combining with the score identity yields

\[
\boxed{
\mathbb E[r^{2n+2}]
<\frac{2n+3}{20}\mathbb E[r^{2n}].
}
\]

Iterating from `E[1]=1`,

\[
\boxed{
\mathbb E[r^{2n}]<\frac{(2n+1)!!}{20^n},
\qquad n\ge1.
}
\]

The first case is

\[
\boxed{\mathbb E[r^2]<\frac3{20}.}
\]

## 4. Exponential-square concentration

For `0<=lambda<10`, expand the exponential and use the even-moment hierarchy:

\[
\mathbb E[e^{\lambda r^2}]
=\sum_{n\ge0}\frac{\lambda^n}{n!}\mathbb E[r^{2n}]
\le\sum_{n\ge0}\frac{(2n+1)!!}{20^n n!}\lambda^n.
\]

Since

\[
\frac{(2n+1)!!}{20^n}
=\frac{(3/2)_n}{10^n},
\]

the binomial series gives

\[
\boxed{
\mathbb E[e^{\lambda r^2}]
\le(1-\lambda/10)^{-3/2},
\qquad 0\le\lambda<10.
}
\]

For `lambda>0` the inequality is strict under the strict G004 curvature margin.

## 5. A global upper envelope for the kernel curvature

Write the theta-channel variables as in SOH-G004,

\[
r_n=\pi n^2t,\qquad t=e^{2s}\ge1.
\]

For a channel,

\[
-g_n''=4r_n+\frac{24r_n}{(2r_n-3)^2}.
\]

Because `r_n>3`, the second term is below `8`. The log-sum identity gives

\[
L''(s)=\sum_np_n(-g_n'')-\operatorname{Var}_p(g_n')
<4\mathbb E_p[r_n]+8.
\]

It remains to control the excess over the first channel. From the same ratio estimate used in G004,

\[
\frac{\phi_n}{\phi_1}<2n^4e^{-\pi(n^2-1)t},
\]

we obtain

\[
\mathbb E_p[r_n]-r_1
<2\pi t\sum_{n\ge2}n^4(n^2-1)e^{-\pi(n^2-1)t}.
\]

Every term is decreasing for `t>=1`, so evaluate the conservative bound at `t=1`. For `n=2`, using `pi<22/7`, `pi>3`, and `e^3>20`,

\[
2\pi\,16\,3\,e^{-3\pi}
<\frac{33}{875}.
\]

For `n>=3`, the first conservative term is below `10^{-6}` and successive terms have ratio below `12/20^7`; this tail is far below the remaining `2/875`. Hence

\[
\boxed{\mathbb E_p[r_n]-r_1<\frac1{25}.}
\]

Consequently, using `pi<22/7` and `t>=1`,

\[
L''(s)
<4\pi t+\frac4{25}+8
<21t.
\]

By evenness,

\[
\boxed{10<L''(s)<21e^{2|s|}\qquad(s\in\mathbb R).}
\]

The lower inequality is G004; the upper inequality is the new companion envelope used below.

## 6. Upper bound for the mean bridge curvature

The bridge curvature is

\[
B_u(r)=L''(u+r)+L''(u-r).
\]

The upper envelope gives

\[
B_u(r)<42e^{2u+2|r|}.
\]

Use the elementary square inequality

\[
2|r|\le\frac52r^2+\frac25.
\]

Then the bridge exponential-square bound at `lambda=5/2` yields

\[
\mathbb E[B_u]
<42e^{2u+2/5}\left(1-\frac14\right)^{-3/2}
=42e^{2u+2/5}\left(\frac43\right)^{3/2}.
\]

Define

\[
C_B:=42e^{2/5}\left(\frac43\right)^{3/2}.
\]

We need only the elementary comparison `C_B<36e`. A self-contained bound is available: the exponential series gives `e<49/18`, hence `e^(2/5)<3/2`; while `e^3>20`. Thus

\[
C_B<63\left(\frac43\right)^{3/2}
<36\,20^{1/3}<36e.
\]

The middle inequality is purely algebraic: after simplification it is equivalent to

\[
2744^2<3\cdot1620^2,
\]

which holds. Therefore

\[
\boxed{\mathbb E[B_u]<36e\,e^{2u}.}
\]

## 7. Exponential lower bound for the external first-order surplus

The lower G004 curvature estimate can also be sharpened before averaging. Since

\[
L''(s)
=\sum_np_n(-g_n'')-\operatorname{Var}_p(g_n')
>4\pi e^{2|s|}-2,
\]

and

\[
A_u(r)=L'(u+r)+L'(u-r)
=\int_{r-u}^{r+u}L''(s)\,ds
\]

for `r>=0`, the even increasing lower envelope is minimized when the interval is centered at zero. Hence

\[
A_u(r)>\int_{-u}^{u}(4\pi e^{2|s|}-2)\,ds
=4\pi(e^{2u}-1)-4u.
\]

Averaging gives

\[
R(u)>4\pi(e^{2u}-1)-4u.
\]

Since

\[
T_y(u)=2a\tanh(2au)<4a^2u<u,
\]

we obtain

\[
\boxed{
N_y(u)>12(e^{2u}-1)-5u.
}
\]

For `u>=1/2`, the function

\[
6e^{2u}-12-5u
\]

is increasing and is already positive at `u=1/2` because `e^3>20` implies `e>29/12`. Therefore

\[
\boxed{N_y(u)>6e^{2u}\qquad(u\ge1/2).}
\]

## 8. SOH-G024 second-order tail theorem

For `u>=1/2`, `e^(2u)>=e`. The curvature bound gives

\[
\mathbb E[B_u]<36e\,e^{2u}\le36e^{4u}.
\]

At the same time,

\[
N_y(u)^2>36e^{4u}.
\]

Hence

\[
\boxed{N_y(u)^2>\mathbb E[B_u]\qquad(u\ge1/2).}
\]

Return to the exact second-order bridge normal form:

\[
\frac{4u^3H_y''(u^2)}{H_y(u^2)}
=N_y+u\left[N_y^2+\operatorname{Var}(A_u)-\mathbb E(B_u)
+4a^2\operatorname{sech}^2(2au)\right].
\]

Every omitted term is non-negative and `N_y>0`. Therefore

\[
\boxed{
H_y''(q)>0
\qquad
\left(q\ge\frac14,\quad0<|y|<\frac12\right).
}
\]

This is a genuine analytic tail theorem. It is not a finite-grid statement.

## 9. Remaining compact core

The second-order proof obligation is now reduced to

\[
\boxed{
0\le q<\frac14,
\qquad0<|y|<\frac12.
}
\]

The crude separation `N^2-E[B]` is deliberately not used in the small-`u` region because it destroys the exact cancellation present as `u->0`. The compact core should instead be treated by a cancellation-preserving Taylor/bridge expansion or an independent exact inequality.

## 10. Proof firewall

**PROVED / EXACT:** bridge score identity, all even-moment bounds, exponential-square concentration, the companion curvature upper envelope `L''<21e^(2|s|)`, the exponential lower bound on `N_y`, and `H_y''>0` for `q>=1/4` across the full open Dimitrov-Xu strip.

**OPEN:** `H_y''>=0` on `0<=q<1/4`, complete monotonicity at derivative orders `m>=3`, strict external Fourier positivity on the full strip, SOH-G003, SOH-C005, PF3, PF-infinity, and RH.
