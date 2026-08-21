# SOH-HYB-008 — Peano Global-Domain Reduction

Date: 2026-08-21

Status: research branch only. No RH proof claim. No canonical promotion.

Let `J_eta(u)` be the corrected internal Jensen kernel and define

`rho_eta(u)=J_eta(u)/J_eta(0)`,
`q_eta(u)=-log rho_eta(u)`,
`F_eta(u)=q_eta'(u)^2-(1-exp(-2q_eta(u)))q_eta''(u)`.

Angular concavity is equivalent to `F_eta(u)>=0`.

For the internal measure

`nu_{u,eta}(r) proportional to r^2 cosh(2 eta r) K(u+r)K(u-r)`, `|eta|<1/2`,

set

`A=L'(u+r)+L'(u-r)`,
`B=L''(u+r)+L''(u-r)`,
where `L=-log K`.

Integrated G024 gives `L''>17` and `L''''<20L''` globally.

Exact derivative identities:

`q'=E[A]`,
`q''=E[B]-Var(A)`.

Since

`A=integral_{r-u}^{r+u} L''(s) ds >34u`,

we have `q'(u)>34u`.

The G024-Q Peano identity is

`uB-A=(1/2) integral_{-u}^{u} (u^2-v^2)L''''(r+v) dv`.

Using `L''''<20L''` gives pointwise

`uB-A<10u^2 A`.

Therefore

`u q''-q' <10u^2 q'`

and

`q''<q'(1/u+10u)`.

If `u^2>=1/24`, then

`q'>34u>=1/u+10u`,

so `q'^2>q''`. Since `0<1-exp(-2q)<1` for `u>0`, it follows that

`F_eta(u)>0`

for every

`u>=1/sqrt(24)=0.2041241452319315...`, `|eta|<1/2`.

Thus all former midrange and tail obligations are absorbed into one exact analytic closed domain.

At the origin, symmetry gives `q'(0)=q'''(0)=0`. Writing `q2=q''(0)` and `q4=q''''(0)`, the exact expansion is

`F_eta(u)=(q2/4)(2q2^2-q4)u^4+O(u^6)`.

The kernel inputs imply `q2>34` and `q4<20q2`, so the quartic leading coefficient is uniformly greater than `13872`. Hence a nonzero analytic neighborhood of the origin is proved positive.

Current remaining obligation:

`0<u<1/sqrt(24)`, uniformly for `|eta|<1/2`.

This is the only angular-core gap in the HYB-008 reduction.

Promotion firewall:

- finite diagnostics do not prove the remaining compact core;
- local Taylor positivity without an explicit uniform remainder radius is not compact-core closure;
- 3-point Gram positivity does not by itself prove all PF3 Toeplitz minors;
- PF3 does not imply PF-infinity;
- RH remains OPEN.
