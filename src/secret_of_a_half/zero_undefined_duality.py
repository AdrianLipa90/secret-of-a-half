"""Zero--undefined reciprocal duality for the Secret of a Half project.

The authoritative source is
``construction/phasenav/secret_of_half_zero_undefined_duality.pnv``.

The construction uses two *labels* as simplex vertices:
``DEFINED_ZERO`` and ``UNDEFINED_BOTTOM``.  IEEE NaN is never treated as a
number, an ordered endpoint, or a value that can enter ordinary arithmetic.
It may only be recognized as an implementation marker and mapped to the
abstract undefined label before the mathematical construction is applied.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
from pathlib import Path
import re
from typing import Iterable

_EQUATION_RE = re.compile(r"^Μ\(([^)]+)\)\s*=\s*(.+)$")

DEFINED_ZERO = "DEFINED_ZERO"
UNDEFINED_BOTTOM = "UNDEFINED_BOTTOM"


@dataclass(frozen=True)
class ZeroUndefinedProgram:
    """Parsed native PhaseNav profile."""

    path: Path
    equations: dict[str, str]

    @classmethod
    def load(cls, path: str | Path) -> "ZeroUndefinedProgram":
        source_path = Path(path)
        equations: dict[str, str] = {}
        for raw_line in source_path.read_text(encoding="utf-8").splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#") or line.startswith("───"):
                continue
            match = _EQUATION_RE.match(line)
            if match:
                equations[match.group(1).strip()] = match.group(2).strip()
        program = cls(source_path, equations)
        program.validate()
        return program

    def validate(self) -> None:
        required = {
            "PROGRAM",
            "VERSION",
            "BASE_HEAD",
            "STATE_SPACE",
            "LEFT_VERTEX",
            "RIGHT_VERTEX",
            "IMPLEMENTATION_MARKER",
            "PROJECTIVE_COORDINATE",
            "RECIPROCAL_MAP",
            "STATUS",
            "CONJUGACY",
            "SELF_DUAL_WEIGHT",
            "FISHER_RAO_MIDPOINT",
            "NAN_BOUNDARY",
            "NO_PROMOTION",
        }
        missing = sorted(required.difference(self.equations))
        if missing:
            raise ValueError(f"missing PhaseNav equations: {', '.join(missing)}")
        if self.equations["LEFT_VERTEX"] != DEFINED_ZERO:
            raise ValueError("left vertex must be DEFINED_ZERO")
        if self.equations["RIGHT_VERTEX"] != UNDEFINED_BOTTOM:
            raise ValueError("right vertex must be UNDEFINED_BOTTOM")
        if "NAN" not in self.equations["IMPLEMENTATION_MARKER"]:
            raise ValueError("the NaN implementation boundary must be explicit")


def default_program_path() -> Path:
    return (
        Path(__file__).resolve().parents[2]
        / "construction"
        / "phasenav"
        / "secret_of_half_zero_undefined_duality.pnv"
    )


def _validate_probability(p: float) -> float:
    value = float(p)
    if math.isnan(value):
        raise ValueError("NaN is an implementation marker, not a probability")
    if not 0.0 <= value <= 1.0:
        raise ValueError("p must lie in [0, 1]")
    return value


def classify_implementation_value(value: object) -> str:
    """Map an implementation token to a labelled vertex without arithmetic.

    Numeric zero is mapped to ``DEFINED_ZERO``.  IEEE NaN is mapped to
    ``UNDEFINED_BOTTOM``.  Other objects are not silently classified.
    """

    if isinstance(value, float) and math.isnan(value):
        return UNDEFINED_BOTTOM
    if isinstance(value, (int, float)) and not isinstance(value, bool) and value == 0:
        return DEFINED_ZERO
    raise ValueError("value is neither the defined-zero marker nor an IEEE NaN marker")


def complement(p: float) -> float:
    """Return the label-weight complement 1-p."""

    value = _validate_probability(p)
    return 1.0 - value


def projective_odds(p: float) -> float:
    """Return p/(1-p) on the extended non-negative line."""

    value = _validate_probability(p)
    if value == 1.0:
        return math.inf
    return value / (1.0 - value)


def inverse_odds(z: float) -> float:
    """Return z/(1+z) for z in the extended non-negative line."""

    value = float(z)
    if math.isnan(value) or value < 0.0:
        raise ValueError("odds coordinate must be non-negative and not NaN")
    if math.isinf(value):
        return 1.0
    return value / (1.0 + value)


def reciprocal(z: float) -> float:
    """Return reciprocal duality with 0 and +infinity exchanged."""

    value = float(z)
    if math.isnan(value) or value < 0.0:
        raise ValueError("reciprocal coordinate must be non-negative and not NaN")
    if value == 0.0:
        return math.inf
    if math.isinf(value):
        return 0.0
    return 1.0 / value


def amplitude_state(p: float) -> tuple[float, float]:
    """Hellinger/spinor embedding (sqrt(1-p), sqrt(p))."""

    value = _validate_probability(p)
    return math.sqrt(1.0 - value), math.sqrt(value)


def fisher_rao_coordinate(p: float) -> float:
    """Return theta=2 asin(sqrt(p)), the Bernoulli Fisher--Rao coordinate."""

    value = _validate_probability(p)
    return 2.0 * math.asin(math.sqrt(value))


def fisher_rao_distance(left: float, right: float) -> float:
    """Geodesic distance in the one-dimensional Bernoulli Fisher metric."""

    return abs(fisher_rao_coordinate(right) - fisher_rao_coordinate(left))


def binary_entropy(p: float) -> float:
    """Binary Shannon entropy in nats, continuously extended at endpoints."""

    value = _validate_probability(p)
    if value in (0.0, 1.0):
        return 0.0
    return -value * math.log(value) - (1.0 - value) * math.log(1.0 - value)


def conjugacy_residual(p: float) -> float:
    """Residual of odds(1-p)=1/odds(p), including endpoints."""

    left = projective_odds(complement(p))
    right = reciprocal(projective_odds(p))
    if math.isinf(left) and math.isinf(right):
        return 0.0
    return abs(left - right) / (1.0 + abs(left) + abs(right))


def self_dual_probability() -> float:
    """Unique fixed point of complement on [0,1]."""

    return 0.5


def run_duality_audit(
    program: ZeroUndefinedProgram,
    *,
    grid: Iterable[float] | None = None,
) -> dict[str, object]:
    """Run exact-identity regressions and return a deterministic receipt."""

    samples = tuple(grid) if grid is not None else (
        0.0,
        0.01,
        0.1,
        0.25,
        0.5,
        0.75,
        0.9,
        0.99,
        1.0,
    )
    residuals = [conjugacy_residual(p) for p in samples]
    half = self_dual_probability()
    state = amplitude_state(half)
    midpoint_left = fisher_rao_distance(0.0, half)
    midpoint_right = fisher_rao_distance(half, 1.0)

    return {
        "program": program.equations["PROGRAM"],
        "version": program.equations["VERSION"],
        "base_head": program.equations["BASE_HEAD"],
        "status": program.equations["STATUS"],
        "vertices": [DEFINED_ZERO, UNDEFINED_BOTTOM],
        "ieee_nan_is_numeric_endpoint": False,
        "ieee_nan_marker_maps_to": classify_implementation_value(float("nan")),
        "zero_marker_maps_to": classify_implementation_value(0.0),
        "projective_endpoints": {
            "p_0": projective_odds(0.0),
            "p_1": "INFINITY" if math.isinf(projective_odds(1.0)) else projective_odds(1.0),
        },
        "max_conjugacy_residual": max(residuals),
        "self_dual": {
            "p": half,
            "odds": projective_odds(half),
            "amplitude_state": list(state),
            "swap_residual": abs(state[0] - state[1]),
        },
        "fisher_rao": {
            "distance_0_to_half": midpoint_left,
            "distance_half_to_1": midpoint_right,
            "midpoint_residual": abs(midpoint_left - midpoint_right),
            "total_distance": fisher_rao_distance(0.0, 1.0),
        },
        "entropy": {
            "at_half": binary_entropy(half),
            "ln_2": math.log(2.0),
            "residual": abs(binary_entropy(half) - math.log(2.0)),
        },
        "claim_boundary": {
            "exact_geometry": True,
            "undefined_zero_ontology": "EXPLORATORY",
            "proof_of_rh": False,
        },
    }
