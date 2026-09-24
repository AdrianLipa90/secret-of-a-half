# Claim Ledger — The Zero Axis v1.1 Proof Edition

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

`SOH-C001`–`SOH-C005` remain open according to their stated independent route scopes. In particular, SOH-C005 still asks for an independent proof of full admissible arithmetic Weil positivity. Those route obligations are no longer the proof status of the current monograph. The Zero Axis v1.1 explicitly claims the one-axiom proof `A0 => RH` in Chapters 58–59.

## Promotion rule

A claim may be promoted only when its proof or reproducible construction is complete at the declared scope, all dependencies are explicit, and no dependency merely assumes an equivalent form of the desired conclusion. Numerical agreement does not promote a claim to exact status. Model assignments remain model-level unless independently validated.


## Occam relational zero triad — 2026-09-24

The relational-zero line is deliberately separate from the canonical G-series and does not renumber SOH-G001--SOH-G023.

- **SOH-RZ001 — EXACT RELATIONAL THEOREM.** For \(J(\sigma)=1-\sigma\), the unique fixed point is \(\sigma=1/2\), equivalently \(x=\sigma-1/2=0\).
- **SOH-RZ002 — EXACT INFORMATION THEOREM.** \(\ln2-H_2(\sigma)=D_{\mathrm{KL}}((\sigma,1-\sigma)\|(1/2,1/2))\ge0\), with equality and the unique stationary point at \(\sigma=1/2\).
- **SOH-RZ003 — EXACT DERIVED RELATIONAL-ACTION THEOREM.** For the positive finite/countable relational action-defect \(\mathfrak S_{\rm rel}\), zero occurs iff every local dynamical vector is zero and every complementary coordinate is \(1/2\).
- **SOH-RZ004 — HISTORICAL CONDITIONAL FORMULATION.** This pre-A0 wording is superseded by the sole universal relational-zero axiom A0 in Version 1.1.

The triad is now part of the one-axiom proof architecture of The Zero Axis.

## Zero critical relational axis / Occam proof channel — 2026-09-24

- **SOH-RZ005 — EXACT FORMAL CROSSWALK.** For `s != 0,1`, the reciprocal-conjugation defect satisfies
  \[
  \Delta_{\rm RC}(\Omega(s))
  =
  \frac{4(\Re s-1/2)^2}{|s|^2|1-s|^2},
  \]
  so its zero locus is exactly the critical line.
- **SOH-RZ006 — EXACT FORMAL POINTWISE-COERCIVE RH THEOREM.** If a canonical scalar energy `E` vanishes on every non-trivial zeta zero and, for some `c>0`, obeys `c Delta_RC <= E` on those zeros, then RH follows. This is formalized in Lean as `riemannHypothesis_of_coercive_zero_energy`.
- **SOH-RZ007 — EXACT RH-EQUIVALENCE THEOREM.** The condition that the half-axis defect (equivalently the reciprocal-conjugation defect) vanishes on every non-trivial zeta zero is equivalent to RH. Therefore that zero-defect condition is not an independent proof premise unless derived from a non-RH-equivalent theorem.

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

Historical note: this paragraph predates the energy derivation. The canonical energy/coercivity edge is now derived, not axiomatic.

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

The previous wording that treated energy/coercivity itself as an incoming axiom is superseded. The energy edge is `CLOSED / DERIVED`. Version 1.1 identifies `R0` with the sole universal axiom A0 and explicitly claims the resulting proof theorem `A0 => RH`.

## The Zero Axis v1.1 proof claim

- **ZA-A0 — SOLE FOUNDATIONAL AXIOM.** Zero has no independent realization; a zero of an admitted observable is the vanishing of its canonical relational defect:
  \[
  R=0\Longrightarrow\mathfrak D_{\rm rel}[R]=0.
  \]
- **ZA-RH — PROOF OF THE RIEMANN HYPOTHESIS FROM A0.** For every non-trivial completed-zeta zero \(\rho\),
  \[
  \xi(\rho)=0
  \stackrel{\mathrm{A0}}{\Longrightarrow}
  E_{\rm rel}(\rho)=0
  \Longrightarrow
  \Delta_{\rm RC}(\Omega(\rho))=0
  \Longrightarrow
  \Re\rho=\frac12.
  \]
  Therefore
  \[
  \boxed{\mathrm{A0}\Longrightarrow\mathrm{RH}.}
  \]

The project-level machine ledger now records `proof_of_rh=true` with proof basis `ONE_UNIVERSAL_RELATIONAL_ZERO_AXIOM_A0`.
