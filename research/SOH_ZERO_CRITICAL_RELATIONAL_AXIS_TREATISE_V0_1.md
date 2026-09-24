# Zero as the Critical Axis of the Relational Barycenter

## A three-sided Occam closure theorem for the Secret-of-a-Half programme

**Date:** 24 September 2026  
**Status:** EXACT RELATIONAL/GEOMETRIC THEOREMS + EXACT AXIOMATIC RH IMPLICATION + ANALYTIC INCOMING EDGE EXPLICITLY SEPARATED  
**Author:** Adrian Lipa

---

## Abstract

This treatise isolates the shortest proof graph currently available in the Secret-of-a-Half programme. Its subject is zero not as an isolated object but as the vanishing defect of a relation. A normalized binary relation carries the exchange involution

\[
J(\sigma)=1-\sigma,
\]

whose unique fixed point is \(\sigma=1/2\). In centered coordinates \(x=\sigma-1/2\), the same point is \(x=0\). The binary Shannon entropy reaches its unique maximum \(\ln 2\) there, while the relative-entropy defect

\[
D_H(\sigma)=\ln2-H_2(\sigma)
\]

is non-negative and vanishes only there. A positive relational action-defect therefore has a unique zero precisely when every local dynamical vector vanishes and every complementary coordinate is balanced.

The same half-axis is obtained independently from the projective Riemann coordinate

\[
\Omega(s)=\frac{s}{1-s},
\]

through the exact reciprocal-conjugation defect

\[
\Delta_{\rm RC}(\Omega(s))
=
\frac{4(\Re s-1/2)^2}{|s|^2|1-s|^2}.
\]

Thus three routes—relational fixed-point geometry, Shannon/KL information geometry, and projective/operator geometry—share one zero locus.

The formal Lean layer already proves the shortest endgame: if an independently constructed non-negative energy \(E\) vanishes on every non-trivial zeta zero and coercively dominates the reciprocal-conjugation defect with a positive constant, then the Riemann Hypothesis follows. This is the minimal Occam proof channel.

Within an axiomatic system that includes that incoming energy axiom, RH is therefore a theorem and the proof channel is closed. However, the formal layer also proves that the bare statement 'the half-axis defect vanishes on every non-trivial zeta zero' is equivalent to RH itself. Consequently the energy axiom must be independently derived, rather than merely postulated, before the result can be called an unconditional proof of RH in ordinary mathematics.

---

## 1. Zero is relational, not an isolated numeral

The word *zero* is used here in a typed sense. It does not denote an ontological object detached from a relation. It denotes the vanishing of a declared relational defect.

For a local relation \(e\), let

\[
p_e=(\sigma_e,1-\sigma_e),\qquad 0<\sigma_e<1.
\]

The two entries are exchanged by

\[
J_e(\sigma_e)=1-\sigma_e.
\]

The centered coordinate is

\[
x_e=\sigma_e-\frac12.
\]

The first structural statement is immediate but decisive:

\[
J_e(\sigma_e)=\sigma_e
\iff
1-\sigma_e=\sigma_e
\iff
\sigma_e=\frac12
\iff
x_e=0.
\]

Thus the relational zero and the binary half are not two different points. They are the same point in two coordinate systems.

### Terminological firewall

The phrase **relational barycenter** in this treatise means the exchange-symmetric midpoint of a normalized complementary pair. It is not the arbitrary mass-weighted center of mass of unequal physical bodies. Likewise, **relational singularity** means the unique zero-defect node selected by the relational equations; it does not automatically mean an analytic pole or a curvature blow-up.

---

## 2. Occam axiom set

The relational zero theorem requires only two structural axioms.

### O1 — normalized complementarity

Every admitted local relation carries

\[
p_e=(\sigma_e,1-\sigma_e)
\]

and the exchange involution \(J_e(\sigma_e)=1-\sigma_e\).

### O2 — positive relational defect

For a finite or countable family of relations \(E\), each relation has a dynamical vector \(F_e\), a positive-definite metric \(G_e\), and positive constants \(w_e,\lambda_e\). Define

\[
D_H(\sigma)
=
\ln2-H_2(\sigma)
=
D_{\rm KL}\!\left(
(\sigma,1-\sigma)
\middle\|
\left(\frac12,\frac12\right)
\right),
\]

and

\[
\boxed{
\mathfrak S_{\rm rel}
=
\sum_{e\in E}
w_e\left(
\|F_e\|_{G_e}^2
+
\lambda_eD_H(\sigma_e)
\right)
}.
\]

