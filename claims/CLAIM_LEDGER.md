# Claim Ledger — Version 0.9 Integrated Canon V2

The machine-readable source of truth is [`claim_ledger.json`](claim_ledger.json). The previous 0.6.1-review ledger is preserved unchanged at [`archive/claim_ledger_v0.6.1_review.json`](archive/claim_ledger_v0.6.1_review.json).

## Canonical V2 line

`SOH-L001`–`SOH-L011` retain their established meanings. `SOH-L012`–`SOH-L032` are now exclusively the promoted V2 critical-axis / Li / Weil line:

| Range | Canonical content | Status |
|---|---|---|
| L012–L016 | Projective coordinate `Omega=s/(1-s)`, anti-linear reciprocal conjugacy, unit-circle critical axis, `B=log|Omega|`, `V=B^2` | Exact / exact reformulation |
| L017–L023 | Li coordinate `z_L=1-1/s=-1/Omega`, reciprocal-conjugate quartet formula, local growth radius and off-circle negative subsequence | Exact |
| L024–L026 | Li generating singularity, global Li criterion, global Weil positivity criterion | Exact classical criteria / reformulations |
| L027–L030 | Log-radial prime shifts and the positive-weight hinge no-go lemma | Exact reductions / no-go |
| L031–L032 | Localized arithmetic Weil spectral floor and nested-domain monotonicity | Exact reduction / domain monotonicity |

## Legacy-ID migration

Several development snapshots used numbers L012–L022 for earlier arithmetic results. Those statements remain canonical under domain IDs; the old numeric names are deprecated aliases only.

| Historical pre-v0.9 ID | Current canonical ID | Content |
|---|---|---|
| L012 | SOH-WA001 | Gaussian Weil arithmetic Fourier transform |
| L013 | SOH-HM001 | Hermite finite-span density |
| L014 | SOH-HM002 | Hermite kernel Fourier transform |
| L015 | SOH-ZU001 | complement / reciprocal-odds conjugacy |
| L016 | SOH-ZU002 | unique positive reciprocal fixed point |
| L017 | SOH-ZU003 | Fisher–Rao midpoint |
| L018 | SOH-PT001 | reciprocal prime-tail compactification |
| L019 | SOH-PT002 | incomplete-gamma prime-tail majorant |
| L020 | SOH-PT003 | finite-section norm / Weyl enclosure |
| L021 | SOH-AC001 | adaptive cutoff collapse |
| L022 | SOH-DHSE-M001 | finite Stage-M classification |

Historical prose in development chapters that displays one of these old numeric IDs is governed by this migration table. It does **not** redefine the current V2 `SOH-L012`–`SOH-L032` identifiers.

## Open firewall

`SOH-C001`–`SOH-C005` remain open according to their stated scope. In particular:

- **SOH-C005 remains OPEN:** independently prove the full admissible arithmetic Weil form non-negative, equivalently establish the corresponding global Li positivity, without assuming an RH-equivalent premise.
- **RH remains OPEN.**

Finite PSD receipts, exact coordinate equivalences, local quartet theorems, prime-tail certificates, and localized operator reductions do not by themselves close SOH-C005.

## Promotion rule

A claim may be promoted only when its proof or reproducible construction is complete at the declared scope, all dependencies are explicit, and no dependency merely assumes an equivalent form of the desired conclusion. Numerical agreement does not promote a claim to exact status. Model assignments remain model-level unless independently validated.


## Occam relational zero triad — 2026-09-24

The relational-zero line is deliberately separate from the canonical G-series and does not renumber SOH-G001--SOH-G023.

- **SOH-RZ001 — EXACT WITHIN DECLARED RELATIONAL MODEL.** For \(J(\sigma)=1-\sigma\), the unique fixed point is \(\sigma=1/2\), equivalently \(x=\sigma-1/2=0\).
- **SOH-RZ002 — EXACT WITHIN DECLARED RELATIONAL MODEL.** \(\ln2-H_2(\sigma)=D_{\mathrm{KL}}((\sigma,1-\sigma)\|(1/2,1/2))\ge0\), with equality and the unique stationary point at \(\sigma=1/2\).
- **SOH-RZ003 — EXACT WITHIN DECLARED RELATIONAL MODEL.** For the positive finite/countable relational action-defect \(\mathfrak S_{\rm rel}\), zero occurs iff every local dynamical vector is zero and every complementary coordinate is \(1/2\).
- **SOH-RZ004 — CONDITIONAL RH COROLLARY.** If every non-trivial \(\xi\)-zero is independently bound to a global RZ zero-mode, then \(\Re\rho=1/2\).

The triad closes the project's internal relational-zero theorem. It does not by itself discharge SOH-C001, SOH-C004, SOH-C005, SOH-G003, or any RH-equivalent incoming bridge.

## Zero critical relational axis / Occam proof channel — 2026-09-24

- **SOH-RZ005 — EXACT FORMAL CROSSWALK.** For `s != 0,1`, the reciprocal-conjugation defect satisfies
  \[
  \Delta_{\rm RC}(\Omega(s))
  =
  \frac{4(\Re s-1/2)^2}{|s|^2|1-s|^2},
  \]
  so its zero locus is exactly the critical line.
- **SOH-RZ006 — EXACT FORMAL CONDITIONAL RH THEOREM.** If a canonical scalar energy `E` vanishes on every non-trivial zeta zero and, for some `c>0`, obeys `c Delta_RC <= E` on those zeros, then RH follows. This is formalized in Lean as `riemannHypothesis_of_coercive_zero_energy`.
- **SOH-RZ007 — EXACT RH-EQUIVALENCE FIREWALL.** The condition that the half-axis defect (equivalently the reciprocal-conjugation defect) vanishes on every non-trivial zeta zero is equivalent to RH. Therefore that zero-defect condition is not an independent proof premise unless derived from a non-RH-equivalent theorem.

