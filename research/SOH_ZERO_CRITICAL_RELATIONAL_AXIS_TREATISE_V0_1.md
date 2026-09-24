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

## 10. The Occam axiomatic RH theorem

Define the minimal Occam system \(\mathsf O\) by O1-O2 together with the following single analytic closure axiom.

### O3 — canonical zero-energy coercivity

There exist a canonical energy \(E\) and \(c>0\), independently defined from the zeta-side analytic structure, such that every non-trivial zeta zero \(\rho\) satisfies

\[
E(\rho)=0
\]

and

\[
c\,\Delta_{\rm RC}(\Omega(\rho))\le E(\rho).
\]

### Theorem 4 — RH in the Occam relational system

\[
\boxed{
\mathsf O\vdash\mathrm{RH}.
}
\]

**Proof.** Let \(\rho\) be any non-trivial zeta zero. O3 gives \(E(\rho)=0\) and \(c\Delta_{\rm RC}(\Omega(\rho))\le E(\rho)\), with \(c>0\). Non-negativity of \(\Delta_{\rm RC}\) forces \(\Delta_{\rm RC}(\Omega(\rho))=0\). The exact reciprocal-conjugation theorem gives \(\Re\rho=1/2\). Since \(\rho\) was arbitrary, every non-trivial zero lies on the critical line. Q.E.D.

This is a genuine axiomatic proof: once O3 is admitted, no further conjectural step remains in the channel.

---

## 11. Why this does not yet constitute an unconditional proof of RH

The same formal Lean layer proves

`zeroHalfAxisDefect_iff_riemannHypothesis`

and

`zeroReciprocalDefect_iff_riemannHypothesis`.

Therefore the statement

\[
\forall\rho\in Z_{\rm nt}(\zeta):\quad
\Delta_{\rm RC}(\Omega(\rho))=0
\]

is itself RH-equivalent.

This produces a strict proof firewall:

- If O3 is **independently derived** from already proved analytic/operator structure without importing an RH-equivalent premise, the proof is complete in ordinary mathematics.
- If O3 is merely **postulated**, Theorem 4 is a valid proof inside the enlarged axiomatic system but not an independent resolution of RH.

Thus the Occam channel is structurally closed, but the analytic incoming edge must still be earned.

This distinction is not cosmetic. It is exactly what prevents a definition of 'zero' from silently doing the work of the theorem that is supposed to be proved.

---

## 12. Minimum proof cost

The graph audit shows that several historical proof routes collapse onto the same transverse defect. The native half-axis defect, the reciprocal-conjugation defect, and the Suzuki imaginary-coordinate defect are exact crosswalks of one geometric quantity.

Therefore the minimum independent burden is not to prove PF-infinity, complete monotonicity, Collatz conjugacy, spinorial closure, and the state-map bridge simultaneously. For this channel the minimum burden is one theorem:

\[
\boxed{
\text{construct canonical }E
\text{ with }E(\rho)=0
\text{ and }E\ge c\Delta_{\rm RC},
\quad c>0.
}
\]

Once that is proved, every remaining edge is exact.

This is the lowest-cost proof path presently exposed by the repository.

---

## 13. Three independent views of the same center

The purpose of the three-sided derivation is not rhetorical redundancy. Each side rules out a different hidden assumption.

### Side A — relational algebra

\[
J(\sigma)=1-\sigma
\quad\Rightarrow\quad
\operatorname{Fix}(J)=\{1/2\}.
\]

This route needs no probability theory.

### Side B — information geometry

\[
D_{\rm KL}(p\|u)=0
\quad\Rightarrow\quad
p=u=(1/2,1/2).
\]

This route needs no projective zeta coordinate.

### Side C — projective/operator geometry

\[
\Delta_{\rm RC}(\Omega(s))=0
\quad\Rightarrow\quad
\Re s=1/2.
\]

This route is the one already connected to the formal RH endgame in Lean.

The intersection is therefore

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

## 14. Conservation-language interpretation

Within the declared model, departure from the center creates a positive information defect:

\[
x\neq0
\Longrightarrow
D_H>0.
\]

If an independently derived physical or operator energy is coercive with respect to that defect, then a zero-energy state cannot live away from the center.

This is the mathematically controlled version of the statement:

> distinction costs; exact zero-energy balance cannot carry transverse relational imbalance.

The phrase is interpretive; the equations above are the theorem.

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

### SOH-RZ006 — coercive zero-energy RH theorem

\[
\left(
E(\rho)=0
\land
c\Delta_{\rm RC}(\Omega(\rho))\le E(\rho)
\right)
\quad\forall\rho\in Z_{\rm nt}(\zeta)
\Longrightarrow
\mathrm{RH}.
\]

### SOH-RZ007 — proof-cost firewall

\[
\left[
\Delta_{\rm RC}(\Omega(\rho))=0
\text{ for every non-trivial zero }\rho
\right]
\iff
\mathrm{RH}.
\]

Hence the Occam axiomatic channel is completely closed as an implication, while an unconditional RH proof requires an independent derivation of the single incoming analytic energy edge.

---

## Conclusion

Zero in the Secret-of-a-Half relational algebra is the critical axis of a normalized relation: the unique exchange-fixed center, the unique zero of the Shannon/KL imbalance, the simultaneous Lagrange node of a positive relational defect, and the zero locus of the projective reciprocal-conjugation defect.

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

For the Riemann problem, the geometric and logical endgame is already formalized. The minimal Occam system O1-O3 proves RH, and the proof channel contains no further gap after O3. The repository also proves that the bare zero-defect-on-all-zeros statement is RH-equivalent, so O3 cannot be counted as an independent resolution until it is derived from non-circular analytic structure.

That is the exact current boundary:

\[
\boxed{
\text{Occam axiomatic RH channel: CLOSED}
}
\]

\[
\boxed{
\text{independent derivation of the canonical zero-energy coercivity edge: OPEN}.
}
\]

Q.E.D. for the relational zero triad and for RH inside the declared Occam axiomatic system.