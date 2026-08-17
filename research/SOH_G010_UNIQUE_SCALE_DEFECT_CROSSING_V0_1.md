# SOH-G010 — Unique positive scale-defect crossing

Status: **PROVED on the positive real u-axis**.

Let

\[
X(u)=\xi\!\left(\frac{u}{1+u}\right),\qquad u>0,
\]

and for `a>1`

\[
\Delta_a(u)=X(au)-X(u).
\]

Write `u=e^lambda`. Since

\[
\frac{u}{1+u}=\frac12+\frac12\tanh\frac\lambda2,
\]

and `xi(1/2+z)=F(z^2)`, one has

\[
X(e^\lambda)=F\!\left(\frac14\tanh^2\frac\lambda2\right).
\]

From SOH-G003, `F(w)=sum a_k w^k` with every `a_k>0`. Hence for `w>=0`,

\[
F'(w)=\sum_{k\ge1}k a_k w^{k-1}>0.
\]

Therefore `X(e^lambda)` is even in `lambda` and strictly increasing with `|lambda|`.

Let `L=log a>0`. Then

\[
\Delta_a(e^\lambda)=X(e^{\lambda+L})-X(e^\lambda),
\]

so its sign is exactly the sign of

\[
|\lambda+L|-|\lambda|.
\]

This quantity is negative for `lambda<-L/2`, zero only at `lambda=-L/2`, and positive for `lambda>-L/2`. Thus

\[
\boxed{\Delta_a(u)<0\iff 0<u<a^{-1/2}},
\]
\[
\boxed{\Delta_a(u)=0\iff u=a^{-1/2}},
\]
\[
\boxed{\Delta_a(u)>0\iff u>a^{-1/2}}.
\]

For the Uroboros scale `a=32`, the unique crossing is `u=32^{-1/2}`.

This is a theorem about the positive real axis. It does not imply zero-location in the complex plane, SOH-G003 real-rootedness, PF-infinity, or RH.
