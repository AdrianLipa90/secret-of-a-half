# SOH Screw–GNS/Bochner Crosswalk and No-Go v0.1

Status: **EXACT_REDUCTION / DIRECT_SCREW_GNS_IS_RH_EQUIVALENT / INDEPENDENT_PD_KERNEL_ROUTE_OPEN**

Date: 2026-09-26

Parents:
- \`research/SOH_LOG_SCALE_CONTRACTION_GROUP_CRITICAL_LINE_CRITERION_V0_1.md\`
- \`research/SOH_SUZUKI_HEAT_SEMIGROUP_CAR_CROSSWALK_NOGO_V0_1.md\`
- \`research/SOH_C005_LOCALIZED_POSITIVITY_V0_1.md\`

External source:
- M. Suzuki, *Aspects of the screw function corresponding to the Riemann zeta-function*, 2023 / arXiv:2206.03682v4.

## 1. Existing zeta screw kernel

Let \(g\) be Suzuki's zeta screw function and let

\[
G_g(t,u)
=
g(t-u)-g(t)-g(-u)+g(0).
\]

The repository implements the same source-normalized object in
\`src/secret_of_a_half/zeta_screw.py\`.

Suzuki's theorem gives the global equivalence, on the stated admissible
localized test classes,

\[
\boxed{
\mathrm{RH}
\iff
\langle\phi,\phi\rangle_{G_g,a}\ge0
\quad
\text{for every }a>0.
}
\]

Therefore global non-negative definiteness of the screw form is already an
RH-equivalent condition.

Suzuki also gives the pointwise criterion

\[
\boxed{
\mathrm{RH}
\iff
\Psi(t)\ge0
\quad
\text{for all }t\in\mathbb R,
}
\]

with \(g=-\Psi\) in the repository convention.

## 2. What a direct GNS construction would require

A GNS/RKHS-style construction from \(G_g\) begins by declaring finite linear
combinations of formal vectors \(k_t\) and the sesquilinear form

\[
\left\langle
\sum_i c_i k_{t_i},
\sum_j d_j k_{u_j}
\right\rangle
=
\sum_{i,j}
\overline{c_i}d_j
G_g(t_i,u_j).
\]

For this to define a Hilbert seminorm, every finite Gram matrix

\[
[G_g(t_i,t_j)]_{i,j}
\]

must be positive semidefinite on the declared domain, equivalently the
associated integral/hermitian form must be non-negative on a dense test class.

Thus the incoming condition required by the direct screw-GNS construction is
precisely the global positivity condition that Suzuki identifies with RH.

Hence:

\[
\boxed{
\text{direct global GNS from the zeta screw kernel}
\not\Rightarrow
\text{new independent RH input}.
}
\]

It is an equivalent repackaging unless the needed positivity is independently
proved by a genuinely new arithmetic estimate.

## 3. Pointwise positivity is not enough

The statement

\[
G_g(t,u)\ge0
\]

pointwise on a region does not imply that the matrices

\[
[G_g(t_i,t_j)]
\]

are positive semidefinite for arbitrary finite point sets.

Likewise a finite set of positive numerical eigenvalues does not establish the
global kernel positivity needed by GNS.

Therefore:
- pointwise small-scale positivity;
- finite-grid PSD;
- one localized positive block;

may be useful diagnostics but do not supply the global GNS Hilbert space.

## 4. Local GNS does not automatically globalize

Suppose positivity is known on one bounded interval \((-a,a)\). Then one may
form a local quotient/completion on that interval.

To obtain a global scale representation one needs, in addition:

1. positivity for an exhausting family \(a\to\infty\);
2. consistency of the local embeddings;
3. a translation/scale action preserving the inner product;
4. strong continuity;
5. a zeta spectral-label intertwiner.

Failure at any one of these gates prevents promotion to the global group
required by SOH-MD003C.

In particular, the monotonic enlargement of the localization domain does not
preserve positivity automatically; that is exactly the C005/RH-hard issue.

## 5. Bochner does not rescue the same kernel

For a continuous translation-invariant positive-definite function \(C(a-b)\),
Bochner's theorem gives a positive measure \(\mu\) such that

\[
C(a-b)
=
\int_{\mathbb R}
e^{i(a-b)\gamma}\,d\mu(\gamma).
\]

The associated GNS representation of \(\mathbb R\) is unitary.

This is powerful only after positive definiteness has been proved
independently.

If \(C\) is manufactured from the zeta screw form by assuming the global
Suzuki positivity, the argument has merely replaced

\[
\mathrm{RH}
\iff
\text{Weil/screw positivity}
\]

by

\[
\text{assumed screw positivity}
\Longrightarrow
\text{GNS/Bochner unitary representation}.
\]

That is circular as an RH proof.

## 6. The genuinely independent route

The useful target is therefore not "GNS the existing screw kernel".

It is:

### SOH-MD004C — independent arithmetic positive-definite scale kernel

Construct, without RH, zero lists, global Weil positivity, or the Montgomery
target, a continuous translation-invariant kernel

\[
\boxed{
C_\zeta(a,b)=C_\zeta(a-b)
}
\]

directly from theta/prime/explicit-formula arithmetic such that:

1. \(C_\zeta\) is positive definite by an independent arithmetic theorem;
2. its GNS representation \(U(a)\) is the scale/log-translation
   representation relevant to the zeta object;
3. a zero-list-free intertwiner identifies every nontrivial zeta spectral
   channel with the character
   \[
   e^{a(\rho-1/2)};
   \]
4. the identification is complete enough that no nontrivial zero channel is
   omitted.

Then the GNS representation is unitary, so every represented character has
unit modulus and the critical line follows.

## 7. Exact Bochner character criterion

Every one-dimensional continuous unitary character of \((\mathbb R,+)\) is

\[
a\mapsto e^{ia\gamma},
\qquad
\gamma\in\mathbb R.
\]

Suppose an independently constructed unitary scale representation contains a
non-zero vector \(v_\rho\) satisfying

\[
U(a)v_\rho
=
e^{a(\rho-1/2)}v_\rho
\qquad
\forall a\in\mathbb R.
\]

Taking norms gives

\[
\|v_\rho\|
=
\|U(a)v_\rho\|
=
e^{a(\Re\rho-1/2)}
\|v_\rho\|.
\]

For any nonzero \(a\),

\[
e^{a(\Re\rho-1/2)}=1.
\]

Therefore

\[
\boxed{
\Re\rho=\frac12.
}
\]

This is the GNS/Bochner version of SOH-MD003A.

## 8. Relation to the CAR criterion

The two open constructions can now be compared cleanly.

### CAR route

Construct a positive contraction with occupation weights

\[
q^{2\Re\rho-1}.
\]

Then reflection forces the critical line.

### GNS/Bochner route

Construct an independently positive-definite scale kernel whose unitary
representation carries the characters

\[
e^{a(\rho-1/2)}.
\]

Then unitarity forces the critical line directly.

Both require a zero-list-free zeta spectral-label theorem. Neither is supplied
by the mere occurrence of prime shifts at \(\pm\log n\).

## 9. Strong no-go statement

The following three shortcuts are not independent proof routes:

\[
\boxed{
\text{global GNS of Suzuki }G_g
}
\]

because its required positivity is RH-equivalent;

\[
\boxed{
e^{-tA_a}\text{ contractive}
}
\]

because that is exactly \(A_a\ge0\);

and

\[
\boxed{
\text{ordinary translation group on }L^2(\mathbb R)
}
\]

because it lacks the zeta spectral intertwiner.

Thus the surviving operator target is sharply typed:

\[
\boxed{
\text{independent arithmetic PD kernel}
+
\text{zero-list-free zeta character intertwiner}.
}
\]

## 10. Compact theorem/no-go

### Theorem — direct screw-GNS no-go

A direct GNS construction using Suzuki's zeta screw kernel \(G_g\) as its
inner-product kernel requires global non-negative definiteness of the
corresponding screw form. By Suzuki's theorem this global condition is
equivalent to RH. Therefore such a direct GNS construction is not an
independent incoming edge to an RH proof unless that positivity is established
by a new, non-RH-equivalent arithmetic argument.

### Criterion — independent Bochner scale kernel

If an independently proved continuous positive-definite arithmetic kernel on
\(\mathbb R\) has a GNS representation containing every zeta channel with
character \(e^{a(\rho-1/2)}\), then every represented nontrivial zero obeys

\[
\Re\rho=\frac12.
\]

Q.E.D. for both implications under their stated hypotheses.
