# SOH-G024 — Third-order bridge cumulant frontier

**Status:** EXACT REDUCTION / THIRD COMPLETE-MONOTONICITY SIGN OPEN / RH OPEN  
**Branch:** `proof/soh-g024-jensen-kernel-positive-definite-v1`  
**Date:** 19 August 2026

## 1. Scope

SOH-G024 already proves, for every external Dimitrov–Xu tilt with `0<|y|<1/2`,

\[
H_y'(q)<0,
\qquad
H_y''(q)>0
\]

for every `q>=0`.  The second inequality uses the explicit SOH-G024-Q computer-assisted fourth-log-curvature certificate on the former compact core and analytic bounds outside it.

This note derives the exact next condition

\[
-H_y'''(q)\ge0.
\]

It does not prove its global sign.

## 2. Logarithmic-slope recurrence

Let

\[
S_y(q)=-\frac{d}{dq}\log H_y(q).
\]

For

\[
F_m(q):=(-1)^m\frac{H_y^{(m)}(q)}{H_y(q)},
\]

direct differentiation gives the exact recurrence

\[
\boxed{F_{m+1}=S_yF_m-F_m'.}
\]

Thus

\[
F_1=S_y,
\]

\[
F_2=S_y^2-S_y',
\]

and

\[
\boxed{
F_3=S_y^3-3S_yS_y'+S_y''.
}
\]

The first two quantities are globally positive on G024.  The third remains open.

## 3. Radial form

Write

\[
q=u^2,
\qquad
H_y(q)=D_y(u).
\]

Repeated use of

\[
\frac{d}{dq}=\frac1{2u}\frac{d}{du}
\]

gives

\[
H_y'''(u^2)
=
\frac{u^2D_y'''(u)-3uD_y''(u)+3D_y'(u)}{8u^5}.
\]

Hence

\[
\boxed{
-H_y'''(u^2)\ge0
\iff
-u^2D_y'''+3uD_y''-3D_y'\ge0.
}
\]

## 4. External logarithmic slope

Recall

\[
D_y(u)=\cosh(2yu)C(u),
\]

\[
R(u)=-\frac{C'(u)}{C(u)},
\]

\[
T_y(u)=2a\tanh(2au),
\qquad a=|y|,
\]

and

\[
\boxed{N_y(u)=R(u)-T_y(u)=-\frac{D_y'(u)}{D_y(u)}.}
\]

Then

\[
\frac{D_y''}{D_y}=N_y^2-N_y'
\]

and

\[
\frac{D_y'''}{D_y}=-N_y^3+3N_yN_y'-N_y''.
\]

Substitution into the radial identity yields