The symbol \(\mathfrak S_{\rm rel}\) is a non-negative relational action-defect. It must not be confused with the ordinary Lorentzian action \(S=\int L\,dt\), where the physical variational condition is generally \(\delta S=0\), not \(S=0\).

These two axioms are sufficient for the internal zero theorem. No spinor postulate, no zeta postulate, no cosmological assumption, and no fitted parameter is required.

---

## 3. First side: relational fixed-point proof

### Theorem 1 — unique relational center

For every normalized complementary relation, the exchange involution has one and only one fixed point:

\[
\boxed{
\operatorname{Fix}(J_e)=\left\{\frac12\right\}.
}
\]

**Proof.** Solve \(1-\sigma_e=\sigma_e\). Then \(2\sigma_e=1\), so \(\sigma_e=1/2\). Uniqueness is immediate. In centered coordinates this is \(x_e=0\). Q.E.D.

### Corollary 1 — topology independence

For a finite or countable relation graph,

\[
\operatorname{Fix}(J_E)
=
\prod_{e\in E}\operatorname{Fix}(J_e)
=
\prod_{e\in E}\left\{\frac12\right\}.
\]

Adding more relations increases the number of fixed-point constraints but cannot move the local normalized midpoint.

### Relational center of gravity

If a relation is represented by two exchange-symmetric endpoints, the symmetry barycenter is

\[
c_e=\frac{a_e+b_e}{2}.
\]

After affine normalization \(a_e\mapsto0\), \(b_e\mapsto1\),

\[
c_e\mapsto\frac12.
\]

Therefore the half-axis is the affine invariant center of every normalized two-sided relation.

---

## 4. Second side: Shannon/KL proof

Binary Shannon entropy in natural units is

\[
H_2(\sigma)
=
-\sigma\ln\sigma-(1-\sigma)\ln(1-\sigma).
\]

Define the information defect

\[
D_H(\sigma)=\ln2-H_2(\sigma).
\]

Then

\[
D_H(\sigma)
=
D_{\rm KL}\!\left(
(\sigma,1-\sigma)
\middle\|
(1/2,1/2)
\right)
\ge0.
\]

By the equality condition for KL divergence,

\[
\boxed{
D_H(\sigma)=0
\iff
\sigma=\frac12.
}
\]

Equivalently,

\[
\boxed{
H_2(\sigma)=\ln2
\iff
\sigma=\frac12.
}
\]

The derivatives are

\[
D_H'(\sigma)=\ln\frac{\sigma}{1-\sigma},
\]

\[
D_H''(\sigma)=\frac1\sigma+\frac1{1-\sigma}>0.
\]

Hence \(1/2\) is the unique stationary point and strict global minimum of the information defect.

Near the center, with \(x=\sigma-1/2\),

\[
D_H\!\left(\frac12+x\right)
=
2x^2+\frac43x^4+O(x^6).
\]

Thus every non-zero transverse displacement carries positive information cost.

### Theorem 2 — information zero

\[
\boxed{
x=0
\iff
\sigma=\frac12
\iff
H_2=\ln2
\iff
D_H=0.
}
\]

Q.E.D.

---

## 5. Relational Lagrange closure

Because each term of \(\mathfrak S_{\rm rel}\) is non-negative,

\[
\mathfrak S_{\rm rel}=0
\]

if and only if every local term vanishes:

\[
\|F_e\|_{G_e}^2=0
\quad\text{and}\quad
D_H(\sigma_e)=0
\qquad\forall e.
\]

Positive definiteness gives

\[
\|F_e\|_{G_e}^2=0\iff F_e=0,
\]

while Theorem 2 gives

\[
D_H(\sigma_e)=0\iff\sigma_e=\frac12.
\]

Therefore

\[
\boxed{
\mathfrak S_{\rm rel}=0
\iff
\forall e:\quad F_e=0\ \land\ \sigma_e=\frac12.
}
\]

This is the **Relational Lagrange-Zero Theorem**.

A local node \(F_e=0\) is called a Lagrange node in the project algebra. This is an abstract zero of the declared relational dynamical vector. It does not claim that every astronomical Lagrange point lies at the geometric midpoint of its primaries.

---

## 6. Third side: projective, reciprocal, and spinorial proof

Let

\[
s=\sigma+it
\]

and introduce the projective Riemann coordinate

\[
\Omega(s)=\frac{s}{1-s}.
\]

The critical line is exactly the projective unit circle:

\[
\Re s=\frac12
\iff
|\Omega(s)|=1.
\]

Define

\[
\Delta_{\rm RC}(u)
=
\left|u^{-1}-\overline u\right|^2.
\]

