import Mathlib

namespace SecretOfAHalfFormal

/-- Abstract two-channel destructive cancellation. -/
def TwoChannelCancellation (a b : ℂ) : Prop := a + b = 0

/-- Destructive cancellation forces equal channel amplitudes.  This conclusion
contains no horizontal coordinate and therefore cannot by itself force
Re(s)=1/2. -/
theorem twoChannelCancellation_equal_norm
    {a b : ℂ} (h : TwoChannelCancellation a b) :
    ‖a‖ = ‖b‖ := by
  unfold TwoChannelCancellation at h
  have hb : b = -a := by
    linear_combination h
  rw [hb, norm_neg]

/-- The corresponding squared channel weights are equal as well. -/
theorem twoChannelCancellation_equal_norm_sq
    {a b : ℂ} (h : TwoChannelCancellation a b) :
    ‖a‖ ^ 2 = ‖b‖ ^ 2 := by
  rw [twoChannelCancellation_equal_norm h]

/-- If the cancelling pair is non-degenerate, the usual Euclidean normalized
weight of either channel is exactly 1/2.  This is a channel-space half, not a
critical-line theorem. -/
theorem twoChannelCancellation_weight_half
    {a b : ℂ} (ha : a ≠ 0) (h : TwoChannelCancellation a b) :
    ‖a‖ ^ 2 / (‖a‖ ^ 2 + ‖b‖ ^ 2) = (1 / 2 : ℝ) := by
  have hab : ‖a‖ = ‖b‖ := twoChannelCancellation_equal_norm h
  have hpos : 0 < ‖a‖ ^ 2 := sq_pos_of_pos (norm_pos_iff.mpr ha)
  rw [← hab]
  field_simp
  nlinarith

end SecretOfAHalfFormal
