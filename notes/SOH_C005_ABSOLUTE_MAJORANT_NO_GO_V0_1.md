# SOH-C005 absolute-majorant no-go lemma v0.1

Status: **EXACT functional-analytic obstruction for the current proof route; not a proof of SOH-C005 or RH.**

## Setup

Let \((\psi_n)_{n\ge 0}\) be the normalized translated/scaled Hermite basis used by the PhaseNav--Weil ladder. For a real frequency \(x\), define the unitary modulation operator

\[
(U_x f)(r)=e^{-2\pi i x r}f(r).
\]

The existing closed transform is exactly the matrix coefficient

\[
\widehat H_{mn}(x)=\langle \psi_m,U_x\psi_n\rangle
\]

up to the already-fixed inner-product convention used in the repository.

Because \((\psi_n)\) is a complete orthonormal basis and \(U_x\) is unitary, Parseval gives, for every fixed \(m\) and real \(x\),

\[
\sum_{n=0}^{\infty}|\widehat H_{mn}(x)|^2
=\|U_x^*\psi_m\|_2^2
=1.
\]

Consequently, for any fixed cutoff \(N\),

\[
\sum_{n\ge N}|\widehat H_{mn}(x)|^2
=1-\sum_{n<N}|\widehat H_{mn}(x)|^2.
\]

For large modulation frequency, the Hermite mass is transported to higher oscillator indices rather than disappearing. Therefore one cannot prove infinite-complement decay merely by replacing every prime-side matrix coefficient with its absolute value and summing the resulting positive majorants over the full Hermite complement.

## Exact consequence for the current C005 route

The finite-window certificate

\[
|T_{mn}^{\rm prime-tail}(Q)|\le B_{mn}(Q)
\]

remains valid whenever its monotonicity condition is satisfied. Likewise, finite rectangular norm bounds obtained from \(B_{mn}(Q)\) remain valid.

However, the implication

\[
\text{finite rectangular absolute majorants}
\Longrightarrow
\|P_NT(I-P_N)\|\to0
\]

is **not available** from absolute majorization alone. A proof of the infinite-complement coupling must retain cancellation/phase information across the arithmetic sum.

## Required replacement mechanism

The prime-side term carries the oscillatory factor induced by the translated Hermite center,

\[
e^{-2\pi i x t_0},\qquad x=\frac{\log n}{2\pi},
\]

hence

\[
e^{-2\pi i x t_0}=n^{-it_0}.
\]

Therefore the next admissible route is to keep the arithmetic phase and rewrite the prime-power sum through Abel/Stieltjes summation against the Chebyshev function

\[
\psi(X)=\sum_{n\le X}\Lambda(n),
\]

or against the twisted cumulative sum

\[
S_{t_0}(X)=\sum_{n\le X}\Lambda(n)n^{-1/2-it_0}.
\]

The proof target is then a cancellation-sensitive bound on the resulting integral/operator kernel, rather than an \(\ell^1\) sum of absolute prime weights.

## Epistemic boundary

Established here:

1. modulation unitarity;
2. Parseval completeness identity for Hermite matrix coefficients;
3. the resulting obstruction to an absolute-value-only infinite-complement proof;
4. necessity of a cancellation-sensitive arithmetic estimate for this route.

Still open:

1. a sufficient unconditional bound for the twisted cumulative prime sum in the exact normalization used here;
2. conversion of that bound into a uniform operator estimate for \(P_NA_a(I-P_N)\);
3. complement lower bound \(\nu_{N,a}\ge0\);
4. SOH-C005;
5. RH.

`proof_of_rh = false`
