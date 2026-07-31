"""Compact deterministic receipt for DHSE-001 Stage B."""
from __future__ import annotations

import hashlib
import json
from typing import Any

from .dhse_001_stage_b import run_stage_b


def compact_stage_b_receipt(full: dict[str, Any] | None = None) -> dict[str, Any]:
    receipt = run_stage_b() if full is None else full
    canonical = json.dumps(
        receipt,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")
    return {
        "experiment": receipt["experiment"],
        "stage": receipt["stage"],
        "base_seed": receipt["base_seed"],
        "parameters": receipt["parameters"],
        "primary_rule": receipt["primary_rule"],
        "families": [
            {
                "family": row["family"],
                "calibration_only": row["calibration_only"],
                "maps": row["maps"],
                "reciprocal_conjugacy_sample_matches": row[
                    "reciprocal_conjugacy_sample_matches"
                ],
                "reciprocal_conjugacy_sample_comparisons": row[
                    "reciprocal_conjugacy_sample_comparisons"
                ],
                "observed_states": row["observed_states"],
                "observed_transitions": row["observed_transitions"],
                "primary_statistic": row["primary_statistic"],
            }
            for row in receipt["families"]
        ],
        "summary": receipt["summary"],
        "technical_status": receipt["technical_status"],
        "scientific_status": receipt["scientific_status"],
        "interpretation_boundary": receipt["interpretation_boundary"],
        "full_receipt_sha256": hashlib.sha256(canonical).hexdigest(),
    }
