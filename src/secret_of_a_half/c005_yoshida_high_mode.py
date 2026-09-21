"""End-to-end explicit high-mode coercivity certificate at source level.

Combines:
- Suzuki equation (4.11), including its 1/(2*pi) normalization;
- explicit c=2 bounds C1 <= 5/6 and C2(a1);
- the DLMF-based explicit gamma window (t0,C0);
- the explicit Yoshida Fourier leakage B(a0,t0)/N.

For I = int_R |Phi_1(phi,z)|^2 dz and
L = int_{|z|<=t0} |Phi_1(phi,z)|^2 dz, equation (4.11) and z -> -z
symmetry give

  <phi,phi> >= [(C-2 C1 C2) I - (C+C0) L] / pi.

Hence L/I <= B/N yields the explicit raw-integral floor

  nu_N = [C-2 C1 C2 - (C+C0) B/N] / pi.

This closes the existential N in Suzuki Theorem 4.3 at source-form level.
It does NOT yet identify the repository's finite Hermite operator with the
localized Suzuki/Friedrichs operator.
"""
from __future__ import annotations

from dataclasses import dataclass

import mpmath as mp

from .c005_yoshida_gamma_window import gamma_window_certificate


mp.mp.dps = max(mp.mp.dps, 100)


@dataclass(frozen=True)
class HighModeCoercivityCertificate:
    a0: str
    a1: str
    target_mu: str
    c1_upper: str
    c2_upper: str
    chosen_C: str
    t0: str
    C0_upper: str
    leakage_B: str
    cutoff_N: str
    certified_raw_integral_floor: str
    floor_margin: str

    @property
    def pass_floor(self) -> bool:
        return mp.mpf(self.floor_margin) >= 0


def _positive(value: float | str | mp.mpf, name: str) -> mp.mpf:
    x = mp.mpf(value)
    if not mp.isfinite(x) or x <= 0:
        raise ValueError(f"{name} must be finite and positive")
    return x


def c1_upper_c_eq_2_mp() -> mp.mpf:
    return mp.mpf(5) / 6


def c2_upper_c_eq_2_mp(a1: float | str | mp.mpf) -> mp.mpf:
    a = _positive(a1, "a1")
    return mp.expm1(4 * a) / (4 * a)


def leakage_B_mp(
    a0: float | str | mp.mpf,
    t0: float | str | mp.mpf,
) -> mp.mpf:
    a = _positive(a0, "a0")
    t = _positive(t0, "t0")
    return (
        8 * a / (mp.pi**2)
        * (t + a * t**2 + a**2 * t**3 / 3)
    )


def raw_integral_floor(
    C: float | str | mp.mpf,
    c1c2: float | str | mp.mpf,
    C0: float | str | mp.mpf,
    B: float | str | mp.mpf,
    N: int,
) -> mp.mpf:
    if N < 1:
        raise ValueError("N must be positive")
    C = _positive(C, "C")
    p = _positive(c1c2, "c1c2")
    C0 = mp.mpf(C0)
    B = mp.mpf(B)
    if C0 < 0 or B < 0:
        raise ValueError("C0 and B must be non-negative")
    return (C - 2 * p - (C + C0) * B / N) / mp.pi


def explicit_high_mode_certificate(
    a0: float | str | mp.mpf,
    a1: float | str | mp.mpf,
    target_mu: float | str | mp.mpf,
    *,
    C_margin: float | str | mp.mpf = "1",
) -> HighModeCoercivityCertificate:
    """Construct an explicit N with source-level floor >= target_mu.

    We deliberately choose
        C = 3*C1*C2 + pi*mu + C_margin,
    which is stronger than the existential source choice and keeps the
    printed 1/(2*pi) factors of equation (4.11) explicit.
    """
    a0m = _positive(a0, "a0")
    a1m = _positive(a1, "a1")
    mu = _positive(target_mu, "target_mu")
    margin = _positive(C_margin, "C_margin")
    if not a1m > a0m:
        raise ValueError("a1 must be strictly larger than a0")

    c1 = c1_upper_c_eq_2_mp()
    c2 = c2_upper_c_eq_2_mp(a1m)
    p = c1 * c2

    C = 3 * p + mp.pi * mu + margin
    gamma = gamma_window_certificate(C)
    t0 = mp.mpf(gamma.t0)
    C0 = mp.mpf(gamma.C0_upper)
    B = leakage_B_mp(a0m, t0)

    denominator = C - 2 * p - mp.pi * mu
    if denominator <= 0:
        raise RuntimeError("internal raw-integral margin is not positive")

    required = (C + C0) * B / denominator
    N = max(1, int(mp.ceil(required)))

    floor = raw_integral_floor(C, p, C0, B, N)
    # Protect against arbitrary-precision ceil/string roundoff by tightening.
    while floor < mu:
        N += 1
        floor = raw_integral_floor(C, p, C0, B, N)

    return HighModeCoercivityCertificate(
        a0=mp.nstr(a0m, 50),
        a1=mp.nstr(a1m, 50),
        target_mu=mp.nstr(mu, 50),
        c1_upper=mp.nstr(c1, 50),
        c2_upper=mp.nstr(c2, 50),
        chosen_C=mp.nstr(C, 50),
        t0=mp.nstr(t0, 50),
        C0_upper=mp.nstr(C0, 50),
        leakage_B=mp.nstr(B, 50),
        cutoff_N=str(N),
        certified_raw_integral_floor=mp.nstr(floor, 50),
        floor_margin=mp.nstr(floor - mu, 50),
    )


def high_mode_gate_receipt(
    a0: float | str | mp.mpf,
    a1: float | str | mp.mpf,
    target_mu: float | str | mp.mpf,
) -> dict[str, object]:
    cert = explicit_high_mode_certificate(a0, a1, target_mu)
    digits = len(cert.cutoff_N)
    return {
        "schema": "SOH_YOSHIDA_EXPLICIT_HIGH_MODE_COERCIVITY_V0_1",
        "a0": cert.a0,
        "a1": cert.a1,
        "target_mu_raw_integral": cert.target_mu,
        "C1_upper": cert.c1_upper,
        "C2_upper": cert.c2_upper,
        "chosen_C": cert.chosen_C,
        "t0": cert.t0,
        "C0_upper": cert.C0_upper,
        "leakage_B": cert.leakage_B,
        "cutoff_N": cert.cutoff_N,
        "cutoff_decimal_digits": digits,
        "certified_raw_integral_floor": cert.certified_raw_integral_floor,
        "floor_margin": cert.floor_margin,
        "source_level_gate_pass": cert.pass_floor,
        "closed": [
            "equation (4.11) raw-integral coefficient bookkeeping",
            "explicit C1/C2 envelope at c=2",
            "explicit DLMF gamma window",
            "explicit Fourier leakage B/N",
            "constructive finite high-mode cutoff N for any bounded a interval",
        ],
        "open": [
            "repository-to-Suzuki localized operator/domain/Friedrichs join",
            "constant optimization (current certificate is intentionally conservative)",
            "low/high coupling and effective finite Schur gap in the repository operator",
            "all-scale continuation",
            "completion null-mode exclusion",
            "SOH-C005",
            "Riemann Hypothesis",
        ],
        "proof_of_rh": False,
    }
