"""Explicit unconditional envelopes for the zeta screw function.

For t>=0 Suzuki's Psi formula gives g(t)=-Psi(t).  Using only

    Lambda(n) <= log n,
    sum_{n=2}^M n^(-1/2) <= 2(sqrt(M)-1),

and elementary Hurwitz--Lerch majorants, one obtains closed upper bounds for

    G0(T) = int_0^T |g(t)|^2 dt,
    G1(T) = int_0^T |g'(t)|^2 dt.

The formulas below are intentionally conservative but unconditional.  They
use mpmath interval arithmetic to evaluate the closed-form upper envelopes
with outward rounding.

These are scalar analytic envelopes only.  They do not prove a finite low
Fourier block is positive and therefore do not prove C005 or RH.
"""
from __future__ import annotations

from dataclasses import dataclass
import math

import mpmath as mp


iv = mp.iv


@dataclass(frozen=True)
class ScrewL2Envelope:
    a0: float
    T: float
    g_l2_sq_upper: float
    gprime_l2_sq_upper: float
    pointwise_g_abs_upper: float
    derivative_regular_part_upper: float


@dataclass(frozen=True)
class UniformMixedTailEnvelope:
    a0: float
    target_epsilon: float
    cutoff_N: int
    mixed_norm_upper: float
    g_l2_sq_upper: float
    gprime_l2_sq_upper: float

    @property
    def pass_target(self) -> bool:
        return self.mixed_norm_upper <= self.target_epsilon


def _point_interval(value: float | str) -> object:
    x = float(value)
    if not math.isfinite(x) or x <= 0.0:
        raise ValueError("value must be finite and positive")
    return iv.mpf([x, x])


def _upper(x: object) -> float:
    return float(x.b)


def screw_l2_envelope(a0: float | str) -> ScrewL2Envelope:
    """Uniform 1D g/g' L2 envelopes on [0,2*a0]."""
    a = _point_interval(a0)
    T = 2 * a

    # |psi(1/4)-log(pi)| via the exact digamma quarter-value identity:
    # psi(1/4) = -EulerGamma - pi/2 - 3 log 2.
    Aabs = iv.euler + iv.pi / 2 + 3 * iv.log(2) + iv.log(iv.pi)
    C = iv.pi**2 + 8 * iv.catalan

    exp_half = iv.exp(T / 2)
    exp_minus_half = iv.exp(-T / 2)

    # Prime hinge:
    # sum Lambda(n)/sqrt(n)*(t-log n)
    # <= 2 t^2 (exp(t/2)-1), uniformly maximized at T.
    prime_hinge = 2 * T**2 * (exp_half - 1)

    exp_piece = 4 * (exp_half + exp_minus_half - 2)
    linear_piece = Aabs * T / 2
    lerch2_piece = C / 4

    g_abs_upper = exp_piece + prime_hinge + linear_piece + lerch2_piece
    g_l2_sq = T * g_abs_upper**2

    # A.e. derivative bound:
    # prime derivative <= 2 T (exp(T/2)-1)
    # and
    # 0.5*exp(-t/2)*Phi(exp(-2t),1,1/4)
    # <= 2 + 0.5*[-log(1-exp(-2t))].
    # Since exp(2t)>=1+2t,
    # -log(1-exp(-2t)) <= log((1+2T)/(2t)).
    prime_derivative = 2 * T * (exp_half - 1)
    exp_derivative = 2 * (exp_half - exp_minus_half)
    K = prime_derivative + exp_derivative + Aabs / 2 + 2

    L0 = iv.log((1 + 2 * T) / (2 * T))
    # Integrals:
    # int_0^T log(A/t) dt = T(L0+1)
    # int_0^T log(A/t)^2 dt = T(L0^2+2L0+2)
    gprime_l2_sq = T * (
        K**2
        + K * (L0 + 1)
        + iv.mpf("0.25") * (L0**2 + 2 * L0 + 2)
    )

    return ScrewL2Envelope(
        a0=float(a0),
        T=2.0 * float(a0),
        g_l2_sq_upper=_upper(g_l2_sq),
        gprime_l2_sq_upper=_upper(gprime_l2_sq),
        pointwise_g_abs_upper=_upper(g_abs_upper),
        derivative_regular_part_upper=_upper(K),
    )


