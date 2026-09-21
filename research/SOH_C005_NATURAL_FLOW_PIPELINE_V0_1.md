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


## 10. Source-constant gate at c=2

The Yoshida/Suzuki proof constants can be partially frozen analytically before
touching the gamma window.

For contour parameter \(c=2\),

\[
C_1=
\max_{\Re w=3}
\left\{
\left|\frac1{w-1}+\frac1w\right|,
\left|\frac{\zeta'}{\zeta}(w)\right|
\right\}
\]

admits the safe bound

\[
\boxed{C_1\le\frac56}.
\]

The rational part is bounded by \(1/2+1/3\).  For the zeta logarithmic
derivative, absolute convergence on \(\Re w=3\) and
\(\Lambda(n)\le\log n\le n-1\) give

\[
\left|\frac{\zeta'}{\zeta}(3+it)\right|
\le
\sum_{n\ge2}\frac{n-1}{n^3}
=
\zeta(2)-\zeta(3)
<
\zeta(2)-1
<
\frac56.
\]

For the kernel comparison constant on \(|t|,|u|\le a_1\), the explicit
Suzuki kernel at \(y=\pm2\) gives the safe envelope

\[
\boxed{
C_2(a_1)\le
\frac{e^{4a_1}-1}{4a_1}.
}
\]

Therefore the source inequality can use the constructive choice

\[
\boxed{
C=
3C_1C_2+\mu+\delta_C,
\qquad \delta_C>0.
}
\]

This stage is now executable in
\`src/secret_of_a_half/c005_yoshida_constants.py\`
and CI emits
\`SOH_YOSHIDA_CONSTANT_GATE_V0_1\`.

The first unresolved analytic gate has therefore moved again.  It is now

\[
\boxed{\texttt{GAMMA\_WINDOW}(C)
=
\{t_0,C_0\}}
\]

with

\[
\Re\!\left[
\psi\!\left(\frac14-\frac{iz}{2}\right)
-\frac12\log\pi
\right]\ge C
\qquad (|z|\ge t_0)
\]

and

\[
C_0\ge
\max_{|z|\le t_0}
\Re\!\left[
\psi\!\left(\frac14-\frac{iz}{2}\right)
-\frac12\log\pi
\right].
\]

Once a rigorous \(t_0,C_0\) pair is available, the coefficients \(A,D\) in
the bulk-minus-leakage inequality become explicit and flow directly into the
already-implemented cutoff/resolvent/Schur stages.


## 11. Equation (4.11) normalization closure

The printed source equation (4.11) keeps a \(1/(2\pi)\) factor in each of
the two symmetric \(+\!z\) and \(-\!z\) channels.  Since

\[
\int_{\mathbb R}|\Phi_1(\phi,-z)|^2dz
=
\int_{\mathbb R}|\Phi_1(\phi,z)|^2dz
\]

and the same holds for the low-frequency window, the two-channel inequality
collapses exactly to

\[
\boxed{
\langle\phi,\phi\rangle_{G_g,a}
\ge
\frac{C-2C_1C_2}{\pi}\,I
-
\frac{C+C_0}{\pi}\,L,
}
\]

where

\[
I=\int_{\mathbb R}|\Phi_1(\phi,z)|^2dz,
\qquad
L=\int_{|z|\le t_0}|\Phi_1(\phi,z)|^2dz.
\]

Combining this with the explicit Fourier leakage law

\[
\frac LI\le\frac{B(a_0,t_0)}{N}
\]

gives the fully explicit high-mode floor

\[
\boxed{
\nu_N
=
\frac{
C-2C_1C_2-(C+C_0)B(a_0,t_0)/N
}{\pi}.
}
\]

Therefore, for a desired raw-integral floor \(\mu>0\), it is sufficient to
choose \(C\) so that

\[
C-2C_1C_2-\pi\mu>0
\]

and then take

\[
\boxed{
N\ge
\left\lceil
\frac{(C+C_0)B(a_0,t_0)}
{C-2C_1C_2-\pi\mu}
\right\rceil.
}
\]

The implementation deliberately uses the stronger normalization-safe choice

\[
C=3C_1C_2+\pi\mu+\delta_C,
\qquad \delta_C>0.
\]

This absorbs the printed \(1/(2\pi)\) factors explicitly instead of hiding
them in the symbol \(\mu\).

The complete source-level certificate now lives in

\`src/secret_of_a_half/c005_yoshida_high_mode.py\`.

Hence the existential high-frequency statement on every fixed bounded
\(a\)-interval has been turned into a constructive certificate.  The current
constants are intentionally very conservative; efficiency is a separate
optimization problem.

The first remaining cross-domain gate is now

\[
\boxed{
\texttt{LOCALIZED\_FORM\_JOIN}:
\quad
\langle\cdot,\cdot\rangle_{G_g,a}
\longleftrightarrow
Q_W^a
\longleftrightarrow
A_a
}
\]

with exact domains, zero-mean/primitive map, boundary terms, and Friedrichs
extension tracked.  Downstream of that join, the next proof-bearing object is
the finite low/high Schur gap, not the high-mode coercivity itself.


## 12. Source-side localized operator join

The old gate \`LOCALIZED_FORM_JOIN\` is now split into a closed source-side
coordinate/operator join and an open repository implementation join.

Suzuki's source operator is

\[
B_a=D_y^*G_aD_y,\qquad
\mathfrak D(B_a)=H_0^1(-a,a),
\]

with \(D_y=i\,d/dy\), \(G_a=P_aGP_a\), and \(A_a\) the Friedrichs extension
of \(B_a\). On \(H_0^1(-a,a)\),

\[
Q_W^a(v)=\langle B_av,v\rangle.
\]

Under the exact SOH scaling

\[
y=2\pi x,
\qquad
(Uf)(x)=\sqrt{2\pi}\,f(2\pi x),
\]

the convolution operator acquires kernel

\[
2\pi\,g(2\pi(x-x')),
\]

the zero-mean projection is preserved, and

\[
U D_y U^{-1}
=
\frac1{2\pi}D_x.
\]

Hence

\[
\boxed{
U B_a U^{-1}
=
\frac1{(2\pi)^2}
D_x^*(U G_aU^{-1})D_x.
}
\]

This closes the coordinate/Jacobian/domain ambiguity of the source operator.

The current first open gate is therefore narrower:

\[
\boxed{
\texttt{REPOSITORY\_LOCALIZED\_IMPLEMENTATION\_JOIN}
}
\]

namely: instantiate the actual zeta screw kernel in the SOH coordinate and
verify its localized Fourier matrix elements against the repository's
arithmetic Weil decomposition.

The existing global translated-Hermite matrix is retained as a dense-core
diagnostic and is not promoted into this localized role.

Downstream plumbing is already present:

\[
\text{localized interval matrix entries}
\to
\text{interval eigenvalue/coupling bounds}
\to
\text{Schur gap}
\to
\text{continuation cells}.
\]


## 13. Direct C005 route no longer waits on the operator domain

A structural simplification is now explicit.

Yoshida/Suzuki high-mode coercivity is already a statement about the localized
Weil/Hermitian form.  Therefore the direct C005 positivity route can remain at
form level:

\[
q_a[\ell+h]
=
q_{LL,a}[\ell]
+
2\Re q_{LH,a}(\ell,h)
+
q_{HH,a}[h].
\]

With

\[
q_{LL,a}[\ell]\ge\mu\|\ell\|^2,
\]

\[
|q_{LH,a}(\ell,h)|
\le\varepsilon\|\ell\|\|h\|,
\]

and the source high-mode theorem

\[
q_{HH,a}[h]\ge\nu\|h\|^2,
\]

the scalar C005 theorem gives the complete form-level gate

\[
\mu\nu-\varepsilon^2\ge0.
\]

Thus the Friedrichs/domain join belongs to the Suzuki spectral exit, not to the
minimal direct C005 route.

The direct route now has the shorter flow

\[
\boxed{
\text{localized source form}
\to
\text{finite low Fourier block}
+
\text{mixed Fourier tail}
+
\text{explicit high coercivity}
\to
\text{interval Schur}
\to
\text{continuation}.
}
\]

The immediate analytic frontier is the uniform mixed-form tail
\(\varepsilon_{N,I}\), with the finite low block developed in parallel.
