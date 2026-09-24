# SOH Half-Kernel Wronskian Completion v0.3

Status: `EXACT_WRONSKIAN_COMPLETION_IDENTITY / BLOCKWISE_POSITIVITY_FAIL_NUMERICAL / G024_THIRD_ORDER_OPEN / RH_OPEN`

Date: 2026-09-14

Let
\[
p(z)=z^2+\frac14,
\qquad
\Xi(z)=p(z)g(z),
\]
where `g` is the Fourier transform of the corrected Green carrier from v0.2.  Define the Laguerre/Wronskian functional
\[
W_f=f'^2-ff''.
\]
For any product `f=pg`, direct differentiation gives
\[
W_f=p^2W_g+(p'^2-pp'')g^2.
\]
Since `p'=2z` and `p''=2`,
\[
\boxed{
W_\Xi(z)
=p(z)^2W_g(z)
+2\left(z^2-\frac14\right)g(z)^2.
}
\]
This is the exact completion decomposition of the external Dimitrov--Xu/Laguerre functional already used by SOH-G024.

The identity does not split the RH-equivalent sign problem into two positive problems.  Finite high-precision witnesses show the opposite.  At `z=0+0.2 i`, the stripped term has positive real part while the completion defect has negative real part.  At `z=1+0.2 i`, their signs reverse.  In both cases the full sum remains positive on the diagnostic point.

Thus independent blockwise positivity is rejected as a stronger route:
\[
\boxed{
\Re[p^2W_g]\ge0\ \text{and}\
\Re[2(z^2-1/4)g^2]\ge0
\quad\text{globally}
}
\]
is false.  The full cancellation must be retained.

This exactly matches the existing SOH/XF lesson that local positive pieces are insufficient: the admissible target is the coupled global kernel/function, not separately signed completion blocks.

The current G024 proof frontier remains the third complete-monotonicity condition
\[
-H_y'''(q)\ge0,
\]
or an equivalent direct proof of the full external Wronskian sign.  v0.3 supplies a completion-aware normal form for that search; it does not promote RH.

Proof firewall:

- exact: product-Wronskian identity and its specialization to `p=z^2+1/4`;
- numerical no-go: sign-reversal witnesses for the two separate summands;
- open: global coupled Wronskian positivity, G024 order three and higher, RH.
