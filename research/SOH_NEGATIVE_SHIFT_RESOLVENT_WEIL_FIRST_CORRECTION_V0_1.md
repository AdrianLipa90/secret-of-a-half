# SOH Negative-Shift Resolvent First-Correction / Weil-Form Bridge v0.1

Status: **EXACT_FORM_DOMAIN_BINDING / EXACT_FIXED-a_RESOLVENT_FIRST_CORRECTION / ITERATED_PRIME_TARGET_CLOSED / JOINT_SCHEDULE_OPEN**

Date: 2026-09-26

Parents:
- \`research/SOH_PIECEWISE_EXPONENTIAL_WEIL_CROSS_CONVOLUTION_V0_1.md\`
- \`research/SOH_EXPLICIT_GLOBAL_LIVSIC_SHIFT_V0_1.md\`
- \`research/SOH_LIVSIC_NEAR_ZERO_SHIFT_NOGO_V0_1.md\`

Primary source:
- M. Suzuki, *Weil's quadratic form via the screw function*,
  arXiv:2606.09096v3, Sections 1.1 and 3.1.

No RH and no zero list are used.

## 1. Form-domain status of finite-interval exponentials

Fix \(a>0\) and real \(p\). Define

\[
v_p^{(a)}(x)
=
e^{px}\mathbf1_{[-a,a]}(x).
\]

Suzuki defines the closed localized Weil-form domain by

\[
\mathfrak D(Q_W^a)
=
\left\{
v\in L^2(-a,a):
|Q_W^a(v)|<\infty
\right\}.
\]

The source also proves form-core density by cutting finite-interval Fourier
vectors off in boundary layers and estimating the Fourier transform of the
boundary error by the pair of bounds

\[
|\widehat w_\varepsilon(z)|
\ll_a
\varepsilon,
\qquad
|\widehat w_\varepsilon(z)|
\ll_a
|z|^{-1}.
\]

The same proof applies to every fixed smooth function on the closed interval,
in particular \(e^{px}\):

- on the boundary layers of total length \(2\varepsilon\),
  \[
  |e^{px}|\le e^{|p|a};
  \]
- the \(L^1\) norm of the derivative of the cutoff error is bounded uniformly
  in \(\varepsilon\) for fixed \(a,p\);
- hence the same low-frequency \(O(\varepsilon)\) and high-frequency
  \(O(|z|^{-1})\) Fourier bounds hold.

Therefore

\[
\boxed{
v_p^{(a)}\in\mathfrak D(Q_W^a)
}
\]

for every fixed \(a>0\) and real \(p\).

Moreover, if \(v_{p,\varepsilon}^{(a)}\in C_c^\infty(-a,a)\) are the cutoff
approximants, then

\[
v_{p,\varepsilon}^{(a)}
\to
v_p^{(a)}
\]

in the form norm.

## 2. Cross-form identity

For compactly supported smooth inputs Suzuki uses

\[
Q_W(v_1,v_2)
=
W(v_1*\widetilde v_2).
\]

Passing to the form-norm limit of the cutoff approximants gives, for the sharp
finite-interval exponentials,

\[
\boxed{
Q_W^a(v_p^{(a)},v_q^{(a)})
=
W\!\left(
v_p^{(a)}*\widetilde v_q^{(a)}
\right).
}
\]

Thus the normalized cross-convolution theorem is genuinely a statement about
the closed localized Weil form.

It is **not** yet a statement that \(v_p^{(a)}\in\mathfrak D(A_a)\); that
stronger operator-domain claim is unnecessary below.

## 3. Abstract semibounded resolvent theorem

Let \(A=A^*\) be bounded from below and let \(q_A\) be its closed quadratic
form.

For

\[
f,g\in\mathfrak D(q_A)
\]

and

\[
\mu>-\inf\sigma(A),
\]

define

\[
R_\mu=(A+\mu I)^{-1}.
\]

Then

\[
\boxed{
\lim_{\mu\to\infty}
\mu^2
\left[
\langle f,R_\mu g\rangle
-
\frac{\langle f,g\rangle}{\mu}
\right]
=
-q_A(f,g).
}
\]

### Proof

For \(f=g\), let \(d\nu_f(\lambda)\) be the spectral measure of \(A\). Then

\[
\mu^2
\left[
\langle f,R_\mu f\rangle
-
\frac{\|f\|^2}{\mu}
\right]
=
-\int
\frac{\mu\lambda}{\mu+\lambda}
\,d\nu_f(\lambda).
\]

Because \(A\) is semibounded, the negative spectral part lies in a bounded
interval. On the positive part,

\[
0\le
\frac{\mu\lambda}{\mu+\lambda}
\le
\lambda.
\]

Membership in the form domain is exactly sufficient for integrability of the
positive first spectral moment, while the negative first moment is finite by
semiboundedness.

Dominated convergence therefore gives

\[
-\int\lambda\,d\nu_f(\lambda)
=
-q_A[f].
\]

The sesquilinear statement follows by polarization. Q.E.D.

## 4. Application to the localized Weil operator

Take

\[
A=A_a,
\qquad
f=v_y^{(a)},
\qquad
g=v_1^{(a)},
\qquad
y>\frac12.
\]

Let

\[
I_a(y)
=
\langle v_y^{(a)},v_1^{(a)}\rangle
=
\frac{2\sinh((y+1)a)}{y+1}.
\]

Then

\[
\boxed{
-\lim_{\mu\to\infty}
\frac{\mu^2}{I_a(y)}
\left[
\left\langle
v_y^{(a)},
(A_a+\mu I)^{-1}
v_1^{(a)}
\right\rangle
-
\frac{I_a(y)}{\mu}
\right]
=
\frac{
Q_W^a(v_y^{(a)},v_1^{(a)})
}{
I_a(y)
}.
}
\]

By the exact cross-form identity,

\[
\frac{
Q_W^a(v_y^{(a)},v_1^{(a)})
}{
I_a(y)
}
=
W(f_{a,y}),
\]

where \(f_{a,y}\) is the normalized finite cross-convolution from the parent
theorem.

## 5. Iterated zero-free prime target

The parent theorem proves

\[
W(f_{a,y})
\longrightarrow
r_0+r(s),
\]

where

\[
s=\frac12+y>1,
\]

\[
r_0=\frac{\xi'(3/2)}{\xi(3/2)},
\qquad
r(s)=\frac{\xi'(s)}{\xi(s)}.
\]

Therefore

\[
\boxed{
\lim_{a\to\infty}
\lim_{\mu\to\infty}
\left\{
-\frac{\mu^2}{I_a(y)}
\left[
\left\langle
v_y^{(a)},
(A_a+\mu I)^{-1}
v_1^{(a)}
\right\rangle
-
\frac{I_a(y)}{\mu}
\right]
\right\}
=
r_0+r(s).
}
\]

This is a zero-list-free resolvent realization of the same scalar combination
that appears in the denominator of Suzuki's infinite characteristic object.

## 6. Prime-side form of the limit

For \(s>1\),

\[
r(s)
=
\frac1s+\frac1{s-1}
-\frac12\log\pi
+\frac12\psi(s/2)
-
\sum_{n\ge2}\frac{\Lambda(n)}{n^s}.
\]

Thus the iterated resolvent first correction is explicitly arithmetic on the
zero-free half-plane.

At each finite \(a\), the cross form contains prime powers only through

\[
n\le e^{2a}.
\]

The missing infinite prime tail has the already-proved exponentially decaying
bound on \(s\ge1+\eta\).

## 7. Why this avoids the near-zero-shift no-go

The resolvent parameter here is

\[
\lambda=-\mu,
\qquad
\mu\to+\infty.
\]

It never approaches the RH-hard value \(\lambda=0\).

The free leading term

\[
\frac{\langle f,g\rangle}{\mu}
\]

is subtracted explicitly.

The arithmetic information lives in the first renormalized correction

\[
-\mu^2
\left[
\langle f,R_\mu g\rangle
-
\frac{\langle f,g\rangle}{\mu}
\right].
\]

Thus the large-negative-shift free-limit no-go is not discarded; it is
resolved by extracting the next asymptotic coefficient rather than pretending
the leading free term is the zeta target.

## 8. What remains open

The theorem is exact for the iterated limit

\[
\mu\to\infty
\quad\text{first, then}\quad
a\to\infty.
\]

The proof programme needs one computable joint schedule

\[
\mu=\mu(a)\to\infty
\]

such that

\[
\boxed{
-\frac{\mu(a)^2}{I_a(y)}
\left[
\left\langle
v_y^{(a)},
(A_a+\mu(a)I)^{-1}
v_1^{(a)}
\right\rangle
-
\frac{I_a(y)}{\mu(a)}
\right]
-
W(f_{a,y})
\to0
}
\]

uniformly on a zero-free accumulation set \(y>1/2\), preferably on compact
\(y\)-intervals.

This requires a quantitative remainder for the resolvent first-correction
expansion that is controlled jointly in \(a\).

## 9. Updated Livšic gates

### LIV-MD2c1
Finite Weil scalar \(\to\) finite prime target:
**CLOSED**.

### LIV-MD2c2
Sharp finite exponential \(\to\) closed Weil form:
**CLOSED**.

### LIV-MD2c3
Fixed-\(a\) negative-shift resolvent first correction \(\to\) Weil form:
**CLOSED**.

### LIV-MD2c4
Computable joint schedule \(\mu(a)\) with uniform first-correction remainder:
**OPEN**.

This is now the unique analytic bridge in this particular denominator-channel
lane.

## 10. Compact theorem

For \(y>1/2\),

\[
\boxed{
\lim_{a\to\infty}
\lim_{\mu\to\infty}
-\frac{\mu^2}{I_a(y)}
\left[
\langle
v_y^{(a)},
(A_a+\mu I)^{-1}v_1^{(a)}
\rangle
-
\frac{I_a(y)}{\mu}
\right]
=
\frac{\xi'(3/2)}{\xi(3/2)}
+
\frac{\xi'(1/2+y)}{\xi(1/2+y)}.
}
\]

No RH, no zero list, and no Montgomery/GUE input occur in the derivation.

Q.E.D.
