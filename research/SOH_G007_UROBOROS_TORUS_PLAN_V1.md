# SOH-G007 — Uroboros scaling quotient and Collatz–Riemann conjugacy

Status: **IMPLEMENTATION PLAN / exact identities separated from interpretation**

## Scope

This workstream formalizes the exact algebraic structure behind the proposed Uroboros picture without assuming the Collatz conjecture and without claiming a new functional equation for the Riemann xi function.

## Exact objects

For positive real `x`, define

\[
u=2x,\qquad s=\frac{u}{1+u}=\frac{2x}{1+2x}.
\]

Then

\[
x=\frac12 \Longleftrightarrow u=1 \Longleftrightarrow s=\frac12.
\]

Define the inversion about the half-layer

\[
I_x(x)=\frac{1}{4x}.
\]

Under the above normalization,

\[
u\mapsto\frac1u,\qquad s\mapsto1-s.
\]

For the halving branch `x -> x/2`, the conjugated map is

\[
H(s)=\frac{s}{2-s}.
\]

For the odd Collatz branch `x -> 3x+1`, the conjugated map is

\[
O(s)=\frac{s+2}{3}.
\]

With `J(s)=1-s`,

\[
JHJ=H^{-1},\qquad H^{-1}(s)=\frac{2s}{1+s}.
\]

## Uroboros quotient

The finite halving chain

\[
16\to8\to4\to2\to1\to\frac12
\]

changes scale by a factor of `32 = 2^5`. If, as an additional cycle-identification convention, endpoints related by this scale are identified, then

\[
u\sim32u.
\]

Writing `lambda = log u`, the quotient lattice is

\[
\Lambda=5\log 2\,\mathbb Z+2\pi i\,\mathbb Z,
\]

and the resulting quotient `C / Lambda` is a complex torus.

**INTERPRETACJA:** the identification `u ~ 32u` is the mathematical realization of the proposed Uroboros cycle closure. It is not a theorem about all Collatz trajectories.

## Deliverables

1. `src/secret_of_a_half/uroboros.py` — exact maps and torus-coordinate utilities.
2. `tests/test_uroboros.py` — exact/rational regression tests and fail-closed domain checks.
3. `scripts/run_soh_g007_uroboros_receipt.py` — deterministic proof receipt.
4. `monograph/chapters/32_uroboros_torus_and_collatz_riemann_conjugacy.tex` — theorem/interpretation split.
5. CI gate and compiled monograph.

## Proof firewall

This workstream does **not** claim:

- that every Collatz orbit reaches the halving chain;
- that `xi` is periodic or quasi-periodic under `u -> 32u`;
- that the quotient torus proves zero location;
- SOH-G003 real-rootedness;
- RH.

A genuinely new Riemann-side bridge would require an independently derived scaling or q-difference law for

\[
X(u)=\xi\!\left(\frac{u}{1+u}\right),
\]

beyond the already exact inversion symmetry `X(u)=X(1/u)`.