"""Executor and auditor for the native PhaseNav-Weil positivity probe.

The authoritative execution profile is
``construction/phasenav/secret_of_half_weil_operator.pnv``.

Mathematical status
-------------------
For an involution-fixed finite zero fixture, the matrix implemented here
reduces algebraically to a positive-semidefinite Gram matrix. The synthetic
off-axis fixture is a falsification/sensitivity experiment. It is not evidence
that the full arithmetic Weil form is positive and it is not a proof of the
Riemann Hypothesis.
"""

from __future__ import annotations

from dataclasses import dataclass
import cmath
import math
from pathlib import Path
import re
from typing import Iterable

_EQUATION_RE = re.compile(r"^Μ\(([^)]+)\)\s*=\s*(.+)$")
_ZERO_RE = re.compile(r"^Z(\d{2}):\s*gamma=(.+)$")


@dataclass(frozen=True)
class Hermitian2:
    """Two-by-two Hermitian matrix represented by its independent entries."""

    a: float
    b: complex
    d: float

    def eigenvalues(self) -> tuple[float, float]:
        midpoint = 0.5 * (self.a + self.d)
        radius = math.sqrt((0.5 * (self.a - self.d)) ** 2 + abs(self.b) ** 2)
        return midpoint - radius, midpoint + radius


@dataclass(frozen=True)
class WeilProbeProgram:
    """Parsed executable subset of the native PhaseNav source."""

    path: Path
    equations: dict[str, str]
    ordinates: tuple[float, ...]

    @classmethod
    def load(cls, path: str | Path) -> "WeilProbeProgram":
        source_path = Path(path)
        equations: dict[str, str] = {}
        ordinates: list[float] = []

        for raw_line in source_path.read_text(encoding="utf-8").splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#") or line.startswith("───"):
                continue

            equation_match = _EQUATION_RE.match(line)
            if equation_match:
                equations[equation_match.group(1).strip()] = equation_match.group(2).strip()
                continue

            zero_match = _ZERO_RE.match(line)
            if zero_match:
                ordinates.append(float(zero_match.group(2)))

        program = cls(source_path, equations, tuple(ordinates))
        program.validate()
        return program

    def validate(self) -> None:
        required = {
            "PROGRAM",
            "VERSION",
            "CHANNEL_COUNT",
            "ZERO_ORDINATE_COUNT",
            "TARGET_ORDINATE",
            "SYNTHETIC_DELTA",
            "GAUSSIAN_WIDTH",
            "CONTROL_TOLERANCE",
            "WITNESS_THRESHOLD",
            "INVOLUTION",
            "OPERATOR",
            "STATUS",
        }
        missing = sorted(required.difference(self.equations))
        if missing:
            raise ValueError(f"missing PhaseNav equations: {', '.join(missing)}")

        if self.channel_count != 2:
            raise ValueError("the v0.1 witness requires exactly two channels")
        if len(self.ordinates) != self.zero_ordinate_count:
            raise ValueError("ZERO_ORDINATE_COUNT does not match the native fixture")
        if not self.ordinates or any(gamma <= 0.0 for gamma in self.ordinates):
            raise ValueError("all control ordinates must be positive")
        if tuple(sorted(self.ordinates)) != self.ordinates:
            raise ValueError("control ordinates must be strictly ordered")
        if abs(self.target_ordinate - self.ordinates[0]) > 1e-14:
            raise ValueError("TARGET_ORDINATE must equal the first control ordinate")
        if self.synthetic_delta <= 0.0 or self.gaussian_width <= 0.0:
            raise ValueError("delta and Gaussian width must be positive")
        if self.control_tolerance <= 0.0:
            raise ValueError("CONTROL_TOLERANCE must be positive")
        if self.witness_threshold >= 0.0:
            raise ValueError("WITNESS_THRESHOLD must be negative")

    @property
    def channel_count(self) -> int:
        return int(float(self.equations["CHANNEL_COUNT"]))

    @property
    def zero_ordinate_count(self) -> int:
        return int(float(self.equations["ZERO_ORDINATE_COUNT"]))

    @property
    def target_ordinate(self) -> float:
        return float(self.equations["TARGET_ORDINATE"])

    @property
    def synthetic_delta(self) -> float:
        return float(self.equations["SYNTHETIC_DELTA"])

    @property
    def gaussian_width(self) -> float:
        return float(self.equations["GAUSSIAN_WIDTH"])

    @property
    def control_tolerance(self) -> float:
        return float(self.equations["CONTROL_TOLERANCE"])

    @property
    def witness_threshold(self) -> float:
        return float(self.equations["WITNESS_THRESHOLD"])

    @property
    def half_separation(self) -> float:
        return math.pi / self.target_ordinate


