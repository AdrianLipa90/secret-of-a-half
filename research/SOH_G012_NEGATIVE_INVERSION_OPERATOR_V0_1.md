# SOH-G012 — Euler–Riemann Negative-Inversion Operator Algebra

## Status

**THEOREM-LEVEL OPERATOR GEOMETRY / PROVED.**

This note derives negative inversion as the exact composition of the Riemann reciprocal reflection and the Euler half-turn. It establishes the operator algebra and its fixed-point geometry across the `u`, centered `t`, centered `z`, and quotient `w` coordinates. It makes no claim about the location of nontrivial zeros of the Riemann xi function and does not prove RH.

## 1. Coordinates

Use

\[
u=\frac{s}{1-s},
\qquad
s=\frac{u}{1+u},
\]

and the centered variables

\[
t=2s-1=\frac{u-1}{u+1},
\qquad
z=s-\frac12=\frac{t}{2},
\qquad
w=z^2.
\]

## 2. Two primitive involutions

The Riemann reflection is

\[
\mathcal R_s(s)=1-s.
\]

In the `u` coordinate this becomes

\[
\boxed{\mathcal R_u(u)=\frac1u}.
\]

The Euler half-turn is multiplication by

\[
e^{i\pi}=-1,
\]

hence

\[
\boxed{\mathcal E_u(u)=-u}.
\]

Both are involutions.

## 3. Negative inversion is their composition

The two primitive maps commute on their natural projective domain:

\[
\mathcal R_u\mathcal E_u(u)
=\frac1{-u}
=-\frac1u
=\mathcal E_u\mathcal R_u(u).
\]

Define

\[
\mathcal N:=\mathcal R\circ\mathcal E
=\mathcal E\circ\mathcal R.
\]

Then

\[
\boxed{\mathcal N_u(u)=-\frac1u=\frac{e^{i\pi}}u}.
\]

Furthermore,

\[
\mathcal R^2=\mathcal E^2=\mathcal N^2=\mathrm{id},
\qquad
\mathcal R\mathcal E=\mathcal E\mathcal R=\mathcal N.
\]

Therefore

\[
\boxed{\{\mathrm{id},\mathcal R,\mathcal E,\mathcal N\}\cong V_4},
\]

the Klein four group.

## 4. Centered-chart conjugacies

From

\[
t=\frac{u-1}{u+1},
\]

one obtains exactly

\[
\boxed{\mathcal R_t(t)=-t},
\qquad
\boxed{\mathcal E_t(t)=\frac1t},
\qquad
\boxed{\mathcal N_t(t)=-\frac1t}.
\]

Thus the negative-inversion map in the centered chart is not an independent ansatz: it is the product of the Riemann sign reflection and the Euler reciprocal action.

Since `z=t/2`,

\[
\boxed{\mathcal R_z(z)=-z},
\qquad
\boxed{\mathcal E_z(z)=\frac1{4z}},
\qquad
\boxed{\mathcal N_z(z)=-\frac1{4z}}.
\]

After quotienting by `w=z^2`,

\[
\boxed{\mathcal R_w(w)=w},
\]

while

\[
\boxed{\mathcal E_w(w)=\mathcal N_w(w)=\frac1{16w}}.
\]

Therefore the square quotient kills the distinction between `E` and `N` because it has already quotiented out the sign reflection `R`.

## 5. Fixed points of negative inversion

The fixed-point equation in the `u` coordinate is

\[
u=-\frac1u,
\]

or equivalently

\[
\boxed{u^2=e^{i\pi}=-1}.
\]

Hence

\[
\boxed{u_\pm=\pm i}.
\]

Mapping back to `s` gives

\[
\boxed{s_\pm=\frac12\pm\frac{i}{2}}.
\]

Both satisfy

\[
\Re(s_\pm)=\frac12.
\]

Thus the affine fixed pair of the Euler–Riemann negative inversion lies exactly on the Riemann critical line. This is a geometric operator theorem only; it does not imply that xi zeros must be fixed points of this operator.

In the centered coordinates,

\[
\boxed{t_\pm=\pm i},
\qquad
\boxed{z_\pm=\pm\frac{i}{2}},
\qquad
\boxed{w=-\frac14}.
\]

## 6. Quotient fixed-point stratification

The quotient map

\[
\mathcal N_w(w)=\frac1{16w}
\]

has two fixed values:

\[
\boxed{w=\pm\frac14}.
\]

They have different origins.

For

\[
w=-\frac14,
\]

the preimages

\[
z=\pm\frac{i}{2}
\]

are genuine fixed points of `N_z`.

For

\[
w=+\frac14,
\]

the preimages

\[
z=\pm\frac12
\]

form a two-cycle:

\[
\mathcal N_z\!\left(\frac12\right)=-\frac12,
\qquad
\mathcal N_z\!\left(-\frac12\right)=\frac12.
\]

The square quotient identifies that two-cycle and therefore creates a second fixed value in `w`.

## 7. Logarithmic cylinder

Let

\[
u=e^\lambda.
\]

Then negative inversion has the logarithmic lift

\[
\boxed{\mathcal N_\lambda(\lambda)=i\pi-\lambda}
\]

modulo the full logarithmic period `2πi`.

Its fixed lifts satisfy

\[
\lambda=i\pi-\lambda+2\pi i k,
\]

hence

\[
\boxed{\lambda_k=\frac{i\pi}{2}+\pi i k}.
\]

Exponentiation gives the two classes `u=+i` and `u=-i`.

## 8. Proof firewall

Proved here:

- `R(u)=1/u` and `E(u)=-u` are involutions;
- `R` and `E` commute;
- `N=RE=ER=-1/u`;
- `{id,R,E,N}` is the Klein four group;
- the exact conjugacies in `t`, `z`, and `w`;
- the affine fixed pair `u=±i`;
- its images `s=1/2±i/2` lie on the critical line;
- the distinction between genuine and quotient-created fixed values at `w=±1/4`;
- the logarithmic lift `lambda -> i*pi-lambda` and its fixed family.

Not proved here:

- that any nontrivial xi zero must be a fixed point of `N`;
- that all xi zeros lie on the critical line;
- PF-infinity;
- SOH-G003 real-rootedness;
- the Riemann hypothesis.
