# SOH Localized Screw-Kernel / Explicit-Weil Cross-Check v0.1

Status: **INDEPENDENT NUMERICAL NORMALIZATION CROSS-CHECK PASS / FULL INTERVAL JOIN OPEN**

Date: 2026-09-26

Parents:
- research/SOH_SUZUKI_LOCALIZED_OPERATOR_JOIN_V0_1.md
- research/SOH_LOCALIZED_FOURIER_GALERKIN_OPERATOR_V0_1.md
- src/secret_of_a_half/zeta_screw.py

No RH and no zeta-zero list are used.

## 1. Purpose

The localized arithmetic matrix is now computed directly from Suzuki's explicit
Weil functional.

A separate implementation of the same source theory already exists through the
screw kernel

\[
g(t)=-\Psi(|t|)
\]

and the localized operator

\[
B_a=D^*G_aD.
\]

The purpose of this test is to catch:
- sign errors;
- missing \(2\pi\) factors;
- interval-normalization mismatches;
- wrong screw-function convention.

It is deliberately independent of the global Hermite diagnostic.

## 2. Test vector

Use the first normalized Dirichlet mode

\[
\boxed{
\phi_1(x)
=
a^{-1/2}
\sin\left(
\frac{\pi(x+a)}{2a}
\right).
}
\]

Then

\[
\phi_1(\pm a)=0
\]

and

\[
D\phi_1=i\phi_1'
\]

has zero mean automatically.

Thus the zero-mean projections in \(G_a=P_aGP_a\) do not alter the quadratic
pairing.

## 3. Screw-side reduction

For \(0\le t\le2a\), define the derivative autocorrelation

\[
C_1(t)
=
\int_{-a}^{a-t}
\phi_1'(x)\phi_1'(x+t)\,dx.
\]

Direct trigonometric integration gives

\[
\boxed{
C_n(t)
=
\frac{k_n^2}{2a}
\left[
(2a-t)\cos(k_nt)
-
\frac{\sin(k_nt)}{k_n}
\right],
}
\]

where

\[
k_n=\frac{n\pi}{2a}.
\]

Since both \(g\) and the diagonal correlation are even,

\[
\boxed{
Q_{\rm screw}(\phi_n)
=
2\int_0^{2a}
g(t)C_n(t)\,dt.
}
\]

This is a one-dimensional integral through the independently implemented screw
function.

## 4. Weil-side reduction

The same Dirichlet mode is a two-frequency combination

\[
\phi_n
=
c_-v_{-k_n}
+
c_+v_{+k_n}.
\]

By sesquilinearity,

\[
Q_{\rm Weil}(\phi_n)
=
\sum_{\sigma,\tau\in\{-,+\}}
c_\sigma\overline{c_\tau}
Q_W^a(v_{\sigma k_n},v_{\tau k_n}),
\]

using the localized explicit-Weil cross-form evaluator.

The two calculations therefore share the source theorem but not the numerical
route.

## 5. Prime-free normalization sample

Take

\[
a=0.345<\frac12\log2.
\]

No prime-power threshold lies in the screw support \(|t|\le2a\).

For \(n=1\), adaptive endpoint-resolved quadrature gives

\[
\boxed{
Q_{\rm screw}
=
0.00262569081058866498516318
}
\]

and the independent explicit-Weil calculation gives

\[
\boxed{
Q_{\rm Weil}
=
0.002625690810588664988342864.
}
\]

Therefore

\[
\boxed{
|Q_{\rm screw}-Q_{\rm Weil}|
\approx
3.18\times10^{-21}.
}
\]

## 6. Interpretation

This strongly validates:
- the sign convention \(g=-\Psi\);
- the \(D=i\,d/dx\) convention;
- the localized interval normalization;
- the explicit-Weil cross-form implementation.

It also demonstrates why naive fixed-node quadrature was misleading: the
screw kernel has nontrivial endpoint structure near \(t=0\), and unresolved
Gauss quadrature converges slowly.

## 7. Status

### LF-G3a — single-mode source normalization

\[
\boxed{\text{PASS numerically}.}
\]

### LF-G3b — full finite matrix cross-check

\[
\boxed{\text{OPEN}.}
\]

### LF-G3c — interval-certified equality

\[
\boxed{\text{OPEN}.}
\]

A theorem-level implementation join still requires interval control of the
screw-side integral or an analytic integration-by-parts identity at the code
level.

## 8. Firewall

This is not:
- an RH result;
- a proof of localized positivity;
- an interval certificate;
- a substitute for a full \(A_{LL},B,A_{HH}\) cross-check.

It is a high-precision independent normalization test with a \(10^{-21}\)
residual.


## 9. Three-mode integration-by-parts upgrade

The screw-side integral can be accelerated without changing the source object.

For the normalized Dirichlet mode \(\phi_n\), let

\[
k_n=\frac{n\pi}{2a}
\]

and define

\[
F_n(t)
=
1+\frac{t-2a}{2a}\cos(k_nt)
-\frac{\sin(k_nt)}{2ak_n}.
\]

Then

\[
F_n''(t)=C_n(t),
\]

with boundary data

\[
F_n(0)=F_n'(0)=0,
\qquad
F_n(2a)=1,
\qquad
F_n'(2a)=0.
\]

In the prime-free window,

\[
g''(t)
=
-2\cosh(t/2)
+
\frac{e^{-t/2}}{1-e^{-2t}}
\qquad(t>0).
\]

Two integrations by parts give

\[
\boxed{
Q_{\rm screw}(\phi_n)
=
2\left[
-g'(2a)
+
\int_0^{2a}
g''(t)F_n(t)\,dt
\right].
}
\]

Near zero,

\[
g''(t)\sim\frac1{2t},
\qquad
F_n(t)\sim\frac{k_n^2t^2}{2},
\]

so the product is regular and tends to zero.

At \(a=0.345\), the independent screw and explicit-Weil lanes agree for the
first three modes:

\[
\boxed{
Q_1
=
0.00262569081058866498516318025485,
}
\]

\[
\boxed{
Q_2
=
0.157045650889994298960677934719,
}
\]

\[
\boxed{
Q_3
=
0.700976786436366215066158696726.
}
\]

The maximum cross-lane discrepancy in the high-precision regression is below

\[
10^{-28}.
\]

This remains numerical rather than interval-certified, but it upgrades the
single-mode normalization smoke test to a three-mode independent modal
cross-check.
