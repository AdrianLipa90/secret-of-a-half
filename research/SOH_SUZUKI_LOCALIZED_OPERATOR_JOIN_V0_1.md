# SOH Suzuki Localized Operator Join v0.1

Status: **SOURCE OPERATOR JOIN CLOSED / REPOSITORY IMPLEMENTATION JOIN OPEN / RH OPEN**

Primary source: Masatoshi Suzuki, *Weil's quadratic form via the screw
function*, arXiv:2606.09096, version dated 19 August 2026.

## 1. Source-side operator chain

Suzuki defines the continuous even screw kernel \(g\), the convolution operator

\[
(Gu)(y)=\int_{\mathbb R} g(y-v)u(v)\,dv,
\]

the zero-mean localized space

\[
L_0^2(-a,a)
=
\left\{
u\in L^2(-a,a):
\int_{-a}^a u(y)\,dy=0
\right\},
\]

and the orthogonal projection \(P_a\) onto that space.  The localized kernel
operator is

\[
G_a=P_aGP_a.
\]

With

\[
D_y=i\frac{d}{dy}
\]

and Dirichlet boundary conditions, Suzuki defines

\[
\boxed{
B_a=D_y^*G_aD_y,
\qquad
\mathfrak D(B_a)=H_0^1(-a,a).
}
\]

Theorem 1.1 identifies the localized self-adjoint Weil operator \(A_a\) as the
Friedrichs extension of \(B_a\).  Lemma 3.1 / equation (1.8) gives

\[
\boxed{
Q_W^a(v)=\langle B_av,v\rangle
\qquad
(v\in H_0^1(-a,a)).
}
\]

This part is external prior art and does not assume RH.

## 2. Exact SOH coordinate pullback

The SOH arithmetic Fourier convention uses

\[
y=2\pi x.
\]

Define the unitary map

\[
\boxed{
(U_af)(x)=\sqrt{2\pi}\,f(2\pi x)
}
\]

from

\[
L^2(-a,a;dy)
\]

to

\[
L^2\!\left(
-\frac{a}{2\pi},
\frac{a}{2\pi};dx
\right).
\]

The interval, \(L^2\) norm, zero-mean condition, and Dirichlet endpoints are
all preserved exactly under this map.

The Yoshida/Suzuki Fourier basis

\[
e_n^{(a)}(y)
=
\frac1{\sqrt{2a}}
e^{\pi i n y/a}
\]

becomes

\[
\boxed{
(U_ae_n^{(a)})(x)
=
\sqrt{\frac{\pi}{a}}\,
e^{2\pi^2 i n x/a}.
}
\]

## 3. Convolution kernel pullback

For any convolution kernel \(g\),

\[
UGU^{-1}
\]

is again convolution on the scaled interval, with kernel

\[
\boxed{
g_{\rm pull}(x-x')
=
2\pi\,g(2\pi(x-x')).
}
\]

The zero-mean orthogonal projection is transported into the corresponding
zero-mean projection on the SOH interval. Therefore

\[
\boxed{
UG_aU^{-1}
=
P_{a/(2\pi)}^{(0)}
\,G_{\rm pull}\,
P_{a/(2\pi)}^{(0)}.
}
\]

No arithmetic approximation is involved in this identity.

## 4. Derivative and \(B_a\) pullback

The derivative scales as

\[
\boxed{
U D_y U^{-1}
=
\frac1{2\pi}D_x,
\qquad
D_x=i\frac{d}{dx}.
}
\]

Consequently,

\[
\boxed{
U B_a U^{-1}
=
\frac1{(2\pi)^2}
D_x^*
\left(UG_aU^{-1}\right)
D_x.
}
\]

Equivalently, if one removes the \(2\pi\) Jacobian from the pulled convolution
operator and defines \(G_{\rm raw}\) with kernel \(g(2\pi(x-x'))\), then

\[
\boxed{
U B_a U^{-1}
=
\frac1{2\pi}
D_x^*G_{\rm raw}D_x.
}
\]

This resolves the coordinate/Jacobian ambiguity in the localized operator.

Executable contract:

\`src/secret_of_a_half/c005_suzuki_localization.py\`.

## 5. What is now actually open

The old label "Suzuki localization normalization" was too coarse.  It now
splits into two pieces.

### CLOSED

- \(z_{\rm Suzuki}=-r_{\rm SOH}\);
- \(x_{\rm Suzuki}=2\pi x_{\rm SOH}\);
- support interval scaling;
- unitary \(L^2\) Jacobian;
- Fourier-basis normalization;
- zero-mean subspace;
- Dirichlet endpoint correspondence;
- generic convolution-kernel pullback;
- derivative and \(D^*GD\) prefactors;
- source theorem \(A_a=\mathrm{Friedrichs}(B_a)\);
- source form identity on \(H_0^1\).

### OPEN

The remaining repository-specific join is

\[
\boxed{
\text{implement the actual zeta screw kernel }g
\text{ and verify that the resulting localized matrix elements}
}
\]

match the arithmetic Weil formulas used elsewhere in SOH, including every
prime, archimedean, conductor, pole/boundary, and regularization contribution.

The current translated Hermite arithmetic matrix is a global dense-core
diagnostic and must **not** be silently treated as a finite section of
\(A_a\).

## 6. Natural next object

The next proof-bearing implementation should therefore be a separate localized
Fourier operator module, not another patch to the global Hermite matrix.

Its API should expose, for fixed \(a,N\),

\[
A_{LL}(a),\qquad
B(a),\qquad
A_{HH}(a)
\]

in the pulled-back Suzuki Fourier basis, together with interval/error
enclosures.

Those outputs feed directly into the already-created interval Schur layer:

\[
\boxed{
\texttt{localized Fourier entries}
\to
\texttt{interval Schur}
\to
\texttt{uniform continuation}.
}
\]

\`proof_of_rh = false\`
