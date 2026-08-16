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
