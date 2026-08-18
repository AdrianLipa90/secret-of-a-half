# SOH-G018 — Reciprocal paired-spectrum polynomial

Status: **THEOREM / exact finite-set algebraic reduction**

Version: 0.1

## Scope

SOH-G015 proved that the quotient paired-root set

\[
P_J:=\{w:F(w)=0,\ F(J(w))=0\},
\qquad
J(w)=\frac1{16w},
\]

is finite. SOH-G017 classified its orbit parity through the corresponding \(V_4\) action in the \(s\)-plane.

This note packages the finite quotient paired set into a canonical self-reciprocal polynomial.

No claim is made that \(P_J\) is nonempty. The status of \(F(-1/4)\) remains **UNKNOWN**.

## Normalized reciprocal coordinate

Define

\[
\lambda=4w.
\]

Then

\[
4J(w)=\frac{4}{16w}=\frac1{4w}=\frac1\lambda.
\]

Thus the quotient negative inversion becomes the ordinary reciprocal involution

\[
\boxed{\lambda\mapsto\lambda^{-1}}.
\]

Let

\[
\Lambda:=4P_J=\{4w:w\in P_J\}.
\]

Because \(P_J\) is finite and contains no \(0\) (SOH-G015, since \(F(0)=\xi(1/2)>0\)), 
\(\Lambda\) is a finite subset of \(\mathbb C^\times\).

## Inversion and conjugation closure

### Proposition 1 — reciprocal closure

\[
\lambda\in\Lambda
\Longrightarrow
\lambda^{-1}\in\Lambda.
\]

This follows immediately from the \(J\)-invariance of \(P_J\).

### Proposition 2 — conjugation closure

The quotient entire function \(F\) has real Taylor coefficients. Therefore

\[
F(\bar w)=\overline{F(w)}.
\]

Since \(J\) has real coefficients,

\[
J(\bar w)=\overline{J(w)}.
\]

Hence

\[
w\in P_J
\Longrightarrow
\bar w\in P_J,
\]

and therefore

\[
\lambda\in\Lambda
\Longrightarrow
\bar\lambda\in\Lambda.
\]

## Canonical monic orbit polynomial

Let

\[
n:=|P_J|=|\Lambda|
\]

and define

\[
Q(x):=\prod_{\lambda\in\Lambda}(x-\lambda).
\]

If \(P_J=\varnothing\), use the standard empty-product convention \(Q(x)=1\).

## Product of normalized roots

By SOH-G017, every reciprocal orbit has size \(2\), except possibly the fixed point

\[
\lambda=-1,
\]

which corresponds to \(w=-1/4\). The other reciprocal fixed point

\[
\lambda=+1
\]

corresponds to \(w=+1/4\), but this is excluded because the positive-coefficient theorem gives

\[
F(1/4)>0.
\]

Write

\[
n=2a+\varepsilon,
\qquad
\varepsilon\in\{0,1\},
\]

where \(\varepsilon=1\) precisely when \(-1\in\Lambda\).

Every two-cycle \(\{\lambda,\lambda^{-1}\}\) has product \(1\). Therefore

\[
\prod_{\lambda\in\Lambda}\lambda=(-1)^\varepsilon.
\]

Since \(n\equiv\varepsilon\pmod2\), the constant term of \(Q\) is

\[
Q(0)=(-1)^n\prod_{\lambda\in\Lambda}\lambda=1.
\]

Thus

\[
\boxed{Q(0)=1}.
\]

## Theorem — exact self-reciprocity

\[
\boxed{Q(x)=x^nQ(1/x)}.
\]

### Proof

Compute

\[
x^nQ(1/x)
=x^n\prod_{\lambda\in\Lambda}\left(\frac1x-\lambda\right)
=\prod_{\lambda\in\Lambda}(1-\lambda x).
\]

The roots of this polynomial are \(\lambda^{-1}\), and reciprocal closure gives

\[
\{\lambda^{-1}:\lambda\in\Lambda\}=\Lambda.
\]

Hence \(x^nQ(1/x)\) and \(Q(x)\) have exactly the same roots. Their leading coefficients also agree:

\[
(-1)^n\prod_{\lambda\in\Lambda}\lambda
=Q(0)
=1.
\]

Both are monic degree-\(n\) polynomials with the same roots, so they are identical. QED.

## Corollary — palindromic coefficients

Write

\[
Q(x)=x^n+c_1x^{n-1}+\cdots+c_{n-1}x+1.
\]

The self-reciprocal identity implies

\[
\boxed{c_k=c_{n-k}}
\]

for all coefficient indices. Therefore the coefficient vector is palindromic.

Because \(\Lambda\) is conjugation invariant, \(Q\) is fixed by coefficientwise conjugation, so

\[
\boxed{Q\in\mathbb R[x]}.
\]

## Orbit factorization

Choose one representative \(\lambda_j\) from each nonfixed reciprocal two-cycle. Define

\[
\tau_j:=\lambda_j+\lambda_j^{-1}.
\]

Then

\[
(x-\lambda_j)(x-\lambda_j^{-1})
=x^2-\tau_jx+1.
\]

Consequently

\[
\boxed{
Q(x)
=(x+1)^\varepsilon
\prod_{j=1}^{a}\left(x^2-\tau_jx+1\right).
}
\]

Individual \(\tau_j\) may be complex, but conjugation closure of \(\Lambda\) makes the full product real.

## Exceptional root criterion

The excluded reciprocal fixed point is

\[
\lambda=+1
\iff
w=+\frac14,
\]

and \(F(1/4)>0\), so

\[
\boxed{Q(1)\neq0}.
\]

The only allowed reciprocal fixed point is

\[
\lambda=-1
\iff
w=-\frac14.
\]

Therefore

\[
\boxed{
Q(-1)=0
\iff
\varepsilon=1
\iff
F(-1/4)=0.
}
\]

This criterion does not decide whether the condition holds.

## Equivalent form in the original \(w\)-coordinate

Let

\[
H(w):=\prod_{r\in P_J}(w-r).
\]

Since

\[
Q(x)=4^nH(x/4),
\]

the self-reciprocal identity becomes

\[
\boxed{
H(w)=4^n w^n H\!\left(\frac1{16w}\right).
}
\]

Thus the finite paired-root polynomial inherits an exact functional relation from the quotient negative inversion.

## Claim firewall

PROVED here:

- normalization \(\lambda=4w\) converts \(J\) to ordinary reciprocal inversion;
- the normalized paired set is finite, reciprocal invariant, and conjugation invariant;
- its monic polynomial \(Q\) has real palindromic coefficients;
- \(Q(0)=1\);
- \(Q(x)=x^nQ(1/x)\);
- \(Q(1)\neq0\);
- \(Q(-1)=0\iff F(-1/4)=0\);
- exact reciprocal-orbit factorization into quadratics, with a possible single \(x+1\) factor.

NOT proved here:

- that \(P_J\) is nonempty;
- the zero or nonzero status of \(F(-1/4)\) by a new analytic theorem;
- real-rootedness of \(F\);
- PF-infinity;
- SOH-G003;
- RH.
