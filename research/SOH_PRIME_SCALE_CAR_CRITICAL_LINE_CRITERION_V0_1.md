# SOH Prime-Scale CAR Critical-Line Criterion v0.1

Status: **EXACT_CONDITIONAL_CRITERION / ZETA_TO_CAR_BINDING_OPEN**

Date: 2026-09-26

Parents:
- \`research/SOH_MONTGOMERY_DYSON_HARDY_CAR_BINDING_V0_1.md\`
- \`research/SOH_MONTGOMERY_FORM_FACTOR_PRIME_SCALE_CROSSWALK_V0_1.md\`
- existing \`SecretOfAHalfFormal/RiemannSeam.lean\` unit-circle/critical-line seam.

## 1. Normalized prime-scale channel

Let

\[
s=\sigma+it
\]

and fix a real scale

\[
q>1.
\]

Define the normalized prime-scale channel

\[
\boxed{
Z_q(s)
=
q^{\,s-\frac12}
=
\exp\!\left(
(s-\tfrac12)\log q
\right).
}
\]

Then

\[
Z_q(s)
=
q^{\sigma-\frac12}
e^{it\log q}
\]

and therefore

\[
\boxed{
|Z_q(s)|
=
q^{\sigma-\frac12}.
}
\]

Hence

\[
\boxed{
|Z_q(s)|=1
\iff
\sigma=\frac12.
}
\]

For any one fixed \(q>1\), unit modulus of the normalized channel is therefore exactly the critical-line condition.

This is an elementary coordinate theorem. It does not use zeta zerohood.

## 2. Zero-channel specialization

For a nontrivial zeta zero

\[
\rho=\beta+i\gamma,
\]

the normalized explicit-formula channel is

\[
\boxed{
Z_q(\rho)
=
q^{\rho-\frac12}
=
q^{\beta-\frac12}
e^{i\gamma\log q}.
}
\]

Its squared amplitude is

\[
\boxed{
\lambda_q(\rho)
=
|Z_q(\rho)|^2
=
q^{2\beta-1}.
}
\]

Thus

\[
\boxed{
\lambda_q(\rho)=1
\iff
\beta=\frac12.
}
\]

The phase

\[
e^{i\gamma\log q}
\]

and the radial defect

\[
q^{\beta-\frac12}
\]

are therefore exactly separated.

## 3. Pure-CAR / Slater projector criterion

Suppose a canonical zeta-to-CAR construction produces a one-particle density operator

\[
\Gamma_q
\]

whose spectral label associated with each nontrivial zero \(\rho\) has occupation eigenvalue

\[
\lambda_q(\rho)=q^{2\beta-1}.
\]

If the resulting CAR state is pure quasi-free / Slater, then

\[
\Gamma_q^2=\Gamma_q.
\]

Every occupation eigenvalue therefore obeys

\[
\lambda^2=\lambda.
\]

Since

\[
\lambda_q(\rho)>0,
\]

idempotence forces

\[
\lambda_q(\rho)=1.
\]

Hence

\[
q^{2\beta-1}=1.
\]

Because \(q>1\),

\[
\boxed{
\beta=\frac12.
}
\]

Therefore:

### Theorem SOH-MD002A — Slater projector criterion

If a canonical zero-list-free zeta construction realizes the normalized prime-scale weights \(q^{2\Re\rho-1}\) as the occupation spectrum of a pure CAR one-particle projector, then every nontrivial zeta zero lies on the critical line.

The algebraic implication is exact.

The construction hypothesis is open.

## 4. Weaker CAR-contraction criterion

A general gauge-invariant fermionic one-particle density operator obeys

\[
\boxed{
0\le\Gamma_q\le I.
}
\]

Thus every occupation eigenvalue must satisfy

\[
0\le\lambda\le1.
\]

If

\[
\lambda_q(\rho)=q^{2\beta-1},
\]

the contraction condition gives

\[
q^{2\beta-1}\le1.
\]

Since \(q>1\),

\[
\beta\le\frac12.
\]

Now use the standard zeta functional-equation symmetry: if

\[
\rho=\beta+i\gamma
\]

is a nontrivial zero, then the reflected point with real part

\[
1-\beta
\]

is also a nontrivial zero.

Applying the same contraction condition to the reflected zero gives

\[
1-\beta\le\frac12,
\]

so

\[
\beta\ge\frac12.
\]

Therefore

\[
\boxed{
\beta=\frac12.
}
\]

### Theorem SOH-MD002B — CAR contraction + reflection criterion

If a canonical zeta-to-CAR construction realizes every normalized prime-scale weight

\[
q^{2\Re\rho-1}
\]

as an occupation eigenvalue of a positive contraction

\[
0\le\Gamma_q\le I,
\]

for the full reflection-symmetric nontrivial zero set, then RH follows.

Again the implication is exact; the zeta-to-CAR construction is the open step.

## 5. Why the contraction theorem is stronger structurally

The pure-projector criterion requires

\[
\Gamma_q^2=\Gamma_q.
\]

The contraction criterion needs only

\[
0\le\Gamma_q\le I
\]

plus the already-standard reflected-zero symmetry.

Thus the RH-forcing property does not require the full sine-kernel determinantal process.

It is enough that the normalized zeta radial weights become legitimate fermionic occupation numbers for the complete reflected zero set.

This separates two logical tasks:

\[
\boxed{
\text{CAR admissibility}
\Longrightarrow
\text{critical line}
}
\]

and

\[
\boxed{
\text{pure consecutive-mode CAR projector}
\Longrightarrow
\text{critical line + sine-kernel/ramp}.
}
\]

The second contains the first plus the local spectral-statistics structure.

## 6. Off-axis quartet obstruction

Suppose

\[
\beta\ne\frac12.
\]

The zeta symmetries generate a reflected zero with real part

\[
1-\beta.
\]

If \(\beta<1/2\), then \(1-\beta>1/2\), and

\[
\lambda_q(1-\rho)
=
q^{1-2\beta}
>
1.
\]

If \(\beta>1/2\), the original zero already has

\[
\lambda_q(\rho)>1.
\]

Therefore every off-axis reflection orbit contains at least one normalized channel whose squared amplitude exceeds one.

Hence:

\[
\boxed{
\text{off-axis zero orbit}
\Longrightarrow
\text{violation of CAR occupation bound}
}
\]

provided the normalized channel is genuinely identified with the one-particle occupation spectrum.

This is a sharp falsification criterion for any proposed zeta-to-CAR map.

## 7. Relation to the existing SOH unit-circle seam

SOH already contains the exact projective criterion

\[
|\Omega(s)|=1
\iff
\Re s=\frac12,
\qquad
\Omega(s)=\frac{s}{1-s}.
\]

The present criterion is different but compatible:

\[
\boxed{
|q^{s-1/2}|=1
\iff
\Re s=\frac12.
}
\]

The first is a reciprocal projective coordinate.

The second is the radial amplitude of a normalized prime-scale / explicit-formula channel.

Their shared unit circle is not assumed to prove zerohood. It shows that two independently defined coordinates have the same critical-axis locus.

## 8. Exact link to phase spectroscopy

On the critical line,

\[
Z_q(\rho)
=
e^{i\gamma\log q}.
\]

Thus the channel becomes a pure phase, exactly the phase bank used by the Montgomery–Dyson spectroscopy programme.

Off the critical line,

\[
Z_q(\rho)
=
q^{\beta-1/2}e^{i\gamma\log q},
\]

so the same phase carries a non-unit radial amplitude.

Therefore the phase-spectroscopy representation has a precise two-layer structure:

\[
\boxed{
\text{radial amplitude}
=
q^{\beta-1/2},
\qquad
\text{angular phase}
=
\gamma\log q.
}
\]

A unitary pure-phase representation for all normalized zero channels is equivalent to critical-line placement.

## 9. Exact missing binding

The theorem does **not** establish that a CAR density operator with these eigenvalues exists canonically.

The remaining construction gate is:

### SOH-MD002C — zero-list-free zeta-to-CAR density construction

Construct from the zeta/theta/Weil/explicit-formula object, without consuming a zero list and without assuming RH, a canonical positive operator

\[
\Gamma_q
\]

such that:

1. its relevant spectral labels are the nontrivial zeta spectral channels;
2. the associated radial occupation weights are derived as
   \[
   q^{2\Re\rho-1};
   \]
3. positivity/contraction
   \[
   0\le\Gamma_q\le I
   \]
   is proved independently from arithmetic/operator structure;
4. the construction does not define \(\Gamma_q\) by first assuming the zeros lie on the critical line.

If this gate is closed, Theorem SOH-MD002B gives RH immediately.

If in addition

\[
\Gamma_q^2=\Gamma_q
\]

and the local occupied modes are the already-declared consecutive Hardy/Yoshida Fourier sector, the forced sine-kernel/ramp theorem follows in the same representation.

## 10. Circularity firewall

The following constructions are invalid as RH proofs:

- define
  \[
  \Gamma_q
  \]
  only after replacing every \(\rho\) by \(1/2+i\gamma\);
- normalize every occupation by hand to one;
- use a verified zero table as the definition of the operator;
- assume RH to prove
  \[
  \Gamma_q\le I
  \]
  and then infer RH;
- choose the CAR state because it reproduces GUE statistics.

The operator must come first.

## 11. Compact criterion chain

The current chain is

\[
\boxed{
q^{\rho-1/2}
=
q^{\beta-1/2}e^{i\gamma\log q}
}
\]

\[
\boxed{
\text{canonical CAR contraction}
\Longrightarrow
q^{2\beta-1}\le1
}
\]

plus reflection

\[
\boxed{
\beta\leftrightarrow1-\beta
}
\]

which yields

\[
\boxed{
\beta=\frac12.
}
\]

For a pure projector one has the stronger immediate condition

\[
\boxed{
q^{2\beta-1}\in\{0,1\}
\quad\&\quad
q^{2\beta-1}>0
\Longrightarrow
\beta=\frac12.
}
\]

The critical-line implication is exact.

The zeta-to-CAR operator construction remains the sole nontrivial binding in this criterion.
