import Mathlib

namespace SecretOfAHalfFormal

/-- A concrete entire polynomial with the same centered reflection and
conjugation symmetries as the xi problem, but with zeros off Re(s)=1/2.

In z = s - 1/2 coordinates it is
  ((z^2 + 15/16)^2 + 1/4).
Its roots are ±1/4 ± i. -/
noncomputable def symmetryWitness (s : ℂ) : ℂ :=
  let z := s - (1 / 2 : ℂ)
  (z ^ 2 + (15 / 16 : ℂ)) ^ 2 + (1 / 4 : ℂ)

theorem symmetryWitness_reflection (s : ℂ) :
    symmetryWitness (1 - s) = symmetryWitness s := by
  simp [symmetryWitness]
  ring

theorem symmetryWitness_conjugation (s : ℂ) :
    symmetryWitness (Complex.conj s) = Complex.conj (symmetryWitness s) := by
  simp [symmetryWitness]
  ring

noncomputable def offAxisWitnessZero : ℂ := (3 / 4 : ℂ) + Complex.I

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

/-- Reflection + conjugation symmetry are jointly consistent with a zero
strictly inside the critical strip but off the critical line. Thus those
symmetries alone cannot prove RH; an xi-specific incoming theorem is needed. -/
theorem reflection_conjugation_symmetry_does_not_force_half_line :
    symmetryWitness offAxisWitnessZero = 0 ∧
      symmetryWitness (1 - offAxisWitnessZero) = 0 ∧
      symmetryWitness (Complex.conj offAxisWitnessZero) = 0 ∧
      offAxisWitnessZero.re ≠ (1 / 2 : ℝ) := by
  refine ⟨symmetryWitness_has_offAxis_zero, ?_, ?_, offAxisWitnessZero_not_on_critical_line⟩
  · rw [symmetryWitness_reflection]
    exact symmetryWitness_has_offAxis_zero
  · rw [symmetryWitness_conjugation, symmetryWitness_has_offAxis_zero]
    simp

end SecretOfAHalfFormal
