"""Fail-closed Yoshida/Suzuki Fourier-tail -> resolvent -> Schur pipeline.

This module only automates the quantitative plumbing that is already justified
by the explicit Fourier-tail estimate and elementary spectral inequalities.

It does NOT instantiate the missing repository-to-Suzuki normalization, does
NOT manufacture a high-mode coercivity constant, and does NOT prove SOH-C005
or RH.  Any coercivity value supplied to the resolvent/Schur functions must
come from an independently verified analytic theorem in the exact
normalization being audited.
"""
from __future__ import annotations

from dataclasses import dataclass
import math


@dataclass(frozen=True)
class FourierLeakageSchedule:
    a0: float
    t0: float
    tolerance: float
    cutoff: int
    coefficient: float
    certified_bound: float

    @property
    def pass_bound(self) -> bool:
        return self.certified_bound <= self.tolerance


@dataclass(frozen=True)
class ResolventCertificate:
    coercivity_floor: float
    spectral_parameter: float
    gap: float
    norm_upper_bound: float

    @property
    def admissible(self) -> bool:
        return self.gap > 0.0


@dataclass(frozen=True)
class ScalarSchurCertificate:
    mu: float
    epsilon: float
    nu: float
    determinant_margin: float

    @property
    def nonnegative(self) -> bool:
        return (
            self.mu >= 0.0
            and self.nu >= 0.0
            and self.determinant_margin >= 0.0
        )

    @property
    def strict(self) -> bool:
        return (
            self.mu > 0.0
            and self.nu > 0.0
            and self.determinant_margin > 0.0
        )


def fourier_tail_sum_upper(cutoff: int) -> float:
    """Return 2/(pi^2 N), bounding sum_{|n|>N} 1/(pi n)^2."""
    if cutoff < 1:
        raise ValueError("cutoff must be at least 1")
    return 2.0 / (math.pi * math.pi * cutoff)


def leakage_coefficient(a0: float, t0: float) -> float:
    """Return B(a0,t0) in the explicit Yoshida/Suzuki leakage bound.

    For 0 < a <= a0,
        leakage <= B(a0,t0) / N.
    """
    if a0 <= 0.0 or t0 <= 0.0:
        raise ValueError("a0 and t0 must be positive")
    return (
        8.0
        * a0
        / (math.pi * math.pi)
        * (t0 + a0 * t0 * t0 + (a0 * a0 * t0**3) / 3.0)
    )


def integrated_low_frequency_leakage_upper(
    a0: float,
    t0: float,
    cutoff: int,
) -> float:
    """Uniform upper bound for 0 < a <= a0."""
    if cutoff < 1:
        raise ValueError("cutoff must be at least 1")
    return leakage_coefficient(a0, t0) / cutoff


def cutoff_for_leakage(
    a0: float,
    t0: float,
    tolerance: float,
) -> FourierLeakageSchedule:
    """Smallest integer N from the explicit B/N schedule."""
    if tolerance <= 0.0:
        raise ValueError("tolerance must be positive")
    coefficient = leakage_coefficient(a0, t0)
    cutoff = max(1, math.ceil(coefficient / tolerance))
    bound = integrated_low_frequency_leakage_upper(a0, t0, cutoff)
    # Numerical rounding can put ceil(B/eta) one ulp below eta.  Tighten
    # fail-closed rather than silently accepting it.
    while bound > tolerance:
        cutoff += 1
        bound = integrated_low_frequency_leakage_upper(a0, t0, cutoff)
    return FourierLeakageSchedule(
        a0=a0,
        t0=t0,
        tolerance=tolerance,
        cutoff=cutoff,
        coefficient=coefficient,
        certified_bound=bound,
    )


def high_mode_resolvent_certificate(
    coercivity_floor: float,
    spectral_parameter: float,
) -> ResolventCertificate:
    """Elementary resolvent bound below a certified coercivity floor.

    If a self-adjoint high-mode block H satisfies H >= nu I and z < nu is
    real, then ||(H-zI)^(-1)|| <= 1/(nu-z).  This function performs only the
    scalar gap calculation; it does not prove H >= nu I.
    """
    if not math.isfinite(coercivity_floor) or not math.isfinite(spectral_parameter):
        raise ValueError("parameters must be finite")
    gap = coercivity_floor - spectral_parameter
    if gap <= 0.0:
        raise ValueError("spectral_parameter must be strictly below coercivity_floor")
    return ResolventCertificate(
        coercivity_floor=coercivity_floor,
        spectral_parameter=spectral_parameter,
        gap=gap,
        norm_upper_bound=1.0 / gap,
    )


