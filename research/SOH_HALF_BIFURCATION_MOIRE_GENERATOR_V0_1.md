# Secret-of-a-Half: Half-Bifurcation and Moire Generator v0.1

Status: CANDIDATE_EXACT_AFFINE_SUBTHEORY / RH_CLOSURE_NOT_CLAIMED
Date: 2026-09-24

## 1. Affine half generator

Define

\[
T(x)=2x+1.
\]

Its exact nth iterate is

\[
\boxed{T^n(x)=2^n x+(2^n-1)}.
\]

Therefore the symmetric half inputs produce two exact branches:

\[
\boxed{T^n(+1/2)=3\cdot2^{n-1}-1},
\]

\[
\boxed{T^n(-1/2)=2^{n-1}-1}.
\]

For n starting at 1:

\[
+\tfrac12\to 2\to5\to11\to23\to47\to95\to\cdots,
\]

\[
-\tfrac12\to0\to1\to3\to7\to15\to31\to\cdots.
\]

The positive branch obeys the Cunningham recurrence `next = 2*current+1`; its initial values 2,5,11,23,47 are prime and 95 is composite. The negative branch is the Mersenne-form sequence \(2^m-1\); not every term is prime.

## 2. Zero and even-prime bifurcation

At one step,

\[
\boxed{T(-1/2)=0,\qquad T(+1/2)=2.}
\]

The midpoint of the outputs is 1. This is an exact affine symmetry fact. It does not by itself establish a zeta theorem or a physical law.

## 3. Moire half coordinates

For two equal-amplitude phase carriers,

\[
e^{i\phi_1}+e^{i\phi_2}
=2e^{i(\phi_1+\phi_2)/2}\cos\!\left(\frac{\phi_1-\phi_2}{2}\right).
\]

Thus the factor 1/2 appears canonically in both the carrier mean and interference half-difference. This is a mathematically exact source of a half-coordinate in two-layer interference.

Conjugation and antiphase remain distinct:

\[
\text{conjugate}:\ \phi\mapsto-\phi,
\qquad
\text{antiphase}:\ \phi\mapsto\phi+\pi.
\]

Only the second gives exact equal-amplitude cancellation for every \(\phi\).

## 4. Relation to the critical half-axis

If a problem has an independently derived involution

\[
s\mapsto1-s,
\]

then \(s=1/2\) is its fixed set. This project may use the half-bifurcation algebra as a representation tool, but the affine identities above do **not** prove the Riemann Hypothesis.

The existing formal RH seam/no-go results remain authoritative. Promotion to an RH theorem requires closing every analytic implication in that seam.

## 5. Algebra class

Define the project-local half-bifurcation algebra

\[
\mathcal H_{1/2}=\langle T,J\rangle,
\qquad T(x)=2x+1,\quad J(x)=-x,
\]

with the distinguished seed pair \(\{-1/2,+1/2\}\). Its exact orbit formulas and branch relations are theorem-level elementary algebra; any identification with zeta zeros, primes beyond the explicit recurrence, or physics remains a separate gate.

## 6. Promotion ledger

- closed-form iterate: PASS EXACT
- ±1/2 -> {0,2}: PASS EXACT
- positive recurrence and initial prime run: PASS EXACT FINITE
- negative Mersenne-form branch: PASS EXACT
- moire mean/half-difference identity: PASS EXACT
- RH critical line forced by these identities alone: FAIL / NOT IMPLIED
- RH proof: OPEN under existing formal seam
