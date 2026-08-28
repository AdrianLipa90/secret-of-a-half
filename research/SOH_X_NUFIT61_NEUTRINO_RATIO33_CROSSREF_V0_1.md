# SOH-X — NuFIT 6.1 Neutrino Ratio-33 Cross-reference v0.1

Status: `CROSS_REFERENCE_ONLY / NON_PROMOTING`

## Scope

GREMLIN v2.6 evaluates the TIR / NOEMA tetrahedron neutrino mass-ratio relation

\[
[1,2,10]\quad\Longrightarrow\quad
\frac{\Delta m^2_{31}}{\Delta m^2_{21}}=33
\]

against the official NuFIT 6.1 `DMS/DMA` marginalized surfaces.

The profiled minima are

\[
\Delta\chi^2_{\min}=0.9902209322450616
\]

for `TBoff-NO` and

\[
\Delta\chi^2_{\min}=0.44097506178386237
\]

for `TByes-NO`.

Both results were reproduced on separate GitHub Actions runners with exact NuFIT source hashes verified before parsing.

GREMLIN provenance commit: `b9b20f573b95d63cc069cbd0aedfa01f56a28f89`.

## SOH boundary

The v2.6 NuFIT statistic consumes the TIR mass-ratio relation. It does not consume the SOH half-interface kernel.

The current SOH crosslink remains

\[
D(\sigma,\phi)=1+2\sqrt{\sigma(1-\sigma)}\cos\phi
\]

with exact cancellation at

\[
\sigma=\frac12,\qquad \phi=\pi\pmod{2\pi},
\]

and, under the existing IDT spinorial lift \(\phi=\Delta\tau/2\), at

\[
\Delta\tau=2\pi\pmod{4\pi}.
\]

The NuFIT mass-splitting compatibility result therefore supplies no promotion of the SOH spectral-null, Zeeman-type, zeta-shell, or half-interface claims.

## Why the cross-reference is retained

The broader neutrino-information program now has two distinct empirical/formal coordinates:

1. the TIR mass-spectrum coordinate, tested by GREMLIN v2.6 against NuFIT 6.1;
2. the SOH balanced-phase cancellation coordinate, used as an interference diagnostic in phase/flavor reductions.

Keeping both coordinates cross-referenced prevents a later neutrino adapter from silently conflating a mass-spectrum test with an interference-kernel test.

## Current pins

- SOH base: `206e49e306b246c4b0f4d182b0d32d5511739408`
- GREMLIN v2.6 evidence: `b9b20f573b95d63cc069cbd0aedfa01f56a28f89`
- TIR current main at evidence binding: `8f0118845e7497964ac92bf26d34410a539b6063`
- IDT current main at evidence binding: `2ede618a5d03aa410f1d03b7286494622babd215`
- RFC current main at evidence binding: `01240c9d1f022cf59105b00ab15db1954e7f497a`

Claim promotion: `false`.
