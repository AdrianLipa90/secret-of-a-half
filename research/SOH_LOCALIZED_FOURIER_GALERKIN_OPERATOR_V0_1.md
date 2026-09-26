# SOH Localized Fourier Galerkin Operator v0.1

Status: **ACTUAL LOCALIZED ARITHMETIC GALERKIN MATRIX IMPLEMENTED / GLOBAL HERMITE SURROGATE NOT USED / INTERVAL SCHUR PROMOTION OPEN**

Date: 2026-09-26

Parents:
- research/SOH_SUZUKI_LOCALIZED_OPERATOR_JOIN_V0_1.md
- research/SOH_LOCALIZED_EXPONENTIAL_WEIL_CROSS_FORM_RANK_WITNESS_V0_1.md
- research/SOH_C005_FORM_LEVEL_SCHUR_REBASE_V0_1.md

No RH and no zeta-zero list are used.

## 1. Fourier basis

On the actual localized interval

\[
[-a,a],
\]

use Suzuki's normalized Fourier basis

\[
\boxed{
e_n^{(a)}(x)
=
\frac1{\sqrt{2a}}
e^{\pi i n x/a}.
}
\]

The exponential cross-form module uses

\[
v_z(x)=e^{-izx}\mathbf1_{[-a,a]}(x).
\]

Thus

\[
\boxed{
e_n^{(a)}
=
\frac1{\sqrt{2a}}
v_{-\pi n/a}.
}
\]

## 2. Exact matrix-element reduction

Therefore the localized Galerkin matrix is

\[
\boxed{
A_{nm}^{(N)}(a)
=
Q_W^a(e_n^{(a)},e_m^{(a)})
=
\frac1{2a}
Q_W^a
\left(
v_{-\pi n/a},
v_{-\pi m/a}
\right).
}
\]

The right side is evaluated directly by the source-faithful compactly
supported Weil functional.

This is the actual localized arithmetic form.

It is not the global dense-core Hermite matrix.

## 3. Implementation

The module is

src/secret_of_a_half/localized_weil_fourier_matrix.py.

It exposes:

- individual matrix entries;
- the full \(|n|\le N\) Galerkin matrix;
- the low/high partition
  \[
  A_{LL},\quad B,\quad A_{HH};
  \]
- Hermitian and parity residuals.

This matches the API requested in the earlier Suzuki-localization join note.

## 4. Prime-free regression at a=0.345

At

\[
a=0.345<\frac12\log2,
\]

the prime-power support is empty.

The \(N=1\) matrix is approximately

\[
\begin{pmatrix}
0.38794022&-0.23089457&0.23089457\\
-0.23089457&0.18218370&-0.23089457\\
0.23089457&-0.23089457&0.38794022
\end{pmatrix}.
\]

Its numerical eigenvalues are

\[
\boxed{
0.00771077,\quad
0.15704565,\quad
0.79330772.
}
\]

For larger truncations:

\[
N=2:
\quad
\lambda_{\min}\approx0.00316033,
\]

\[
N=3:
\quad
\lambda_{\min}\approx0.00216026.
\]

The observed full \(N=3\) spectrum is approximately

\[
\boxed{
0.00216026,\;
0.11759507,\;
0.67793805,\;
0.96394167,\;
1.22226293,\;
1.41507437,\;
1.64052584.
}
\]

## 5. Interpretation firewall

These positive finite spectra do **not** prove

\[
A_a\ge0.
\]

The smallest Galerkin eigenvalue decreases as \(N\) grows in this sample.

Therefore:
- no extrapolation to \(N=\infty\);
- no C005 promotion;
- no RH claim.

The result is implementation/provenance closure, not spectral-theorem closure.

## 6. What is now closed

The repository-specific gap

> implement an actual localized arithmetic Fourier matrix rather than reusing
> the global Hermite diagnostic

is now closed at high-precision numerical level.

The exact source object is

\[
Q_W^a(e_n,e_m).
\]

The old global-Hermite substitution remains forbidden.

## 7. Next proof-bearing upgrade

### LF-G1 — interval localized matrix

Replace high-precision quadrature by rigorous interval enclosures for selected
finite Fourier blocks.

### LF-G2 — interval low/high Schur feed

Pass certified

\[
A_{LL},\quad B,\quad A_{HH}
\]

into the existing interval Schur complement layer.

### LF-G3 — screw-kernel cross-check

Independently compute the same localized matrix elements from

\[
B_a=D^*G_aD
\]

using the source-normalized zeta screw kernel and verify equality with the
arithmetic Weil evaluator including all boundary/regularization terms.

Only after those gates may the localized numerical implementation be treated
as a rigorous C005 certificate.

## 8. Compact result

The localized Fourier matrix now has the executable definition

\[
\boxed{
A_{nm}(a)
=
\frac1{2a}
\operatorname{Weil}
\left[
v_{-\pi n/a}*
\widetilde v_{-\pi m/a}
\right].
}
\]

This supplies the actual localized Galerkin operator and its low/high blocks
without any zero list and without the global Hermite surrogate.
