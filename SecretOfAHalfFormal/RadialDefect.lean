import Mathlib
import SecretOfAHalfFormal.RiemannSeam
import SecretOfAHalfFormal.RHBridge

namespace SecretOfAHalfFormal

open scoped ComplexConjugate

/-- Exact reciprocal--conjugation defect. It vanishes precisely when the
reciprocal and conjugation actions coincide. -/
noncomputable def reciprocalConjugationDefect (u : ℂ) : ℝ :=
  ‖u⁻¹ - conj u‖ ^ 2

theorem reciprocalConjugationDefect_nonneg (u : ℂ) :
    0 ≤ reciprocalConjugationDefect u := by
  unfold reciprocalConjugationDefect
  exact sq_nonneg _

/-- Vanishing of the exact defect is equivalent to the reciprocal--conjugation
seam, with no nonzero hypothesis needed for this direction. -/
theorem reciprocalConjugationDefect_eq_zero_iff_seam (u : ℂ) :
    reciprocalConjugationDefect u = 0 ↔ reciprocalConjugationSeam u := by
  unfold reciprocalConjugationDefect reciprocalConjugationSeam
  rw [sq_eq_zero_iff]
  rw [norm_eq_zero]
  exact sub_eq_zero

/-- For the projective Riemann coordinate, vanishing of the exact defect is
equivalent to the critical-line condition away from the exceptional points. -/
theorem omega_defect_eq_zero_iff_re_half
    {s : ℂ} (hs0 : s ≠ 0) (hs1 : s ≠ 1) :
    reciprocalConjugationDefect (omega s) = 0 ↔
      s.re = (1 / 2 : ℝ) := by
  rw [reciprocalConjugationDefect_eq_zero_iff_seam]
  exact omega_reciprocalConjugationSeam_iff_re_half hs0 hs1

/-- The missing statement written as defect vanishing on every non-trivial
zeta zero. -/
def ZeroReciprocalDefectCondition : Prop :=
  ∀ (s : ℂ), riemannZeta s = 0 →
    (¬ ∃ n : ℕ, s = -2 * (n + 1)) →
    s ≠ 1 →
    reciprocalConjugationDefect (omega s) = 0

/-- The defect-vanishing formulation is exactly RH-equivalent. -/
theorem zeroReciprocalDefect_iff_riemannHypothesis :
    ZeroReciprocalDefectCondition ↔ RiemannHypothesis := by
  constructor
  · intro h s hz htriv hs1
    have hs0 : s ≠ 0 := riemannZeta_zero_point_ne_zero hz
    exact (omega_defect_eq_zero_iff_re_half hs0 hs1).mp
      (h s hz htriv hs1)
  · intro h s hz htriv hs1
    have hs0 : s ≠ 0 := riemannZeta_zero_point_ne_zero hz
    exact (omega_defect_eq_zero_iff_re_half hs0 hs1).mpr
      (h s hz htriv hs1)

/-- Abstract incoming-edge interface for an operator/energy construction.

To prove RH through an independently constructed scalar certificate E, it is
enough to prove on every non-trivial zero that (i) E vanishes and (ii) E is
exactly the reciprocal--conjugation defect. This theorem deliberately does not
provide either analytic/operator premise. -/
theorem riemannHypothesis_of_zero_energy_representation
    {E : ℂ → ℝ}
    (hEzero :
      ∀ (s : ℂ), riemannZeta s = 0 →
        (¬ ∃ n : ℕ, s = -2 * (n + 1)) →
        s ≠ 1 →
        E s = 0)
    (hErepr :
      ∀ (s : ℂ), riemannZeta s = 0 →
        (¬ ∃ n : ℕ, s = -2 * (n + 1)) →
        s ≠ 1 →
        E s = reciprocalConjugationDefect (omega s)) :
    RiemannHypothesis := by
  rw [← zeroReciprocalDefect_iff_riemannHypothesis]
  intro s hz htriv hs1
  rw [← hErepr s hz htriv hs1]
  exact hEzero s hz htriv hs1


/-- Stronger operator-facing interface: an independently constructed energy
that vanishes on non-trivial zeros and coercively dominates the projective
defect with a strictly positive constant forces RH. -/
theorem riemannHypothesis_of_coercive_zero_energy
    {E : ℂ → ℝ} {c : ℝ}
    (hc : 0 < c)
    (hEzero :
      ∀ (s : ℂ), riemannZeta s = 0 →
        (¬ ∃ n : ℕ, s = -2 * (n + 1)) →
        s ≠ 1 →
        E s = 0)
    (hcoercive :
      ∀ (s : ℂ), riemannZeta s = 0 →
        (¬ ∃ n : ℕ, s = -2 * (n + 1)) →
        s ≠ 1 →
        c * reciprocalConjugationDefect (omega s) ≤ E s) :
    RiemannHypothesis := by
  rw [← zeroReciprocalDefect_iff_riemannHypothesis]
  intro s hz htriv hs1
  have hnonneg : 0 ≤ reciprocalConjugationDefect (omega s) :=
    reciprocalConjugationDefect_nonneg _
  have hupper :
      c * reciprocalConjugationDefect (omega s) ≤ 0 := by
    simpa [hEzero s hz htriv hs1] using hcoercive s hz htriv hs1
  have hdefect_le : reciprocalConjugationDefect (omega s) ≤ 0 := by
    nlinarith
  exact le_antisymm hdefect_le hnonneg

end SecretOfAHalfFormal
