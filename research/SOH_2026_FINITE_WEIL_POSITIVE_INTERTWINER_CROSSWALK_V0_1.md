# SOH 2026 Finite Weil / Positive-Intertwiner Prior-Art Crosswalk v0.1

Status: **EXTERNAL_ALIGNMENT / NO_NEW_BINDING / MD004D_REMAINS_OPEN**

Date: 2026-09-26

Parent:
- \`research/SOH_PRIME_AUTOCORRELATION_WEIL_POSITIVITY_DILEMMA_V0_1.md\`

## 1. Purpose

The current SOH frontier isolates a positive prime-to-zeta intertwiner as the missing operator object.

Two recent 2026 finite Weil constructions are close enough that they must be separated explicitly from that gate.

## 2. Finite Guinand–Weil dictionary

A. Groskin, *A finite Guinand-Weil dictionary and archimedean tail order for the truncated Weil quadratic form* (2026), constructs an exact finite map

\[
v\longmapsto g_v
\]

from Galerkin coefficient vectors to admissible band-limited Guinand–Weil test functions such that the finite quadratic value equals the corresponding absolutely convergent zero sum.

Thus, at fixed finite rank, the prime/pole/archimedean matrix value has an exact zero-side dictionary.

This is stronger than a numerical analogy.

However the source explicitly keeps the map one-way:
- no inverse from arbitrary Guinand–Weil test functions is claimed;
- total positivity of the post-band archimedean increment does not imply positivity of the complete Weil form;
- no RH claim is made.

Therefore this finite dictionary does not supply SOH-MD004D.

## 3. Finite Hilbert–Pólya / Prime–Weil pencils

Y. Shi, *Construction of Finite Hilbert--Pólya Matrices from Weil's Explicit Formula* (2026), constructs finite real-symmetric arithmetic Prime–Weil matrices and Hermitian definite quotient pencils.

For a dimension-matched zero-side pencil built from ordinates

\[
\gamma_1,\ldots,\gamma_N,
\]

the quotient spectrum is exactly

\[
\{\pm\gamma_1,\ldots,\pm\gamma_N\}.
\]

But the ordinates are inputs. The source explicitly classifies this as a reconstruction/consistency theorem rather than an independent derivation.

The paper identifies the remaining problem as a relative prime-to-zero perturbation theorem with uniform control of the compressed metric.

This is structurally the same missing object isolated by SOH-MD004D.

## 4. Exact correspondence with the SOH frontier

The SOH spectral-positivity dilemma states:

\[
\text{prime side}
=
\text{easy positive metric, arithmetic frequencies}
\]

while

\[
\text{zero-sensitive Weil side}
=
\text{correct zeta content, positivity RH-hard}.
\]

The 2026 finite results sharpen this as follows.

### CLOSED externally at finite level

- exact coefficient/test-function dictionary;
- exact finite quadratic value = zero sum;
- finite Hermitian quotient construction;
- exact reconstruction of supplied real ordinates;
- controlled positive archimedean tail increments.

### STILL OPEN

- zero-list-free derivation of zeta ordinates as the spectrum;
- uniform relative prime-to-zero perturbation with a controlled positive metric;
- full infinite-rank positive intertwiner;
- global Weil positivity without RH-equivalent input.

## 5. Refined MD004D

The open gate can now be stated in finite-to-infinite language.

### SOH-MD004D — relative positive-metric prime-to-zeta intertwiner

Construct a sequence of zero-list-free arithmetic finite systems

\[
(K_N^{\rm p},G_N^{\rm p})
\]

and a limiting Hilbert representation such that:

1. \(G_N^{\rm p}\succ0\) is proved from arithmetic data;
2. the generalized spectra are stable under the declared compression;
3. a relative perturbation theorem identifies the limiting spectral labels with the zeta channels without consuming the ordinates as inputs;
4. the metric distortion is uniformly controlled as \(N\to\infty\);
5. the limiting representation intertwines log-scale translation and has characters
   \[
   e^{a(\rho-1/2)};
   \]
6. no RH, zero list, Montgomery target, or global Weil positivity is used upstream.

This is more specific than a generic Hilbert–Pólya request.

## 6. No-go distinctions

The following do not close MD004D:

\[
\boxed{
\text{exact zero-side reconstruction from supplied }\gamma_k
}
\]

because it consumes the target spectrum;

\[
\boxed{
v\mapsto g_v\text{ finite Guinand–Weil dictionary}
}
\]

because a one-way quadratic-value dictionary is not a positive spectral intertwiner;

\[
\boxed{
\text{positive archimedean tail}
}
\]

because it does not prove positivity of the complete prime/pole/archimedean Weil block.

## 7. Current target

The next proof-bearing object should be a **relative metric estimate**, not another raw finite spectrum.

A useful certificate would bound, on a common contrast space,

\[
\|G_N^{-1/2}(K_N^{\rm p}-K_N^{\rm target})G_N^{-1/2}\|
\]

and the relative metric distortion

\[
\|G_N^{-1/2}(G_N^{\rm p}-G_N^{\rm target})G_N^{-1/2}\|
\]

by quantities tending to zero, where the target is defined zero-list-free by an operator/trace construction rather than by supplied ordinates.

Only then can ordinary Hermitian spectral perturbation theory transfer a genuinely derived spectrum.

## 8. Prior-art status

This note makes no novelty claim for the cited finite Weil constructions. Their role is to prevent the SOH programme from confusing finite reconstruction with the missing zero-list-free spectral binding.

The agreement is useful: an independently developed SOH audit and recent external finite-matrix work identify essentially the same missing relative-metric convergence problem.
