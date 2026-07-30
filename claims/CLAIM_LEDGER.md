# Claim Ledger — Version 0.5

| ID | Statement | Status | Evidence / location | Blocking gap |
|---|---|---|---|---|
| SOH-L001 | Binary Shannon entropy is uniquely maximal at \(\sigma=1/2\), with value \(\ln 2\). | Exact | Monograph, Theorem 4.1 | None |
| SOH-L002 | Equal-gain normalized two-channel cancellation occurs only at \(\sigma=1/2\) and relative phase \(\pi\). | Exact | Monograph, Theorem 5.1 | None |
| SOH-L003 | The fixed set of \(\mathcal J(s)=1-\overline{s}\) is \(\operatorname{Re}s=1/2\). | Exact | Monograph, Theorem 3.2 | None |
| SOH-L004 | The entropy deficit from balance equals a Bernoulli KL divergence and is strictly positive away from \(1/2\). | Exact | Monograph, Theorem 4.2 | None |
| SOH-L005 | Within the binary-spinor model, complement symmetry, maximal entropy, spinorial sign and phase-locked cancellation are equivalent to \(\sigma=1/2\). | Exact model theorem | Monograph, Theorem 6.1 | Explicit model assumptions |
| SOH-L006 | In the open critical strip, \(\eta\) and \(\zeta\) have the same zeros with multiplicity. | Exact classical | Monograph, Theorem 7.1 | None |
| SOH-L007 | Unequal channel gains shift cancellation to \(|b|^2/(|a|^2+|b|^2)\). | Exact | Monograph, Theorem B.1 | None |
| SOH-C001 | A canonical regular, covariant, gauge-independent zeta-state map converts every non-trivial zero into equal-gain cancellation. | Open bridge | Monograph, Chapter 8 | Canonical construction |
| SOH-T001 | Under SOH-C001 and the channel hypotheses, every non-trivial zero lies on \(\operatorname{Re}s=1/2\). | Conditional | Monograph, Theorem 9.1 | SOH-C001 |
| SOH-C002 | A theta-kernel, analytic-vector, positivity or reproducing-kernel construction satisfies the canonical bridge. | Open programme | Monograph, Chapter 11 | Positivity and zero-equivalence |
| SOH-C003 | A self-adjoint operator has spectral determinant proportional to \(\Xi\). | Open spectral route | Monograph, Chapter 12 | Operator construction |
| SOH-L008 | The native paired theta state satisfies \(P(J(s))=X\overline{P(s)}\). | Exact | Native PhaseNav source and tests | None |
| SOH-L009 | The normalized native closure defect equals \((\operatorname{Re}s-1/2)^2\). | Exact | Monograph, Theorem 16.2 | None |
| SOH-L010 | The continuous paired theta-Mellin detector equals \(\xi(s)\). | Exact classical | Monograph, Proposition 16.3 | None |
| SOH-C004 | Every non-trivial \(\xi\) zero closes in the canonical self-dual PhaseNav shell. | Open bridge | Postulate 16.4 | Positivity or uniqueness theorem |
| SOH-T002 | Under SOH-C004, every non-trivial zero lies on \(\operatorname{Re}s=1/2\). | Conditional | Monograph, Theorem 16.5 | SOH-C004 |
| SOH-N001 | The 18-pair detector is a low-height numerical quadrature approximation to \(\xi(s)\). | Numerical | CSV receipt and tests | Finite quadrature |
| SOH-L011 | For an involution-fixed finite fixture, the PhaseNav–Weil matrix is a PSD Gram matrix. | Exact finite lemma | Native `.pnv` and tests | Not the complete arithmetic criterion |
| SOH-N002 | The two-channel Gaussian profile detects a synthetic off-axis quartet through a negative eigenvalue. | Numerical falsification witness | JSON receipt and tests | Synthetic finite fixture |
| SOH-C005 | The complete arithmetic PhaseNav–Weil operator is positive on a dense admissible family and its null structure forces native closure. | Open positivity bridge | PhaseNav–Weil docs | Uniform positivity, basis-uniform cutoff control, regularization, closure implication |
| SOH-T003 | Under SOH-C005 and exact Weil correspondence, all non-trivial zeros lie on the half-axis. | Conditional | PhaseNav–Weil operator | SOH-C005 |
| SOH-L012 | The Gaussian matrix test has the declared closed Fourier transform. | Exact analytic lemma | Arithmetic v0.2 docs and tests | None |
| SOH-N003 | The declared prime-side matrix is cutoff-stable and matches the low-height spectral receipt. | Numerical audit | Arithmetic JSON receipt | One profile and finite cutoffs |
| SOH-L013 | Finite spans of translated-scaled Hermite PhaseNav channels are dense in Schwartz space. | Exact functional-analytic lemma | Chapter 17 and Hermite basis theorem | None |
| SOH-L014 | The Hermite kernel has the declared closed Fourier transform and \(\widehat H_{mn}(0)=\delta_{mn}\). | Exact analytic lemma | Chapter 17 and regression tests | None |
| SOH-T004 | PSD of every finite Hermite section plus continuity extends non-negativity to the dense core. | Conditional reduction theorem | Chapter 17 | Uniform PSD and continuity |
| SOH-N004 | The finite Hermite ladder through basis size six is cutoff-audited and PSD-tested. | Numerical audit | Deterministic receipt | Finite basis and cutoffs |
| SOH-L015 | Binary complement is conjugate to reciprocal inversion in projective odds coordinates. | Exact lemma | Chapter 18, Theorem 18.3 | None |
| SOH-L016 | The unique positive reciprocal fixed point corresponds to the unique complement-fixed weight \(p=1/2\). | Exact lemma | Chapter 18, Corollary 18.4 | None |
| SOH-L017 | \(p=1/2\) is the Fisher–Rao geodesic midpoint between the two labelled pure states. | Exact information-geometric lemma | Chapter 18, Theorem 18.5 | None |
| SOH-H001 | `DEFINED_ZERO` and `UNDEFINED_BOTTOM` are interpreted as informational boundary labels. | Exploratory hypothesis | Chapter 18 and native `.pnv` | Canonical physical or zeta-state interpretation |
| SOH-L018 | The logarithmic prime tail is compactified by \(z_{\rm t}=1/\log x\) to a finite interval whose new endpoint is smooth and flat. | Exact analytic lemma | Chapter 19, Theorem 19.3 | None |
| SOH-L019 | Every fixed Hermite matrix entry has the declared upper-incomplete-gamma prime-tail majorant under an explicit monotonicity condition. | Exact analytic theorem | Chapter 19, Theorems 19.2 and 19.4 | None |
| SOH-L020 | Entrywise prime-tail certificates imply a finite-section operator-norm bound and a Weyl eigenvalue enclosure. | Exact finite-section theorem | Chapter 19, Corollary 19.5 | None |
| SOH-N005 | For \(w=0.8\), \(Q=100000\), and \(N\le6\), the largest certified prime-tail operator-norm bound is \(7.717202889\times10^{-13}\). | Numerical certificate | Prime-tail JSON receipt and tests | Fixed finite sections only |

## Promotion rule

An open claim may be promoted only when its complete proof or reproducible construction is present, every dependency is listed, and no dependency is merely an equivalent formulation of the Riemann Hypothesis left unproved. Numerical agreement cannot promote a claim to exact status. IEEE NaN is not a numeric endpoint in SOH-H001. The reciprocal tail coordinate in SOH-L018 is not a map of zeta zeros.
