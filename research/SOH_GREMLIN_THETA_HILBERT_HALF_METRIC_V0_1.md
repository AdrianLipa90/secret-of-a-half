# SOH GREMLIN Theta-Hilbert Half Metric v0.1

Status: `EXACT THETA-METRIC LEMMA / CANDIDATE_INTEGRATION / NON_CANONICAL`

Source state:

- SOH base main: `a759a64c498d5ab6b31fb8566969dcf0716feb59`
- GREMLIN main: `f775cd5f0b2619692e6d2250e2c6204776b6ce24`
- OCTOPUS router: `GREMLIN_MCP_OCTOPUS_ROUTER_V0_5`
- authority: `production_runtime_write=false`, `execution_admitted=false`, `canon_allowed=false`

Focused OCTOPUS route:

```text
route_mask = [MOLE, HOUND, OWL]
route_commitment = ecdd90aaed73f8f21fcd379cf021666c832a1634d9b3cd33ffed3cf6adabb01c
scores:
  MOLE   16
  HOUND  12
  OWL    10
  SPIDER  5
  ANT     2
threshold = 7.2
```

The purpose of this note is to derive a canonical positive metric directly from the already-used theta-Mellin weight and to determine exactly what its `1/2` locus means.

## 1. Canonical theta channel vectors

Use

\[
z=s-\frac12=\delta+it,
\qquad \delta=\Re(s)-\frac12,
\]

and the positive theta-Mellin weight

\[
W(u)=\psi(e^u)e^{u/4}>0,
\qquad u>0.
\]

The canonical theta representation uses the complementary factors

\[
e^{+zu/2},\qquad e^{-zu/2}.
\]

Define two vectors in the positive Hilbert space `L^2((0,∞),du)`:

\[
\boxed{
\Psi_+(u;s)=\sqrt{W(u)}e^{+zu/2},
\qquad
\Psi_-(u;s)=\sqrt{W(u)}e^{-zu/2}.
}
\]

The theta weight decays sufficiently rapidly for all exponential moments used in the open critical strip, so these vectors have finite norms there.

## 2. Exact norm law

Define the positive moment-generating function

\[
\boxed{
M(a)=\int_0^\infty W(u)e^{au}\,du.
}
\]

Then the phases cancel in the Hilbert norms:

\[
\boxed{
\|\Psi_+(s)\|^2=M(\delta),
\qquad
\|\Psi_-(s)\|^2=M(-\delta).
}
\]

Hence the theta metric sees the horizontal displacement from the half-axis directly and is independent of the ordinate `t`.

## 3. Exact orbit-separating defect

Define

\[
\boxed{
\Delta_\Theta(s)
:=\|\Psi_+(s)\|^2-\|\Psi_-(s)\|^2
=M(\delta)-M(-\delta).
}
\]

Equivalently,

\[
\boxed{
\Delta_\Theta(s)
=2\int_0^\infty W(u)\sinh(\delta u)\,du.
}
\]

Because `W(u)>0` and `u>0`, the integrand has the sign of `delta`. Therefore

\[
\boxed{
\operatorname{sgn}\Delta_\Theta(s)=\operatorname{sgn}\delta
}
\]

and, in particular,

\[
\boxed{
\Delta_\Theta(s)=0
\iff
\delta=0
\iff
\Re(s)=\frac12.
}
\]

This is an exact theta-kernel half-axis detector. No zeta-zero input is used.

Under the critical reflection `s -> 1-conj(s)`, `delta -> -delta`, so

\[
\boxed{\Delta_\Theta\mapsto-\Delta_\Theta.}
\]

Thus `Delta_Theta` is an orbit-separating defect rather than an orbit average.

## 4. Canonical normalized theta coordinate

Define

\[
\boxed{
q_\Theta(\delta)
:=
\frac{M(\delta)}{M(\delta)+M(-\delta)}.
}
\]

Immediately,

\[
q_\Theta(-\delta)=1-q_\Theta(\delta),
\qquad
q_\Theta(0)=\frac12.
\]

To prove strict monotonicity, set

\[
\ell(\delta)=\log M(\delta)-\log M(-\delta).
\]

Since

\[
M'(a)=\int_0^\infty uW(u)e^{au}\,du>0,
\]

we have

