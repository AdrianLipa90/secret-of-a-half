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
    "NativePhaseState",
    "PhaseNavProgram",
    "Rotor",
    "ThetaNode",
    "binary_entropy",
    "closure_defect",
    "complementary_amplitude",
    "covariance_residual",
    "involution",
    "native_closed",
    "phase_state",
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
