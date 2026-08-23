# SOH-HYB-006/007 — Theta × HTRI Research Ledger

Date: 2026-08-21

Branch status: research only. No RH proof claim. No canonical promotion.

## Scope

This ledger records the current Theta × HTRI route derived from the exact Riemann theta kernel and the native PhaseNav complementary-channel construction.

## HYB-006 — corrected internal Jensen / QHTRI verifier

### Exact analytic objects

Let

- `Xi(w) = xi(1/2 + i w)`, `w = x + i eta`,
- `K(t) = Phi(|t|)/2`,
- `Delta = T1 - T2`,
- `Sigma = T1 + T2`.

Define the two-copy relative-mode state

`Omega_eta(t1,t2) ∝ (t1-t2) exp(eta (t1-t2)/2) sqrt(K(t1) K(t2))`.

The internal Jensen channel is

`J_eta(u) = integral r^2 cosh(2 eta r) K(u+r)K(u-r) dr`.

The finite verifier checks the discretized expectation

`4 Jhat_eta(2x) = <Omega_eta | cos(x Sigma) | Omega_eta>`.

### Evidential status

- internal `J_eta` channel: ACTIVE research route;
- finite NumPy verifier: IMPLEMENTED;
- Qiskit Hadamard-test construction: IMPLEMENTED, OPTIONAL;
- faithful native 18-pair / 36-signed-mode fixture: 13 logical qubits (12 data + 1 ancilla);
- Qiskit/finite computation is an independent verifier, not a premise of a proof;
- external `D_y` route: QUARANTINE_PENDING_SIGN_AUDIT; do not use as authority for promotion.

## HYB-007 — angular three-point Gram reduction

Normalize

`rho_eta(u) = J_eta(u)/J_eta(0)`

and define

`theta_eta(u) = arccos(rho_eta(u))`.

For the translation-invariant 3-point Gram matrix on points `{0,a,b}`,

`det G3 = 1 + 2 rho(a)rho(b)rho(|a-b|) - rho(a)^2 - rho(b)^2 - rho(|a-b|)^2`.

Writing

`alpha = theta(a)`, `beta = theta(b)`, `gamma = theta(|a-b|)`, `s=(alpha+beta+gamma)/2`,

the exact identity is

`det G3 = 4 sin(s) sin(s-alpha) sin(s-beta) sin(s-gamma)`.

Therefore monotonicity plus concavity of `theta_eta` on `R_+` is a sufficient condition for every 3-point translation-invariant Gram matrix to be positive semidefinite.

### Internal curvature inputs

The integrated G024 line proves the kernel bounds

- `L(t) = -log K(t)`,
- `L''(t) > 17` globally,
- `L''''(t) < 20 L''(t)` globally, with the declared computer-assisted compact certificate plus analytic tail.

For the corrected internal Jensen channel, the current derivation obtains the working bounds

- `q_eta'(u) > 34 u`, where `q_eta = -log rho_eta`,
- an internal moment hierarchy with effective denominator 33,
- `q_eta''(u) < C exp(2u)`, `C = 42 exp(1/3) (11/9)^(3/2)`.

The angular concavity condition can be written as

`theta_eta''(u) <= 0`

iff

`q_eta'(u)^2 >= (1-exp(-2 q_eta(u))) q_eta''(u)`.

A stronger sufficient inequality is `q_eta'(u)^2 >= q_eta''(u)`.

### Certified region

The accompanying outward interval endpoint receipt certifies the stronger sufficient inequality throughout

`2/5 <= u <= 2`, `|eta| < 1/2`.

Status:

- exact determinant / angular factorization: PROVED;
- analytic neighborhood of `u=0`: PROVED from the local expansion plus `L'''' < 20 L''` and `L'' > 17`;
- midrange `[2/5,2]`: PASS_INTERVAL_ENDPOINT_CERTIFICATE;
- compact remainder between the local neighborhood and `2/5`: OPEN;
- tail `u>2`: OPEN;
- global 3-point Gram positivity: OPEN;
- PF3/PF-infinity/RH: OPEN.

## Files

- `construction/phasenav/soh_hyb006_qiskit_verifier.py`
- `construction/phasenav/soh_hyb007_angle_pf3.py`
- `data/SOH_HYB007_ANGLE_MIDRANGE_RECEIPT_V1.json`

## Promotion firewall

The following implications are forbidden until separately proved:

`finite diagnostics -> global theorem`

`3-point Gram positivity -> PF3`

`PF3 -> PF-infinity`

`kernel-shape evidence -> RH`

Next target: `SOH-HYB-008`, consisting of a fail-closed compact-angle certificate and an analytic dominant-theta tail for global concavity of `theta_eta`.
