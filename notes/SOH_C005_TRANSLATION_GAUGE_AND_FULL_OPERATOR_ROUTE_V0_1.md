# SOH-C005 translation gauge and full-operator route v0.1

Status: **EXACT reduction clarification + OPEN proof route.**

## 1. Translation of the Hermite basis is not a localization of the theorem

For any fixed real center \(\tau\) and width \(w>0\), define

\[
\psi_n^{(\tau,w)}(r)
=
\left(\frac{w}{\sqrt\pi\,2^n n!}\right)^{1/2}
H_n(w(r-\tau))e^{-w^2(r-\tau)^2/2}.
\]

Translation and dilation are invertible continuous automorphisms of Schwartz space and unitary maps on \(L^2(\mathbb R)\). Hence for every single fixed \(\tau\),

\[
\overline{\operatorname{span}\{\psi_n^{(\tau,w)}:n\ge0\}}^{\,\mathcal S}
=\mathcal S(\mathbb R).
\]

Therefore the dense-core implication

\[
\bigl(\forall N:\;W_N^{(\tau)}\succeq0\bigr)
+\text{continuity of the Weil form}
\Longrightarrow
\mathcal W[h]\ge0\quad\forall h\in\mathcal S
\]

requires positivity for one complete translated Hermite basis, not uniform positivity in every \(\tau\).

### Epistemic hygiene

The current numerical profile uses

\[
\tau=14.134725141734695,
\]

the first standard zero ordinate. This does not enter the arithmetic sum as a zero list and is not logically required by the dense-core reduction; nevertheless a proof-oriented implementation should separate:

- `PROOF_BASIS_CENTER`: a fixed zero-independent real constant;
- `VALIDATION_TARGET_ORDINATE`: optional benchmark/falsification fixture.

That separation prevents a coordinate choice from being mistaken for spectral input.

## 2. Why the infinite-complement estimate must be full-operator

The existing finite decomposition is

\[
W=P+C+A+R,
\]

where the symbols denote pole, conductor, archimedean and prime/arithmetic contributions in the repository normalization.

Finite rectangular blocks of every component are computable. However the absolute-majorant no-go shows that the prime component alone is not an appropriate object for an \(M\to\infty\) operator-norm proof: modulation matrix coefficients transport Hermite mass to high indices, and termwise absolute prime weights destroy arithmetic cancellation.

Accordingly the next target is not

\[
\|P_N R(I-P_M)\|\to0
\]

in isolation, but a bound on the complete coupling

\[
\boxed{
\|P_N W(I-P_M)\|
}
\]

or on the localized operator \(A_a\) once its exact repository normalization is wired.

This permits cancellations that are invisible after splitting components and taking absolute values separately.

## 3. Revised C005 block target

For a fixed proof basis center and projection \(P_N\), seek computable quantities

\[
\mu_{N,a},\qquad \varepsilon_{N,a},\qquad \nu_{N,a}
\]

with

\[
P_NA_aP_N\ge\mu_{N,a}P_N,
\]

\[
\|P_NA_a(I-P_N)\|\le\varepsilon_{N,a},
\]

\[
(I-P_N)A_a(I-P_N)\ge\nu_{N,a}(I-P_N),
\]

and finally

\[
\mu_{N,a}\nu_{N,a}\ge\varepsilon_{N,a}^2.
\]

The finite prime-tail certificates remain valid sub-certificates, but they are no longer promoted as a standalone path to the infinite-complement norm.

## Claim boundary

Exact here:

1. translated/scaled Hermite density for any one fixed center;
2. one fixed complete basis is sufficient for the dense-core positivity reduction;
3. the current zero ordinate is not required by that reduction;
4. componentwise absolute prime majorization is insufficient as an infinite-complement strategy, by the separate no-go lemma.

Open:

1. a zero-independent proof-basis implementation;
2. a cancellation-sensitive full-operator complement estimate;
3. a lower bound on the high-index complement;
4. SOH-C005;
5. RH.

`proof_of_rh = false`
