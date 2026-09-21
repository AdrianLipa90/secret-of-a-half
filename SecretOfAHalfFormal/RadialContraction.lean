import Mathlib
import SecretOfAHalfFormal.CollatzConjugacy
import SecretOfAHalfFormal.RadialDefect

namespace SecretOfAHalfFormal

/-- Reciprocal--conjugation defect written only in the positive radial
coordinate q = |u|. -/
noncomputable def radialReciprocalDefect (q : ℝ) : ℝ :=
  (q - 1 / q) ^ 2

/-- Exact multiplicative factor induced on the reciprocal defect by the
Stage-D radial Collatz selector q ↦ (3q+1)/4. -/
noncomputable def radialCollatzDefectFactor (q : ℝ) : ℝ :=
  9 * q ^ 2 * (3 * q + 5) ^ 2 /
    (16 * (q + 1) ^ 2 * (3 * q + 1) ^ 2)

/-- The complex reciprocal--conjugation defect depends only on |u|. -/
theorem reciprocalConjugationDefect_eq_radialReciprocalDefect
    {u : ℂ} (hu : u ≠ 0) :
    reciprocalConjugationDefect u = radialReciprocalDefect ‖u‖ := by
  rw [reciprocalConjugationDefect_eq_normSq_formula hu,
      Complex.normSq_eq_norm_sq]
  unfold radialReciprocalDefect
  have hnorm : ‖u‖ ≠ 0 := norm_ne_zero_iff.mpr hu
  field_simp [hnorm]
  ring

/-- Exact Lyapunov-factor identity for one radial Collatz step. -/
theorem radialReciprocalDefect_step_factor
    {q : ℝ} (hq : 0 < q) :
    radialReciprocalDefect (radialSelfDualWord q) =
      radialCollatzDefectFactor q * radialReciprocalDefect q := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hq1 : q + 1 ≠ 0 := by nlinarith
  have h3 : 3 * q + 1 ≠ 0 := by nlinarith
  unfold radialReciprocalDefect radialSelfDualWord radialCollatzDefectFactor
  field_simp [hq0, hq1, h3]
  ring

theorem radialCollatzDefectFactor_nonneg
    {q : ℝ} (hq : 0 < q) :
    0 ≤ radialCollatzDefectFactor q := by
  unfold radialCollatzDefectFactor
  positivity

/-- The multiplicative factor is strictly below one on the positive radial
domain.  Algebraically, denominator minus numerator factors as
(3q+4)(7q+1)(3q^2+q+4). -/
theorem radialCollatzDefectFactor_lt_one
    {q : ℝ} (hq : 0 < q) :
    radialCollatzDefectFactor q < 1 := by
  unfold radialCollatzDefectFactor
  have hden :
      0 < 16 * (q + 1) ^ 2 * (3 * q + 1) ^ 2 := by
    positivity
  rw [div_lt_one hden]
  have hp :
      0 < (3 * q + 4) * (7 * q + 1) *
        (3 * q ^ 2 + q + 4) := by
    positivity
  nlinarith

theorem radialReciprocalDefect_pos
    {q : ℝ} (hq : 0 < q) (hq1 : q ≠ 1) :
    0 < radialReciprocalDefect q := by
  unfold radialReciprocalDefect
  apply sq_pos_of_ne_zero
  intro h
  have hq0 : q ≠ 0 := ne_of_gt hq
  field_simp [hq0] at h
  apply hq1
  nlinarith

/-- The radial Collatz selector is a strict Lyapunov contraction for the exact
reciprocal--conjugation defect away from the self-dual point q=1. -/
theorem radialReciprocalDefect_strictly_contracts
    {q : ℝ} (hq : 0 < q) (hq1 : q ≠ 1) :
    radialReciprocalDefect (radialSelfDualWord q) <
      radialReciprocalDefect q := by
  rw [radialReciprocalDefect_step_factor hq]
  have hfactor := radialCollatzDefectFactor_lt_one hq
  have hdefect := radialReciprocalDefect_pos hq hq1
  have hmul :=
    mul_lt_mul_of_pos_right hfactor hdefect
  simpa using hmul

/-- Non-strict version valid on the whole positive radial domain, including
the fixed point. -/
theorem radialReciprocalDefect_nonincreasing
    {q : ℝ} (hq : 0 < q) :
    radialReciprocalDefect (radialSelfDualWord q) ≤
      radialReciprocalDefect q := by
  by_cases hq1 : q = 1
  · subst q
    norm_num [radialReciprocalDefect, radialSelfDualWord]
  · exact (radialReciprocalDefect_strictly_contracts hq hq1).le

end SecretOfAHalfFormal
