# SOH-G024 — CURRENT STATUS

**Current active note:** `SOH_G024_UNIFIED_CLOSURE_V0_6.md`  
**Status:** UNIFIED RADIAL / LAGUERRE / DUAL-GRAM CLOSURE — RH OPEN

Historical progression:

1. `SOH_G024_JENSEN_WIENER_KERNEL_V0_1.md` — retained for provenance; external-bilinear complex-continuation frontier quarantined.
2. `SOH_G024_HERMITIAN_CORRECTION_V0_2.md` — corrects the odd Fourier channel and identifies the Hermitian Jensen quantity as the Wick-rotated relative susceptibility.
3. `SOH_G024_NBODY_LAGUERRE_HIERARCHY_V0_3.md` — identifies the q-expansion of the partition with the classical extended Laguerre hierarchy.
4. `SOH_G024_RELATIVE_MOMENT_STRUCTURE_V0_4.md` — proves inherited strong log-concavity, fixed-u Stieltjes/Hankel positivity, the positive-definite generating mixture, and a generic no-go boundary.
5. `SOH_G024_ACHILLES_RADIAL_GATE_V0_5.md` — resums the hierarchy into the first-q radial response and proves the critical-strip RH-equivalent q-gate / positive-definite tangent criterion.
6. `SOH_G024_UNIFIED_CLOSURE_V0_6.md` — identifies that same q-gate with the SOH-G025 pole-free dual-Gram diagonal combination in the square-quotient plane.

Canonical generating object:

\[
\mathcal Q_x(q)
=
\frac12\left|\Xi(x+i\sqrt q)\right|^2
=
\mathcal Z(-ix,\sqrt q).
\]

Canonical scalar gate:

\[
\mathcal A_F(w)
:=
\widehat K_0(w,w)+|w|\widehat K_1(w,w),
\qquad
w=-(x+i\sqrt q)^2.
\]

Exact crosswalk:

\[
\mathcal A_F(w)
=
\partial_q\mathcal Q_x(q)
=
\widehat G_q(2x)
=
\frac12\sum_{n\ge1}nL_n[\Xi](x)q^{n-1}.
\]

Critical quotient domain:

\[
\Omega_{1/2}
=
\left\{
w:
0<
\frac{|w|+\Re w}{2}
<
\frac14
\right\}.
\]

Current RH-equivalent frontier:

\[
\boxed{
RH
\iff
\mathcal A_F(w)\ge0
\quad\forall w\in\Omega_{1/2}.
}
\]

The SOH-G024 coordinate assembly is closed. The remaining theorem is the
Riemann-specific sign of this single scalar gate.

**RH status: OPEN.**
