# SOH Yoshida–Fourier Projector Sine-Kernel Compatibility v0.1

Status: **EXACT_PROJECTOR_KERNEL / FORCED_SINE_KERNEL_COMPATIBILITY / ZETA_POINT_PROCESS_BINDING_OPEN**

Date: 2026-09-26

Parents:
- \`research/SOH_C005_YOSHIDA_FOURIER_REBASE_V0_1.md\`
- \`research/SOH_MONTGOMERY_DYSON_HARDY_CAR_BINDING_V0_1.md\`
- Infinities \`TIR_HARDY_CAR_SINE_KERNEL_FORCED_PREDICTION_V0_1\`

## 1. Existing SOH Fourier carrier

The C005 Yoshida rebase already declares the normalized Fourier modes on \([-a,a]\),

\[
e_n^{(a)}(x)
=
(2a)^{-1/2}e^{\pi i n x/a},
\qquad n\in\mathbb Z,
\]

and the low-mode orthogonal projector \(P^F_{N,a}\) onto

\[
\operatorname{span}\{e_n^{(a)}:|n|\le N\}.
\]

This basis was introduced for the Weil-form finite/high-frequency split. No Montgomery/GUE input occurs in its definition.

Put

\[
M=2N+1.
\]

## 2. Exact finite projection kernel

The projector kernel is

\[
K_{N,a}(x,y)
=
\frac1{2a}
\sum_{n=-N}^{N}
e^{\pi i n(x-y)/a}.
\]

With \(\Delta=x-y\), the symmetric geometric sum gives

\[
\boxed{
K_{N,a}(x,y)
=
\frac1{2a}
\frac{
\sin\!\left(M\pi\Delta/(2a)\right)
}{
\sin\!\left(\pi\Delta/(2a)\right)
}.
}
\]

The diagonal is constant:

\[
\boxed{
\rho_{N,a}
=
K_{N,a}(x,x)
=
\frac{M}{2a}.
}
\]

## 3. Microscopic unfolding

Use the projector's own unit-density coordinate

\[
s
=
\rho_{N,a}(x-y)
=
\frac{M\Delta}{2a}.
\]

Then

\[
\frac{\pi\Delta}{2a}
=
\frac{\pi s}{M}
\]

and therefore

\[
\boxed{
\frac{K_{N,a}(x,y)}{\rho_{N,a}}
=
\frac{\sin(\pi s)}
{M\sin(\pi s/M)}.
}
\]

The support parameter \(a\) cancels exactly after unfolding.

Hence

\[
\boxed{
\lim_{N\to\infty}
\frac{K_{N,a}}{\rho_{N,a}}
=
\frac{\sin\pi s}{\pi s}
}
\]

uniformly on every fixed compact \(s\)-window.

Thus the existing SOH Yoshida/Fourier rebase and the one-sided Hardy/Hilbert-Hotel projector have the same unit-density local projection-kernel limit.

## 4. CAR lift and two-point law

If the standard filled CAR/Slater state is formed on

\[
\operatorname{Ran}P^F_{N,a},
\]

then its two-point density is

\[
\rho_{2,N,a}(x,y)
=
\rho_{N,a}^2
-
|K_{N,a}(x,y)|^2.
\]

After normalization,

\[
\boxed{
g_{2,N}^{F}(s)
=
1-
\left[
\frac{\sin(\pi s)}
{M\sin(\pi s/M)}
\right]^2,
\qquad M=2N+1.
}
\]

Therefore

\[
\boxed{
g_2^{F}(s)
=
1-
\left(
\frac{\sin\pi s}{\pi s}
\right)^2.
}
\]

In phase coordinates \(\Delta\Phi=2\pi s\),

\[
\boxed{
g_2^{F}(\Delta\Phi)
=
1-
\left[
\frac{\sin(\Delta\Phi/2)}
{\Delta\Phi/2}
\right]^2.
}
\]

No zeta zero list, random matrix, Montgomery pair-correlation target or fitted kernel enters the derivation.

## 5. What this closes

The previous crosswalk left a possible basis mismatch:

\[
\text{SOH Hermite/Fourier test space}
\quad\text{vs}\quad
\text{Hardy consecutive-shift projector}.
\]

At the local projector-kernel level, the Yoshida Fourier rebase removes that mismatch. Both canonical consecutive-mode projectors yield the same sine kernel after their own mean-density unfolding.

Thus the Montgomery–Dyson bridge is no longer blocked by the choice between:
- one-sided Hardy modes \(0,\ldots,N-1\), and
- symmetric SOH/Yoshida Fourier modes \(-N,\ldots,N\).

Their local normalized projector limits coincide exactly.

## 6. What remains open

The remaining gate is not projector geometry.

It is the spectral-occupancy statement:

\[
\boxed{
\text{zeta-zero point process}
\stackrel{?}{=}
\text{CAR occupancy process associated with the canonical SOH Fourier projector}
}
\]

or a rigorously equivalent local-projector convergence theorem.

The current Weil form acts on test functions. Its Fourier projection is a basis decomposition of the test-function domain. That fact alone does not turn zeta zeros into fermions occupying those modes.

Accordingly:

\[
\boxed{
\text{SOH Fourier projector}
\to
\text{sine kernel}
=
\text{CLOSED / EXACT}
}
\]

but

\[
\boxed{
\text{zeta zeros}
\to
\text{filled-CAR SOH Fourier projector}
=
\text{OPEN / SOH-MD001}.
}
\]

## 7. Refined SOH-MD001

The gate can now be stated more narrowly.

### SOH-MD001 — zeta spectral occupancy binding

Construct from the zeta/Weil spectral object, without GUE/Montgomery input, a canonical quasi-free/CAR state or equivalent determinantal projector whose local one-particle density operator is asymptotic to \(P^F_{N,a}\) after mean-density unfolding.

A sufficient formulation is local kernel convergence:

\[
\frac{1}{\rho_T}
K_{\zeta,T}
\!\left(
x_T+\frac{u}{\rho_T},
x_T+\frac{v}{\rho_T}
\right)
\longrightarrow
\frac{\sin\pi(u-v)}{\pi(u-v)}
\]

derived from the zeta/Weil operator itself rather than assumed from pair-correlation data.

If such convergence is proved, Wick/CAR determinant structure transfers the already-forced pair law.

## 8. Compact theorem

### Theorem — SOH Fourier/Hardy local-kernel equivalence

For the Yoshida Fourier projector \(P^F_{N,a}\) onto \(|n|\le N\), with \(M=2N+1\) and unit-density microscopic coordinate \(s=M(x-y)/(2a)\),

\[
\boxed{
\frac{K_{N,a}(x,y)}{\rho_{N,a}}
=
\frac{\sin(\pi s)}
{M\sin(\pi s/M)}
\to
\frac{\sin\pi s}{\pi s}.
}
\]

Therefore the local normalized projector kernel agrees in the limit with the Hardy/Hilbert-Hotel consecutive-mode projector kernel. With the standard filled CAR lift, both force the same sinc-square two-point law. Q.E.D.