def default_program_path() -> Path:
    return (
        Path(__file__).resolve().parents[2]
        / "construction"
        / "phasenav"
        / "secret_of_half_weil_operator.pnv"
    )


def centered_involution(z: complex) -> complex:
    """Return J_z(z) = -conjugate(z)."""
    return -complex(z).conjugate()


def gaussian_channel_transform(
    z: complex,
    *,
    center: float,
    width: float,
    target_ordinate: float,
) -> complex:
    """Centered Laplace transform of one modulated Gaussian test channel."""
    shifted = complex(z) - 1j * target_ordinate
    return cmath.exp(center * shifted + 0.5 * width * width * shifted * shifted)


def feature_vector(z: complex, program: WeilProbeProgram) -> tuple[complex, complex]:
    """Return the two complementary PhaseNav channel responses at z."""
    return (
        gaussian_channel_transform(
            z,
            center=-program.half_separation,
            width=program.gaussian_width,
            target_ordinate=program.target_ordinate,
        ),
        gaussian_channel_transform(
            z,
            center=+program.half_separation,
            width=program.gaussian_width,
            target_ordinate=program.target_ordinate,
        ),
    )


def finite_weil_matrix(
    centered_zeros: Iterable[complex],
    program: WeilProbeProgram,
) -> Hermitian2:
    """Evaluate the finite involution-coupled PhaseNav-Weil matrix."""
    raw = [[0j, 0j], [0j, 0j]]

    for z in centered_zeros:
        direct = feature_vector(z, program)
        complement = feature_vector(centered_involution(z), program)
        for i in range(2):
            for j in range(2):
                raw[i][j] += complement[i].conjugate() * direct[j]

    # An involution-closed fixture is Hermitian analytically. Projecting the
    # off-diagonal pair removes only floating-point antisymmetry.
    return Hermitian2(
        a=raw[0][0].real,
        b=0.5 * (raw[0][1] + raw[1][0].conjugate()),
        d=raw[1][1].real,
    )


def on_axis_fixture(program: WeilProbeProgram) -> tuple[complex, ...]:
    """Return conjugate pairs z = +/- i gamma from the native control profile."""
    return tuple(z for gamma in program.ordinates for z in (1j * gamma, -1j * gamma))


def synthetic_off_axis_fixture(program: WeilProbeProgram) -> tuple[complex, ...]:
    """Replace the first on-axis pair by the declared symmetric off-axis quartet."""
    gamma0 = program.target_ordinate
    delta = program.synthetic_delta
    background = [
        z
        for gamma in program.ordinates[1:]
        for z in (1j * gamma, -1j * gamma)
    ]
    quartet = (
        +delta + 1j * gamma0,
        -delta + 1j * gamma0,
        +delta - 1j * gamma0,
        -delta - 1j * gamma0,
    )
    return tuple(background) + quartet


def run_probe(program: WeilProbeProgram) -> dict[str, object]:
    """Run the control and synthetic witness fixtures."""
    control_matrix = finite_weil_matrix(on_axis_fixture(program), program)
    synthetic_matrix = finite_weil_matrix(synthetic_off_axis_fixture(program), program)
    control_eigenvalues = control_matrix.eigenvalues()
    synthetic_eigenvalues = synthetic_matrix.eigenvalues()

    return {
        "program": program.equations["PROGRAM"],
        "version": program.equations["VERSION"],
        "status": program.equations["STATUS"],
        "target_ordinate": program.target_ordinate,
        "synthetic_delta": program.synthetic_delta,
        "gaussian_width": program.gaussian_width,
        "on_axis_control": {
            "lambda_min": control_eigenvalues[0],
            "lambda_max": control_eigenvalues[1],
            "pass": control_eigenvalues[0] >= -program.control_tolerance,
        },
        "synthetic_off_axis": {
            "lambda_min": synthetic_eigenvalues[0],
            "lambda_max": synthetic_eigenvalues[1],
            "pass": synthetic_eigenvalues[0] < program.witness_threshold,
        },
    }
