"""Explicit safe constants from Suzuki 2023 Theorem 4.3 at contour c=2.

The point is to close two previously implicit constants analytically:

C1 <= 5/6 on Re(s)=3, using the absolutely convergent Dirichlet series and
Lambda(n) <= log n <= n-1.

C2(a1) <= (exp(4 a1)-1)/(4 a1), using Suzuki's explicit K(t,u;y) formula.

The remaining gamma-window constants t0 and C0 are intentionally left open for
rigorous interval/asymptotic certification.
"""
from __future__ import annotations

from dataclasses import dataclass
import math


C1_MAJORANT_C_EQ_2 = 5.0 / 6.0


@dataclass(frozen=True)
class YoshidaConstantEnvelope:
    a1: float
    target_mu: float
    safety_margin: float
    c1_majorant: float
    c2_majorant: float
    chosen_C: float
    bulk_coefficient: float

    @property
    def source_inequality_margin(self) -> float:
        return self.chosen_C - (
            3.0 * self.c1_majorant * self.c2_majorant + self.target_mu
        )

    @property
    def pass_source_gate(self) -> bool:
        return self.source_inequality_margin > 0.0


def c1_majorant_c_eq_2() -> float:
    """Safe analytic majorant for Suzuki's C1 with contour parameter c=2."""
    return C1_MAJORANT_C_EQ_2


def c2_majorant_c_eq_2(a1: float) -> float:
    """Safe analytic majorant for K(t,u;+/-2) / K(t,u) on |t|,|u|<=a1."""
    if a1 <= 0.0 or not math.isfinite(a1):
        raise ValueError("a1 must be finite and positive")
    x = 4.0 * a1
    return math.expm1(x) / x


def choose_constant_envelope(
    a1: float,
    target_mu: float,
    *,
    safety_margin: float = 1.0,
) -> YoshidaConstantEnvelope:
    """Choose C > 3 C1 C2 + mu with an explicit positive margin."""
    if target_mu <= 0.0 or not math.isfinite(target_mu):
        raise ValueError("target_mu must be finite and positive")
    if safety_margin <= 0.0 or not math.isfinite(safety_margin):
        raise ValueError("safety_margin must be finite and positive")

    c1 = c1_majorant_c_eq_2()
    c2 = c2_majorant_c_eq_2(a1)
    chosen_C = 3.0 * c1 * c2 + target_mu + safety_margin
    bulk = chosen_C - 2.0 * c1 * c2
    return YoshidaConstantEnvelope(
        a1=a1,
        target_mu=target_mu,
        safety_margin=safety_margin,
        c1_majorant=c1,
        c2_majorant=c2,
        chosen_C=chosen_C,
        bulk_coefficient=bulk,
    )


def constant_gate_receipt(a1: float, target_mu: float) -> dict[str, object]:
    env = choose_constant_envelope(a1, target_mu)
    return {
        "schema": "SOH_YOSHIDA_CONSTANT_GATE_V0_1",
        "contour_c": 2.0,
        "a1": env.a1,
        "target_mu": env.target_mu,
        "C1_majorant": env.c1_majorant,
        "C2_majorant": env.c2_majorant,
        "chosen_C": env.chosen_C,
        "bulk_coefficient_C_minus_2C1C2": env.bulk_coefficient,
        "source_gate_pass": env.pass_source_gate,
        "closed": [
            "C1 majorant at c=2",
            "C2(a1) kernel-ratio majorant at c=2",
            "choice C > 3*C1*C2 + mu",
        ],
        "open": [
            "rigorous gamma-tail threshold t0 for the chosen C",
            "rigorous compact gamma maximum C0 on |z|<=t0",
            "localized operator/domain join",
            "uniform Schur gap",
            "SOH-C005",
            "Riemann Hypothesis",
        ],
        "proof_of_rh": False,
    }