The resulting shortest graph is

\[
\xi(\rho)=0
\Longrightarrow
E(\rho)=0
\stackrel{E\ge c\Delta}{\Longrightarrow}
\Delta(\rho)=0
\Longrightarrow
\Re\rho=\frac12.
\]

Within the enlarged Occam axiom system that includes the canonical zero-energy coercivity axiom, RH is a theorem and the axiomatic channel is closed. The repository still keeps `proof_of_rh=false` because the canonical zero-energy coercivity edge has not been independently derived from non-RH-equivalent analytic structure.

## Derived relational-energy coercivity — 2026-09-24

- **SOH-RZ008 — EXACT RELATIONAL-MODEL COERCIVITY.** For (0<Re s<1), (s\neq0,1),
  \[
  D_H(\Re s)
  \ge
  2(\Re s-1/2)^2
  =
  \frac{|s|^2|1-s|^2}{2}\,\Delta_{\rm RC}(\Omega(s)).
  \]
  This follows from (D_H''(\sigma)=1/[\sigma(1-\sigma)]\ge4) and the exact reciprocal-defect crosswalk. Existing non-negative TIR (U(1))/holonomy energy terms only strengthen the inequality.
- **SOH-RZ009 — AXIOMATIC OCCAM RH THEOREM.** Under the universal relational-zero realization principle `R0`,
  \[
  \xi(\rho)=0
  \Longrightarrow
  E_{\rm rel}(\rho)=0
  \Longrightarrow
  \Delta_{\rm RC}(\Omega(\rho))=0
  \Longrightarrow
  \Re\rho=1/2.
  \]
  Therefore RH is a theorem inside the declared Occam relational system.

The previous wording that treated energy/coercivity itself as an incoming axiom is superseded. The energy edge is `CLOSED / DERIVED`. The remaining foundational statement is `R0`. The external repository firewall remains: `R0` specialized to all non-trivial zeta zeros has not been independently proved in standard analysis and must not be silently counted as an unconditional RH resolution.


## Suzuki–Livšic zero-free resolvent line — 2026-09-26

- **SOH-LIV001 — EXACT.** Suzuki's finite-\(a\) characteristic quotient is Schur in the upper half-plane for every admissible shift \(\lambda<\lambda_a\), with \(\chi_{a,\lambda}(i)=0\); convergence to the declared infinite characteristic on any zero-free accumulation set implies RH by Montel/Vitali and the identity theorem.
- **SOH-LIV002 — EXACT / UNCONDITIONAL.** The explicit lower bound
  \[
  \lambda_a\ge-\log a-\log(2\pi)-\gamma-8ae^a-4a\cosh a-a/2
  \]
  yields a zero-list-free admissible shift for every \(a>0\).
- **SOH-LIV003 — EXACT NO-GO.** Any independently proved admissible shift schedule with \(\lambda(a)\to0\) already forces \(\lambda_a\ge0\) for all \(a\), hence imports the RH-hard Weil-positivity conclusion.
- **SOH-LIV004 — EXACT.** On \(s=1/2+y>1\), the Cayley target reduces to the zero-free prime-side scalar \(\xi'(s)/\xi(s)\), with explicit prime truncation error \(O_\eta(ae^{-2a\eta})\) at cutoff \(n\le e^{2a}\).
- **SOH-LIV005 — EXACT.** The piecewise-exponential Weil functional and finite cross-convolution realize the denominator combination \(r_0+\xi'(s)/\xi(s)\); the finite prime support is exactly \(n\le e^{2a}\).
- **SOH-LIV006 — EXACT.** The large-negative-shift resolvent first correction converges at fixed \(a\) to the localized Weil form on the closed form domain.
- **SOH-LIV007 — EXACT / EFFECTIVE.** Endpoint-zero operator-domain vectors admit a certified first-correction error \(M_a(f)M_a(g)/(\mu+1)\).
- **SOH-LIV008 — EXACT / EFFECTIVE.** Sharp exponential vectors admit the explicit boundary-layer form-norm bound \(O_{a,p}(\delta\log(1/\delta))\), with displayed constants.
- **SOH-LIV009 — EXACT / EFFECTIVE.** On \(1\le y\le2\), the finite denominator cross-Weil scalar has a uniform error \(E_W^\ast(a)=O(ae^{-a})\), and explicit \((a_n,\delta_n,\mu_n)\) schedules yield zero-list-free denominator convergence.
- **SOH-LIV010 — OPEN STRUCTURAL GATE.** The second deficiency/numerator channel must be transported to the target \(r(s)-r_0\) by a source-compatible finite-part, boundary-triple, or equivalent construction that preserves the finite Schur/self-adjoint geometry. Direct termwise analytic continuation is forbidden.
- **SOH-LIV-N001 — NUMERICAL FALSIFICATION DIAGNOSTIC.** Direct evaluation of the naturally normalized finite numerator Weil functional at \(y=1\) does not exhibit convergence to its formal value \(0\) over the tested \(a\)-range; large cancellations and growing oscillations appear. This diagnostic is not a theorem, but it falsifies treating naive termwise continuation as an established limit.

**Firewall:** SOH-LIV001–SOH-LIV009 do not prove RH because SOH-LIV010 remains open. The direct near-zero shift shortcut is RH-hard by SOH-LIV003.
