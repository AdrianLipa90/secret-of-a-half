"""Generic mixed Fourier-tail certificate for localized integral forms.

Let T be the integral operator on L2(-a,a) with kernel K(t,u), and let Q_N
project onto Fourier modes |n|>N for
    e_n(u)=(2a)^(-1/2) exp(pi*i*n*u/a).

Assume, in the u-variable, K(t,.) is absolutely continuous for a.e. t and

    E_boundary = ∫ |K(t,a)-K(t,-a)|^2 dt
    E_derivative = ∬ |∂_u K(t,u)|^2 du dt

are finite.

One integration by parts gives

  ||T Q_N||^2
    <= 4 a^2/(pi^2 N)
       * [E_boundary/(2a) + E_derivative].

Hence any finite low projection P_N satisfies the same mixed bound
||P_N T Q_N|| <= ||T Q_N||.

This is an abstract analytic adapter for the bounded screw integral operator
G_a itself.  It must NOT be identified with the mixed block of the Weil form
on the primitive/test-function variable psi, because
Q_W(psi)=<D psi, G_a D psi> carries derivative weights on both Fourier
indices.  The actual C005 mixed-form estimate therefore remains a separate
gate.  The actual zeta screw kernel also still needs rigorous
E_boundary/E_derivative envelopes on each a-interval.
"""
from __future__ import annotations

from dataclasses import dataclass
import math


@dataclass(frozen=True)
class KernelRegularityEnvelope:
    a: float
    boundary_jump_l2_sq: float
    du_l2_sq: float

    @property
    def energy(self) -> float:
        return self.boundary_jump_l2_sq / (2.0 * self.a) + self.du_l2_sq


@dataclass(frozen=True)
class MixedFourierTailCertificate:
    cutoff_N: int
    norm_upper: float
    norm_sq_upper: float
    regularity_energy: float

    @property
    def finite(self) -> bool:
        return math.isfinite(self.norm_upper)


def _validate_envelope(envelope: KernelRegularityEnvelope) -> None:
    if not math.isfinite(envelope.a) or envelope.a <= 0.0:
        raise ValueError("a must be finite and positive")
    for name, value in (
        ("boundary_jump_l2_sq", envelope.boundary_jump_l2_sq),
        ("du_l2_sq", envelope.du_l2_sq),
    ):
        if not math.isfinite(value) or value < 0.0:
            raise ValueError(f"{name} must be finite and non-negative")


def mixed_fourier_tail_norm_sq_upper(
    envelope: KernelRegularityEnvelope,
    cutoff_N: int,
) -> float:
    """HS/operator-norm-square upper bound for T Q_N."""
    _validate_envelope(envelope)
    if cutoff_N < 1:
        raise ValueError("cutoff_N must be at least 1")
    return (
        4.0
        * envelope.a
        * envelope.a
        / (math.pi * math.pi * cutoff_N)
        * envelope.energy
    )


def mixed_fourier_tail_norm_upper(
    envelope: KernelRegularityEnvelope,
    cutoff_N: int,
) -> float:
    return math.sqrt(mixed_fourier_tail_norm_sq_upper(envelope, cutoff_N))


def mixed_fourier_tail_certificate(
    envelope: KernelRegularityEnvelope,
    cutoff_N: int,
) -> MixedFourierTailCertificate:
    sq = mixed_fourier_tail_norm_sq_upper(envelope, cutoff_N)
    return MixedFourierTailCertificate(
        cutoff_N=cutoff_N,
        norm_upper=math.sqrt(sq),
        norm_sq_upper=sq,
        regularity_energy=envelope.energy,
    )


def cutoff_for_mixed_norm(
    envelope: KernelRegularityEnvelope,
    target_epsilon: float,
) -> MixedFourierTailCertificate:
    """Construct N sufficient for ||P_N T Q_N|| <= target_epsilon."""
    _validate_envelope(envelope)
    if not math.isfinite(target_epsilon) or target_epsilon <= 0.0:
        raise ValueError("target_epsilon must be finite and positive")

    numerator = 4.0 * envelope.a * envelope.a * envelope.energy
    denominator = math.pi * math.pi * target_epsilon * target_epsilon
    cutoff = max(1, math.ceil(numerator / denominator))
    cert = mixed_fourier_tail_certificate(envelope, cutoff)
    while cert.norm_upper > target_epsilon:
        cutoff += 1
        cert = mixed_fourier_tail_certificate(envelope, cutoff)
    return cert


