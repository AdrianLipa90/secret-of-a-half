# 2026-07-30 — PhaseNav–Weil adaptive cutoff schedule v0.6

## Scope

Extended the fixed-finite-section prime-tail certificate to a basis-adaptive
diagonal schedule.

## Changes

- Added `secret_of_half_weil_adaptive_cutoff_schedule.pnv`.
- Added parser, exact elementary envelope, asymptotic coarse majorant and audit executor.
- Added the schedule `log Q_N=max(log 100000,2N)`.
- Added a sharp v0.5 certificate scan through `N=20`.
- Added deterministic JSON receipt and eight regression tests.
- Added Chapter 20 and synchronized Markdown, JSON and LaTeX claim ledgers.
- Added `SOH-L021` and `SOH-N006`.

## Result

- All declared sections pass `1e-12`.
- Maximum certified norm: `3.280365246530569e-14` at `N=5`.
- The coarse envelope decreases on the final audit window.
- Exact asymptotic theorem: for every `c>0`, `Q_N=exp(cN)` forces the coarse envelope to zero.

## Boundary

The result is basis-adaptive, not fixed-cutoff uniform. Global arithmetic
positivity, form closure, the null-space implication and `SOH-C005` remain
open. No proof of RH is claimed.
