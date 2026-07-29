"""Executable auditor for the native PhaseNav theta-bridge construction.

The PhaseNav source file is authoritative for the construction profile.  This
module parses its 18 theta nodes and evaluates the corresponding 36-dimensional
weighted phase state.

Mathematical status
-------------------
The theta-Mellin detector converges to the completed Riemann xi function in the
continuous limit.  The native closure defect is exactly (Re(s)-1/2)^2.  The
statement that every non-trivial xi zero must satisfy native closure remains an
explicit conjectural bridge; this module does not promote it to a theorem.
"""

from __future__ import annotations

from dataclasses import dataclass
import cmath
import math
from pathlib import Path
import re
from typing import Iterable, Sequence

TAU = 2.0 * math.pi
_HALF = 0.5
_EQUATION_RE = re.compile(r"^Μ\(([^)]+)\)\s*=\s*(.+)$")
_NODE_RE = re.compile(r"^(N\d{2}):\s*(.+)$")


@dataclass(frozen=True)
class ThetaNode:
    """One quadrature node and weight in u = log(x)."""

    identifier: str
    u: float
    q: float


@dataclass(frozen=True)
class Rotor:
    """A weighted PhaseNav rotor: positive gain and phase on S^1."""

    gain: float
    phase: float

    @property
    def value(self) -> complex:
        return self.gain * cmath.exp(1j * self.phase)

    def conjugate(self) -> "Rotor":
        return Rotor(self.gain, (-self.phase) % TAU)


@dataclass(frozen=True)
class NativePhaseState:
    """36D state arranged as 18 interleaved complementary rotor pairs."""

    s: complex
    nodes: tuple[ThetaNode, ...]
    rotors: tuple[Rotor, ...]

    def __post_init__(self) -> None:
        if len(self.nodes) * 2 != len(self.rotors):
            raise ValueError("state must contain exactly two rotors per theta node")

    @property
    def phase_vector(self) -> tuple[float, ...]:
        return tuple(rotor.phase for rotor in self.rotors)

    @property
    def gain_vector(self) -> tuple[float, ...]:
        return tuple(rotor.gain for rotor in self.rotors)

    @property
    def complex_vector(self) -> tuple[complex, ...]:
        return tuple(rotor.value for rotor in self.rotors)

    def pair(self, index: int) -> tuple[Rotor, Rotor]:
        return self.rotors[2 * index], self.rotors[2 * index + 1]


@dataclass(frozen=True)
class PhaseNavProgram:
    """Parsed executable subset of the native .pnv source."""

    path: Path
    equations: dict[str, str]
    nodes: tuple[ThetaNode, ...]

    @property
    def vector_dim(self) -> int:
        return int(float(self.equations["VECTOR_DIM"]))

    @property
    def pair_count(self) -> int:
        return int(float(self.equations["PAIR_COUNT"]))

    @classmethod
    def load(cls, path: str | Path) -> "PhaseNavProgram":
        source_path = Path(path)
        equations: dict[str, str] = {}
        nodes: list[ThetaNode] = []

        for raw_line in source_path.read_text(encoding="utf-8").splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#") or line.startswith("───"):
                continue

            equation_match = _EQUATION_RE.match(line)
            if equation_match:
                equations[equation_match.group(1).strip()] = equation_match.group(2).strip()
                continue

            node_match = _NODE_RE.match(line)
            if node_match:
                identifier, payload = node_match.groups()
                fields: dict[str, str] = {}
                for part in payload.split(","):
                    if "=" in part:
                        key, value = part.split("=", 1)
                        fields[key.strip()] = value.strip()
                if "u" in fields and "q" in fields:
                    nodes.append(ThetaNode(identifier, float(fields["u"]), float(fields["q"])))

        program = cls(source_path, equations, tuple(nodes))
        program.validate()
        return program

    def validate(self) -> None:
        required = {
            "PROGRAM",
            "VERSION",
            "VECTOR_DIM",
            "PAIR_COUNT",
            "KERNEL",
            "INVOLUTION",
            "DETECTOR",
            "CLOSURE",
        }
        missing = sorted(required.difference(self.equations))
        if missing:
            raise ValueError(f"missing PhaseNav equations: {', '.join(missing)}")
        if self.vector_dim != 36:
            raise ValueError("this construction requires PhaseNav VECTOR_DIM = 36")
        if self.pair_count != 18 or len(self.nodes) != 18:
            raise ValueError("this construction requires 18 complementary theta pairs")
        if self.vector_dim != 2 * self.pair_count:
            raise ValueError("VECTOR_DIM must equal 2 * PAIR_COUNT")
        if any(node.u <= 0.0 or node.q <= 0.0 for node in self.nodes):
            raise ValueError("theta nodes and quadrature weights must be positive")


def default_program_path() -> Path:
    """Return the project-relative native PhaseNav source path."""
    return (
        Path(__file__).resolve().parents[2]
        / "construction"
        / "phasenav"
        / "secret_of_half_theta_bridge.pnv"
    )


