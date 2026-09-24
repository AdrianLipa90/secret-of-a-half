# SOH U(1)–Shannon Relational Energy Derivation v0.1

**Date:** 24 September 2026  
**Status:** EXACT COERCIVITY IN THE DECLARED RELATIONAL MODEL / ZERO-REALIZATION PRINCIPLE SEPARATE

## 1. Correction of the proof graph

The canonical relational energy need not be introduced as an additional axiom. Its coercive part follows already from the binary Shannon/KL defect; the existing TIR U(1) Lagrangian and White-Thread holonomy potential add further non-negative terms.

Let

\[
s=\sigma+it,\qquad
x=\sigma-\frac12,\qquad
0<\sigma<1.
\]

Define

\[
D_H(\sigma)=\ln2-H_2(\sigma).
\]

Then

\[
D_H\left(\frac12\right)=0,
\qquad
D_H'\left(\frac12\right)=0,
\]

and

\[
D_H''(\sigma)
=
\frac1\sigma+\frac1{1-\sigma}
=
\frac1{\sigma(1-\sigma)}
\ge4.
\]

Therefore strong convexity gives

\[
\boxed{
D_H(\sigma)
\ge
2\left(\sigma-\frac12\right)^2
=
2x^2.
}
\]

Equality in the zero condition occurs only at \(x=0\).

## 2. Exact projective defect crosswalk

For

\[
\Omega(s)=\frac{s}{1-s}
\]

the formal So½ layer already proves

\[
\boxed{
\Delta_{\rm RC}(\Omega(s))
=
\frac{4x^2}{|s|^2|1-s|^2}
}
\]

for \(s\ne0,1\). Hence

\[
2x^2
=
\frac{|s|^2|1-s|^2}{2}
\Delta_{\rm RC}(\Omega(s)).
\]

Combining with the Shannon bound gives the pointwise coercive theorem

\[
\boxed{
D_H(\Re s)
\ge
c(s)\,\Delta_{\rm RC}(\Omega(s)),
\qquad
c(s):=\frac{|s|^2|1-s|^2}{2}>0
}
\]

for every \(s\ne0,1\) in the open strip.

No RH assumption is used in this inequality.

## 3. U(1) / holonomy strengthening

TIR supplies a semantic U(1) connection

\[
W_\gamma=\exp\!\left(i\oint_\gamma\mathcal A\right),
\qquad
F=d\mathcal A,
\]

and the spin-lift mismatch potential

\[
V_{\rm WT}
=
\sum_e K^{(1)}_e(1-\cos\Delta_e)
+
K^{(1/2)}_e\left(1-\cos\frac{\Delta_e}{2}\right)
\ge0.
\]

The isolated phase energy is

\[
\mathcal E_{\rm WT}
=
\sum_i\frac{I_i}{2}\dot\Theta_i^2
+
V_{\rm WT}
\ge0.
\]

For static holonomy the exact Lyapunov identity is

\[
\dot{\mathcal E}_{\rm WT}
=
-\sum_i\eta_i\dot\Theta_i^2
\le0.
\]

Therefore the canonical relational energy may be taken in the form

\[
\boxed{
E_{\rm rel}(s)
=
D_H(\Re s)
+
\mathcal E_{\rm WT}(s)
+
E_{\rm other,+}(s),
}
\]

where every additional declared term is non-negative.

Immediately,

\[
\boxed{
E_{\rm rel}(s)
\ge
D_H(\Re s)
\ge
c(s)\Delta_{\rm RC}(\Omega(s)).
}
\]

Thus the coercive energy edge is derived, not postulated.

## 4. Exact half-turn U(1) coordinate

The TIR normalized Berry closure gives

\[
q_B=-(1-\sigma)\pmod1.
\]

For the canonical representative \(0<\sigma<1\),

\[
q_B=\sigma.
\]

Therefore the displacement from the balanced half-turn is exactly

\[
\delta q_B
=
q_B-\frac12
=
\sigma-\frac12
=
x.
\]

In radians,

\[
\delta\phi_B=2\pi x.
\]

So the horizontal Riemann displacement, the Shannon imbalance, and the U(1) half-turn displacement are the same scalar defect in three coordinate systems.

## 5. What remains after energy derivation

Once the energy is derived, the shortest RH implication is

\[
E_{\rm rel}(\rho)=0
\Longrightarrow
c(\rho)\Delta_{\rm RC}(\Omega(\rho))=0
\Longrightarrow
\Delta_{\rm RC}(\Omega(\rho))=0
\Longrightarrow
\Re\rho=\frac12.
\]

Thus the only extra premise required by the Occam relational system is no longer an energy axiom. It is the general relational-zero realization principle:

\[
\boxed{
\text{R0: a zero of an admitted relational observable is represented by}
\text{ a zero of its canonical relational action-defect.}
}
\]

Applied to the canonical zeta/Xi observable,

\[
\xi(\rho)=0
\stackrel{R0}{\Longrightarrow}
E_{\rm rel}(\rho)=0.
\]

Then the derived coercivity theorem completes the critical-line implication.

## 6. Occam closure theorem

Under normalized complementarity, the derived relational energy above, and R0, every non-trivial zeta zero satisfies

\[
\Re\rho=\frac12.
\]

Hence

\[
\boxed{
\mathsf O_{\rm rel}\vdash\mathrm{RH}.
}
\]

The energy/coercivity layer is theorem-level inside the declared relational model. The only genuinely foundational step is R0.

## 7. External proof firewall

In ordinary mathematics, R0 specialized to all non-trivial zeta zeros is not yet an independently proved theorem. Because the formal layer proves that zero reciprocal/half-axis defect on all non-trivial zeros is RH-equivalent, R0 cannot be counted as an independent resolution unless it is established as a general theorem about the analytic observable without importing RH.

This does not weaken the internal Occam closure. It identifies the exact logical status:

- energy/coercivity: DERIVED;
- U(1) half-turn coordinate: DERIVED;
- critical-line zero locus: DERIVED;
- RH from relational-zero realization: DERIVED;
- universal relational-zero realization R0: FOUNDATIONAL AXIOM OF THE OCCAM SYSTEM.

Q.E.D. for the energy derivation and for RH inside the declared Occam relational system.