def uniform_mixed_norm_sq_upper(
    a0: float | str,
    cutoff_N: int,
) -> float:
    """Uniform mixed-form norm-square bound for every 0<a<=a0.

    From the screw-kernel reduction:
      E_boundary <= 4 G0,
      E_du <= 16 a G1.

    Therefore
      eps^2 <= [8 a G0 + 64 a^3 G1]/(pi^2 N).

    Monotonicity of the positive right side lets us evaluate at a0.
    """
    if cutoff_N < 1:
        raise ValueError("cutoff_N must be positive")
    env = screw_l2_envelope(a0)

    a = _point_interval(a0)
    G0 = iv.mpf([env.g_l2_sq_upper, env.g_l2_sq_upper])
    G1 = iv.mpf([env.gprime_l2_sq_upper, env.gprime_l2_sq_upper])
    value = (8 * a * G0 + 64 * a**3 * G1) / (iv.pi**2 * cutoff_N)
    return _upper(value)


def uniform_mixed_norm_upper(
    a0: float | str,
    cutoff_N: int,
) -> float:
    return math.sqrt(uniform_mixed_norm_sq_upper(a0, cutoff_N))


def cutoff_for_uniform_mixed_norm(
    a0: float | str,
    target_epsilon: float,
) -> UniformMixedTailEnvelope:
    """Explicit N ensuring the analytic mixed-tail envelope <= epsilon."""
    if not math.isfinite(target_epsilon) or target_epsilon <= 0.0:
        raise ValueError("target_epsilon must be finite and positive")

    env = screw_l2_envelope(a0)
    a = float(a0)
    numerator = (
        8.0 * a * env.g_l2_sq_upper
        + 64.0 * a**3 * env.gprime_l2_sq_upper
    )
    denominator = math.pi**2 * target_epsilon**2
    cutoff = max(1, math.ceil(numerator / denominator))
    bound = uniform_mixed_norm_upper(a, cutoff)
    while bound > target_epsilon:
        cutoff += 1
        bound = uniform_mixed_norm_upper(a, cutoff)

    return UniformMixedTailEnvelope(
        a0=a,
        target_epsilon=target_epsilon,
        cutoff_N=cutoff,
        mixed_norm_upper=bound,
        g_l2_sq_upper=env.g_l2_sq_upper,
        gprime_l2_sq_upper=env.gprime_l2_sq_upper,
    )


def screw_analytic_gate_receipt(a0: float, target_epsilon: float) -> dict[str, object]:
    env = screw_l2_envelope(a0)
    mixed = cutoff_for_uniform_mixed_norm(a0, target_epsilon)
    return {
        "schema": "SOH_ZETA_SCREW_ANALYTIC_ENVELOPES_V0_1",
        "a0": a0,
        "T": env.T,
        "g_l2_sq_upper": env.g_l2_sq_upper,
        "gprime_l2_sq_upper": env.gprime_l2_sq_upper,
        "pointwise_g_abs_upper": env.pointwise_g_abs_upper,
        "derivative_regular_part_upper": env.derivative_regular_part_upper,
        "target_mixed_epsilon": target_epsilon,
        "mixed_cutoff_N": mixed.cutoff_N,
        "mixed_norm_upper": mixed.mixed_norm_upper,
        "mixed_gate_pass": mixed.pass_target,
        "closed": [
            "unconditional closed-form majorant for int_0^(2a0)|g|^2",
            "unconditional closed-form majorant for int_0^(2a0)|g'|^2",
            "uniform mixed Fourier-tail schedule on 0<a<=a0",
        ],
        "open": [
            "finite localized low Fourier block interval enclosure",
            "sharp/optimized screw envelopes",
            "all-scale interval continuation of the low Schur gap",
            "SOH-C005",
            "Riemann Hypothesis",
        ],
        "proof_of_rh": False,
    }
