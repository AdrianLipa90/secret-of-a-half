# SOH-G024 — CURRENT STATUS

**Current active note:** `SOH_G024_NBODY_LAGUERRE_HIERARCHY_V0_3.md`  
**Status:** N-BODY / EXTENDED-LAGUERRE HIERARCHY ACTIVE — RH OPEN

Historical progression:

1. `SOH_G024_JENSEN_WIENER_KERNEL_V0_1.md` — retained for provenance; its external-bilinear complex-continuation frontier is quarantined.
2. `SOH_G024_HERMITIAN_CORRECTION_V0_2.md` — corrects the Fourier odd-channel convention and identifies the Hermitian Jensen quantity as the Wick-rotated relative susceptibility.
3. `SOH_G024_NBODY_LAGUERRE_HIERARCHY_V0_3.md` — identifies the complete q-expansion of that same partition with the classical extended Laguerre hierarchy.

Current active chain:

\[
\text{positive theta kernel}
\to \mathcal Z(-ix,y)=\tfrac12|\Xi(x+iy)|^2
\to \mathcal Z(-ix,y)=\tfrac12\sum_{n\ge0}L_n[\Xi](x)y^{2n}
\to \{L_n[\Xi](x)\ge0\}_{x,n}
\iff \Xi\in\mathcal{LP}
\iff \mathrm{RH}.
\]

The equivalence is a reformulation. The missing proof obligation is global positivity of the complete hierarchy. At `x=0` the hierarchy is unconditionally positive from the theta-kernel moments; the open obstruction is phase/translation stability for `x != 0`.

No RH claim is promoted by this status pointer.
