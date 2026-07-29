#!/usr/bin/env python3
"""Generate deterministic figures and numerical tables for the monograph."""
from __future__ import annotations

import csv
import math
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import mpmath as mp

# Embed TrueType outlines in PDF figures; avoid Type 3 fonts.
mpl.rcParams["pdf.fonttype"] = 42
mpl.rcParams["ps.fonttype"] = 42
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT / "monograph" / "figures"
DATA = ROOT / "data" / "processed"
FIG.mkdir(parents=True, exist_ok=True)
DATA.mkdir(parents=True, exist_ok=True)


def binary_entropy(p: np.ndarray) -> np.ndarray:
    return -p * np.log(p) - (1.0 - p) * np.log(1.0 - p)


def xi(s: complex | mp.mpc) -> mp.mpc:
    s = mp.mpc(s)
    return mp.mpf("0.5") * s * (s - 1) * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def save_entropy() -> None:
    p = np.linspace(1e-4, 1 - 1e-4, 1200)
    h = binary_entropy(p)
    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    ax.plot(p, h, linewidth=2.0)
    ax.axvline(0.5, linewidth=1.0, linestyle="--")
    ax.scatter([0.5], [math.log(2)], zorder=3)
    ax.annotate(r"$H(1/2)=\ln 2$", xy=(0.5, math.log(2)), xytext=(0.61, 0.61),
                arrowprops={"arrowstyle": "->"})
    ax.set_xlabel(r"binary weight $\sigma$")
    ax.set_ylabel(r"entropy $H(\sigma)$ (nats)")
    ax.set_title("Binary entropy and the unique balanced point")
    ax.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(FIG / "binary_entropy.pdf")
    fig.savefig(FIG / "binary_entropy.png", dpi=220)
    plt.close(fig)


def save_entropy_deficit() -> None:
    x = np.linspace(-0.499, 0.499, 1200)
    p = 0.5 + x
    deficit = math.log(2) - binary_entropy(p)
    quadratic = 2 * x**2
    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    ax.plot(x, deficit, label=r"$\ln2-H(1/2+x)$", linewidth=2.0)
    ax.plot(x, quadratic, linestyle="--", label=r"$2x^2$")
    ax.set_xlabel(r"displacement $x=\sigma-1/2$")
    ax.set_ylabel("information deficit (nats)")
    ax.set_title("Coercive cost of leaving the half-axis")
    ax.legend()
    ax.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(FIG / "entropy_deficit.pdf")
    fig.savefig(FIG / "entropy_deficit.png", dpi=220)
    plt.close(fig)


def save_cancellation_landscape() -> None:
    sigma = np.linspace(0.001, 0.999, 500)
    phase = np.linspace(0, 2 * np.pi, 500)
    S, P = np.meshgrid(sigma, phase)
    mag2 = 1 + 2 * np.sqrt(S * (1 - S)) * np.cos(P)
    fig, ax = plt.subplots(figsize=(7.4, 5.0))
    im = ax.pcolormesh(sigma, phase / np.pi, mag2, shading="auto")
    ax.scatter([0.5], [1.0], marker="x", s=80, linewidths=2.0)
    ax.set_xlabel(r"channel weight $\sigma$")
    ax.set_ylabel(r"relative phase $\phi/\pi$")
    ax.set_title(r"$|\sqrt{\sigma}+e^{i\phi}\sqrt{1-\sigma}|^2$")
    cbar = fig.colorbar(im, ax=ax)
    cbar.set_label("squared amplitude")
    fig.tight_layout()
    fig.savefig(FIG / "cancellation_landscape.pdf")
    fig.savefig(FIG / "cancellation_landscape.png", dpi=220)
    plt.close(fig)


