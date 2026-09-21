# SOH Suzuki Corollary 1.6 Pole Audit v0.1

Status: **SOURCE-LEVEL DOMAIN AUDIT / CORRECTED LOCAL TARGET PROPOSED / RH OPEN**

Primary source: Masatoshi Suzuki, *Weil's quadratic form via the screw
function*, arXiv:2606.09096. Corollary 1.6 states the conditional limit

\[
e^{\phi(a,z)}W(a,\theta(a);z)
\longrightarrow
F(z):=
z^2\frac{\xi(1/2-iz)}{\xi'(1/2-iz)}
\]

uniformly on every compact subset of the complex plane.

Theorem 1.5 proves unconditionally that \(W(a,\theta;\cdot)\) is entire and
has only real zeros for each finite \(a\).

## 1. Meromorphic-target issue

The target

\[
F(z)=z^2\frac{\xi(1/2-iz)}{\xi'(1/2-iz)}
\]

is naturally meromorphic, not entire.

Set

\[
\Xi(z)=\xi(1/2-iz).
\]

Then

\[
\Xi'(z)=-i\,\xi'(1/2-iz).
\]

At a zero \(z_0\) of \(\Xi\) of multiplicity \(m\ge1\),

\[
\frac{\Xi(z)}{\Xi'(z)}
\]

has a removable singularity and extends with a simple zero at \(z_0\).
Therefore the xi zeros themselves are not the problem.

The problem is a critical point \(c\) satisfying

\[
\Xi'(c)=0,\qquad \Xi(c)\ne0.
\]

At every such point \(F\) has a genuine pole, except for the special factor
\(z^2\) when \(c=0\).

## 2. Why genuine poles occur

Classically, Hardy's theorem gives infinitely many real zeros of \(\Xi\).
Choose two consecutive distinct positive real zeros

\[
0<\alpha<\beta.
\]

By Rolle's theorem there exists

\[
c\in(\alpha,\beta)
\]

with

\[
\Xi'(c)=0.
\]

Consecutiveness gives \(\Xi(c)\ne0\), and \(c\ne0\). Hence

\[
\boxed{F\text{ has a genuine pole at }c.}
\]

Thus the target in Corollary 1.6 cannot be treated as an everywhere-entire
finite-valued function.

## 3. Consequence for literal compact-uniform convergence

Under the ordinary complex-valued meaning of uniform convergence on every
compact subset of \(\mathbb C\), a sequence of finite holomorphic functions
cannot converge uniformly on a compact neighborhood containing a genuine pole
to \(F\).

Therefore the literal all-compact formulation needs a domain/topology
qualification before it can be used as the repository's analytic target.

This does **not** invalidate Suzuki's finite-\(a\) Theorem 1.5. The real-zero
characteristic functions remain an unconditional and useful input. The audit
only concerns the global form of the conjectural limiting statement.

## 4. Corrected local formulation sufficient for the SOH endgame

For RH we do not need convergence across the pole set.

Let

\[
P=\{z:\xi'(1/2-iz)=0,\ \xi(1/2-iz)\ne0\}
\]

be the genuine pole set of \(F\). A sufficient analytic package would be:

1. choose a normalization that is holomorphic and non-vanishing on the local
   domains used, so it does not create or destroy zeros;
2. obtain locally uniform convergence on compact subsets of
   \(\mathbb C\setminus P\), after taking the removable extension of
   \(\Xi/\Xi'\) at xi zeros;
3. prove zero attraction near every zero of the extended target.

If a target zero \(z_0\notin\mathbb R\) existed, choose a small closed disk
around \(z_0\) disjoint from both the real axis and \(P\). Hurwitz/Rouché
zero stability would force zeros of the finite-\(a\) approximants inside that
disk for sufficiently large \(a\), contradicting Theorem 1.5 because all their
zeros are real.

Hence this repaired local statement would still force every xi zero to have
real Suzuki coordinate.

## 5. Lean interface already avoids the global pole issue

The formal file

\`SecretOfAHalfFormal/SuzukiLimit.lean\`

does not assume the questionable global convergence formula. It assumes only
the exact endgame needed at each zero:

\[
z_n\in\mathbb R,\qquad
z_n\to i(s-1/2).
\]

Lean then proves

\[
\Re(s)=1/2.
\]

Thus the formal target is robust under replacement of Corollary 1.6 by any
correct local zero-attraction theorem.

## 6. Updated incoming edge

The most precise surviving Suzuki route is now

\[
\boxed{
\text{finite-}a\text{ real-zero }W
+
\text{local meromorphic-limit control}
+
\text{zero attraction}
\Longrightarrow
\text{RH}.
}
\]

The remaining hard work is to derive the local convergence/zero-attraction
from the arithmetic screw/theta kernel while controlling the normalization and
the parameter \(\lambda<\lambda_a\).

\`proof_of_rh = false\`
