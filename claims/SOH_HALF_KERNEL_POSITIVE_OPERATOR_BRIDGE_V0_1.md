# So½ Half-Kernel Positive-Operator Bridge v0.1

Status: `EXACT_FINITE_HALF_KERNEL / EXACT_XI_OPERATOR_IDENTITY / INFINITE_GRAM_FACTORIZATION_OPEN`

Date: 2026-09-14

## Scope

This module introduces the half-state mechanism only at the level that survives exact algebraic falsification. It does **not** claim the Riemann Hypothesis.

The bridge has two components:

1. a finite directed terminal operator whose unique kernel is the projective endpoint `1/2`;
2. the infinite-dimensional positive half-operator already latent in the standard Riemann Xi theta kernel.

The remaining RH-equivalent gate is the explicit construction of a translation map `V_y(T)` that factorizes the XF-8C derivative Gram family.

## 1. Directed terminal axis

Use the ordered basis

\[
(|4\rangle,|2\rangle,|1\rangle,|1/2\rangle)
\]

and the deterministic transfer

\[
4\to2,\qquad 2\to1,\qquad 1\to\frac12,\qquad \frac12\to\frac12.
\]

Its column transfer matrix is

\[
P_C=
\begin{pmatrix}
0&0&0&0\\
1&0&0&0\\
0&1&0&0\\
0&0&1&1
\end{pmatrix}.
\]

Set

\[
G_C=I-P_C,\qquad A_C=G_C^\dagger G_C.
\]

Then exactly

\[
\boxed{
A_C=
\begin{pmatrix}
2&-1&0&0\\
-1&2&-1&0\\
0&-1&2&0\\
0&0&0&0
\end{pmatrix}
\succeq0.
}
\]

The annihilating polynomial is

\[
A_C(A_C-2I)(A_C^2-4A_C+2I)=0,
\]

so the spectrum is

\[
\boxed{\{0,2,2-\sqrt2,2+\sqrt2\}}.
\]

Since `rank(A_C)=3`,

\[
\boxed{\ker A_C=\operatorname{span}\{|1/2\rangle\}.}
\]

Thus the half-state is selected as a unique zero mode of a positive, self-adjoint finite operator rather than inserted as a numerical label.

## 2. Exact half projector

Spectral interpolation gives the exact projector

\[
\boxed{
\Pi_{1/2}=I-\frac52A_C+\frac32A_C^2-\frac14A_C^3=|1/2\rangle\langle1/2|.
}
\]

In the declared basis,

\[
\Pi_{1/2}=\operatorname{diag}(0,0,0,1).
\]

No floating-point diagonalization is required.

## 3. Xi theta-kernel half operator

For the standard Xi kernel write

\[
x_n=\pi n^2e^{2u},\qquad D=\frac{d}{du}.
\]

For one theta term,

\[
D e^{-x_n}=-2x_ne^{-x_n},
\]

and

\[
D^2 e^{-x_n}=(4x_n^2-4x_n)e^{-x_n}.
\]

Therefore

\[
(D^2+D)e^{-x_n}=(4x_n^2-6x_n)e^{-x_n}.
\]

After multiplication by \(e^{u/2}\), this produces exactly the standard Xi powers

\[
e^{9u/2},\qquad e^{5u/2}.
\]

If

\[
\Psi(u)=\frac12e^{u/2}\vartheta(e^{2u}),
\]

then the constant theta term is annihilated and

\[
\boxed{\Phi(u)=\left(D^2-\frac14\right)\Psi(u).}
\]

Equivalently define

\[
\boxed{L_{1/2}:=-D^2+\frac14.}
\]

On a boundary-decaying/suitable dense domain,

\[
\boxed{L_{1/2}=\left(D+\frac12\right)^\dagger\left(D+\frac12\right)\succeq0.}
\]

This is an infinite-carrier positive operator with the same distinguished half-shift.

## 4. Exact inverse-scale ladder

The TIR incidence weights satisfy

\[
c=\frac25,\qquad a=\frac27,\qquad b=\frac29,
\]

hence

\[
\boxed{c^{-1}=\frac52,\qquad a^{-1}=\frac72,\qquad b^{-1}=\frac92.}
\]

The Xi-kernel endpoint exponents are exactly `9/2` and `5/2`, and their midpoint is

\[
\boxed{\frac12\left(\frac92+\frac52\right)=\frac72=a^{-1}.}
\]

This is retained as an exact cross-framework structural identity. It is not by itself a physical coupling theorem.

## 5. Finite-rank obstruction

The finite half operator has

\[
\operatorname{rank}A_C=3.
\]

Therefore every factorization of the form

\[
V^\dagger A_CV
\]

has rank at most three. The XF-8C target, however, concerns derivative translation-Gram matrices of arbitrary finite size. Consequently a **bare** finite \(A_C\) cannot close the all-\(n\) gate by itself.

This is a structural no-go, not a failure of the half-state selector.

## 6. Surviving candidate

The admissible carrier is instead

\[
\boxed{\mathscr L_{1/2}=\Pi_{1/2}\otimes L_{1/2}\succeq0.}
\]

The exact remaining target is

\[
\boxed{\dot G_y(T)\stackrel{?}{=}V_y(T)^\dagger\mathscr L_{1/2}V_y(T)}
\]

for every finite translation set \(T\) and every \(0<y<1/2\), with \(V_y(T)\) constructed explicitly from the Xi/theta translation data and without assuming RH.

If such a factorization is derived, positivity follows immediately. Until then the XF-8C gate and RH remain open.

## Promotion ledger

- directed terminal transfer: `EXACT DEFINITION`
- \(A_C=G_C^\dagger G_C\): `EXACT / PSD`
- unique half kernel: `EXACT`
- polynomial half projector: `EXACT`
- Xi theta differential identity: `EXACT`
- \(L_{1/2}\) factorization: `EXACT FORMAL OPERATOR IDENTITY ON SUITABLE DOMAIN`
- inverse ladder \(5/2,7/2,9/2\): `EXACT`
- bare finite-\(A_C\) all-Gram closure: `FAIL / RANK OBSTRUCTION`
- \(\mathscr L_{1/2}=\Pi_{1/2}\otimes L_{1/2}\): `CANDIDATE POSITIVE CARRIER`
- explicit \(V_y(T)\) factorization: `OPEN / RH-EQUIVALENT FRONTIER`
- Riemann Hypothesis: `OPEN`

Executable receipt:

`python scripts/run_soh_half_kernel_operator_bridge.py`
