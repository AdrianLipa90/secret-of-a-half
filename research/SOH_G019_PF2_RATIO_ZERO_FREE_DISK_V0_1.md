# SOH-G019 — PF2 Ratio-Majorant Zero-Free Disk

## Status

**THEOREM-LEVEL / PROVED from SOH-G005 PF2 plus entirety of `F`.**

This result is independent of any table of Riemann zeros. It strengthens the explicit quarter-disk exclusion of G018 by exploiting the full PF2 coefficient-ratio monotonicity.

## 1. Setup

Write

\[
F(w)=\sum_{k\ge0}a_k w^k,
\qquad a_k>0,
\]

where

\[
\xi\!\left(\frac12+z\right)=F(z^2).
\]

G005 proves PF2:

\[
a_k^2\ge a_{k-1}a_{k+1}\qquad(k\ge1).
\]

Since every coefficient is positive, the adjacent ratios

\[
q_k:=\frac{a_{k+1}}{a_k}
\]

are non-increasing:

\[
q_k\le q_{k-1}.
\]

In particular, with

\[
q_0:=\frac{a_1}{a_0},
\]

we have

\[
q_k\le q_0\qquad(k\ge0).
\]

## 2. Geometric coefficient majorant

By induction,

\[
a_k
=a_0\prod_{j=0}^{k-1}q_j
\le a_0 q_0^k.
\]

Therefore for any radius `r` with `q_0 r<1`,

\[
\sum_{k\ge1}a_k r^k
\le
 a_0\sum_{k\ge1}(q_0r)^k
=
 a_0\frac{q_0r}{1-q_0r}.
\]

Define

\[
\boxed{
R_0:=\frac1{2q_0}=\frac{a_0}{2a_1}.}
\]

For `r<R_0`, one has `q_0r<1/2`, hence

\[
\sum_{k\ge1}a_k r^k<a_0.
\]

Consequently

\[
|F(w)|
\ge a_0-\sum_{k\ge1}a_k|w|^k
>0
\qquad(|w|<R_0).
\]

## 3. Why the boundary is also zero-free

At `r=R_0`, the geometric majorant gives

\[
\sum_{k\ge1}a_kR_0^k\le a_0.
\]

Equality in this bound would require

\[
a_k=a_0q_0^k
\qquad\text{for every }k\ge1,
\]

because every summand is nonnegative and bounded termwise by the corresponding geometric summand.

That would make

\[
\limsup_{k\to\infty}a_k^{1/k}=q_0>0,
\]

so the power series for `F` would have finite radius of convergence `1/q_0`. But `F` is entire. Therefore at least one coefficient inequality is strict and

\[
\sum_{k\ge1}a_kR_0^k<a_0.
\]

Hence

\[
\boxed{F(w)\ne0\quad\text{for every }|w|\le R_0.}
\]

This is a closed zero-free disk.

## 4. Canonical numerical regression

Using

\[
a_0=F(0)=\xi(1/2)
\]

and

\[
a_1=\frac12\frac{d^2}{dz^2}\xi(1/2+z)\bigg|_{z=0},
\]

high-precision regression gives approximately

\[
a_0\approx0.4971207781883141,
\qquad
 a_1\approx0.01148597215757272,
\]

and therefore

\[
\boxed{R_0\approx21.64034403742489.}
\]

The numerical value is not used in the proof.

## 5. `z`- and `s`-plane consequence

Since `w=z^2`, every xi zero `rho` satisfies

\[
\left|\rho-\frac12\right|^2>R_0.
\]

Equivalently,

\[
\boxed{
\left|\rho-\frac12\right|>\sqrt{R_0}.}
\]

Numerically,

\[
\sqrt{R_0}\approx4.6519.
\]

Thus the disk centered at the half-axis origin with this radius is zero-free for the completed xi function.

## 6. Relation to G018

G018 proves a fully explicit rational zero-free disk

\[
|w|\le\frac14
\]

and uses it to close the negative-inversion paired-zero frontier.

G019 uses the stronger structural input PF2 and obtains the much larger symbolic radius

\[
R_0=\frac{a_0}{2a_1}.
\]

G019 does not replace G018's elementary rational certificate; it is a stronger downstream consequence of the coefficient theorem.

## 7. Proof firewall

Proved here:

- PF2 implies non-increasing adjacent coefficient ratios;
- `a_k <= a_0(a_1/a_0)^k`;
- the closed disk `|w| <= a_0/(2a_1)` is zero-free;
- every xi zero satisfies `|rho-1/2| > sqrt(a_0/(2a_1))`.

Not proved or claimed here:

- real-rootedness of `F`;
- PF3 or PF-infinity from this argument;
- SOH-G003 real-rootedness;
- the Riemann Hypothesis.
