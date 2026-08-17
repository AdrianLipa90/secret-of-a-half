#!/usr/bin/env python3
"""Deterministic receipt for SOH-G007 exact Uroboros identities."""
from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

from secret_of_a_half.uroboros import (
    UROBOROS_SCALE,
    exact_halving_s,
    exact_odd_collatz_s,
    exact_x_to_s,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports" / "SOH_G007_UROBOROS_RECEIPT_V1.json"


def main() -> None:
    chain = [Fraction(16), Fraction(8), Fraction(4), Fraction(2), Fraction(1), Fraction(1, 2)]
    mapped = [exact_x_to_s(x) for x in chain]
    expected = [
        Fraction(32, 33), Fraction(16, 17), Fraction(8, 9),
        Fraction(4, 5), Fraction(2, 3), Fraction(1, 2),
    ]
    if mapped != expected:
        raise RuntimeError("fundamental halving chain failed exact conjugacy")
    for current, nxt in zip(mapped, mapped[1:]):
        if exact_halving_s(current) != nxt:
            raise RuntimeError("halving map failed exact rational check")

    branch_rows = []
    for n in range(1, 65):
        s = exact_x_to_s(Fraction(n))
        next_n = n // 2 if n % 2 == 0 else 3 * n + 1
        transformed = exact_halving_s(s) if n % 2 == 0 else exact_odd_collatz_s(s)
        expected_next = exact_x_to_s(Fraction(next_n))
        if transformed != expected_next:
            raise RuntimeError(f"Collatz conjugacy failed at n={n}")
        branch_rows.append({"n": n, "branch": "even" if n % 2 == 0 else "odd"})

    if UROBOROS_SCALE != 32:
        raise RuntimeError("Uroboros scale must equal 2^5 = 32")

    payload = {
        "certificate": "SOH_G007_UROBOROS_RECEIPT_V1",
        "status": "EXACT_ALGEBRAIC_IDENTITIES_VERIFIED",
        "fundamental_chain": [str(x) for x in chain],
        "s_chain": [str(x) for x in mapped],
        "uroboros_scale": UROBOROS_SCALE,
        "collatz_branch_checks": len(branch_rows),
        "claims": {
            "half_layer_x_maps_to_s_half": True,
            "halving_conjugacy": True,
            "odd_branch_conjugacy": True,
            "scale_32_from_five_halvings": True,
            "all_collatz_orbits_converge": False,
            "xi_has_scale_32_law": False,
            "rh_proved": False,
        },
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
