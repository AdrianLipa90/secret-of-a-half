"""Public API for the PhaseNav--Weil prime-tail certificate v0.5."""
from .phasenav_weil_prime_tail_program import (
    PrimeTailProgram, default_prime_tail_program_path, monotone_log_threshold,
    monotonicity_margin,
)
from .phasenav_weil_prime_tail_integrals import (
    entry_bound_matrix,
    entry_tail_bound,
    high_index_block_tail_bound,
    operator_norm_tail_bound,
    rectangular_entry_bound_matrix,
    rectangular_operator_norm_tail_bound,
    reciprocal_tail_integrand,
    tail_term_integral_gamma,
    tail_term_integral_log,
    tail_term_integral_reciprocal,
)
from .phasenav_weil_prime_tail_audit import prime_shell_entry, run_prime_tail_certificate

__all__ = [
    "PrimeTailProgram", "default_prime_tail_program_path",
    "monotone_log_threshold", "monotonicity_margin",
    "tail_term_integral_gamma", "tail_term_integral_log",
    "reciprocal_tail_integrand", "tail_term_integral_reciprocal",
    "entry_tail_bound", "entry_bound_matrix", "operator_norm_tail_bound",
    "rectangular_entry_bound_matrix", "rectangular_operator_norm_tail_bound",
    "high_index_block_tail_bound",
    "prime_shell_entry", "run_prime_tail_certificate",
]