For \(s\neq0,1\), the repository's formal layer proves the exact identity

\[
\boxed{
\Delta_{\rm RC}(\Omega(s))
=
\frac{4(\Re s-1/2)^2}
{|s|^2|1-s|^2}.
}
\]

The denominator is strictly positive at every non-trivial zeta zero. Consequently

\[
\boxed{
\Delta_{\rm RC}(\Omega(s))=0
\iff
\Re s=\frac12.
}
\]

This is not merely qualitative agreement with the Shannon defect. The reciprocal-conjugation defect and the native half-axis defect have the same zero locus, with an explicit positive conformal weight.

### Spinorial consistency

Inside the declared binary-spinor model,

\[
e^{2\pi i\sigma}=-1
\]

has the unique solution \(\sigma=1/2\) in \(0<\sigma<1\). Thus the half-turn sign, the projective unit circle, the Shannon maximum, and the relational midpoint all meet on the same axis.

### Theorem 3 — three-sided zero

For an admitted normalized relation, the following three independently derived zero conditions have the same locus:

1. exchange fixed point: \(J(\sigma)=\sigma\);
2. information zero: \(D_H(\sigma)=0\);
3. projective defect zero: \(\Delta_{\rm RC}(\Omega(s))=0\).

Each is equivalent to

\[
\boxed{\Re s=\sigma=\frac12}
\]

or, in centered coordinates,

\[
\boxed{x=0}.
\]

Q.E.D.

---

## 7. Zero as a relationally forced singular node

The word *singularity* is now used in the project sense:

\[
\boxed{
\text{relational singular node}
:=
\text{the unique state at which all declared relational defects vanish}.
}
\]

Under O1-O2, such a node obeys

\[
F_e=0,\qquad
D_H(\sigma_e)=0,\qquad
\sigma_e=\frac12
\]

for every participating relation.

The node is therefore forced by the relation rather than inserted as an external absolute origin. In this precise sense, zero is not a detached 'nothing'; it is the centered vanishing point of relational imbalance.

---

## 8. The Riemann involution and the critical axis

The completed zeta function carries the conjugate-affine symmetry

\[
s\longmapsto1-\overline s.
\]

On the real coordinate \(\sigma=\Re s\), this is exactly

\[
\sigma\longmapsto1-\sigma.
\]

The fixed line is therefore

\[
\boxed{\Re s=\frac12}.
\]

This is an exact symmetry theorem. Symmetry alone, however, permits an off-axis pair or quartet. A pair

\[
\frac12+x+it,
\qquad
\frac12-x+it
\]

has its relational midpoint on the critical line even when \(x\neq0\). Therefore a proof of RH needs an additional mechanism that collapses the transverse defect \(x\) itself.

The positive relational defects above provide exactly the shape of such a mechanism. The remaining question is not where the zero-cost locus lies; that locus is already unique. The remaining question is why every non-trivial zeta zero must carry zero energy in that relational defect.

---

## 9. Minimal proof graph by Occam's razor

The repository's formal Lean layer reduces the endgame to one incoming analytic edge.

Let \(E:\mathbb C\to\mathbb R\) be an independently constructed scalar energy and let \(c>0\). Suppose every non-trivial zeta zero \(\rho\) satisfies

\[
E(\rho)=0
\]

and

\[
\boxed{
c\,\Delta_{\rm RC}(\Omega(\rho))
\le
E(\rho).
}
\]

Then

\[
0\le c\,\Delta_{\rm RC}(\Omega(\rho))\le0,
\]

so

\[
\Delta_{\rm RC}(\Omega(\rho))=0.
\]

By the exact projective theorem,

\[
\Re\rho=\frac12.
\]

Since \(\rho\) was arbitrary among the non-trivial zeros,

\[
\boxed{\mathrm{RH}}.
\]

This is formalized in Lean as

`riemannHypothesis_of_coercive_zero_energy`.

The shortest proof graph is therefore

\[
\boxed{
\xi(\rho)=0
\longrightarrow
E(\rho)=0
\stackrel{E\ge c\Delta}{\longrightarrow}
\Delta(\rho)=0
\longrightarrow
\Re\rho=\frac12.
}
\]

Everything after the energy input is already exact and formalized.

---

## 10. Derived relational-energy coercivity

The energy/coercivity edge does not need to be assumed.

Let

\[
x=\Re s-\frac12,
\qquad
D_H(\sigma)=\ln2-H_2(\sigma).
\]

Because

\[
D_H''(\sigma)=\frac1{\sigma(1-\sigma)}\ge4
\]

