# SOH-G024 v0.4 — Relative-moment structure, inherited strong log-concavity, and a no-go boundary

**Status:** EXACT STRUCTURAL THEOREMS / ADVERSARIAL NO-GO PASS / RH OPEN  
**Branch:** `proof/theta-nbody-hermitian-bilinear-rigidity-v0.1`  
**Date:** 17 September 2026

## 1. Scope

SOH-G024 v0.3 reduced the active RH frontier to coefficientwise Fourier positivity of the relative-moment kernels

\[
C_n(u)=\int_{\mathbb R} r^{2n}K(u+r)K(u-r)\,dr,
\]

because

\[
L_n[f](x)
=
\frac{2^{2n+1}}{(2n)!}
\widehat C_n(2x),
\]

and for \(f=\Xi\),

\[
RH
\iff
L_n[\Xi](x)\ge 0
\quad
\forall x\in\mathbb R,\; n\ge0.
\]

The present note asks how much structure the entire family \(C_n\) inherits from the positive, strongly log-concave Riemann kernel.

The answer has three exact parts:

1. every \(C_n\) inherits **twice** the strong-log-concavity curvature of \(K\);
2. for every fixed \(u\), the sequence \(\{C_n(u)\}_{n\ge0}\) is a Stieltjes moment sequence and hence has positive Hankel matrices;
3. the exponential generating mixture of all \(C_n\) is positive definite in \(u\) for every real transverse parameter.

A fourth result is a HOUND boundary: even the conjunction of these three positivity structures is not sufficient, in general, to force coefficientwise Fourier positivity. An explicit strongly log-concave positive Schwartz kernel has a negative second extended-Laguerre gate.

RH remains open.

## 2. Strong log-concavity inherited by every relative moment

Assume

\[
K(t)=e^{-L(t)}>0
\]

is even and

\[
\boxed{L''(t)\ge\kappa>0.}
\]

For \(r>0\), define the joint integrand

\[
F_n(u,r)=2r^{2n}K(u+r)K(u-r).
\]

Its negative logarithm, up to an additive constant, is

\[
V_n(u,r)
=
L(u+r)+L(u-r)-2n\log r.
\]

Write

\[
a=L''(u+r),
\qquad
b=L''(u-r).
\]

Then

\[
\nabla^2V_n
=
\begin{pmatrix}
a+b & a-b\\
a-b & a+b+\dfrac{2n}{r^2}
\end{pmatrix}.
\]

The matrix without the last diagonal term has eigenvalues \(2a\) and \(2b\). Hence

\[
\nabla^2V_n\ge2\kappa I.
\]

The added \(2n/r^2\) term is positive semidefinite, so the bound holds for every \(n\ge0\).

Strong log-concavity is preserved under marginalization (strong Prékopa / Brascamp–Lieb). Since

\[
C_n(u)=\int_0^\infty F_n(u,r)\,dr,
\]

we obtain

\[
\boxed{
-\frac{d^2}{du^2}\log C_n(u)\ge2\kappa
\qquad
\forall n\ge0.
}
\]

Thus the entire relative-moment hierarchy inherits a uniform curvature gap.

For the Riemann kernel, the repository's G004/G024 estimates give the stronger-than-needed internal bound

\[
-(\log K)''>10
\]

on the smooth even kernel. Therefore the hierarchy satisfies

\[
\boxed{
-(\log C_n)''>20
\qquad
\forall n\ge0.
}
\]

This is below RH: strong log-concavity does not imply Fourier positivity.

## 3. Uniform first radial complete-monotonicity gate

Each \(C_n\) is even, so

\[
(\log C_n)'(0)=0.
\]

Integrating the curvature inequality for \(u>0\),

\[
-(\log C_n)'(u)\ge2\kappa u.
\]

Hence

\[
\boxed{
C_n(u)\le C_n(0)e^{-\kappa u^2}.
}
\]

Put

\[
R_n(q)=C_n(\sqrt q),\qquad q\ge0.
\]

For \(q>0\), \(u=\sqrt q\),

