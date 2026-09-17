# SOH — Theta/N-body Hermitian–bilinear rigidity audit v0.1

**Status:** EXACT IDENTITIES / ADVERSARIAL COMPUTATION PASS / RIEMANN EXTERNAL SIGN-CONFLICT QUARANTINED / RH OPEN  
**Branch:** `proof/theta-nbody-hermitian-bilinear-rigidity-v0.1`  
**Base:** `23eae95d8cbc33782c4a819ae40b2b166b566235`  
**Date:** 17 September 2026

## 1. Scope

This note records the theta transverse potential, the two-body free-energy geometry, and the exact separation between the external bilinear Wronskian quantity and the internal Hermitian Jensen quantity.

Nothing in this note proves or disproves the Riemann hypothesis. A high-precision sign conflict found for the external Riemann diagnostic is explicitly quarantined pending an independent source/convention audit.

This note is additive. It does not rewrite or silently promote any earlier SOH claim.

## 2. Fourier normalization

Let the even full-line Riemann kernel be

\[
K(t)=\frac12\Phi(|t|),
\]

and define

\[
f(z)=\int_{\mathbb R}K(t)e^{-izt}\,dt=\Xi(z)=\xi\!\left(\frac12+iz\right).
\]

Write

\[
z=x+iy,
\qquad
s=\frac12+iz=\frac12-y+ix.
\]

Hence the transverse displacement from the critical line is

\[
\delta=\Re s-\frac12=-y.
\]

## 3. Canonical theta transverse potential

For real \(\lambda\), define

\[
M(\lambda)=\int_{\mathbb R}K(t)e^{\lambda t}\,dt.
\]

Since \(K\) is positive and even,

\[
M(-\lambda)=M(\lambda)>0.
\]

Define

\[
\boxed{
\mathcal V_\Theta(y)
=\log\frac{M(y)M(-y)}{M(0)^2}.
}
\]

Cauchy–Schwarz gives

\[
M(y)M(-y)\ge M(0)^2.
\]

For a non-degenerate positive kernel equality holds only at \(y=0\). Therefore

\[
\boxed{
\mathcal V_\Theta(y)\ge0,
\qquad
\mathcal V_\Theta(y)=0\iff y=0.
}
\]

Let \(h=\log M\). Then

