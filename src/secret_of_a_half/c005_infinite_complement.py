"""Fail-closed schedules for extending prime-tail envelopes to growing Hermite windows.

This module does not prove infinite-complement positivity or RH.  It separates
an exact validity condition for the integral-test majorant from the still-open
question whether the resulting operator-norm envelopes converge as the window
grows.
"""
from __future__ import annotations

from dataclasses import dataclass
import math

from .phasenav_weil_prime_tail_program import monotone_log_threshold, monotonicity_margin


@dataclass(frozen=True)
class InfiniteWindowSchedule:
    """Adaptive prime cutoff certifying all entrywise bounds in a finite M-window."""

    window_stop: int
    gaussian_width: float
    safety_margin: float
    max_degree: int
    log_cutoff_threshold: float
    cutoff: int

    @property
    def proof_of_convergence(self) -> bool:
        return False

    @property
    def proof_of_rh(self) -> bool:
        return False


def cutoff_for_window(
    window_stop: int,
    gaussian_width: float,
    *,
    safety_margin: float = 1e-9,
) -> InfiniteWindowSchedule:
    """Return the minimal integer cutoff (up to rounding safety) valid through M-1.

    For Hermite orders 0,...,M-1, the largest degree entering the linearized
    product is d_max = 2(M-1).  The existing integral-test certificate is valid
    once log(Q) is above monotone_log_threshold(d_max, w).

    The returned schedule certifies applicability of the majorant only.  It does
    not assert that a growing-window norm bound tends to zero.
    """
    if window_stop < 1:
        raise ValueError("window_stop must be positive")
    if gaussian_width <= 0.0:
        raise ValueError("gaussian_width must be positive")
    if safety_margin <= 0.0:
        raise ValueError("safety_margin must be positive")

    max_degree = 2 * (window_stop - 1)
    threshold = monotone_log_threshold(max_degree, gaussian_width)
    raw = math.exp(threshold + safety_margin)
    cutoff = max(3, math.ceil(raw))
    while monotonicity_margin(max_degree, cutoff, gaussian_width) < 0.0:
        cutoff += 1

    return InfiniteWindowSchedule(
        window_stop=window_stop,
        gaussian_width=gaussian_width,
        safety_margin=safety_margin,
        max_degree=max_degree,
        log_cutoff_threshold=threshold,
        cutoff=cutoff,
    )


def schedule_receipt(
    max_window_stop: int,
    gaussian_width: float,
    *,
    safety_margin: float = 1e-9,
) -> dict[str, object]:
    """Build a deterministic validity receipt for M=1,...,max_window_stop."""
    if max_window_stop < 1:
        raise ValueError("max_window_stop must be positive")
    rows = []
    previous_cutoff = 0
    monotone_schedule = True
    all_valid = True
    for window_stop in range(1, max_window_stop + 1):
        item = cutoff_for_window(
            window_stop,
            gaussian_width,
            safety_margin=safety_margin,
        )
        margin = monotonicity_margin(item.max_degree, item.cutoff, gaussian_width)
        valid = margin >= 0.0
        all_valid &= valid
        monotone_schedule &= item.cutoff >= previous_cutoff
        previous_cutoff = item.cutoff
        rows.append(
            {
                "window_stop": item.window_stop,
                "max_degree": item.max_degree,
                "log_cutoff_threshold": item.log_cutoff_threshold,
                "cutoff": item.cutoff,
                "monotonicity_margin": margin,
                "valid": valid,
            }
        )
    return {
        "schema": "SOH_C005_INFINITE_WINDOW_CUTOFF_SCHEDULE_V0_2",
        "status": "PASS_VALIDITY_ONLY" if all_valid and monotone_schedule else "FAIL",
        "rows": rows,
        "all_integral_test_bounds_valid": all_valid,
        "cutoff_schedule_monotone": monotone_schedule,
        "claim_boundary": {
            "exact": [
                "d_max=2(M-1) for the M-window Hermite product degrees",
                "closed monotonicity threshold from the existing tail majorant",
                "adaptive Q_M makes every entrywise integral-test bound legal in each finite M-window",
            ],
            "open": [
                "uniform summability of the entrywise majorants as M tends to infinity",
                "vanishing infinite-complement coupling norm",
                "positive lower bound on the infinite high-index complement",
                "SOH-C005",
                "Riemann hypothesis",
            ],
            "proof_of_convergence": False,
            "proof_of_rh": False,
        },
    }
