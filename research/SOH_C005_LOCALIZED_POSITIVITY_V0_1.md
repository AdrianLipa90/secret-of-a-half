# SOH-C005 Localized Positivity Programme v0.1

Status: **OPEN — proof frontier decomposition**

This note does not claim the Riemann Hypothesis or SOH-C005. It isolates a non-circular route from the localized Weil operators to the global positivity criterion.

## 1. Target

Let

\[
Q_W(f)=\mathcal W[|f|^2]
\]

on the admissible Weil test class, and for \(a>0\) let \(Q_W^a\) denote the localization to \((-a,a)\). Define

\[
\lambda(a)=\inf_{0\neq f\in C_c^\infty(-a,a)}\frac{Q_W^a(f)}{\|f\|_2^2}.
\]

SOH-C005 is the global statement

\[
Q_W(f)\ge 0\qquad\text{for every admissible }f.
\]

Under the standard Weil criterion this is equivalent to RH. Therefore none of the lemmas below may use RH, Li positivity for all orders, global Weil positivity, or a square root of an operator whose positivity has not already been proved independently.

## 2. Exact lemmas already available

### C005-L001 — Nested-domain monotonicity

For \(0<a_1<a_2\),

\[
C_c^\infty(-a_1,a_1)\subset C_c^\infty(-a_2,a_2),
\]

hence

\[
\lambda(a_2)\le \lambda(a_1).
\]

Status: **EXACT**.

### C005-L002 — Termwise prime-weight positivity is insufficient

The single hinge kernel

\[
h_a(t)=(|t|-a)_+,
\qquad
K_a(x,y)=h_a(x-y)-h_a(x)-h_a(y)+h_a(0)
\]

is indefinite. At \(x=a/2\), \(y=3a/2\),

\[
\det\begin{pmatrix}0&-a/2\\-a/2&-a\end{pmatrix}=-a^2/4<0.
\]

Therefore positivity cannot follow termwise from \(\Lambda(n)\ge0\).

Status: **EXACT NO-GO**.

### C005-L003 — Local-to-core reduction

If \(Q_W^a(f)\ge0\) for every \(a>0\) and every \(f\in C_c^\infty(-a,a)\), then \(Q_W(f)\ge0\) on the compactly supported smooth core.

Status: **EXACT once localization agrees with the global form on compact support**. The compatibility identity is a required checked hypothesis, not an implicit assumption.

### C005-L004 — Core-to-global closure

If the compactly supported smooth core is form-dense in the admissible Weil domain and \(Q_W\) is closable with lower-semicontinuous closure, then non-negativity on the core extends to the full admissible domain.

Status: **CONDITIONAL REDUCTION**. Required analytic hypotheses must be proved independently.

## 3. The useful spectral reduction

Because \(\lambda(a)\) is non-increasing, proving a lower bound at arbitrarily large localization scales is enough if it is uniform in the correct sense.

### C005-L005 — Uniform asymptotic lower-bound criterion

If

\[
\liminf_{a\to\infty}\lambda(a)\ge0,
\]

then monotonicity gives

\[
\lambda(a)\ge0\qquad\text{for every }a>0.
\]

Proof: for fixed \(a\), \(\lambda(A)\le\lambda(a)\) for all \(A>a\). Hence

\[
\liminf_{A\to\infty}\lambda(A)\le\lambda(a).
\]

If the left side is non-negative, so is \(\lambda(a)\).

Status: **EXACT**.

This converts the frontier into a uniform lower-bound problem rather than an independent proof at every finite \(a\).

## 4. Finite-section strategy and its missing block

Let \(P_N\) be the projection onto a chosen finite basis section and write schematically

\[
A_a = P_NA_aP_N + P_NA_a(I-P_N) + (I-P_N)A_aP_N + (I-P_N)A_a(I-P_N).
\]

The existing Hermite/prime-tail certificates control finite sections and selected truncation errors. They do **not** by themselves control the infinite complement.

A sufficient non-circular certificate would consist of the following three bounds for a schedule \(N=N(a)\):

