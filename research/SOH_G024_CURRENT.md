# SOH-G024 — CURRENT STATUS

**Current active note:** `SOH_G024_ACHILLES_RADIAL_GATE_V0_5.md`  
**Status:** FIRST-q RADIAL GATE / PD-TANGENT RH-EQUIVALENT REDUCTION — RH OPEN

Historical progression:

1. `SOH_G024_JENSEN_WIENER_KERNEL_V0_1.md` — retained for provenance; external-bilinear complex-continuation frontier quarantined.
2. `SOH_G024_HERMITIAN_CORRECTION_V0_2.md` — corrects the odd Fourier channel and identifies the Hermitian Jensen quantity as the Wick-rotated relative susceptibility.
3. `SOH_G024_NBODY_LAGUERRE_HIERARCHY_V0_3.md` — identifies the q-expansion of the partition with the classical extended Laguerre hierarchy.
4. `SOH_G024_RELATIVE_MOMENT_STRUCTURE_V0_4.md` — proves inherited strong log-concavity, fixed-u Stieltjes/Hankel positivity, the positive-definite generating mixture, and a generic no-go boundary.
5. `SOH_G024_ACHILLES_RADIAL_GATE_V0_5.md` — resums the hierarchy into the first-q radial response and proves the critical-strip criterion
   \[
   RH\iff \partial_q\mathcal Q_x(q)\ge0
   \quad\forall x\in\mathbb R,\ 0<q<1/4.
   \]

Current generating object:

\[
\mathcal Q_x(q)
=
\frac12\left|\Xi(x+i\sqrt q)\right|^2
=
\mathcal Z(-ix,\sqrt q).
\]

Every off-axis Xi zero is an even-order touchdown of this non-negative surface and necessarily produces a negative \(\partial_q\mathcal Q\) witness earlier on the same vertical line.

Equivalent positive-definite tangent form:

\[
G_q(u)=\partial_q B_{\sqrt q}(u),
\qquad
\widehat G_q(2x)=\partial_q\mathcal Q_x(q),
\]

so

\[
RH
\iff
G_q\text{ is positive definite for every }0<q<1/4.
\]

This is the active proof frontier. It is an exact reduction, not an RH proof.

**RH status: OPEN.**
