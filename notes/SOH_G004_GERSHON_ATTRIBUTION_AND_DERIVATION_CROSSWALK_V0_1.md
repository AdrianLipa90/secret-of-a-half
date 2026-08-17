# SOH-G004 — Gershon attribution and derivation crosswalk

Status: **ATTRIBUTION / PROVENANCE NOTE. No new theorem claim.**

## Primary precedent

Avi Gershon, *On the Log-Concavity of the Riemann Xi Kernel*, Preprints.org v2, posted 29 June 2026, DOI `10.20944/preprints202604.0159.v2`.

Gershon proves strict log-concavity (TP2) of the classical Riemann Xi kernel `Phi` on `[0, infinity)`. Version 2 presents both a rigorous interval-arithmetic proof and a purely analytic proof based on a convex-potential decomposition of the theta channels. Gershon explicitly leaves the TP-infinity / Laguerre-Pólya step open.

## Overlap with the SOH derivation

The SOH-G004 derivation independently reaches the same half-line kernel shape property and shares the following structural ingredients with Gershon:

1. decomposition of `Phi` into positive theta channels `phi_n`;
2. strict negative logarithmic curvature for each channel;
3. dominance of the `n=1` channel and exponential suppression of higher theta modes;
4. a quantitative tail/mixing estimate used to retain negative total curvature.

Accordingly, **SOH does not claim priority for strict log-concavity of the classical kernel `Phi`**. Any use of that property in the monograph or downstream PF2/PF3 derivations must cite Gershon.

## Distinct downstream SOH objects

The SOH programme then applies the self-dual compactification

`eta = tanh(y)`

and studies

`W(eta) = Phi(atanh eta)/(1-eta^2)`.

The SOH-G004 theorem recorded in the monograph is the strict log-concavity inequality for this compactified weight `W`, including explicit control of the Jacobian-induced terms. The subsequent coefficient programme uses

`a_k = m_k/(2k)!`

and develops the PF2 theorem and PF3 ratio-curvature frontier. These downstream statements must be kept logically distinct from Gershon's prior TP2 theorem for `Phi`.

## Required citation rule

Whenever a derivation invokes strict log-concavity of `Phi`, cite `gershon2026logconcavity` and state that SOH independently rederives the property. Do not present the half-line TP2 result as novel to SOH.

When discussing SOH-G004, distinguish:

- **prior literature:** strict log-concavity of `Phi` — Gershon 2026;
- **SOH derivation:** independent mixture-variance proof and compactified `W` inequality;
- **SOH downstream frontier:** PF2, PF3 ratio-curvature, PF-infinity, real-rootedness;
- **open:** PF3 globally, PF-infinity, SOH-G003, RH.