def save_local_cancellation() -> None:
    x = np.linspace(-0.18, 0.18, 420)
    d = np.linspace(-0.8, 0.8, 420)
    X, D = np.meshgrid(x, d)
    S = 0.5 + X
    P = np.pi + D
    exact = 1 + 2 * np.sqrt(S * (1 - S)) * np.cos(P)
    quadratic = 2 * X**2 + 0.5 * D**2
    err = np.abs(exact - quadratic)
    fig, ax = plt.subplots(figsize=(7.4, 5.0))
    im = ax.pcolormesh(x, d, err, shading="auto")
    ax.set_xlabel(r"$x=\sigma-1/2$")
    ax.set_ylabel(r"$\delta=\phi-\pi$")
    ax.set_title("Error of the local quadratic cancellation model")
    cbar = fig.colorbar(im, ax=ax)
    cbar.set_label(r"$|\,|A|^2-(2x^2+\delta^2/2)\,|$")
    fig.tight_layout()
    fig.savefig(FIG / "cancellation_quadratic_error.pdf")
    fig.savefig(FIG / "cancellation_quadratic_error.png", dpi=220)
    plt.close(fig)


def save_involution_geometry() -> None:
    fig, ax = plt.subplots(figsize=(7.0, 5.2))
    ax.axvspan(0, 1, alpha=0.08)
    ax.axvline(0.5, linestyle="--", linewidth=1.5, label=r"$\Re s=1/2$")
    points = [(0.23, 7.0), (0.77, 7.0), (0.23, -7.0), (0.77, -7.0)]
    labels = [r"$\rho$", r"$1-\bar\rho$", r"$\bar\rho$", r"$1-\rho$"]
    for (x, y), label in zip(points, labels):
        ax.scatter([x], [y], s=55)
        ax.text(x + 0.025, y + 0.35, label)
    ax.annotate("", xy=(0.77, 7.0), xytext=(0.23, 7.0), arrowprops={"arrowstyle": "<->"})
    ax.annotate("", xy=(0.23, -7.0), xytext=(0.23, 7.0), arrowprops={"arrowstyle": "<->", "linestyle": ":"})
    ax.set_xlim(-0.08, 1.08)
    ax.set_ylim(-9.2, 9.2)
    ax.set_xlabel(r"$\Re s$")
    ax.set_ylabel(r"$\Im s$")
    ax.set_title("Zero orbit under conjugation and functional symmetry")
    ax.legend(loc="lower right")
    ax.grid(alpha=0.2)
    fig.tight_layout()
    fig.savefig(FIG / "involution_geometry.pdf")
    fig.savefig(FIG / "involution_geometry.png", dpi=220)
    plt.close(fig)


def save_bloch_geometry() -> None:
    fig = plt.figure(figsize=(7.0, 6.0))
    ax = fig.add_subplot(111, projection="3d")
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 60)
    X = np.outer(np.cos(u), np.sin(v))
    Y = np.outer(np.sin(u), np.sin(v))
    Z = np.outer(np.ones_like(u), np.cos(v))
    ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10, linewidth=0.35, alpha=0.35)
    ax.plot(np.cos(u), np.sin(u), np.zeros_like(u), linewidth=2.0)
    ax.scatter([1, -1], [0, 0], [0, 0], s=65)
    ax.text(1.08, 0, 0, r"$|+\rangle$")
    ax.text(-1.28, 0, 0, r"$|-\rangle$")
    ax.text(0, 0, 1.14, r"$|0\rangle$")
    ax.text(0, 0, -1.22, r"$|1\rangle$")
    ax.set_box_aspect((1, 1, 1))
    ax.set_axis_off()
    ax.set_title("Balanced states form the Bloch equator; exact cancellation selects one ray")
    fig.tight_layout()
    fig.savefig(FIG / "bloch_equator.pdf")
    fig.savefig(FIG / "bloch_equator.png", dpi=220)
    plt.close(fig)


