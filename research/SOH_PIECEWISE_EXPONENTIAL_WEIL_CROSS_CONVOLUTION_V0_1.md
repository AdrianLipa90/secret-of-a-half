# SOH Piecewise-Exponential Weil Evaluation and Cross-Convolution Limit v0.1

Status: **EXACT_EXTENDED_WEIL_EVALUATION / EXACT_FINITE_CROSS_CONVOLUTION / WEIL_LIMIT_CLOSED / OPERATOR_DOMAIN_BINDING_OPEN**

Date: 2026-09-26

Parents:
- \`research/SOH_LIVSIC_CAYLEY_LOG_DERIVATIVE_PRIME_BRIDGE_V0_1.md\`
- \`research/SOH_SUZUKI_LIVSIC_SCHUR_REDUCTION_V0_1.md\`

Primary source normalization:
- M. Suzuki, *Weil's quadratic form via the screw function*,
  arXiv:2606.09096v3, Weil functional at the start of Section 1.1.

No RH and no zeta-zero list are used.

## 1. Piecewise-exponential test

Let

\[
p>\frac12,
\qquad
q>\frac12,
\]

and define

\[
\boxed{
F_{p,q}(t)
=
\begin{cases}
e^{-pt},&t\ge0,\\
e^{qt},&t\le0.
\end{cases}
}
\]

Then \(F_{p,q}(0)=1\).

Every term in Suzuki's explicit Weil functional converges absolutely for this
test:
- the two elementary exponential integrals converge because \(p,q>1/2\);
- the prime sums converge because \(p+1/2>1\) and \(q+1/2>1\);
- the regularization integral has the required cancellation at \(0\) and
  decays exponentially at infinity.

We therefore use \(W(F_{p,q})\) for the value of that absolutely convergent
explicit expression.

## 2. Elementary term

The first term in Suzuki's functional is

\[
\int_{\mathbb R}
F_{p,q}(t)
\left(e^{t/2}+e^{-t/2}\right)dt.
\]

Direct integration gives

\[
\boxed{
\frac1{p-1/2}
+
\frac1{p+1/2}
+
\frac1{q-1/2}
+
\frac1{q+1/2}.
}
\]

Set

\[
s_p=p+\frac12,
\qquad
s_q=q+\frac12.
\]

Then this is

\[
\frac1{s_p-1}+\frac1{s_p}
+
\frac1{s_q-1}+\frac1{s_q}.
\]

## 3. Prime term

For \(n\ge2\),

\[
F_{p,q}(\log n)=n^{-p},
\qquad
F_{p,q}(-\log n)=n^{-q}.
\]

Hence the two prime sums are

\[
-\sum_{n\ge2}
\Lambda(n)
\left(
n^{-s_p}+n^{-s_q}
\right).
\]

Using the absolutely convergent identity

\[
\frac{\zeta'(s)}{\zeta(s)}
=
-\sum_{n\ge2}
\frac{\Lambda(n)}{n^s},
\qquad
s>1,
\]

the prime contribution is

\[
\boxed{
\frac{\zeta'(s_p)}{\zeta(s_p)}
+
\frac{\zeta'(s_q)}{\zeta(s_q)}.
}
\]

## 4. Archimedean regularization identity

Split the final regularization integral into the \(p\)- and \(q\)-channels.

For \(s=p+1/2>1\),

\[
J(p)
=
\int_0^\infty
\left(
e^{-px}-e^{-x/2}
\right)
\frac{e^{x/2}}{e^x-e^{-x}}\,dx.
\]

Since

\[
\frac{e^{x/2}}{e^x-e^{-x}}
=
\frac{e^{-x/2}}{1-e^{-2x}},
\]

we obtain

\[
J(p)
=
\int_0^\infty
\frac{
e^{-sx}-e^{-x}
}{
1-e^{-2x}
}\,dx.
\]

With \(u=2x\),

\[
J(p)
=
\frac12
\int_0^\infty
\frac{
e^{-(s/2)u}-e^{-u/2}
}{
1-e^{-u}
}\,du.
\]

The standard digamma difference formula gives

\[
\boxed{
J(p)
=
\frac12
\left[
\psi\!\left(\frac12\right)
-
\psi\!\left(\frac s2\right)
\right].
}
\]

Using

\[
\psi(1/2)=-\gamma-2\log2,
\]

we get

\[
\boxed{
J(p)
=
-\frac12
\left[
\gamma+\log4+\psi(s/2)
\right].
}
\]

The same formula holds for \(q\).

## 5. Exact Weil evaluation

Suzuki's constant term is

\[
-(\log4\pi+\gamma)F_{p,q}(0)
=
-(\log4\pi+\gamma).
\]

Combining Sections 2--4 and splitting that constant equally between the two
channels gives, for each \(s>1\),

\[
\frac1s+\frac1{s-1}
-\frac12\log\pi
+\frac12\psi(s/2)
+\frac{\zeta'(s)}{\zeta(s)}.
\]

Because Suzuki uses

\[
\xi(s)
=
s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),
\]

this expression is exactly

\[
\frac{\xi'(s)}{\xi(s)}.
\]

Therefore

\[
\boxed{
W(F_{p,q})
=
\frac{\xi'(p+1/2)}{\xi(p+1/2)}
+
\frac{\xi'(q+1/2)}{\xi(q+1/2)}.
}
\]

This is an exact zero-free identity on \(p,q>1/2\).

## 6. Finite interval cross-convolution

Fix

\[
a>0,
\qquad
y>\frac12,
\]

and define the sharp finite-interval vectors

\[
v_y^{(a)}(x)=e^{yx}\mathbf1_{[-a,a]}(x),
\]

\[
v_1^{(a)}(x)=e^x\mathbf1_{[-a,a]}(x).
\]

Their overlap is

\[
I_a(y)
=
\langle v_y^{(a)},v_1^{(a)}\rangle
=
\frac{2\sinh((y+1)a)}{y+1}.
\]

Let

\[
f_{a,y}(t)
=
\frac{
(v_y^{(a)}*\widetilde v_1^{(a)})(t)
}{
I_a(y)
}.
\]

Put

\[
c=y+1,
\qquad
d=e^{-2ca}.
\]

A direct convolution calculation gives

\[
\boxed{
f_{a,y}(t)
=
\begin{cases}
0,&|t|>2a,\\[2mm]
e^{-t}
\dfrac{
1-e^{-c(2a-t)}
}{
1-e^{-2ca}
},
&0\le t\le2a,\\[4mm]
e^{yt}
\dfrac{
1-e^{-c(2a+t)}
}{
1-e^{-2ca}
},
&-2a\le t\le0.
\end{cases}
}
\]

In particular,

\[
f_{a,y}(0)=1.
\]

## 7. Exact domination and pointwise limit

Define

\[
F_{1,y}(t)
=
\begin{cases}
e^{-t},&t\ge0,\\
e^{yt},&t\le0.
\end{cases}
\]

For \(0\le t\le2a\),

\[
e^{-c(2a-t)}
\ge
e^{-2ca},
\]

so

\[
0\le
\frac{1-e^{-c(2a-t)}}{1-e^{-2ca}}
\le1.
\]

The same argument applies on the negative half-line.

Therefore, for every \(a>0\),

\[
\boxed{
0\le f_{a,y}(t)\le F_{1,y}(t)
\qquad
(t\in\mathbb R).
}
\]

For every fixed \(t\),

\[
\boxed{
f_{a,y}(t)\longrightarrow F_{1,y}(t)
\qquad(a\to\infty).
}
\]

The finite-support approximation is thus monotone-bounded in amplitude, though
no monotonicity in \(a\) is required.

## 8. Convergence through the Weil functional

We now apply the four components of Suzuki's explicit \(W\).

### Elementary integral

Because

\[
F_{1,y}(t)
\left(
e^{t/2}+e^{-t/2}
\right)
\in L^1(\mathbb R)
\]

exactly when \(y>1/2\), dominated convergence gives convergence of the first
integral.

### Prime sums

The domination in Section 7 gives

\[
\frac{\Lambda(n)}{\sqrt n}
f_{a,y}(\log n)
\le
\frac{\Lambda(n)}{n^{3/2}},
\]

and

\[
\frac{\Lambda(n)}{\sqrt n}
f_{a,y}(-\log n)
\le
\frac{\Lambda(n)}{n^{y+1/2}}.
\]

Both majorant series converge because \(y>1/2\). Therefore the two prime sums
converge by dominated convergence for series.

### Constant term

For every \(a\),

\[
f_{a,y}(0)=F_{1,y}(0)=1.
\]

The constant term is therefore identical at every \(a\).

### Regularization integral

For \(a\ge1\), the one-sided derivatives of \(f_{a,y}\) on \(0\le x\le1\)
are uniformly bounded in \(a\). Since \(f_{a,y}(0)=1\), the bracket

\[
f_{a,y}(x)+f_{a,y}(-x)-2e^{-x/2}
\]

is \(O_y(x)\) uniformly on \(0<x\le1\). The regularization kernel is
\(O(1/x)\) there, so the product is uniformly bounded.

For \(x\ge1\), Section 7 gives the integrable majorant

\[
e^{-x}+e^{-yx}+2e^{-x/2}
\]

times

\[
\frac{e^{x/2}}{e^x-e^{-x}}
=
O(e^{-x/2}).
\]

Hence dominated convergence applies to the final integral as well.

Thus

\[
\boxed{
W(f_{a,y})
\longrightarrow
W(F_{1,y}).
}
\]

By Section 5,

\[
\boxed{
W(f_{a,y})
\longrightarrow
r_0
+
\frac{\xi'(1/2+y)}{\xi(1/2+y)},
}
\]

where

\[
r_0
=
\frac{\xi'(3/2)}{\xi(3/2)}.
\]

## 9. Exact finite prime-support compatibility

Because

\[
\operatorname{supp}f_{a,y}\subset[-2a,2a],
\]

the prime terms in \(W(f_{a,y})\) vanish whenever

\[
\log n>2a.
\]

Therefore the finite cross-convolution sees exactly

\[
\boxed{
n\le e^{2a},
}
\]

the same arithmetic support cutoff already appearing in the localized Suzuki
operator and in the Livšic prime-side target.

This is not an imposed cutoff.

It is forced by finite-interval support geometry.

## 10. Relation to the Livšic denominator channel

On \(s=1/2+y>1\), the infinite characteristic denominator contains

\[
Bf(iy)+iAf'(iy)
=
A\xi(s)
\left[
r_0+\frac{\xi'(s)}{\xi(s)}
\right].
\]

The theorem above reconstructs precisely the bracket

\[
\boxed{
r_0+\frac{\xi'(s)}{\xi(s)}
}
\]

as the large-\(a\) limit of the normalized finite cross-convolution Weil
functional.

Thus one full scalar combination appearing in the infinite Livšic
characteristic object now has a zero-list-free prime-side realization.

## 11. Operator-domain firewall

The vectors

\[
v_y^{(a)}(x)=e^{yx}\mathbf1_{[-a,a]}(x)
\]

have sharp endpoint jumps.

The theorem above is a statement about:
- their explicit convolution;
- Suzuki's absolutely convergent Weil functional applied to that convolution.

It does **not** silently assert that

\[
W(f_{a,y})
=
\frac{
\langle v_y^{(a)},A_av_1^{(a)}\rangle
}{
\langle v_y^{(a)},v_1^{(a)}\rangle
}
\]

in the closed-operator sense.

That identity requires a separate form-domain/approximation theorem or a
smooth-cutoff replacement.

This is the remaining binding if the result is to be inserted directly into
the finite Suzuki resolvent machinery.

## 12. New narrowed gate

### LIV-MD2c1 — finite Weil scalar to finite prime target
Status: **CLOSED AT EXPLICIT-FUNCTIONAL LEVEL**.

The normalized cross-convolution has exact finite prime support and converges
to

\[
r_0+\xi'(s)/\xi(s).
\]

### LIV-MD2c2 — closed-form/operator-domain binding
Status: **OPEN**.

Show that a domain-admissible smooth approximation or closed-form pairing
carries the same limit into the localized operator/resolvent construction.

### LIV-MD2c3 — resolvent-to-form renormalized first correction
Status: **OPEN**.

Relate the negative-shift scalar resolvent/Cayley observable to the normalized
Weil cross form with a quantified error uniform in the joint \(a\to\infty\)
schedule.

## 13. Compact theorem

### Theorem — piecewise-exponential Weil / finite cross-convolution bridge

For \(p,q>1/2\),

\[
\boxed{
W(F_{p,q})
=
\frac{\xi'(p+1/2)}{\xi(p+1/2)}
+
\frac{\xi'(q+1/2)}{\xi(q+1/2)}.
}
\]

For \(y>1/2\), let \(f_{a,y}\) be the normalized convolution of
\(e^{yx}\mathbf1_{[-a,a]}\) with the reflected
\(e^x\mathbf1_{[-a,a]}\). Then

\[
\boxed{
0\le f_{a,y}\le F_{1,y},
\qquad
f_{a,y}(t)\to F_{1,y}(t),
}
\]

and

\[
\boxed{
W(f_{a,y})
\to
\frac{\xi'(3/2)}{\xi(3/2)}
+
\frac{\xi'(1/2+y)}{\xi(1/2+y)}.
}
\]

The finite prime support is exactly \(n\le e^{2a}\).

Q.E.D.