\[
h''(y)
=\frac{M''}{M}-\left(\frac{M'}M\right)^2
=\operatorname{Var}_y(t)>0,
\]

and

\[
\boxed{
\mathcal V_\Theta''(y)=h''(y)+h''(-y)>0.
}
\]

Thus the theta kernel supplies a canonical strictly convex transverse cost whose unique minimum is the critical line. This is a mathematical free-energy/potential object. No physical energy unit or particle-mass identification is asserted here.

## 4. Two-body generating function and real free-energy Hessian

Introduce center/relative parameters

\[
\alpha,\beta\in\mathbb R
\]

and

\[
\boxed{
\mathcal Z(\alpha,\beta)
=\frac12M(\alpha+\beta)M(\alpha-\beta).
}
\]

Let

\[
\mathcal F=\log\mathcal Z.
\]

Then

\[
\mathcal F_{\alpha\alpha}
= h''(\alpha+\beta)+h''(\alpha-\beta),
\]

\[
\mathcal F_{\beta\beta}=\mathcal F_{\alpha\alpha},
\]

\[
\mathcal F_{\alpha\beta}
= h''(\alpha+\beta)-h''(\alpha-\beta),
\]

and therefore

\[
\boxed{
\det\nabla^2\mathcal F
=4h''(\alpha+\beta)h''(\alpha-\beta)>0.
}
\]

The real two-body free energy is therefore strictly convex.

The receipt evaluates, at \((\alpha,\beta)=(0.3,0.1)\),

\[
\det\nabla^2\mathcal F
\approx 8.533214645620778\times10^{-3}>0.
\]

## 5. External bilinear and internal Hermitian quantities are different

Define

\[
\boxed{
E(z)=\Re\!\left(f'(z)^2-f(z)f''(z)\right)
}
\]

and

\[
\boxed{
H(z)=|f'(z)|^2
-\Re\!\left(f''(z)\overline{f(z)}\right).
}
\]

They coincide on the real axis for a real entire \(f\), but are different for general complex \(z\).

The repository G024 external correlation route uses the bilinear object \(E\). The complex Laguerre/Jensen inequality uses the Hermitian object \(H\). They must never be identified without an additional theorem.

External references used for the audit:

- D. K. Dimitrov and Y. Xu, *Wronskians of Fourier and Laplace Transforms*, Trans. AMS 372 (2019), arXiv:1606.05011. Its Theorem 1.1 explicitly states the external tilted correlation kernel \(\Phi_{2,y}(t)=\cosh(ty)\nu_2(t)\).
- G. Csordas and A. Escassut, *The Laguerre inequality and the distribution of zeros of entire functions*, Ann. Math. Blaise Pascal 12 (2005), for the complex/Hermitian Laguerre inequality.

This source check corrects an earlier conversational overreach: the external Dimitrov–Xu route is **not declared wrong** in this repository update.

## 6. Exact adversarial tent-kernel control

Take

\[
K_\triangle(t)=\frac{2-|t|}{4}\,\mathbf 1_{|t|\le2}.
\]

Its Fourier transform is

\[
\boxed{
f_\triangle(z)=\left(\frac{\sin z}{z}\right)^2.}
\]

Direct exact piecewise integration gives its order-two correlation. With \(a=|t|\),

\[
\nu_2(t)=
\begin{cases}
\dfrac{3a^5-20a^4+80a^3-160a^2+256}{480},&0\le a\le2,\\[6pt]
\dfrac{(4-a)^5}{480},&2\le a\le4,\\[6pt]
0,&a>4.
\end{cases}
\]

For

\[
\Psi_y(t)=\cosh(yt)\nu_2(t),
\]

the exact Fourier/Wronskian normalization is

\[
\boxed{
\widehat\Psi_y(x)=2E(x+iy).
}
\]

At

\[
y=0.1,
\qquad
x=\pi,
\]

the independent piecewise-polynomial quadrature gives

\[
\widehat\Psi_{0.1}(\pi)
=-0.000408260137624939349527856298856\ldots
\]

while

\[
E(\pi+0.1i)
=-0.000204130068812469674763928149428\ldots
\]

and the identity residual at 100-digit working precision is approximately

\[
1.05\times10^{-104}.
\]

At the same point,

\[
H(\pi+0.1i)
=0.000623131997394436068710492228236\ldots>0.
\]

Therefore the adversarial control proves only the following:

\[
\boxed{
H(z)>0\ \not\Rightarrow\ E(z)>0
}
\]

without additional hypotheses. The example has multiple real zeros, so it is not used as a counterexample to any simplicity-sensitive theorem.

## 7. Riemann high-precision conflict diagnostic — QUARANTINED

Using directly

\[
\Xi(z)=\xi\!\left(\frac12+iz\right)
\]

with 100-digit arithmetic, the receipt records for

\[
y=0.499
\]

that

\[
E(110+0.499i)
=8.4000005444218380783955\ldots\times10^{-68}>0,
\]

whereas

\[
E(111+0.499i)
=-5.7790891317437284950868\ldots\times10^{-69}<0.
\]

At both endpoints the Hermitian quantity remains positive:

\[
H(110+0.499i)>0,
\qquad
H(111+0.499i)>0.
\]

This sign change is stable under the committed 100-digit computation, but its interpretation is deliberately quarantined.

Combining it naively with the published Dimitrov–Xu density criterion and Wiener would have major consequences. Therefore **no such consequence is asserted** until all of the following have been independently rechecked:

1. the published theorem and its proof, including Fourier-sign conventions;
2. every scaling factor between \(\Phi_{2,y}\), \(D_y\), and the repository transform;
3. direct correlation-kernel quadrature independent of differentiation of \(\Xi\);
4. an interval/arbitrary-precision enclosure of the sign change;
5. independent reproduction outside the present code path.

Current classification:

`FINITE_HIGH_PRECISION_DIAGNOSTIC_REQUIRES_INDEPENDENT_SOURCE_CONVENTION_AUDIT`.

It is **not** classified as evidence for either RH or not-RH.

## 8. Numerical receipt

The deterministic runner

`python scripts/run_soh_theta_nbody_rigidity.py`

writes

`reports/SOH_THETA_NBODY_RIGIDITY_RECEIPT_V0_1.json`.

The corresponding adversarial test module is

`tests/test_theta_nbody_rigidity.py`.

Fresh branch-local validation before writeback:

```text
7 passed
```

## 9. Proof firewall

**EXACT / PROVED FROM THE DISPLAYED DEFINITIONS**

1. \(\mathcal V_\Theta\ge0\) and its unique exact minimum at \(y=0\) for a non-degenerate positive kernel.
2. Strict real convexity of \(\log\mathcal Z\).
3. The algebraic distinction between \(E\) and \(H\).
4. The exact tent transform and the piecewise polynomial \(\nu_2\).
5. The external tent Fourier/Wronskian identity.

**FINITE COMPUTATION / PASS**

1. sampled positive theta-potential values away from zero;
2. sampled positive-definite N-body Hessian;
3. tent external-negative / Hermitian-positive separation;
4. 7/7 adversarial tests.

**QUARANTINED**

1. the Riemann external sign-change bracket at \(y=0.499\).

**OPEN**

1. independent resolution of the external-sign conflict;
2. a full potential selecting the Riemann zero heights;
3. any theorem mapping the theta potential to physical mass/energy units;
4. RH.
