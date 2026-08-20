#!/usr/bin/env python3
"""Generate deterministic explanatory figures for the Secret of a Half monograph.

The figures visualize exact coordinate maps, proof dependencies, and proved
analytic envelopes. They do not promote numerical evidence to theorem status.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "monograph" / "figures"
OUT.mkdir(parents=True, exist_ok=True)


def save(fig: plt.Figure, name: str) -> None:
    fig.tight_layout()
    fig.savefig(OUT / name, dpi=220, bbox_inches="tight")
    plt.close(fig)


def projective_map() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.4))
    ax, bx = axes
    t = np.linspace(-4.0, 4.0, 900)
    for sigma in np.linspace(0.08, 0.92, 8):
        s = sigma + 1j * t
        u = s / (1.0 - s)
        ax.plot(np.full_like(t, sigma), t, linewidth=0.8)
        bx.plot(u.real, u.imag, linewidth=0.8)
    for tau in np.linspace(-3.5, 3.5, 8):
        sigma = np.linspace(0.02, 0.98, 700)
        s = sigma + 1j * tau
        u = s / (1.0 - s)
        ax.plot(sigma, np.full_like(sigma, tau), linewidth=0.7, alpha=0.65)
        bx.plot(u.real, u.imag, linewidth=0.7, alpha=0.65)
    ax.axvline(0.5, linewidth=2.2, label=r"$\Re s=1/2$")
    theta = np.linspace(0, 2 * np.pi, 800)
    bx.plot(np.cos(theta), np.sin(theta), linewidth=2.2, label=r"$|\Omega|=1$")
    ax.set(xlim=(0, 1), ylim=(-4, 4), xlabel=r"$\sigma$", ylabel=r"$t$", title=r"Critical strip in $s=\sigma+it$")
    bx.set(xlim=(-3.2, 3.2), ylim=(-3.2, 3.2), xlabel=r"$\Re\,\Omega$", ylabel=r"$\Im\,\Omega$", title=r"Projective image $\Omega=s/(1-s)$")
    ax.legend(loc="upper right")
    bx.legend(loc="upper right")
    bx.set_aspect("equal", adjustable="box")
    save(fig, "projective_conformal_map.png")


def square_quotient_map() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.4))
    ax, bx = axes
    y = np.linspace(-3.0, 3.0, 850)
    for x in np.linspace(-0.5, 0.5, 9):
        z = x + 1j * y
        w = z * z
        ax.plot(np.full_like(y, x), y, linewidth=0.8)
        bx.plot(w.real, w.imag, linewidth=0.8)
    for yy in np.linspace(-2.8, 2.8, 8):
        x = np.linspace(-0.5, 0.5, 500)
        z = x + 1j * yy
        w = z * z
        ax.plot(x, np.full_like(x, yy), linewidth=0.7, alpha=0.65)
        bx.plot(w.real, w.imag, linewidth=0.7, alpha=0.65)
    ax.axvline(0.0, linewidth=2.2, label=r"critical line: $\Re z=0$")
    rr = np.linspace(0.0, 9.0, 500)
    bx.plot(-rr, np.zeros_like(rr), linewidth=2.2, label=r"image: $w\leq 0$")
    ax.set(xlim=(-0.55, 0.55), ylim=(-3.1, 3.1), xlabel=r"$\Re z$", ylabel=r"$\Im z$", title=r"Centered strip, $z=s-1/2$")
    bx.set(xlim=(-9.2, 1.0), ylim=(-3.3, 3.3), xlabel=r"$\Re w$", ylabel=r"$\Im w$", title=r"Square quotient $w=z^2$")
    ax.legend(loc="upper right")
    bx.legend(loc="upper left")
    save(fig, "square_quotient_map.png")


def dependency_graph() -> None:
    fig, ax = plt.subplots(figsize=(10.5, 6.2))
    ax.axis("off")
    nodes = {
        "xi": (0.08, 0.82, r"$\xi(1/2+z)$"),
        "quot": (0.33, 0.82, "$F(z^2)$\nG001--G003"),
        "kernel": (0.08, 0.55, "Riemann kernel $K$\nG004"),
        "pf": (0.58, 0.82, "PF$_2$ / PF$_3$\nG005--G023"),
        "corr": (0.33, 0.55, "$C,D_y,H_y$\nG024"),
        "m12": (0.58, 0.55, "$m=1,2$ CM\nPROVED"),
        "m3": (0.82, 0.55, "$m\\geq3$ CM\nOPEN"),
        "fourier": (0.58, 0.28, "$\\widehat D_y>0$\nOPEN"),
        "rh": (0.82, 0.28, "RH\nOPEN"),
        "weil": (0.08, 0.28, "Weil positivity\nC005 OPEN"),
    }
    for _, (x, y, text) in nodes.items():
        ax.text(x, y, text, ha="center", va="center", transform=ax.transAxes,
                bbox=dict(boxstyle="round,pad=0.45", fc="white", ec="black", lw=1.1))
    edges = [
        ("xi", "quot"), ("quot", "pf"), ("xi", "kernel"), ("kernel", "corr"),
        ("corr", "m12"), ("m12", "m3"), ("m3", "fourier"),
        ("fourier", "rh"), ("weil", "rh"), ("quot", "rh")
    ]
    for a, b in edges:
        xa, ya, _ = nodes[a]
        xb, yb, _ = nodes[b]
        ax.annotate("", xy=(xb, yb), xytext=(xa, ya), xycoords=ax.transAxes,
                    arrowprops=dict(arrowstyle="->", lw=1.2, shrinkA=35, shrinkB=35))
    ax.set_title("Proof dependency and open-frontier map", pad=16)
    save(fig, "proof_dependency_graph.png")


def bridge_moment_envelope() -> None:
    ns = np.arange(0, 13)
    bounds = []
    for n in ns:
        odd_double_fact = 1
        for k in range(1, 2 * n + 2, 2):
            odd_double_fact *= k
        bounds.append(odd_double_fact / (34.0 ** n))
    bounds = np.asarray(bounds)
    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    ax.semilogy(ns, bounds, marker="o")
    ax.set_xlabel(r"moment index $n$")
    ax.set_ylabel(r"bound on $\mathrm{E}[r^{2n}]$")
    ax.set_title(r"G024 bridge-moment envelope: $(2n+1)!!/34^n$")
    ax.grid(True, which="both", alpha=0.25)
    save(fig, "bridge_moment_envelope.png")


def g024_regions() -> None:
    fig, ax = plt.subplots(figsize=(9.2, 3.1))
    ax.set_ylim(0, 1)
    ax.set_xlim(0, 1.05)
    ax.set_yticks([])
    ax.axvspan(0, 1 / 9, alpha=0.24)
    ax.axvspan(1 / 9, 1.0, alpha=0.12)
    ax.axvline(1 / 9, linewidth=1.5)
    ax.text(0.055, 0.68, "former compact core\nclosed by Q/R", ha="center", va="center")
    ax.text(0.56, 0.68, r"analytic second-order region $q\geq1/9$", ha="center", va="center")
    ax.text(0.50, 0.28, r"$H_y'<0$ and $H_y''>0$ globally", ha="center", va="center", fontsize=11)
    ax.text(0.50, 0.08, r"$-H_y'''\geq0$ and all $m\geq3$: OPEN", ha="center", va="center", fontsize=10)
    ax.set_xlabel(r"radial-square coordinate $q$")
    ax.set_title("G024 complete-monotonicity status by region")
    save(fig, "g024_proof_regions.png")


def curvature_certificate_regions() -> None:
    fig, ax = plt.subplots(figsize=(9.0, 3.0))
    ax.set_xlim(0, 1.5)
    ax.set_ylim(0, 1)
    ax.set_yticks([])
    ax.axvspan(0, 0.4, alpha=0.25)
    ax.axvspan(0.4, 1.5, alpha=0.12)
    ax.axvline(0.4, linewidth=1.5)
    ax.text(0.2, 0.58, "outward interval certificate\n" + r"$0\leq t\leq2/5$", ha="center", va="center")
    ax.text(0.92, 0.58, "analytic theta-tail proof\n" + r"$t\geq2/5$", ha="center", va="center")
    ax.text(0.75, 0.18, r"global target: $20L''-L''''>0$", ha="center", va="center")
    ax.set_xlabel(r"kernel coordinate $t$")
    ax.set_title("Trust boundary of SOH-G024-Q")
    save(fig, "g024_curvature_certificate_regions.png")


def main() -> None:
    projective_map()
    square_quotient_map()
    dependency_graph()
    bridge_moment_envelope()
    g024_regions()
    curvature_certificate_regions()
    print(f"Generated 6 monograph figures in {OUT}")


if __name__ == "__main__":
    main()
