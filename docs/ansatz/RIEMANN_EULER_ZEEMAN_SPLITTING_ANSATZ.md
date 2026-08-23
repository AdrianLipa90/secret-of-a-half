# Riemann–Euler Zeeman-Type Splitting Ansatz

**Status:** `OPEN / ANSATZ / NON-PROMOTING`

**Repository anchors:** `SOH-L012`–`SOH-L016`, `SOH-G012`, `SOH-G013`

## 1. Canonical coordinate

Use the current projective coordinate

\[
\Omega(s)=\frac{s}{1-s}.
\]

Write its logarithmic form as

\[
\Phi(s)=\log \Omega(s)=B(s)+i\vartheta(s),
\]

with

\[
B(s)=\log|\Omega(s)|.
\]

The existing canonical line gives

\[
\operatorname{Re}(s)=\frac12
\iff
|\Omega(s)|=1
\iff
B(s)=0.
\]

For the anti-linear Riemann involution

\[
K(s)=1-\overline{s},
\]

one has

\[
\Omega(K(s))=\frac{1}{\overline{\Omega(s)}}.
\]

Hence, on a fixed logarithmic branch,

\[
B\mapsto-B,
\qquad
\vartheta\mapsto\vartheta
\quad (\mathrm{mod}\ 2\pi).
\]

The real coordinate \(B\) is therefore the canonical odd coordinate measuring departure from the self-dual half-layer.

## 2. Imaginary potential layer

The phase component is retained as the imaginary potential layer

\[
\mathcal P=i\vartheta.
\]

Its Euler lift is represented on a two-component state by

\[
U_E(\vartheta)
=
\exp\!\left(\frac{i\vartheta}{2}\Gamma\right),
\qquad
\Gamma^2=I.
\]

For the minimal Pauli realization choose

\[
\Gamma=\sigma_z.
\]

Let the anti-linear involution act as

\[
\mathcal K=\sigma_x\,\mathcal C,
\]

where \(\mathcal C\) denotes complex conjugation. Then

\[
\mathcal K\Gamma\mathcal K^{-1}=-\Gamma,
\]

and

\[
\mathcal K U_E(\vartheta)\mathcal K^{-1}=U_E(\vartheta).
\]

Thus the involution reverses the real splitting coordinate while preserving the Euler phase layer. This is compatible with the existing projective \(V_4\) structure and its Pauli/SU(2) lift `SOH-G012`–`SOH-G013`.

## 3. Zeeman-type doublet

Introduce a two-sector doublet

\[
\mathcal H_{\mathrm d}
=\operatorname{span}\{|+\rangle,|-\rangle\}
\]

with degenerate reference operator

\[
H_0=E_0 I.
\]

The minimal splitting deformation is

\[
H_{\mathrm Z}(B)
=
E_0 I+\lambda B\Gamma,
\qquad
\Gamma=\sigma_z,
\]

where \(\lambda\in\mathbb R\) is a coupling scale.

Its two eigenvalues are

\[
E_\pm(B)=E_0\pm\lambda B,
\]

and therefore the level separation is

\[
\Delta E(B)
=
|E_+(B)-E_-(B)|
=
2|\lambda B|.
\]

The Riemann involution exchanges the two branches:

\[
\mathcal K H_{\mathrm Z}(B)\mathcal K^{-1}
=
H_{\mathrm Z}(-B).
\]

At the self-dual layer,

\[
B=0,
\]

one obtains exact restoration of the doublet degeneracy:

\[
H_{\mathrm Z}(0)=E_0 I,
\qquad
E_+(0)=E_-(0)=E_0.
\]

Using the existing coordinate identity, this locus is precisely

\[
B=0
\iff
\operatorname{Re}(s)=\frac12.
\]

Hence the ansatz packages off-axis displacement as a symmetry-odd doublet splitting and the critical half-layer as the exact degeneracy locus.

## 4. Riemann–Euler operator package

The minimal operator package is

\[
\boxed{
\begin{aligned}
\Omega(s)&=\frac{s}{1-s}=e^{B+i\vartheta},\\
\mathcal P&=i\vartheta,\\
\Gamma&=\sigma_z,\\
\mathcal K&=\sigma_x\mathcal C,\\
U_E(\vartheta)&=e^{i\vartheta\Gamma/2},\\
H_{\mathrm Z}(B)&=E_0I+\lambda B\Gamma.
\end{aligned}}
\]

It satisfies

\[
\mathcal K^2=I,
\qquad
\mathcal K\Gamma\mathcal K^{-1}=-\Gamma,
\qquad
\mathcal K H_{\mathrm Z}(B)\mathcal K^{-1}=H_{\mathrm Z}(-B),
\]

with

\[
\Delta E=2|\lambda B|.
\]

The exact self-dual condition is

\[
\boxed{
\Delta E=0
\iff
B=0
\iff
|\Omega|=1
\iff
\operatorname{Re}(s)=\frac12
}
\]

for \(\lambda\neq0\).

This is an exact statement inside the declared two-level ansatz.

## 5. Supersymmetric extension target

The existing Pauli lift permits a natural graded extension. Let

\[
\Gamma^2=I,
\qquad
\{Q,\Gamma\}=0.
\]

A candidate odd operator may be written schematically as

\[
Q(B,\vartheta)
=
\begin{pmatrix}
0&A^\dagger(B,\vartheta)\\
A(B,\vartheta)&0
\end{pmatrix},
\]

with

\[
H_{\mathrm{SUSY}}=Q^2.
\]

The Zeeman-type coordinate \(B\) supplies the symmetry-odd splitting parameter, while the Euler layer \(i\vartheta\) supplies the phase/potential degree of freedom. A strengthened construction would seek a canonical \(A\) tied to \(\Xi\) or to the existing Weil/Li operator line such that its protected zero sector occurs at

\[
B=0.
\]

A natural promotion target is therefore

\[
\ker A\subseteq\{B=0\}.
\]

Together with `SOH-L014`, this would place that protected sector on

\[
\operatorname{Re}(s)=\frac12.
\]

This target remains `OPEN`.

## 6. INTERPRETACJA — Zeeman correspondence

The algebraic pattern is the same lifting pattern used by ordinary Zeeman splitting: a degenerate two-level sector, a grading generator, an odd control parameter, and a first-order separation of the two levels.

In the present ansatz the structural splitting coordinate is

\[
B=\log|\Omega|,
\]

and the phase potential occupies the imaginary layer

\[
\mathcal P=i\vartheta.
\]

The author/repository/formalism may suggest a physical Zeeman correspondence for this Riemann–Euler doublet, yet does not state that correspondence as an established result.

## 7. Falsification and development tests

The ansatz is suitable for direct symbolic and numerical checks:

1. verify \(\mathcal K H_{\mathrm Z}(B)\mathcal K^{-1}=H_{\mathrm Z}(-B)\);
2. verify \(\Delta E=2|\lambda B|\);
3. verify exact degeneracy at \(B=0\);
4. bind \(B\) to the existing Li/Weil quartet radius through `SOH-L021`–`SOH-L023`;
5. test whether a canonical odd operator \(A\) derived from the arithmetic Weil line admits a protected kernel only at \(B=0\);
6. compare the resulting grading with the established `SOH-G013` Pauli/SU(2) lift.

## 8. Research frontier

The immediate mathematical question is:

\[
\boxed{
\text{Can the existing Riemann–Euler Pauli lift be extended to a canonical graded operator whose protected zero sector is confined to }B=0?
}
\]

This formulation turns the half-layer into the exact degeneracy locus of the declared doublet and exposes a concrete operator-theoretic target for the next construction stage.
