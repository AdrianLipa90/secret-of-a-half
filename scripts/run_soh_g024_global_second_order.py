#!/usr/bin/env python3
from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INTERVAL_REPORT = ROOT / "reports" / "SOH_G024_FOURTH_LOG_CURVATURE_INTERVAL_V1.json"
G024_REPORT = ROOT / "reports" / "SOH_G024_JENSEN_WIENER_KERNEL_RECEIPT_V1.json"
OUT = ROOT / "reports" / "SOH_G024_GLOBAL_SECOND_ORDER_V1.json"


def main() -> None:
    if not INTERVAL_REPORT.exists():
        raise RuntimeError("missing fourth-log-curvature interval certificate")
    if not G024_REPORT.exists():
        raise RuntimeError("missing G024 Jensen-Wiener receipt")

    interval = json.loads(INTERVAL_REPORT.read_text(encoding="utf-8"))
    g024 = json.loads(G024_REPORT.read_text(encoding="utf-8"))

    if interval.get("status") != "COMPUTER_ASSISTED_INTERVAL_PLUS_ANALYTIC_TAIL_PASS":
        raise RuntimeError("fourth-log-curvature interval certificate is not PASS")
    if "L''''(t)<20 L''(t)" not in interval.get("claim", ""):
        raise RuntimeError("fourth-log-curvature claim mismatch")
    if not g024.get("proof_firewall", {}).get("second_order_q_ge_one_ninth_proved"):
        raise RuntimeError("q>=1/9 second-order theorem is not present in G024 receipt")

    # Exact elementary upper bound on e used by the compact-core estimate.
    partial = sum(Fraction(1, 1) / __import__("math").factorial(k) for k in range(7))
    tail = Fraction(1, __import__("math").factorial(7)) * Fraction(8, 7)
    e_upper_from_series = partial + tail
    declared_e_upper = Fraction(87, 32)
    if e_upper_from_series != Fraction(31967, 11760):
        raise RuntimeError("elementary e-series upper bound identity mismatch")
    if not e_upper_from_series < declared_e_upper:
        raise RuntimeError("e<87/32 rational enclosure failed")

    # (17/14)^(3/2) < 47/35, checked without floating point by squaring.
    if not Fraction(17, 14) ** 3 < Fraction(47, 35) ** 2:
        raise RuntimeError("bridge MGF square-root rational enclosure failed")

    # Compact core q<=1/9 means u<=1/3.  The certified kernel inequality
    # L''''<20L'' and the existing L''<21 exp(2|s|) envelope give the Peano
    # trapezoid bound
    #
    #   E[u B-A] <= 280 u^3 exp(2u) E exp(2|r|).
    #
    # The sharpened bridge MGF and 2|r|<=3r^2+1/3 give
    # E exp(2|r|) <= exp(1/3)(17/14)^(3/2).  Since u<=1/3,
    # exp(2u+1/3)<=e.  Dividing by 4u^3 gives the bridge contribution
    # 70 e (17/14)^(3/2) to S_y'.
    bridge_sprime_upper = 70 * declared_e_upper * Fraction(47, 35)

    # For T=2a tanh(2au), x=2au and 0<=a<1/2,
    # F(x)=tanh(x)-x sech^2(x) has F'(x)=2x sech^2(x)tanh(x)<=2x^2.
    # Hence T-uT' <= (2/3)u^3 and its S_y' contribution is <=1/6.
    tilt_sprime_upper = Fraction(1, 6)
    sprime_upper = bridge_sprime_upper + tilt_sprime_upper

    expected_sprime_upper = Fraction(12275, 48)
    if sprime_upper != expected_sprime_upper:
        raise RuntimeError("compact-core S_y' rational bound mismatch")

    # The sharpened first-order theorem gives S_y>33/2, so S_y^2>1089/4.
    s_square_lower = Fraction(1089, 4)
    riccati_gap = s_square_lower - sprime_upper
    if riccati_gap != Fraction(793, 48) or riccati_gap <= 0:
        raise RuntimeError("compact-core Riccati gap is not strictly positive")

    payload = {
        "certificate": "SOH_G024_GLOBAL_SECOND_ORDER_V1",
        "status": "COMPUTER_ASSISTED_GLOBAL_SECOND_ORDER_COMPLETE_MONOTONICITY_PASS",
        "dependency": {
            "fourth_log_curvature": "L''''<20L'' globally; interval certificate on 0<=t<=2/5 plus analytic tail",
            "first_order_log_slope": "S_y>33/2 globally",
            "second_order_tail": "H_y''>0 for q>=1/9",
        },
        "compact_core": {
            "domain": "0<=q<=1/9, 0<|y|<1/2",
            "bridge_Sprime_upper": str(bridge_sprime_upper),
            "tilt_Sprime_upper": str(tilt_sprime_upper),
            "Sprime_upper": str(sprime_upper),
            "S_squared_lower": str(s_square_lower),
            "riccati_gap_lower": str(riccati_gap),
            "conclusion": "H_y''(q)>0 throughout the compact core; q=0 follows by continuity",
        },
        "global_conclusion": "H_y''(q)>0 for every q>=0 and every 0<|y|<1/2",
        "proof_firewall": {
            "first_order_complete_monotonicity_proved": True,
            "second_order_complete_monotonicity_global_proved": True,
            "second_order_computer_assisted_dependency": True,
            "third_and_higher_complete_monotonicity_proved": False,
            "complete_monotonicity_all_orders_proved": False,
            "strict_fourier_positivity_proved": False,
            "wiener_density_proved_for_riemann_family": False,
            "soh_g003_real_rootedness_proved": False,
            "pf3_proved": False,
            "pf_infinity_proved": False,
            "rh_proved": False,
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