1. finite block lower bound
   \[
   P_NA_aP_N\ge \mu_{N,a}P_N;
   \]
2. off-diagonal norm bound
   \[
   \|P_NA_a(I-P_N)\|\le \varepsilon_{N,a};
   \]
3. complement lower bound
   \[
   (I-P_N)A_a(I-P_N)\ge \nu_{N,a}(I-P_N).
   \]

Then the block operator is bounded below by the scalar two-by-two matrix

\[
M_{N,a}=
\begin{pmatrix}
\mu_{N,a}&-\varepsilon_{N,a}\\
-\varepsilon_{N,a}&\nu_{N,a}
\end{pmatrix}.
\]

Therefore a sufficient condition for \(A_a\ge0\) is

\[
\mu_{N,a}\ge0,\qquad \nu_{N,a}\ge0,\qquad
\mu_{N,a}\nu_{N,a}\ge\varepsilon_{N,a}^2.
\]

### C005-L006 — Block positivity criterion

Under the three operator bounds above, the determinant condition

\[
\mu_{N,a}\nu_{N,a}-\varepsilon_{N,a}^2\ge0
\]

and non-negative diagonal bounds imply \(A_a\ge0\).

Status: **EXACT ABSTRACT OPERATOR LEMMA**.

The unresolved issue is now explicit: obtain a **positive lower bound on the infinite complement** and a **uniform off-diagonal bound** from the arithmetic/theta representation without using RH-equivalent input.

## 5. Prime-shift decomposition target

The arithmetic support occurs at shifts \(\pm\log n\). A future exact decomposition should have the form

\[
A_a=A_{\mathrm{arch},a}+A_{\mathrm{prime},a}+A_{\mathrm{bdry},a}+A_{\mathrm{reg},a},
\]

with every normalization derived from the explicit formula or screw-function representation. This line is **not yet a theorem in this note**; it is a bookkeeping target.

The key objective is not termwise positivity. It is a compensated estimate of the form

\[
A_{\mathrm{arch},a}+A_{\mathrm{bdry},a}+A_{\mathrm{reg},a}
\ge -A_{\mathrm{prime},a}
\]

on the complement or, more realistically, a quadratic-form bound sufficient to produce \(\nu_{N,a}\ge0\).

## 6. Minimal closure chain

A complete non-circular proof of SOH-C005 is obtained if all of the following are established independently:

- **C005-P1:** exact localization/global compatibility on compact support;
- **C005-P2:** form closability and core density;
- **C005-P3:** for every sufficiently large \(a\), a schedule \(N(a)\) and certified \(\mu_{N,a},\varepsilon_{N,a},\nu_{N,a}\) satisfying the block positivity criterion;
- **C005-P4:** the resulting lower bound is uniform enough to imply \(\liminf_{a\to\infty}\lambda(a)\ge0\).

Then

\[
\text{P1+P2+P3+P4}
\Longrightarrow
\lambda(a)\ge0\ \forall a
\Longrightarrow
Q_W\ge0
\Longrightarrow
\text{SOH-C005}
\Longrightarrow
\text{RH}
\]

under the standard Weil equivalence.

## 7. Circularity firewall

The following inputs are forbidden in proving P1--P4:

- RH or an equivalent zero-location assumption;
- global Li non-negativity;
- global Weil positivity;
- positivity of \(A_a\) assumed before the lower-bound argument;
- defining a factor \(B_a=A_a^{1/2}\) before positivity is independently established;
- finite numerical PSD presented as proof of the infinite-dimensional complement.

## 8. Current frontier

The immediate theorem target is:

> **C005-TARGET-A.** Derive explicit, unconditional complement and off-diagonal bounds \(\nu_{N,a}\) and \(\varepsilon_{N,a}\) from the prime/theta/screw representation, with a computable schedule \(N(a)\), such that
> \[
> \mu_{N,a}\nu_{N,a}-\varepsilon_{N,a}^2\ge0
> \]
> for all sufficiently large \(a\).

Status: **OPEN**.

This is narrower than SOH-C005 and is the next proof-bearing target.
