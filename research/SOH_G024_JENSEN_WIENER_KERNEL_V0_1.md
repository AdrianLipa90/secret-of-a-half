# SOH-G024 — Jensen–Wiener correlation kernel and complete-monotonicity target

**Status:** EXACT REPARAMETRIZATION / EXACT SUFFICIENT ROUTE / GLOBAL COMPLETE MONOTONICITY OPEN / RH OPEN  
**Branch:** `proof/soh-g024-jensen-kernel-positive-definite-v1`  
**Date:** 19 August 2026

## 1. Scope

This generation leaves the PF3 staircase and returns directly to an RH-equivalent correlation-kernel criterion. It also corrects a potential conflation between two different `y`-tilts which coincide at `y=0` but are different for `y != 0`.

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

## 5. Complete-monotonicity sufficient route

Define the radial-square profile

\[
\boxed{H_y(q):=D_y(\sqrt q)=\cosh(2y\sqrt q)\,C(\sqrt q),\qquad q\ge0.}
\]

Consider the following open property:

\[
\boxed{(-1)^mH_y^{(m)}(q)\ge0\quad\forall m\ge0,\ q\ge0,\quad 0<|y|<\frac12.}
\tag{CM}
\]

If (CM) holds, Bernstein's theorem gives a positive measure `mu_y` such that

\[
H_y(q)=\int_0^\infty e^{-\lambda q}\,d\mu_y(\lambda).
\]

Consequently

\[
D_y(u)=\int_0^\infty e^{-\lambda u^2}\,d\mu_y(\lambda).
\]

Because the Riemann correlation kernel is integrable and decays at infinity, there is no non-zero constant component. Hence the representing mass relevant to the non-zero kernel lies on `lambda>0`. Fourier transformation gives a positive Gaussian mixture,

\[
\widehat D_y(x)=\int_{(0,\infty)}\sqrt{\frac{\pi}{\lambda}}\exp\!\left(-\frac{x^2}{4\lambda}\right)\,d\mu_y(\lambda)>0.
\]

Therefore

\[
\boxed{(CM)\text{ for every }0<|y|<\frac12\Longrightarrow RH.}
\]

This implication is exact. The premise (CM) is **OPEN**.

## 6. The `y=0` slice

At `y=0`,

\[
D_0(u)=C(u).
\]

This is the centered order-two correlation kernel associated with the first Laguerre/Csordas frontier. The branch does not infer the `y != 0` family from the `y=0` case.

## 7. Distinct internal tilt for the complex Jensen functional

There is a second exact kernel:

\[
\boxed{J_y(u):=\int_{\mathbb R}r^2\cosh(2yr)K(u+r)K(u-r)\,dr.}
\]

Let

\[
f(z)=\int_{\mathbb R}K(t)e^{-izt}\,dt.
\]

A direct two-variable change of variables gives

\[
\boxed{4\widehat J_y(2x)=|f'(x+iy)|^2-\Re\!\left(f''(x+iy)\overline{f(x+iy)}\right).}
\]

This is the complex Jensen/Laguerre functional in Fourier-correlation form. The derivation is independent of the external Dimitrov–Xu tilt.

The distinction is essential:

\[
\boxed{D_y(u)=\cosh(2yu)C(u)\neq J_y(u)=\int r^2\cosh(2yr)K(u+r)K(u-r)\,dr}
\]

for general `y != 0`, while

\[
D_0=J_0=C.
\]

No later proof step may identify these two tilted families without an explicit additional identity.

## 8. Exact monotonicity inherited from strict log-concavity

Assume the full even kernel `K` is positive and strictly log-concave. Write `ell=log K`. Differentiating with respect to `u` gives the correct identity

\[
\frac{\partial}{\partial u}[K(u+r)K(u-r)]
=K(u+r)K(u-r)[\ell'(u+r)+\ell'(u-r)].
\]

For `u>0` it is enough, by evenness in `r`, to consider `r>=0`.

If `0<=r<=u`, both `u+r` and `u-r` are non-negative and strict log-concavity of the even kernel makes `ell'` negative away from zero, so the sum is strictly negative except at a null boundary case.

If `r>u`, evenness gives `ell'(u-r)=-ell'(r-u)`. Since `u+r>r-u>=0` and `ell'` is strictly decreasing on the positive half-line,

\[
\ell'(u+r)-\ell'(r-u)<0.
\]

Thus in both regions the derivative of the product is negative for `u>0` almost everywhere in `r`. Integrating against `r^2` yields

\[
\boxed{C'(u)<0\quad(u>0).}
\]

Hence `C` is positive, even and strictly decreasing on the positive half-line. This does **not** by itself imply positive definiteness or complete monotonicity of `H_y`.

For the external tilt,

\[
D_y'(u)=\cosh(2yu)C'(u)+2y\sinh(2yu)C(u),
\]

so even first-order monotonicity of `D_y` requires a quantitative decay bound on `C`; it does not follow from `C'<0` alone.

## 9. Finite numerical diagnostic

The accompanying script evaluates `H_y(q)` with the repository Riemann kernel and applies symmetric five-point finite differences through order four on a small declared grid including values close to `|y|=1/2`.

Any observed sign pattern is recorded only as

`FINITE_DIAGNOSTIC_NOT_PROOF`.

Finite differences do not prove complete monotonicity, do not prove positive definiteness, and do not prove RH.

## 10. Current proof obligation

The direct G024 route is now:

\[
\boxed{\text{Riemann theta kernel}\longrightarrow H_y(q)=\cosh(2y\sqrt q)C(\sqrt q)\longrightarrow H_y\text{ completely monotone}\longrightarrow\widehat D_y>0\longrightarrow\text{Wiener density}\longrightarrow RH.}
\]

Only the first definition and the final implications are established here. The global complete-monotonicity step remains open.

## 11. Proof firewall

**EXACT / EXTERNAL CLASSICAL:**

1. The Dimitrov–Xu density criterion stated above is RH-equivalent.
2. Wiener's theorem converts density of translates into absence of real Fourier zeros.
3. `nu_2(2u)=4C(u)` and `Psi_y(2u)=4D_y(u)` are exact changes of variables.
4. Complete monotonicity of every `H_y` is a sufficient condition for the required strict Fourier positivity.
5. The internal-tilt identity for the complex Jensen functional is exact.
6. `D_y` and `J_y` are different families for general `y != 0`.
7. Under the stated strict log-concavity/evenness assumptions, `C'(u)<0` for `u>0` follows from the corrected derivative identity with a **sum** of logarithmic derivatives.

**NUMERICAL ONLY:** finite sampled derivative signs of `H_y`.

**OPEN:** complete monotonicity of `H_y` for the actual Riemann kernel, strict Fourier positivity for all real frequencies and all `0<|y|<1/2`, SOH-G003, SOH-C005, PF3, PF-infinity, and RH.
