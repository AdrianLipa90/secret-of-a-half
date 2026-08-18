# SOH-G018 — Zero-Free Quarter Disk and Complete Negative-Inversion Spectral Exclusion

**Claim status:** PROVED from the positive Taylor coefficients of the even quotient, the exact value `F(1/4)=xi(1)=1/2`, and an elementary lower bound `F(0)=xi(1/2)>1/4` obtained from the Dirichlet eta representation.

No table of zeta zeros is used.

## 1. Setup

The even quotient is defined by

\[
\xi\!\left(\frac12+z\right)=F(z^2),
\qquad
F(w)=\sum_{n\ge0}a_nw^n.
\]

SOH-G003 proved

\[
a_n>0\qquad(n\ge0).
\]

The canonical quotient negative inversion is

\[
J(w)=\frac{1}{16w}.
\]

G015 defined the paired root set

\[
P_J=\{w:F(w)=0,\ F(J(w))=0\}.
\]

G016 proved the exact two-sheeted correspondence

\[
q(P_N)=P_J,
\qquad
q(s)=\left(s-\frac12\right)^2,
\]

where

\[
P_N=\{\rho:\xi(\rho)=0,\ \xi(N_s(\rho))=0\}.
\]

The goal of G018 is to prove that both paired sets are actually empty.

## 2. Exact value at the quarter point

At `w=1/4`, one may choose `z=1/2`, so

\[
F\!\left(\frac14\right)=\xi(1).
\]

For the completed xi function

\[
\xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),
\]

the simple pole of `zeta(s)` at `s=1` has residue one. Therefore

\[
\boxed{F(1/4)=\xi(1)=\frac12}.
\]

## 3. Elementary lower bound for `F(0)`

At `w=0`,

\[
F(0)=\xi\!\left(\frac12\right)
=-\frac18\pi^{-1/4}\Gamma\!\left(\frac14\right)\zeta\!\left(\frac12\right).
\]

Use the Dirichlet eta identity

\[
\eta(s)=\bigl(1-2^{1-s}\bigr)\zeta(s),
\qquad \Re s>0.
\]

At `s=1/2`,

\[
-\zeta\!\left(\frac12\right)
=(1+\sqrt2)\eta\!\left(\frac12\right).
\]

The alternating eta series has strictly decreasing positive terms. Its fourth partial sum is therefore a strict lower bound:

\[
\eta\!\left(\frac12\right)
>
1-\frac1{\sqrt2}+\frac1{\sqrt3}-\frac12
=
\frac12-\frac1{\sqrt2}+\frac1{\sqrt3}.
\]

For the gamma factor, `e^{-t}>1-t` on `0<t<=1`, hence

\[
\Gamma\!\left(\frac14\right)
=
\int_0^\infty t^{-3/4}e^{-t}\,dt
>
\int_0^1 t^{-3/4}(1-t)\,dt
=
4-\frac45
=
\frac{16}{5}.
\]

Finally, `pi<4` implies

\[
\pi^{-1/4}>\frac1{\sqrt2}.
\]

Combining these inequalities gives

\[
F(0)>L,
\]

where

\[
L:=
\frac{2}{5\sqrt2}(1+\sqrt2)
\left(
\frac12-\frac1{\sqrt2}+\frac1{\sqrt3}
\right).
\]

We now prove `L>1/4` exactly. Direct simplification yields

\[
60\left(L-\frac14\right)
=
4\sqrt6+8\sqrt3-15-6\sqrt2.
\]

Both sides in

\[
4\sqrt6+8\sqrt3
>
15+6\sqrt2
\]

are positive. Squaring them preserves the inequality. Their squared difference is

\[
(4\sqrt6+8\sqrt3)^2-(15+6\sqrt2)^2
=
-9+12\sqrt2.
\]

Since

\[
\sqrt2>\frac34
\]

(the square comparison is `2>9/16`, equivalently `32>9`), one has

\[
-9+12\sqrt2>0.
\]

Therefore

\[
\boxed{F(0)>L>\frac14}.
\]

## 4. Zero-free closed quarter disk

Let `a_0=F(0)`. For any `|w|<=1/4`, coefficient positivity gives

\[
\begin{aligned}
|F(w)-a_0|
&=
\left|\sum_{n\ge1}a_nw^n\right|\\
&\le
\sum_{n\ge1}a_n|w|^n\\
&\le
\sum_{n\ge1}a_n4^{-n}\\
&=
F(1/4)-F(0)\\
&=
\frac12-a_0.
\end{aligned}
\]

But `a_0>1/4`, so

\[
\frac12-a_0<a_0.
\]

Hence

\[
|F(w)|
\ge
 a_0-|F(w)-a_0|
\ge
2a_0-\frac12
>
2L-\frac12
>0.
\]

Thus:

\[
\boxed{F(w)\neq0\quad\text{for every }|w|\le\frac14.}
\]

Equivalently, every root `w` of `F` satisfies

\[
\boxed{|w|>\frac14.}
\]

This is a global zero-free disk theorem for the even quotient.

## 5. Complete exclusion of negative-inversion paired roots

Suppose, for contradiction, that `w in P_J`. Then `F(w)=0`, so the zero-free disk theorem gives

\[
|w|>\frac14.
\]

But then

\[
|J(w)|
=
\frac{1}{16|w|}
<
\frac14.
\]

The zero-free disk theorem therefore gives

\[
F(J(w))\neq0,
\]

contradicting the definition of `P_J`.

Hence

\[
\boxed{P_J=\varnothing.}
\]

In set language,

\[
\boxed{Z_F\cap J(Z_F)=\varnothing.}
\]

Thus the canonical quotient negative inversion never maps an `F` root to another `F` root.

## 6. Lift to the xi zero set

G016 proved

\[
q(P_N)=P_J.
\]

Since `P_J` is empty,

\[
\boxed{P_N=\varnothing.}
\]

Equivalently,

\[
\boxed{
\xi(\rho)=0
\quad\Longrightarrow\quad
\xi(N_s(\rho))\neq0
}
\]

for every xi zero `rho`, where

\[
N_s(s)=\frac{s-1}{2s-1}.
\]

Therefore the canonical negative inversion is not merely non-invariant on the complete xi zero set: it is **spectrally disjoint** from it.

## 7. Relation to G014--G017

G014 proved that only finitely many xi zeros could possibly be paired by `N_s`.

G015 proved that only finitely many quotient roots could possibly be paired by `J`.

G016 proved the exact two-to-one correspondence between those finite candidate paired sets.

G017 excluded the two fixed points of `J` and forced any remaining exceptions into two-cycles/four-point lifts.

G018 closes the remaining frontier completely:

\[
\boxed{P_J=P_N=\varnothing.}
\]

The G014--G017 results remain valid, but their finite exceptional sets are now proved to have cardinality zero.

## 8. Proof firewall

SOH-G018 proves:

- `F(0)>1/4` by an elementary eta/gamma bound;
- the closed disk `|w|<=1/4` is zero-free for `F`;
- `P_J` is empty;
- `P_N` is empty;
- no xi zero is mapped to another xi zero by the canonical negative inversion.

SOH-G018 does **not** prove:

- that all roots of `F` are real;
- that all xi zeros lie on the critical line;
- PF-infinity;
- SOH-G003 real-rootedness;
- the Riemann Hypothesis.
