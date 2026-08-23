#!/usr/bin/env python3
"""
SOH-HYB-006: corrected Jensen–HTRI finite verifier.

Purpose
-------
Independent finite-quadrature verifier for the exact continuous identity

    4 * Jhat_eta(2 x)
      = <Omega_eta | cos(x Sigma) | Omega_eta>

with
    Delta = T1 - T2
    Sigma = T1 + T2
    Omega_eta(t1,t2) ∝ Delta * exp(eta Delta/2) * sqrt(K(t1)K(t2)).

This script does NOT prove RH.  It checks the finite discretization and optionally
builds a Qiskit Hadamard-test circuit.

Native 18-positive-node / ± pairing:
    36 signed modes -> 6 qubits per copy
    2 copies + 1 ancilla = 13 logical qubits.

Qiskit is optional.  The NumPy reference runs without it.
"""

from __future__ import annotations

import argparse
import math
import numpy as np


def riemann_phi_positive(t: np.ndarray, nmax: int = 32) -> np.ndarray:
    """Classical positive half-line Xi kernel Phi(t), t >= 0."""
    t = np.asarray(t, dtype=np.float64)
    if np.any(t < 0):
        raise ValueError("riemann_phi_positive expects t >= 0")
    out = np.zeros_like(t)
    e2t = np.exp(2.0 * t)
    for n in range(1, nmax + 1):
        a = np.pi * n * n
        out += (
            4.0 * a
            * np.exp(2.5 * t)
            * (2.0 * a * e2t - 3.0)
            * np.exp(-a * e2t)
        )
    return out


def K_even(t: np.ndarray, nmax: int = 32) -> np.ndarray:
    """Even full-line kernel K(t) = Phi(|t|)/2."""
    return 0.5 * riemann_phi_positive(np.abs(np.asarray(t)), nmax=nmax)


def native_signed_nodes(n_pairs: int = 18, umax: float = 2.0):
    """
    Positive Gauss-Legendre nodes on [0,umax], reflected to ± nodes.

    This preserves the 18-pair / 36-mode bookkeeping of the native PhaseNav
    construction.  It is a finite verifier only; umax and quadrature order are
    not a global theorem.
    """
    z, q = np.polynomial.legendre.leggauss(n_pairs)
    up = 0.5 * (z + 1.0) * umax
    wp = 0.5 * umax * q

    t = np.concatenate([-up[::-1], up])
    w = np.concatenate([wp[::-1], wp])
    return t, w


def omega_fixture(x: float, eta: float, n_pairs: int = 18, umax: float = 2.0):
    t, w = native_signed_nodes(n_pairs=n_pairs, umax=umax)
    kval = K_even(t)

    amp1 = np.sqrt(np.maximum(kval * w, 0.0))
    t1, t2 = np.meshgrid(t, t, indexing="ij")
    delta = t1 - t2
    sigma = t1 + t2

    omega = (delta / math.sqrt(2.0)) * np.exp(0.5 * eta * delta)
    omega *= np.outer(amp1, amp1)

    norm2 = float(np.vdot(omega.ravel(), omega.ravel()).real)
    if not (norm2 > 0.0 and np.isfinite(norm2)):
        raise RuntimeError("degenerate/non-finite finite Omega state")

    omega_n = omega / math.sqrt(norm2)
    phase = np.exp(-1j * x * sigma)

    expectation = np.vdot(omega_n.ravel(), (phase * omega_n).ravel())
    return {
        "t": t,
        "w": w,
        "omega": omega_n,
        "sigma": sigma,
        "norm2_unnormalized": norm2,
        "unitary_expectation": expectation,
        "cos_expectation": float(expectation.real),
    }


def packed_state(omega: np.ndarray):
    """
    Pack a 36x36 state into two 6-qubit registers (64x64 basis).
    Unused basis states are exactly zero.
    """
    n = omega.shape[0]
    if omega.shape != (n, n):
        raise ValueError("omega must be square")
    bits = math.ceil(math.log2(n))
    dim_reg = 1 << bits
    vec = np.zeros(dim_reg * dim_reg, dtype=np.complex128)
    for i in range(n):
        for j in range(n):
            idx = i | (j << bits)
            vec[idx] = omega[i, j]
    vec /= np.linalg.norm(vec)
    return vec, bits, dim_reg


def packed_diagonal(x: float, t: np.ndarray, bits: int, dim_reg: int):
    phases = np.ones(dim_reg * dim_reg, dtype=np.complex128)
    for i in range(len(t)):
        for j in range(len(t)):
            idx = i | (j << bits)
            phases[idx] = np.exp(-1j * x * (t[i] + t[j]))
    return phases


def qiskit_hadamard_test(x: float, eta: float, shots: int = 20000):
    """
    Optional Qiskit circuit.  Returns a circuit plus ideal reference.

    Requires:
        qiskit
        qiskit-aer   (only if shot simulation is requested externally)
    """
    try:
        from qiskit import QuantumCircuit
        from qiskit.circuit.library import StatePreparation, DiagonalGate
    except Exception as exc:
        raise RuntimeError(
            "Qiskit is not installed. NumPy reference is still available."
        ) from exc

    fx = omega_fixture(x=x, eta=eta)
    vec, bits, dim_reg = packed_state(fx["omega"])
    phases = packed_diagonal(x, fx["t"], bits, dim_reg)

    n_data = 2 * bits
    anc = n_data
    qc = QuantumCircuit(n_data + 1, 1)

    qc.append(StatePreparation(vec), list(range(n_data)))
    qc.h(anc)

    U = DiagonalGate(phases)
    qc.append(U.control(1), [anc] + list(range(n_data)))

    qc.h(anc)
    qc.measure(anc, 0)

    return {
        "circuit": qc,
        "logical_qubits": n_data + 1,
        "data_qubits": n_data,
        "ancilla_qubits": 1,
        "ideal_real_expectation": fx["cos_expectation"],
        "shots_suggested": shots,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--x", type=float, default=14.134725)
    ap.add_argument("--eta", type=float, default=0.1)
    ap.add_argument("--n-pairs", type=int, default=18)
    ap.add_argument("--umax", type=float, default=2.0)
    ap.add_argument("--qiskit", action="store_true")
    args = ap.parse_args()

    fx = omega_fixture(
        x=args.x,
        eta=args.eta,
        n_pairs=args.n_pairs,
        umax=args.umax,
    )
    vec, bits, dim_reg = packed_state(fx["omega"])

    print("SOH-HYB-006 FINITE VERIFIER")
    print("status=FINITE_DIAGNOSTIC_NOT_PROOF")
    print(f"signed_modes={len(fx['t'])}")
    print(f"qubits_per_copy={bits}")
    print(f"data_qubits={2*bits}")
    print(f"hadamard_total_qubits={2*bits+1}")
    print(f"x={args.x:.12g}")
    print(f"eta={args.eta:.12g}")
    print(f"cos_expectation={fx['cos_expectation']:.17g}")
    print(f"imag_residual={fx['unitary_expectation'].imag:.3e}")
    print(f"packed_norm={np.linalg.norm(vec):.17g}")

    if args.qiskit:
        q = qiskit_hadamard_test(args.x, args.eta)
        print(q["circuit"])
        print(f"qiskit_ideal_reference={q['ideal_real_expectation']:.17g}")


if __name__ == "__main__":
    main()
