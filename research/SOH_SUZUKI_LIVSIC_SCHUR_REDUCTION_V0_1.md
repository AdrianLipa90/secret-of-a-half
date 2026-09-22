# SOH Suzuki–Livšic Schur Reduction v0.1

Status: **EXACT FINITE-\(a\) SCHUR LEMMA / ZERO-FREE RH REDUCTION / ANALYTIC INCOMING EDGE OPEN**

Source baseline:

- repository main: eeb93832f0e72c2fa86ec427900c708dfe86fd10;
- primary source: Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096v2 (17 August 2026);
- Suzuki Theorem 1.5: finite-\(a\) characteristic functions have only real zeros;
- Suzuki Corollary 1.6 in **v2** targets
  \[
  \frac{\xi(1/2-iz)}
       {\xi(1/2-iz)+\xi'(1/2-iz)}.
  \]

This note supersedes, for current-v2 proof search only, any repository working note that still treats
\(z^2\xi/\xi'\) as the Corollary 1.6 target. Historical notes are not rewritten.

No proof of RH is claimed.

---

## 1. Finite-\(a\) characteristic quotient

Fix \(a>0\) and choose \(\lambda<\lambda_a\), as in Suzuki Section 6. Let
\(\mathscr D_a\) be the symmetric first-order operator on \(\mathcal H(T_a)\),
with deficiency indices \((1,1)\). Choose deficiency vectors

\[
\mathscr D_a^*v_\pm=\pm i v_\pm,
\qquad
\|v_+\|_{T_a}=\|v_-\|_{T_a}=N_a>0.
\]

For the Riesz/evaluation vector \(v_z\),

\[
\mathscr D_a^*v_z=zv_z.
\]

Suzuki's boundary-form calculation gives

\[
W(v_z,w_\theta)
=
(z+i)\langle v_z,v_+\rangle_{T_a}
+
e^{-i\theta}(z-i)\langle v_z,v_-\rangle_{T_a}.
\]

Define

\[
A_a(z):=\langle v_z,v_+\rangle_{T_a},
\qquad
B_a(z):=\langle v_z,v_-\rangle_{T_a},
\]

and the normalized characteristic quotient

\[
\boxed{
\chi_{a,\lambda}(z)
:=
-\frac{(z-i)B_a(z)}
       {(z+i)A_a(z)}.
}
\]

Whenever \(z\) is a zero of the characteristic function of the extension
labelled by \(\theta\),

\[
\chi_{a,\lambda}(z)=e^{i\theta}.
\]

The quotient is holomorphic in the open upper half-plane because Suzuki's
Fourier representation makes \(A_a,B_a\) entire and the denominator is
nonzero there by the positivity identity below.

---

## 2. Exact finite-\(a\) Schur theorem

Let

\[
v_z=v_0+\alpha v_+ + \beta v_-,
\qquad
v_0\in\mathfrak D(\overline{\mathscr D_a}).
\]

The boundary form vanishes on the closure domain. With the inner-product
convention used by Suzuki,

\[
W(v_+,v_+)=2iN_a^2,
\qquad
W(v_-,v_-)=-2iN_a^2,
\qquad
W(v_+,v_-)=0.
\]

Therefore

\[
W(v_z,v_z)
=
2iN_a^2\left(|\alpha|^2-|\beta|^2\right).
\]

On the other hand, since \(\mathscr D_a^*v_z=zv_z\),

\[
W(v_z,v_z)
=
(z-\bar z)\|v_z\|_{T_a}^2
=
2i\,\Im z\,\|v_z\|_{T_a}^2.
\]

Hence

\[
\boxed{
N_a^2\left(|\alpha|^2-|\beta|^2\right)
=
\Im z\,\|v_z\|_{T_a}^2.
}
\tag{2.1}
\]

Pairing with \(v_\pm\) gives

\[
\alpha
=
\frac{(z+i)A_a(z)}{2iN_a^2},
\qquad
\beta
=
-\frac{(z-i)B_a(z)}{2iN_a^2}.
\]

Thus

\[
\chi_{a,\lambda}(z)=\frac{\beta}{\alpha}.
\]

For \(\Im z>0\), (2.1) implies \(|\alpha|>|\beta|\), hence

\[
\boxed{
|\chi_{a,\lambda}(z)|<1
\qquad(\Im z>0).
}
\tag{2.2}
\]

Moreover \(z=i\) lies in the \(+i\) deficiency space, so

\[
\boxed{\chi_{a,\lambda}(i)=0.}
\tag{2.3}
\]

This is exactly the Schur/Livšic geometry of the finite-\(a\) symmetric
operator. It requires neither RH nor positivity of \(A_a\); it requires only
the admissible shift \(\lambda<\lambda_a\) already used in Suzuki's
unconditional construction.

---

## 3. Quantitative Cayley bound

From (2.1),

\[
1-|\chi_{a,\lambda}(z)|^2
=
\frac{4\,\Im z\,N_a^2\|v_z\|_{T_a}^2}
{|z+i|^2|A_a(z)|^2}.
\]

Cauchy--Schwarz gives

\[
|A_a(z)|^2
\le
N_a^2\|v_z\|_{T_a}^2.
\]

Therefore

\[
1-|\chi_{a,\lambda}(z)|^2
\ge
\frac{4\,\Im z}{|z+i|^2},
\]

or equivalently

\[
\boxed{
|\chi_{a,\lambda}(z)|
\le
\left|\frac{z-i}{z+i}\right|
<1
\qquad(\Im z>0).
}
\tag{3.1}
\]

The bound is independent of \(a\) and of the admissible \(\lambda\).

This is the Schwarz--Pick bound normalized at \(i\), obtained directly from
Suzuki's boundary form.

---

## 4. HOUND firewall: reject zero-conditioned boundary saturation

A tempting incoming statement is

\[
\xi(\rho)=0
\Longrightarrow
\limsup_{a\to\infty}
|\chi_{a,\lambda(a)}(i(\rho-\tfrac12))|=1.
\]

This must **not** be promoted as independent progress.

Indeed, if \(\Re\rho>1/2\), then

\[
z_\rho=i(\rho-\tfrac12)
\]

lies in the open upper half-plane, and (3.1) gives the strict \(a\)-uniform
bound

\[
|\chi_{a,\lambda(a)}(z_\rho)|
\le
\left|\frac{z_\rho-i}{z_\rho+i}\right|
<1.
\]

Therefore boundary saturation at every zeta zero already excludes off-axis
zeros. It packages the desired conclusion into a zero-conditioned premise.

The previous working target called LAST is therefore rejected as a
**non-circular incoming theorem target**.

---

## 5. Infinite normalized characteristic dictated by Suzuki v2

Put

\[
f(z):=\xi\!\left(\frac12-iz\right),
\]

and define the real constants

\[
A:=\xi(3/2),
\qquad
B:=\xi'(3/2).
\]

Suzuki Section 7 uses

\[
E(z)=f(z)+if'(z),
\qquad
E^\#(z)=f(z)-if'(z),
\]

equivalently \(E(z)=\xi(1/2-iz)+\xi'(1/2-iz)\).

Writing

\[
q(z)=\frac{E^\#(z)}{E(z)},
\]

Suzuki's infinite-model boundary equation is

\[
q(z)=\frac{C_\theta}{\overline{C_\theta}},
\qquad
C_\theta
=
A\cos\frac\theta2+iB\sin\frac\theta2.
\]

Solving algebraically for \(t=e^{i\theta}\) gives the normalized infinite
characteristic candidate

\[
\boxed{
\chi_\infty(z)
=
\frac{(A+B)q(z)-(A-B)}
     {(A+B)-(A-B)q(z)}.
}
\tag{5.1}
\]

Eliminating \(q\) gives the pole-safe cross-multiplied form

\[
\boxed{
\chi_\infty(z)
=
\frac{Bf(z)-iAf'(z)}
     {Bf(z)+iAf'(z)}
}
\tag{5.2}
\]

wherever the denominator is nonzero, with removable continuation where
appropriate.

At \(z=i\),

\[
\chi_\infty(i)=0,
\]

matching the finite normalization.

If \(z_0\) is any zero of \(f\), of multiplicity \(m\ge1\),

\[
f(z)=(z-z_0)^m h(z),
\qquad h(z_0)\ne0,
\]

so after cancellation,

\[
\boxed{
\chi_\infty(z_0)=-1.
}
\tag{5.3}
\]

This conclusion is independent of the zero multiplicity.

---

## 6. Zero-free Vitali/normal-family reduction to RH

The finite family

\[
\{\chi_{a,\lambda}\}
\]

is locally bounded by one in the upper half-plane by (2.2), hence is a normal
family.

Choose any sequence \(a_n\to\infty\) and admissible shifts

\[
\lambda_n<\lambda_{a_n}.
\]

Let \(Y\subset(1/2,\infty)\) have an accumulation point in
\((1/2,\infty)\). The points

\[
z=iy,\qquad y\in Y,
\]

lie in the upper half-plane and correspond to

\[
s=\frac12+y>1,
\]

where the Dirichlet/Euler-product representation of zeta is absolutely
convergent and no zeta zero is being used as input.

Assume the **zero-free scalar convergence condition**

\[
\boxed{
\chi_{a_n,\lambda_n}(iy)
\longrightarrow
\frac{Bf(iy)-iAf'(iy)}
     {Bf(iy)+iAf'(iy)}
\qquad
(y\in Y).
}
\tag{6.1}
\]

Then Montel/Vitali gives a subsequential holomorphic Schur limit
\(\chi:\mathbb H\to\overline{\mathbb D}\). Define the entire functions

\[
N(z):=Bf(z)-iAf'(z),
\qquad
D(z):=Bf(z)+iAf'(z).
\]

On \(iY\),

\[
D(z)\chi(z)-N(z)=0.
\]

Because \(iY\) has an accumulation point inside the upper half-plane, the
identity theorem yields

\[
\boxed{
D(z)\chi(z)=N(z)
\qquad(z\in\mathbb H).
}
\tag{6.2}
\]

Suppose \(f(z_0)=0\) for some \(z_0\in\mathbb H\), with multiplicity \(m\).
Divide (6.2) by \((z-z_0)^{m-1}\) and let \(z\to z_0\). Since
\(A=\xi(3/2)\ne0\),

\[
iAmh(z_0)\chi(z_0)
=
-iAmh(z_0),
\]

hence

\[
\chi(z_0)=-1.
\]

But \(\chi(i)=0\), so \(\chi\) is not the constant function \(-1\). A
nonconstant holomorphic map into the closed unit disk cannot attain modulus
one at an interior point. Contradiction.

Therefore \(f\) has no zero in the upper half-plane. Functional symmetry gives
the same conclusion in the lower half-plane. Hence every nontrivial zeta zero
has

\[
\Re\rho=\frac12.
\]

Thus:

\[
\boxed{
\text{zero-free scalar convergence (6.1)}
\Longrightarrow
\mathrm{RH}.
}
\]

This is a strictly better proof-search target than convergence imposed at the
unknown zeta zeros.

---

## 7. The convergence condition is only scalar resolvent data

Suzuki Section 6.3 proves

\[
v_z=T_a^{-1}e_z,
\qquad
e_z(x)=e^{-izx}.
\]

Therefore

\[
A_a(z)
=
\langle e_z,T_a^{-1}e_{+i}\rangle_{L^2}
\]

and, up to the fixed phase/normalization chosen for the equal-norm deficiency
basis,

\[
B_a(z)
=
\langle e_z,T_a^{-1}e_{-i}\rangle_{L^2}.
\]

Consequently (6.1) asks only for convergence of the ratio of two scalar
resolvent matrix elements on the zero-free line \(z=iy\), \(y>1/2\).

The required analytic object is therefore not full norm-resolvent convergence
and not global compact convergence of \(W\). It is a scalar matrix-element
limit.

---

## 8. True remaining obstruction: the shift \(\lambda\)

Suzuki's unconditional finite construction requires

\[
\lambda<\lambda_a.
\]

Under RH, \(A_a>0\) and \(\lambda=0\) may be used for all \(a\). Suzuki's
Section 7 heuristic for the infinite de Branges model is explicitly developed
under this positivity assumption.

Therefore the proof search must not silently put \(\lambda=0\) into the
finite family.

Likewise, one must not assume that the spectra or characteristic quotient are
independent of \(\lambda\). Suzuki states this only as an expectation and
explicitly notes that controlling \(\lambda\) is likely important.

A valid proof must do one of the following independently of RH:

1. construct an explicit admissible schedule
   \[
   \lambda(a)<\lambda_a
   \]
   and prove the scalar limit (6.1) for that schedule; or
2. prove a genuine \(\lambda\)-invariance theorem for the normalized
   characteristic data; or
3. replace the \(T_a\)-dependent formulation by an equivalent continuous-kernel
   Fredholm/Wiener--Hopf object for which the limiting normalization can be
   controlled without assuming \(A_a\ge0\).

This is the current fail-closed analytic frontier.

---

## 9. Relation to C005

The existing C005 machinery contains:

\[
\text{Fourier tail}
\to
\text{high-mode coercivity}
\to
\text{resolvent}
\to
\text{Schur complement}.
\]

For the present route it should be retargeted from proving global positivity to
the two scalar quantities

\[
\boxed{
\langle e_{iy},T_a^{-1}e_{+i}\rangle,
\qquad
\langle e_{iy},T_a^{-1}e_{-i}\rangle,
\qquad y>1/2.
}
\]

A Feshbach decomposition can be applied directly to these matrix elements.
This may require substantially less information than a uniform positive lower
bound for the whole completed Weil form.

However, the repository still lacks:

- the exact localized form/domain/Friedrichs join in repository-native
  normalization;
- a certified all-scale control of the relevant inverse;
- a proof that the chosen \(\lambda(a)\) produces the target scalar limit.

Those are open. No positive finite diagnostic is promoted to a theorem.

---

## 10. Proof-search graph after pruning

The current shortest non-circular graph is

\[
\boxed{
\begin{array}{c}
\text{Suzuki finite deficiency theory}\\
\downarrow\\
\chi_{a,\lambda}\in\mathrm{Schur}(\mathbb H),\ \chi_{a,\lambda}(i)=0\\
\downarrow\\
\text{scalar resolvent/Fredholm convergence on }z=iy,\ y>1/2\\
\downarrow\\
\text{Vitali + identity theorem}\\
\downarrow\\
\chi_\infty\in\mathrm{Schur}(\mathbb H)\\
\downarrow\\
f(z_0)=0\Rightarrow\chi_\infty(z_0)=-1\text{ impossible in }\mathbb H\\
\downarrow\\
\mathrm{RH}.
\end{array}
}
\]

Epistemic status:

\[
\boxed{
\begin{aligned}
&\text{finite Schur lemma: EXACT},\\
&\text{Cayley bound: EXACT},\\
&\text{Vitali/identity-theorem endgame: EXACT CONDITIONAL},\\
&\text{scalar resolvent convergence: OPEN},\\
&\text{RH: OPEN}.
\end{aligned}
}
\]

proof_of_rh = false