def common_cutoff(
    high_mode_cutoff: int,
    mixed_tail_cutoff: int,
) -> int:
    """One Fourier cutoff satisfying both high-coercivity and mixed-tail gates."""
    if high_mode_cutoff < 1 or mixed_tail_cutoff < 1:
        raise ValueError("cutoffs must be positive")
    return max(high_mode_cutoff, mixed_tail_cutoff)



def screw_kernel_regularity_envelope_from_even_g(
    a: float,
    g_l2_sq_0_2a: float,
    gprime_l2_sq_0_2a: float,
) -> KernelRegularityEnvelope:
    """Reduce the screw-kernel regularity constants to 1D g/g' integrals.

    For the even real screw kernel
        K(t,u)=g(t-u)-g(t)-g(-u)+g(0),
    one has
        E_boundary <= 4 * int_0^(2a) |g(v)|^2 dv
    and
        E_du <= 16*a * int_0^(2a) |g'(v)|^2 dv.

    The derivative estimate uses
        d_u K = -g'(t-u)-g'(u)
    for even g (so g' is odd), followed by |x+y|^2<=2|x|^2+2|y|^2.
    """
    if not math.isfinite(a) or a <= 0.0:
        raise ValueError("a must be finite and positive")
    for name, value in (
        ("g_l2_sq_0_2a", g_l2_sq_0_2a),
        ("gprime_l2_sq_0_2a", gprime_l2_sq_0_2a),
    ):
        if not math.isfinite(value) or value < 0.0:
            raise ValueError(f"{name} must be finite and non-negative")
    return KernelRegularityEnvelope(
        a=a,
        boundary_jump_l2_sq=4.0 * g_l2_sq_0_2a,
        du_l2_sq=16.0 * a * gprime_l2_sq_0_2a,
    )


def screw_mixed_tail_norm_upper_from_even_g(
    a: float,
    cutoff_N: int,
    g_l2_sq_0_2a: float,
    gprime_l2_sq_0_2a: float,
) -> float:
    """Direct mixed-tail bound in terms of the 1D screw-function norms."""
    envelope = screw_kernel_regularity_envelope_from_even_g(
        a, g_l2_sq_0_2a, gprime_l2_sq_0_2a
    )
    return mixed_fourier_tail_norm_upper(envelope, cutoff_N)

def mixed_tail_gate_map() -> dict[str, object]:
    return {
        "schema": "SOH_SCREW_G_MIXED_FOURIER_TAIL_V0_2",
        "bound": (
            "||P_N T Q_N|| <= 2*a/(pi*sqrt(N)) * "
            "sqrt(E_boundary/(2*a)+E_du)"
        ),
        "closed": [
            "generic one-integration-by-parts Fourier tail inequality",
            "Hilbert-Schmidt to operator-norm domination",
            "explicit N schedule for a requested mixed norm epsilon",
            "common-cutoff max rule with high-mode coercivity schedule",
        ],
        "open": [
            "rigorous boundary-jump L2 envelope for the actual zeta screw kernel",
            "rigorous u-derivative L2 envelope for the actual zeta screw kernel",
            "uniformization of those envelopes on a-cells",
            "rigorous 1D bounds for int_0^(2a)|g|^2 and int_0^(2a)|g'|^2 for the zeta screw function",
            "derivative-weighted mixed Weil-form estimate for D*G_a*D",
            "finite localized low Fourier block interval enclosure",
            "all-scale Schur continuation",
            "SOH-C005",
            "Riemann Hypothesis",
        ],
        "claim_boundary": "G_a operator tail only; not the C005 Weil-form mixed block",
        "proof_of_rh": False,
    }
