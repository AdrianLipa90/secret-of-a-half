import Mathlib

namespace SecretOfAHalfFormal

open Complex

/-- Projective coordinate used by the reciprocal--conjugation formulation. -/
noncomputable def omega (s : ℂ) : ℂ := s / (1 - s)

/-- The reciprocal--conjugation seam in projective coordinates. -/
def reciprocalConjugationSeam (u : ℂ) : Prop := u⁻¹ = conj u

/-- Unit-modulus points lie on the reciprocal--conjugation seam. -/
theorem norm_one_implies_reciprocalConjugationSeam {u : ℂ} (h : ‖u‖ = 1) :
    reciprocalConjugationSeam u := by
  unfold reciprocalConjugationSeam
  exact Complex.inv_eq_conj h

/-- Away from zero, reciprocal--conjugation coincidence forces unit modulus. -/
theorem reciprocalConjugationSeam_implies_norm_one {u : ℂ} (hu : u ≠ 0)
    (h : reciprocalConjugationSeam u) : ‖u‖ = 1 := by
  unfold reciprocalConjugationSeam at h
  have hn := congrArg norm h
  have hinv : ‖u‖⁻¹ = ‖u‖ := by
    simpa using hn
  have hpos : 0 < ‖u‖ := norm_pos_iff.mpr hu
  have hmul : ‖u‖ * ‖u‖ = 1 := by
    calc
      ‖u‖ * ‖u‖ = ‖u‖ * ‖u‖⁻¹ := by rw [hinv]
      _ = 1 := mul_inv_cancel₀ (ne_of_gt hpos)
  nlinarith

/-- Exact reciprocal--conjugation coincidence criterion on ℂˣ. -/
theorem reciprocalConjugationSeam_iff_norm_one {u : ℂ} (hu : u ≠ 0) :
    reciprocalConjugationSeam u ↔ ‖u‖ = 1 := by
  constructor
  · exact reciprocalConjugationSeam_implies_norm_one hu
  · exact norm_one_implies_reciprocalConjugationSeam

end SecretOfAHalfFormal
