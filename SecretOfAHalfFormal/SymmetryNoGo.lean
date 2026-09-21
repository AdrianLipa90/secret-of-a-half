import Mathlib

namespace SecretOfAHalfFormal

open Complex

/-- A concrete entire polynomial with the same reflection and conjugation
symmetries as the centered xi problem, but with zeros off Re(s)=1/2.

This witnesses that those symmetries alone cannot prove RH. -/
def symmetryWitness (s : ℂ) : ℂ :=
  let z := s - (1 / 2 : ℂ)
  ((z - (1 / 4 : ℂ)) ^ 2 + 1) * ((z + (1 / 4 : ℂ)) ^ 2 + 1)

theorem symmetryWitness_reflection (s : ℂ) :
    symmetryWitness (1 - s) = symmetryWitness s := by
  simp [symmetryWitness]
  ring

theorem symmetryWitness_conjugation (s : ℂ) :
    symmetryWitness (conj s) = conj (symmetryWitness s) := by
  simp [symmetryWitness]
  ring

def offAxisWitnessZero : ℂ := (3 / 4 : ℂ) + I

theorem symmetryWitness_has_offAxis_zero :
    symmetryWitness offAxisWitnessZero = 0 := by
  simp [symmetryWitness, offAxisWitnessZero, Complex.I_sq]
  ring

theorem offAxisWitnessZero_in_critical_strip :
    0 < offAxisWitnessZero.re ∧ offAxisWitnessZero.re < 1 := by
  norm_num [offAxisWitnessZero]

theorem offAxisWitnessZero_not_on_critical_line :
    offAxisWitnessZero.re ≠ (1 / 2 : ℝ) := by
  norm_num [offAxisWitnessZero]

/-- Therefore reflection + conjugation symmetry + an off-axis strip zero are
jointly consistent. Any RH proof must use additional xi-specific structure. -/
theorem reflection_conjugation_symmetry_does_not_force_half_line :
    symmetryWitness offAxisWitnessZero = 0 ∧
      symmetryWitness (1 - offAxisWitnessZero) = 0 ∧
      symmetryWitness (conj offAxisWitnessZero) = 0 ∧
      offAxisWitnessZero.re ≠ (1 / 2 : ℝ) := by
  refine ⟨symmetryWitness_has_offAxis_zero, ?_, ?_, offAxisWitnessZero_not_on_critical_line⟩
  · rw [symmetryWitness_reflection]
    exact symmetryWitness_has_offAxis_zero
  · rw [symmetryWitness_conjugation]
    simp [symmetryWitness_has_offAxis_zero]

end SecretOfAHalfFormal
