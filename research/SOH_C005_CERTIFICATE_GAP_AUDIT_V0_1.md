# SOH-C005 Certificate Gap Audit v0.1

Status: **VERIFIED CODE-SCOPE AUDIT**

Purpose: identify exactly which part of the block-positivity criterion is already certified by the current PhaseNav--Weil code and which parts remain mathematically absent.

## 1. Required block certificate

For a finite Hermite projection \(P_N\), the proof programme uses

\[
A_a=
\begin{pmatrix}
P_NA_aP_N & P_NA_a(I-P_N)\\
(I-P_N)A_aP_N & (I-P_N)A_a(I-P_N)
\end{pmatrix}.
\]

The sufficient certificate requires

\[
P_NA_aP_N\ge\mu_{N,a}P_N,
\]

\[
\|P_NA_a(I-P_N)\|\le\varepsilon_{N,a},
\]

and

\[
(I-P_N)A_a(I-P_N)\ge\nu_{N,a}(I-P_N),
\]

with

\[
\mu_{N,a}\ge0,\qquad
\nu_{N,a}\ge0,\qquad
\mu_{N,a}\nu_{N,a}\ge\varepsilon_{N,a}^2.
\]

## 2. What the existing prime-tail certificate proves

`src/secret_of_a_half/phasenav_weil_prime_tail_integrals.py` constructs entrywise majorants for the omitted prime-power tail in a finite Hermite section. Its `entry_bound_matrix(basis_size, ...)` is an \(N\times N\) matrix, and `operator_norm_tail_bound` returns the maximum row-sum norm of that same finite matrix.

Therefore this certificate controls a finite-block perturbation of

\[
P_NA_aP_N.
\]

It can contribute to a rigorous lower bound of the form

\[
\mu_{N,a}\ge
\lambda_{\min}(P_NA_{a,Q}P_N)-\delta_{N,a,Q},
\]

where \(\delta_{N,a,Q}\) is the certified omitted prime-tail norm.

It does **not** certify

\[
\|P_NA_a(I-P_N)\|
\]

and does **not** lower-bound

\[
(I-P_N)A_a(I-P_N).
\]

## 3. What the adaptive-cutoff certificate proves

`src/secret_of_a_half/phasenav_weil_adaptive_cutoff.py` constructs a basis-dependent prime cutoff

\[
\log Q_N=\max(\log Q_0,cN)
\]

and proves decay of the coarse finite-section prime-tail envelope for that schedule. The code itself records `global arithmetic positivity` among its OPEN claims.

Thus the adaptive schedule strengthens control of the finite projected block as \(N\) increases, but it does not close the infinite-dimensional projection complement.

## 4. Exact current allocation of proof obligations

### Already available or reducible from current code

- finite projected Hermite matrices;
- finite-block minimum eigenvalues;
- omitted prime-power entry bounds inside the finite block;
- finite-block operator-norm envelopes;
- adaptive cutoffs that drive those finite-block tail envelopes down;
- no spectral-zero input in the adaptive certificate.

These data can be assembled into a certified \(\mu_{N,a}\) once the localization parameter \(a\) is wired into the same exact normalization.

### Missing

#### C005-GAP-EPSILON

An unconditional bound

\[
\boxed{\|P_NA_a(I-P_N)\|\le\varepsilon_{N,a}}
\]

with explicit dependence on \(N\) and \(a\).

#### C005-GAP-NU

An unconditional lower bound

\[
\boxed{(I-P_N)A_a(I-P_N)\ge\nu_{N,a}(I-P_N)}
\]

with \(\nu_{N,a}\ge0\), or a compensated variant strong enough for the Schur/block positivity criterion.

#### C005-GAP-LOCALIZATION

A checked identity connecting the current Hermite arithmetic matrix construction to Suzuki's localized form \(Q_W^a\) with exactly the same normalization, boundary terms, and regularization.

## 5. Next implementation target

The next code must not merely increase `MAX_BASIS_SIZE`. It must estimate matrix elements with one or both indices **outside** the projected block.

A useful first target is the rectangular coupling tail

\[
E_{N,M}^{(a)}=
\left(\langle \psi_j,A_a\psi_k\rangle\right)_{
0\le j<N,\;N\le k<M},
\]

and a certified bound

\[
\|E_{N,M}^{(a)}\|\le\varepsilon_{N,M,a}.
\]

The second target is a lower bound for the high-index block

\[
H_{N,M}^{(a)}=
\left(\langle \psi_j,A_a\psi_k\rangle\right)_{N\le j,k<M}
\]

plus a certified tail beyond \(M\), sufficient to produce \(\nu_{N,a}\).

## 6. Verdict

The existing prime-tail and adaptive-cutoff programmes are not failed approaches; they solve the finite projected arithmetic-tail component needed for \(\mu_{N,a}\). The proof frontier is now located strictly at the projection boundary and high-index complement.

Current state:

\[
\boxed{\mu\text{-side: PARTIALLY CERTIFIED}}
\]

\[
\boxed{\varepsilon\text{-side: OPEN}}
\]

\[
\boxed{\nu\text{-side: OPEN}}
\]

\[
\boxed{\text{SOH-C005: OPEN}}
\]

\[
\boxed{\text{RH: OPEN}}
\]
