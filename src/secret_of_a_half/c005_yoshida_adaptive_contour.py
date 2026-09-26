"""Adaptive-contour Yoshida/Suzuki high-mode envelopes.

Source structure: Suzuki 2023, proof of Theorem 4.3, equations (4.4),
(4.11)-(4.13).  The source allows any contour parameter c>1.

For |t|,|u|<=a1 the explicit shifted kernel gives
    C2(a1,c) <= (exp(2*c*a1)-1)/(2*c*a1).

For Re(s)=1+c,
    |1/(s-1)+1/s| <= 1/c + 1/(1+c),
and
    |zeta'/zeta(s)|
      <= sum_{n>=2} log(n)/n^(1+c)
      <= log(2)/2^(1+c)
         + 2^(-c)*(log(2)/c + 1/c^2),
using monotonicity of log(x)/x^(1+c) for x>=2.

The module provides a log-domain sufficient-cutoff calculation and an adaptive
large-a schedule c=1+a^-2, a1=a+a^-2.  It does not claim the resulting cutoff
is minimal.
"""
from __future__ import annotations

from dataclasses import dataclass
import mpmath as mp


mp.mp.dps=max(mp.mp.dps,100)

_UPPER_GAMMA_COEFF=mp.sqrt(2)/6-mp.mpf(1)/8


@dataclass(frozen=True)
class GeneralContourEnvelope:
    a0: str
    a1: str
    c: str
    target_mu: str
    c_margin: str
    c1_upper: str
    c2_upper: str
    chosen_C: str
    log_t0: str
    C0_upper: str
    log_leakage_B: str
    log_required_continuous_cutoff: str


def _positive(x,name):
    y=mp.mpf(x)
    if not mp.isfinite(y) or y<=0:
        raise ValueError(f"{name} must be finite and positive")
    return y


def c1_upper_general(c):
    c=_positive(c,"c")
    if not c>1:
        raise ValueError("Suzuki contour parameter c must be > 1")
    rational=1/c+1/(1+c)
    log2=mp.log(2)
    zeta_series=(
        log2/mp.power(2,1+c)
        + mp.power(2,-c)*(log2/c+1/(c*c))
    )
    return max(rational,zeta_series)


def c2_upper_general(a1,c):
    a=_positive(a1,"a1")
    c=_positive(c,"c")
    if not c>1:
        raise ValueError("c must be > 1")
    x=2*c*a
    return mp.expm1(x)/x


def adaptive_parameters(a):
    a=_positive(a,"a")
    return 1+1/(a*a), a+1/(a*a)


def _log_gamma_window_data(C):
    # Existing conservative rule t0=2 sqrt(pi) exp(C+1).
    log_t0=mp.log(2*mp.sqrt(mp.pi))+C+1
    # C0 uses rmax=sqrt(1/16+t0^2/4), evaluated stably.
    log_rmax=(
        log_t0-mp.log(2)
        + mp.log1p(mp.mpf("0.25")*mp.e**(-2*log_t0))/2
    )
    C0=log_rmax+16*_UPPER_GAMMA_COEFF-mp.log(mp.pi)/2
    return log_t0,C0


def _log_leakage_B(a,log_t0):
    # B=(8a/pi^2)*(t+a t^2+a^2 t^3/3).
    return (
        mp.log(8*a/mp.pi**2)
        + 3*log_t0
        + mp.log(
            a*a/3
            + a*mp.e**(-log_t0)
            + mp.e**(-2*log_t0)
        )
    )


def general_contour_envelope(
    a0,
    a1,
    target_mu,
    c,
    *,
    C_margin=1,
):
    a=_positive(a0,"a0")
    a1m=_positive(a1,"a1")
    if not a1m>a:
        raise ValueError("a1 must exceed a0")
    mu=_positive(target_mu,"target_mu")
    margin=_positive(C_margin,"C_margin")
    cm=_positive(c,"c")
    if not cm>1:
        raise ValueError("c must exceed 1")

    c1=c1_upper_general(cm)
    c2=c2_upper_general(a1m,cm)
    p=c1*c2
    C=3*p+mp.pi*mu+margin

    log_t0,C0=_log_gamma_window_data(C)
    logB=_log_leakage_B(a,log_t0)

    denominator=C-2*p-mp.pi*mu
    if denominator<=0:
        raise RuntimeError("internal source margin must be positive")

    logN=mp.log(C+C0)+logB-mp.log(denominator)

    return GeneralContourEnvelope(
        a0=mp.nstr(a,50),
        a1=mp.nstr(a1m,50),
        c=mp.nstr(cm,50),
        target_mu=mp.nstr(mu,50),
        c_margin=mp.nstr(margin,50),
        c1_upper=mp.nstr(c1,50),
        c2_upper=mp.nstr(c2,50),
        chosen_C=mp.nstr(C,50),
        log_t0=mp.nstr(log_t0,50),
        C0_upper=mp.nstr(C0,50),
        log_leakage_B=mp.nstr(logB,50),
        log_required_continuous_cutoff=mp.nstr(logN,50),
    )


def adaptive_contour_envelope(a,target_mu=1,*,C_margin=1):
    c,a1=adaptive_parameters(a)
    return general_contour_envelope(
        a,a1,target_mu,c,C_margin=C_margin
    )


def adaptive_asymptotic_loglog(a):
    a=_positive(a,"a")
    return 2*a-mp.log(a)+mp.log(mp.mpf(27)/4)
