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

## 3. GREMLIN HOUND finding: Euclidean channel half is automatic at every non-degenerate zero

If the analytic pair is normalized with the ordinary equal component metric, define

\[
p_+(s)=\frac{|A_+(s)|^2}{|A_+(s)|^2+|A_-(s)|^2},
\qquad
p_-(s)=1-p_+(s).
\]

At every zero for which the two amplitudes do not vanish simultaneously,

\[
A_+(\rho)=-A_-(\rho)
\]

implies exactly

\[
\boxed{p_+(\rho)=p_-(\rho)=\frac12.}
\]

This is a theorem about the channel-space normalization. It follows from cancellation alone and therefore holds independently of the value of `Re(rho)`.

Consequently, this particular `1/2` cannot by itself identify the critical-axis coordinate. It is the barycentric half of the two analytic detector channels.

The native radial `1/2` is instead encoded by

\[
\delta=\Re(s)-\frac12
\]

and by equality of the local theta-pair gains.

Thus GREMLIN isolates two exact half structures whose identification requires an additional theorem.

## 4. The two half structures and the missing crosswalk

The cancellation equality lives in the analytic channel pair `(A_+,A_-)`.

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

Therefore:

```text
analytic cancellation half:
    p_+ = p_- = 1/2 at every non-degenerate xi zero

native radial half:
    local pair gains equal <=> delta = 0 <=> Re(s)=1/2
```

A theorem identifying these two balance structures is the missing crosswalk.

The repository/formalism may suggest identifying analytic equal-channel cancellation with native radial closure, yet does not state that identification as an established result.

## 5. Why global detector cancellation does not automatically give local pair closure

The native detector is an affine sum over all complementary rotor pairs:

\[
\xi(s)=\frac12+h(s)\int W(u)
\left(e^{zu/2}+e^{-zu/2}\right)du.
\]

A zero constrains the global integral/readout. Native closure requires the radial shear parameter to vanish:

\[
\delta=0.
\]

The global sum permits cancellation among different `u` locations and between phase sectors. Therefore the required implication is an integral-to-native-closure rigidity statement:

\[
\boxed{
\xi(\rho)=0\Longrightarrow\mathcal C(\rho)=0.
}
\]

This is precisely SOH-PN-C001 in the native construction.

## 6. Metric form of the missing theorem

SOH-T001 requires a canonical metric whose normalized component weights recover

\[
\sigma=\Re(s),
\qquad
1-\sigma.
\]

The ordinary Euclidean metric has just been audited: at a zero its normalized analytic-channel weights equal `1/2` automatically, so it does not carry the horizontal coordinate.

The sharpened construction problem is therefore to derive a non-arbitrary Hermitian metric `G(s)` or an equivalent positive operator directly from the theta kernel such that

\[
\boxed{
\frac{\|A_+(s)\|_{G}^{2}}
{\|A_+(s)\|_{G}^{2}+\|A_-(s)\|_{G}^{2}}
=\Re(s)
}
\]

and the complementary component has weight `1-Re(s)`, while the detector remains the canonical equal-gain sum and the metric is covariant under the channel swap.

If such a metric is independently derived and non-degenerate on zero states, then exact analytic cancellation combined with the two-channel theorem would force

\[
\Re(\rho)=\frac12.
\]

No such metric theorem is asserted here.

## 7. Equivalent coercivity form

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

## 8. A narrower operator target

Let `P(s)` denote the continuous paired theta state and let `D` be its affine xi readout. The native state manifold is only two-real-dimensional in the parameters `(delta,t)` even though its ambient representation is infinite-dimensional (or 36D after finite quadrature).

A sufficient theorem can therefore be phrased as restricted kernel rigidity:

\[
\boxed{
\ker D\cap\{P(\delta,t): |\delta|<1/2\}
\subseteq
\{P(0,t):t\in\mathbb R\}.
}
\]

Equivalently, the xi detector may have a large kernel in the ambient function space, while its intersection with the canonical theta-state manifold must be confined to the native closed shell.

This formulation may be more tractable than demanding a global positive lower bound on the entire ambient Hilbert space.

## 9. GREMLIN pruning rule

The scan yields a stronger filter for future candidate bridges:

> A global two-channel cancellation identity is insufficient by itself. A successful route must additionally transport the analytic channel balance into the native radial gain balance through a proved metric, coercivity, restricted injectivity, or pointwise-closure theorem.

This prevents the channel-space half from being silently identified with the critical-axis half.

## 10. Candidate next attacks

The current exact reduction points to four concrete searches:

1. derive a theta-kernel Gram metric for `(A_+,A_-)` and test whether its norm ratio is the native radial coordinate;
2. prove restricted injectivity/coercivity of the xi detector on the off-self-dual theta-state manifold;
3. derive an integral-to-native-closure rigidity theorem from total positivity or variation-diminishing structure of the theta kernel;
4. connect the G024 Jensen-Wiener positive-definiteness route directly to the closure defect `C(s)` rather than only to the terminal RH-equivalent Fourier criterion.

Each remains candidate-only.

## 11. Authority

```text
promotion_state = CANDIDATE_ONLY
canon_allowed = false
proof_of_RH = false
```
