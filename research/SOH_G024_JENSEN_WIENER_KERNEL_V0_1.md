# SOH-G024 — Jensen–Wiener correlation kernel and complete-monotonicity target

**Status:** EXACT REPARAMETRIZATION / FIRST-ORDER COMPLETE MONOTONICITY PROVED / HIGHER ORDERS OPEN / RH OPEN  
**Branch:** `proof/soh-g024-jensen-kernel-positive-definite-v1`  
**Date:** 19 August 2026

## 1. Scope

This generation leaves the PF3 staircase and returns directly to an RH-equivalent correlation-kernel criterion. It also separates two different `y`-tilts which coincide at `y=0` but are different for `y != 0`.

No statement below promotes RH, SOH-G003, PF3, or PF-infinity.

Primary external sources:

- D. K. Dimitrov and Y. Xu, *Wronskians of Fourier and Laplace Transforms*, arXiv:1606.05011, especially Theorem 1.1 and the order-two correlation kernel.
- G. Csordas, *Fourier transforms of positive definite kernels and the Riemann xi-Function*, arXiv:1309.0055, for the positive-definite-kernel / Laguerre frontier at `y=0`.

## 2. Repository normalization on the full line

The repository uses the positive half-line kernel `Phi` satisfying

\[
\xi\!\left(\frac12+z\right)=\int_0^\infty \Phi(t)\cosh(zt)\,dt.
\]

Define the even full-line kernel

\[
\boxed{K(t):=\frac12\Phi(|t|).}
\]

Then

\[
\boxed{\Xi(x):=\xi\!\left(\frac12+ix\right)=\int_{\mathbb R}K(t)e^{-ixt}\,dt.}
\]

The factor `1/2` is only the conversion from the repository half-line normalization to a full-line Fourier transform.

## 3. Exact Dimitrov–Xu order-two correlation

For a suitable even positive kernel `K`, define

\[
\nu_2(t):=\int_{\mathbb R}(t-2s)^2K(t-s)K(s)\,ds.
\]

Dimitrov and Xu use the tilted order-two kernel

\[
\Psi_y(t):=\cosh(ty)\nu_2(t).
\]

Their Theorem 1.1 gives, for the Riemann kernel,

\[
\boxed{RH\iff\mathcal T(\Psi_y)\text{ is dense in }L^1(\mathbb R)\quad\text{for every }0<|y|<\frac12.}
\]

By Wiener's `L^1` Tauberian theorem, this is equivalently the statement that the Fourier transform of `Psi_y` has no real zero, for every such `y`.

## 4. Exact centered reparametrization

Put

\[
t=2u,\qquad s=u-r.
\]

Then

\[
t-s=u+r,\qquad s=u-r,\qquad t-2s=2r,
\]

and therefore

\[
\boxed{\nu_2(2u)=4\int_{\mathbb R}r^2K(u+r)K(u-r)\,dr.}
\]

Define

\[
\boxed{C(u):=\int_{\mathbb R}r^2K(u+r)K(u-r)\,dr.}
\]

Thus

\[
\boxed{\Psi_y(2u)=4D_y(u),\qquad D_y(u):=\cosh(2yu)C(u).}
\]

A non-zero scalar factor and a fixed dilation do not change the density question. Hence the exact RH-equivalent target can be written as

\[
\boxed{RH\iff\mathcal T(D_y)\text{ is dense in }L^1(\mathbb R)\quad\forall\,0<|y|<\frac12.}
\]

Since `D_y` is real, even and integrable, its Fourier transform is continuous and real. Its value at zero is strictly positive. Therefore Wiener's no-real-zero condition is equivalently

\[
\boxed{\widehat D_y(x)>0\quad\forall x\in\mathbb R,\quad0<|y|<\frac12.}
\]

This is an exact reformulation, not a new proof.

## 5. Exact external Wronskian/Laguerre identity

Let

\[
f(z)=\int_{\mathbb R}K(t)e^{-izt}\,dt.
\]

Writing `t=a+b`, `s=b` in the Fourier transform of `nu_2` gives

\[
\widehat\nu_2(z)
=\iint (a-b)^2K(a)K(b)e^{-iz(a+b)}\,da\,db.
\]

Using

\[
\int tK(t)e^{-izt}dt=i f'(z),
\qquad
\int t^2K(t)e^{-izt}dt=-f''(z),
\]

one obtains the exact identity

