# Native PhaseNav–Weil Prime-Tail Certificate v0.5

## Status

This construction replaces a purely empirical prime-cutoff comparison by an
explicit analytic majorant for every fixed finite Hermite section. It does not
prove global PhaseNav–Weil positivity and does not prove the Riemann
Hypothesis.

The authoritative profile is:

```text
construction/phasenav/secret_of_half_weil_prime_tail_certificate.pnv
```

The reciprocal map is applied to the logarithmic tail coordinate. It is not a
map of zeta zeros.

## 1. Omitted prime-power tail

For Hermite orders `m,n`, let

\[
R_{mn}(Q)=-\frac1{2\pi}\sum_{q>Q}\frac{\Lambda(q)}{\sqrt q}
\left[
\widehat H_{mn}\!\left(\frac{\log q}{2\pi}\right)+
\widehat H_{mn}\!\left(-\frac{\log q}{2\pi}\right)
\right].
\]

Writing

\[
d_k=m+n-2k,\qquad
c_k=2^k k!\binom mk\binom nk,
\]

and

\[
A_{mn}=\frac1{\sqrt{2^{m+n}m!n!}},
\]

the closed Hermite Fourier transform gives

\[
\left|\widehat H_{mn}(\pm x)\right|
\le
A_{mn}e^{-\kappa^2/4}\sum_k c_k\kappa^{d_k},
\qquad
\kappa=\frac{2\pi |x|}{w}.
\]

Since `Lambda(q) <= log(q)`, prime powers can be majorized by all integers.
For each degree `d`, the resulting positive summand is decreasing once

\[
\log Q\ge
\tau_d(w)=\frac{\sqrt{w^4+8w^2(d+1)}-w^2}{2}.
\]

Therefore

\[
|R_{mn}(Q)|\le
\frac{A_{mn}}{\pi}\sum_k c_k J_{d_k}(Q,w),
\]

where

\[
J_d(Q,w)=\frac1{w^d}\int_Q^\infty
(\log x)^{d+1}x^{-1/2}
\exp\!\left[-\frac{(\log x)^2}{4w^2}\right]dx.
\]

## 2. Reciprocal compactification

Set

\[
u=\log x,\qquad z_{\rm t}=\frac1u.
\]

Then the infinite half-line is mapped to the compact interval

\[
[\log Q,\infty)\longrightarrow
\left(0,\frac1{\log Q}\right],
\]

and

\[
J_d(Q,w)=\frac1{w^d}
\int_0^{1/\log Q}
z_{\rm t}^{-(d+3)}
\exp\!\left[-\frac1{4w^2z_{\rm t}^2}+\frac1{2z_{\rm t}}\right]
dz_{\rm t}.
\]

The integrand extends to `z_t=0` with value zero and is flat there. The
Gaussian `exp(-const/z_t^2)` dominates every algebraic factor.

## 3. Closed incomplete-gamma expression

Completing the square in the log coordinate and expanding the shifted integer
power gives

\[
\begin{aligned}
J_d(Q,w)
={}&\frac{e^{w^2/4}}{w^d}
\sum_{j=0}^{d+1}
\binom{d+1}{j}w^{2(d+1-j)}2^jw^{j+1}\\
&\times
\Gamma\!\left(
\frac{j+1}{2},
\left(\frac{\log Q-w^2}{2w}\right)^2
\right).
\end{aligned}
\]

The implementation verifies equality of the log-half-line, reciprocal-compact,
and gamma representations at high precision.

## 4. Matrix certificate

Let `B_N(Q)` be the symmetric matrix of entrywise bounds. If `E_N(Q)` is the
omitted prime-tail matrix, then

\[
\|E_N(Q)\|_2
\le \sqrt{\|E_N(Q)\|_1\|E_N(Q)\|_\infty}
\le \max_m\sum_n B_{mn}(Q).
\]

Consequently, Weyl's inequality gives

\[
\lambda_{\min}(W_N^{(\infty)})
\ge
\lambda_{\min}(W_N^{(Q)})-\|E_N(Q)\|_2.
\]

This is a controlled cutoff-removal statement for each fixed finite section.
Uniform control as `N -> infinity` remains open.

## 5. Deterministic receipt

For `w=0.8`, `Q=100000`, and `N<=6`:

| N | max entry bound | operator-norm bound |
|---:|---:|---:|
| 1 | 4.4511e-21 | 4.4511e-21 |
| 2 | 4.7479e-19 | 5.2054e-19 |
| 3 | 2.5805e-17 | 2.9621e-17 |
| 4 | 9.5233e-16 | 1.1312e-15 |
| 5 | 2.6835e-14 | 3.2804e-14 |
| 6 | 6.1560e-13 | 7.7172e-13 |

The finite shell `100000 < q <= 200000` is independently checked for entries
`(0,0)`, `(2,3)`, and `(5,5)` and lies below the corresponding full-tail
majorant.

## 6. Claim boundary

Exact:

- reciprocal compactification of the log tail;
- flat extension at the reciprocal endpoint;
- incomplete-gamma identity;
- entrywise von-Mangoldt majorant;
- finite-section operator-norm envelope and Weyl enclosure.

Numerical:

- high-precision evaluation for the declared `N<=6`, `Q=100000` profile;
- finite shell regression checks.

Open:

- a useful bound uniform in basis size;
- global positivity of every Hermite section;
- continuity of the complete regularized form;
- the null-space implication to native theta-shell closure.
