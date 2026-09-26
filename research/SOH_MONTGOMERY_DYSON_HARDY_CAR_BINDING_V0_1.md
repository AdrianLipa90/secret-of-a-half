# SOH Montgomery–Dyson / Hardy–CAR Binding Crosswalk v0.1

Status: **FORCED_PREDICTION_IMPORTED / ZETA_TO_HARDY_CAR_BINDING_OPEN**

Date: 2026-09-26

Dependency:
- AdrianLipa90/Infinities
- branch: \`formalize/hardy-car-sine-kernel-forced-prediction-v0.1-20260926\`
- dependency head at crosswalk creation: \`7008a9121d878674a7190d0966faa727f9eacb55\`
- theorem: \`research/TIR_HARDY_CAR_SINE_KERNEL_FORCED_PREDICTION_V0_1.md\`

## 1. Imported exact theorem

The dependency proves inside the declared Hardy–CAR sector that the canonical projector onto the first \(N\) consecutive unilateral-shift modes,

\[
P_N:\ H^2(S^1)\to\operatorname{span}\{1,z,\ldots,z^{N-1}\},
\]

combined with the filled CAR/Slater state forces

\[
g_{2,N}(s)
=
1-
\left[
\frac{\sin(\pi s)}
{N\sin(\pi s/N)}
\right]^2
\]

and therefore

\[
\boxed{
g_2(s)
=
1-
\left(
\frac{\sin\pi s}{\pi s}
\right)^2
}
\]

under unit-density microscopic unfolding.

Equivalently, with \(\Delta\Phi=2\pi s\),

\[
\boxed{
g_2(\Delta\Phi)
=
1-
\left[
\frac{\sin(\Delta\Phi/2)}
{\Delta\Phi/2}
\right]^2.
}
\]

GUE, Montgomery pair correlation, random matrices and zeta-zero data are excluded from the derivation inputs. The functional match is therefore a forced prediction of that sector, not a fitted reference.

## 2. What Secret-of-a-Half already supplies

The current SOH main line already contains:
- the theta–Mellin representation and explicit Riemann kernel;
- native PhaseNav theta and Weil arithmetic constructions;
- prime-power arithmetic evaluation of localized Weil forms;
- the Hermite/Fourier finite-section programme;
- the relational-zero / critical-axis theorem package;
- a proof firewall separating internal relational theorems from external zeta bindings.

These structures establish multiple exact phase, symmetry, positivity and arithmetic identities. They do **not** currently identify the zeta-zero point process with the consecutive-mode Hardy projector process of the imported theorem.

## 3. Exact missing binding

The remaining Montgomery–Dyson binding is not the sine-kernel calculation. That calculation is already closed in the dependency.

The missing statement is operator-level:

\[
\boxed{
\text{zeta spectral process}
\longrightarrow
\text{canonical consecutive-mode Hardy–CAR projector sector}.
}
\]

A sufficient strong form would be the construction of a self-adjoint zeta spectral operator \(H_\zeta\) and local scaling maps \(U_T\) such that its spectral projector in a height window obeys

\[
U_T E_{H_\zeta}(I_T) U_T^\dagger
\longrightarrow
P_{\rm Hardy}
\]

in a topology strong enough to transfer local two-point kernels, after the standard mean-density unfolding.

A finite-window version may instead prove that the normalized local projector kernel converges directly to

\[
K_{\sin}(x,y)
=
\frac{\sin\pi(x-y)}{\pi(x-y)}.
\]

However, using the desired pair-correlation law itself as the premise would be circular. The incoming edge must be obtained from the zeta/Weil/operator construction independently of Montgomery–Dyson.

## 4. Why existing SOH projectors do not silently close this gate

The current C005 finite-section machinery uses Hermite and localized integral-operator projections. Those are proof/positivity bases. They are not identified in main as the consecutive Hardy shift orbit

\[
\{1,z,\ldots,z^{N-1}\}
\]

with the filled CAR state required by the forced-prediction theorem.

Likewise, the current relational-zero principle constrains the horizontal critical-axis defect. It does not determine the local statistics of the ordinates \(\gamma_n\).

Therefore the following implication is **not yet in main**:

\[
\xi(\tfrac12+i\gamma_n)=0
\quad\Longrightarrow\quad
\{\gamma_n\}\text{ is the spectrum/eigenphase process of }P_N.
\]

## 5. New gate

Define:

### SOH-MD001 — Zeta/Hardy–CAR projector binding

Construct, without using Montgomery/GUE statistics as input, a canonical provenance-bearing map from the zeta/Weil spectral object to a Hardy/CAR projector family whose microscopic local projector converges to the consecutive-mode shift projector of the Infinities theorem.

Promotion condition:

\[
\boxed{
\mathrm{SOH\!-\!MD001}
+
\mathrm{INF\!-\!270}
\Longrightarrow
\text{Montgomery–Dyson law as a zeta-specific forced prediction}.
}
\]

Until SOH-MD001 is closed:
- the sine-kernel law is **DERIVED_IN_FRAMEWORK / FORCED_PREDICTION** in the Hardy–CAR sector;
- its application to zeta zeros is **BINDING_OPEN**;
- its use as a benchmark against zeta zeros is valid, but does not itself close the binding.

## 6. Non-circular derivation routes to test

Admissible routes include:
1. derive a self-adjoint spectral operator from the existing Weil/arithmetic form and prove a local projector equivalence;
2. derive a canonical Hardy/model-space representation of the completed-zeta spectral data with consecutive shift-orbit occupancy;
3. derive the same local projector kernel from the prime-power explicit-formula operator without inserting the sine kernel or pair-correlation target.

Disallowed as proof of SOH-MD001:
- fitting to Odlyzko zeros and then declaring the fitted kernel canonical;
- assuming GUE universality;
- assuming Montgomery pair correlation;
- choosing a projector because it yields sinc.

## 7. Status split

\[
\boxed{
\text{Hardy–CAR}\to\text{sine kernel}
=
\text{CLOSED / DERIVED / FORCED}
}
\]

\[
\boxed{
\text{zeta zeros}\to\text{Hardy–CAR projector}
=
\text{OPEN BINDING}
}
\]

This split is the current non-circular proof boundary.