def scalar_schur_certificate(
    mu: float,
    epsilon: float,
    nu: float,
) -> ScalarSchurCertificate:
    """Return the scalar Schur margin mu*nu-epsilon^2."""
    if not all(math.isfinite(x) for x in (mu, epsilon, nu)):
        raise ValueError("parameters must be finite")
    return ScalarSchurCertificate(
        mu=mu,
        epsilon=epsilon,
        nu=nu,
        determinant_margin=mu * nu - epsilon * epsilon,
    )


def low_block_effective_floor(
    mu: float,
    epsilon: float,
    nu: float,
) -> float:
    """Coarse Schur lower bound mu - epsilon^2/nu for nu>0."""
    if nu <= 0.0:
        raise ValueError("nu must be positive")
    if not all(math.isfinite(x) for x in (mu, epsilon, nu)):
        raise ValueError("parameters must be finite")
    return mu - (epsilon * epsilon) / nu



def scalar_block_lower_eigenvalue(
    mu: float,
    epsilon: float,
    nu: float,
) -> float:
    """Exact lower eigenvalue of [[mu,-epsilon],[-epsilon,nu]].

    A positive value is the quantitative no-Weyl-sequence gap for the scalar
    block model, stronger information than determinant positivity alone.
    """
    if not all(math.isfinite(x) for x in (mu, epsilon, nu)):
        raise ValueError("parameters must be finite")
    discriminant = math.hypot(mu - nu, 2.0 * epsilon)
    return 0.5 * (mu + nu - discriminant)


def strict_block_gap(
    mu: float,
    epsilon: float,
    nu: float,
) -> float:
    """Return the exact scalar coercivity gap, requiring strict positivity."""
    gap = scalar_block_lower_eigenvalue(mu, epsilon, nu)
    if gap <= 0.0:
        raise ValueError("block is not strictly positive")
    return gap

def pipeline_gate_map() -> dict[str, object]:
    """Return the explicit fail-closed proof-flow contract."""
    return {
        "schema": "SOH_C005_YOSHIDA_RESOLVENT_PIPELINE_V0_1",
        "flow": [
            "YOSHIDA_FOURIER_TAIL_BOUND",
            "EXACT_SOH_SUZUKI_FOURIER_SCALING",
            "LOCALIZED_FORM_DOMAIN_BOUNDARY_JOIN",
            "HIGH_MODE_COERCIVITY_NU",
            "HIGH_MODE_RESOLVENT_BOUND",
            "LOW_HIGH_COUPLING_EPSILON",
            "FINITE_LOW_BLOCK_MU",
            "STRICT_SCHUR_MARGIN",
            "UNIFORM_BLOCK_COERCIVITY_GAP",
            "NO_APPROXIMATE_NULL_SEQUENCE",
            "SPECTRAL_NONDEGENERACY_OR_SUZUKI_ZERO_ATTRACTION",
        ],
        "closed": [
            "explicit SOH<->Suzuki spectral/Fourier scaling",
            "explicit Fourier-tail B(a0,t0)/N schedule",
            "scalar resolvent gap formula below a supplied coercivity floor",
            "scalar Schur margin and effective low-block floor",
            "exact scalar 2x2 coercivity gap from the lower eigenvalue",
        ],
        "open": [
            "localized form equality with boundary/domain/Friedrichs-extension join",
            "certified high-mode coercivity constant nu in that normalization",
            "certified full low/high coupling epsilon",
            "uniform positive finite low-block floor mu",
            "uniform positive Schur/coercivity gap excluding approximate null sequences",
            "all-scale continuation a0 -> infinity",
            "SOH-C005",
            "Riemann Hypothesis",
        ],
        "proof_of_rh": False,
    }
