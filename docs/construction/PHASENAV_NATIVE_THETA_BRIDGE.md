# Native PhaseNav Theta-Bridge Construction v0.1

## Status

This document specifies an executable candidate construction for the missing bridge in **Secret of a Half**. It is not a proof of the Riemann Hypothesis.

The new object is not text encoded into PhaseNav. The mathematics itself is represented as a 36-dimensional weighted phase state, with PhaseNav operators acting on that state.

## 1. Why the theta representation is the correct entry point

Let

\[
\psi(x)=\sum_{n=1}^{\infty}e^{-\pi n^2x},\qquad x\ge 1.
\]

The completed zeta function admits the symmetric theta-Mellin representation

\[
\xi(s)=\frac12+\frac{s(s-1)}2\int_1^{\infty}\psi(x)
\left(x^{s/2}+x^{(1-s)/2}\right)\frac{dx}{x}.
\]

With \(x=e^u\), \(u\ge0\), and

\[
s=\frac12+z,\qquad z=\delta+it,
\]

this becomes

\[
\xi(s)=\frac12+\frac{s(s-1)}2\int_0^{\infty}
\psi(e^u)e^{u/4}
\left(e^{zu/2}+e^{-zu/2}\right)du.
\]

The two exponentials are a canonical complementary pair. No arbitrary decomposition of \(\xi\) has been introduced.

## 2. The 36D PhaseNav state

The native PhaseNav profile uses 18 positive quadrature nodes \((u_k,q_k)\). Each node produces two complementary rotors, giving exactly 36 dimensions:

\[
R_{k,+}(s)=b_k e^{+zu_k/2},\qquad
R_{k,-}(s)=b_k e^{-zu_k/2},
\]

where

\[
b_k=q_k\psi(e^{u_k})e^{u_k/4}>0.
\]

Writing each rotor as gain times phase,

\[
R_{k,\pm}=\rho_{k,\pm}e^{i\phi_{k,\pm}},
\]

gives

\[
\rho_{k,\pm}=b_k e^{\pm\delta u_k/2},\qquad
\phi_{k,\pm}=\pm t u_k/2\pmod{2\pi}.
\]

Thus \(t\) is represented by phase transport, while \(\delta=\Re(s)-1/2\) is represented by antisymmetric radial gain shear.

## 3. Exact involution covariance

For

\[
J(s)=1-\overline{s},
\]

one has \(z\mapsto-\overline z\). Therefore

\[
R_{k,+}(J(s))=\overline{R_{k,-}(s)},\qquad
R_{k,-}(J(s))=\overline{R_{k,+}(s)}.
\]

If \(X\) swaps every complementary pair, the full state satisfies

\[
P(J(s))=X\overline{P(s)}.
\]

This is an exact identity, tested directly by the executor.

## 4. Native closure defect

The canonical self-dual PhaseNav shell is the shell with equal gains inside each pair. Define

\[
\mathcal C_{18}(s)=
\frac{\sum_{k=0}^{17}\left[\log\left(\rho_{k,+}/\rho_{k,-}\right)\right]^2}
{\sum_{k=0}^{17}u_k^2}.
\]

Since

\[
\log\left(\frac{\rho_{k,+}}{\rho_{k,-}}\right)=\delta u_k,
\]

we obtain the exact identity

\[
\boxed{\mathcal C_{18}(s)=\left(\Re(s)-\frac12\right)^2.}
\]

Consequently,

\[
\mathcal C_{18}(s)=0
\quad\Longleftrightarrow\quad
\Re(s)=\frac12.
\]

This conclusion does not depend on numerical fitting, the location of known zeros, or the quadrature accuracy.

## 5. The detector

The finite PhaseNav detector is

\[
D_{18}(s)=\frac12+\frac{s(s-1)}2
\sum_{k=0}^{17}\left(R_{k,+}(s)+R_{k,-}(s)\right).
\]

As the quadrature is refined and its domain extended,

\[
D_N(s)\longrightarrow\xi(s).
\]

The 18-pair profile is a low-height computational realization. The continuous theta state is the exact mathematical construction.

## 6. Conditional half-axis theorem

For the exact continuous detector, the following implication is immediate:

\[
\xi(s)=0\quad\text{and}\quad\mathcal C(s)=0
\quad\Longrightarrow\quad
\Re(s)=\frac12.
\]

The construction therefore isolates the remaining research statement in one line.

### SOH-PN-C001 — Native Phase Closure Axiom

Every non-trivial zero of \(\xi\) is represented by a zero state that closes in the canonical self-dual PhaseNav shell:

\[
\xi(\rho)=0\quad\Longrightarrow\quad\mathcal C(\rho)=0.
\]

Together with the exact closure identity, SOH-PN-C001 implies the Riemann Hypothesis.

## 7. What has actually been constructed

The construction supplies all of the following without assuming RH:

1. a canonical 36D state derived from the classical theta-Mellin representation;
2. an exact implementation of the zeta involution as pair-swap plus conjugation;
3. a strict separation between phase transport \(t\) and radial shear \(\sigma-1/2\);
4. an exact, gauge-independent closure defect equal to \((\sigma-1/2)^2\);
5. a finite detector converging to \(\xi(s)\);
6. a precise executable formulation of the sole open promotion required by this route.

## 8. What has not been proved

The functional equation alone maps an off-axis zero to a complementary zero. It does not prove that both must occupy one native self-dual PhaseNav shell. Establishing SOH-PN-C001 requires an additional analytic mechanism, such as:

- positivity of a canonical theta-kernel Gram operator;
- a self-adjoint generator whose zero modes are exactly the native closed states;
- a de Branges or Weil positivity theorem adapted to the paired theta state;
- a uniqueness theorem showing that the zero-state representation cannot split into two radially distinct involution partners.

This is now a sharply defined construction problem rather than a verbal analogy.

## 9. Source of truth

The native source is:

```text
construction/phasenav/secret_of_half_theta_bridge.pnv
```

The Python module parses the node basis and execution profile from that file and evaluates the state. It is an auditor, not the primary statement of the construction.
