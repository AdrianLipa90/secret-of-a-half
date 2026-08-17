#!/usr/bin/env python3
"""Deterministic exact-rational receipt for SOH-G009 Bloch rapidity conjugacy."""
from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

from secret_of_a_half.uroboros import (
    compose_boost_parameters,
    exact_halving_t,
    exact_odd_collatz_t,
    exact_scale_t,
    exact_x_to_t,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports" / "SOH_G009_BLOCH_RAPIDITY_RECEIPT_V1.json"


def main() -> None:
    chain = [Fraction(16), Fraction(8), Fraction(4), Fraction(2), Fraction(1), Fraction(1, 2)]
    t_chain = [exact_x_to_t(x) for x in chain]
    expected = [
        Fraction(31, 33), Fraction(15, 17), Fraction(7, 9),
        Fraction(3, 5), Fraction(1, 3), Fraction(0),
    ]
    if t_chain != expected:
        raise RuntimeError("centered-coordinate fundamental chain mismatch")

    for current, nxt in zip(t_chain, t_chain[1:]):
        if exact_halving_t(current) != nxt:
            raise RuntimeError("exact halving Möbius translation mismatch")

    p = Fraction(-1, 3)
    total = p
    for _ in range(4):
        total = compose_boost_parameters(total, p)
    if total != Fraction(-31, 33):
        raise RuntimeError("five-step boost parameter must equal -31/33")

    if exact_scale_t(Fraction(31, 33), Fraction(1, 32)) != 0:
        raise RuntimeError("scale 1/32 must send 31/33 to centered zero")

    branch_checks = 0
    for n in range(1, 65):
        t = exact_x_to_t(Fraction(n))
        next_n = n // 2 if n % 2 == 0 else 3 * n + 1
        transformed = exact_halving_t(t) if n % 2 == 0 else exact_odd_collatz_t(t)
        expected_next = exact_x_to_t(Fraction(next_n))
        if transformed != expected_next:
            raise RuntimeError(f"centered Collatz branch conjugacy failed at n={n}")
        branch_checks += 1

    payload = {
        "certificate": "SOH_G009_BLOCH_RAPIDITY_RECEIPT_V1",
        "status": "EXACT_RATIONAL_IDENTITIES_VERIFIED",
        "x_chain": [str(x) for x in chain],
        "t_chain": [str(t) for t in t_chain],
        "single_halving_parameter": "-1/3",
        "five_halving_parameter": str(total),
        "branch_checks": branch_checks,
        "claims": {
            "half_layer_maps_to_centered_zero": True,
            "halving_is_hyperbolic_mobius_translation": True,
            "five_halvings_send_31_over_33_to_zero": True,
            "all_collatz_orbits_converge": False,
            "xi_zero_location_proved": False,
            "rh_proved": False,
        },
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
