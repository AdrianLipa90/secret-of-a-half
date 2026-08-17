# SOH-G006 — PF3 ratio-curvature reduction

Status: **EXACT ALGEBRAIC REDUCTION / PF3 OPEN / RH OPEN**

Let

\[
F(w)=\sum_{k\ge0} a_k w^k,\qquad a_k>0,
\]

with the SOH-G005 coefficients

\[
a_k=\frac{m_k}{(2k)!},\qquad m_k=\int_0^\infty \Phi(y)y^{2k}\,dy.
\]

SOH-G005 proves PF2, equivalently

\[
a_k^2\ge a_{k-1}a_{k+1}.
\]

Define adjacent coefficient ratios

\[
r_k:=\frac{a_k}{a_{k-1}}\quad(k\ge1).
\]

PF2 is exactly the monotonicity `r_{k+1} <= r_k`.

## Exact solid order-three minor

For `k >= 2`, consider

\[
\Delta_k=
\det\begin{pmatrix}
 a_k&a_{k+1}&a_{k+2}\\
 a_{k-1}&a_k&a_{k+1}\\
 a_{k-2}&a_{k-1}&a_k
\end{pmatrix}.
\]

Direct expansion gives

\[
\boxed{
\Delta_k=
-a_{k-2}a_ka_{k+2}
+a_{k-2}a_{k+1}^2
+a_{k-1}^2a_{k+2}
-2a_{k-1}a_ka_{k+1}
+a_k^3.
}
\]

Now define

\[
u_k:=\frac{r_k}{r_{k-1}},\qquad
v_k:=\frac{r_{k+1}}{r_k},\qquad
w_k:=\frac{r_{k+2}}{r_{k+1}}.
\]

After dividing by the positive factor `a_{k-2}^3 r_{k-1}^2 r_k`, the sign of the solid PF3 minor is exactly the sign of

\[
\boxed{
M_k:=1-2v_k+v_k^2\bigl(u_k+w_k-u_kw_k\bigr).
}
\]

Hence

\[
\boxed{\Delta_k\ge0\iff M_k\ge0.}
\]

This isolates the first obstruction beyond PF2.

## PF2 is insufficient

PF2 only supplies

\[
0<u_k,v_k,w_k\le1.
\]

Those inequalities alone do not force `M_k >= 0`; for example values with `v_k` near one and `u_k,w_k` small make the expression negative. Therefore PF3 is genuinely stronger than the SOH-G005 result.

## Active analytic target

For the Riemann-kernel coefficients, finite high-precision diagnostics show

\[
u_k<v_k<w_k<1
\]

through the sampled range, together with `M_k>0`. This is **not** a proof.

The next analytic target is to derive quantitative control of the discrete ratio curvature

\[
q_k:=\frac{r_{k+1}}{r_k}
\]

from the normalized-moment function

\[
R(p)=\Gamma(p+1)^{-1}\int_0^\infty y^p\Phi(y)\,dy,
\qquad a_k=R(2k).
\]

SOH-G005 gives concavity of `log R`, hence `r_k` decreases. PF3 requires a stronger constraint on the *change* of those decreases. No claim is made here that such a bound has been proved.

## Firewall

- PF2: **PROVED** (SOH-G005).
- Solid PF3 reduction to `M_k`: **PROVED algebraically**.
- `M_k >= 0` for every `k`: **OPEN**.
- all order-three Toeplitz minors / PF3: **OPEN**.
- PF-infinity, SOH-G003 real-rootedness, RH: **OPEN**.
