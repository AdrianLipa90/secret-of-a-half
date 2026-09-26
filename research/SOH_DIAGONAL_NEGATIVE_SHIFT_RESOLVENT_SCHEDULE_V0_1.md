# SOH Diagonal Negative-Shift Resolvent Schedule v0.1

Status: **JOINT_SCHEDULE_EXISTENCE_CLOSED / LOCAL_UNIFORM_ZERO_FREE_LIMIT / EFFECTIVE_RATE_OPEN**

Date: 2026-09-26

Parents:
- \`research/SOH_NEGATIVE_SHIFT_RESOLVENT_WEIL_FIRST_CORRECTION_V0_1.md\`
- \`research/SOH_PIECEWISE_EXPONENTIAL_WEIL_CROSS_CONVOLUTION_V0_1.md\`
- \`research/SOH_LIVSIC_CAYLEY_LOG_DERIVATIVE_PRIME_BRIDGE_V0_1.md\`

No RH and no zero list are used.

## 1. Complex zero-free parameter domain

Let

\[
\mathbb H_{1/2}
=
\{z\in\mathbb C:\Im z>1/2\}.
\]

For \(z\in\mathbb H_{1/2}\), put

\[
p(z)=-iz.
\]

Then

\[
\Re p(z)=\Im z>\frac12.
\]

The piecewise-exponential Weil identity extends from real \(p>1/2\) to
complex \(\Re p>1/2\) by absolute/local-uniform convergence and the identity
theorem:

\[
\boxed{
W(F_{1,p(z)})
=
r_0
+
\frac{\xi'(1/2-iz)}
{\xi(1/2-iz)}.
}
\]

The right-hand side is holomorphic on \(\mathbb H_{1/2}\), because

\[
\Re(1/2-iz)>1.
\]

## 2. Complex finite-interval vectors

For fixed \(a>0\), define

\[
v_z^{(a)}(x)
=
e^{-izx}\mathbf1_{[-a,a]}(x),
\]

and

\[
v_1^{(a)}(x)
=
e^x\mathbf1_{[-a,a]}(x).
\]

The overlap

\[
I_a(z)
=
\langle v_z^{(a)},v_1^{(a)}\rangle
=
\int_{-a}^{a}
e^{(1-iz)x}\,dx
\]

is

\[
\boxed{
I_a(z)
=
\frac{
2\sinh((1-iz)a)
}{
1-iz
}.
}
\]

On \(\mathbb H_{1/2}\),

\[
\Re(1-iz)=1+\Im z>\frac32,
\]

so \(I_a(z)\ne0\).

The form-domain cutoff argument from the parent theorem applies locally
uniformly in \(z\) on compact subsets of \(\mathbb H_{1/2}\).

## 3. Finite normalized resolvent first correction

For

\[
\mu>-\lambda_a,
\]

define

\[
\boxed{
\mathcal R_{a,\mu}(z)
=
-\frac{\mu^2}{I_a(z)}
\left[
\left\langle
v_z^{(a)},
(A_a+\mu I)^{-1}
v_1^{(a)}
\right\rangle
-
\frac{I_a(z)}{\mu}
\right].
}
\]

For every fixed \(a\),

\[
\mathcal R_{a,\mu}(z)
\longrightarrow
\frac{
Q_W^a(v_z^{(a)},v_1^{(a)})
}{
I_a(z)
}
\]

as \(\mu\to\infty\).

## 4. Local uniformity in \(z\) for fixed \(a\)

Let \(K\Subset\mathbb H_{1/2}\) be compact.

The map

\[
z\mapsto v_z^{(a)}
\]

is continuous from \(K\) into the localized form Hilbert space. Therefore its
image is compact in that form space.

The spectral multipliers underlying the first-correction theorem are uniformly
bounded on the form Hilbert space and converge strongly to the identity
multiplier that represents \(q_{A_a}\).

Strong convergence of a uniformly bounded operator family is uniform on
compact subsets.

Since

\[
\inf_{z\in K}|I_a(z)|>0,
\]

we obtain

\[
\boxed{
\sup_{z\in K}
\left|
\mathcal R_{a,\mu}(z)
-
\frac{
Q_W^a(v_z^{(a)},v_1^{(a)})
}{
I_a(z)
}
\right|
\to0
}
\]

for every fixed \(a\).

## 5. Local-uniform large-\(a\) form limit

The finite normalized cross-convolution formulas extend holomorphically in
\(p=-iz\) on \(\Re p>1/2\).

On every compact

\[
K\Subset\mathbb H_{1/2},
\]

the exponential majorants used in the real-\(y\) proof may be chosen uniformly
because

\[
\inf_{z\in K}\Im z>\frac12.
\]

Therefore

\[
\boxed{
\sup_{z\in K}
\left|
\frac{
Q_W^a(v_z^{(a)},v_1^{(a)})
}{
I_a(z)
}
-
\left[
r_0+
\frac{\xi'(1/2-iz)}
{\xi(1/2-iz)}
\right]
\right|
\to0
}
\]

as \(a\to\infty\).

## 6. Diagonal schedule theorem

Choose any deterministic sequence

\[
a_n\to\infty.
\]

Let

\[
K_1\subset K_2\subset\cdots
\]

be a compact exhaustion of \(\mathbb H_{1/2}\).

For each \(n\), Section 4 allows us to choose a finite

\[
\mu_n>\max(0,-\lambda_{a_n})
\]

large enough that

\[
\sup_{z\in K_n}
\left|
\mathcal R_{a_n,\mu_n}(z)
-
\frac{
Q_W^{a_n}(v_z^{(a_n)},v_1^{(a_n)})
}{
I_{a_n}(z)
}
\right|
<
\frac1n.
\]

The explicit lower bound on \(\lambda_a\) from the global-shift theorem ensures
that the admissible half-line for \(\mu_n\) is itself known without RH.

Combining with Section 5 gives

\[
\boxed{
\mathcal R_{a_n,\mu_n}(z)
\longrightarrow
r_0+
\frac{\xi'(1/2-iz)}
{\xi(1/2-iz)}
}
\]

locally uniformly on \(\mathbb H_{1/2}\).

Thus a joint large-\(a\), large-negative-shift schedule exists.

## 7. Epistemic boundary: existence is not an effective schedule

The choice of \(\mu_n\) in Section 6 uses the proven convergence but does not
provide an explicit closed formula or computable a priori rate.

Therefore the following are different statements:

### LIV-MD2c4a — joint schedule existence
Status: **CLOSED**.

There exists a zero-list-free admissible diagonal schedule with local-uniform
convergence on \(\mathbb H_{1/2}\).

### LIV-MD2c4b — effective schedule
Status: **OPEN**.

Produce an explicit computable function

\[
\mu(a)
\]

and a certified error bound

\[
E(a,K)\to0
\]

such that

\[
\sup_{z\in K}
\left|
\mathcal R_{a,\mu(a)}(z)
-
r_0-
\frac{\xi'(1/2-iz)}
{\xi(1/2-iz)}
\right|
\le
E(a,K).
\]

This requires quantitative spectral/form-domain information beyond the
qualitative dominated-convergence argument.

## 8. Why this still does not prove RH

The limit in Section 6 is obtained on

\[
\Im z>1/2,
\]

which corresponds to the already zero-free half-plane

\[
\Re s>1.
\]

The renormalized first-correction family is not yet shown to be the same Schur
characteristic family whose finite zeros are all real.

Therefore no zero-attraction theorem across the full upper half-plane follows
from this result alone.

The remaining structural gate is to transport the zero-free resolvent
first-correction information into a characteristic/Schur object while
preserving the finite self-adjoint real-zero constraint.

## 9. Updated frontier

The analytic problem is no longer:

"Does any joint schedule exist?"

It is:

\[
\boxed{
\text{effective joint schedule}
+
\text{Schur/characteristic compatibility of the renormalized correction}.
}
\]

The first component is quantitative.

The second is structural.

## 10. Compact theorem

There exist sequences

\[
a_n\to\infty,
\qquad
\mu_n\to\infty
\]

with \(\mu_n>-\lambda_{a_n}\) such that

\[
\boxed{
-\frac{\mu_n^2}{I_{a_n}(z)}
\left[
\left\langle
v_z^{(a_n)},
(A_{a_n}+\mu_n I)^{-1}
v_1^{(a_n)}
\right\rangle
-
\frac{I_{a_n}(z)}{\mu_n}
\right]
\to
r_0+
\frac{\xi'(1/2-iz)}
{\xi(1/2-iz)}
}
\]

locally uniformly for

\[
\Im z>\frac12.
\]

The schedule exists unconditionally; an effective rate remains open.
