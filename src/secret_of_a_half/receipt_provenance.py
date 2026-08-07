"""Compatibility helpers for immutable historical DHSE receipts.

Historical receipts are provenance records and are not rewritten merely because
a later runtime serializes an equivalent exact value differently.  These helpers
separate scientific/decision payload equality from representation-level or
historical full-receipt fingerprints.
"""
from __future__ import annotations

from copy import deepcopy
from fractions import Fraction
from typing import Any

STAGE_B_HISTORICAL_FULL_RECEIPT_SHA256 = (
    "d0457d72fedf988bf79287fdbc8d45cd80b266c45d160f5a60d4b5f0827c5ca3"
)

_STAGE_I_PAIR_KEYS = {
    "radius",
    "pass_ratio",
    "odds",
    "forcing_rate",
    "median_control_count",
    "target_to_control_median_ratio",
}
_STAGE_I_PAIR_SEQUENCE_KEYS = {
    "centres_odds",
    "target_rate_sequence",
}


def payload_without_full_receipt_hash(receipt: dict[str, Any]) -> dict[str, Any]:
    """Return the semantic compact payload while retaining the input unchanged."""
    payload = deepcopy(receipt)
    payload.pop("full_receipt_sha256", None)
    return payload


def canonical_fraction_pair(value: Any) -> Any:
    """Reduce a JSON exact-rational pair ``[numerator, denominator]``.

    Non-pairs and ``None`` are returned unchanged so callers can apply this only
    at schema-declared rational fields.
    """
    if (
        isinstance(value, list)
        and len(value) == 2
        and all(isinstance(item, int) and not isinstance(item, bool) for item in value)
        and value[1] != 0
    ):
        fraction = Fraction(value[0], value[1])
        return [fraction.numerator, fraction.denominator]
    return value


def _canonical_fraction_sequence(value: Any) -> Any:
    """Reduce each exact-rational pair in a schema-declared sequence field."""
    if not isinstance(value, list):
        return value
    return [canonical_fraction_pair(item) for item in value]


def canonicalize_stage_i_receipt(receipt: dict[str, Any]) -> dict[str, Any]:
    """Canonicalize only schema-declared rational fields of a Stage-I receipt.

    The original Stage-I JSON contains some unreduced but mathematically exact
    fraction pairs.  Current code uses :class:`fractions.Fraction`, which emits
    reduced pairs.  This function makes the equivalence explicit without
    rewriting the historical receipt or treating arbitrary two-integer lists as
    fractions.
    """

    def visit(value: Any) -> Any:
        """Walk nested receipt values while normalizing only declared fields."""
        if isinstance(value, dict):
            normalized: dict[str, Any] = {}
            for key, item in value.items():
                if key in _STAGE_I_PAIR_KEYS:
                    normalized[key] = canonical_fraction_pair(item)
                elif key in _STAGE_I_PAIR_SEQUENCE_KEYS:
                    normalized[key] = _canonical_fraction_sequence(item)
                else:
                    normalized[key] = visit(item)
            return normalized
        if isinstance(value, list):
            return [visit(item) for item in value]
        return value

    return visit(deepcopy(receipt))
