# SOH-X — Half Interface, Spectral Nulls, and the Resonant-Chemistry Crosslink v0.1

Status: `STRUCTURAL_CROSSLINK_CANDIDATE / NON_PROMOTING`

Base provenance: `AdrianLipa90/secret-of-a-half@b4a842fe82e2d0a2781c887145ff6559e9666f05` (`main`).

Contract: `RCE_CHEM_PHOTO_EM_BRIDGE_V0_1`

## 1. Existing exact half kernel

Secret of a Half uses

\[
|\psi\rangle=\sqrt{\sigma}|0\rangle+e^{i\phi}\sqrt{1-\sigma}|1\rangle
\]

with cancellation defect

\[
D(\sigma,\phi)=1+2\sqrt{\sigma(1-\sigma)}\cos\phi.
\]

The exact zero occurs at

\[
\boxed{\sigma=\frac12,\qquad\phi\equiv\pi\pmod{2\pi}.}
\]

The IDT spinorial lift supplies

\[
\phi=\frac{\Delta\tau}{2},
\]

so the same kernel becomes

\[
\boxed{D_{1/2}(\sigma,\Delta\tau)=1+2\sqrt{\sigma(1-\sigma)}\cos\!\left(\frac{\Delta\tau}{2}\right)}
\]

with exact zero at

\[
\boxed{\sigma=\frac12,\qquad\Delta\tau\equiv2\pi\pmod{4\pi}.}
\]

This is an exact cross-repository local identity.

## 2. Existing Riemann–Euler Zeeman-type ansatz

The repository already defines

\[
H_Z(B)=E_0I+\lambda B\sigma_z,
\]

with

\[
E_\pm(B)=E_0\pm\lambda B,
\qquad
\Delta E(B)=2|\lambda B|.
\]

When this declared two-level ansatz is supplied to a standard electromagnetic transition layer, its internal doublet difference frequency is

\[
\boxed{\omega_{+-}(B)=\frac{2|\lambda B|}{\hbar}.}
\]

At the self-dual layer \(B=0\), the doublet is degenerate and the splitting closes. This adds a spectroscopy-compatible observable coordinate to the existing Zeeman-type construction while preserving its current ansatz status.

## 3. Spectral-null role of the half interface

For two admitted transition pathways with equal normalized weight, the spinorial half-turn gives relative phase \(\pi\). Their symmetric channel therefore cancels:

\[
\boxed{
\frac12_{\rm amplitude\ balance}
+
\frac12_{\rm spinorial\ turn}
\longrightarrow
0_{\rm relational\ projection}.
}
\]

This structure is relevant to dark channels, destructive interference, antiresonance and line suppression whenever a physical two-path mapping is independently supplied.

## 4. Proof firewall

`SOH-C004` and `SOH-C005` retain their current status.

The repository/formalism may suggest that the same half-interface geometry participates in physical spectroscopy and in the zeta self-dual shell, yet does not state that identification as an established result.

The crosslink exports only:

```text
balanced_two_channel_kernel
spinorial_half_turn
Riemann–Euler doublet splitting coordinate
exact local cancellation condition
```

No zeta-zero claim is promoted by a chemical or spectroscopic fit.

## 5. Resonant Chemistry export

Adapter name:

`SOH_HALF_INTERFACE_SPECTRAL_NULL_V0_1`

Fields:

```text
sigma
delta_tau
half_defect
is_relational_zero
optional_B_coordinate
optional_doublet_gap
source_claim_ids
source_commit
```

A Resonant Chemistry consumer may use this adapter as an interference diagnostic alongside its independently admitted energy levels and transition matrix elements.
