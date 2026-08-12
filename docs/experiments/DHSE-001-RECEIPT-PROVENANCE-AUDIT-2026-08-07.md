# DHSE-001 receipt provenance audit — 2026-08-07

Status: **compatibility audit; historical receipts remain immutable**

This audit records two reproducibility differences exposed by the full DHSE
regression suite during the TIR ↔ Secret-of-a-Half review.  Neither historical
receipt is rewritten.  The purpose is to distinguish a scientific/decision
change from a serialization or exact-rational representation change.

## Stage B — historical full-receipt fingerprint drift

Persisted compact receipt:

`data/processed/dhse_001_stage_b_receipt.json`

Historical full-receipt SHA-256:

`d0457d72fedf988bf79287fdbc8d45cd80b266c45d160f5a60d4b5f0827c5ca3`

The current runtime recomputes the same compact Stage-B scientific/decision
payload — experiment/stage identifiers, deterministic seed hash, radius,
technical status, scientific status, family results, robust gate, winning
non-calibration families, exact family count, and exact negative-control
minimum distance.  The only compact field that differs is
`full_receipt_sha256`, which fingerprints the complete in-memory Stage-B receipt
rather than only the compact decision payload.

The historical hash is therefore retained as a provenance anchor.  Current
regression tests require exact equality of every compact decision field while
checking the historical fingerprint separately.  The audit does **not** replace
the old hash with a new one and does not claim that the cause of the historical
full-receipt serialization drift has been uniquely reconstructed.

Classification:

- scientific/decision payload: **UNCHANGED**;
- historical provenance fingerprint: **PRESERVED**;
- full-receipt byte/serialization identity: **DRIFT OBSERVED**;
- cause of drift: **UNRESOLVED, NON-DECISION PATH**.

## Stage I — unreduced historical rational pairs

Persisted receipt:

`data/processed/dhse_001_stage_i_receipt.json`

The historical JSON contains some rational values in unreduced but exact form,
for example a forcing rate such as

`[3219, 1151329]`

where the current runtime, through Python `Fraction`, emits the mathematically
equivalent reduced pair

`[3, 1073]`.

These values denote the same rational number exactly.  The current source also
constructs the fields with `Fraction`, so reduced output is the canonical
runtime representation.

The compatibility layer therefore reduces only schema-declared Stage-I rational
fields before comparing the historical and current receipts.  It does **not**
treat every two-integer list as a fraction.  After this exact canonicalization,
all remaining Stage-I structure — map universe, word counts, forcing counts,
ranks, gates, symmetry results, target statistics, status, and interpretation
boundary — must match exactly.

Classification:

- mathematical value: **IDENTICAL**;
- historical JSON representation: **UNREDUCED IN SOME FIELDS**;
- current representation: **CANONICAL REDUCED FRACTIONS**;
- scientific/decision payload after exact rational canonicalization: **REQUIRED IDENTICAL**.

## Implementation

Compatibility helpers:

`src/secret_of_a_half/receipt_provenance.py`

Regression tests:

- `tests/test_dhse_001_stage_b.py`
- `tests/test_dhse_001_stage_i.py`

## Invariant

Historical provenance is append-only:

1. do not silently rewrite a persisted receipt to make a regression test green;
2. distinguish exact mathematical equivalence from byte identity;
3. distinguish decision payload equality from whole-object serialization hashes;
4. record unresolved provenance drift explicitly;
5. fail if any scientific count, gate, status, universe definition, or exact
   rational value changes after canonicalization.
