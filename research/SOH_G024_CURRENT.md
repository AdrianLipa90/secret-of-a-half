# SOH-G024 — CURRENT STATUS

**Current active note:** `SOH_G024_ZERO_SHADOW_HARMONIC_V0_7.md`  
**Status:** ZERO-SHADOW / 4D HARMONIC GATE GEOMETRY — RH OPEN

Historical progression:

1. `SOH_G024_JENSEN_WIENER_KERNEL_V0_1.md` — retained for provenance; external-bilinear complex-continuation frontier quarantined.
2. `SOH_G024_HERMITIAN_CORRECTION_V0_2.md` — corrects the odd Fourier channel and identifies the Hermitian Jensen quantity as the Wick-rotated relative susceptibility.
3. `SOH_G024_NBODY_LAGUERRE_HIERARCHY_V0_3.md` — identifies the q-expansion of the partition with the classical extended Laguerre hierarchy.
4. `SOH_G024_RELATIVE_MOMENT_STRUCTURE_V0_4.md` — proves inherited strong log-concavity, fixed-u Stieltjes/Hankel positivity, the positive-definite generating mixture, and a generic no-go boundary.
5. `SOH_G024_ACHILLES_RADIAL_GATE_V0_5.md` — resums the hierarchy into the first-q radial response and proves the critical-strip RH-equivalent q-gate / positive-definite tangent criterion.
6. `SOH_G024_UNIFIED_CLOSURE_V0_6.md` — identifies the same q-gate with the SOH-G025 pole-free dual-Gram diagonal combination in the square-quotient plane.
7. `SOH_G024_ZERO_SHADOW_HARMONIC_V0_7.md` — decomposes the normalized q-gate into exact zero-shadow kernels, proves unconditional positivity on q=1/4, and lifts the gate to an axisymmetric harmonic field in R^4.

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
\widehat K_0(w,w)+|w|\widehat K_1(w,w)
=
\partial_q\mathcal Q_x(q),
\qquad
w=-(x+i\sqrt q)^2.
\]

Normalized zero-potential gate:

\[
\boxed{
\mathcal R_\Xi(x,q)
=
\frac{\partial_q\mathcal Q_x(q)}{\mathcal Q_x(q)}
=
-\frac1{\sqrt q}
\Im\frac{\Xi'(x+i\sqrt q)}{\Xi(x+i\sqrt q)}.
}
\]

For a conjugate zero pair \(u\pm iv\),

\[
\boxed{
S_{u,v}(x,\sqrt q)
=
\frac{
2((x-u)^2+q-v^2)
}{
((x-u)^2+(\sqrt q-v)^2)
((x-u)^2+(\sqrt q+v)^2)
}.
}
\]

It is negative exactly in

\[
(x-u)^2+q<v^2.
\]

Every hypothetical off-axis Xi zero therefore creates an interior negative
shadow immediately below its zero shell. Conversely, gate negativity can occur
only inside the union of such off-axis shadow disks.

Because every Xi zero satisfies \(|\Im z|<1/2\),

\[
\boxed{
\mathcal R_\Xi(x,1/4)>0
\quad\forall x\in\mathbb R
}
\]

unconditionally.

Away from zeros,

\[
\boxed{
\mathcal R_{xx}+6\mathcal R_q+4q\mathcal R_{qq}=0.
}
\]

With \(W(x,y)=\mathcal R(x,y^2)\),

\[
\boxed{
W_{xx}+W_{yy}+\frac2yW_y=0,
}
\]

the axisymmetric Laplace equation in four dimensions.

Current RH-equivalent frontier:

\[
\boxed{
RH
\iff
\mathcal R_\Xi(x,q)\ge0
\quad
\forall x\in\mathbb R,\quad0<q<1/4,
}
\]

with zeros handled by the unnormalized gate.

The algebraic/coordinate assembly remains closed. The remaining theorem is now
localized as exclusion of interior off-axis zero shells / negative shadows.

**RH status: OPEN.**
