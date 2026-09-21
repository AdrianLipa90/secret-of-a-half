# SOH Suzuki × C005 Shared Arithmetic Bottleneck v0.1

Status: **STRUCTURAL CROSSWALK / CANDIDATE PROGRAM / RH OPEN**

## 1. Two operator routes, one quantitative core

The repository currently has two distinct operator routes.

Route A is the C005 positivity route:

\[
A_a\ge0\ \forall a
\quad\Longrightarrow\quad
Q_W\ge0
\quad\Longrightarrow\quad
\mathrm{RH}.
\]

Route B starts from Suzuki's unconditional finite-\(a\) characteristic
functions:

\[
W(a,\theta;\cdot)\text{ entire with only real zeros}
\]

and seeks a large-\(a\) limit/zero-attraction theorem tying those spectral
zeros to zeros of the xi-derived target.

These are not logically identical routes.  But Suzuki's own discussion after
Corollary 1.6 says that proving the conjectural limit is expected to require
control of the shift parameter

\[
\lambda<\lambda_a
\]

and detailed analysis of the arithmetic prime contribution to \(Q_W^a\).

That is precisely the quantitative region already being attacked by C005.

## 2. Existing C005 decomposition

For the Fourier low/high split,

\[
A_a=
\begin{pmatrix}
A_{LL}(a)&B(a)\\
B(a)^*&A_{HH}(a)
\end{pmatrix}.
\]

Yoshida/Suzuki high-mode coercivity supplies the external mechanism

\[
A_{HH}(a)\ge\nu I,\qquad \nu>0
\]

on bounded \(a\)-intervals after a sufficiently large Fourier cutoff.

The remaining finite Schur operator is

\[
S_a=A_{LL}(a)-B(a)A_{HH}(a)^{-1}B(a)^*.
\]

The existing Lean scalar terminus packages the coarser sufficient condition

\[
\mu\nu-\varepsilon^2\ge0.
\]

## 3. Why the same estimates matter for Suzuki W

Suzuki's deficiency eigenfunctions \(v_\pm(a,\cdot)\), used to define

\[
W(a,\theta;z),
\]

solve integral/operator equations built from the same localized Weil/screw
kernel.  Therefore quantitative control of the high-frequency inverse and the
finite low-mode Schur block can potentially serve two purposes:

1. exclude a zero crossing of the localized spectral floor \(\lambda_a\);
2. control the finite-\(a\) deficiency/eigenfunction data entering
   \(W(a,\theta;z)\) as \(a\to\infty\).

This is a structural programme, not a proved implication.

## 4. Shared all-scale target

A useful common package would provide, for every bounded interval
\(0<a\le a_0\):

\[
A_{HH}(a)\ge\nu(a_0)I,
\]

\[
\|B(a)\|\le\varepsilon(a_0,N),
\]

and a certified finite-dimensional inverse/resolvent bound for the Schur
operator away from its spectrum.

Then one can ask for a schedule \(N=N(a_0)\) with explicit constants as
\(a_0\to\infty\).

For Route A the objective is positivity/nondegeneracy.

For Route B the objective is stability of the deficiency vectors,
normalization, and zero attraction of \(W(a,\theta;\cdot)\).

## 5. Exact geometric output already unified

In Suzuki's spectral coordinate

\[
z=i(s-\tfrac12),
\]

the native PhaseNav defect is

\[
\mathcal C(s)=(\Im z)^2.
\]

The projective reciprocal--conjugation defect is exactly

\[
\Delta_{\rm RC}(\Omega(s))
=
\frac{4(\Im z)^2}{|s|^2|1-s|^2}.
\]

Thus either operator route, if completed independently, lands on the same
formally verified seam.

## 6. Pole-safe Route B

The Corollary 1.6 target

\[
z^2\xi(1/2-iz)/\xi'(1/2-iz)
\]

is meromorphic.  The repository therefore uses the pole-safe local formulation
recorded in

\`SOH_SUZUKI_COROLLARY_1_6_POLE_AUDIT_V0_1.md\`:

- local convergence on pole-free neighborhoods;
- holomorphic non-vanishing normalization;
- zero attraction near xi zeros.

The Lean endgame requires only the last consequence: real finite-\(a\)
spectral points converging to each target zero.

## 7. Concrete next implementation target

Instead of increasing finite Hermite basis size, freeze the Fourier-adapted
localized normalization and produce one quantitative object reusable by both
routes:

\[
\boxed{
\mathcal R_{N,a}(z)
=
\bigl(A_{HH}(a)-z\bigr)^{-1}
}
\]

on a declared pole-free spectral window, together with a certified norm bound
and low/high coupling estimate.

This would turn the already-known high-mode coercivity into resolvent control.
The finite Schur complement could then be used both for positivity and for
stability of the finite-\(a\) characteristic data.

No such all-scale resolvent certificate is claimed here.

\`proof_of_rh = false\`
