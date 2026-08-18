# SOH-G018 — Quarter-Disk Zero Exclusion and Complete Negative-Inversion Spectral No-Go

## Status

**THEOREM-LEVEL / PROVED.**

This result closes the finite exceptional-pair frontier left by G014–G017. It does not prove real-rootedness of `F`, PF-infinity, SOH-G003, or the Riemann Hypothesis.

## 1. Setup

Recall the even quotient

\[
\xi\!\left(\frac12+z\right)=F(z^2),
\qquad
F(w)=\sum_{k\ge0}a_k w^k,
\qquad a_k>0,
\]

and the quotient negative inversion

\[
J(w)=\frac1{16w}.
\]

G015 proved that the paired set

\[
P_J=\{w:F(w)=0,\;F(J(w))=0\}
\]

is finite. G017 excluded the two fixed points of `J`. G018 proves the stronger statement

\[
\boxed{P_J=\varnothing.}
\]

By the exact two-to-one correspondence of G016 this also gives

\[
\boxed{P_N=\varnothing}
\]

for the paired xi-zero set in the `s`-plane.

## 2. Elementary lower bound for `xi(1/2)`

With the standard completed xi normalization,

\[
\xi\!\left(\frac12\right)
=\frac18\pi^{-1/4}\Gamma\!\left(\frac14\right)
\bigl(-\zeta(1/2)\bigr).
\]

We derive a rational lower bound using only elementary inequalities.

### 2.1 Dirichlet eta bound

The alternating eta series gives

\[
\eta\!\left(\frac12\right)
>1-\frac1{\sqrt2}+\frac1{\sqrt3}-\frac12.
\]

The exact integer inequalities

\[
2\cdot71^2>100^2,
\qquad
3\cdot57^2<100^2
\]

imply

\[
\frac1{\sqrt2}<\frac{71}{100},
\qquad
\frac1{\sqrt3}>\frac{57}{100}.
\]

Hence

\[
\eta\!\left(\frac12\right)>\frac9{25}.
\]

Since

\[
\eta(s)=(1-2^{1-s})\zeta(s),
\]

we have at `s=1/2`

\[
-\zeta\!\left(\frac12\right)
=(\sqrt2+1)\eta\!\left(\frac12\right).
\]

Using `sqrt(2)>7/5`,

\[
-\zeta\!\left(\frac12\right)
>\frac{12}{5}\frac9{25}
=\frac{108}{125}.
\]

### 2.2 Gamma bound

For `0<=t<=1`, the alternating Taylor remainder gives

\[
e^{-t}\ge1-t+\frac{t^2}{2}-\frac{t^3}{6}.
\]

Therefore

\[
\Gamma\!\left(\frac14\right)
>\int_0^1 t^{-3/4}
\left(1-t+\frac{t^2}{2}-\frac{t^3}{6}\right)dt
\]

and the integral is exact:

\[
4-\frac45+\frac29-\frac2{39}
=\frac{1972}{585}.
\]

Thus

\[
\Gamma\!\left(\frac14\right)>\frac{1972}{585}.
\]

### 2.3 Pi bound

The classical elementary bound `pi<22/7`, together with

\[
\frac{22}{7}<\left(\frac{50}{37}\right)^4,
\]

gives

\[
\pi^{-1/4}>\frac{37}{50}.
\]

### 2.4 Combined xi bound

Multiplying the three strict lower bounds,

\[
\xi\!\left(\frac12\right)
>\frac18\frac{37}{50}\frac{1972}{585}\frac{108}{125}
=\frac{54723}{203125}
>\frac14.
\]

Hence

\[
\boxed{F(0)=\xi(1/2)>54723/203125>1/4.}
\]

## 3. Exact quarter-disk zero exclusion

The positive-coefficient theorem gives `a_k>0`. Also

\[
F\!\left(\frac14\right)
=\xi(1)
=\frac12.
\]

For every `|w|<=1/4`,

\[
\begin{aligned}
|F(w)|
&\ge a_0-\sum_{k\ge1}a_k|w|^k\\
&\ge a_0-\sum_{k\ge1}a_k4^{-k}\\
&=2a_0-F(1/4).
\end{aligned}
\]

Using the rational lower bound for `a_0=F(0)`,

\[
|F(w)|
>2\frac{54723}{203125}-\frac12
=\frac{15767}{406250}
>0.
\]

Therefore

\[
\boxed{F(w)\neq0\quad\text{for every }|w|\le1/4.}
\]

Equivalently, every zero `w` of `F` satisfies

\[
\boxed{|w|>1/4.}
\]

This is an analytic zero-free disk, not a finite numerical scan.

## 4. Complete negative-inversion spectral no-go

If `F(w)=0`, then the quarter-disk theorem gives `|w|>1/4`. Therefore

\[
|J(w)|
=\frac1{16|w|}
<\frac14.
\]

But the entire closed quarter-disk is zero-free. Hence

\[
F(J(w))\neq0.
\]

Thus

\[
\boxed{P_J=\varnothing.}
\]

In set form,

\[
\boxed{Z_F\cap J(Z_F)=\varnothing.}
\]

G016 proves `q(P_N)=P_J` with `q(s)=(s-1/2)^2`, so

\[
\boxed{P_N=\varnothing}
\]

and therefore

\[
\boxed{Z_\xi\cap N_s(Z_\xi)=\varnothing.}
\]

The canonical negative inversion remains an exact projective/operator symmetry of the coordinate geometry, but it maps **no xi zero to another xi zero**.

## 5. Relation to G014–G017

- G014: `P_N` finite.
- G015: `P_J` finite.
- G016: `q:P_N->P_J` exactly two-to-one.
- G017: no fixed exceptional roots; exceptional sets, if nonempty, consist only of finite two-/four-cycles.
- **G018: the exceptional sets are empty.**

Thus the negative-inversion spectral frontier is closed completely.

## 6. Proof firewall

Proved here:

- the exact rational lower bound `xi(1/2)>54723/203125>1/4`;
- the uniform bound `|F(w)|>15767/406250` for `|w|<=1/4`;
- the zero-free disk `|w|<=1/4`;
- every root of `F` has modulus strictly greater than `1/4`;
- `P_J=empty`;
- `P_N=empty` via G016;
- the canonical negative inversion maps no xi zero to another xi zero.

Not proved or claimed here:

- that all roots of `F` are real;
- PF-infinity;
- SOH-G003 real-rootedness;
- the Riemann Hypothesis.
