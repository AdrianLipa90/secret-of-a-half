# SOH Conservative Yoshida High-Mode Cutoff Growth v0.1

Status: **EXACT_ASYMPTOTIC_OF_CURRENT_SUFFICIENT_CERTIFICATE / NEGATIVE_INDEX_ENVELOPE_EXPLICIT / MINIMAL_CUTOFF_UNKNOWN**

Date: 2026-09-26

Parents:
- \`src/secret_of_a_half/c005_yoshida_high_mode.py\`
- \`src/secret_of_a_half/c005_yoshida_gamma_window.py\`
- \`research/SOH_C005_YOSHIDA_EXPLICIT_FOURIER_TAIL_V0_1.md\`
- \`research/SOH_LOCALIZED_WEIL_NEGATIVE_INDEX_MONOTONICITY_V0_1.md\`

No RH and no zero list are used.

## 1. Scope

The repository already contains a constructive source-level Yoshida/Suzuki
high-mode certificate.  This note asks only how the cutoff produced by that
**particular conservative certificate** grows as the localization radius
\(a\to\infty\).

It does not identify that cutoff with the minimal coercivity threshold.

Fix:
\[
\mu>0,
\qquad
\delta_C>0
\]
independent of \(a\).

Set
\[
a_0=a
\]
and choose the explicit auxiliary radius
\[
\boxed{
a_1(a)=a+\frac1a.
}
\]

Then \(a_1>a_0\) for every \(a>0\), while
\[
a_1-a\to0.
\]

## 2. Source constants at \(c=2\)

The implemented certificate uses
\[
C_1=\frac56
\]
and
\[
C_2(a_1)
=
\frac{e^{4a_1}-1}{4a_1}.
\]

Put
\[
p(a)=C_1C_2(a_1).
\]

Then
\[
p(a)
=
\frac{5}{24}
\frac{e^{4a_1}-1}{a_1}.
\]

Since
\[
a_1=a+\frac1a,
\]
we have
\[
e^{4a_1}
=
e^{4a}e^{4/a}
=
e^{4a}(1+o(1))
\]
and
\[
a_1=a(1+o(1)).
\]

Therefore
\[
\boxed{
p(a)
\sim
\frac{5}{24}\frac{e^{4a}}{a}.
}
\]

## 3. Chosen bulk constant

The implemented normalization-safe choice is
\[
C(a)
=
3p(a)+\pi\mu+\delta_C.
\]

Hence
\[
\boxed{
C(a)
\sim
\frac58\frac{e^{4a}}{a}.
}
\]

The gamma-window routine chooses
\[
\boxed{
t_0(a)
=
2\sqrt\pi\,e^{C(a)+1}.
}
\]

Consequently
\[
\boxed{
\log t_0(a)
=
C(a)+1+\log(2\sqrt\pi).
}
\]

Thus the source gamma window is already exponentially large in
\(C(a)\), which itself is exponentially large in \(a\).

## 4. Compact gamma constant

The implemented upper envelope is
\[
C_0(a)
=
\log r_{\max}(t_0)
+
16\left(\frac{\sqrt2}{6}-\frac18\right)
-\frac12\log\pi,
\]
with
\[
r_{\max}(t_0)
=
\sqrt{\frac1{16}+\frac{t_0^2}{4}}.
\]

As \(a\to\infty\),
\[
\log r_{\max}(t_0)
=
\log t_0-\log2+o(1),
\]
so
\[
\boxed{
C_0(a)=C(a)+O(1).
}
\]

## 5. Leakage coefficient

The exact implemented leakage coefficient is
\[
B(a,t_0)
=
\frac{8a}{\pi^2}
\left(
t_0
+
at_0^2
+
\frac{a^2t_0^3}{3}
\right).
\]

Because \(t_0\to\infty\),
\[
B(a,t_0)
\sim
\frac{8}{3\pi^2}
a^3t_0^3.
\]

Therefore
\[
\boxed{
\log B(a,t_0)
=
3C(a)+3\log a+O(1).
}
\]

## 6. Required sufficient cutoff

The source-level floor is
\[
\nu_N
=
\frac{
C-2p-(C+C_0)B/N
}{\pi}.
\]

To certify
\[
\nu_N\ge\mu,
\]
the implemented cutoff is the ceiling of
\[
N_*(a)
=
\frac{
(C+C_0)B
}{
C-2p-\pi\mu
}.
\]

For the chosen \(C\),
\[
C-2p-\pi\mu
=
p+\delta_C.
\]

Also
\[
C+C_0=2C+O(1)
\]
and
\[
C/p\to3.
\]

Hence
\[
\frac{C+C_0}{p+\delta_C}\to6.
\]

Therefore
\[
\boxed{
N_*(a)
\sim
6B(a,t_0).
}
\]

In particular
\[
\boxed{
\log N_*(a)
=
3C(a)+3\log a+O(1)
}
\]
and
\[
\boxed{
\log N_*(a)
\sim
\frac{15}{8}\frac{e^{4a}}{a}.
}
\]

Taking another logarithm gives the clean scale law
\[
\boxed{
\log\log N_*(a)
=
4a-\log a+\log\frac{15}{8}+o(1).
}
\]

The integer ceiling
\[
N_{\rm cert}(a)=\lceil N_*(a)\rceil
\]
has the same asymptotics.

## 7. Interpretation

The present \(c=2\) certificate therefore has a **double-exponential** sufficient
cutoff in the localization radius.

Equivalently,
\[
\boxed{
N_{\rm cert}(a)
=
\exp\!\left[
\left(\frac{15}{8}+o(1)\right)
\frac{e^{4a}}{a}
\right].
}
\]

This is a statement about the current proof certificate, not about the true
operator.

It does not show that the actual minimal high-mode threshold grows
double-exponentially.

The dominant source of pessimism is visible:
\[
C_2(a_1)
\sim e^{4a}/a
\]
forces a huge \(C\), and the conservative gamma-window choice exponentiates
that constant once more.

## 8. Exact negative-index envelope

Whenever the source high-mode theorem is transported to the localized
Friedrichs form at scale \(a\), strict positivity on the Fourier tail
\[
|n|>N_{\rm cert}(a)
\]
implies the exact dimension bound
\[
\boxed{
\kappa_a=n_-(A_a)
\le
2N_{\rm cert}(a)+1.
}
\]

Thus the current certificate gives a fully explicit but astronomically loose
upper envelope on the Pontryagin index.

Combined with index monotonicity,
\[
\kappa_{a_1}\le\kappa_{a_2},
\]
the project now has both:
- a monotone lower-history constraint on any defect that has appeared;
- a constructive finite upper envelope at every fixed \(a\).

## 9. What this does not say about defect escape

Because high-block positivity does not force negative eigenvectors to have
literal low-Fourier support, the growth of \(N_{\rm cert}(a)\) alone does not
prove either compact obstruction or defect escape.

Moreover the current sufficient cutoff is so loose that even a
frequency-localization interpretation would allow enormous migration.

Therefore the result **fails to obstruct** the Pontryagin escape lane.

That failure is informative: the next useful theorem must sharpen the
certificate or control the generalized-Schur/Feshbach transfer directly.

## 10. Optimization frontier

The current asymptotic is tied to:
- contour choice \(c=2\);
- the safe bound
  \[
  C_2(a_1)\le\frac{e^{4a_1}-1}{4a_1};
  \]
- the conservative gamma threshold
  \[
  t_0=2\sqrt\pi e^{C+1}.
  \]

A meaningful optimization programme is therefore:

### YHC-OPT1 — general contour
Derive \(C_1(c)\), \(C_2(a_1,c)\) and the source lower bound for admissible
\(c\), then optimize \(c=c(a)\).

### YHC-OPT2 — direct gamma inversion
Replace the sufficient exponential rule for \(t_0(C)\) by a certified inverse
of the explicit digamma lower envelope.

### YHC-OPT3 — minimal-vs-sufficient cutoff
Separate the true minimal coercivity cutoff from the current certificate and
seek a lower-complexity sufficient family.

Only after such optimization can cutoff growth become strong evidence about
the location of the Pontryagin defect.

## 11. Compact theorem

For fixed \(\mu,\delta_C>0\), choose
\[
a_0=a,
\qquad
a_1=a+a^{-1},
\]
and use the current repository \(c=2\) high-mode certificate.

Then its sufficient cutoff satisfies
\[
\boxed{
\log\log N_{\rm cert}(a)
=
4a-\log a+\log\frac{15}{8}+o(1).
}
\]

Equivalently,
\[
\boxed{
N_{\rm cert}(a)
=
\exp\!\left[
\left(\frac{15}{8}+o(1)\right)
\frac{e^{4a}}{a}
\right].
}
\]

If strict high-mode positivity is transported to \(A_a\), then
\[
\boxed{
n_-(A_a)\le2N_{\rm cert}(a)+1.
}
\]

No minimal-cutoff claim and no RH claim is made.
