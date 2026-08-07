# DHSE-001 — Stage M exact continuous forcing theorem

## Decision

- Status: **exact finite computer-assisted theorem**.
- Arithmetic: integer matrix arithmetic with exact reduced rational endpoint classification.
- Declared vectorized backend: signed 64-bit integers, with a pre-run overflow certificate for every declared word length.
- Domain: the complete primitive `K=6` positive Möbius universe.
- Word lengths: `1,2,3,4`.
- Projective radius: `1/10`.
- No centre grid is used.
- No main-claim promotion is implied by this finite theorem.

Stage M replaces every finite centre scan by an exact classification of the
forcing-count function on the whole positive axis `q>0`.

It also corrects an earlier informal argument. Reciprocal symmetry proves

\[
N(q)=N(1/q),
\]

but symmetry by itself does **not** prove that `q=1` is a maximum. The exact
continuous result shows that `q=1` is the unique global maximum at word lengths
2 and 3, but not at lengths 1 and 4.

## Operator universe

Let

\[
\mathcal M_6=
\left\{
\begin{pmatrix}a&b\\c&d\end{pmatrix}:
1\le a,d\le6,
\ 0\le b,c\le6,
\ ad-bc>0,
\ \gcd(a,b,c,d)=1
\right\}.
\]

The universe contains exactly `952` primitive matrices. Each matrix acts on the
positive projective line by

\[
f(z)=\frac{az+b}{cz+d}.
\]

For each ordered pair `(L,R)` in `M_6 x M_6` and each binary word `w` of length
`n`, compose the matrices from left to right. The resulting transformation is
written

\[
W(z)=\frac{Az+B}{Cz+D}.
\]

## Exact-arithmetic backend certificate

The implementation uses NumPy `int64` arrays for the high-volume matrix
composition and then converts reduced endpoints to Python integer pairs and
`Fraction` objects for exact ordering. Because fixed-width overflow would void
an exact finite theorem, Stage M now checks a conservative bound before each
vectorized census.

If every base coefficient is at most `K`, and `M_n` bounds every absolute
coefficient after a word of length `n`, then matrix multiplication gives

\[
M_{n+1}\le 2K M_n,
\qquad M_0=1,
\]

so

\[
M_n\le(2K)^n.
\]

For the declared `K=6`, `n<=4`,

\[
M_4\le12^4=20736.
\]

The largest product used in the forcing predicate is conservatively bounded by

\[
121M_4^2=52{,}027{,}785{,}216,
\]

well below

\[
2^{63}-1=9{,}223{,}372{,}036{,}854{,}775{,}807.
\]

Endpoint numerators are bounded by `11 M_4 = 228096`, also safely inside the
same range. Therefore the declared Stage M lengths cannot overflow the int64
backend. The implementation refuses a word length for which this certificate
fails instead of silently extending the theorem. For example, the same
conservative bound is already unsafe at length 8, so such a run would require a
wider exact-integer backend.

## Target ball

For the projective residual

\[
d_q(z)=\frac{|z-q|}{z+q}
\]

and radius `r=1/10`, the exact target ball is

\[
B_r(q)=\left[\frac9{11}q,\frac{11}{9}q\right].
\]

## Lemma 1 — image interval

Because every admitted composed map is orientation preserving,

\[
W'(z)=\frac{AD-BC}{(Cz+D)^2}>0.
\]

When `B>0` and `C>0`, its positive-line image is

\[
W((0,\infty))=\left(\frac BD,\frac AC\right).
\]

If `B=0` or `C=0`, the image cannot be contained in any bounded positive target
ball and contributes no forcing interval.

## Lemma 2 — exact admissible-centre interval

The whole image is contained in `B_r(q)` exactly when

\[
\frac9{11}q\le\frac BD,
\qquad
\frac AC\le\frac{11}{9}q.
\]

Equivalently,

\[
q\in I_W=
\left[
\frac{9A}{11C},
\frac{11B}{9D}
\right].
\]

The interval is non-empty precisely when

\[
81AD\le121BC.
\]

