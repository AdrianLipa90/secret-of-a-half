# SOH-C005 Yoshida Fourier Rebase v0.1

Status: **PRIOR-ART REDUCTION / CANDIDATE REBASE / RH OPEN**

Purpose: replace the current Hermite-complement search by a projection adapted to an unconditional finite-codimension coercivity theorem already present in the Yoshida--Suzuki literature.

## 1. Why this rebase matters

The present C005 block programme uses a Hermite projection \(P_N\) and asks for

\[P_NA_aP_N\ge \mu_{N,a}P_N,\qquad \|P_NA_a(I-P_N)\|\le\varepsilon_{N,a},\]

and

\[(I-P_N)A_a(I-P_N)\ge\nu_{N,a}(I-P_N).\]

The difficult term has been the high-index complement lower bound \(\nu_{N,a}\). That difficulty is basis-dependent.

Yoshida introduced a Fourier-tail subspace \(K_N(a)\) by removing the modes \(|n|\le N\) on \([-a,a]\). Suzuki's 2023 exposition of Yoshida's Lemma 3 records the unconditional statement: for every fixed \(a_0>0\) and every \(\mu>0\), there exists \(N\) such that the Weil Hermitian form is bounded below by \(\mu\) on \(K_N(a)\), uniformly for \(0<a\le a_0\). Suzuki also proves a direct screw-function analogue in Theorem 4.3.

This is external prior art, not a new project theorem.

## 2. Fourier low/high split

Let

\[e_n^{(a)}(x)=(2a)^{-1/2}e^{\pi i n x/a}\]

and let \(P_{N,a}^{F}\) be the \(L^2(-a,a)\) projection onto modes \(|n|\le N\). Put \(Q_{N,a}^{F}=I-P_{N,a}^{F}\). On the periodic smooth test space used by Yoshida, \(K_N(a)=\operatorname{Ran}(Q_{N,a}^{F})\cap K(a)\).

After the exact normalization/domain crosswalk is checked, the desired replacement has the schematic form

\[\boxed{Q_{N,a}^{F}A_aQ_{N,a}^{F}\ge \mu\,Q_{N,a}^{F}}\]

for \(0<a\le a_0\), with \(N=N(a_0,\mu)\). The box is a crosswalk target, not yet promoted as an operator identity in this repository.

## 3. Consequence for C005

If the crosswalk is verified, the old OPEN high-complement problem becomes external coercivity on the Fourier-adapted split. The remaining obligations are the finite low block, low/high coupling, and the exact normalization/domain join.

Write schematically

\[A_a=\begin{pmatrix}A_{LL}&B\\B^\ast&A_{HH}\end{pmatrix}.\]

If \(A_{HH}\ge\nu I\) with \(\nu>0\), positivity reduces to the finite Schur target

\[\boxed{A_{LL}-BA_{HH}^{-1}B^\ast\ge0}.\]

A coarser sufficient certificate is the already-formalized scalar condition

\[\mu_{N,a}\nu_{N,a}-\varepsilon_{N,a}^2\ge0.\]

Thus SecretOfAHalfFormal/C005Block.lean is the correct algebraic terminus, but the projection should be reconsidered.

## 4. What this does not solve

The rebase does not prove RH. It does not yet provide the exact repository crosswalk, an explicit all-scale schedule \(N(a_0,\mu)\), the finite low-mode inequality for every \(a>0\), or the Schur/cross-term estimate for every \(a>0\).

## 5. Spectral-flow form

Suzuki's 2026 operator paper identifies the localized self-adjoint operator \(A_a\), proves it is the Friedrichs extension of a screw-function operator, records its discrete lower-bounded spectrum, and proves continuity of the lowest eigenvalue \(\lambda_a\). Since \(\lambda_a>0\) for sufficiently small \(a\), the remaining global target is

\[\boxed{\lambda_a\ge0\quad\forall a>0}.\]

The Fourier rebase is useful because the high-frequency sector already has an unconditional finite-codimension coercivity mechanism; any dangerous crossing is forced into a finite low-frequency sector at each bounded support scale.

## 6. Lean boundary

The current Lean branch proves only algebraic/geometric reductions: seam/critical-line equivalences, literal zero-to-seam equivalence to mathlib RH, a symmetry/entire-function no-go witness, scalar C005 block positivity, and the two-channel cancellation half no-go. It does not import Yoshida's theorem as an axiom.

## 7. References

- H. Yoshida, *On Hermitian forms attached to zeta functions*, Advanced Studies in Pure Mathematics 21 (1992), 281--325.
- M. Suzuki, *Aspects of the screw function corresponding to the Riemann zeta-function*, J. London Math. Soc. (2023), DOI 10.1112/jlms.12785.
- M. Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096, version dated 19 August 2026.

`proof_of_rh = false`
