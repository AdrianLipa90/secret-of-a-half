#!/usr/bin/env python3
"""Generate deterministic v0.7 identity/holonomy monograph figures."""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from secret_of_a_half.identity_holonomy_solver import route_residuals

plt.rcParams["pdf.fonttype"] = 42
plt.rcParams["ps.fonttype"] = 42

ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT / "monograph" / "figures"
FIG.mkdir(parents=True, exist_ok=True)


def route_residual_arrays(sigma: np.ndarray) -> dict[str, np.ndarray]:
    """Vectorized form of the four scalar balance residuals used by the solver.

    This is plotting/runtime support only.  The scalar solver remains the canonical
    logical implementation; the vectorized expressions are regression-checked at
    representative points before figures are emitted.
    """
    s = np.asarray(sigma, dtype=float)
    if np.any((s <= 0.0) | (s >= 1.0)):
        raise ValueError("sigma values must lie in (0,1)")
    ln2 = np.log(2.0)
    entropy = -(s * np.log(s) + (1.0 - s) * np.log(1.0 - s))
    cancellation = np.abs(np.sqrt(s) - np.sqrt(1.0 - s)) ** 2
    berry = np.abs(np.exp(-2j * np.pi * (1.0 - s)) + 1.0) ** 2
    return {
        "complement": (2.0 * s - 1.0) ** 2,
        "entropy": ln2 - entropy,
        "cancellation": cancellation,
        "berry_minus_one": berry,
    }


def _validate_vectorization() -> None:
    for value in (0.125, 0.333, 0.5, 0.777, 0.875):
        scalar = route_residuals(value)
        vector = route_residual_arrays(np.asarray([value]))
        for key, expected in scalar.items():
            observed = float(vector[key][0])
            if not np.isclose(observed, expected, rtol=1e-12, atol=1e-14):
                raise RuntimeError(
                    f"vectorized residual mismatch for {key} at sigma={value}: "
                    f"{observed} != {expected}"
                )


def half_axis_routes() -> None:
    sigma = np.linspace(0.02, 0.98, 801)
    series = route_residual_arrays(sigma)
    fig, ax = plt.subplots(figsize=(8.0, 4.8))
    for key, values in series.items():
        ax.plot(sigma, values, label=key.replace("_", " "))
    ax.axvline(0.5, linewidth=1.0, linestyle="--")
    ax.set_xlabel(r"binary coordinate $\sigma$")
    ax.set_ylabel("non-negative residual")
    ax.set_title("Four independent balance residuals share the half axis")
    ax.set_ylim(bottom=0.0)
    ax.legend(loc="upper center", ncol=2, fontsize=8)
    fig.tight_layout()
    fig.savefig(FIG / "identity_half_routes.pdf")
    plt.close(fig)


def cycle_hierarchy() -> None:
    labels = ["half-turn units", "projective cycles", "spinor cycles", "information cycles"]
    counts = [24, 12, 6, 1]
    fig, ax = plt.subplots(figsize=(7.2, 4.5))
    ax.bar(labels, counts)
    ax.set_ylabel("count within declared information cycle")
    ax.set_title("Normalized cycle hierarchy before angular representation")
    ax.tick_params(axis="x", rotation=18)
    for i, value in enumerate(counts):
        ax.text(i, value, str(value), ha="center", va="bottom")
    fig.tight_layout()
    fig.savefig(FIG / "cycle_hierarchy_24_12_6.pdf")
    plt.close(fig)


def relation_graph() -> None:
    nodes = {
        "Sigma=1/2": (0.0, 0.0),
        "entropy ln2": (-2.2, 1.2),
        "Bloch equator": (0.0, 1.5),
        "Berry -1": (2.2, 1.2),
        "cancellation": (2.4, -0.8),
        "centered zeta axis": (-2.4, -0.8),
        "q in R/Z": (-0.8, -2.0),
        "spinor double cover": (1.5, -2.0),
        "canonical zero state": (0.0, -3.2),
        "RH (open)": (0.0, -4.4),
    }
    edges = [
        ("Sigma=1/2", "entropy ln2", "exact"),
        ("Sigma=1/2", "Bloch equator", "standard"),
        ("Bloch equator", "Berry -1", "holonomy"),
        ("Sigma=1/2", "cancellation", "exact + half-turn"),
        ("centered zeta axis", "Sigma=1/2", "fixed-axis crosswalk"),
        ("q in R/Z", "spinor double cover", "double cover"),
        ("canonical zero state", "Sigma=1/2", "OPEN bridge"),
        ("canonical zero state", "RH (open)", "OPEN"),
    ]
    fig, ax = plt.subplots(figsize=(8.0, 7.0))
    for source, target, label in edges:
        x1, y1 = nodes[source]
        x2, y2 = nodes[target]
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1), arrowprops={"arrowstyle": "->"})
        ax.text((x1+x2)/2, (y1+y2)/2, label, fontsize=7, ha="center", va="center")
    for label, (x, y) in nodes.items():
        ax.scatter([x], [y], s=90)
        ax.text(x, y + 0.16, label, ha="center", va="bottom", fontsize=8)
    ax.set_title("Typed relation graph: pair does not imply holonomy")
    ax.set_xlim(-3.2, 3.2)
    ax.set_ylim(-4.8, 2.0)
    ax.set_aspect("equal", adjustable="box")
    ax.axis("off")
    fig.tight_layout()
    fig.savefig(FIG / "typed_identity_relation_graph.pdf")
    plt.close(fig)


def main() -> None:
    _validate_vectorization()
    half_axis_routes()
    cycle_hierarchy()
    relation_graph()
    print(FIG)


if __name__ == "__main__":
    main()
