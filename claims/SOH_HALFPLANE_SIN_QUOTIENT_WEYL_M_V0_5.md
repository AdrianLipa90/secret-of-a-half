# SOH Sin-Quotient Half-Plane / Weyl m-Function Bridge v0.5

Status: `EXACT_SIN_QUOTIENT_HALFPLANE / STANDARD_ZERO_COUNT_PLUS_EXACT_BLASCHKE / RH_EQUIVALENT_HERglotz_ZEROSET_GATE / CONSTRUCTIVE_M_FROM_KERNEL_OPEN / RH_OPEN`

The v0.4 disk coordinate has a simpler Cayley parent.  With
\[
\zeta=s-\frac12,\qquad w=\zeta^2,
\]
define
\[
\boxed{t=\cos(\pi\sqrt w)=\cos(\pi\zeta)=\sin(\pi s).}
\]
Because cosine is even, `cos(pi*sqrt(w))` is an entire function of `w`.

For `s=beta+i gamma`,
\[
t=\sin(\pi\beta)\cosh(\pi\gamma)
+i\cos(\pi\beta)\sinh(\pi\gamma).
\]
Thus
\[
\Re t>0\qquad(0<\beta<1),
\]
while the strip boundaries map to the imaginary axis.  Inside one critical strip, equality of `sin(pi*s)` implies only `s'=s` or `s'=1-s`; hence after quotienting the functional-equation pair, the map is biholomorphic onto the right half-plane.

The v0.4 disk coordinate is merely the Cayley transform
\[
\boxed{q=\frac{t-1}{t+1},\qquad t=\frac{1+q}{1-q}.}
\]
On the critical line,
\[
\boxed{s=\frac12+i\gamma\Longrightarrow t=\cosh(\pi\gamma)\in[1,\infty).}
\]
For a nontrivial zero `rho=beta+i gamma`, `gamma!=0`; therefore within `0<beta<1`,
\[
\boxed{\Im t=0\iff\beta=\frac12.}
\]
G018 excludes the real interval `0<t<1`, which corresponds to `0<w<1/4`.  Consequently
\[
\boxed{RH\iff\text{all zeros of the half-plane quotient lie on }t>1.}
\]

## Blaschke condition

For a zero with `zeta=a+i gamma`, v0.4 gives
\[
|q|=\frac{\cosh(\pi\gamma)-\cos(\pi a)}{\cosh(\pi\gamma)+\cos(\pi a)},
\]
hence
\[
0<1-|q|=
\frac{2\cos(\pi a)}{\cosh(\pi\gamma)+\cos(\pi a)}
\le4e^{-\pi|\gamma|}.
\]
Together with the standard Riemann zero-count bound `N(T)=O(T log T)`, this proves
\[
\sum_\rho(1-|q_\rho|)<\infty.
\]
Thus the compactified zeros unconditionally define a convergent Blaschke product, equivalently a right-half-plane Blaschke product `B(t)`.

Because zeros are closed under conjugation, conjugate factors can be paired.  For a real zero `a>0` the factor is, up to a unimodular constant,
\[
\frac{t-a}{t+a}.
\]
For a nonreal conjugate pair `a,bar(a)` the paired factor is
\[
\frac{(t-a)(t-\bar a)}{(t+\bar a)(t+a)}.
\]
Each paired factor obeys `P(-t)=1/P(t)`, so `-B'(t)/B(t)` is even and descends to a meromorphic function of `x=t^2`.

Define
\[
\boxed{
M(x):=-\left.\frac{d}{dt}\log B(t)\right|_{t=\sqrt x}.
}
\]
If RH holds, all zeros are real `t_n=cosh(pi gamma_n)>1` and
\[
\boxed{
M(x)=\sum_n\frac{2t_n}{t_n^2-x}
=\int_{[1,\infty)}\frac{d\mu(\lambda)}{\lambda-x},
}
\]
with positive discrete measure
\[
\boxed{d\mu(\lambda)=\sum_n2t_n\,\delta_{t_n^2}.}
\]
Hence `M` is Herglotz on the upper half-plane.

Conversely, if a zero `a=u+iv` has `u>0,v>0`, then the descended logarithmic derivative has a pole at
\[
a^2=(u^2-v^2)+2iuv\in\mathbb C_+.
\]
A Herglotz function must be analytic in `C_+`, so this is impossible.  Conjugation covers `v<0`.  G018 excludes real zeros with `0<a<1`. Therefore
\[
\boxed{RH\iff M\text{ is Herglotz on }\mathbb C_+.}
\]
This is a zero-set/Weyl reformulation.  It is not an independent construction of `M`; deriving the same `M` directly from the theta/Xi operator without first knowing the zeros remains the decisive open bridge.

## Hyperbolic no-shortcut

On the critical line `q=tanh^2(pi gamma/2)`, so the Poincare distance in the disk is
\[
\boxed{
d_{\mathbb D}(0,q)=2\operatorname{artanh}q
=\log\cosh(\pi\gamma)=\log t.
}
\]
Thus the Euclidean compression of all high zeros near `q=1` does not make the problem conformally small: the remaining distance still grows linearly as `pi*|gamma|` asymptotically.

Proof firewall:

- exact: `t=sin(pi s)=cos(pi sqrt(w))`, right-half-plane quotient, critical-line image, disk Cayley relation, hyperbolic-distance identity;
- standard zero count + exact bound: Blaschke convergence;
- exact zero-set equivalence: RH iff the descended Blaschke logarithmic derivative is Herglotz;
- conditional spectral realization: under RH the positive measure has atoms `lambda_n=cosh^2(pi gamma_n)`;
- open: construct the same Weyl `M` from the Xi/theta carrier without zero input; RH.
