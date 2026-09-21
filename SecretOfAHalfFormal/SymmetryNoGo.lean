import Mathlib

namespace SecretOfAHalfFormal

open Complex
open scoped ComplexConjugate

/-- A concrete entire polynomial with the same reflection and conjugation
symmetries used in the centered zeta problem, but with zeros away from
Re(s)=1/2. Thus those symmetries alone cannot imply RH. -/
noncomputable def symmetryWitness (s : ℂ) : ℂ :=
  (s - ((1 / 4 : ℝ) : ℂ)) * (s - ((3 / 4 : ℝ) : ℂ))

theorem symmetryWitness_reflection (s : ℂ) :
    symmetryWitness (1 - s) = symmetryWitness s := by
  simp [symmetryWitness]
  ring

theorem symmetryWitness_conjugation (s : ℂ) :
    symmetryWitness (conj s) = conj (symmetryWitness s) := by
  simp [symmetryWitness, map_div₀]

noncomputable def offAxisWitnessZero : ℂ := ((3 / 4 : ℝ) : ℂ)

theorem symmetryWitness_has_offAxis_zero :
    symmetryWitness offAxisWitnessZero = 0 := by
  simp [symmetryWitness, offAxisWitnessZero]

theorem offAxisWitnessZero_in_critical_strip :
    0 < offAxisWitnessZero.re ∧ offAxisWitnessZero.re < 1 := by
  norm_num [offAxisWitnessZero]

theorem offAxisWitnessZero_not_on_critical_line :
    offAxisWitnessZero.re ≠ (1 / 2 : ℝ) := by
  norm_num [offAxisWitnessZero]

/-- Reflection + conjugation symmetry are compatible with an off-axis strip
zero, so any RH proof needs additional xi-specific structure. -/
theorem reflection_conjugation_symmetry_does_not_force_half_line :
    symmetryWitness offAxisWitnessZero = 0 ∧
      symmetryWitness (1 - offAxisWitnessZero) = 0 ∧
      symmetryWitness (conj offAxisWitnessZero) = 0 ∧
      offAxisWitnessZero.re ≠ (1 / 2 : ℝ) := by
  refine ⟨symmetryWitness_has_offAxis_zero, ?_, ?_, offAxisWitnessZero_not_on_critical_line⟩
  · rw [symmetryWitness_reflection]
    exact symmetryWitness_has_offAxis_zero
  · rw [symmetryWitness_conjugation, symmetryWitness_has_offAxis_zero]
    simp

end SecretOfAHalfFormal
