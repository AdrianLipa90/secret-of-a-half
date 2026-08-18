# SOH-G016 — Paired-Spectrum Quotient Correspondence

## Status

**THEOREM-LEVEL EXACT CORRESPONDENCE / PROVED.**

This note identifies the precise relation between the finite paired-zero set `P_N` from G014 and the finite paired-root set `P_J` from G015.

## 1. Quotient map

Define

\[
q(s)=\left(s-\frac12\right)^2.
\]

Then

\[
q(1-s)=q(s),
\]

so `q` is exactly the even quotient associated with

\[
\xi\!\left(\frac12+z\right)=F(z^2).
\]

For every `w != 0`, the fiber is exactly

\[
q^{-1}(w)
=\left\{\frac12+\sqrt w,\frac12-\sqrt w\right\},
\]

a pair exchanged by `s -> 1-s`.

Because

\[
F(0)=\xi(1/2)>0,
\]

zero is not in `Z_F`. Hence every quotient root has exactly two distinct xi-zero preimages.

## 2. Commuting negative-inversion diagram

G014 gives

\[
N_s(s)=\frac{s-1}{2s-1}.
\]

G015 gives

\[
J(w)=\frac1{16w}.
\]

Writing `z=s-1/2`, G012 gives `N_z(z)=-1/(4z)`. Therefore

\[
q(N_s(s))
=N_z(z)^2
=\frac1{16z^2}
=J(q(s)).
\]

Thus the diagram commutes exactly:

\[
\boxed{q\circ N_s=J\circ q.}
\]

## 3. Paired sets

Recall

\[
P_N
=\{\rho:\xi(\rho)=0,\ \xi(N_s(\rho))=0\}
\]

and

\[
P_J
=\{w:F(w)=0,\ F(J(w))=0\}.
\]

## 4. Main correspondence theorem

### Theorem

\[
\boxed{q(P_N)=P_J.}
\]

Moreover, the restriction

\[
q:P_N\to P_J
\]

is exactly two-to-one. Consequently

\[
\boxed{|P_N|=2|P_J|.}
\]

### Proof

Take `rho in P_N`. Then `xi(rho)=0`, so by the quotient identity

\[
F(q(\rho))=0.
\]

Also `xi(N_s(rho))=0`. Using the commuting diagram,

\[
F(J(q(\rho)))
=F(q(N_s(\rho)))
=0.
\]

Hence `q(rho) in P_J`, proving

\[
q(P_N)\subseteq P_J.
\]

Conversely, take `w in P_J`. Since `F(w)=0` and `w != 0`, choose either point

\[
\rho_\pm=\frac12\pm\sqrt w
\]

in the fiber. The quotient identity gives

\[
\xi(\rho_\pm)=F(w)=0.
\]

The commuting diagram gives

\[
q(N_s(\rho_\pm))=J(w).
\]

Since `F(J(w))=0`, every point in the fiber over `J(w)` is an xi zero, so in particular

\[
\xi(N_s(\rho_\pm))=0.
\]

Thus both `rho_+` and `rho_-` lie in `P_N`, and

\[
w=q(\rho_\pm)\in q(P_N).
\]

Therefore

\[
P_J\subseteq q(P_N),
\]

and equality follows.

Finally, `w=0` is not a root of `F`, so every `w in P_J` has exactly two distinct preimages under `q`. The argument above shows both belong to `P_N`. Hence the restricted map is exactly two-to-one and

\[
|P_N|=2|P_J|.
\]

QED.

## 5. Orbit lift

The quotient involution satisfies `J^2=id`, while `N_s^2=id`. The commuting diagram therefore lifts every quotient paired orbit to paired xi-zero orbits.

If

\[
\{w,J(w)\}
\]

is a non-fixed two-cycle in `P_J`, its two quotient fibers contain four xi zeros. Negative inversion arranges those four points into two `N_s` two-cycles, with the two cycles exchanged by the functional reflection `s -> 1-s`.

If the exceptional quotient fixed root

\[
w=-\frac14
\]

were present, its fiber is

\[
\left\{\frac12+\frac i2,\frac12-\frac i2\right\},
\]

and both points are fixed individually by `N_s`, exactly as proved in G012.

The positive fixed value `w=+1/4` is excluded by `F(1/4)>0` and therefore contributes no paired xi-zero fiber.

## 6. Cardinality consequences

Because G014 and G015 prove both paired sets finite,

\[
\boxed{|P_N|\text{ is always even}.}
\]

More precisely, if `P_J` consists of `M` non-fixed two-cycles and possibly the fixed root `-1/4`, then

\[
|P_J|=2M+\varepsilon,
\qquad
|P_N|=4M+2\varepsilon,
\]

where

\[
\varepsilon\in\{0,1\}
\]

records whether `F(-1/4)=0`.

Thus the unresolved fixed-root question appears consistently in both coordinate layers, but the two-to-one quotient correspondence itself is unconditional.

## 7. Proof firewall

Proved here:

- `q(s)=(s-1/2)^2` identifies the functional-reflection pair;
- `q o N_s = J o q` exactly;
- `q(P_N)=P_J`;
- `q:P_N -> P_J` is exactly two-to-one;
- `|P_N|=2|P_J|`;
- every non-fixed quotient paired two-cycle lifts to two xi paired two-cycles;
- the possible fixed quotient root `-1/4` lifts to the G012 fixed xi pair.

Not proved or claimed here:

- whether `F(-1/4)` vanishes;
- that either paired set is empty;
- real-rootedness of `F`;
- PF-infinity;
- SOH-G003;
- RH.
