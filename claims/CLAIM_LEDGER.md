# Claim Ledger — Version 0.2

| ID | Statement | Status | Evidence / location | Blocking gap |
|---|---|---|---|---|
| SOH-L001 | Binary Shannon entropy is uniquely maximal at \(\sigma=1/2\), with value \(\ln 2\). | Exact | Monograph, Theorem 4.1 | None |
| SOH-L002 | Equal-gain normalized two-channel cancellation occurs only at \(\sigma=1/2\) and relative phase \(\pi\). | Exact | Monograph, Theorem 5.1 | None |
| SOH-L003 | The fixed set of \(\mathcal J(s)=1-\overline{s}\) is \(\operatorname{Re}s=1/2\). | Exact | Monograph, Theorem 3.2 | None |
| SOH-L004 | The entropy deficit from balance equals a Bernoulli KL divergence and is strictly positive away from \(1/2\). | Exact | Monograph, Theorem 4.2 | None |
| SOH-L005 | Within the stated binary-spinor model, complement symmetry, maximal entropy, spinorial sign and phase-locked cancellation are equivalent to \(\sigma=1/2\). | Exact model theorem | Monograph, Theorem 6.1 | Model assumptions are explicit |
| SOH-L006 | In the open critical strip, \(\eta\) and \(\zeta\) have the same zeros with the same multiplicities. | Exact classical | Monograph, Theorem 7.1 | None |
| SOH-L007 | Unequal channel gains shift exact cancellation to \(|b|^2/(|a|^2+|b|^2)\). | Exact | Monograph, Theorem B.1 | None |
| SOH-C001 | A canonical zeta-state map converts every non-trivial zero into equal-gain complementary cancellation and is regular, covariant and gauge-independent. | Open bridge | Monograph, Axioms 8.1–8.5 and Postulate 8.3 | No canonical construction yet |
| SOH-T001 | Under SOH-C001 and the stated channel hypotheses, every non-trivial zero lies on \(\operatorname{Re}s=1/2\). | Conditional | Monograph, Theorem 9.1 | Depends on SOH-C001 |
| SOH-C002 | A theta-kernel, analytic-vector, positivity or reproducing-kernel construction satisfies the canonical bridge requirements. | Open programme | Monograph, Chapter 11 | Positivity and zero-equivalence unproved |
| SOH-C003 | A self-adjoint operator has a spectral determinant proportional to \(\Xi\). | Open spectral route | Monograph, Theorem 12.1 gives the implication | Operator not constructed |

| SOH-L008 | The native paired theta state satisfies $P(J(s))=X\overline{P(s)}$. | Exact lemma | Direct channel calculation and executable PhaseNav test | None |
| SOH-L009 | The normalized native PhaseNav closure defect equals $(\operatorname{Re}s-1/2)^2$. | Exact lemma | Log-gain identity and executable PhaseNav test | None |
| SOH-L010 | The continuous theta-Mellin detector defined by the paired state equals $\xi(s)$. | Exact classical identity | Symmetric theta-Mellin representation | None |
| SOH-C004 | Every non-trivial $\xi$ zero closes in the canonical self-dual PhaseNav shell. | Open native-closure bridge | Native `.pnv` construction specifies the condition | Positivity, self-adjointness, or zero-state uniqueness theorem |
| SOH-T002 | Under SOH-C004, every non-trivial zero lies on $\operatorname{Re}s=1/2$. | Conditional theorem | SOH-L009 and SOH-L010 | Depends on SOH-C004 |
| SOH-N001 | The 18-pair detector is a low-height numerical quadrature approximation to $\xi(s)$. | Numerical construction | Regression tests and CSV receipt | Finite quadrature is not exact globally |

| SOH-L011 | For an involution-fixed finite centred zero fixture, the PhaseNav–Weil matrix reduces to a positive-semidefinite Gram matrix. | Exact finite lemma | Native `.pnv` source, derivation and regression test | Does not establish the complete arithmetic Weil criterion |
| SOH-N002 | The declared two-channel Gaussian profile detects a synthetic off-axis quartet through a negative minimum eigenvalue. | Numerical falsification witness | JSON receipt and regression tests | Synthetic finite fixture; not evidence for global positivity |
| SOH-C005 | The complete arithmetic PhaseNav–Weil operator is positive on a dense admissible test-channel family and its null structure forces native closure. | Open positivity bridge | `docs/construction/PHASENAV_WEIL_OPERATOR.md` | Prime-side explicit formula, regularization and closure implication unproved |
| SOH-T003 | Under SOH-C005 and the exact Weil correspondence, every non-trivial zero lies on \(\operatorname{Re}s=1/2\). | Conditional theorem | SOH-L011 and SOH-C005 | Depends on SOH-C005 |

## Promotion rule

An open claim may be promoted only when its complete proof or reproducible construction is present, every dependency is listed, and no dependency is merely an equivalent formulation of the Riemann Hypothesis left unproved. Numerical agreement cannot promote a claim to exact status.
