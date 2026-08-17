# Version 0.9 LaTeX Canon Reconciliation

Status: candidate pending GitHub Actions compile gate.

## Reconciled structure

- one active title page;
- one English abstract;
- 25 contiguous chapters included by `monograph/main.tex`;
- Chapter 21 remains the PhaseNav dependency canon;
- identity axis, holonomy graph, and typed solver are Chapters 22–24;
- Chapter 25 is the canonical Li negative-inverse / global Weil frontier;
- duplicate historical Chapter 19 source removed from the active tree.

## Claim-ID migration

Canonical V2 owns `SOH-L012` through `SOH-L032` exclusively. Pre-v0.9 meanings are retained under domain IDs (`SOH-WA001`, `SOH-HM*`, `SOH-ZU*`, `SOH-PT*`, `SOH-AC001`, `SOH-DHSE-M001`) with explicit legacy aliases in `claims/claim_ledger.json` and Appendix D.

## Proof firewall

`SOH-C005` remains OPEN. RH remains OPEN. The project frontier is an independent proof of full admissible arithmetic Weil positivity, equivalently global Li positivity, without an RH-equivalent premise.

## L032 audit

For the standard localized Rayleigh characterization over `C_c^infinity(-a,a)`, the domains are nested when `a` increases. Therefore the infimum is non-increasing. This is retained as an exact domain-monotonicity lemma; it does not provide the missing lower bound.

## CI hardening

`scripts/audit_monograph_integration.py` now fails closed on omitted chapters, discontinuous numbering, duplicate title pages, stale active frontmatter, canonical claim-ID duplication, legacy active claim collisions, incomplete V2 claim range, or violation of the `proof_of_rh=false` firewall. The build workflow also generates the identity/holonomy figures before compiling all 25 chapters.
