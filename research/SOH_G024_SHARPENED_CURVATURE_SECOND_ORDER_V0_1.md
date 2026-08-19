# SOH-G024 — Sharpened kernel curvature and second-order region

**Status:** SHARPENED STRONG CONVEXITY PROVED / SECOND ORDER PROVED FOR q >= 1/9 / CORE q < 1/9 OPEN / RH OPEN  
**Branch:** `proof/soh-g024-jensen-kernel-positive-definite-v1`  
**Date:** 19 August 2026

## 1. Scope

SOH-G024 already proved the conservative full-kernel curvature margin

\[
L''>10
\]

and used it to establish global first-order complete monotonicity and the second-order tail theorem `H_y''>0` for `q>=1/4`.

The same canonical G004 decomposition contains a stronger channelwise constant. This note extracts it exactly and uses it to shrink the unresolved second-order core from `q<1/4` to `q<1/9`.

## 2. Sharp elementary channel floor

For every theta channel,

\[
-g_n''=h(r_n),
\qquad
h(r)=4r+\frac{24r}{(2r-3)^2},
\qquad
r_n=\pi n^2e^{2t}>3.
\]

We claim

\[
\boxed{h(r)>19\qquad(r>3).}
\]

Indeed,

\[
h(r)-19
=\frac{16r^3-124r^2+288r-171}{(2r-3)^2}.
\]

Set `x=r-3>=0`. The numerator becomes

\[
16x^3+20x^2-24x+9.
\]

The quadratic part

\[
20x^2-24x+9
\]

has discriminant

\[
(-24)^2-4\cdot20\cdot9=-144<0
\]

and positive leading coefficient. Hence it is strictly positive for every real `x`, and adding `16x^3>=0` preserves strict positivity on `x>=0`. Thus `h(r)>19`.

## 3. SOH-G024 sharpened strong-convexity theorem

The exact log-sum identity used in G004 gives

\[
L''=\sum_np_n(-g_n'')-\operatorname{Var}_p(g_n').
\]

G004 proves

\[
\operatorname{Var}_p(g_n')<2.
\]

Since every channel satisfies `-g_n''>19`, it follows immediately that

\[
\boxed{L''(t)>17\qquad(t\in\mathbb R).}
\]

This is a repository-internal sharpening of the earlier conservative `L''>10` consequence.

## 4. Improved first-order and bridge concentration constants

Strong convexity with margin `17` gives

\[
-\frac{C'(u)}{C(u)}>34u.
\]

For `a=|y|<1/2`, the external tilt obeys

\[
T_y(u)=2a\tanh(2au)<u.
\]

Hence

\[
\boxed{N_y(u)>33u}
\]

and therefore

\[
\boxed{
-\frac{H_y'(q)}{H_y(q)}>\frac{33}{2}.
}
\]

The previous `19/2` lower floor remains correct but is superseded on this branch by the stronger `33/2` floor.

The transverse score hierarchy now gives

\[
\boxed{
\mathbb E[r^{2n+2}]
<\frac{2n+3}{34}\mathbb E[r^{2n}],
}
\]

so

\[
\boxed{
\mathbb E[r^{2n}]<\frac{(2n+1)!!}{34^n}
}
\]

and

\[
\boxed{
\mathbb E[e^{\lambda r^2}]
\le(1-\lambda/17)^{-3/2},
\qquad0\le\lambda<17.
}
\]

## 5. Improved mean-curvature bound

The already-proved companion upper envelope remains

\[
L''(s)<21e^{2|s|}.
\]

Thus

\[
B_u(r)<42e^{2u+2|r|}.
\]

Use

\[
2|r|\le3r^2+\frac13.
\]

At `lambda=3`, the improved bridge MGF gives

\[
\mathbb E[B_u]
<42e^{2u+1/3}\left(1-\frac3{17}\right)^{-3/2}
=42e^{2u+1/3}\left(\frac{17}{14}\right)^{3/2}.
\]

Define

\[
C_{17}=42e^{1/3}\left(\frac{17}{14}\right)^{3/2}.
\]

A simple rational enclosure is

\[
\boxed{C_{17}<79.}
\]

For completeness, the exponential series gives

\[
e
<\sum_{k=0}^{6}\frac1{k!}
+\frac1{7!}\sum_{j\ge0}8^{-j}
=\frac{31967}{11760}
<\frac{87}{32}.
\]

Hence `e^(1/3)<7/5`. Also

\[
\left(\frac{17}{14}\right)^{3/2}<\frac{47}{35},
\]

which follows by squaring and comparing the resulting rational numbers. Therefore

\[
C_{17}
<42\cdot\frac75\cdot\frac{47}{35}
=\frac{1974}{25}
<79.
\]

Consequently

\[
\boxed{\mathbb E[B_u]<79e^{2u}.}
\]

## 6. Compact-tail bridge from u=1/3 to u=1/2

Use the exact second-order normal form and discard only non-negative terms:

\[
\frac{4u^3H_y''}{H_y}
>N_y+u\left[N_y^2-\mathbb E[B_u]\right].
\]

With `N_y>33u` and `E[B_u]<79e^(2u)`,

\[
\frac{4u^3H_y''}{H_y}
>u\left[33+1089u^2-79e^{2u}\right].
\]

Define

\[
F(u)=33+1089u^2-79e^{2u}.
\]

On `1/3<=u<=1/2`,

\[
F'(u)=2178u-158e^{2u}
\ge726-158e.
\]

Using `e<87/32`,

\[
726-158e
>726-158\frac{87}{32}
=\frac{4743}{16}>0.
\]

Thus `F` is strictly increasing on this interval. At the left endpoint,

\[
F(1/3)=154-79e^{2/3}>0.
\]

The last inequality follows from `e<87/32`; after cubing the positive quantities it reduces to the exact integer comparison

\[
79^3\,87^2
<154^3\,32^2,
\]

namely

\[
3731812191<3739918336.
\]

Therefore

\[
\boxed{H_y''(q)>0\qquad(1/9\le q\le1/4).}
\]

## 7. Combined SOH-G024 second-order region

Chapter 52 already proves

\[
H_y''(q)>0
\qquad(q\ge1/4).
\]

Combining the two analytic regions gives

\[
\boxed{
H_y''(q)>0
\qquad
\left(q\ge\frac19,\quad0<|y|<\frac12\right).
}
\]

Thus the remaining second-order compact core is reduced to

\[
\boxed{0\le q<\frac19.}
\]

## 8. Proof firewall

**PROVED / EXACT:** `L''>17`, the improved first-order log-slope floor `33/2`, the improved bridge moment/MGF hierarchy with denominator `34` and radius `17`, the bound `E[B_u]<79e^(2u)`, and `H_y''>0` for all `q>=1/9` throughout the open Dimitrov-Xu strip.

**OPEN:** second-order complete monotonicity on `0<=q<1/9`, derivative orders `m>=3`, strict external Fourier positivity on the entire strip, SOH-G003, SOH-C005, PF3, PF-infinity, and RH.