\[
\boxed{
\ell'(\delta)
=\frac{M'(\delta)}{M(\delta)}
+\frac{M'(-\delta)}{M(-\delta)}>0.
}
\]

Moreover

\[
q_\Theta=\frac{1}{1+e^{-\ell}},
\]

so

\[
\boxed{q_\Theta'(\delta)>0.}
\]

Therefore

\[
\boxed{
q_\Theta(\delta)=\frac12
\iff
\delta=0
\iff
\Re(s)=\frac12.
}
\]

This gives a canonical theta-derived compact balance coordinate. It need not equal the affine coordinate `Re(s)` numerically; it is a strictly monotone, reflection-covariant reparametrization of the same half-axis defect.

## 5. Exact crosswalk to the projective half geometry

For

\[
\Omega(s)=\frac{s}{1-s},
\qquad
B(s)=\log|\Omega(s)|,
\]

observe

\[
|s|^2-|1-s|^2=2\Re(s)-1=2\delta.
\]

Hence

\[
\boxed{
\operatorname{sgn}B(s)=\operatorname{sgn}\delta
=\operatorname{sgn}\Delta_\Theta(s)
}
\]

throughout the open strip, and

\[
\boxed{
B=0
\iff
\Delta_\Theta=0
\iff
q_\Theta=\frac12
\iff
|\Omega|=1
\iff
\Re(s)=\frac12.
}
\]

Thus the projective self-dual layer and the theta-Hilbert equal-norm layer are exactly the same locus. This closes the geometric/metric crosswalk without using RH.

## 6. HOUND firewall: scalar detector half versus Hilbert metric half

The analytic detector channels

\[
A_+(s),\qquad A_-(s)
\]

satisfy at every non-degenerate xi zero

\[
A_+(\rho)=-A_-(\rho),
\]

so their ordinary scalar magnitudes are equal and their normalized scalar-channel masses are automatically `1/2`.

That equality is not the same statement as

\[
\|\Psi_+(\rho)\|=\|\Psi_-(\rho)\|.
\]

The first concerns two scalar projections/readout channels. The second is the theta-Hilbert norm balance and, by the theorem above, is exactly equivalent to `Re(rho)=1/2`.

Therefore the remaining proof-bearing implication has been compressed to

\[
\boxed{
\xi(\rho)=0
\Longrightarrow
\Delta_\Theta(\rho)=0.
}
\]

Equivalently,

\[
\boxed{
\xi(\rho)=0
\Longrightarrow
q_\Theta(\rho)=\frac12.
}
\]

This implication is RH-equivalent. It is not proved here.

## 7. Projection-residual formulation of the remaining obstruction

Let

\[
e_0(u)=\frac{\sqrt{W(u)}}{\sqrt{M(0)}}.
\]

The Mellin channel integrals are scalar projections of `Psi_±` onto `e_0`:

\[
\int_0^\infty W(u)e^{\pm zu/2}du
=\sqrt{M(0)}\,\langle e_0,\Psi_\pm(s)\rangle.
\]

Decompose

\[
\Psi_\pm=c_\pm e_0+r_\pm,
\qquad
r_\pm\perp e_0.
\]

Then

\[
\|\Psi_\pm\|^2=|c_\pm|^2+\|r_\pm\|^2.
\]

The xi-zero condition constrains the affine scalar readouts built from `c_+` and `c_-`; it does not presently constrain the residual energies `||r_±||^2` strongly enough to force equal total norms.

This identifies the exact missing structure as a projection-to-norm rigidity theorem on the canonical exponential theta manifold.

## 8. Sharpened search targets

GREMLIN therefore replaces the earlier vague `find a metric` task with three narrower candidates:

1. **Projection-to-norm rigidity:** prove that detector cancellation on the canonical theta exponential manifold forces `Delta_Theta=0`.
2. **Residual-energy coercivity:** derive a positive identity or inequality controlling the difference `||r_+||^2-||r_-||^2` by the scalar detector residual.
3. **Weil/Jensen coupling:** construct a non-circular positive quadratic form whose value on the theta pair is proportional to, or coercive in, `Delta_Theta^2`.

Any successful theorem must be derived independently of RH-equivalent premises.

## 9. Authority

```text
metric_crosswalk = EXACT
zero_to_metric_balance = OPEN_RH_EQUIVALENT
promotion_state = CANDIDATE_INTEGRATION
canon_allowed = false
proof_of_RH = false
```
