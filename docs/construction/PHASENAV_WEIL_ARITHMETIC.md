# Native PhaseNav–Weil Arithmetic Operator v0.2

## Status

This is the first **prime-side** execution of the PhaseNav–Weil matrix. It is
not a proof of the Riemann Hypothesis and it does not promote `SOH-C005`.

The authoritative profile is:

```text
construction/phasenav/secret_of_half_weil_arithmetic.pnv
```

The arithmetic calculation consumes:

- prime powers through the von Mangoldt function;
- the archimedean gamma factor;
- the conductor term and the two pole evaluations.

It does **not** consume a list of zeta zeros. The declared target ordinate is a
probe centre; the old low-height zero fixture is used only as an independent
normalization cross-check after the arithmetic matrix has been computed.

## 1. Spectral coordinate and channel product

Write

\[
s=\frac12+z,\qquad z=ir.
\]

The centred involution becomes

\[
J_z(z)=-\overline z
\quad\Longleftrightarrow\quad
J_r(r)=\overline r.
\]

For channel centre \(c\), define

\[
\psi_c(r)=
\exp\left[
 ic(r-\gamma_0)
 -\frac{w^2}{2}(r-\gamma_0)^2
\right].
\]

The matrix test function is

\[
H_{ij}(r)=\overline{\psi_{c_i}(\overline r)}\psi_{c_j}(r)
=
\exp\left[
-w^2(r-\gamma_0)^2
+i(c_j-c_i)(r-\gamma_0)
\right].
\]

This function is entire and rapidly decreasing on the real axis.

## 2. Closed Fourier transform

Using

\[
\widehat H(x)=\int_{-\infty}^{\infty}H(r)e^{-2\pi ixr}\,dr,
\]

one obtains exactly

\[
\widehat H_{ij}(x)
=
\frac{\sqrt\pi}{w}
 e^{-2\pi i x\gamma_0}
 \exp\left[
 -\frac{((c_j-c_i)-2\pi x)^2}{4w^2}
 \right].
\]

The executor verifies this identity by direct numerical integration.

## 3. Prime-side explicit formula

For each matrix entry, the implemented normalization is

\[
\sum_\rho H_{ij}\!\left(\frac{\rho-1/2}{i}\right)
=
H_{ij}\!\left(\frac{1}{2i}\right)
+H_{ij}\!\left(-\frac{1}{2i}\right)
-\frac{\log\pi}{2\pi}\widehat H_{ij}(0)
\]

\[
\quad+
\frac{1}{2\pi}\int_{-\infty}^{\infty}
H_{ij}(r)
\operatorname{Re}\psi\!\left(\frac14+\frac{ir}{2}\right)dr
-
\frac{1}{2\pi}\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}
\left[
\widehat H_{ij}\!\left(\frac{\log n}{2\pi}\right)
+
\widehat H_{ij}\!\left(-\frac{\log n}{2\pi}\right)
\right].
\]

The four terms are stored separately in the receipt. The exact formula is
classical; the finite prime cutoff and numerical archimedean integral are
numerical approximations.

## 4. Deterministic receipt

The profile uses

\[
\gamma_0=14.134725141734695,
\quad w=0.8,
\quad c_\pm=\pm\frac{\pi}{\gamma_0}.
\]

The arithmetic matrix at the audit cutoff is approximately

\[
W_{\mathrm{arith}}
\approx
\begin{pmatrix}
1.000000000000065 & 0.999999999999935+4.7\times10^{-15}i\\
0.999999999999935-4.7\times10^{-15}i & 1.000000000000065
\end{pmatrix}.
\]

Its eigenvalues are approximately

\[
\lambda_{\min}=1.30\times10^{-13},
\qquad
\lambda_{\max}=2.000000000000000.
\]

The result has three checks:

1. the \(10^4\) and \(10^5\) prime cutoffs agree within the declared tolerance;
2. the sampled arithmetic matrix is positive semidefinite to numerical error;
3. the prime-side result matches the previous low-height spectral receipt.

The third check validates normalization. It does not turn the spectral fixture
into an input of the arithmetic computation.

## 5. What this advances

Version 0.1 showed that a synthetic off-axis quartet generates a negative
finite witness. Version 0.2 evaluates the corresponding on-axis localized
matrix from arithmetic data rather than from a zero list.

This closes the first executable loop

\[
\text{primes}
\longrightarrow
\text{explicit formula}
\longrightarrow
\text{PhaseNav Hermitian matrix}
\longrightarrow
\text{spectral receipt}.
\]

## 6. What remains open

`SOH-C005` still requires:

1. a dense admissible PhaseNav test-channel family;
2. controlled removal of all prime and integration cutoffs;
3. positivity for every channel combination, not one localized sample;
4. a proof that the null structure forces the native theta-shell closure;
5. verification that no equivalent form of RH has merely been assumed.

## 7. Claim boundary

- `SOH-L012`: the Gaussian matrix test has the stated closed Fourier transform.
- `SOH-N003`: the prime-side arithmetic matrix is cutoff-stable and matches the
  low-height spectral receipt for the declared profile.
- `SOH-C005`: remains open.

One positive arithmetic sample is a successful bridge validation, not a proof
of global positivity.
