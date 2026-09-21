import Mathlib

namespace SecretOfAHalfFormal

open scoped ComplexConjugate

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
  have hne : ‖u‖ ≠ 0 := norm_ne_zero_iff.mpr hu
  have hsq : ‖u‖ * ‖u‖ = 1 := by
    calc
      ‖u‖ * ‖u‖ = ‖u‖ * ‖u‖⁻¹ := congrArg (fun x : ℝ => ‖u‖ * x) hinv.symm
      _ = 1 := mul_inv_cancel₀ hne
  nlinarith [norm_nonneg u]

/-- Exact reciprocal--conjugation coincidence criterion on ℂˣ. -/
theorem reciprocalConjugationSeam_iff_norm_one {u : ℂ} (hu : u ≠ 0) :
    reciprocalConjugationSeam u ↔ ‖u‖ = 1 := by
  constructor
  · exact reciprocalConjugationSeam_implies_norm_one hu
  · exact norm_one_implies_reciprocalConjugationSeam


/-- Anti-holomorphic reflection whose fixed locus is the full critical line. -/
noncomputable def criticalInvolution (s : ℂ) : ℂ := 1 - conj s

/-- The critical line is exactly the fixed locus of the anti-holomorphic
reflection s ↦ 1 - conjugate(s). -/
theorem criticalInvolution_fixed_iff_re_half (s : ℂ) :
    criticalInvolution s = s ↔ s.re = (1 / 2 : ℝ) := by
  constructor
  · intro h
    have hr := congrArg Complex.re h
    simp [criticalInvolution] at hr
    linarith
  · intro hr
    apply Complex.ext
    · simp [criticalInvolution]
      linarith
    · simp [criticalInvolution]

/-- Equality of squared distances to 0 and 1 is exactly the critical line. -/
theorem normSq_reflection_eq_iff_re_half (s : ℂ) :
    Complex.normSq s = Complex.normSq (1 - s) ↔ s.re = (1 / 2 : ℝ) := by
  rw [Complex.normSq_apply, Complex.normSq_apply]
  simp only [Complex.sub_re, Complex.one_re, Complex.sub_im, Complex.one_im, zero_sub]
  constructor <;> intro h <;> nlinarith

/-- Equality of distances to 0 and 1 is exactly the critical line. -/
theorem norm_reflection_eq_iff_re_half (s : ℂ) :
    ‖s‖ = ‖1 - s‖ ↔ s.re = (1 / 2 : ℝ) := by
  rw [← sq_eq_sq₀ (norm_nonneg s) (norm_nonneg (1 - s))]
  rw [Complex.sq_norm, Complex.sq_norm]
  exact normSq_reflection_eq_iff_re_half s

/-- Away from the pole of the projective coordinate, the unit circle in
`omega`-space is exactly the Riemann critical line. -/
theorem omega_norm_one_iff_re_half {s : ℂ} (hs1 : s ≠ 1) :
    ‖omega s‖ = 1 ↔ s.re = (1 / 2 : ℝ) := by
  have hden : ‖1 - s‖ ≠ 0 := by
    exact norm_ne_zero_iff.mpr (sub_ne_zero.mpr (Ne.symm hs1))
  rw [omega, Complex.norm_div, div_eq_one_iff_eq hden]
  exact norm_reflection_eq_iff_re_half s

end SecretOfAHalfFormal
