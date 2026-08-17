# SOH-C005 decay-schedule candidate v0.2

Status: **OPEN CANDIDATE — NOT PROMOTED**

This note separates integral-test validity from actual asymptotic decay of the prime-tail majorant.

For one degree-`d` logarithmic tail term, the continuous majorant contains

\[
 u^{d+1}\exp\!\left(-\frac{u^2}{4w^2}+\frac{u}{2}\right),
 \qquad u=\log x.
\]

The exact monotonicity threshold already implemented in the repository is

\[
 t_d=\frac{\sqrt{w^4+8w^2(d+1)}-w^2}{2}=O(\sqrt d).
\]

Choosing `log Q` only just above `t_d` certifies that the integral test is legal. It does **not** by itself certify that the resulting growing-degree envelope tends to zero.

A stronger candidate schedule is

\[
 u_d:=\log Q_d=c\sqrt{d\log(d+2)},
 \qquad c>\sqrt{2}\,w.
\]

At this scale,

\[
 -\frac{u_d^2}{4w^2}
 =-\frac{c^2}{4w^2}d\log(d+2),
\]

while

\[
 (d+1)\log u_d
 =\frac12d\log d+O(d\log\log d).
\]

Therefore the Gaussian exponent beats the bare polynomial factor whenever

\[
 \frac{c^2}{4w^2}>\frac12,
 \quad\text{i.e.}\quad c>\sqrt2\,w.
\]

This comparison is **not yet a proof for the complete Hermite entry bound**. The remaining work is to include, uniformly in the Hermite orders, the exact normalization

\[
 \bigl(2^m m!\,2^n n!\bigr)^{-1/2}
\]

and the linearization coefficients

\[
 2^k k!\binom{m}{k}\binom{n}{k},
\]

then prove a summable bound on the rectangular row/column envelopes required for

\[
 \|P_N T_{\rm tail}(I-P_N)\|.
\]

## Claim boundary

Exact:
- the displayed asymptotic comparison for the isolated `u^(d+1)` Gaussian tail factor;
- `c > sqrt(2) w` makes the Gaussian `d log d` coefficient stronger than the bare polynomial `d log d` coefficient.

Open:
- a uniform bound including all Hermite linearization coefficients;
- summability over the infinite right Hermite index;
- vanishing of the full prime-tail cross-block norm;
- retained-prime, archimedean, pole/conductor and localization contributions to the full `epsilon_{N,a}`;
- positive lower bound `nu_{N,a}`;
- SOH-C005;
- RH.

`proof_of_rh = false`.
