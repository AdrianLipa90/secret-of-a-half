"""Secret of a Half mathematical and PhaseNav construction package."""

from .core import binary_entropy, complementary_amplitude, involution
from .zero_undefined_duality import (
    DEFINED_ZERO,
    UNDEFINED_BOTTOM,
    ZeroUndefinedProgram,
    complement as label_complement,
    fisher_rao_coordinate,
    projective_odds,
    reciprocal,
    run_duality_audit,
)
from .phasenav_weil_prime_tail import (
    PrimeTailProgram,
    entry_tail_bound,
    operator_norm_tail_bound,
    run_prime_tail_certificate,
)
from .phasenav_weil_adaptive_cutoff import (
    AdaptiveCutoffProgram,
    adaptive_cutoff,
    adaptive_log_cutoff,
    run_adaptive_cutoff_audit,
)
from .phasenav_theta_bridge import (
    NativePhaseState,
    PhaseNavProgram,
    Rotor,
    ThetaNode,
    closure_defect,
    covariance_residual,
    native_closed,
    phase_state,
    theta_detector,
    zeta_involution,
)

__all__ = [
    "AdaptiveCutoffProgram",
    "NativePhaseState",
    "PhaseNavProgram",
    "PrimeTailProgram",
    "Rotor",
    "ThetaNode",
    "adaptive_cutoff",
    "adaptive_log_cutoff",
    "binary_entropy",
    "closure_defect",
    "complementary_amplitude",
    "covariance_residual",
    "entry_tail_bound",
    "involution",
    "native_closed",
    "operator_norm_tail_bound",
    "phase_state",
    "run_adaptive_cutoff_audit",
    "run_prime_tail_certificate",
    "theta_detector",
    "zeta_involution",
    "DEFINED_ZERO",
    "UNDEFINED_BOTTOM",
    "ZeroUndefinedProgram",
    "label_complement",
    "fisher_rao_coordinate",
    "projective_odds",
    "reciprocal",
    "run_duality_audit",
]
