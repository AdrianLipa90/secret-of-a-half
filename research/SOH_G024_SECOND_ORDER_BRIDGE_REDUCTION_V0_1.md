# SOH-G024 — Second-order bridge-measure curvature–variance reduction

**Status:** EXACT REDUCTION / SECOND-ORDER SIGN OPEN / RH OPEN  
**Branch:** `proof/soh-g024-jensen-kernel-positive-definite-v1`  
**Date:** 19 August 2026

## 1. Scope

SOH-G024 already proves the first non-trivial complete-monotonicity inequality

\[
H_y'(q)<0,
\qquad
-\frac{H_y'(q)}{H_y(q)}>\frac{19}{2},
\]

for the actual Riemann kernel, every `q>0`, and every `0<|y|<1/2`.

This note reduces the next condition `H_y''>=0` to an exact curvature–variance identity under a normalized correlation measure. The identity is exact; its global sign is not proved here.

## 2. Correlation measure

Let

\[
C(u)=\int_{\mathbb R}r^2K(u+r)K(u-r)\,dr,
\]

and write

\[
L=-\log K.
\]

For `u>0` define the probability measure

\[
\boxed{
 d\mu_u(r)
 =\frac{r^2K(u+r)K(u-r)}{C(u)}\,dr.
}
\]

Define the bridge slope and bridge curvature observables

\[
\boxed{
 A_u(r)=L'(u+r)+L'(u-r),
}
\]

and

\[
\boxed{
 B_u(r)=L''(u+r)+L''(u-r).
}
\]

## 3. Exact logarithmic derivative identities

Differentiating the correlation under the integral sign gives

\[
C'(u)
=-\int A_u(r)\,r^2K(u+r)K(u-r)\,dr.
\]

Hence

\[
\boxed{
 R(u):=-\frac{C'(u)}{C(u)}
 =\mathbb E_{\mu_u}[A_u].
}
\]

For any integrable observable `F_u`, differentiation of the normalized bridge expectation gives

\[
\frac{d}{du}\mathbb E_{\mu_u}[F_u]
=\mathbb E_{\mu_u}[\partial_uF_u]
-\operatorname{Cov}_{\mu_u}(F_u,A_u).
\]

Taking `F_u=A_u` and using `partial_u A_u=B_u` yields

\[
\boxed{
R'(u)
=\mathbb E_{\mu_u}[B_u]
-\operatorname{Var}_{\mu_u}(A_u).
}
\]

This identity isolates the competition between mean bridge curvature and slope variance.

## 4. External tilt and first-order surplus

Put

\[
a=|y|,
\qquad
T_y(u)=2a\tanh(2au),
\]

and define

\[
\boxed{
N_y(u)=R(u)-T_y(u).
}
\]

Because

\[
D_y(u)=\cosh(2yu)C(u),
\]

we have

\[
\boxed{
-\frac{D_y'(u)}{D_y(u)}=N_y(u).
}
\]

The proved first-order theorem gives

\[
\boxed{N_y(u)>19u.}
\]

Also

\[
\boxed{
T_y'(u)=4a^2\operatorname{sech}^2(2au).
}
\]

## 5. Exact second-order normal form

Since `q=u^2` and `H_y(q)=D_y(u)`, direct differentiation gives

\[
H_y''(q)
=\frac{uD_y''(u)-D_y'(u)}{4u^3}.
\]

Therefore

\[
\boxed{
H_y''(q)\ge0
\iff
uD_y''(u)-D_y'(u)\ge0.
}
\]

Using

\[
\frac{D_y''}{D_y}
=N_y^2-N_y'
=N_y^2-R'+T_y',
\]

and the bridge identity for `R'`, one obtains

\[
\boxed{
\frac{4u^3H_y''(u^2)}{H_y(u^2)}
=N_y(u)
+u\left[
N_y(u)^2
+\operatorname{Var}_{\mu_u}(A_u)
-\mathbb E_{\mu_u}[B_u]
+4a^2\operatorname{sech}^2(2au)
\right].
}
\]

Thus the second complete-monotonicity condition is exactly equivalent to non-negativity of the right-hand side.

## 6. Equivalent Riccati form

Define

\[
S_y(q)=-\frac{d}{dq}\log H_y(q).
\]

Since

\[
S_y(u^2)=\frac{N_y(u)}{2u},
\]

we recover

\[
\boxed{
\frac{H_y''}{H_y}=S_y^2-S_y'.
}
\]

Hence

\[
\boxed{
H_y''\ge0
\iff
S_y'\le S_y^2.
}
\]

The bridge-measure formula is the expanded curvature–variance form of this Riccati condition.

## 7. Sign structure

The reduction separates four contributions:

1. `N_y>0`, already proved with `N_y>19u`;
2. `N_y^2>0`, a positive quadratic surplus;
3. `Var(A_u)>=0`, a positive fluctuation contribution;
4. `-E[B_u]`, the only explicitly negative bridge-curvature term, partly offset by the positive tilt-curvature term `4a^2 sech^2(2au)`.

The canonical G004 bound `L''>10` implies

\[
B_u(r)>20,
\]

but this is a lower bound on `E[B_u]`, whereas the second-order normal form requires sufficient control of its size relative to the positive terms. Strong log-concavity alone therefore does not close the second-order inequality.

## 8. Gaussian regression fixture

For

\[
K(t)=e^{-t^2/2},
\qquad
L(t)=\frac{t^2}{2},
\]

we have exactly

\[
A_u(r)=2u,
\qquad
B_u(r)=2,
\qquad
\operatorname{Var}(A_u)=0.
\]

The implemented bridge formula agrees to high precision with direct differentiation of

\[
H_y(q)=\frac{\sqrt\pi}{2}e^{-q}\cosh(2y\sqrt q).
\]

This is a regression of the identity, not evidence for the Riemann-kernel sign.

## 9. Current proof obligation

The exact second-order target is now

\[
\boxed{
N_y
+u\left[N_y^2+\operatorname{Var}(A_u)-\mathbb E[B_u]
+4a^2\operatorname{sech}^2(2au)\right]\ge0
}
\]

for every `u>0` and `0<a<1/2`.

Equivalent routes are:

- prove a sharp upper bound on `E[B_u]-Var(A_u)=R'(u)` compatible with the already-proved lower bound on `N_y`;
- prove the Riccati inequality `S_y'<=S_y^2` directly;
- prove `uD_y''-D_y'>=0` directly from the Riemann theta-channel expansion.

## 10. Proof firewall

**PROVED / EXACT:** the bridge probability measure, `R=E[A]`, `R'=E[B]-Var(A)`, the external-tilt surplus `N`, the `uD''-D'` reduction, and the boxed curvature–variance identity.

**PROVED FROM EARLIER G024:** `N_y(u)>19u` and global `H_y'<0`.

**NUMERICAL ONLY:** sampled positivity of higher finite-difference derivatives.

**OPEN:** the global sign of the second-order margin, `H_y''>=0`, all higher complete-monotonicity inequalities, strict external Fourier positivity, SOH-G003, SOH-C005, PF3, PF-infinity, and RH.
