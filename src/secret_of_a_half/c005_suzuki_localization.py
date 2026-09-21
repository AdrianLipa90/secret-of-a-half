"""Unitary coordinate crosswalk for Suzuki localization intervals.

Let y denote Suzuki's physical interval coordinate on (-a,a) and x the SOH
Fourier coordinate with y = 2*pi*x.  Define

    (U_a f)(x) = sqrt(2*pi) f(2*pi*x),

mapping L2(-a,a;dy) unitarily to
L2(-a/(2*pi), a/(2*pi);dx).

This module closes only the coordinate/domain Jacobian and Fourier-basis
normalization.  It does not by itself prove equality of the localized Weil
quadratic forms or identify the screw kernel operators.
"""
from __future__ import annotations

import cmath
import math


_TWO_PI = 2.0 * math.pi


def soh_halfwidth_from_suzuki_a(a: float) -> float:
    if not math.isfinite(a) or a <= 0.0:
        raise ValueError("a must be finite and positive")
    return a / _TWO_PI


def suzuki_y_from_soh_x(x: float) -> float:
    return _TWO_PI * float(x)


def soh_x_from_suzuki_y(y: float) -> float:
    return float(y) / _TWO_PI


def unitary_amplitude_factor() -> float:
    """sqrt(dy/dx) for y=2*pi*x."""
    return math.sqrt(_TWO_PI)


def suzuki_fourier_basis_value(n: int, a: float, y: float) -> complex:
    """e_n^(a)(y)=(2a)^(-1/2) exp(pi i n y/a)."""
    if a <= 0.0 or not math.isfinite(a):
        raise ValueError("a must be finite and positive")
    return (
        1.0 / math.sqrt(2.0 * a)
        * cmath.exp(math.pi * 1j * int(n) * float(y) / a)
    )


def soh_pulled_back_fourier_basis_value(n: int, a: float, x: float) -> complex:
    """U_a e_n^(a), in the SOH x-coordinate."""
    if a <= 0.0 or not math.isfinite(a):
        raise ValueError("a must be finite and positive")
    return (
        math.sqrt(math.pi / a)
        * cmath.exp(2.0 * math.pi * math.pi * 1j * int(n) * float(x) / a)
    )


def pullback_basis_via_definition(n: int, a: float, x: float) -> complex:
    return unitary_amplitude_factor() * suzuki_fourier_basis_value(
        n, a, suzuki_y_from_soh_x(x)
    )


def derivative_conjugation_factor() -> float:
    """U (d/dy) U^{-1} = (1/(2*pi)) d/dx."""
    return 1.0 / _TWO_PI


def zero_mean_integral_scale() -> float:
    """Integral_y f(y) dy = sqrt(2*pi) Integral_x (U f)(x) dx."""
    return math.sqrt(_TWO_PI)



def pulled_convolution_kernel_multiplier() -> float:
    """For (Gf)(y)=∫g(y-v)f(v)dv, U G U^-1 has kernel 2*pi*g(2*pi*(x-x'))."""
    return _TWO_PI


def pulled_convolution_kernel_argument(delta_x: float) -> float:
    """Argument of the original Suzuki kernel after y=2*pi*x."""
    return _TWO_PI * float(delta_x)


def raw_scaled_kernel_B_prefactor() -> float:
    """If G_raw uses kernel g(2*pi*(x-x')) without the 2*pi Jacobian,
    then U (D_y^* G D_y) U^-1 = (1/(2*pi)) D_x^* G_raw D_x.
    """
    return 1.0 / _TWO_PI


def pulled_full_kernel_B_derivative_prefactor() -> float:
    """If G_pull := U G U^-1 includes kernel 2*pi*g(2*pi*delta),
    then U B U^-1=(1/(2*pi)^2) D_x^* G_pull D_x.
    """
    return 1.0 / (_TWO_PI * _TWO_PI)

def localization_crosswalk_receipt() -> dict[str, object]:
    return {
        "schema": "SOH_SUZUKI_LOCALIZATION_UNITARY_CROSSWALK_V0_1",
        "coordinate": "y_suzuki = 2*pi*x_soh",
        "unitary_map": "(U f)(x)=sqrt(2*pi)*f(2*pi*x)",
        "support": "(-a,a)_Suzuki <-> (-a/(2*pi),a/(2*pi))_SOH",
        "basis": (
            "sqrt(pi/a)*exp(2*pi^2*i*n*x/a)"
        ),
        "derivative": "U*(d/dy)*U^-1=(1/(2*pi))*(d/dx)",
        "zero_mean": "preserved exactly (integrals differ by nonzero sqrt(2*pi))",
        "H0_1_boundary": "preserved by endpoint coordinate map",
        "closed": [
            "interval coordinate/Jacobian",
            "L2 unitary amplitude",
            "Fourier basis normalization and frequency scaling",
            "zero-mean equivalence",
            "derivative scaling",
            "Dirichlet endpoint correspondence",
            "generic convolution pullback G -> kernel 2*pi*g(2*pi*delta)",
            "D=i*d/dy scaling and induced D*G D prefactors",
        ],
        "open": [
            "instantiate the actual zeta screw kernel g in repository-native localized code",
            "quadratic-form equality Q_W^a=<D*G_aD ., .> against repository arithmetic formulas",
            "repository implementation of the localized operator",
            "uniform Schur gap",
            "SOH-C005",
            "Riemann Hypothesis",
        ],
        "proof_of_rh": False,
    }
