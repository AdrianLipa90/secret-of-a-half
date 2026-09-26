# SOH Montgomery Form-Factor / Prime-Scale Crosswalk v0.1

Status: **FORCED_FORM_FACTOR_IMPORTED / ARITHMETIC_FREQUENCY_MAP_EXACT / RESTRICTED_ZETA_BINDING_STANDARD / FULL_LOCAL_PROCESS_OPEN**

Date: 2026-09-26

Dependencies:
- Infinities: \`TIR_HARDY_CAR_SPECTRAL_FORM_FACTOR_V0_1\`
- On-Primes: \`PHASE_BANK_FORM_FACTOR_DUALITY_V0_1\`
- SOH: \`SOH_YOSHIDA_FOURIER_SINE_KERNEL_COMPATIBILITY_V0_1\`

## 1. Forced projector-side form factor

The imported Hardy–CAR theorem gives, from the same consecutive-mode projector that forces the sine kernel,

\[
\boxed{
S_N(k/N)=\min(|k|/N,1)
}
\]

on the finite frequency lattice, and therefore

\[
\boxed{
S(\tau)=\min(|\tau|,1)
}
\]

in the microscopic continuum limit.

GUE, Montgomery and zeta data are excluded from this derivation.

## 2. SOH Fourier compatibility

The current SOH Yoshida Fourier projector has the same normalized local sine-kernel limit as the Hardy consecutive-mode projector. Therefore its filled-CAR lift inherits the same finite triangular Fourier coefficients and the same ramp/plateau limit.

This closes the projector-geometry/form-factor part of the SOH crosswalk.

## 3. Arithmetic frequency map

For a finite spectral sample \(\{\gamma_j\}\) near a reference height \(T\), define the frozen smooth zero density

\[
\nu_T=\frac1{2\pi}\log\frac{T}{2\pi},
\qquad
u_{T,j}=\nu_T(\gamma_j-T).
\]

For any \(q>0\), put

\[
\tau_q(T)=\frac{\log q}{\log(T/2\pi)}.
\]

Then

\[
q^{i\gamma_j}
=
q^{iT}e^{2\pi i\tau_q u_{T,j}},
\]

and consequently

\[
\boxed{
K_{\Gamma,T}(\tau_q)
=
N
\left|
\frac1N\sum_j q^{i\gamma_j}
\right|^2.
}
\]

For prime powers \(q=p^m\),

\[
\boxed{
\tau_{p^m}(T)
=
\frac{m\log p}{\log(T/2\pi)}.
}
\]

Thus the prime-power phase bank samples the finite pair-power/form-factor observable on an exact logarithmic arithmetic frequency lattice.

## 4. Critical asymptotic distinction

Fixed-\(q\) Landau asymptotics and fixed-\(\tau\) Montgomery scaling are not the same limit.

For fixed \(q\),

\[
\tau_q(T)\to0.
\]

To keep \(0<\tau<1\) fixed,

\[
q(T)\asymp (T/2\pi)^\tau.
\]

Therefore the remaining zeta-specific task cannot be closed by citing fixed-\(q\) Landau response alone.

It requires a smoothed/windowed \(q(T)\)-scaled derivation or another equivalent local spectral theorem.

## 5. Refined gate ledger

The Montgomery–Dyson programme is now split as follows.

### SOH-MD001A — restricted-support consistency
Status: **EXTERNAL_STANDARD / PARTIAL_BINDING**.

Classical Montgomery-type results agree with the sine-kernel/GUE correlation law on the appropriate restricted test class under their stated hypotheses.

### SOH-MD001B1 — projector geometry
Status: **CLOSED / EXACT**.

The native SOH Fourier projector has the same normalized local sine-kernel limit as the shared Hardy projector.

### SOH-MD001B2 — form-factor dual
Status: **CLOSED / FORCED_IN_DECLARED_PROJECTOR_CAR_SECTOR**.

The same projector forces

\[
S(\tau)=\min(|\tau|,1).
\]

### SOH-MD001B3 — arithmetic frequency coordinate
Status: **CLOSED / EXACT_FINITE_IDENTITY**.

Prime-power phases sample pair-power at

\[
\tau_{p^m}(T)=\frac{m\log p}{\log(T/2\pi)}.
\]

### SOH-MD001B4 — full zeta local-process binding
Status: **OPEN**.

One still must derive, without importing the target statistics, the full local zero process / smoothed pair form / quasi-free projector occupancy needed to transfer the forced sine-kernel and ramp beyond the classical restricted-support theorem.

This is now the unique substantive Montgomery–Dyson gate.

## 6. No-go against a false shortcut

The following implication is invalid:

\[
\text{Landau fixed-}q\text{ phase line}
\Longrightarrow
\text{full GUE ramp}.
\]

The reason is structural: fixed \(q\) samples only \(\tau_q(T)\to0\), whereas a nonzero point of the ramp requires logarithmically growing \(q(T)\).

Any proposed closure that ignores this scaling distinction is rejected.

## 7. Current sharp target

A sufficient next theorem has the form:

For a declared smooth window around height \(T\), construct from the prime/Weil side a zero-list-free pair-power observable \(F_T(\tau)\) such that for every fixed \(0<\tau<1\),

\[
F_T(\tau)\longrightarrow |\tau|
\]

and for \(|\tau|>1\),

\[
F_T(\tau)\longrightarrow1,
\]

with all normalization, diagonal subtraction, smoothing, and hypothesis dependence explicit.

If this is proved without inserting the GUE target, SOH-MD001B4 is closed.
