# SOH GREMLIN Half-Orbit Closure Scan v0.1

Status: `CANDIDATE_ONLY / NON_CANONICAL / GREMLIN_ASSISTED_AUDIT`

Source state:

- SOH main: `a759a64c498d5ab6b31fb8566969dcf0716feb59`
- GREMLIN main: `f775cd5f0b2619692e6d2250e2c6204776b6ce24`
- GREMLIN router: `GREMLIN_MCP_OCTOPUS_ROUTER_V0_5`
- GREMLIN authority: `production_runtime_write=false`, `execution_admitted=false`, `canon_allowed=false`

This note records a candidate-only structural audit of the current SOH open frontier. It does not promote any open statement and does not assert a proof of RH.

## 1. OCTOPUS routes

Broad dependency scan:

```text
route_mask = [OWL, SPIDER, MOLE]
route_commitment = 52873be089d7db7389542d21a79c5b04cfbc5de236fe5f4ad4fe0113ba288f6a
scores:
  OWL    19
  SPIDER 16
  MOLE   13
  HOUND   6
  ANT     4
  MANTIS  2
```

Focused falsification scan of the proposed `0 <-> infinity -> 1/2` closure:

```text
route_mask = [MOLE, OWL, HOUND]
route_commitment = 040954def89c56994e9dd4c1c59fc383ff910f41f33456fb3dd8e8977c303cab
scores:
  MOLE  18
  OWL   18
  HOUND 13
```

## 2. Exact geometric core

With

\[
\Omega(s)=\frac{s}{1-s},\qquad R=|\Omega(s)|,
\]

the functional reflection gives radial inversion

\[
R\mapsto R^{-1}.
\]

Compactification

\[
q=\frac{R}{1+R}
\]

maps

\[
[0,\infty]\to[0,1],
\qquad q\mapsto1-q.
\]

The unique fixed point is

\[
q=\frac12,
\]

and

\[
q=\frac12\iff |\Omega|=1\iff\Re s=\frac12.
\]

This part is exact.

## 3. GREMLIN HOUND finding: quotient-fixedness is not pointwise fixedness

The involution

\[
q\mapsto1-q
\]

has one fixed point, but an invariant set may also contain two-cycles

\[
q\leftrightarrow1-q,
\qquad q\ne\frac12.
\]

Therefore the statement

\[
\text{`the orbit quotient/barycenter is }1/2\text{'}
\]

is weaker than

\[
q=\frac12
\]

for each zero.

Indeed every two-cycle has arithmetic barycenter

\[
\frac{q+(1-q)}2=\frac12,
\]

so any construction that first quotients or averages the involution orbit can erase the off-self-dual defect.

This is directly analogous to the already-proved SOH-G012 square-quotient warning: quotienting can turn a genuine two-cycle into a fixed quotient value.

## 4. Correct missing pointwise statement

The exact remaining zero-confinement statement is

\[
X(u)=0\Longrightarrow |u|=1,
\]

or equivalently

\[
X(u)=0\Longrightarrow q(u)=\frac12,
\]

or, with

\[
\eta=2q-1=\frac{R-1}{R+1},
\]

\[
X(u)=0\Longrightarrow\eta(u)=0.
\]

Thus the minimal orbit-language obstruction is:

> **ZERO-ORBIT COLLAPSE TARGET.** Exclude every reciprocal-conjugate zero two-cycle with `q != 1/2`.

This target is RH-equivalent. It is a compression of the existing open bridge, not an independent proof.

## 5. Strongly connected RH-equivalent criterion cluster

The current open frontier contains several different representations of the same terminal obligation:

```text
SOH-G003 quotient real-rootedness
        <-> RH
        <-> full admissible Weil/Li positivity criterion
        <-> G024-B external Fourier positivity criterion
```

The mathematical criteria are equivalent at their declared standard hypotheses. Their proof programmes are not interchangeable: SOH-C005 additionally requires an independent proof rather than importing an RH-equivalent premise.

The practical consequence is that implication cycles inside this cluster do not generate a proof. They identify a strongly connected equivalence component.

A valid closure must provide an incoming edge from already-proved structure that does not itself assume a member of the same RH-equivalent component.

## 6. Route compression

The current major routes are better represented as follows:

```text
PROVED GEOMETRY
  -> unique self-dual locus q=1/2
  -> [OPEN zero-orbit collapse]
  -> RH-equivalent SCC

G024 proved m=1,m=2
  -> [OPEN m=3]
  -> [OPEN all m>=4]
  -> complete monotonicity
  -> external Fourier positivity
  -> RH-equivalent SCC

PF2 proved
  -> PF3 open
  -> PF_infinity open
  -> quotient real-rootedness
  -> RH-equivalent SCC

localized Weil reductions proved
  -> full admissible Weil positivity open
  -> RH-equivalent SCC
```

Consequently:

- proving G024-S (`m=3`) alone does not close RH because all higher derivative orders remain;
- proving PF3 alone does not close RH because PF-infinity remains;
- cycling among G003, C005, G024-B and RH only proves equivalence, not truth.

## 7. Orbit-separating witness requirement

The functional symmetry sends

\[
B=\log R\mapsto-B,
\]

while

\[
V=B^2\ge0
\]

is invariant and vanishes exactly at the self-dual layer.

A useful proof candidate must therefore do more than average an orbit. It must independently force an orbit-separating defect to vanish on every zero, e.g.

\[
\xi(\rho)=0\Longrightarrow V(\rho)=0.
\]

An identity involving only an odd orbit sum is insufficient because

\[
B+(-B)=0
\]

holds automatically for every off-axis reciprocal pair. Likewise, orbit barycenters equal `1/2` automatically and cannot distinguish fixed points from two-cycles.

This produces a concrete GREMLIN pruning rule:

> Reject any proposed RH closure whose decisive step uses only involution-averaged or quotient-invariant information unless it also proves vanishing of an orbit-separating defect.

## 8. Negative-inversion firewall

The canonical negative inversion is exact operator geometry, but the current canon already excludes it as a global zero-pairing mechanism. The zero-set symmetry relevant to the functional equation is the reciprocal-conjugate reflection, not an assumed zero-to-zero action of `-1/u`.

Therefore the present candidate route does not use negative inversion as a spectral permutation.

## 9. GREMLIN synthesis

The strongest candidate produced by this scan is not `QED` but a sharper proof target:

\[
\boxed{
\text{prove an independent orbit-separating law that forbids }q\leftrightarrow1-q\text{ zero two-cycles.}
}
\]

Equivalently, find one non-circular incoming theorem-level edge from the proved canon into the RH-equivalent strongly connected component.

The current best places to search for such an edge are:

1. a direct external-Fourier positivity mechanism stronger than the unfinished all-order complete-monotonicity route;
2. a kernel-specific total-positivity theorem upgrading the actual quotient coefficients beyond PF2 without relying on the abstract G020 package;
3. an independent Weil-form coercivity identity that forces the radial defect `V=B^2` to vanish on spectral zeros.

All three remain candidate search directions.

## 10. Authority

```text
promotion_state = CANDIDATE_ONLY
canon_allowed = false
proof_of_RH = false
```