Thus every pair-word event contributes either one exact closed rational
interval in centre space or nothing.

## Theorem 1 — finite step-function representation

For fixed word length `n`, define

\[
N_n(q)=
\sum_{(L,R)\in\mathcal M_6^2}
\sum_{w\in\{L,R\}^n}
\mathbf 1_{I_{W_{L,R,w}}}(q).
\]

Then `N_n` is an integer-valued step function on `(0,infinity)`. Its value can
change only at a rational endpoint

\[
\frac{9A}{11C}
\quad\text{or}\quad
\frac{11B}{9D}.
\]

Therefore its global maximum is decided exactly by sweeping all endpoints and
the open cells between consecutive endpoints. No sampling density or numerical
tolerance enters the decision.

## Theorem 2 — reciprocal symmetry

Let

\[
J(z)=1/z.
\]

The primitive universe is closed under reciprocal conjugation

\[
W\mapsto J\circ W\circ J.
\]

The corresponding centre interval transforms as

\[
I_{J W J}=I_W^{-1}
=\{1/q:q\in I_W\}.
\]

Consequently

\[
N_n(q)=N_n(1/q)
\]

for every `q>0` and every declared length.

This theorem establishes symmetry, not the location of the maximum.

## Theorem 3 — exact continuous maximizers

The exhaustive rational endpoint sweep gives:

| Length | Non-empty forcing intervals | Breakpoints | `N_n(1)` | Global maximum | Exact maximizer set |
|---:|---:|---:|---:|---:|---|
| 1 | 188,496 | 44 | 24,752 | 39,984 | `[9/11,11/12] union [12/11,11/9]` |
| 2 | 1,741,094 | 3,359 | 314,690 | 314,690 | `{1}` |
| 3 | 5,068,044 | 150,239 | 943,740 | 943,740 | `{1}` |
| 4 | 11,594,096 | 1,595,693 | 2,219,236 | 2,224,570 | `[9882/9911,341/342] union [342/341,9911/9882]` |

Hence:

1. `q=1` is the **unique global maximizer** for lengths 2 and 3.
2. At length 1, the maxima form two reciprocal intervals away from `q=1`.
3. At length 4, the maxima form two extremely narrow reciprocal intervals
   immediately adjacent to `q=1`, but not containing it.
4. The length-4 excess above the self-dual point is

\[
2,224,570-2,219,236=5,334,
\]

approximately `0.2398%` of the global maximum.

## Proof certificate

For each length, the implementation:

1. certifies that the declared int64 vectorized arithmetic cannot overflow;
2. enumerates all `952^2 * 2^n` pair-word events;
3. forms the composed integer matrix exactly within the certified range;
4. retains exactly the events satisfying `B>0`, `C>0` and `81AD<=121BC`;
5. reduces both rational centre endpoints by their integer gcd;
6. aggregates equal start and end endpoints;
7. sorts the reduced fractions exactly;
8. sweeps every endpoint and every intervening open cell;
9. verifies reciprocal start/end multiplicities;
10. records every global-maximizer component.

This is an exhaustive proof over the declared finite universe, not a floating
point estimate. The fixed-width arithmetic premise is now explicit and tested.

## Correct formal conclusion

The statement

> self-duality alone forces the global maximum at the fixed point

is false in this generality. Lengths 1 and 4 are exact counterexamples inside
the same reciprocal-symmetric universe.

What the experiments establish instead is sharper:

> Reciprocal symmetry organizes the forcing landscape around the self-dual
> coordinate. For the primitive `K=6` universe at radius `1/10`, the exact
> maximizer equals the self-dual point for word lengths 2 and 3, while lengths 1
> and 4 produce reciprocal off-centre maximizer sets. At length 4 the splitting
> is a very small near-half doublet.

The next mathematical task is to characterize which algebraic properties of a
word length or composition sector determine whether the central self-dual peak
remains unsplit or bifurcates into a reciprocal pair.

IEEE `NaN` remains outside the state space. No numeric ordering of `NaN` and no
Riemann-hypothesis bridge is asserted by Stage M.
