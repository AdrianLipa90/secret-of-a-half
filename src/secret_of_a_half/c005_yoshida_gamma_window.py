"""Rigorous explicit gamma-window envelope for the Yoshida/Suzuki flow.

For real z put
    w = 1/4 - i z/2,
    G(z) = Re psi(w) - (1/2) log(pi).

DLMF 5.11.2 together with the complex remainder bound in 5.11(ii), truncated
before the B2 term, gives on Re(w)>0

    psi(w) = log(w) - 1/(2w) + R(w),
    |R(w)| <= sec(arg(w)/2)^3 / (12 |w|^2).

Here |arg(w)| < pi/2, hence sec(arg(w)/2)^3 <= 2 sqrt(2).  Therefore

    G(z) >= log|w| - (1/8 + sqrt(2)/6)/|w|^2 - (1/2)log(pi),

and a corresponding upper envelope is available.

The explicit tail threshold below is intentionally conservative.  It removes
the existential t0/C0 step from the analytic plumbing without pretending that
the resulting constants are numerically efficient.
"""
from __future__ import annotations

from dataclasses import dataclass

import mpmath as mp


mp.mp.dps = max(mp.mp.dps, 80)

_REMAINDER_COEFF = mp.sqrt(2) / 6
_LOWER_RADIAL_COEFF = mp.mpf(1) / 8 + _REMAINDER_COEFF
_UPPER_RADIAL_COEFF = _REMAINDER_COEFF - mp.mpf(1) / 8
_SIMPLE_TAIL_COEFF = mp.mpf(1) / 2 + 2 * mp.sqrt(2) / 3


@dataclass(frozen=True)
class GammaWindowCertificate:
    target_C: str
    t0: str
    C0_upper: str
    tail_lower_at_t0: str
    tail_margin: str

    @property
    def pass_tail(self) -> bool:
        return mp.mpf(self.tail_margin) > 0


def _positive_mpf(value: float | str | mp.mpf, name: str) -> mp.mpf:
    x = mp.mpf(value)
    if not mp.isfinite(x) or x <= 0:
        raise ValueError(f"{name} must be finite and positive")
    return x


def gamma_radius(z_abs: float | str | mp.mpf) -> mp.mpf:
    """|1/4 - i z/2| for real z, expressed through |z|."""
    z = mp.mpf(z_abs)
    if z < 0 or not mp.isfinite(z):
        raise ValueError("z_abs must be finite and non-negative")
    return mp.sqrt(mp.mpf(1) / 16 + z * z / 4)


def gamma_profile_lower(z_abs: float | str | mp.mpf) -> mp.mpf:
    """DLMF-based lower envelope for G(z) at real |z|."""
    r = gamma_radius(z_abs)
    return (
        mp.log(r)
        - _LOWER_RADIAL_COEFF / (r * r)
        - mp.log(mp.pi) / 2
    )


def gamma_profile_upper(z_abs: float | str | mp.mpf) -> mp.mpf:
    """DLMF-based pointwise upper envelope for G(z) at real |z|."""
    r = gamma_radius(z_abs)
    return (
        mp.log(r)
        + _UPPER_RADIAL_COEFF / (r * r)
        - mp.log(mp.pi) / 2
    )


def simple_tail_lower(z_abs: float | str | mp.mpf) -> mp.mpf:
    """Simpler monotone lower bound used for an explicit t0 schedule.

    For |z|>0:
        G(z) >= log(|z|/(2 sqrt(pi))) - K/|z|^2,
    K = 1/2 + 2 sqrt(2)/3.
    """
    z = _positive_mpf(z_abs, "z_abs")
    return (
        mp.log(z / (2 * mp.sqrt(mp.pi)))
        - _SIMPLE_TAIL_COEFF / (z * z)
    )


def explicit_t0_for_target_C(
    target_C: float | str | mp.mpf,
) -> mp.mpf:
    """Conservative closed-form t0 with G(z)>C for all |z|>=t0.

    We choose
        t0 = 2 sqrt(pi) exp(C+1).
    Since C>0 in the Yoshida gate, t0>1 and
        log(t0/(2sqrt(pi))) = C+1,
    while K/t0^2 < 1.  Thus the simple tail lower bound is > C.
    """
    C = _positive_mpf(target_C, "target_C")
    return 2 * mp.sqrt(mp.pi) * mp.exp(C + 1)


def compact_C0_upper(t0: float | str | mp.mpf) -> mp.mpf:
    """Uniform upper envelope for max_{|z|<=t0} G(z).

    Since |w|>=1/4 and |w|<=sqrt(1/16+t0^2/4),
        G(z) <= log(r_max) + 16*A_+ - 1/2 log(pi),
    where A_+ = sqrt(2)/6 - 1/8 > 0.
    """
    t = _positive_mpf(t0, "t0")
    r_max = gamma_radius(t)
    return (
        mp.log(r_max)
        + 16 * _UPPER_RADIAL_COEFF
        - mp.log(mp.pi) / 2
    )


def gamma_window_certificate(
    target_C: float | str | mp.mpf,
) -> GammaWindowCertificate:
    """Return a deterministic explicit (t0,C0) certificate."""
    C = _positive_mpf(target_C, "target_C")
    t0 = explicit_t0_for_target_C(C)
    tail_lower = simple_tail_lower(t0)
    margin = tail_lower - C
    C0 = compact_C0_upper(t0)
    if margin <= 0:
        raise RuntimeError("internal gamma-tail certificate failed")
    return GammaWindowCertificate(
        target_C=mp.nstr(C, 50),
        t0=mp.nstr(t0, 50),
        C0_upper=mp.nstr(C0, 50),
        tail_lower_at_t0=mp.nstr(tail_lower, 50),
        tail_margin=mp.nstr(margin, 50),
    )


def gamma_window_gate_receipt(
    target_C: float | str | mp.mpf,
) -> dict[str, object]:
    cert = gamma_window_certificate(target_C)
    return {
        "schema": "SOH_YOSHIDA_GAMMA_WINDOW_V0_1",
        "target_C": cert.target_C,
        "t0": cert.t0,
        "C0_upper": cert.C0_upper,
        "tail_lower_at_t0": cert.tail_lower_at_t0,
        "tail_margin": cert.tail_margin,
        "tail_gate_pass": cert.pass_tail,
        "analytic_basis": [
            "DLMF 5.11.2 digamma asymptotic expansion",
            "DLMF 5.11(ii) complex remainder bound at n=1",
            "|arg(1/4-i z/2)|<pi/2 implies sec(arg/2)^3<=2*sqrt(2)",
        ],
        "closed": [
            "explicit conservative gamma-tail threshold t0(C)",
            "explicit compact gamma upper envelope C0(t0)",
        ],
        "open": [
            "extract exact coefficients of Suzuki equation (4.11) in repository normalization",
            "localized form/domain/boundary/Friedrichs join",
            "efficient constant optimization",
            "uniform Schur gap and completion-null-mode exclusion",
            "SOH-C005",
            "Riemann Hypothesis",
        ],
        "proof_of_rh": False,
    }
