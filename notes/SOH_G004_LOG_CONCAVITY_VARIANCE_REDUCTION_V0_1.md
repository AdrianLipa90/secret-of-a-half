# SOH-G004 — Log-concavity reduction for the compactified Riemann kernel

Status: **OPEN CANDIDATE / exact reduction, not a proof of real-rootedness or RH**

Let

\[
\Phi(y)=\sum_{n\ge 1}\phi_n(y),
\qquad
\phi_n(y)=4a_n e^{5y/2}(2r_n-3)e^{-r_n},
\]
with

\[
a_n=\pi n^2,
\qquad
r_n=a_n e^{2y}.
\]

For every \(y\ge0\), \(r_n\ge\pi>3/2\), hence every \(\phi_n(y)>0\).

## 1. Exact single-channel curvature

Define

\[
g_n(y)=\log \phi_n(y).
\]

Then

\[
g_n'(y)
=\frac52+\frac{4r_n}{2r_n-3}-2r_n,
\]

and, using \(r_n'=2r_n\),

\[
\boxed{
 g_n''(y)
 =-4r_n-\frac{24r_n}{(2r_n-3)^2}<0.
}
\]

Thus every individual theta channel is strictly log-concave on \([0,\infty)\).

## 2. Exact mixture identity

Let

\[
p_n(y)=\frac{\phi_n(y)}{\Phi(y)}.
\]

Then \(p_n>0\) and \(\sum_n p_n=1\). Writing \(L(y)=\log\Phi(y)\), differentiation gives the exact identity

\[
\boxed{
L''(y)
=\sum_n p_n(y)g_n''(y)
+\operatorname{Var}_{p(y)}\!\bigl(g_n'(y)\bigr).
}
\]

Therefore the only obstruction to transferring strict log-concavity from every individual theta channel to the full Riemann kernel is the positive slope-variance term.

Equivalently, strict log-concavity of \(\Phi\) follows from

\[
\boxed{
\operatorname{Var}_{p(y)}\!\bigl(g_n'(y)\bigr)
<
-\sum_n p_n(y)g_n''(y).
}
\]

This is a concrete quantitative inequality on the exact theta sum, not a reformulation of RH.

## 3. Compactified weight

For

\[
\eta=\tanh y,
\qquad
W(\eta)=\frac{\Phi(y)}{1-\eta^2},
\]
we have exactly

\[
\frac{d^2}{d\eta^2}\log W(\eta)
=
\frac{
L''(y)+2\tanh y\,L'(y)+2(1+\tanh^2y)
}{(1-\tanh^2y)^2}.
\]

Hence strict log-concavity of the compactified weight is equivalent to

\[
\boxed{
L''(y)+2\tanh y\,L'(y)+2(1+\tanh^2y)<0,
\qquad y>0.
}
\]

Substituting the mixture identity yields a still more explicit SOH-G004 target:

\[
\boxed{
\operatorname{Var}_{p(y)}(g_n')
<
-\sum_n p_n g_n''
-2\tanh y\sum_n p_n g_n'
-2(1+\tanh^2y).
}
\]

No claim is made here that this inequality has been proved globally.

## 4. Dominance structure

The channel ratio is exponentially suppressed in \(n^2\):

\[
\frac{\phi_n(y)}{\phi_1(y)}
\propto
n^2\,\frac{2\pi n^2e^{2y}-3}{2\pi e^{2y}-3}
\exp\!\bigl[-\pi(n^2-1)e^{2y}\bigr].
\]

Thus the variance term is generated only by an exponentially small tail relative to the \(n=1\) channel, while every channel contributes negative curvature. A rigorous proof route may therefore split the problem into:

1. an exact \(n=1\) negative-curvature margin;
2. a certified bound on the total tail mass \(\sum_{n\ge2}p_n\);
3. a certified bound on the slope spread \(|g_n'-g_1'|\);
4. comparison of the resulting variance bound with the negative-curvature margin.

This is the active analytic route for SOH-G004. It remains strictly below SOH-G003 real-rootedness and below RH.