# SOH-G005 — PF2 coefficient theorem from the compactified Riemann-kernel geometry

Status: **PROVED at order 2 / does not prove PF_infinity, SOH-G003, or RH**

Let

\[
F(w)=\sum_{k\ge 0} a_k w^k,
\qquad
a_k=\frac{m_k}{(2k)!},
\qquad
m_k=\int_0^\infty y^{2k}\Phi(y)\,dy.
\]

The preceding SOH-G004 theorem proves that the exact Riemann kernel \(\Phi\) is strictly log-concave on \([0,\infty)\). In fact the same proof gives \((\log\Phi)''<-10\).

## 1. Normalized moment theorem

A classical moment inequality for log-concave functions states that if \(f:[0,\infty)\to[0,\infty)\) is integrable and log-concave, then

\[
R(p):=\frac{1}{\Gamma(p+1)}\int_0^\infty x^p f(x)\,dx
\]

is log-concave for \(p>-1\). This is the moment-concavity result used in the Karlin--Proschan--Barlow/Borell line of inequalities for Pólya-frequency and log-concave functions.

Apply it with \(f=\Phi\). Since

\[
a_k=R(2k),
\]

restriction of a log-concave function to the arithmetic progression \(0,2,4,\dots\) gives

\[
\boxed{a_k^2\ge a_{k-1}a_{k+1}\qquad(k\ge1).}
\]

All coefficients are strictly positive, so there are no internal zeros.

## 2. Toeplitz interpretation

For a nonnegative sequence without internal zeros, order-two Pólya-frequency (PF2) is equivalent to log-concavity. Hence the coefficient sequence \((a_k)_{k\ge0}\) is PF2. Equivalently every adjacent 2x2 Toeplitz minor

\[
\det\begin{pmatrix}
a_k&a_{k+1}\\
a_{k-1}&a_k
\end{pmatrix}
=a_k^2-a_{k-1}a_{k+1}
\]

is nonnegative.

Thus SOH-G004 produces a genuine zero-preserving coefficient constraint that is stronger than coefficient positivity.

## 3. Hankel positivity is not progress

The raw moment sequence \(m_k\) has positive Hankel matrices for the automatic reason

\[
\sum_{i,j}c_ic_jm_{i+j}
=\int_0^\infty \Phi(y)\left(\sum_i c_i y^{2i}\right)^2dy\ge0.
\]

Therefore Hankel positivity alone contains no new zero-location information here. It is retained as a NO-GO against treating generic moment positivity as evidence for RH.

## 4. Exact remaining frontier

PF2 is strictly weaker than PF_infinity. The classical Aissen--Edrei--Schoenberg--Whitney theory identifies total positivity of the coefficient Toeplitz matrix (PF_infinity) with the real-negative-zero generating-function structure in the relevant nonnegative-coefficient setting.

Accordingly the next nontrivial hierarchy is

\[
\mathrm{PF}_2\quad\longrightarrow\quad\mathrm{PF}_3\quad\longrightarrow\cdots\longrightarrow\mathrm{PF}_\infty.
\]

SOH-G005 proves only the first arrow's starting point. No claim is made that PF3 or PF_infinity has been proved.

## References

- S. Karlin, F. Proschan, R. E. Barlow, *Moment inequalities of Pólya frequency functions*, Pacific Journal of Mathematics **11** (1961), 1023--1033, DOI: 10.2140/pjm.1961.11.1023.
- M. Aissen, A. Edrei, I. J. Schoenberg, A. Whitney, *On the generating functions of totally positive sequences*, Proc. Natl. Acad. Sci. USA **37** (1951), 303--307, DOI: 10.1073/pnas.37.5.303.
