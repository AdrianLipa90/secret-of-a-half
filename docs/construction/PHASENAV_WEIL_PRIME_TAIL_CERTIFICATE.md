# PhaseNav–Weil Prime-Tail Certificate v0.5

## Scope

This module certifies the omitted prime-power tail of each fixed finite
Hermite principal section of the arithmetic PhaseNav–Weil operator.

It does **not** map zeta zeros. It does **not** establish global positivity or
prove the Riemann Hypothesis.

## Tail coordinate

For the omitted range \(x>Q\), use

\[
u=\log x,
\qquad
z_{\rm t}=\frac1u.
\]

The logarithmic half-line \(u\in[\log Q,\infty)\) becomes the compact interval

\[
z_{\rm t}\in\left(0,\frac1{\log Q}\right].
\]

After the substitution, the degree-\(d\) majorant density is

\[
\frac1{w^d}
z_{\rm t}^{-(d+3)}
\exp\!\left(
-\frac1{4w^2z_{\rm t}^2}
+\frac1{2z_{\rm t}}
\right).
\]

It extends by zero to a smooth flat endpoint at \(z_{\rm t}=0\).

## Monotonicity threshold

For

\[
g_d(x)=x^{-1/2}(\log x)^{d+1}
\exp\!\left[-\frac{(\log x)^2}{4w^2}\right],
\]

the integral test is valid once

\[
\log Q\ge
\tau_d(w)
=
\frac{\sqrt{w^4+8w^2(d+1)}-w^2}{2}.
\]

The declared profile has positive margin for every degree through \(10\).

## Closed integral

Define

\[
I_d(Q,w)=
\frac1{w^d}
\int_Q^\infty
(\log x)^{d+1}x^{-1/2}
e^{-(\log x)^2/(4w^2)}\,dx.
\]

With

\[
a_Q=\frac{\log Q-w^2}{2w},
\]

the exact upper-incomplete-gamma representation is

\[
I_d(Q,w)=
\frac{e^{w^2/4}}{w^d}
\sum_{j=0}^{d+1}
\binom{d+1}{j}
w^{2(d+1-j)}
2^j w^{j+1}
\Gamma\!\left(\frac{j+1}{2},a_Q^2\right).
\]

The executor verifies this expression independently against direct
\(u=\log x\) quadrature and compact \(z_{\rm t}=1/u\) quadrature.

## Entrywise bound

For the Hermite product-kernel coefficients \(c_{mn,d}\) and prefactor
\(A_{mn}\),

\[
|E_{mn}(Q)|
\le
B_{mn}(Q)
=
\frac{A_{mn}}{\pi}
\sum_d c_{mn,d}I_d(Q,w).
\]

The proof uses only:

1. \(\Lambda(n)\le\log n\);
2. replacement of prime-power support by all integers;
3. the explicit monotonicity threshold;
4. the integral test.

No prime number theorem or zero-free hypothesis is used.

## Finite-section operator norm

For the \(N\times N\) tail matrix,

\[
\|E_N(Q)\|_2
\le
\max_m\sum_{n=0}^{N-1}B_{mn}(Q).
\]

Weyl perturbation then gives the same bound on the displacement of every
ordered eigenvalue between the finite-cutoff and infinite-cutoff matrices.

## Declared receipt

For

\[
w=0.8,
\qquad
Q=100000,
\qquad
N\le6,
\]

the largest certified operator-norm envelope is

\[
\boxed{
7.717202888999335\times10^{-13}
}.
\]

The deterministic receipt also checks selected finite prime-power shells
between \(Q\) and \(2Q\) against the complete analytic majorant.

## Claim boundary

Exact:

- reciprocal compactification identity;
- flat endpoint extension;
- incomplete-gamma formula;
- entrywise von Mangoldt majorant;
- fixed finite-section norm and eigenvalue enclosure.

Numerical:

- high-precision receipt for the declared \(w,Q,N\);
- finite-shell regression checks.

Open:

- a useful estimate uniform as \(N\to\infty\);
- positivity of all infinite-cutoff sections;
- closure of the full arithmetic form;
- the null-space implication to native PhaseNav closure;
- `SOH-C005`.

The authoritative source is
`construction/phasenav/secret_of_half_weil_prime_tail_certificate.pnv`.
