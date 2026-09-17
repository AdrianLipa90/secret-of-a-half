# SOH-G025 — Square quotient, Stieltjes log derivative, and dual Gram gates

**Status:** `EXACT_ALGEBRAIC_REDUCTION / STANDARD_EXTERNAL_STIELTJES_CRITERION / FIRST_FINITE_GATES_EXPOSED / RH_OPEN`  
**Branch:** `research/soh-g025-stieltjes-square-quotient-v1`  
**Date:** 17 September 2026

## 1. Scope and firewall

SOH-G001 already gives the exact quotient factorization

\[
\xi\!\left(\frac12+z\right)=F(z^2),
\]

with \(F\) entire and positive Taylor coefficients, and reduces RH to real-rootedness
of \(F\), equivalently to all zeros of \(F\) lying on \(( -\infty,0)\).

This note does **not** claim RH. It adds an exact crosswalk from the square
quotient to:

1. the logarithmic derivative \(F'/F\);
2. a Stieltjes moment sequence;
3. two Hankel/Gram positivity families;
4. the Stieltjes continued fraction (S-fraction);
5. a first explicit ratio-curvature gate beyond the existing PF2 statement.

The external Stieltjes/logarithmic-derivative criterion is recorded as
`STANDARD_EXTERNAL_THEOREM`; all finite algebra below is `EXACT`.

## 2. Logarithmic derivative moments

Write

\[
F(w)=\sum_{k\ge0}a_k w^k,\qquad a_0>0,
\]

and define

\[
\phi(w):=\frac{F'(w)}{F(w)}
       =\sum_{n\ge0}(-1)^n\mu_n w^n.
\]

The first moments are

\[
\boxed{\mu_0=\frac{a_1}{a_0}},
\]

\[
\boxed{\mu_1=
\frac{a_1^2-2a_0a_2}{a_0^2}},
\]

and

\[
\boxed{
\mu_2=
\frac{a_1^3-3a_0a_1a_2+3a_0^2a_3}{a_0^3}.
}
\]

For an entire function \(F\) with \(F(0)\neq0\), the classical
logarithmic-derivative criterion says that

\[
F\in\mathcal{LP}^+
\]

is equivalent to \((\mu_n)_{n\ge0}\) being a Stieltjes moment sequence. In
the SOH normalization, because G001 already identifies RH with all quotient
zeros being real negative,

\[
\boxed{
\mathrm{RH}
\iff
(\mu_n)_{n\ge0}\text{ is a Stieltjes moment sequence}.
}
\]

This is an RH-equivalent reformulation, not a proof.

If RH holds and the quotient zeros are \(-\lambda_j\) with \(\lambda_j>0\),
then

\[
\phi(w)=\sum_j\frac{1}{w+\lambda_j}
       =\int_0^\infty\frac{d\nu(x)}{1+wx},
\]

after the reciprocal reparametrization
\(x=\lambda_j^{-1}\) with the corresponding positive atomic weights. Thus

\[
\mu_n=\int_0^\infty x^n\,d\nu(x).
\]

For the Riemann quotient one may take \(\lambda_j=\gamma_j^2\) under RH.

## 3. Dual Stieltjes Hankel gates

A real sequence is a Stieltjes moment sequence iff both Hankel families

\[
H_N^{(0)}=[\mu_{i+j}]_{i,j=0}^{N},
\qquad
H_N^{(1)}=[\mu_{i+j+1}]_{i,j=0}^{N}
\]

are positive semidefinite for every \(N\).

Therefore the square-quotient route can be encoded as

\[
\boxed{
\mathrm{RH}
\iff
H_N^{(0)}\succeq0
\ \text{and}\
H_N^{(1)}\succeq0
\quad\forall N\ge0.
}
\]

A convenient non-negative defect functional is

\[
\Delta_{\rm RH}
:=
\sup_{N\ge0}
\max\!\left(
0,
-\lambda_{\min}H_N^{(0)},
-\lambda_{\min}H_N^{(1)}
\right).
\]

At the level of this exact reformulation,

\[
\boxed{\mathrm{RH}\iff\Delta_{\rm RH}=0.}
\]

This definition is only a compression of the moment problem; it does not
supply the missing positivity proof.

## 4. Gram-kernel realization

If

\[
\phi(w)=\int_0^\infty\frac{d\nu(x)}{1+wx},
\]

then define

\[
K_0(w,v)
=
\frac{w\phi(w)-\bar v\,\overline{\phi(v)}}{w-\bar v},
\]

and

\[
K_1(w,v)
=
\frac{\phi(w)-\overline{\phi(v)}}{\bar v-w}.
\]

Direct algebra gives

\[
\boxed{
K_0(w,v)
=
\int_0^\infty
\frac{d\nu(x)}
{(1+wx)(1+\bar vx)}
}
\]

and

\[
\boxed{
K_1(w,v)
=
\int_0^\infty
\frac{x\,d\nu(x)}
{(1+wx)(1+\bar vx)}.
}
\]

Hence both are Gram kernels. Their Taylor coefficients reproduce the two
Hankel families:

\[
K_0(w,v)
=
\sum_{i,j\ge0}
(-1)^{i+j}\mu_{i+j}w^i\bar v^j,
\]

\[
K_1(w,v)
=
\sum_{i,j\ge0}
(-1)^{i+j}\mu_{i+j+1}w^i\bar v^j.
\]

Multiplying out the logarithmic-derivative poles gives the pole-free kernels

\[
\widehat K_0(w,v)
=
\frac{
wF'(w)\overline{F(v)}
-
\bar vF(w)\overline{F'(v)}
}{
w-\bar v
},
\]

and

\[
\boxed{
\widehat K_1(w,v)
=
\frac{
F(w)\overline{F'(v)}
-
F'(w)\overline{F(v)}
}{
w-\bar v
}.
}
\]

These are the quotient-plane counterparts of the regularized Pick/de Branges
kernel developed in TIR XF-9.

## 5. Stieltjes S-fraction

Let

\[
M(t):=\sum_{n\ge0}\mu_n t^n=\phi(-t).
\]

The classical Stieltjes continued-fraction criterion is

\[
M(t)
=
\cfrac{\alpha_0}{
1-\cfrac{\alpha_1t}{
1-\cfrac{\alpha_2t}{
1-\ddots}}},
\qquad
\alpha_k\ge0.
\]

Thus RH is equivalently encoded by non-negativity of the complete S-fraction
coefficient sequence, subject to the standard entire-function hypotheses.

The first coefficients are

\[
\alpha_0=\mu_0,
\qquad
\alpha_1=\frac{\mu_1}{\mu_0},
\qquad
\alpha_2=
\frac{\mu_0\mu_2-\mu_1^2}{\mu_0\mu_1}.
\]

## 6. Normalized quotient ratios and the first open gate

Define

\[
\gamma_k:=k!\,a_k,
\qquad
r_k:=\frac{\gamma_k}{\gamma_{k-1}}
\quad(k\ge1).
\]

Then

\[
\boxed{\alpha_0=r_1},
\qquad
\boxed{\alpha_1=r_1-r_2}.
\]

The first non-trivial \(2\times2\) Hankel determinant is

\[
D_1
:=
\mu_0\mu_2-\mu_1^2
=
\frac{
3a_0a_1a_3-4a_0a_2^2+a_1^2a_2
}{a_0^3}.
\]

Exactly,

\[
\boxed{
D_1
=
\frac{r_1^2r_2}{2}
\left(r_1-2r_2+r_3\right).
}
\]

Consequently, when the preceding factors are positive,

\[
\boxed{
\alpha_2
=
\frac{r_2}{2}\,
\frac{r_1-2r_2+r_3}{r_1-r_2}.
}
\]

The next gate is therefore simply

\[
\boxed{
r_1-2r_2+r_3\ge0,
}
\]

or

\[
\boxed{
r_1-r_2\ge r_2-r_3.
}
\]

This is discrete convexity of the normalized coefficient ratios. Existing
SOH-G005 PF2 proves monotone ratios but does not by itself prove this stronger
second-difference sign.

If \(p_k=a_k/a_{k-1}\), then \(r_k=kp_k\), so the same gate is

\[
\boxed{
p_1-4p_2+3p_3\ge0.
}
\]

This interfaces directly with the ratio-curvature language already used by
SOH-G006.

## 7. Moment form of the first open determinant

With the existing SOH normalization

\[
a_k=\frac{m_k}{(2k)!},
\qquad
m_k=\int_0^\infty y^{2k}\Phi(y)\,dy,
\]

the determinant condition becomes

\[
\boxed{
D_1\ge0
\iff
3m_0m_1m_3
-10m_0m_2^2
+15m_1^2m_2
\ge0.
}
\]

This cubic moment inequality is not identified here with the standard
double-Turán inequality. No implication from the Planat--Solé
second-level-concavity result is promoted without a separate derivation.

## 8. Relation to earlier SOH gates

The current hierarchy is:

```text
G001 exact square quotient
    -> G005 PF2 / monotone coefficient ratios
    -> G006 PF3 ratio-curvature frontier
    -> G025 Stieltjes dual-Hankel / S-fraction frontier
```

G025 does not replace G006. It exposes a different finite gate whose
completion would certify the next Stieltjes coefficient.

The immediate analytic target is

\[
\boxed{
r_1-2r_2+r_3\ge0.
}
\]

The long-range target is positivity of both Stieltjes Hankel families at all
orders, equivalently all S-fraction coefficients \(\alpha_k\ge0\).

## 9. Executable exact algebra

`src/secret_of_a_half/stieltjes_square_quotient.py` implements:

- formal-series extraction of \(\mu_n=(-1)^n[w^n]F'/F\);
- Hankel matrix construction;
- exact \(2\times2\) determinant;
- normalized ratios \(r_k\);
- the G025 ratio gate \(r_1-2r_2+r_3\);
- \(\alpha_0,\alpha_1,\alpha_2\) in the stated S-fraction convention.

`tests/test_stieltjes_square_quotient.py` uses exact rational arithmetic and a
negative-real-root fixture. The tests validate algebra only; they do not
promote an RH-level sign.

## 10. Epistemic ledger

| Claim | Status |
|---|---|
| `xi(1/2+z)=F(z^2)` | EXACT, inherited G001 |
| RH iff quotient zeros are all real negative | EXACT reduction, inherited G001 |
| LP+ iff log-derivative coefficients form a Stieltjes moment sequence | STANDARD_EXTERNAL_THEOREM |
| Stieltjes iff both Hankel families are PSD | STANDARD_EXTERNAL_THEOREM |
| Stieltjes iff S-fraction coefficients are non-negative | STANDARD_EXTERNAL_THEOREM |
| formulas for mu0, mu1, mu2 | EXACT |
| dual Gram kernels K0, K1 | EXACT_CONDITIONAL on a Stieltjes representation |
| pole-free kernels | EXACT algebra |
| D1 formula | EXACT |
| D1 iff `r1-2r2+r3 >= 0` under positive prefactors | EXACT |
| full Stieltjes positivity for the Riemann quotient | OPEN / RH_EQUIVALENT |
| Riemann hypothesis | OPEN |

## References

- A. D. Sokal, *When does a hypergeometric function belong to the
  Laguerre--Pólya class LP+?*, J. Math. Anal. Appl. **515** (2022), 126432;
  see the logarithmic-derivative and Stieltjes continued-fraction criteria.
- A. D. Sokal and J. Walrad, *Continued-fraction characterization of
  Stieltjes moment sequences with support in [xi, infinity)*,
  arXiv:2404.12131 (2024).
- G. Csordas, *Fourier transforms of positive definite kernels and the
  Riemann xi-Function*, arXiv:1309.0055.
- J. C. Lagarias, *On a positivity property of the Riemann xi-function*,
  Acta Arith. **89** (1999), 217--234, with correction in Acta Arith.
  **116** (2005), 293--294.
