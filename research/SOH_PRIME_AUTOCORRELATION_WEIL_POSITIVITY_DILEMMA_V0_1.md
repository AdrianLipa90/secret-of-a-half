# SOH Prime-Autocorrelation vs Weil-Positivity Spectral Dilemma v0.1

Status: **EXACT_PRIME_SIDE_PD / EXACT_SPECTRAL_SUPPORT / WEIL_SIDE_RH_EQUIVALENT / POSITIVE_INTERTWINER_OPEN**

Date: 2026-09-26

Parents:
- \`research/SOH_SCREW_GNS_BOCHNER_CROSSWALK_NOGO_V0_1.md\`
- \`research/SOH_LOG_SCALE_CONTRACTION_GROUP_CRITICAL_LINE_CRITERION_V0_1.md\`
- On-Primes phase-bank/form-factor duality and Fejér autocorrelation line.

## 1. An unconditional positive-definite prime kernel

Let \(I\) be any finite set of positive integers and let \(b_n\in\mathbb C\).

Define

\[
\boxed{
C_I(a,b)
=
\sum_{n\in I}
|b_n|^2
e^{i(a-b)\log n}.
}
\]

For arbitrary points \(a_1,\ldots,a_m\in\mathbb R\) and coefficients
\(c_1,\ldots,c_m\),

\[
\sum_{j,k}
\overline{c_j}c_k C_I(a_j,a_k)
=
\sum_{n\in I}
|b_n|^2
\left|
\sum_j c_j e^{-ia_j\log n}
\right|^2
\ge0.
\]

Therefore

\[
\boxed{
C_I
\text{ is positive definite unconditionally.}
}
\]

The same statement extends to countable square-summable weights whenever the
sum converges in the declared topology.

## 2. Its GNS spectrum is arithmetic, not the zeta-zero spectrum

The feature map may be written explicitly as

\[
\Phi(a)
=
\left(
b_n e^{-ia\log n}
\right)_{n\in I}
\in\ell^2(I).
\]

Translation acts by

\[
(U(t)\Phi(a))_n
=
\Phi(a+t)_n
=
e^{-it\log n}\Phi(a)_n.
\]

Hence the GNS/feature-space representation is unitary and its spectral
frequencies are exactly

\[
\boxed{
\{\log n:n\in I,\ b_n\ne0\}.
}
\]

For von-Mangoldt weights, the nonzero arithmetic support reduces to prime
powers.

Thus unconditional positive definiteness on the prime side does **not**
produce a Hilbert--Pólya operator for the zeta ordinates.

## 3. The zero-side quadratic form has the complementary problem

The Guinand--Weil explicit formula converts suitable linear test-function
observables between prime/archimedean data and zero data.

But the natural zero-sensitive quadratic form is the Weil form.

For the complete admissible test class,

\[
\boxed{
Q_W(f)\ge0\ \forall f
\iff
\mathrm{RH}
}
\]

under the standard Weil criterion.

Likewise, the Suzuki screw form gives an RH-equivalent global positivity
condition.

Therefore the straightforward zero-side Hilbert construction has the desired
spectral information but does not have an independently available global
positive metric.

## 4. The spectral-positivity dilemma

The two obvious Hilbert-space constructions therefore supply complementary
halves:

### Prime autocorrelation GNS

\[
\boxed{
\text{positivity: CLOSED unconditionally}
}
\]

but

\[
\boxed{
\text{spectral labels: }\log p^m,\ \text{not }\gamma.
}
\]

### Weil/screw GNS

\[
\boxed{
\text{zeta spectral sensitivity: PRESENT}
}
\]

but

\[
\boxed{
\text{global positivity: RH-equivalent}.
}
\]

This is the exact spectral-positivity dilemma.

## 5. Why the explicit formula does not automatically solve it

A linear explicit-formula identity does not imply that the prime-side
\(\ell^2\) metric is transported to a positive zero-side metric.

In particular,

\[
\text{linear equality of distributions}
\]

does not imply

\[
\text{unitary equivalence of the two Hilbert representations}.
\]

To close the gap, one needs a map with metric control.

## 6. Positive-intertwiner target

Define the new gate:

### SOH-MD004D — positive prime-to-zeta intertwiner

Construct, without a zero list and without RH, a densely defined map

\[
\boxed{
\mathcal J_\zeta:
\mathcal H_{\rm prime}
\to
\mathcal H_{\rm zeta}
}
\]

such that:

1. \(\mathcal H_{\rm prime}\) carries the unconditional prime-side unitary
   log-scale representation
   \[
   U_{\rm p}(a)e_n=e^{ia\log n}e_n;
   \]
2. \(\mathcal J_\zeta\) intertwines scale translation:
   \[
   \mathcal J_\zeta U_{\rm p}(a)
   =
   U_\zeta(a)\mathcal J_\zeta;
   \]
3. the target zeta representation has channels
   \[
   U_\zeta(a)v_\rho
   =
   e^{a(\rho-1/2)}v_\rho;
   \]
4. positivity is transported independently, for example through a proved
   isometry/contraction/positive quotient relation;
5. completeness guarantees that every nontrivial zero channel appears;
6. no step uses RH, global Weil positivity, or a supplied zero table.

If these conditions hold with a unitary target representation, then

\[
\Re\rho=\frac12
\]

for every represented zero by the exact MD003/MD004 character criterion.

## 7. Intertwining obstruction

An ordinary bounded unitary intertwiner cannot simply relabel distinct
spectra.

If

\[
U_{\rm p}(a)
\]

has pure point frequencies \(\log n\), while

\[
U_\zeta(a)
\]

has frequencies \(\gamma\), a unitary equivalence would require equality of the
corresponding spectral measures/multiplicities.

Therefore a valid \(\mathcal J_\zeta\) is unlikely to be a trivial unitary
basis change from the raw prime autocorrelation space.

It must involve at least one of:
- a quotient/compression;
- a scattering or transfer construction;
- an unbounded transform with controlled domain;
- a reproducing-kernel completion;
- a relative trace/determinant construction.

This prevents the false shortcut
\[
\log p^m \equiv \gamma.
\]

## 8. Relation to the explicit formula

The explicit formula should be viewed as a candidate **distributional
intertwining relation**, not yet a Hilbert-space isometry.

The proof obligation is to upgrade

\[
\boxed{
\text{prime distribution identity}
\longleftrightarrow
\text{zero distribution identity}
}
\]

to a positive metric statement strong enough to define \(U_\zeta\).

That metric upgrade is precisely where Weil positivity enters in the standard
route.

A genuinely new proof must obtain the needed metric control from a weaker,
independent arithmetic structure.

## 9. Exact theorem/no-go

### Theorem — unconditional prime-side GNS

Every finite kernel
\[
C_I(a,b)
=
\sum_{n\in I}|b_n|^2e^{i(a-b)\log n}
\]
is positive definite and has a unitary translation representation whose
spectral support is the arithmetic set \(\{\log n\}\).

### No-go — positivity alone does not transfer zeta labels

This unconditional GNS construction does not realize the zeta-zero channels.
Conversely, using the global Weil/screw metric to obtain the zero-side Hilbert
space imports an RH-equivalent positivity condition.

Therefore the missing object is a noncircular positive prime-to-zeta
intertwiner, not merely another positive kernel or another linear explicit
formula. Q.E.D.
