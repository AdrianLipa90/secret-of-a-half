"""Exact elementary identities used by the initial ansatz."""

from __future__ import annotations

import cmath
import math


def binary_entropy(sigma: float) -> float:
    """Return binary Shannon entropy in nats for 0 < sigma < 1."""
    if not 0.0 < sigma < 1.0:
        raise ValueError("sigma must lie strictly between 0 and 1")
    return -sigma * math.log(sigma) - (1.0 - sigma) * math.log(1.0 - sigma)


def complementary_amplitude(sigma: float, phase: float) -> complex:
    """Return sqrt(sigma) + exp(i phase) sqrt(1-sigma)."""
    if not 0.0 <= sigma <= 1.0:
        raise ValueError("sigma must lie in [0, 1]")
    return math.sqrt(sigma) + cmath.exp(1j * phase) * math.sqrt(1.0 - sigma)


def involution(s: complex) -> complex:
    """Return the critical-strip involution J(s) = 1 - conjugate(s)."""
    return 1.0 - s.conjugate()
