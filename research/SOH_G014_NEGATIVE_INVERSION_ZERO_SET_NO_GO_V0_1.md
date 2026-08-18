# SOH-G014 — Negative-Inversion Zero-Set No-Go

## Status

**THEOREM-LEVEL NO-GO / PROVED.**

This note proves that the canonical negative inversion from SOH-L017/G012 cannot be a global symmetry of the Riemann xi zero set. In fact, only finitely many xi zeros can be paired with another xi zero by this map. The proof is unconditional and does not assume RH.

## 1. Canonical map in the s-plane

Let

\[
u=\Omega(s)=\frac{s}{1-s}
\]

and let the canonical negative inversion be

\[
N_u(u)=-\frac1u.
\]

Conjugating back to the `s`-plane gives

\[
\boxed{N_s(s)=\frac{s-1}{2s-1}}.
\]

This is a Möbius involution on the Riemann sphere. Its affine pole is `s=1/2`, with the projective exchange

\[
\frac12\longleftrightarrow\infty.
\]

The exact defect from the half is

\[
\boxed{
N_s(s)-\frac12=-\frac1{4s-2}.
}
\]

Therefore

\[
|s|\to\infty
\quad\Longrightarrow\quad
N_s(s)\to\frac12.
\]

## 2. Critical-line height contraction

For

\[
s=\frac12+it,
\qquad t\ne0,
\]

a direct substitution gives

\[
\boxed{
N_s\!\left(\frac12+it\right)
=\frac12+\frac{i}{4t}.
}
\]

Thus negative inversion preserves the critical line as a geometric locus but exchanges large height with small reciprocal height.

Its affine fixed points are

\[
\boxed{s=\frac12\pm\frac{i}{2}},
\]

as already proved in G012.

## 3. Positive value at the accumulation target

The positive Riemann-kernel result proved earlier in this programme gives

\[
\xi\!\left(\frac12\right)
=\int_0^\infty \Phi(y)\,dy>0.
\]

Hence

\[
\boxed{\xi(1/2)\ne0}.
\]

No hypothesis about the location of the remaining zeros is used here.

## 4. The paired-zero set

Let

\[
Z_\xi=\{\rho\in\mathbb C:\xi(\rho)=0\}
\]

and define

\[
P_N
=\{\rho\in Z_\xi:\xi(N_s(\rho))=0\}.
\]

Because `xi(1/2) != 0`, the affine pole of `N_s` is not itself an xi zero, so `N_s(rho)` is defined for every `rho in Z_xi`.

## 5. Main no-go theorem

### Theorem

\[
\boxed{P_N\text{ is finite}.}
\]

### Proof

Assume for contradiction that `P_N` is infinite.

The completed Riemann xi function is a non-zero entire function, so its zeros are isolated. Therefore any infinite subset of its zero set is unbounded. We may choose distinct

\[
\rho_n\in P_N,
\qquad
|\rho_n|\to\infty.
\]

By definition of `P_N`,

\[
\xi(N_s(\rho_n))=0
\]

for every `n`.

But the exact half-defect identity gives

\[
N_s(\rho_n)
=\frac12-\frac1{4\rho_n-2}
\longrightarrow\frac12.
\]

Continuity of the entire function `xi` therefore implies

\[
\xi\!\left(\frac12\right)
=\lim_{n\to\infty}\xi(N_s(\rho_n))
=0,
\]

contradicting the already-proved positivity

\[
\xi(1/2)>0.
\]

Hence `P_N` is finite. QED.

## 6. Immediate corollaries

The xi zero set is infinite; unconditionally, Hardy's theorem already gives infinitely many zeros on the critical line. Therefore finiteness of `P_N` implies:

\[
\boxed{N_s(Z_\xi)\ne Z_\xi}.
\]

More strongly,

\[
\boxed{
\text{all but finitely many xi zeros are sent to non-zeros of xi.}
}
\]

Thus negative inversion is a canonical coordinate/operator symmetry of the SOH geometry, but it is not a global spectral symmetry of the xi zero set.

## 7. Relation to G012 and G013

G012 proves the exact factorization

\[
N_u=R_uE_u=E_uR_u=-1/u
\]

and the projective Klein group `V4`.

G013 lifts that operator algebra to the quaternion subgroup `Q8` of `SU(2)`.

G014 establishes the necessary firewall between that exact geometry and the xi spectrum:

\[
\boxed{
\text{operator symmetry}\not\Rightarrow\text{xi-zero-set symmetry}.
}
\]

The operator algebra remains exact. The rejected statement is only the stronger and false claim that the complete xi zero set is invariant under the negative-inversion operator.

## 8. Numerical regression versus proof

The accompanying tests and receipt evaluate the first few nontrivial zeros and confirm that their images lie near `1/2` and are numerically far from xi zeros. Those calculations are diagnostics only.

The theorem above is analytic and uses only:

1. the exact Möbius formula for `N_s`;
2. analyticity/non-triviality of `xi`;
3. the previously proved positive value `xi(1/2)>0`;
4. infinitude of the xi zero set for the corollary that infinitely many zeros fail to pair.

## 9. Proof firewall

Proved here:

- `N_s(s)=(s-1)/(2s-1)`;
- `N_s(s)-1/2=-1/(4s-2)`;
- `N_s(1/2+it)=1/2+i/(4t)`;
- the paired-zero set `P_N` is finite;
- the complete xi zero set is not invariant under `N_s`;
- all but finitely many xi zeros are mapped to non-zeros of xi.

Not proved or claimed here:

- RH;
- SOH-G003 real-rootedness;
- PF-infinity;
- absence of every possible isolated paired zero under `N_s`;
- any new functional equation for xi;
- any spectral invariance under the Euler half-turn or negative inversion.

## References already present in the monograph bibliography

- G. H. Hardy (1914), *Sur les zeros de la fonction zeta(s) de Riemann*.
- E. C. Titchmarsh, revised by D. R. Heath-Brown (1986), *The Theory of the Riemann Zeta-Function*.
