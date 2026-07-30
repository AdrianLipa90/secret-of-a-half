# Native PhaseNav–Weil Positivity Operator v0.1

## Status

This is an executable finite witness construction aimed at the open bridge
`SOH-C004`. It is **not a proof of the Riemann Hypothesis**.

The authoritative execution profile is:

```text
construction/phasenav/secret_of_half_weil_operator.pnv
```

The Python module parses and audits that source. It is not the source of truth.

## 1. Centered PhaseNav channels

Write

\[
s=\frac12+z,\qquad J_z(z)=-\overline z.
\]

For a log-coordinate test channel \(h(u)\), define

\[
\Phi_h(z)=\int_{\mathbb R}h(u)e^{zu}\,du.
\]

The decomposition

\[
e^{zu}=e^{\delta u}e^{itu}
\]

has the native PhaseNav interpretation:

- \(t=\Im z\): phase transport;
- \(\delta=\Re z\): radial gain shear;
- \(J_z\): centered swap-conjugate involution.

## 2. Involution-coupled matrix

For a finite channel family \(h_1,\ldots,h_m\), set

\[
V(z)=\bigl(\Phi_{h_1}(z),\ldots,\Phi_{h_m}(z)\bigr)^T
\]

and define

\[
(W_m)_{ij}
=
\sum_{\rho}
\overline{\Phi_{h_i}(J_z z_\rho)}
\,\Phi_{h_j}(z_\rho),
\qquad
z_\rho=\rho-\frac12.
\]

For an involution-fixed fixture, \(J_z z_\rho=z_\rho\), hence

\[
W_m=\sum_\rho V(z_\rho)V(z_\rho)^\ast\succeq0.
\]

That finite Gram reduction is exact. Extending it to the complete arithmetic
Weil form with the correct admissible test class and regularization is open.

## 3. Two-channel Gaussian profile

The v0.1 executor uses two Gaussian channels localized around \(u=\pm a\) and
modulated at the first zero ordinate \(\gamma_0\):

\[
\Phi_\pm(z)
=
\exp\left[
\pm a(z-i\gamma_0)
+\frac{w^2}{2}(z-i\gamma_0)^2
\right],
\qquad
a=\frac{\pi}{\gamma_0}.
\]

The native profile declares:

\[
\gamma_0=14.134725141734695,\qquad
w=0.8,\qquad
\delta_{\mathrm{synthetic}}=0.1.
\]

## 4. Receipt

The control fixture uses the first ten on-axis ordinates. The synthetic fixture
replaces the first conjugate pair by the symmetric quartet

\[
z=\pm0.1\pm i\gamma_0.
\]

Expected deterministic output:

```text
on_axis_control:
  lambda_min =  1.304512053935e-13
  lambda_max =  2.000000000000e+00

synthetic_off_axis:
  lambda_min = -1.989005564501e-03
  lambda_max =  4.027671100607e+00
```

Thus the finite control is positive semidefinite to roundoff, while the declared
synthetic radial shear produces a stable negative eigenvalue.

## 5. Claim boundary

### Exact

- centered involution \(J_z(z)=-\overline z\);
- the native channel-transform definition;
- Gram reduction and positive semidefiniteness for an involution-fixed finite
  fixture.

### Numerical

- the declared two-channel Gaussian profile;
- the low-height on-axis control;
- the negative synthetic off-axis witness.

### Open

- construction of the complete prime-side arithmetic operator;
- admissible dense test-channel family and regularization;
- proof that arithmetic positivity forces native theta-shell closure;
- proof of `SOH-C004` without assuming an equivalent statement in disguise.

## 6. Promotion target

The next target is `SOH-C005`:

> The complete arithmetic PhaseNav–Weil operator is positive on a dense
> admissible channel family, and its null structure forces detector-zero states
> into the canonical self-dual PhaseNav shell.

Until that statement is proved, the result remains a falsification-sensitive
numerical construction.
