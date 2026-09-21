# SOH C005 Natural-Flow Pipeline v0.1

Status: **PIPELINE REBASE / FOURIER SCALING CLOSED / OPERATOR JOIN OPEN / RH OPEN**

## 1. Why the previous flow was choking

The old path mixed three coordinate systems and two different basis choices:

- SOH spectral coordinate \(r=(s-1/2)/i\);
- Suzuki spectral coordinate \(z=i(s-1/2)\);
- SOH arithmetic Fourier coordinate \(x\), using
  \(\exp(-2\pi i x r)\);
- Suzuki's physical coordinate on \([-a,a]\), using
  \(\exp(i z x_{\rm Suz})\);
- Hermite dense-core diagnostics versus Yoshida's Fourier low/high split.

That made every estimate look like a new normalization problem.

## 2. First bottleneck opened: the coordinate/Fourier scaling is exact

Since

\[
r=\frac{s-1/2}{i}=-i(s-1/2),
\qquad
z=i(s-1/2),
\]

we have

\[
\boxed{z=-r.}
\]

Now require equality of the Fourier phases:

\[
-2\pi i x_{\rm SOH}r
=
i z x_{\rm Suz}.
\]

Using \(z=-r\),

\[
\boxed{x_{\rm Suz}=2\pi x_{\rm SOH}.}
\]

This immediately explains the arithmetic prime support already present in the
repository:

\[
x_{\rm SOH}=\frac{\log n}{2\pi}
\quad\Longleftrightarrow\quad
x_{\rm Suz}=\log n.
\]

It also converts a Suzuki localization interval \([-a,a]\) into

\[
\boxed{
|x_{\rm SOH}|\le\frac{a}{2\pi}.
}
\]

So the prime-shift normalization and the spectral sign convention are now
joined exactly.  This part is no longer OPEN.

Executable crosswalk:

\`src/secret_of_a_half/c005_suzuki_normalization.py\`

with regression tests in

\`tests/test_c005_suzuki_normalization.py\`.

## 3. Natural flow after the rebase

The proof-oriented pipeline is now

\[
\boxed{
\begin{array}{c}
\text{SOH/Suzuki Fourier scaling}\\
\downarrow\\
\text{localized form + domain/boundary join}\\
\downarrow\\
\text{Yoshida high-mode coercivity}\\
\downarrow\\
\text{high-mode resolvent}\\
\downarrow\\
\text{low/high coupling}\\
\downarrow\\
\text{finite Schur operator}\\
\downarrow\\
\text{strict nondegeneracy}\\
\downarrow\\
\text{spectral flow or Suzuki zero attraction}
\end{array}}
\]

Every stage consumes exactly the certificate produced by the previous stage.

## 4. Explicit Fourier-tail schedule

For Yoshida's high-frequency subspace the already-derived estimate is

\[
S_N
=
\sum_{|n|>N}\frac1{(\pi n)^2}
\le
\frac{2}{\pi^2N}.
\]

For \(0<a\le a_0\),

\[
R_N(a)
\le
\frac{B(a_0,t_0)}{N},
\]

where

\[
B(a_0,t_0)
=
\frac{8a_0}{\pi^2}
\left(
t_0+a_0t_0^2+\frac{a_0^2t_0^3}{3}
\right).
\]

Therefore a requested leakage budget \(\eta>0\) has the explicit schedule

\[
\boxed{
N\ge
\left\lceil
\frac{B(a_0,t_0)}{\eta}
\right\rceil.
}
\]

This is now executable and fail-closed in

\`src/secret_of_a_half/c005_yoshida_resolvent.py\`.

## 5. Resolvent gate

Once an independently proved high-mode coercivity constant

\[
A_{HH}(a)\ge\nu I
\]

is instantiated in the exact localized normalization, every real
\(z<\nu\) gives

\[
\boxed{
\|(A_{HH}-zI)^{-1}\|
\le
\frac1{\nu-z}.
}
\]

The code now treats \(\nu\) as an external proof-bearing input.  It cannot be
silently synthesized from numerics.

## 6. Schur gate

With

\[
A_a=
\begin{pmatrix}
A_{LL}&B\\
B^*&A_{HH}
\end{pmatrix},
\]

the high-block inverse produces the finite Schur operator

\[
S_a=A_{LL}-BA_{HH}^{-1}B^*.
\]

A coarse scalar certificate is

\[
\mu_{\rm eff}
=
\mu-\frac{\varepsilon^2}{\nu}.
\]

Thus

\[
\boxed{
\mu\nu-\varepsilon^2>0
}
\]

gives strict finite-block nondegeneracy.  The corresponding scalar theorem is
formalized in Lean in \`C005Block.lean\`.

## 7. Two exits from the same pipeline

After the Schur gate the pipeline can feed two independent endgames.

### Exit A: C005 spectral flow

A strict positive Schur margin excludes

\[
\lambda_a=0.
\]

Together with Suzuki's unconditional continuity of the lowest localized
eigenvalue and the known small-\(a\) positive anchor, this is the missing
nondegeneracy input in the C005 route.

### Exit B: Suzuki characteristic functions

The same resolvent control can be used to stabilize the deficiency vectors
entering \(W(a,\theta;z)\).  If this yields local pole-safe zero attraction as
\(a\to\infty\), the already-formalized Lean endgame sends real finite-\(a\)
spectral points to the Riemann seam.

These exits should stay separate until one of them is independently closed.

## 8. Remaining hard gate

The normalization problem has now split cleanly.

CLOSED:

- spectral sign map \(z=-r\);
- Fourier scaling \(x_{\rm Suz}=2\pi x_{\rm SOH}\);
- prime support map \(\log n/(2\pi)\leftrightarrow\log n\);
- support half-width scaling \(a\leftrightarrow a/(2\pi)\).

OPEN:

\[
\boxed{
\text{prove exact equality of the localized SOH arithmetic form
with Suzuki/Yoshida }Q_W^a
}
\]

including:

- test-function domain;
- zero-mean projection where required;
- derivative factors from \(B_a=D^*G_aD\);
- boundary terms;
- closure/Friedrichs extension;
- the coercivity constant in that exact normalization.

That is now the first unresolved gate in the natural flow.  It is narrower
than the previous generic "Suzuki normalization" label.

\`proof_of_rh = false\`


## 9. Bulk-minus-leakage gate from Suzuki/Yoshida

Suzuki's proof of Theorem 4.3 has the exact structural form

\[
Q_a(\phi)
\ge
A\,I(\phi)-D\,L_{t_0}(\phi),
\]

where \(I\) is the full transform energy and \(L_{t_0}\) is the transform
energy restricted to \(|z|\le t_0\).  The constants \(A>0\) and \(D\ge0\)
are built from the proof constants \(C,C_0,C_1,C_2\) once the normalization is
frozen.

The explicit Fourier-tail estimate gives

\[
\frac{L_{t_0}(\phi)}{I(\phi)}
\le
\frac{B(a_0,t_0)}{N}.
\]

Therefore

\[
\boxed{
Q_a(\phi)
\ge
\left(
A-
D\frac{B(a_0,t_0)}{N}
\right)I(\phi).
}
\]

This converts the existence statement into a direct cutoff law.  For any
target high-mode floor \(0\le\nu<A\), it is sufficient to take

\[
\boxed{
N
\ge
\left\lceil
\frac{D\,B(a_0,t_0)}
{A-\nu}
\right\rceil.
}
\]

This adapter is now executable as
\`cutoff_for_target_coercivity\`.

What remains is not the \(N\)-dependence.  It is freezing the source constants
\(A,D,t_0\) in the exact localized SOH/Suzuki normalization.