def theta_tail(u: float, *, tolerance: float = 1e-17, max_terms: int = 64) -> float:
    """Return psi(exp(u)) = sum_{n>=1} exp(-pi*n^2*exp(u))."""
    if u < 0.0:
        raise ValueError("the theta-Mellin construction uses u >= 0")
    x = math.exp(u)
    total = 0.0
    for n in range(1, max_terms + 1):
        term = math.exp(-math.pi * n * n * x)
        total += term
        if term < tolerance:
            break
    return total


def base_gain(node: ThetaNode) -> float:
    """Canonical self-dual theta gain at one quadrature node."""
    return node.q * theta_tail(node.u) * math.exp(node.u / 4.0)


def phase_state(s: complex, program: PhaseNavProgram) -> NativePhaseState:
    """Evaluate the 36D complementary theta state for a complex parameter s."""
    delta = float(s.real - _HALF)
    t = float(s.imag)
    rotors: list[Rotor] = []

    for node in program.nodes:
        seed = base_gain(node)
        half_u = node.u / 2.0
        plus_gain = seed * math.exp(+delta * half_u)
        minus_gain = seed * math.exp(-delta * half_u)
        plus_phase = (+t * half_u) % TAU
        minus_phase = (-t * half_u) % TAU
        rotors.extend((Rotor(plus_gain, plus_phase), Rotor(minus_gain, minus_phase)))

    return NativePhaseState(complex(s), program.nodes, tuple(rotors))


def zeta_involution(s: complex) -> complex:
    """Critical-strip involution J(s) = 1 - conjugate(s)."""
    return 1.0 - complex(s).conjugate()


def swap_conjugate(state: NativePhaseState) -> tuple[complex, ...]:
    """Apply the PhaseNav representation of J: conjugate and swap every pair."""
    transformed: list[complex] = []
    for index in range(len(state.nodes)):
        plus, minus = state.pair(index)
        transformed.extend((minus.value.conjugate(), plus.value.conjugate()))
    return tuple(transformed)


def covariance_residual(s: complex, program: PhaseNavProgram) -> float:
    """Max norm residual of P(Js) = X conjugate(P(s))."""
    direct = phase_state(zeta_involution(s), program).complex_vector
    transformed = swap_conjugate(phase_state(s, program))
    return max(abs(a - b) for a, b in zip(direct, transformed, strict=True))


def closure_defect(state: NativePhaseState) -> float:
    """Return the normalized radial closure defect.

    For the exact construction this equals (Re(s)-1/2)^2.  It is calculated
    from the .pnv gains rather than from s, so the identity is independently
    testable.
    """
    numerator = 0.0
    denominator = 0.0
    for index, node in enumerate(state.nodes):
        plus, minus = state.pair(index)
        log_ratio = math.log(plus.gain / minus.gain)
        numerator += log_ratio * log_ratio
        denominator += node.u * node.u
    if denominator == 0.0:
        raise ZeroDivisionError("degenerate theta-node basis")
    return numerator / denominator


def native_closed(state: NativePhaseState, *, tolerance: float = 1e-24) -> bool:
    """Whether the state closes in the canonical self-dual PhaseNav shell."""
    return closure_defect(state) <= tolerance


def theta_detector(state: NativePhaseState) -> complex:
    """Evaluate the 18-pair theta-Mellin detector approximating xi(s)."""
    integral_sum = sum(state.complex_vector)
    s = state.s
    return _HALF + _HALF * s * (s - 1.0) * integral_sum


def phase_berry_connection(left: NativePhaseState, right: NativePhaseState) -> float:
    """PhaseNav 36D Berry-connection proxy, ignoring radial gains by design."""
    if len(left.rotors) != len(right.rotors):
        raise ValueError("state dimensions do not match")
    return sum(
        math.sin(b.phase - a.phase) for a, b in zip(left.rotors, right.rotors, strict=True)
    ) / len(left.rotors)


def trajectory_holonomy(states: Sequence[NativePhaseState]) -> float:
    """Accumulate the PhaseNav Berry proxy along a state trajectory."""
    if len(states) < 2:
        return 0.0
    return sum(phase_berry_connection(a, b) for a, b in zip(states, states[1:]))


def scan_points(points: Iterable[complex], program: PhaseNavProgram) -> list[dict[str, float]]:
    """Evaluate detector, closure and covariance diagnostics for several points."""
    rows: list[dict[str, float]] = []
    for s in points:
        state = phase_state(s, program)
        detector = theta_detector(state)
        rows.append(
            {
                "sigma": float(s.real),
                "t": float(s.imag),
                "detector_re": float(detector.real),
                "detector_im": float(detector.imag),
                "detector_abs": float(abs(detector)),
                "closure_defect": float(closure_defect(state)),
                "covariance_residual": float(covariance_residual(s, program)),
            }
        )
    return rows