\[
\boxed{\widehat\nu_2(z)=2\bigl(f'(z)^2-f(z)f''(z)\bigr).}
\]

Since multiplication by `cosh(ty)` averages the Fourier transform at `x+iy` and `x-iy`, while `Psi_y(2u)=4D_y(u)`,

\[
\boxed{
4\widehat D_y(2x)
=\Re\!\left(f'(x+iy)^2-f(x+iy)f''(x+iy)\right).
}
\]

Thus the direct G024 Fourier target is equivalently

\[
\boxed{
\Re\!\left(f'(x+iy)^2-f(x+iy)f''(x+iy)\right)>0
}
\]

for every real `x` and every `0<|y|<1/2`. This is the external Wronskian/Laguerre form of the Dimitrov–Xu frontier.

## 6. Complete-monotonicity sufficient route

Define the radial-square profile

\[
\boxed{H_y(q):=D_y(\sqrt q)=\cosh(2y\sqrt q)\,C(\sqrt q),\qquad q\ge0.}
\]

If

\[
\boxed{(-1)^mH_y^{(m)}(q)\ge0\quad\forall m\ge0,\ q\ge0,\quad 0<|y|<\frac12,}
\tag{CM}
\]

then Bernstein's theorem gives a positive measure `mu_y` such that

\[
H_y(q)=\int_0^\infty e^{-\lambda q}\,d\mu_y(\lambda).
\]

Consequently

\[
D_y(u)=\int_0^\infty e^{-\lambda u^2}\,d\mu_y(\lambda).
\]

Because the Riemann correlation kernel is integrable and decays at infinity, there is no non-zero constant component. Fourier transformation gives a positive Gaussian mixture,

\[
\widehat D_y(x)=\int_{(0,\infty)}\sqrt{\frac{\pi}{\lambda}}\exp\!\left(-\frac{x^2}{4\lambda}\right)\,d\mu_y(\lambda)>0.
\]

Therefore

\[
\boxed{(CM)\text{ for every }0<|y|<\frac12\Longrightarrow RH.}
\]

The implication is exact. Full complete monotonicity remains open, but its first derivative inequality is proved below.

## 7. Distinct internal tilt for the complex Jensen functional

There is a second exact kernel:

\[
\boxed{J_y(u):=\int_{\mathbb R}r^2\cosh(2yr)K(u+r)K(u-r)\,dr.}
\]

A direct two-variable change of variables gives

\[
\boxed{4\widehat J_y(2x)=|f'(x+iy)|^2-\Re\!\left(f''(x+iy)\overline{f(x+iy)}\right).}
\]

This is the internal complex Jensen/Laguerre functional. It is not the same as the external Wronskian form.

The distinction is essential:

\[
\boxed{D_y(u)=\cosh(2yu)C(u)\neq J_y(u)=\int r^2\cosh(2yr)K(u+r)K(u-r)\,dr}
\]

for general `y != 0`, while

\[
D_0=J_0=C.
\]

No later proof step may identify these two tilted families without an explicit additional identity.

## 8. Quantitative strong log-concavity already contained in SOH-G004

SOH-G004 writes the Riemann kernel as a positive theta-channel mixture and proves, uniformly for every channel and every non-negative argument,

\[
g_n''<-12.
\]

It also proves the global mixture-slope variance bound

\[
\operatorname{Var}_p(g_n')<2.
\]

The exact log-sum identity therefore gives

\[
(\log\Phi)''
=\sum_n p_ng_n''+\operatorname{Var}_p(g_n')
<-12+2=-10.
\]

Hence the even full-line kernel `K=Phi/2` satisfies

\[
\boxed{-(\log K)''>10.}
\]

Put

\[
L=-\log K.
\]

Then `L` is even and

\[
\boxed{L''>10.}
\]

This is a repository-internal quantitative consequence of the already-canonical G004 estimates; no external curvature constant is needed.

## 9. SOH-G024 first-order complete-monotonicity theorem

Differentiate the centered correlation:

\[
C'(u)
=-\int_{\mathbb R}r^2K(u+r)K(u-r)
\bigl[L'(u+r)+L'(u-r)\bigr]dr.
\]

For `u>0`, evenness of `L` gives

\[
L'(u-r)=-L'(r-u).
\]

Because `L''>10`, its derivative is strongly increasing with slope greater than ten, so

\[
L'(u+r)-L'(r-u)>10[(u+r)-(r-u)]=20u.
\]

Therefore

\[
\boxed{C'(u)<-20u\,C(u),\qquad u>0,}
\]

or equivalently

\[
\boxed{-\frac{C'(u)}{C(u)}>20u.}
\]

Now set `u=sqrt(q)`. Since

\[
D_y(u)=\cosh(2yu)C(u),
\]

we obtain

\[
-\frac{H_y'(q)}{H_y(q)}
=-\frac1{2u}\frac{D_y'(u)}{D_y(u)}
>10-\frac{|y|}{u}\tanh(2|y|u).
\]

Using `tanh(v)<v` for `v>0`,

\[
\boxed{
-\frac{H_y'(q)}{H_y(q)}
>10-2y^2
>\frac{19}{2}
}
\]

for every `q>0` and every `0<|y|<1/2`. The continuous limit at `q=0` obeys the same non-strict endpoint estimate. Consequently

\[
\boxed{H_y'(q)<0}
\]

globally. Thus the **first non-trivial complete-monotonicity inequality is proved** for the full Dimitrov–Xu strip.

This does not establish `H_y''>=0` or any higher-order complete-monotonicity inequality.

## 10. Gaussian domination corollary

Integrating the logarithmic-slope estimate gives, for `q>0`,

\[
\boxed{H_y(q)<H_y(0)e^{-19q/2}.}
\]

Equivalently,

\[
\boxed{D_y(u)<D_y(0)e^{-19u^2/2}\qquad(u\ne0).}
\]

This is a uniform Gaussian upper envelope for every external tilt in the open Dimitrov–Xu strip.

## 11. Second-order frontier

Define the positive logarithmic slope

\[
S_y(q):=-\frac{d}{dq}\log H_y(q).
\]

SOH-G024 proves

\[
\boxed{S_y(q)>\frac{19}{2}.}
\]

A direct differentiation gives the exact identity

\[
\boxed{
\frac{H_y''(q)}{H_y(q)}=S_y(q)^2-S_y'(q).
}
\]

Hence the next complete-monotonicity condition is exactly

\[
\boxed{H_y''(q)\ge0\iff S_y'(q)\le S_y(q)^2.}
\]

This Riccati-type inequality is the next analytic target. The first-order lower bound alone does not prove it.

## 12. Finite numerical diagnostic

The accompanying script evaluates `H_y(q)` with the repository Riemann kernel and applies symmetric five-point finite differences through order four on a small declared grid including values close to `|y|=1/2`.

The first-order sign is now independently proved analytically. Numerical signs at derivative orders two through four remain classified only as

`FINITE_DIAGNOSTIC_NOT_PROOF`.

## 13. Current proof obligation

The direct G024 route is now

\[
\boxed{
\text{G004 strong log-concavity}
\Longrightarrow H_y'<0\ \text{PROVED}
\longrightarrow H_y''\ge0\ \text{OPEN}
\longrightarrow \cdots
\longrightarrow H_y\text{ completely monotone}
\longrightarrow\widehat D_y>0
\longrightarrow\text{Wiener density}
\longrightarrow RH.
}
\]

The direct alternative target is the exact external Wronskian inequality

\[
\Re\!\left(f'(x+iy)^2-f(x+iy)f''(x+iy)\right)>0.
\]

## 14. Proof firewall

**EXACT / PROVED / EXTERNAL CLASSICAL:**

1. The Dimitrov–Xu density criterion stated above is RH-equivalent.
2. Wiener's theorem converts density of translates into absence of real Fourier zeros.
3. `nu_2(2u)=4C(u)` and `Psi_y(2u)=4D_y(u)` are exact changes of variables.
4. `hat(nu_2)=2(f'^2-ff'')` and the displayed external Wronskian identity are exact.
5. Complete monotonicity of every `H_y` is a sufficient condition for required strict Fourier positivity.
6. The internal-tilt identity for the complex Jensen functional is exact.
7. `D_y` and `J_y` are different families for general `y != 0`.
8. The canonical G004 estimates imply the quantitative full-kernel bound `-(log K)''>10`.
9. The first-order complete-monotonicity inequality `H_y'<0` is proved globally with uniform logarithmic-slope margin greater than `19/2`.
10. The Gaussian domination corollary follows exactly by integration.

**NUMERICAL ONLY:** finite sampled derivative signs at orders two through four.

**OPEN:** `H_y''>=0` globally, all higher complete-monotonicity inequalities, strict Fourier positivity for all real frequencies and all `0<|y|<1/2`, SOH-G003, SOH-C005, PF3, PF-infinity, and RH.
