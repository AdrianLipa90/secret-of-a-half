# SOH C005 Form-Level Schur Rebase v0.1

Status: **ARCHITECTURAL SIMPLIFICATION / OPERATOR-DOMAIN BOTTLENECK REMOVED FROM C005 ROUTE / RH OPEN**

## 1. The key correction

The Fourier high-mode theorem of Yoshida/Suzuki is already a theorem about the
localized Weil/Hermitian **quadratic form**.  Therefore the C005 positivity
route does not need to pass through the unbounded operator \(B_a\), its
Friedrichs extension \(A_a\), or the operator domain before performing the
low/high split.

Those operator objects remain important for the Suzuki spectral-limit route,
but they are not logically required for the direct C005 form-positivity route.

This removes an unnecessary choke point from the pipeline.

## 2. Form-level split

Let

\[
\mathcal H=L_N\oplus H_N
\]

be the Fourier low/high decomposition of the localized test/form space and
write the Hermitian form schematically as

\[
q_a[\ell+h]
=
q_{LL,a}[\ell]
+
2\Re q_{LH,a}(\ell,h)
+
q_{HH,a}[h].
\]

The source high-mode theorem supplies, after the explicit constants already
developed in the repository,

\[
\boxed{
q_{HH,a}[h]\ge\nu\,\|h\|^2
}
\]

uniformly on each declared bounded \(a\)-interval.

Suppose independently that

\[
q_{LL,a}[\ell]\ge\mu\,\|\ell\|^2
\]

and

\[
|q_{LH,a}(\ell,h)|
\le
\varepsilon\,\|\ell\|\,\|h\|.
\]

Then

\[
q_a[\ell+h]
\ge
\mu\|\ell\|^2
-
2\varepsilon\|\ell\|\|h\|
+
\nu\|h\|^2.
\]

The already-formalized scalar C005 theorem therefore gives positivity whenever

\[
\boxed{
\mu\ge0,\qquad
\nu>0,\qquad
\mu\nu-\varepsilon^2\ge0.
}
\]

No unbounded-operator domain manipulation is needed for this implication.

## 3. What remains finite and what remains infinite

The infinite sector is now controlled by the source coercivity theorem.

The unresolved quantities are:

\[
\boxed{
\mu_{N,a}
=
\lambda_{\min}(q_{LL,a})
}
\]

and

\[
\boxed{
\varepsilon_{N,a}
=
\|q_{LH,a}\|.
}
\]

The low block is finite-dimensional.

The mixed block still has an infinite high index, but because the localized
screw kernel is continuous on a compact square, it is a compact/Hilbert--Schmidt
type object at the integral-kernel level.  A rigorous Fourier-coefficient or
kernel-tail estimate can therefore target \(\varepsilon\) directly.

This is a narrower problem than constructing the entire localized operator
\(A_a\).

## 4. Two different pipelines must now stay separate

### C005 direct form route

\[
\boxed{
\text{localized Weil form}
\to
\text{Fourier split}
\to
(\mu,\varepsilon,\nu)
\to
\text{scalar Schur gate}
\to
Q_W^a\ge0.
}
\]

For this route the active implementation target is the localized form matrix
and its mixed Fourier tail.

### Suzuki spectral route

\[
\boxed{
Q_W^a
\to
B_a=D^*G_aD
\to
A_a=\mathrm{Friedrichs}(B_a)
\to
W(a,\theta;z)
\to
\text{large-}a\text{ zero attraction}.
}
\]

This route genuinely needs the operator domains, extensions, and resolvents.

Mixing these two routes was making the C005 pipeline harder than necessary.

## 5. Natural implementation contract

For each bounded scale cell \(I=[a_-,a_+]\), the C005 implementation should
produce only three proof-bearing objects:

1. an interval Hermitian enclosure of the finite low matrix \(L_N(a)\);
2. an upper bound on the mixed form norm \(\varepsilon_{N,I}\);
3. the explicit source-level high-mode lower bound \(\nu_{N,I}>0\).

Then the existing interval-Schur code computes a certified lower gap.

Thus the desired dataflow is

\[
\boxed{
\begin{array}{c}
\text{source high-mode theorem}
\longrightarrow \nu_{N,I}\\
\text{localized finite Fourier entries}
\longrightarrow \mu_{N,I}\\
\text{localized mixed-tail estimate}
\longrightarrow \varepsilon_{N,I}
\end{array}
}
\]

followed by

\[
\boxed{
\mu_{N,I}\nu_{N,I}-\varepsilon_{N,I}^2>0.
}
\]

## 6. Current first hard analytic target

After this rebase, the immediate bottleneck is no longer the full
Friedrichs-domain join.

It is

\[
\boxed{
\texttt{MIXED\_FOURIER\_TAIL}:
\quad
|q_{LH,a}(\ell,h)|
\le
\varepsilon_{N,I}\|\ell\|\|h\|
}
\]

uniformly for \(a\in I\).

The finite low block should be implemented in parallel, but it is not an
infinite-dimensional conceptual obstruction.

## 7. Firewall

A finite matrix constructed from the global Hermite ladder is not the
localized Fourier low block.

The new localized form implementation must start from the source
screw/Weil form and the exact coordinate normalization already established.

\`proof_of_rh = false\`