def save_eta_prefactor() -> None:
    sigma = np.linspace(0.02, 1.15, 500)
    t = np.linspace(-30, 30, 700)
    S, T = np.meshgrid(sigma, t)
    pref = np.abs(1 - np.exp((1 - S - 1j * T) * math.log(2)))
    fig, ax = plt.subplots(figsize=(7.5, 5.2))
    im = ax.pcolormesh(sigma, t, np.log10(pref + 1e-6), shading="auto")
    ax.axvline(0.5, linestyle="--", linewidth=1.2, label=r"critical line $\sigma=1/2$")
    ax.axvline(1.0, linestyle=":", linewidth=1.2, label=r"prefactor-zero line $\sigma=1$")
    ax.set_xlabel(r"$\sigma=\Re s$")
    ax.set_ylabel(r"$t=\Im s$")
    ax.set_title(r"Binary eta prefactor: $\log_{10}|1-2^{1-s}|$")
    ax.legend(loc="upper right")
    cbar = fig.colorbar(im, ax=ax)
    cbar.set_label("logarithmic modulus")
    fig.tight_layout()
    fig.savefig(FIG / "eta_prefactor.pdf")
    fig.savefig(FIG / "eta_prefactor.png", dpi=220)
    plt.close(fig)


def save_xi_line_and_zeros() -> None:
    mp.mp.dps = 50
    ts = np.linspace(0, 50, 900)
    vals = np.array([float(mp.re(xi(mp.mpf("0.5") + 1j * mp.mpf(str(t))))) for t in ts])
    scale = np.max(np.abs(vals))
    vals_scaled = vals / scale if scale else vals
    zeros = [mp.zetazero(k) for k in range(1, 11)]
    fig, ax = plt.subplots(figsize=(7.6, 4.8))
    ax.plot(ts, vals_scaled, linewidth=1.5)
    ax.axhline(0, linewidth=0.8)
    for z in zeros:
        t0 = float(mp.im(z))
        if t0 <= 50:
            ax.axvline(t0, linewidth=0.6, alpha=0.5)
    ax.set_xlim(0, 50)
    ax.set_xlabel(r"$t$")
    ax.set_ylabel(r"scaled $\Xi(t)=\xi(1/2+it)$")
    ax.set_title("Completed zeta function along the critical line")
    ax.grid(alpha=0.22)
    fig.tight_layout()
    fig.savefig(FIG / "xi_critical_line.pdf")
    fig.savefig(FIG / "xi_critical_line.png", dpi=220)
    plt.close(fig)

    with (DATA / "first_20_zeta_zeros.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["index", "real_part", "imaginary_part", "abs_zeta", "abs_xi"])
        for k in range(1, 21):
            z = mp.zetazero(k)
            writer.writerow([k, mp.nstr(mp.re(z), 20), mp.nstr(mp.im(z), 30), mp.nstr(abs(mp.zeta(z)), 8), mp.nstr(abs(xi(z)), 8)])


def save_functional_equation_residuals() -> None:
    mp.mp.dps = 80
    points = [mp.mpc("0.23", "7.1"), mp.mpc("0.41", "14.2"), mp.mpc("0.77", "22.5"), mp.mpc("0.5", "33.0"), mp.mpc("1.3", "4.0")]
    with (DATA / "functional_equation_residuals.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["sigma", "t", "abs_xi_s_minus_xi_1_minus_s", "abs_xi_Js_minus_conj_xi_s"])
        for s in points:
            r1 = abs(xi(s) - xi(1 - s))
            J = 1 - mp.conj(s)
            r2 = abs(xi(J) - mp.conj(xi(s)))
            writer.writerow([mp.nstr(mp.re(s), 12), mp.nstr(mp.im(s), 12), mp.nstr(r1, 12), mp.nstr(r2, 12)])


def main() -> None:
    save_entropy()
    save_entropy_deficit()
    save_cancellation_landscape()
    save_local_cancellation()
    save_involution_geometry()
    save_bloch_geometry()
    save_eta_prefactor()
    save_xi_line_and_zeros()
    save_functional_equation_residuals()
    print(f"Generated figures in {FIG}")
    print(f"Generated data in {DATA}")


if __name__ == "__main__":
    main()
