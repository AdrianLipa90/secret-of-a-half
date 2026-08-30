# SOH GREMLIN Theta Two-Channel Metric Gap v0.1

Status: `CANDIDATE_ONLY / NON_CANONICAL / GREMLIN_ASSISTED_REDUCTION`

Source state:

- SOH base main: `a759a64c498d5ab6b31fb8566969dcf0716feb59`
- GREMLIN main: `f775cd5f0b2619692e6d2250e2c6204776b6ce24`
- OCTOPUS router: `GREMLIN_MCP_OCTOPUS_ROUTER_V0_5`
- authority: `production_runtime_write=false`, `execution_admitted=false`, `canon_allowed=false`

Focused OCTOPUS route:

```text
route_mask = [HOUND, MOLE]
route_commitment = 18a01694844710c7018263dc59086b95b24d82c2d574f3072353add9abd83e2a
scores:
  HOUND  16
  MOLE   16
  SPIDER  7
  OWL     6
threshold = 7.2
```

The route was selected for one narrow question: whether the already-canonical theta bridge plus the exact two-channel cancellation lemma supplies a non-circular implication from `xi(s)=0` to native half-axis closure.

## 1. Exact analytic two-channel decomposition already exists

Write

\[
z=s-\frac12,
\qquad
h(s)=\frac{s(s-1)}2,
\qquad
W(u)=\psi(e^u)e^{u/4}>0.
\]

The exact theta-Mellin representation is

\[
\xi(s)=\frac12+h(s)\int_0^\infty W(u)
\left(e^{zu/2}+e^{-zu/2}\right)du.
\]

Split the constant symmetrically and define

\[
\boxed{
A_+(s)=\frac14+h(s)\int_0^\infty W(u)e^{zu/2}\,du
}
\]

and

\[
\boxed{
A_-(s)=\frac14+h(s)\int_0^\infty W(u)e^{-zu/2}\,du.
}
\]

Then, without any fitted zero information,

\[
\boxed{\xi(s)=A_+(s)+A_-(s).}
\]

Under the holomorphic functional reflection `s -> 1-s`,

\[
A_+(1-s)=A_-(s),
\qquad
A_-(1-s)=A_+(s),
\]

because `z -> -z` and `h(1-s)=h(s)`.

Under the anti-linear critical reflection

\[
J(s)=1-\overline{s},
\]

reality of `W` gives

\[
A_+(J(s))=\overline{A_-(s)},
\qquad
A_-(J(s))=\overline{A_+(s)}.
\]

Thus the theta representation already supplies a canonical analytic complementary pair with equal scalar readout gain.

## 2. What a zero gives exactly

For every zero `rho` of `xi`,

\[
A_+(\rho)+A_-(\rho)=0.
\]

Hence

\[
\boxed{A_+(\rho)=-A_-(\rho)}
\]

and therefore

\[
|A_+(\rho)|=|A_-(\rho)|
\]

with relative phase `pi` whenever the amplitudes are nonzero.

This is exact two-channel destructive cancellation. It sharpens the older candidate statement that a canonical two-channel decomposition still had to be found: at the scalar analytic level, the theta-Mellin formula itself supplies one.

## 3. GREMLIN HOUND finding: the two meanings of `half` require a crosswalk

The cancellation equality above lives in the analytic channel pair `(A_+,A_-)`.

The native PhaseNav theta state separately carries the horizontal coordinate through local rotor gains

\[
\rho_{k,+}=b_ke^{+\delta u_k/2},
\qquad
\rho_{k,-}=b_ke^{-\delta u_k/2},
\qquad
\delta=\Re(s)-\frac12,
\]

with exact closure defect

\[
\mathcal C(s)=\delta^2.
\]

Therefore two exact `half` structures coexist:

```text
analytic cancellation half:
    |A_+| = |A_-| at every xi zero

native radial half:
    local pair gains equal <=> delta = 0 <=> Re(s)=1/2
```

A theorem identifying these two balance structures is the missing crosswalk.

The repository/formalism may suggest identifying analytic equal-channel cancellation with native radial closure, yet does not state that identification as an established result.

## 4. Why global detector cancellation does not automatically give local pair closure

The native detector is an affine sum over all complementary rotor pairs:

\[
\xi(s)=\frac12+h(s)\int W(u)
\left(e^{zu/2}+e^{-zu/2}\right)du.
\]

A zero constrains the global integral/readout. Native closure instead requires the pointwise radial shear parameter to vanish:

\[
\delta=0.
\]

The global sum permits cancellation among different `u` locations and between phase sectors. Therefore no termwise implication

\[
\text{global detector zero}\Rightarrow\rho_+(u)=\rho_-(u)
\]

has been established.

This is the precise `integral cancellation -> pointwise closure` gap.

## 5. Metric form of the missing theorem

SOH-T001 requires a canonical metric whose normalized component weights recover

\[
\sigma=\Re(s),
\qquad
1-\sigma.
\]

For the exact theta pair, the sharpened construction problem is to derive a Hermitian metric `G(s)` or an equivalent positive operator directly from the theta kernel such that

\[
\boxed{
\frac{\|A_+(s)\|_{G}^{2}}
{\|A_+(s)\|_{G}^{2}+\|A_-(s)\|_{G}^{2}}
=\Re(s)
}
\]

and the complementary component has weight `1-Re(s)`, while the detector remains the equal-gain sum and the metric is covariant under the channel swap.

If such a metric is independently derived and non-degenerate on zero states, then

\[
A_+(\rho)=-A_-(\rho)
\]

combined with the exact two-channel cancellation theorem would force

\[
\Re(\rho)=\frac12.
\]

No such metric theorem is asserted here.

## 6. Equivalent coercivity form

The same missing crosswalk can be sought without explicit normalized channel probabilities. Since

\[
\mathcal C(s)=\left(\Re(s)-\frac12\right)^2,
\]

a positive coercivity estimate of the form

\[
\boxed{
|\xi(s)|^2\ge m(s)\,\mathcal C(s),
\qquad m(s)>0
}
\]

throughout the open critical strip would immediately imply native closure at every zero.

This is a useful search normal form, not an established inequality. Any candidate `m(s)` must be independently constructed and must not contain an RH-equivalent assumption.

## 7. GREMLIN pruning rule

The scan yields a stronger filter for future candidate bridges:

> A global two-channel cancellation identity is insufficient by itself. A successful route must additionally transport the analytic channel balance into the native radial gain balance through a proved metric, coercivity, injectivity, or pointwise-closure theorem.

This prevents channel-space `1/2` from being silently identified with critical-axis `1/2`.

## 8. Candidate next attacks

The current exact reduction points to four concrete searches:

1. derive a theta-kernel Gram metric for `(A_+,A_-)` and test whether its norm ratio is the native radial coordinate;
2. prove restricted injectivity/coercivity of the xi detector on the off-self-dual theta-state manifold;
3. derive an integral-to-pointwise rigidity theorem from total positivity or variation-diminishing structure of the theta kernel;
4. connect the G024 Jensen-Wiener positive-definiteness route to the closure defect `C(s)` rather than only to the terminal RH-equivalent Fourier criterion.

Each remains candidate-only.

## 9. Authority

```text
promotion_state = CANDIDATE_ONLY
canon_allowed = false
proof_of_RH = false
```