\[
\boxed{
8u^5\frac{-H_y'''(u^2)}{H_y(u^2)}
=
 u^2N_y^3
 -3u^2N_yN_y'
 +u^2N_y''
 +3uN_y^2
 -3uN_y'
 +3N_y.
}
\]

This is the exact third-order radial normal form.

## 5. Bridge differentiation calculus

Under the normalized bridge measure

\[
d\mu_u(r)
=\frac{r^2K(u+r)K(u-r)}{C(u)}\,dr,
\]

define

\[
A_u(r)=L'(u+r)+L'(u-r),
\]

\[
B_u(r)=L''(u+r)+L''(u-r),
\]

and the third bridge observable

\[
\boxed{
C_u^{(3)}(r)=L'''(u+r)+L'''(u-r).
}
\]

For any differentiable observable `G_u`,

\[
\frac{d}{du}\mathbb E_{\mu_u}[G_u]
=
\mathbb E_{\mu_u}[\partial_uG_u]
-\operatorname{Cov}_{\mu_u}(G_u,A_u).
\]

The already-used identities are

\[
R=\mathbb E[A_u]
\]

and

\[
R'=\mathbb E[B_u]-\operatorname{Var}(A_u).
\]

Differentiating once more gives

\[
\frac{d}{du}\mathbb E[B_u]
=
\mathbb E[C_u^{(3)}]
-\operatorname{Cov}(A_u,B_u).
\]

Also

\[
\frac{d}{du}\operatorname{Var}(A_u)
=
2\operatorname{Cov}(A_u,B_u)-\mu_3(A_u),
\]

where

\[
\mu_3(A_u)
=
\mathbb E\!\left[(A_u-\mathbb E[A_u])^3\right].
\]

Therefore

\[
\boxed{
R''
=
\mathbb E[C_u^{(3)}]
-3\operatorname{Cov}(A_u,B_u)
+\mu_3(A_u).
}
\]

This is the exact third-order bridge cumulant identity.

## 6. Tilt derivatives

For

\[
T_y(u)=2a\tanh(2au)
\]

one has

\[
\boxed{T_y'(u)=4a^2\operatorname{sech}^2(2au)}
\]

and

\[
\boxed{
T_y''(u)
=-16a^3\operatorname{sech}^2(2au)\tanh(2au).
}
\]

Thus

\[
N_y'=R'-T_y'
\]

and

\[
N_y''=R''-T_y''.
\]

The tilt contribution `-T_y''` is non-negative for `u>=0`.

## 7. Second-margin growth form

Define the normalized second-order margin

\[
\boxed{
M_2(u):=N_y+u(N_y^2-N_y').
}
\]

so that

\[
M_2(u)=4u^3\frac{H_y''(u^2)}{H_y(u^2)}>0.
\]

Differentiation gives an exact cancellation:

\[
\boxed{
M_2'(u)
=N_y^2+u(2N_yN_y'-N_y'').
}
\]

The third-order normal form is equivalently

\[
\boxed{
8u^5\frac{-H_y'''(u^2)}{H_y(u^2)}
=(uN_y+3)M_2-uM_2'.
}
\]

Since `M_2>0` is globally proved, the third-order problem is equivalently the logarithmic-growth inequality

\[
\boxed{
\frac{uM_2'(u)}{M_2(u)}\le uN_y(u)+3.
}
\]

No such global bound is claimed here.

## 8. Current obstruction

The exact bridge formula shows that the new uncontrolled structure is not merely a single pointwise derivative of `L`.  It contains the coupled combination

\[
\boxed{
\mathbb E[C_u^{(3)}]
-3\operatorname{Cov}(A_u,B_u)
+\mu_3(A_u).
}
\]

SOH-G024-Q controls the fourth logarithmic curvature strongly enough to close the second order.  By itself it does not provide the required global sign or growth bound for the third-order cumulant combination above.

A subsequent theorem may proceed by a direct bound on the `M_2` logarithmic growth, by a coupled bridge-cumulant inequality, or by an additional certified higher-log-curvature estimate.  None of those steps is assumed in this note.

## 9. Regression fixture

For

\[
K(t)=e^{-t^2/2},
\]

one has exactly

\[
A_u=2u,
\qquad
B_u=2,
\qquad
C_u^{(3)}=0,
\]

and

\[
\operatorname{Var}(A_u)=0,
\quad
\operatorname{Cov}(A_u,B_u)=0,
\quad
\mu_3(A_u)=0.
\]

The implementation compares the boxed bridge normal form against direct third differentiation of

\[
H_y(q)=\frac{\sqrt\pi}{2}e^{-q}\cosh(2y\sqrt q)
\]

and also checks the equivalent `(uN+3)M_2-uM_2'` recurrence.

## 10. Proof firewall

**PROVED / EXACT:** the generic complete-monotonicity recurrence, radial third-derivative identity, bridge differentiation rule, `R''` cumulant identity, tilt derivatives, third-order normal form, and second-margin growth reformulation.

**PROVED EARLIER ON G024:** `H_y'<0` and `H_y''>0` globally for every `0<|y|<1/2`; the compact part of the second-order result depends explicitly on SOH-G024-Q.

**OPEN:** the global sign `-H_y'''>=0`, all complete-monotonicity orders `m>=3`, full complete monotonicity, strict external Fourier positivity, Wiener density for the Riemann family, SOH-G003, SOH-C005, PF3, PF-infinity, and RH.
