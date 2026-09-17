# SOH-G024 — CURRENT STATUS

**Current active note:** `SOH_G024_RELATIVE_MOMENT_STRUCTURE_V0_4.md`  
**Status:** RELATIVE-MOMENT STRUCTURE / GENERIC POSITIVITY NO-GO IDENTIFIED — RH OPEN

Historical progression:

1. `SOH_G024_JENSEN_WIENER_KERNEL_V0_1.md` — retained for provenance; its external-bilinear complex-continuation frontier is quarantined.
2. `SOH_G024_HERMITIAN_CORRECTION_V0_2.md` — corrects the Fourier odd-channel convention and identifies the Hermitian Jensen quantity as the Wick-rotated relative susceptibility.
3. `SOH_G024_NBODY_LAGUERRE_HIERARCHY_V0_3.md` — identifies the complete q-expansion of that partition with the classical extended Laguerre hierarchy.
4. `SOH_G024_RELATIVE_MOMENT_STRUCTURE_V0_4.md` — proves all-order strong-log-concavity inheritance and fixed-u Stieltjes/Hankel positivity for the relative-moment kernels, identifies the positive-definite generating mixture, and proves by an explicit strongly log-concave control that these generic properties are still insufficient for coefficientwise Fourier positivity.

Current active chain:

\[
\text{positive theta kernel}
\to
C_n(u)=\int r^{2n}K(u+r)K(u-r)\,dr
\to
\begin{cases}
-(\log C_n)''>20,\\
[C_{i+j}(u)]\succeq0,\\
\widehat B_y(2x)=\tfrac12|\Xi(x+iy)|^2
\end{cases}
\]

while

\[
RH
\iff
\widehat C_n(2x)\ge0
\quad\forall x\in\mathbb R,\ n\ge0.
\]

The v0.4 no-go shows that strong log-concavity + pointwise Hankel positivity + positivity of the exponential generating mixture do not imply coefficientwise Fourier positivity in general. The missing ingredient must therefore be Riemann-specific rather than a generic shape property of the relative-moment family.

No RH claim is promoted by this status pointer.
