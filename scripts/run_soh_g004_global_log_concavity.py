from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


def main() -> None:
    # Entirely conservative rational constants used by the analytic proof.
    channel_margin = Fraction(-7, 1)

    # n=2 variance contribution: 14112 e^-9, with e^3 > 20 => e^9 > 8000.
    n2_bound = Fraction(14112, 8000)

    # n=3 first tail term: 98*81*64*e^-24, with e^3 > 20 => e^24 > 20^8.
    n3_bound = Fraction(98 * 81 * 64, 20**8)

    # For n>=3 successive conservative terms have ratio < 12/20^7.
    tail_ratio = Fraction(12, 20**7)
    if not tail_ratio < 1:
        raise AssertionError("SOH-G004 tail ratio must be below one")

    tail_bound = n3_bound / (1 - tail_ratio)
    variance_bound = n2_bound + tail_bound
    if not variance_bound < 2:
        raise AssertionError("SOH-G004 conservative variance bound must remain below two")

    compactified_margin = channel_margin + 2
    if not compactified_margin < 0:
        raise AssertionError("SOH-G004 compactified curvature margin must be negative")

    receipt = {
        "claim_id": "SOH-G004",
        "status": "PROVED_KERNEL_WEIGHT_LOG_CONCAVITY",
        "proof_of_real_rootedness": False,
        "proof_of_rh": False,
        "constants": {
            "pi_lower": "3",
            "pi_upper": "22/7",
            "e_cubed_lower": "20",
        },
        "bounds": {
            "per_channel_compactified_margin_upper": str(channel_margin),
            "n2_variance_upper": str(n2_bound),
            "n_ge_3_tail_upper": str(tail_bound),
            "total_variance_upper": str(variance_bound),
            "total_variance_upper_decimal": float(variance_bound),
            "global_compactified_margin_upper": str(compactified_margin),
        },
        "conclusion": "d2/deta2 log W(eta) < 0 for 0 <= eta < 1",
        "open_target": "SOH-G003 real-rootedness of F",
    }

    out = Path("reports/SOH_G004_GLOBAL_LOG_CONCAVITY_V0_2.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
