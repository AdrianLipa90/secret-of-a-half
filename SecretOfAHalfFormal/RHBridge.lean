import Mathlib
import SecretOfAHalfFormal.RiemannSeam

namespace SecretOfAHalfFormal

/-- The exact missing projective implication: every non-trivial zeta zero is
sent by omega to the unit circle. -/
def ZeroOmegaUnitCondition : Prop :=
  ∀ (s : ℂ), riemannZeta s = 0 →
    (¬ ∃ n : ℕ, s = -2 * (n + 1)) →
    s ≠ 1 →
    ‖omega s‖ = 1

/-- The projective missing condition implies mathlib's literal RH statement. -/
theorem riemannHypothesis_of_zeroOmegaUnit (h : ZeroOmegaUnitCondition) :
    RiemannHypothesis := by
  intro s hz htriv hs1
  exact (omega_norm_one_iff_re_half hs1).mp (h s hz htriv hs1)

/-- Conversely, RH gives the projective unit-circle condition. -/
theorem zeroOmegaUnit_of_riemannHypothesis (h : RiemannHypothesis) :
    ZeroOmegaUnitCondition := by
  intro s hz htriv hs1
  exact (omega_norm_one_iff_re_half hs1).mpr (h s hz htriv hs1)

/-- Therefore the remaining projective zero-to-seam statement is exactly
RH-equivalent; it cannot be imported as an independent premise. -/
theorem zeroOmegaUnit_iff_riemannHypothesis :
    ZeroOmegaUnitCondition ↔ RiemannHypothesis := by
  constructor
  · exact riemannHypothesis_of_zeroOmegaUnit
  · exact zeroOmegaUnit_of_riemannHypothesis


/-- Equivalent missing edge in the slice-gluing language: every non-trivial
zeta zero is fixed by the critical anti-holomorphic involution. -/
def ZeroCriticalFixedCondition : Prop :=
  ∀ (s : ℂ), riemannZeta s = 0 →
    (¬ ∃ n : ℕ, s = -2 * (n + 1)) →
    s ≠ 1 →
    criticalInvolution s = s

theorem zeroCriticalFixed_iff_zeroOmegaUnit :
    ZeroCriticalFixedCondition ↔ ZeroOmegaUnitCondition := by
  constructor
  · intro h s hz htriv hs1
    exact (omega_norm_one_iff_re_half hs1).mpr
      ((criticalInvolution_fixed_iff_re_half s).mp (h s hz htriv hs1))
  · intro h s hz htriv hs1
    exact (criticalInvolution_fixed_iff_re_half s).mpr
      ((omega_norm_one_iff_re_half hs1).mp (h s hz htriv hs1))

theorem zeroCriticalFixed_iff_riemannHypothesis :
    ZeroCriticalFixedCondition ↔ RiemannHypothesis := by
  rw [zeroCriticalFixed_iff_zeroOmegaUnit, zeroOmegaUnit_iff_riemannHypothesis]


/-- A zeta zero cannot occur at s = 0 because ζ(0) = -1/2. -/
theorem riemannZeta_zero_point_ne_zero {s : ℂ} (hz : riemannZeta s = 0) :
    s ≠ 0 := by
  intro hs
  subst s
  norm_num [riemannZeta_zero] at hz

/-- The exact missing edge written literally in reciprocal--conjugation seam
language. -/
def ZeroReciprocalSeamCondition : Prop :=
  ∀ (s : ℂ), riemannZeta s = 0 →
    (¬ ∃ n : ℕ, s = -2 * (n + 1)) →
    s ≠ 1 →
    reciprocalConjugationSeam (omega s)

theorem zeroReciprocalSeam_iff_zeroOmegaUnit :
    ZeroReciprocalSeamCondition ↔ ZeroOmegaUnitCondition := by
  constructor
  · intro h s hz htriv hs1
    have hs0 : s ≠ 0 := riemannZeta_zero_point_ne_zero hz
    have homega : omega s ≠ 0 := by
      unfold omega
      exact div_ne_zero hs0 (sub_ne_zero.mpr (Ne.symm hs1))
    exact reciprocalConjugationSeam_implies_norm_one homega (h s hz htriv hs1)
  · intro h s hz htriv hs1
    exact norm_one_implies_reciprocalConjugationSeam (h s hz htriv hs1)

theorem zeroReciprocalSeam_iff_riemannHypothesis :
    ZeroReciprocalSeamCondition ↔ RiemannHypothesis := by
  rw [zeroReciprocalSeam_iff_zeroOmegaUnit, zeroOmegaUnit_iff_riemannHypothesis]

end SecretOfAHalfFormal
