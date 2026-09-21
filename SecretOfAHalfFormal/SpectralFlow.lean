import Mathlib

namespace SecretOfAHalfFormal

/-- Abstract spectral-flow lemma: if a real continuous eigenvalue branch is
positive at one positive scale and never vanishes at positive scales, then it
stays positive at every positive scale.

This is only topology/order theory. It does not identify any concrete
Riemann/Weil operator, nor prove its nondegeneracy. -/
theorem positive_on_pos_of_continuous_of_anchor_of_no_zero
    {lambda : ℝ → ℝ}
    (hcont : Continuous lambda)
    {a0 : ℝ}
    (ha0 : 0 < a0)
    (hanchor : 0 < lambda a0)
    (hnozero : ∀ a : ℝ, 0 < a → lambda a ≠ 0) :
    ∀ a : ℝ, 0 < a → 0 < lambda a := by
  intro a ha
  by_contra hnotpos
  have hle : lambda a ≤ 0 := le_of_not_gt hnotpos
  by_cases haa0 : a ≤ a0
  · have hz : (0 : ℝ) ∈ Set.Icc (lambda a) (lambda a0) := ⟨hle, hanchor.le⟩
    obtain ⟨c, hc, hc0⟩ :=
      (intermediate_value_Icc haa0 hcont.continuousOn) hz
    have hcpos : 0 < c := lt_of_lt_of_le ha hc.1
    exact (hnozero c hcpos) hc0
  · have ha0a : a0 ≤ a := le_of_not_ge haa0
    have hz : (0 : ℝ) ∈ Set.Icc (lambda a) (lambda a0) := ⟨hle, hanchor.le⟩
    obtain ⟨c, hc, hc0⟩ :=
      (intermediate_value_Icc' ha0a hcont.continuousOn) hz
    have hcpos : 0 < c := lt_of_lt_of_le ha0 hc.1
    exact (hnozero c hcpos) hc0

/-- Under continuity and one positive anchor, positivity at every positive
scale is equivalent to nondegeneracy at every positive scale. -/
theorem positive_on_pos_iff_no_zero_on_pos
    {lambda : ℝ → ℝ}
    (hcont : Continuous lambda)
    {a0 : ℝ}
    (ha0 : 0 < a0)
    (hanchor : 0 < lambda a0) :
    (∀ a : ℝ, 0 < a → 0 < lambda a) ↔
      (∀ a : ℝ, 0 < a → lambda a ≠ 0) := by
  constructor
  · intro hpos a ha
    exact ne_of_gt (hpos a ha)
  · exact positive_on_pos_of_continuous_of_anchor_of_no_zero
      hcont ha0 hanchor


/-- Explicit zero-crossing form of the spectral-flow argument: a continuous
branch that is positive at the left endpoint and negative at the right
endpoint must become degenerate somewhere between them. -/
theorem exists_zero_between_of_continuous_of_pos_neg
    {lambda : ℝ → ℝ}
    (hcont : Continuous lambda)
    {a b : ℝ}
    (hab : a ≤ b)
    (ha : 0 < lambda a)
    (hb : lambda b < 0) :
    ∃ c ∈ Set.Icc a b, lambda c = 0 := by
  have hz : (0 : ℝ) ∈ Set.Icc (lambda b) (lambda a) := ⟨hb.le, ha.le⟩
  exact (intermediate_value_Icc' hab hcont.continuousOn) hz

end SecretOfAHalfFormal
