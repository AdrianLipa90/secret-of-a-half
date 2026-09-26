# SOH Suzuki Heat-Semigroup ↔ CAR Crosswalk No-Go v0.1

Status: **EXACT_FUNCTIONAL_CALCULUS_REDUCTION / NO_NEW_RH_EDGE**

Date: 2026-09-26

Parents:
- \`research/SOH_PRIME_SCALE_CAR_CRITICAL_LINE_CRITERION_V0_1.md\`
- \`research/SOH_SUZUKI_LOCALIZED_OPERATOR_JOIN_V0_1.md\`
- \`research/SOH_C005_SPECTRAL_FLOW_FRONTIER_V0_1.md\`

## 1. Candidate shortcut

Suzuki supplies, for every localization length \(a>0\), a self-adjoint lower-bounded localized Weil operator

\[
A_a.
\]

A natural attempt to realize the prime-scale CAR contraction is to define, for \(t>0\),

\[
\Gamma_{a,t}
=
e^{-tA_a}.
\]

Since the intended arithmetic scale is \(q=e^t\), this superficially resembles the normalized prime-scale channel.

The following audit shows that this does not create a new incoming edge.

## 2. Exact norm of the heat semigroup

For a self-adjoint lower-bounded operator \(A\), spectral functional calculus gives

\[
\sigma(e^{-tA})
=
e^{-t\sigma(A)}.
\]

Let

\[
\lambda_0
=
\inf\sigma(A).
\]

Then

\[
\boxed{
\|e^{-tA}\|
=
e^{-t\lambda_0}.
}
\]

Therefore, for every fixed \(t>0\),

\[
\boxed{
\|e^{-tA}\|\le1
\iff
\lambda_0\ge0
\iff
A\ge0.
}
\]

Thus the heat-semigroup contraction condition is exactly positivity of the original self-adjoint operator.

## 3. Consequence for Suzuki \(A_a\)

For the localized Weil operator,

\[
\lambda_a
=
\inf\sigma(A_a).
\]

Hence

\[
\boxed{
e^{-tA_a}\text{ is a contraction}
\iff
\lambda_a\ge0.
}
\]

The repository already tracks

\[
\lambda_a\ge0
\]

for every \(a>0\) as the global Weil-positivity/RH-hard frontier.

Therefore

\[
\boxed{
\text{Suzuki heat-semigroup contraction}
}
\]

is not an independent proof mechanism.

It is the existing C005 positivity gate written through exponential functional calculus.

## 4. Pure-projector no-go

Could one instead demand that

\[
e^{-tA}
\]

be a pure CAR one-particle projector?

Projection requires

\[
(e^{-tA})^2=e^{-tA}.
\]

On every finite spectral value \(\lambda\),

\[
e^{-2t\lambda}
=
e^{-t\lambda}.
\]

Since

\[
e^{-t\lambda}>0,
\]

we must have

\[
e^{-t\lambda}=1,
\]

hence

\[
\lambda=0.
\]

Therefore if a self-adjoint operator has only finite spectral values in the usual sense,

\[
\boxed{
e^{-tA}\text{ projection}
\Longrightarrow
A=0.
}
\]

So the Suzuki heat semigroup cannot provide the nontrivial consecutive-mode Slater projector required by the forced sine-kernel theorem.

A spectral projection such as

\[
\mathbf1_I(A_a)
\]

is of course idempotent, but its idempotence is automatic functional calculus and does not identify its occupation spectrum with

\[
q^{2\Re\rho-1}.
\]

That identification would remain a separate theorem.

## 5. Spectrum mismatch

The MD002 criterion uses the normalized zero-channel occupation

\[
\lambda_q(\rho)
=
q^{2\Re\rho-1}.
\]

For a heat semigroup,

\[
\lambda=e^{-t\mu}
\]

where \(\mu\) is an eigenvalue or spectral parameter of \(A_a\).

To identify the two one would need

\[
\boxed{
\mu_\rho
=
1-2\Re\rho.
}
\]

No such spectral identification is currently supplied by Suzuki's localized Weil operator theorem or by the repository crosswalk.

Thus the missing statement is not merely self-adjointness.

It is a new spectral-label correspondence.

## 6. Relation to the two existing SOH operator routes

### C005 / Weil positivity route

\[
A_a\ge0\ \forall a
\Longrightarrow
\text{RH}
\]

through the standard Weil criterion.

Replacing \(A_a\ge0\) by

\[
e^{-tA_a}\le I
\]

does not weaken or solve this gate.

### Suzuki real-zero characteristic-function route

Finite-\(a\) characteristic functions have real zeros by self-adjointness, while the hard edge is the large-\(a\) normalized compact-limit identification with the xi-derived target.

This is likewise distinct from constructing a CAR occupation operator with eigenvalues \(q^{2\beta-1}\).

## 7. Refined MD002C target

The zeta-to-CAR construction must therefore be something more specific than a heat semigroup of the existing localized Weil operator.

A valid candidate must establish an incoming spectral correspondence of the form

\[
\boxed{
\rho
\longmapsto
\lambda_q(\rho)=q^{2\Re\rho-1}
}
\]

as the occupation spectrum of a canonically constructed positive operator.

Equivalent generator form:

\[
\boxed{
\rho
\longmapsto
\mu(\rho)=1-2\Re\rho
}
\]

with

\[
\Gamma_q=e^{-(\log q)\mu}.
\]

The spectral labels and the operator must be obtained from arithmetic/theta/Weil data, not from a zero list.

## 8. Compact no-go theorem

### Theorem — Suzuki heat semigroup does not independently close MD002C

For every localized self-adjoint Suzuki operator \(A_a\) and \(t>0\),

\[
\boxed{
\|e^{-tA_a}\|\le1
\iff
A_a\ge0.
}
\]

Thus proving the heat semigroup is contractive is exactly the already-open localized Weil positivity problem.

Moreover,

\[
\boxed{
e^{-tA_a}\text{ is a projection}
\Longrightarrow
A_a=0,
}
\]

so it cannot be the nontrivial filled-CAR projector.

Therefore MD002C requires a new spectral correspondence, not exponential repackaging of \(A_a\). Q.E.D.
