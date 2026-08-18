# SOH-G015 — Quotient Negative-Inversion Zero-Set No-Go

## Status

**THEOREM-LEVEL QUOTIENT NO-GO / PROVED.**

This note transfers the G014 spectral firewall to the even entire quotient

\[
\xi\!\left(\frac12+z\right)=F(z^2).
\]

The G012 negative inversion acts on

\[
w=z^2
\]

as

\[
\boxed{J(w)=\frac1{16w}}.
\]

The result below proves that only finitely many zeros of `F` can be paired with another zero by `J`. It also classifies the possible finite exceptional orbits.

## 1. Quotient entire function

By the evenness of the centered xi function, there is a unique entire function `F` such that

\[
\xi\!\left(\frac12+z\right)=F(z^2).
\]

The positive-kernel/coefficient theorem already proved in this programme gives

\[
F(w)=\sum_{k\ge0}a_k w^k,
\qquad a_k>0.
\]

In particular,

\[
\boxed{F(0)=\xi(1/2)>0}
\]

and

\[
\boxed{F(x)>0\quad\text{for every }x\ge0.}
\]

## 2. Quotient negative inversion

G012 gives

\[
N_z(z)=-\frac1{4z}.
\]

Squaring yields the exact quotient action

\[
\boxed{
J(w)=\frac1{16w}.
}
\]

It is an involution:

\[
J(J(w))=w.
\]

Its fixed points satisfy

\[
w=\frac1{16w},
\]

hence

\[
\boxed{w=\pm\frac14}.
\]

Because `F(x)>0` on the non-negative real axis,

\[
\boxed{F(1/4)>0},
\]

so `+1/4` can never be a quotient fixed root.

## 3. Paired quotient roots

Let

\[
Z_F=\{w\in\mathbb C:F(w)=0\}
\]

and define

\[
P_J
=\{w\in Z_F:F(J(w))=0\}.
\]

The zero set `Z_F` is infinite. Indeed, Hardy's theorem gives infinitely many xi zeros

\[
\rho_n=\frac12+i\gamma_n
\]

with unbounded `|gamma_n|`, and these produce distinct quotient zeros

\[
w_n=(\rho_n-1/2)^2=-\gamma_n^2.
\]

## 4. Main theorem

### Theorem

\[
\boxed{P_J\text{ is finite}.}
\]

### Proof

Assume that `P_J` is infinite.

Since `F` is a non-zero entire function, its zeros are isolated. Therefore an infinite subset of `Z_F` is unbounded. Choose

\[
w_n\in P_J,
\qquad
|w_n|\to\infty.
\]

By definition,

\[
F(J(w_n))=0
\]

for every `n`. But

\[
J(w_n)=\frac1{16w_n}\to0.
\]

Continuity of the entire function `F` therefore gives

\[
F(0)
=\lim_{n\to\infty}F(J(w_n))
=0,
\]

contradicting

\[
F(0)=\xi(1/2)>0.
\]

Hence `P_J` is finite. QED.

## 5. No global quotient-root invariance

Since `Z_F` is infinite while `P_J` is finite,

\[
\boxed{J(Z_F)\ne Z_F}.
\]

More strongly,

\[
\boxed{
\text{all but finitely many roots of }F\text{ are mapped by }J\text{ to non-roots.}
}
\]

Thus the exact quotient geometry

\[
w\mapsto\frac1{16w}
\]

is not a global symmetry of the `F` spectrum.

## 6. Exact orbit classification of the exceptional set

If `w in P_J`, then both `w` and `J(w)` are roots. Since `J^2=id`, the set `P_J` is invariant under `J` and decomposes into finite `J`-orbits.

Every orbit has size one or two.

The size-one orbits are fixed points of `J`, hence are contained in

\[
\left\{\frac14,-\frac14\right\}.
\]

But `F(1/4)>0`. Therefore:

\[
\boxed{
P_J\text{ is a finite union of two-cycles, possibly together with }\{-1/4\}.
}
\]

The present theorem does **not** decide whether

\[
F(-1/4)=0.
\]

Consequently, the parity of `|P_J|` is determined entirely by that single unresolved fixed value: it is even unless `-1/4` is itself a root.

## 7. Relation to the real-rootedness frontier

G002/G003 reduce RH to the statement that all zeros of `F` are real and non-positive. G015 does not prove or disprove that statement.

Even if RH is true, the involution `J(w)=1/(16w)` would merely preserve the negative real axis as a geometric locus. The theorem here shows that it still cannot globally permute the roots of `F`.

Therefore reciprocal quotient symmetry is not a missing requirement for G003 real-rootedness and must not be inserted as one.

## 8. Relation to G014

G014 proves finiteness of paired xi zeros under the induced `s`-plane negative inversion.

G015 is the direct even-quotient counterpart:

\[
\boxed{
\text{projective quotient symmetry}\not\Rightarrow\text{quotient-root symmetry}.
}
\]

The two no-go theorems protect different coordinate layers and jointly prevent a false spectral-invariance shortcut.

## 9. Proof firewall

Proved here:

- `J(w)=1/(16w)` is the exact quotient negative inversion;
- `J` is an involution with fixed values `+/-1/4`;
- `F(0)>0` and `F(1/4)>0` from the previously proved positive coefficients;
- the paired quotient-root set `P_J` is finite;
- the complete root set of `F` is not invariant under `J`;
- all but finitely many `F` roots map to non-roots;
- `P_J` is a finite union of two-cycles and possibly the single fixed root `-1/4`.

Not proved or claimed here:

- `F(-1/4)=0` or `F(-1/4) != 0`;
- real-rootedness of `F`;
- PF-infinity;
- SOH-G003;
- RH.
