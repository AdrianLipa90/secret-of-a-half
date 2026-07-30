# Native PhaseNav–Weil Hermite Ladder v0.3

## Status

This construction advances `SOH-C005` by replacing a single two-channel Gaussian
sample with an explicit ladder of finite principal sections drawn from a dense
admissible core. It is not a proof of the Riemann Hypothesis.

The authoritative source is:

```text
construction/phasenav/secret_of_half_weil_hermite_ladder.pnv
```

The implementation parses and audits that source. It does not redefine it.

## 1. Hermite–PhaseNav channels

Fix a width `w>0` and a real target ordinate `gamma`. With physicists' Hermite
polynomials `H_n`, define

\[
\psi_n(r)=
\left(\frac{w}{\sqrt\pi\,2^n n!}\right)^{1/2}
H_n(w(r-\gamma))
\exp\!\left[-\frac{w^2(r-\gamma)^2}{2}\right].
\]

Translation and positive scaling are automorphisms of Schwartz space. The
ordinary Hermite functions form a topological basis of `S(R)`, hence the finite
spans of the channels above form an explicit dense core.

This is the first exact reduction achieved in v0.3: the phrase "dense admissible
family" is no longer left as an unspecified search target.

## 2. Matrix kernels and closed transform

For orders `m,n`, use

\[
H_{mn}(r)=\overline{\psi_m(\overline r)}\psi_n(r).
\]

The product identity

\[
H_m(y)H_n(y)=
\sum_{k=0}^{\min(m,n)}
2^k k!\binom{m}{k}\binom{n}{k}
H_{m+n-2k}(y)
\]

and the Gaussian-Hermite transform give an exact finite formula for
`widehat H_mn(x)`. At `x=0` it reduces to

\[
\widehat H_{mn}(0)=\delta_{mn},
\]

which is also a normalization regression.

## 3. Prime-side principal ladder

The Guinand–Weil formula is applied entrywise to build

\[
W_N=(\mathcal W[H_{mn}])_{m,n=0}^{N-1},
\qquad N=1,\ldots,N_{\max}.
\]

Each entry is decomposed into pole, conductor, archimedean and prime-power
contributions. The arithmetic evaluation consumes no zero list.

The v0.3 receipt records for every `N`:

- the Hermitian matrix;
- minimum and maximum eigenvalue;
- prime-cutoff change;
- operator norms of all four components;
- sampled positive-semidefiniteness.

## 4. Exact dense-core reduction

For a coefficient vector `a` supported in the first `N` channels,

\[
a^*W_Na=\mathcal W\!\left[\left|\sum_{n<N}a_n\psi_n\right|^2\right].
\]

Therefore positivity of every principal matrix is exactly positivity on every
finite Hermite span. If the arithmetic Weil form is continuous in the declared
Schwartz topology, positivity extends from the dense union of these spans to
all admissible Schwartz channels.

This is a reduction theorem, not the missing positivity proof.

## 5. Remaining gap

The following tasks remain open:

1. prove positive semidefiniteness for every `N`, not only the computed ladder;
2. remove the prime and quadrature cutoffs with uniform error bounds;
3. establish continuity of the fully regularized arithmetic form on the chosen
   Schwartz topology;
4. identify the null space and prove that it forces native theta-shell closure;
5. verify that the argument does not assume an equivalent form of RH.

## 6. Claim promotion proposal

- `SOH-L013` — exact: translated-scaled Hermite PhaseNav channels have dense
  finite span in Schwartz space.
- `SOH-L014` — exact: the matrix kernel has the stated closed Fourier transform
  and `widehat H_mn(0)=delta_mn`.
- `SOH-T004` — conditional reduction: positivity of every finite Hermite
  principal matrix plus continuity implies positivity on the dense admissible
  core.
- `SOH-N004` — numerical: finite sections through the declared `N_max` are
  tested at two finite prime cutoffs.
- `SOH-C005` remains open.

## 7. Independent falsification validation

The arithmetic sum remains zero-list free. Separately, the same six-channel
ladder is evaluated on a low-height spectral control and on a declared synthetic
quartet at

\[
\operatorname{Re}s=\frac12\pm0.1.
\]

The on-axis control is positive semidefinite to roundoff, while the off-axis
quartet produces a stable negative mode. This is a sensitivity test only; it is
not an arithmetic input and it is not evidence that actual off-axis zeros exist.
