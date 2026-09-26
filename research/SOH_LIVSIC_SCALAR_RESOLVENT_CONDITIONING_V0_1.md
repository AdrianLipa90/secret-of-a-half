# SOH Livšic Scalar-Resolvent Conditioning and Direct-Ratio Target v0.1

Status: **EXACT_RESOLVENT_CERTIFICATE / NORM-RESOLVENT_CONDITIONING_NO-GO / DIRECT_PARITY_RATIO_TARGET**

Date: 2026-09-26

Parents:
- \`research/SOH_SUZUKI_LIVSIC_SCHUR_REDUCTION_V0_1.md\`
- \`research/SOH_RELATIVE_METRIC_PENCIL_STABILITY_V0_1.md\`

## 1. Scalar resolvent perturbation

Let \(T=T^*\) and \(\widetilde T=\widetilde T^*\) be positive definite
operators on a common finite-dimensional or bounded-operator model with

\[
T\ge mI,
\qquad
\|T-\widetilde T\|\le\varepsilon<m.
\]

Then

\[
\widetilde T\ge(m-\varepsilon)I.
\]

The resolvent identity gives

\[
T^{-1}-\widetilde T^{-1}
=
T^{-1}(\widetilde T-T)\widetilde T^{-1}.
\]

Therefore

\[
\boxed{
\|T^{-1}-\widetilde T^{-1}\|
\le
\frac{\varepsilon}{m(m-\varepsilon)}.
}
\]

For arbitrary \(f,g\),

\[
\boxed{
\left|
\langle f,T^{-1}g\rangle
-
\langle f,\widetilde T^{-1}g\rangle
\right|
\le
\|f\|\,\|g\|
\frac{\varepsilon}{m(m-\varepsilon)}.
}
\]

This is an exact fail-closed scalar matrix-element certificate.

## 2. Livšic test-vector norms

In the finite interval \([-a,a]\), Suzuki's evaluation vectors use

\[
e_z(x)=e^{-izx}.
\]

For \(z=iy\), \(y>0\),

\[
e_{iy}(x)=e^{yx}
\]

and hence

\[
\boxed{
\|e_{iy}\|_{L^2(-a,a)}^2
=
\int_{-a}^{a}e^{2yx}\,dx
=
\frac{\sinh(2ay)}{y}.
}
\]

For the deficiency vectors \(e_{\pm i}=e^{\pm x}\),

\[
\boxed{
\|e_{\pm i}\|^2
=
\sinh(2a).
}
\]

Therefore the direct norm-resolvent estimate for

\[
M_\pm(a,y)
=
\langle e_{iy},T_a^{-1}e_{\pm i}\rangle
\]

obeys

\[
\boxed{
|\Delta M_\pm|
\le
\sqrt{
\frac{\sinh(2ay)}{y}
\sinh(2a)
}
\,
\frac{\varepsilon_a}
{m_a(m_a-\varepsilon_a)}.
}
\]

For fixed \(y>0\),

\[
\sqrt{
\frac{\sinh(2ay)}{y}
\sinh(2a)
}
=
\Theta_y(e^{a(y+1)}).
\]

Thus a raw operator-norm approximation with bounded spectral gap requires
roughly

\[
\boxed{
\varepsilon_a
=
o(e^{-a(y+1)})
}
\]

to force absolute convergence of each unnormalized scalar matrix element.

This is exponentially stringent.

## 3. Why norm-resolvent convergence is the wrong primary target

The Livšic characteristic quotient on the zero-free axis is

\[
\chi_{a,\lambda}(iy)
=
\frac{1-y}{1+y}
\frac{C_a(y)-S_a(y)}
{C_a(y)+S_a(y)}.
\]

Both \(C_a(y)\) and \(S_a(y)\) are built from exponentially growing test
vectors.

Their common exponential scale may cancel in the ratio.

Therefore proving the two matrix elements separately by the crude operator-norm
bound wastes this cancellation and imposes an artificial exponential
precision requirement.

The correct target is a direct estimate of the normalized ratio.

## 4. Exact ratio perturbation lemma

Let

\[
A=C+S,
\qquad
B=C-S,
\]

and let

\[
\widetilde A=\widetilde C+\widetilde S,
\qquad
\widetilde B=\widetilde C-\widetilde S.
\]

Assume

\[
|A|\ge d>0,
\]

\[
|\widetilde A-A|\le\eta_A<d,
\qquad
|\widetilde B-B|\le\eta_B.
\]

Then

\[
|\widetilde A|
\ge
d-\eta_A.
\]

Moreover,

\[
\frac{\widetilde B}{\widetilde A}
-
\frac BA
=
\frac{
(\widetilde B-B)A
-
B(\widetilde A-A)
}{
A\widetilde A
}.
\]

Hence

\[
\boxed{
\left|
\frac{\widetilde B}{\widetilde A}
-
\frac BA
\right|
\le
\frac{\eta_B}{d-\eta_A}
+
\frac{|B|\,\eta_A}
{d(d-\eta_A)}.
}
\]

If additionally

\[
|B|\le \kappa |A|
\]

for a known \(\kappa\), then

\[
\boxed{
\left|
\frac{\widetilde B}{\widetilde A}
-
\frac BA
\right|
\le
\frac{
\eta_B+\kappa\eta_A
}{
d-\eta_A
}.
}
\]

For the finite Livšic Schur function one has \(|\chi|<1\) in the upper
half-plane, which supplies precisely a natural ratio bound rather than
separate absolute control of \(C\) and \(S\).

## 5. Renormalized parity target

Define a common nonzero scale \(R_a(y)\) and normalized channels

\[
\widehat C_a(y)=\frac{C_a(y)}{R_a(y)},
\qquad
\widehat S_a(y)=\frac{S_a(y)}{R_a(y)}.
\]

Since the Livšic quotient depends only on

\[
\frac{C_a-S_a}{C_a+S_a},
\]

the common scale cancels.

Therefore the proof-bearing target should be:

1. choose \(R_a(y)\) from the arithmetic/Suzuki normalization, not from zero
   data;
2. prove
   \[
   \widehat C_a(y)\to C_\infty(y),
   \qquad
   \widehat S_a(y)\to S_\infty(y)
   \]
   on a zero-free set \(y>1/2\);
3. prove a non-vanishing denominator bound
   \[
   |C_\infty(y)+S_\infty(y)|\ge d(y)>0;
   \]
4. identify
   \[
   \frac{C_\infty-S_\infty}{C_\infty+S_\infty}
   \]
   with the target logarithmic-derivative Cayley transform already derived in
   the Livšic note.

This avoids the exponentially ill-conditioned unnormalized problem.

## 6. Shift schedule remains separate

The scalar target still requires an admissible

\[
\lambda(a)<\lambda_a.
\]

The present theorem does not construct such a schedule.

However it shows that the schedule need only support controlled normalized
scalar ratios; it does not have to provide global norm-resolvent convergence
of the full localized operator.

Thus the remaining Livšic frontier splits into:

### LIV-MD1 — admissible shift schedule
Construct a zero-list-free computable \(\lambda(a)<\lambda_a\).

### LIV-MD2 — direct normalized parity-ratio convergence
Prove the zero-free-axis convergence of
\[
\frac{C_a(y)-S_a(y)}{C_a(y)+S_a(y)}
\]
without separately approximating exponentially large numerator channels.

## 7. Compact result

### Theorem — scalar-resolvent conditioning

If \(T\ge mI\), \(\|T-\widetilde T\|\le\varepsilon<m\), then

\[
\|T^{-1}-\widetilde T^{-1}\|
\le
\frac{\varepsilon}{m(m-\varepsilon)}.
\]

For Suzuki's Livšic test vectors this induces an unnormalized scalar error
prefactor of order

\[
e^{a(y+1)}.
\]

Therefore raw norm-resolvent convergence is an exponentially ill-conditioned
sufficient route to the desired scalar limit.

The natural proof target is instead direct convergence of the scale-free
parity ratio, equipped with the exact ratio perturbation lemma above.

Q.E.D.
