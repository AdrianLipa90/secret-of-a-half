# SOH-C005 Explicit Yoshida Fourier-Tail Bound v0.1

Status: **EXACT ELEMENTARY SHARPENING OF A PRIOR-ART STEP / RH OPEN**

Scope: make the Fourier-tail estimate used in Suzuki 2023 Theorem 4.3 explicit enough to produce a computable high-mode schedule. This is not a proof of Weil positivity.

## 1. Starting inequality

For \(\psi\in K_N(a)\), Suzuki's proof (following Yoshida) expands

\[\psi(t)=(2a)^{-1/2}\sum_{|n|>N}c_n e^{\pi i n t/a}\]

with \(\|\psi\|_2^2=\sum_{|n|>N}|c_n|^2\). Integration by parts and Cauchy--Schwarz give, for real \(z\),

\[|\widehat\psi(z)|\le \sqrt{2a}(1+a|z|)\left(\sum_{|n|>N}\frac1{(\pi n)^2}\right)^{1/2}\|\psi\|_2.\]

Put

\[S_N:=\sum_{|n|>N}\frac1{(\pi n)^2}=\frac{2}{\pi^2}\sum_{n=N+1}^{\infty}\frac1{n^2}.\]

For \(N\ge1\), the integral test gives

\[\boxed{S_N\le \frac{2}{\pi^2N}}.\]

## 2. Explicit low-frequency leakage

Squaring the pointwise estimate and integrating over \(|z|\le t_0\) yields

\[\int_{|z|\le t_0}|\widehat\psi(z)|^2dz\le 4aS_N\left(t_0+a t_0^2+\frac{a^2t_0^3}{3}\right)\|\psi\|_2^2.\]

Hence

\[\boxed{\frac{\int_{|z|\le t_0}|\widehat\psi(z)|^2dz}{\|\psi\|_2^2}\le \frac{8a}{\pi^2N}\left(t_0+a t_0^2+\frac{a^2t_0^3}{3}\right)}.\]

Uniformly for \(0<a\le a_0\),

\[\boxed{R_N(a)\le \frac{B(a_0,t_0)}{N}}\]

with

\[B(a_0,t_0):=\frac{8a_0}{\pi^2}\left(t_0+a_0t_0^2+\frac{a_0^2t_0^3}{3}\right).\]

This is a fully explicit \(O(N^{-1})\) bound for the integrated squared leakage. Suzuki only needs a weaker \(O(N^{-1/2})\) statement at this point.

## 3. Computable schedule consequence

For any requested leakage tolerance \(\eta>0\), it is sufficient to choose

\[\boxed{N\ge \left\lceil\frac{B(a_0,t_0)}{\eta}\right\rceil}.\]

This does not by itself give the final coercivity constant, because the constants \(C,C_0,C_1,C_2,t_0\) in Suzuki's lower bound (4.11) still need to be frozen in exactly the repository normalization. But it removes the nonconstructive Fourier-tail part of the schedule once those constants are fixed.

## 4. Relevance to the current C005 architecture

The existing Hermite route treated the high-index complement as an open asymptotic problem. In the Yoshida Fourier split, high-mode coercivity is prior art, and the estimate above makes the low-frequency leakage schedule explicit. The active proof burden moves to:

1. exact normalization/domain crosswalk to the repository's \(Q_W^a/A_a\);
2. explicit constants in the Suzuki/Yoshida lower bound;
3. finite low-mode block and Schur coupling for all \(a>0\);
4. an all-scale continuation argument.

## 5. Proof firewall

No zero locations, RH, Li positivity, global Weil positivity, or spectral-zero lists are used in the derivation above.

`proof_of_rh = false`
