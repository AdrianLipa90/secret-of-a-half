# SOH Relational Zero Triad v0.1

**Date:** 24 September 2026  
**Status:** EXACT WITHIN THE DECLARED RELATIONAL MODEL / RH BINDING NOT PROMOTED  
**Purpose:** reduce the relational-zero construction to the minimum axioms needed by Occam's razor and prove the same zero by three independent routes.

## 1. Minimal axiom set

### RZ-A1 — normalized relational complementarity

Every admitted local relation \(e\) is represented by a normalized complementary coordinate

\[
p_e=(\sigma_e,1-\sigma_e),\qquad 0<\sigma_e<1,
\]

with involution

\[
J_e(\sigma_e)=1-\sigma_e.
\]

The centered coordinate is

\[
x_e=\sigma_e-\frac12.
\]

No ontological claim about an isolated "absolute zero" is required. Within this model, zero is a property of a relation: vanishing centered displacement and/or vanishing relational dynamical defect.

### RZ-A2 — positive relational action-defect

Let \(E\) be finite or countable. For every relation let \(F_e\) be its relational dynamical vector in a positive-definite metric \(G_e\). Let \(w_e,\lambda_e>0\). Define

\[
D_H(\sigma)
=
\ln 2-H_2(\sigma)
=
D_{\mathrm{KL}}\!\left(
(\sigma,1-\sigma)
\middle\|
\left(\frac12,\frac12\right)
\right),
\]

and define the extended non-negative relational action-defect

\[
\boxed{
\mathfrak S_{\rm rel}
=
\sum_{e\in E}
w_e\left[
\|F_e\|_{G_e}^2+\lambda_e D_H(\sigma_e)
\right]\in[0,\infty].
}
\]

A **local Lagrange node** is a relation with \(F_e=0\). A **global relational zero** is a state with \(\mathfrak S_{\rm rel}=0\).

This \(\mathfrak S_{\rm rel}\) is not the ordinary Lorentzian action \(S=\int L\,dt\). Standard stationarity \(\delta S=0\) must not be conflated with \(\mathfrak S_{\rm rel}=0\).

## 2. Three-route zero theorem

### Theorem SOH-RZ001 — algebraic fixed-point route

For every admitted relation,

\[
J_e(\sigma_e)=\sigma_e
\iff
1-\sigma_e=\sigma_e
\iff
\sigma_e=\frac12
\iff
x_e=0.
\]

Hence the normalized complement involution has a unique relational center.

### Theorem SOH-RZ002 — Shannon/KL route

Binary entropy is

\[
H_2(\sigma)
=
-\sigma\ln\sigma-(1-\sigma)\ln(1-\sigma).
\]

Its deficit from the binary maximum obeys

\[
D_H(\sigma)
=
\ln2-H_2(\sigma)
=
D_{\mathrm{KL}}
\!\left(
(\sigma,1-\sigma)
\middle\|
\left(\frac12,\frac12\right)
\right)
\ge0.
\]

By the equality condition for KL divergence,

\[
D_H(\sigma)=0
\iff
\sigma=\frac12
\iff
x=0.
\]

Equivalently,

\[
H_2(\sigma)=\ln2
\iff
\sigma=\frac12.
\]

Moreover,

\[
D_H'(\sigma)=\ln\frac{\sigma}{1-\sigma},
\qquad
D_H''(\sigma)=\frac1{\sigma}+\frac1{1-\sigma}>0,
\]

so the half is the unique stationary point and strict global minimum of the information defect.

### Theorem SOH-RZ003 — relational Lagrange/action route

Because every summand in \(\mathfrak S_{\rm rel}\) is non-negative and every coefficient is positive,

\[
\mathfrak S_{\rm rel}=0
\]

holds if and only if every summand vanishes. Therefore

\[
\boxed{
\mathfrak S_{\rm rel}=0
\iff
\forall e\in E:
\quad
F_e=0
\quad\text{and}\quad
\sigma_e=\frac12.
}
\]

Thus

\[
\boxed{
\text{global relational zero}
\iff
\text{all local Lagrange nodes close}
\iff
x_e=0\ \forall e
\iff
\sigma_e=\frac12\ \forall e.
}
\]

For the entropy potential alone,

\[
V_e(\sigma_e)=\lambda_e D_H(\sigma_e),
\]

the equilibrium equation is

\[
\frac{\partial V_e}{\partial\sigma_e}
=
\lambda_e\ln\frac{\sigma_e}{1-\sigma_e}
=0,
\]

which has the unique solution \(\sigma_e=1/2\).

The result is independent of the number of relations and of their graph topology. Adding relations increases the number of local conditions; it does not move the normalized complement fixed point.

## 3. Triangular equivalence

The three routes meet at the same point:

\[
\boxed{
x=0
\iff
\sigma=\frac12
\iff
H_2=\ln2
\iff
D_H=0.
}
\]

With the relational dynamics included,

\[
\boxed{
\mathfrak S_{\rm rel}=0
\iff
\bigcap_{e\in E}\{F_e=0,\ \sigma_e=1/2\}.
}
\]

This is the **Relational Zero Triad**.

## 4. Spinorial cross-check

Inside the already declared binary-spinor representation,

\[
e^{2\pi i\sigma}=-1
\]

has the unique solution \(\sigma=1/2\) in \(0<\sigma<1\). Therefore the spinorial sign is a fourth consistency check, not an additional axiom.

## 5. Boundary with standard celestial Lagrange points

The project term "Lagrange node" means a zero of a declared relational vector field \(F_e\). Standard celestial-mechanics Lagrange points are equilibria of an effective rotating-frame potential and are not, in general, located at the geometric midpoint between two bodies. This theorem therefore does **not** claim that every astronomical Lagrange point has coordinate \(1/2\).

## 6. Riemann binding

For the Riemann involution

\[
s\mapsto1-\overline{s},
\]

the normalized horizontal coordinate is

\[
\sigma=\Re s,
\qquad
x=\Re s-\frac12.
\]

The triad proves exactly that any state already established to be a relational zero-mode of this model must satisfy

\[
x=0,
\qquad
\Re s=\frac12.
\]

Hence the following corollary is exact as an implication:

\[
\boxed{
\left[
\xi(\rho)=0
\Longrightarrow
\rho\text{ is a global relational zero-mode}
\right]
\Longrightarrow
\Re\rho=\frac12.
}
\]

The premise in square brackets is the zeta-to-relational-zero binding. This note does not silently identify that premise with the three-route theorem and does not change the external proof status of RH.

## 7. Occam summary

Only two structural assumptions are retained:

1. normalized complementarity of an admitted relation;
2. a positive relational defect built from the dynamical norm and the Shannon/KL imbalance.

Everything else in the zero triad is derived.

\[
\boxed{
0_{\rm centered}
\equiv
\frac12_{\rm binary}
\equiv
\ln2_{\rm Shannon\ maximum}
\equiv
0_{\rm relational\ defect}.
}
\]

Q.E.D. for SOH-RZ001--SOH-RZ003.