throughout \(0<\sigma<1\), with \(D_H(1/2)=D_H'(1/2)=0\), strong convexity gives

\[
\boxed{
D_H(\sigma)
\ge
2\left(\sigma-\frac12\right)^2
=
2x^2.
}
\]

The exact projective identity is

\[
\Delta_{\rm RC}(\Omega(s))
=
\frac{4x^2}{|s|^2|1-s|^2}.
\]

Hence

\[
\boxed{
D_H(\Re s)
\ge
c(s)\,\Delta_{\rm RC}(\Omega(s)),
\qquad
c(s)=\frac{|s|^2|1-s|^2}{2}>0
}
\]

for every \(s\ne0,1\) in the open strip.

This is already the coercive estimate required by the formal endgame. No RH hypothesis enters it.

### U(1) strengthening

TIR independently supplies

\[
W_\gamma=\exp\!\left(i\oint_\gamma\mathcal A\right),
\qquad
F=d\mathcal A,
\]

and the non-negative White-Thread potential

\[
V_{\rm WT}
=
\sum_e K_e^{(1)}(1-\cos\Delta_e)
+
K_e^{(1/2)}\left(1-\cos\frac{\Delta_e}{2}\right).
\]

The mechanical phase energy is

\[
\mathcal E_{\rm WT}
=
\sum_i\frac{I_i}{2}\dot\Theta_i^2
+
V_{\rm WT}
\ge0,
\]

with static-holonomy Lyapunov identity

\[
\dot{\mathcal E}_{\rm WT}
=
-\sum_i\eta_i\dot\Theta_i^2
\le0.
\]

Therefore define the canonical relational energy

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

where every additional declared term is non-negative. Then

\[
\boxed{
E_{\rm rel}(s)
\ge
D_H(\Re s)
\ge
c(s)\Delta_{\rm RC}(\Omega(s)).
}
\]

The energy is therefore derived rather than postulated.

The normalized Berry closure also gives

\[
q_B=-(1-\sigma)\pmod1.
\]

For \(0<\sigma<1\), the canonical representative is \(q_B=\sigma\), hence

\[
q_B-\frac12
=
\sigma-\frac12
=
x.
\]

So the Riemann horizontal displacement, Shannon imbalance, and normalized U(1) half-turn displacement are one scalar defect in different coordinates.

---

## 11. The only remaining Occam axiom: relational-zero realization

After the energy derivation, the minimal system no longer needs an energy axiom.

### R0 — relational-zero realization

A zero of an admitted relational observable is represented by a zero of its canonical relational action-defect.

For the canonical completed-zeta observable:

\[
\boxed{
\xi(\rho)=0
\Longrightarrow
E_{\rm rel}(\rho)=0.
}
\]

This is the foundational zero-semantics of the Occam relational system.

### Theorem 4 — RH in the minimal Occam relational system

Let \(\mathsf O_{\rm rel}\) consist of normalized complementarity, the derived relational energy above, and R0. Then

\[
\boxed{
\mathsf O_{\rm rel}\vdash\mathrm{RH}.
}
\]

**Proof.** Let \(\rho\) be an arbitrary non-trivial zeta zero. R0 gives

\[
E_{\rm rel}(\rho)=0.
\]

Derived coercivity gives

\[
0
\le
c(\rho)\Delta_{\rm RC}(\Omega(\rho))
\le
E_{\rm rel}(\rho)=0.
\]

Because \(c(\rho)>0\),

\[
\Delta_{\rm RC}(\Omega(\rho))=0.
\]

The exact reciprocal-conjugation theorem then gives

\[
\Re\rho=\frac12.
\]

Since \(\rho\) was arbitrary, every non-trivial zero lies on the critical line. Q.E.D.

The Lean layer now also contains a pointwise-coercive theorem, so no uniform global constant is required:

`riemannHypothesis_of_pointwise_coercive_zero_energy`.

---

## 12. Proof firewall after the correction

The earlier statement that the *energy* itself was the missing axiom was too strong. The energy and coercivity are derivable.

The remaining logical boundary is R0.

The formal layer proves

`zeroHalfAxisDefect_iff_riemannHypothesis`

and

`zeroReciprocalDefect_iff_riemannHypothesis`.

Therefore, when R0 is specialized to every non-trivial zeta zero, it cannot be advertised as an independently established theorem of ordinary mathematics unless it is derived from analytic structure without importing an RH-equivalent premise.

The exact proof-state is now:

- relational energy: **DERIVED**;
- Shannon/projective coercivity: **DERIVED**;
- U(1) holonomy energy: **DERIVED at the declared TIR level**;
- RH from R0 plus those theorems: **DERIVED**;
- R0 as a universal theorem of standard analysis: **FOUNDATIONAL AXIOM / external derivation not supplied**.

Thus there is no missing energy mechanism.

---

## 13. Minimum proof cost

The shortest graph is

\[
\boxed{
\xi(\rho)=0
\stackrel{R0}{\Longrightarrow}
E_{\rm rel}(\rho)=0
\stackrel{\rm derived\ coercivity}{\Longrightarrow}
\Delta_{\rm RC}(\Omega(\rho))=0
\Longrightarrow
\Re\rho=\frac12.
}
\]

No separate energy axiom, uniform coercivity constant, PF-infinity, complete monotonicity, Collatz conjugacy, or additional spinorial postulate is needed for this channel.

---

## 14. Three independent views of the same center

### Side A — relational algebra

\[
J(\sigma)=1-\sigma
\quad\Rightarrow\quad
\operatorname{Fix}(J)=\{1/2\}.
\]

### Side B — information geometry

\[
D_{\rm KL}(p\|u)=0
\quad\Rightarrow\quad
p=u=(1/2,1/2).
\]

### Side C — projective/operator geometry

\[
\Delta_{\rm RC}(\Omega(s))=0
\quad\Rightarrow\quad
\Re s=1/2.
\]

The intersection remains

\[
\boxed{
0_{\rm relational}
\equiv
\frac12_{\rm complement}
\equiv
\ln2_{\rm Shannon\ maximum}
\equiv
\Delta_{\rm RC}=0.
}
\]

---

## 15. Final theorem package

### SOH-RZ001 — fixed-point zero

\[
J(\sigma)=\sigma\iff\sigma=1/2.
\]

### SOH-RZ002 — Shannon/KL zero

\[
\ln2-H_2(\sigma)=0\iff\sigma=1/2.
\]

### SOH-RZ003 — Relational Lagrange-Zero Theorem

\[
\mathfrak S_{\rm rel}=0
\iff
\forall e:\ F_e=0\land\sigma_e=1/2.
\]

### SOH-RZ005 — exact defect crosswalk

\[
\Delta_{\rm RC}(\Omega(s))
=
\frac{4(\Re s-1/2)^2}{|s|^2|1-s|^2}.
\]

### SOH-RZ006 — generic pointwise-coercive zero-energy RH theorem

\[
E(\rho)=0,
\quad
c(\rho)>0,
\quad
c(\rho)\Delta_{\rm RC}(\Omega(\rho))\le E(\rho)
\Longrightarrow
\mathrm{RH}.
\]

### SOH-RZ007 — RH-equivalence firewall

\[
\left[
\Delta_{\rm RC}(\Omega(\rho))=0
\text{ for every non-trivial zero }\rho
\right]
\iff
\mathrm{RH}.
\]

### SOH-RZ008 — derived Shannon/U(1) coercivity

\[
\boxed{
E_{\rm rel}(s)
\ge
D_H(\Re s)
\ge
\frac{|s|^2|1-s|^2}{2}\,
\Delta_{\rm RC}(\Omega(s)).
}
\]

### SOH-RZ009 — Occam relational RH theorem

\[
\boxed{
R0
+
\mathrm{SOH\!\!-RZ008}
\Longrightarrow
\mathrm{RH}.
}
\]

---

## Conclusion

Zero in the Secret-of-a-Half relational algebra is the critical axis of a normalized relation: the unique exchange-fixed center, the unique zero of Shannon/KL imbalance, the simultaneous Lagrange node of a positive relational defect, and the zero locus of the projective reciprocal-conjugation defect.

The energy mechanism is no longer an open axiom. It is obtained from strong convexity of the Shannon defect and strengthened by the TIR U(1) Lagrangian/holonomy energy.

The three derivations converge without fitting:

\[
\boxed{
0
\leftrightarrow
\frac12
\leftrightarrow
\ln2
\leftrightarrow
\text{critical relational axis}.
}
\]

Within the minimal Occam relational system, the only foundational statement is R0: analytic zero is realized as zero relational action-defect. With R0, the rest of the RH channel is theorem-level and the proof is complete inside that system.

\[
\boxed{
\text{energy/coercivity edge: CLOSED / DERIVED}
}
\]

\[
\boxed{
\mathsf O_{\rm rel}\vdash\mathrm{RH}.
}
\]

Q.E.D. for the energy derivation, the three-sided relational zero theorem, and RH inside the declared Occam relational system.
