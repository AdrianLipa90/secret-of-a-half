from __future__ import annotations

import json
from pathlib import Path

from secret_of_a_half.c005_infinite_complement import cutoff_for_window
from secret_of_a_half.phasenav_weil_prime_tail_integrals import rectangular_operator_norm_tail_bound
from secret_of_a_half.phasenav_weil_prime_tail_program import PrimeTailProgram, default_prime_tail_program_path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports" / "SOH_C005_GROWING_WINDOW_TAIL_DIAGNOSTIC_V0_2.json"


def main() -> None:
    profile = PrimeTailProgram.load(default_prime_tail_program_path())
    width = profile.gaussian_width
    low_block_stop = 2
    rows = []
    previous = None
    nonincreasing_steps = 0
    for window_stop in range(3, 13):
        schedule = cutoff_for_window(window_stop, width)
        bound = rectangular_operator_norm_tail_bound(
            0,
            low_block_stop,
            low_block_stop,
            window_stop,
            schedule.cutoff,
            width,
        )
        if previous is not None and bound <= previous:
            nonincreasing_steps += 1
        rows.append(
            {
                "low_block_stop": low_block_stop,
                "window_stop": window_stop,
                "cutoff": schedule.cutoff,
                "bound": bound,
            }
        )
        previous = bound

    receipt = {
        "schema": "SOH_C005_GROWING_WINDOW_TAIL_DIAGNOSTIC_V0_2",
        "status": "NUMERICAL_DIAGNOSTIC",
        "gaussian_width": width,
        "rows": rows,
        "nonincreasing_steps": nonincreasing_steps,
        "comparisons": max(0, len(rows) - 1),
        "claim_boundary": {
            "exact": [
                "each reported bound uses an integral-test-valid adaptive cutoff Q_M",
                "each reported rectangular norm is an upper bound for the omitted-prime tail on the stated finite window",
            ],
            "numerical": [
                "trend of the certified finite-window tail envelope for M=3..12",
            ],
            "open": [
                "existence of a vanishing M-to-infinity limit",
                "uniform infinite-complement coupling bound",
                "full epsilon_N,a control",
                "SOH-C005",
                "Riemann hypothesis",
            ],
            "proof_of_convergence": False,
            "proof_of_rh": False,
        },
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
