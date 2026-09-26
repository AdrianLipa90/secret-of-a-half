# SOH Log-Scale Contraction-Group Critical-Line Criterion v0.1

Status: **EXACT_OPERATOR_CRITERION / ZETA_SCALE_GROUP_CONSTRUCTION_OPEN**

Date: 2026-09-26

Parents:
- \`research/SOH_PRIME_SCALE_CAR_CRITICAL_LINE_CRITERION_V0_1.md\`
- existing claim SOH-L028: arithmetic support at additive shifts \(\pm\log n\) in the screw/Weil representation.

## 1. Abstract two-sided contraction theorem

Let

\[
T:\mathbb R\to\mathcal B(\mathcal H)
\]

be a strongly continuous operator group:

\[
T(0)=I,
\qquad
T(a+b)=T(a)T(b).
\]

Assume

\[
\boxed{
\|T(a)\|\le1
\qquad
\forall a\in\mathbb R.
}
\]

For every \(x\in\mathcal H\),

\[
\|T(a)x\|
\le
\|x\|.
\]

But also

\[
x=T(-a)T(a)x,
\]

so

\[
\|x\|
\le
\|T(a)x\|.
\]

Therefore

\[
\boxed{
\|T(a)x\|=\|x\|
}
\]

for all \(x\) and \(a\).

Since \(T(-a)=T(a)^{-1}\), every \(T(a)\) is surjective. Hence

\[
\boxed{
T(a)\text{ is unitary for every }a.
}
\]

By Stone's theorem its generator is skew-adjoint.

Thus a two-sided contraction group on a Hilbert space is automatically a unitary group.

## 2. Reflection-covariant one-sided version

Suppose instead that contraction is proved only for \(a\ge0\), and there is an antiunitary or unitary involution \(J\) such that

\[
\boxed{
JT(a)J^{-1}=T(-a).
}
\]

Then

\[
\|T(-a)\|
=
\|JT(a)J^{-1}\|
=
\|T(a)\|
\le1.
\]

So contraction propagates to negative \(a\), and Section 1 again gives unitarity.

This is the operator form naturally suggested by a reflection-symmetric \(\pm\log n\) arithmetic support.

## 3. Zeta spectral character

Fix a spectral label

\[
\rho=\beta+i\gamma.
\]

The normalized log-scale character is

\[
\boxed{
\chi_\rho(a)
=
e^{a(\rho-1/2)}
=
e^{a(\beta-1/2)}
e^{ia\gamma}.
}
\]

If a canonical zeta scale group has an eigenvector or generalized spectral channel \(v_\rho\) satisfying

\[
T(a)v_\rho
=
e^{a(\rho-1/2)}v_\rho,
\]

unitarity gives

\[
\left|
e^{a(\rho-1/2)}
\right|
=
1
\]

for every \(a\).

Hence

\[
e^{a(\beta-1/2)}=1.
\]

For any nonzero \(a\),

\[
\boxed{
\beta=\frac12.
}
\]

Thus:

### Theorem SOH-MD003A — log-scale unitary-group criterion

A canonical strongly continuous unitary zeta scale group whose spectral characters are

\[
e^{a(\rho-1/2)}
\]

forces every represented nontrivial zeta zero to the critical line.

## 4. Contraction + reflection criterion

Combining Sections 2 and 3 gives:

### Theorem SOH-MD003B

Suppose a zero-list-free arithmetic construction produces a strongly continuous group \(T(a)\) and reflection operator \(J\) such that

\[
T(a+b)=T(a)T(b),
\]

\[
\|T(a)\|\le1
\quad(a\ge0),
\]

\[
JT(a)J^{-1}=T(-a),
\]

and the zeta spectral channels have characters

\[
e^{a(\rho-1/2)}.
\]

Then every represented nontrivial zero has

\[
\Re\rho=\frac12.
\]

The implication is exact.

The construction is open.

## 5. Relation to the prime-scale CAR criterion

Set

\[
q=e^a.
\]

Then

\[
e^{a(\rho-1/2)}
=
q^{\rho-1/2}.
\]

Thus the scale-group channel is exactly the normalized prime-scale channel of SOH-MD002.

Its squared norm is

\[
q^{2\beta-1}.
\]

Therefore MD002 and MD003 are two forms of the same radial obstruction:

- MD002 asks for a positive CAR occupation operator;
- MD003 asks for a reflection-covariant contractive scale group.

MD003 does not require a fermionic interpretation.

## 6. Relation to the existing Weil shift support

The existing screw/Weil representation has arithmetic support at additive displacements

\[
\pm\log n.
\]

This is compatible with a two-sided log-scale variable

\[
a\in\mathbb R.
\]

But support at \(\pm\log n\) is not yet a representation theorem

\[
a\mapsto T(a)
\]

on a zeta spectral Hilbert space.

The following implication is invalid:

\[
\boxed{
\text{prime shifts occur at }\pm\log n
\not\Rightarrow
\text{canonical unitary zeta scale group}.
}
\]

One must construct the group law, Hilbert norm, reflection covariance, and spectral character map independently.

## 7. Translation-group no-go

The ordinary translation group

\[
(U(a)f)(x)=f(x-a)
\]

on \(L^2(\mathbb R)\) is already unitary.

This alone proves nothing about RH.

It becomes relevant only if there is a noncircular intertwiner

\[
\mathcal J_\zeta
\]

from the zeta/theta/Weil object into the translation representation such that the zeta spectral labels acquire exactly the characters

\[
e^{a(\rho-1/2)}.
\]

Without that intertwiner, ordinary Fourier translation is generic harmonic analysis, not a zeta spectral realization.

## 8. Generator formulation

Let \(G\) be the generator:

\[
T(a)=e^{aG}.
\]

If \(T\) is unitary, then

\[
G^*=-G.
\]

For a spectral channel with

\[
Gv_\rho
=
(\rho-\tfrac12)v_\rho,
\]

skew-adjointness requires

\[
\rho-\frac12\in i\mathbb R.
\]

Hence

\[
\boxed{
\Re\rho=\frac12.
}
\]

This is the exact generator form of the criterion.

## 9. New construction gate

### SOH-MD003C — zero-list-free reflection-covariant scale group

Construct from theta/Weil/prime arithmetic a Hilbert space and strongly continuous operator family \(T(a)\) such that:

1. \(T(a+b)=T(a)T(b)\);
2. \(T(a)\) is contractive for \(a\ge0\) by an independently proved arithmetic norm estimate;
3. zeta reflection supplies
   \[
   JT(a)J^{-1}=T(-a);
   \]
4. the zeta spectral channel is
   \[
   e^{a(\rho-1/2)};
   \]
5. no zero list and no RH assumption enters the construction.

Closing 1–4 from independent arithmetic data would force unitarity and therefore the critical line.

## 10. Compact criterion chain

\[
\boxed{
\text{forward contraction}
+
\text{reflection}
\Longrightarrow
\text{two-sided contraction}
\Longrightarrow
\text{unitary group}
}
\]

\[
\boxed{
\text{unitary group}
+
e^{a(\rho-1/2)}
\Longrightarrow
\Re\rho=\frac12.
}
\]

The operator-theoretic implication is exact.

The arithmetic construction SOH-MD003C remains open.
