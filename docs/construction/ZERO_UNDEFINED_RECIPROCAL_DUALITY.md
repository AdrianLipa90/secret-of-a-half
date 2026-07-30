# Zero–Undefined Reciprocal Duality v0.4

## Status

This module formalizes the hypothesis that the half is the balanced state
between a **defined zero** and an **undefined informational state**.  The exact
mathematics is a labelled two-vertex simplex and a reciprocal projective
coordinate.  The ontological interpretation of the second vertex as
"undefined" is exploratory.

IEEE `NaN` is not a number, is not ordered with zero, and is not inserted into
any equation below.  It is only an implementation marker that may be mapped to
the abstract label `UNDEFINED_BOTTOM` before arithmetic begins.

The authoritative native source is:

```text
construction/phasenav/secret_of_half_zero_undefined_duality.pnv
```

## 1. Labelled simplex

Let the two labels be

\[
 Z_0=\texttt{DEFINED\_ZERO},
 \qquad
 U=\texttt{UNDEFINED\_BOTTOM}.
\]

A state is a probability distribution on these labels:

\[
 X(p)=(1-p)Z_0+pU,
 \qquad 0\le p\le1.
\]

This is not arithmetic addition of zero and NaN.  It is a convex coordinate on
a two-element state space.

The label-swap involution is

\[
 C(p)=1-p.
\]

Its unique fixed point is \(p=1/2\).

## 2. Reciprocal projective coordinate

Define the odds coordinate on the extended non-negative line:

\[
 z_{\mathrm{odds}}=\Omega(p)=\frac{p}{1-p}.
\]

The endpoints become

\[
 p=0\longleftrightarrow z_{\mathrm{odds}}=0,
 \qquad
 p=1\longleftrightarrow z_{\mathrm{odds}}=\infty.
\]

A direct calculation gives

\[
 \Omega(1-p)=\frac{1-p}{p}=\frac1{\Omega(p)}.
\]

Thus complement on the simplex is conjugate to the reciprocal map

\[
 z_{\mathrm{odds}}\mapsto\frac1{z_{\mathrm{odds}}}.
\]

The unique positive fixed point is \(z_{\mathrm{odds}}=1\), which corresponds
to \(p=1/2\).

## 3. Spinor and information geometry

Embed the labelled state as

\[
 \Psi(p)=\begin{pmatrix}\sqrt{1-p}\\\sqrt p\end{pmatrix}.
\]

The label swap is the Pauli exchange matrix.  Its positive normalized fixed
state is

\[
 \Psi(1/2)=\frac1{\sqrt2}\begin{pmatrix}1\\1\end{pmatrix}.
\]

For the Bernoulli Fisher metric,

\[
 ds^2=\frac{dp^2}{p(1-p)},
\]

the coordinate

\[
 \theta(p)=2\arcsin\sqrt p
\]

maps the endpoints to \(0\) and \(\pi\).  Therefore

\[
 \theta(1/2)=\frac\pi2,
\]

so the half is also the exact Fisher–Rao geodesic midpoint.

At the same point, binary Shannon entropy is maximal:

\[
 H(1/2)=\ln2.
\]

## 4. Exact claims

- **SOH-L015:** \(\Omega\circ C=R\circ\Omega\), where \(R(z)=1/z\).
- **SOH-L016:** the unique positive reciprocal fixed point corresponds to
  \(p=1/2\), the unique fixed point of label exchange.
- **SOH-L017:** \(p=1/2\) is the Fisher–Rao geodesic midpoint of the two pure
  labelled states.

## 5. Exploratory interpretation

- **SOH-H001:** `DEFINED_ZERO` and `UNDEFINED_BOTTOM` are proposed as the two
  informational boundary labels whose balanced state is the half.

This interpretation is not required for the exact algebra.  It is a proposed
semantic reading of an exact self-dual geometry.

## 6. Claim boundary

The construction does **not** say that IEEE NaN equals infinity.  It does not
order NaN and zero.  It does not prove that zeta zeros obey this labelled-state
model.  Its role in the wider project is to identify another exact mechanism
in which complementarity, reciprocal duality, spinor balance, information
geometry and maximal binary entropy select the same value \(1/2\).
