# SOH-G018 — Central Zero-Free Interval from the Kernel Moment Bound

## Status

**THEOREM-LEVEL CENTRAL ZERO-FREE INTERVAL / PROVED FROM G017.**

SOH-G017 proves the strict moment estimate

\[
m_2<\frac{m_0}{10},
\qquad
m_j=\int_0^\infty y^j\Phi(y)\,dy,
\qquad
m_0=F(0)>0.
\]

This note converts that estimate into an explicit central zero-free interval on the critical line and on the real `w` axis.

## 1. Critical-line representation

For real `t`,

\[
\Xi(t):=\xi\!\left(\frac12+it\right)
=\int_0^\infty\Phi(y)\cos(ty)\,dy
=F(-t^2).
\]

Using the global inequality

\[
\cos x\ge1-\frac{x^2}{2},
\]

we obtain

\[
\Xi(t)
\ge m_0-\frac{t^2}{2}m_2.
\]

For `t != 0`, G017's strict moment inequality gives

\[
\Xi(t)
>m_0\left(1-\frac{t^2}{20}\right).
\]

At `t=0`, `Xi(0)=m0>0` exactly.

## 2. Closed central interval

If

\[
|t|<\sqrt{20},
\]

the right-hand side above is positive. At the two endpoints `t^2=20`, use the strict moment inequality before replacing it by the weak normalized bound:

\[
\Xi(\pm\sqrt{20})
\ge m_0-10m_2
>0.
\]

Therefore

\[
\boxed{
\xi\!\left(\frac12+it\right)>0
\quad\text{for every real }|t|\le\sqrt{20}.
}
\]

In particular, the critical line contains no xi zero in this closed central segment.

## 3. Quotient form

Since `w=-t^2`, the interval `|t|<=sqrt(20)` maps exactly to

\[
-20\le w\le0.
\]

Thus

\[
\boxed{F(w)>0\quad(-20\le w\le0).}
\]

Earlier positive-coefficient results give

\[
F(w)>0\quad(w\ge0).
\]

Combining the two results yields the real-axis theorem

\[
\boxed{F(w)>0\quad\text{for every real }w\ge-20.}
\]

Hence every real zero of `F`, if any, must satisfy

\[
\boxed{w<-20.}
\]

## 4. Relation to the RH frontier

SOH-G003 remains the open statement that every zero of `F` is real. G018 does not advance that reality claim directly. It sharpens the consequence if a zero is already known to be real: such a zero cannot lie at or to the right of `-20`.

Equivalently, any xi zero that lies on the critical line must obey

\[
\boxed{|\Im\rho|>\sqrt{20}.}
\]

This is an unconditional central critical-line zero exclusion derived from the exact positive kernel and the quantitative G004/G017 curvature chain.

## 5. Proof firewall

Proved here:

- `xi(1/2+i t)>0` for every real `|t|<=sqrt(20)`;
- `F(w)>0` for every real `-20<=w<=0`;
- combining with prior coefficient positivity, `F(w)>0` for every real `w>=-20`;
- every real zero of `F` must lie in `(-infinity,-20)`;
- every critical-line xi zero must have `|Im rho|>sqrt(20)`.

Not proved or claimed here:

- that all xi zeros lie on the critical line;
- that all zeros of `F` are real;
- that `F` has any real zeros;
- PF-infinity;
- SOH-G003;
- RH.
