# SOH-G024 — Super-exponential route closure for full complete monotonicity

**Status:** THEOREM-LEVEL ROUTE NO-GO / PROVED ON THIS BRANCH / CANONICAL REVIEW PENDING  
**Scope:** the sufficient full complete-monotonicity route of SOH-G024  
**Source main:** `a759a64c498d5ab6b31fb8566969dcf0716feb59`  
**GREMLIN/OCTOPUS route commitment:** `e3c87b815d509699850802b500d7acdd87ce717a91216969141c4b3d13326f11`  
**GREMLIN route:** `OWL + MOLE + HOUND`  
**Authority:** candidate analysis only; `canon_allowed=false`

## 1. Question isolated by GREMLIN

SOH-G024 introduces, for every fixed `0<|y|<1/2`,

\[
D_y(u)=\cosh(2yu)C(u),
\qquad
C(u)=\int_{\mathbb R}r^2K(u+r)K(u-r)\,dr,
\]

and

\[
H_y(q)=D_y(\sqrt q),\qquad q\ge0.
\]

The existing sufficient route is

\[
H_y\ \text{completely monotone}
\Longrightarrow
D_y\ \text{positive Gaussian mixture}
\Longrightarrow
\widehat D_y>0.
\]

The direct Fourier/Wiener condition `\widehat D_y>0` is the external RH-equivalent target already recorded by G024. The present theorem audits only the stronger sufficient complete-monotonicity route.

## 2. Elementary tail bound for the Riemann kernel

The canonical positive half-line kernel is

\[
\Phi(t)
=
4\sum_{n\ge1}\pi n^2 e^{5t/2}
\left(2\pi n^2e^{2t}-3\right)
 e^{-\pi n^2e^{2t}},
\qquad t\ge0,
\]

and the full-line kernel is

\[
K(t)=\frac12\Phi(|t|).
\]

For `t>=0`, put `x=e^{2t}>=1`. Since every summand is positive and

\[
2\pi n^2x-3<2\pi n^2x,
\]

we obtain

\[
\Phi(t)
<8\pi^2e^{9t/2}
\sum_{n\ge1}n^4e^{-\pi n^2x}.
\]

Define the finite positive constant

\[
A:=\sum_{n\ge1}n^4e^{-\pi(n^2-1)}<\infty.
\]

Because `x>=1`,

\[
e^{-\pi n^2x}
=e^{-\pi x}e^{-\pi(n^2-1)x}
\le e^{-\pi x}e^{-\pi(n^2-1)}.
\]

Therefore

\[
\boxed{
K(t)
<4\pi^2A\,e^{9t/2}e^{-\pi e^{2t}}
\qquad(t\ge0).
}
\tag{1}
\]

Thus the kernel has a double-exponential tail in the physical `t` coordinate.

## 3. Strong convexity bounds the centered correlation

The sharpened G024 curvature theorem proves

\[
L(t):=-\log K(t),
\qquad
\boxed{L''(t)>17}
\]

on the full real line.

For any real `u,r`, the symmetric second difference satisfies

\[
L(u+r)+L(u-r)-2L(u)
=
\int_0^{|r|}(|r|-v)
\bigl[L''(u+v)+L''(u-v)\bigr]\,dv
>17r^2.
\]

Hence

\[
\boxed{
K(u+r)K(u-r)<K(u)^2e^{-17r^2}.
}
\tag{2}
\]

Multiplication by `r^2` and integration give

\[
C(u)
< K(u)^2
\int_{\mathbb R}r^2e^{-17r^2}\,dr
=
\frac{\sqrt\pi}{2\,17^{3/2}}K(u)^2.
\]

Thus, for `u>=0` and `0<|y|<1/2`,

\[
H_y(u^2)=D_y(u)
<
\frac{\sqrt\pi}{2\,17^{3/2}}
\cosh(2|y|u)K(u)^2.
\]

Since `cosh(2|y|u)<=e^u`, equation (1) yields a finite constant `B>0`, independent of `u`, such that

\[
\boxed{
H_y(u^2)
< B\,e^{10u}e^{-2\pi e^{2u}}.
}
\tag{3}
\]

Equivalently, with `q=u^2`,

\[
\boxed{
\forall T>0:\qquad
\lim_{q\to\infty}e^{Tq}H_y(q)=0.
}
\tag{4}
\]

So every external G024 profile `H_y` decays faster than every ordinary exponential in `q`.

## 4. Bernstein lower-envelope lemma