\[
-\frac{R_n'(q)}{R_n(q)}
=
-\frac{(\log C_n)'(u)}{2u}
\ge\kappa.
\]

Therefore

\[
\boxed{
R_n'(q)<0
\quad\text{and}\quad
R_n(q)\le R_n(0)e^{-\kappa q}.
}
\]

This extends the historical first-order radial monotonicity mechanism from one selected G024 correlation to the complete relative-moment hierarchy.

It does **not** establish \(R_n''\ge0\) or higher complete monotonicity.

## 4. Stieltjes/Hankel positivity in hierarchy order

Because the integrand is even in \(r\),

\[
C_n(u)
=
2\int_0^\infty r^{2n}K(u+r)K(u-r)\,dr.
\]

Set \(q=r^2\). Then

\[
\boxed{
C_n(u)
=
\int_0^\infty q^n\,d\mu_u(q),
}
\]

with positive measure

\[
\boxed{
d\mu_u(q)
=
q^{-1/2}
K(u+\sqrt q)K(u-\sqrt q)\,dq.
}
\]

Thus, for every fixed \(u\), \(\{C_n(u)\}_{n\ge0}\) is a Stieltjes moment sequence.

Consequently every finite Hankel matrix

\[
\boxed{
\left[C_{i+j}(u)\right]_{i,j=0}^{m}
\succeq0.
}
\]

Equivalently, for every real polynomial \(p(q)=\sum_j a_jq^j\),

\[
\sum_{i,j}a_ia_jC_{i+j}(u)
=
\int_0^\infty p(q)^2\,d\mu_u(q)
\ge0.
\]

This positivity is unconditional and pointwise in the center coordinate \(u\).

## 5. Positive-definite exponential generating mixture

Define

\[
\boxed{
B_y(u)
=
\int_{\mathbb R}
\cosh(2yr)
K(u+r)K(u-r)\,dr.
}
\]

Expanding \(\cosh\),

\[
\boxed{
B_y(u)
=
\sum_{n=0}^\infty
\frac{(2y)^{2n}}{(2n)!}C_n(u).
}
\]

Let

\[
f(z)=\int_{\mathbb R}K(t)e^{-izt}\,dt.
\]

With \(t=u+r,\ s=u-r\), the Jacobian is \(dt\,ds=2\,du\,dr\). Directly,

\[
\boxed{
\widehat B_y(2x)
=
\frac12 f(x+iy)f(x-iy).
}
\]

For real-entire \(f\),

\[
\boxed{
\widehat B_y(2x)
=
\frac12|f(x+iy)|^2\ge0.
}
\]

Hence \(B_y\) is positive definite in \(u\) for every real \(y\), without RH.

This is the physical-space counterpart of the v0.3 partition identity

\[
\mathcal Z(-ix,y)=\frac12|f(x+iy)|^2.
\]

## 6. The precise non-commuting positivity problem

We now have, unconditionally:

\[
\boxed{
\text{Hankel positivity in }n\text{ at fixed }u,
}
\]

\[
\boxed{
\text{positive definiteness in }u
\text{ after the positive exponential mixture over }n,
}
\]

and, for the Riemann kernel,

\[
\boxed{
\text{uniform strong log-concavity of every }C_n.
}
\]

RH needs the stronger coefficientwise statement

\[
\boxed{
\widehat C_n(\omega)\ge0
\quad
\forall \omega\in\mathbb R,\; n\ge0.
}
\]

Thus the remaining obstruction is an interchange problem:

\[
\boxed{
\text{positive mixture for every }y
\quad\not\Rightarrow\quad
\text{positive Fourier transform coefficient-by-coefficient}.
}
\]

The next theorem shows that the existing positivity package, by itself, cannot bridge that interchange.

## 7. Strong-log-concavity no-go control

Take the explicit positive even Schwartz kernel

\[
\boxed{
K_0(t)
=
e^{-a t^2}\left(1+\varepsilon\cos t\right),
\qquad
a=\frac{13}{100},
\quad
\varepsilon=\frac15.
}
\]

Since \(0<\varepsilon<1\), \(K_0>0\).

For

\[
h(t)=\log(1+\varepsilon\cos t),
\]

\[
h''(t)
=
-\frac{\varepsilon(\cos t+\varepsilon)}
{(1+\varepsilon\cos t)^2}
\le
\frac{\varepsilon}{1-\varepsilon}
=
\frac14.
\]

Therefore

\[
-(\log K_0)''
=
2a-h''
\ge
\frac{26}{100}-\frac14
=
\boxed{\frac1{100}}.
\]

Now scale

\[
K_s(t)=K_0(st),
\qquad s=40.
\]

Then

\[
\boxed{
-(\log K_s)''\ge16>10.
}
\]

So this control is **more strongly log-concave than the lower curvature margin used for the Riemann kernel**.

Its Fourier transform is explicit:

\[
f_0(z)
=
\sqrt{\frac{\pi}{a}}
e^{-z^2/(4a)}
\left[
1+\varepsilon e^{-1/(4a)}
\cosh\!\left(\frac{z}{2a}\right)
\right],
\]

and

\[
f_s(z)=\frac1s f_0(z/s).
\]

At

\[
x_0=\frac{611}{500}=1.222,
\]

direct evaluation of the standard second extended-Laguerre operator gives

\[
\boxed{
L_2[f_0](x_0)
=
-0.9169588809813965290564007845525901088\ldots<0.
}
\]

The scaling law

\[
\boxed{
L_n[f_s](sx)
=
s^{-2n-2}L_n[f_0](x)
}
\]

therefore gives, at

\[
sx_0=48.88,
\]

\[
\boxed{
L_2[f_s](48.88)
=
-2.2386691430209876197666034779\ldots\times10^{-10}<0.
}
\]

Because

\[
L_2[f](x)
=
\frac{2^5}{4!}\widehat C_2(2x)
=
\frac43\widehat C_2(2x),
\]

the corresponding \(C_2\) has a negative Fourier value.

This control still possesses all of the unconditional properties proved above:

- positive even Schwartz kernel;
- arbitrarily strong log-concavity after scaling;
- Stieltjes/Hankel positivity of \(\{C_n(u)\}\) for every \(u\);
- positive-definite generating mixture \(B_y\) for every real \(y\).

Yet coefficientwise Fourier positivity fails already at \(n=2\).

Therefore:

\[
\boxed{
\text{strong log-concavity}
+
\text{pointwise Hankel positivity}
+
\text{positive-definite generating mixture}
\not\Rightarrow
\widehat C_n\ge0\ \forall n.
}
\]

This is a genuine no-go boundary. Any successful Riemann-specific proof must use additional structure beyond those three generic properties.

## 8. Gaussian saturation control

For

\[
K(t)=e^{-at^2},
\]

\[
C_n(u)
=
e^{-2au^2}
\frac{\Gamma(n+\tfrac12)}
{(2a)^{n+1/2}}.
\]

Here

\[
-(\log K)''=2a
\]

and

\[
-(\log C_n)''=4a,
\]

so the inherited factor-of-two curvature bound is sharp.

Also,

\[
B_y(u)
=
e^{-2au^2}
\sqrt{\frac{\pi}{2a}}
e^{y^2/(2a)}
\]

and exactly

\[
\widehat B_y(2x)
=
\frac{\pi}{2a}
e^{(y^2-x^2)/(2a)}
=
\frac12|f(x+iy)|^2.
\]

The deterministic tests use this as a normalization and factor audit.

## 9. Current proof frontier after the no-go

The active chain is now sharper:

\[
\boxed{
\text{theta kernel}
\to
\{C_n\}
\to
\begin{cases}
\text{strong log-concavity},\\
\text{Stieltjes/Hankel positivity in }n,\\
\text{PD generating mixture }B_y
\end{cases}
}
\]

but these generic properties do not imply

\[
\widehat C_n\ge0.
\]

Therefore the next admissible attack must exploit a **Riemann-specific compatibility** absent from the oscillatory-Gaussian control.

Candidate structures that remain legitimate to test are:

- the exact theta-channel decomposition and its \(n^2\)-ordered exponential suppression;
- modular self-duality of the Riemann kernel;
- the G025 logarithmic-derivative/Stieltjes hierarchy;
- a cross-order identity coupling the Fourier transforms of different \(C_n\), stronger than pointwise Hankel positivity.

A generic shape theorem for \(C_n\) alone cannot close RH.

## 10. Proof firewall

**EXACT / PROVED**

1. joint Hessian bound \(\nabla^2V_n\ge2\kappa I\);
2. strong-log-concavity inheritance \( -(\log C_n)''\ge2\kappa\);
3. the first radial monotonicity gate for every \(n\);
4. Stieltjes moment representation of \(C_n(u)\) in hierarchy order;
5. all fixed-\(u\) Hankel matrices are positive semidefinite;
6. generating identity for \(B_y\);
7. \(\widehat B_y(2x)=|f(x+iy)|^2/2\);
8. explicit oscillatory-Gaussian curvature lower bound;
9. exact Fourier transform and scaling law for that control;
10. negative \(L_2\) witness, hence failure of coefficientwise Fourier positivity.

**STANDARD EXTERNAL THEOREM**

Strong log-concavity is preserved by marginalization (strong Prékopa / Brascamp–Lieb). A convenient review is Saumard–Wellner, *Log-concavity and strong log-concavity: a review*, Statistics Surveys 8 (2014), Theorem 3.8.

**FINITE REGRESSION**

The accompanying v0.4 test module contains six tests; all six pass in the staging computation. The deterministic receipt records the Gaussian saturation identities and the oscillatory-Gaussian negative gate.

**OPEN**

1. the additional Riemann-specific structure forcing \(\widehat C_n\ge0\);
2. global positivity of all \(L_n[\Xi](x)\);
3. RH.
