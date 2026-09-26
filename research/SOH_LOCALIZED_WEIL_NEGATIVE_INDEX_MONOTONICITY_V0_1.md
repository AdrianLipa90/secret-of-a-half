# SOH Localized Weil Negative-Index Monotonicity v0.1

Status: **EXACT_DOMAIN_MONOTONICITY / PONTRYAGIN_INDEX_PERSISTS / DEFECT_ESCAPE_REQUIRES_SPECTRAL_MIGRATION**

Date: 2026-09-26

Parents:
- \`research/SOH_C005_SPECTRAL_FLOW_FRONTIER_V0_1.md\`
- \`research/SOH_DE_BRANGES_PONTRYAGIN_COMPLEMENT_V0_1.md\`

No RH and no zero list are used.

## 1. Nested localized form domains

For
\[
0<a_1<a_2,
\]
the compactly supported core on the smaller interval embeds into the larger
one by zero extension:
\[
C_c^\infty(-a_1,a_1)
\hookrightarrow
C_c^\infty(-a_2,a_2).
\]

The localized Weil form is the restriction of the same global arithmetic form,
so zero extension preserves its value:
\[
Q_W^{a_2}(\widetilde f,\widetilde g)
=
Q_W^{a_1}(f,g)
\]
for functions supported in \((-a_1,a_1)\).

The same inclusion persists after closed-form completion.

## 2. Negative subspaces persist

Let
\[
V\subset\mathfrak D(Q_W^{a_1})
\]
be a finite-dimensional subspace on which
\[
Q_W^{a_1}[v]<0
\qquad
(v\in V\setminus\{0\}).
\]

Extend every vector by zero to \((-a_2,a_2)\). Then
\[
Q_W^{a_2}[\widetilde v]
=
Q_W^{a_1}[v]
<0.
\]

Therefore the image of \(V\) is again a negative subspace of the larger
localized form.

Hence the Morse/negative index obeys
\[
\boxed{
\kappa_{a_1}
\le
\kappa_{a_2},
\qquad
\kappa_a:=n_-(A_a).
}
\]

Thus
\[
\boxed{
a\mapsto\kappa_a
\text{ is non-decreasing and integer-valued.}
}
\]

## 3. Persistence after first-correction renormalization

For every admissible \(t\),
\[
C_{a,t}
=
tA_a(I+tA_a)^{-1}
\]
has
\[
n_-(C_{a,t})=\kappa_a.
\]

The de Branges--Pontryagin complement
\[
K_0-K_t
\]
therefore has negative-square index
\[
\kappa_a.
\]

Combining with Section 2,
\[
\boxed{
a_1<a_2
\Longrightarrow
\operatorname{ind}_-(K_0^{(a_1)}-K_t^{(a_1)})
\le
\operatorname{ind}_-(K_0^{(a_2)}-K_t^{(a_2)}).
}
\]

The indefinite defect cannot disappear by index cancellation at larger
localization radius.

## 4. Consequence for the generalized-Schur route

Suppose
\[
\kappa_{a_0}>0
\]
for some \(a_0\).

Then
\[
\boxed{
\kappa_a\ge1
\qquad
\forall a\ge a_0.
}
\]

Therefore an ordinary-Schur limit, if obtained without proving finite-scale
positivity, cannot arise because
\[
\kappa_a\to0.
\]

The only remaining mechanism is **local defect escape**:
the poles/negative-square witnesses of any Kreĭn--Langer realization must leave
every fixed compact subset relevant to the limiting characteristic.

Thus the correct asymptotic statement is not
\[
\kappa_a\to0,
\]
which is impossible after the first negative scale, but rather a localization
statement about where the defect lives.

## 5. Connection to high-mode coercivity

Yoshida/Suzuki high-mode coercivity states that for every bounded scale range

\[
0<a\le a_0
\]

and every prescribed positive coercivity margin, sufficiently high Fourier
modes are positive uniformly in that bounded \(a\)-range.

Let \(K_N(a)\) be the high Fourier subspace \(|n|>N\). If the localized form
is strictly positive on \(K_N(a)\), then any negative subspace has dimension
at most the codimension of \(K_N(a)\). Hence

\[
\boxed{
\kappa_a=n_-(A_a)\le 2N+1.
}
\]

Indeed, any subspace of dimension \(>2N+1\) must intersect \(K_N(a)\)
nontrivially, contradicting strict positivity there.

**Correction to the earlier working interpretation.** High-block positivity
does not imply that every negative eigenvector is literally supported only on
the low Fourier modes. Low/high coupling may give a negative eigenvector a
nonzero high-mode tail. What is finite-dimensional is the negative index and,
after an admissible high-block inverse is supplied, the corresponding
Schur/Feshbach coordinate problem.

Therefore a growth law for a sufficient cutoff \(N_{\rm cert}(a)\) gives a
rigorous upper envelope

\[
\boxed{
\kappa_a\le 2N_{\rm cert}(a)+1,
}
\]

but by itself it does **not** prove a frequency-support law for the defect and
does not imply a necessary escape condition \(N(a)/a\to\infty\).

To turn cutoff growth into a compact-defect obstruction one still needs the
explicit generalized-Schur/Feshbach transfer controlling the high-mode tail
that is slaved to the finite low coordinates.

## 6. Refined defect-escape gate

### LIV-MD2c5P3a — index monotonicity
Status: **CLOSED / EXACT**.

\[
\kappa_a
\]
is non-decreasing.

### LIV-MD2c5P3b — frequency localization of the defect
Status: **OPEN / QUANTITATIVE**.

Obtain a certified large-\(a\) growth law for the minimal high-mode coercivity
cutoff
\[
N_{\rm coh}(a).
\]

### LIV-MD2c5P3c — compact defect obstruction or escape
Status: **OPEN / STRUCTURAL**.

Combine the cutoff law with an explicit Kreĭn--Langer transfer to prove either:
- a persistent compact obstruction if any \(\kappa_a>0\); or
- genuine pole/defect escape compatible with the target limit.

## 7. Compact theorem

For
\[
0<a_1<a_2,
\]
zero extension gives
\[
\boxed{
n_-(A_{a_1})
\le
n_-(A_{a_2}).
}
\]

Hence once a localized negative direction appears, the Pontryagin index remains
positive at every larger scale.

Any ordinary-Schur limiting mechanism that does not prove finite-scale
positivity must therefore operate by **spectral migration of the defect**, not
by disappearance of its negative index.