Let `h:[0,\infty)\to(0,\infty)` be a nonzero completely monotone function with finite `h(0)`. By the Hausdorff--Bernstein--Widder theorem,

\[
h(q)=\int_{[0,\infty)}e^{-\lambda q}\,d\mu(\lambda)
\]

for a finite nonzero positive measure `mu`.

Because

\[
[0,\infty)=\bigcup_{N=1}^{\infty}[0,N]
\]

and `mu` is nonzero, there exists a finite `N` for which

\[
\mu([0,N])>0.
\]

Consequently

\[
h(q)
\ge
\int_{[0,N]}e^{-\lambda q}\,d\mu(\lambda)
\ge
\mu([0,N])e^{-Nq},
\]

and therefore

\[
\boxed{
e^{Nq}h(q)\ge\mu([0,N])>0
\qquad(q\ge0).
}
\tag{5}
\]

A nonzero completely monotone function with finite value at the origin therefore cannot decay faster than every exponential.

## 5. Main theorem

### Theorem — G024 full complete-monotonicity route closure

For every fixed

\[
0<|y|<\frac12,
\]

the canonical G024 profile

\[
H_y(q)=D_y(\sqrt q)
\]

is **not** completely monotone on `[0,\infty)`.

### Proof

Assume that `H_y` is completely monotone. It is positive and finite at `q=0`, so the Bernstein lower-envelope lemma applies. Hence there is a finite `N` such that

\[
e^{Nq}H_y(q)\ge c>0
\]

for every `q>=0`.

But the Riemann-kernel tail and the strong-convexity correlation estimate give equation (4), in particular

\[
e^{Nq}H_y(q)\longrightarrow0.
\]

Contradiction. Therefore `H_y` cannot be completely monotone. QED.

## 6. Consequence for the derivative hierarchy

G024 has already established globally

\[
H_y'(q)<0,
\qquad
H_y''(q)>0
\]

for every `q>=0` and every `0<|y|<1/2` at the declared repository certificate level.

The theorem above implies that, for each fixed admissible `y`, the complete sign hierarchy must fail at some later order. Thus there exist

\[
m\ge3,
\qquad q\ge0,
\]

such that

\[
\boxed{(-1)^mH_y^{(m)}(q)<0.}
\]

The first and second G024 results remain intact. What closes is the extrapolation from those first two signs to complete monotonicity of all orders.

## 7. Proof-graph update

The branch should therefore be represented as

\[
\boxed{
\text{G024 full complete monotonicity}
\;\longrightarrow\;
\text{CLOSED ROUTE / NO-GO}
}
\]

while the direct one-dimensional target remains

\[
\boxed{
\widehat D_y(x)>0
\quad\forall x\in\mathbb R,
\quad 0<|y|<\frac12.
}
\]

The corresponding Wronskian form remains

\[
\boxed{
\Re\!\left(f'(x+iy)^2-f(x+iy)f''(x+iy)\right)>0.
}
\]

The appropriate next search surface is therefore direct one-dimensional positive definiteness / Fourier positivity, rather than an all-dimensions Gaussian-mixture certificate.

## 8. GREMLIN audit provenance

OCTOPUS v0.5 routed the audit to:

- `OWL` — source/provenance and epistemic-boundary verification;
- `MOLE` — analytic derivation of the tail/representation contradiction;
- `HOUND` — attempted falsification of the complete-monotonicity route.

The deterministic route commitment is

`e3c87b815d509699850802b500d7acdd87ce717a91216969141c4b3d13326f11`.

GREMLIN has no canonical promotion authority. Promotion, if any, requires the repository's normal review and validation gates.

## 9. Source bindings

This theorem uses only already-present SOH objects:

- `research/SOH_G024_JENSEN_WIENER_KERNEL_V0_1.md` — definitions of `K,C,D_y,H_y`, Bernstein sufficient route, and direct Fourier target;
- `research/SOH_G024_SHARPENED_CURVATURE_SECOND_ORDER_V0_1.md` — analytic `L''>17` theorem;
- `research/SOH_G024_GLOBAL_SECOND_ORDER_V0_1.md` — current second-order closure status;
- `src/secret_of_a_half/riemann_kernel.py` — exact canonical theta-kernel formula;
- `research/SOH_G024_THIRD_ORDER_CUMULANT_FRONTIER_V0_1.md` — current `m>=3` frontier.

RH status remains governed by the existing canonical claim ledger and the direct RH-equivalent Fourier/Wiener criterion.