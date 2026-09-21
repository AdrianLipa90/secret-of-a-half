import Mathlib
import SecretOfAHalfFormal.RiemannSeam

namespace SecretOfAHalfFormal

/-- The two Möbius branches used in the project's Collatz/Riemann coordinate. -/
noncomputable def halfMobius (s : ℂ) : ℂ := s / (2 - s)
noncomputable def tripleMobius (s : ℂ) : ℂ := (s + 2) / 3

/-- Rescale the projective Riemann coordinate so that the induced affine
branches are literally the standard Collatz maps x ↦ x/2 and x ↦ 3x+1. -/
noncomputable def collatzCoord (s : ℂ) : ℂ := omega s / 2

noncomputable def collatzEven (x : ℂ) : ℂ := x / 2
noncomputable def collatzOdd (x : ℂ) : ℂ := 3 * x + 1

/-- In the projective coordinate omega, the half Möbius branch is u ↦ u/2. -/
theorem omega_halfMobius
    {s : ℂ} (hs1 : s ≠ 1) (hs2 : s ≠ 2) :
    omega (halfMobius s) = omega s / 2 := by
  unfold omega halfMobius
  have h2s : (2 : ℂ) - s ≠ 0 := sub_ne_zero.mpr (Ne.symm hs2)
  have h1s : (1 : ℂ) - s ≠ 0 := sub_ne_zero.mpr (Ne.symm hs1)
  rw [show 1 - s / (2 - s) = ((2 : ℂ) - 2 * s) / (2 - s) by
    field_simp [h2s]
    ring]
  rw [div_div_div_cancel_right₀ h2s]
  rw [show (2 : ℂ) - 2 * s = 2 * (1 - s) by ring]
  field_simp [h1s]

/-- In the projective coordinate omega, the triple branch is u ↦ 3u+2. -/
theorem omega_tripleMobius
    {s : ℂ} (hs1 : s ≠ 1) :
    omega (tripleMobius s) = 3 * omega s + 2 := by
  unfold omega tripleMobius
  have h1s : (1 : ℂ) - s ≠ 0 := sub_ne_zero.mpr (Ne.symm hs1)
  have h3 : (3 : ℂ) ≠ 0 := by norm_num
  rw [show 1 - (s + 2) / 3 = (1 - s) / 3 by
    field_simp
    ring]
  rw [div_div_div_cancel_right₀ h3]
  field_simp [h1s]
  ring

/-- Exact conjugacy of the half Möbius branch to x ↦ x/2. -/
theorem collatzCoord_halfMobius
    {s : ℂ} (hs1 : s ≠ 1) (hs2 : s ≠ 2) :
    collatzCoord (halfMobius s) = collatzEven (collatzCoord s) := by
  unfold collatzCoord collatzEven
  rw [omega_halfMobius hs1 hs2]

/-- Exact conjugacy of the triple Möbius branch to x ↦ 3x+1. -/
theorem collatzCoord_tripleMobius
    {s : ℂ} (hs1 : s ≠ 1) :
    collatzCoord (tripleMobius s) = collatzOdd (collatzCoord s) := by
  unfold collatzCoord collatzOdd
  rw [omega_tripleMobius hs1]
  ring

/-- In the exact Collatz coordinate, the critical line is the circle of
radius 1/2. -/
theorem collatzCoord_norm_half_iff_re_half
    {s : ℂ} (hs1 : s ≠ 1) :
    ‖collatzCoord s‖ = (1 / 2 : ℝ) ↔ s.re = (1 / 2 : ℝ) := by
  have hnorm : ‖collatzCoord s‖ = ‖omega s‖ / 2 := by
    simp [collatzCoord]
  rw [hnorm]
  constructor
  · intro h
    have homega : ‖omega s‖ = 1 := by
      nlinarith
    exact (omega_norm_one_iff_re_half hs1).mp homega
  · intro h
    have homega : ‖omega s‖ = 1 :=
      (omega_norm_one_iff_re_half hs1).mpr h
    nlinarith

/-- The missing zero-confinement statement in literal Collatz coordinates. -/
def ZeroCollatzHalfCircleCondition : Prop :=
  ∀ (s : ℂ), riemannZeta s = 0 →
    (¬ ∃ n : ℕ, s = -2 * (n + 1)) →
    s ≠ 1 →
    ‖collatzCoord s‖ = (1 / 2 : ℝ)

/-- The Collatz-coordinate half-circle condition is exactly RH, not an
independent premise. -/
theorem zeroCollatzHalfCircle_iff_riemannHypothesis :
    ZeroCollatzHalfCircleCondition ↔ RiemannHypothesis := by
  constructor
  · intro h s hz htriv hs1
    exact (collatzCoord_norm_half_iff_re_half hs1).mp (h s hz htriv hs1)
  · intro h s hz htriv hs1
    exact (collatzCoord_norm_half_iff_re_half hs1).mpr (h s hz htriv hs1)

/-- Canonical odd Möbius branch obtained by conjugating x ↦ 3x+1 directly
through omega, without the extra factor-of-two rescaling. -/
noncomputable def canonicalOddMobius (s : ℂ) : ℂ := (2 * s + 1) / (s + 2)

/-- In omega-space the canonical odd Möbius branch is literally u ↦ 3u+1. -/
theorem omega_canonicalOddMobius
    {s : ℂ} (hs1 : s ≠ 1) (hsm2 : s ≠ -2) :
    omega (canonicalOddMobius s) = 3 * omega s + 1 := by
  unfold omega canonicalOddMobius
  have hsp2 : s + 2 ≠ 0 := by
    intro h
    apply hsm2
    linear_combination h
  have h1s : (1 : ℂ) - s ≠ 0 := sub_ne_zero.mpr (Ne.symm hs1)
  rw [show 1 - (2 * s + 1) / (s + 2) = (1 - s) / (s + 2) by
    field_simp [hsp2]
    ring]
  rw [div_div_div_cancel_right₀ hsp2]
  field_simp [h1s]
  ring

/-- Accelerated odd Collatz step and the two-step radial selector used in the
project's Stage-D mechanism. -/
noncomputable def acceleratedOdd (x : ℂ) : ℂ := (3 * x + 1) / 2
noncomputable def selfDualWord (x : ℂ) : ℂ := acceleratedOdd x / 2

/-- The RL word contracts affine deviation from the self-dual point by 3/4. -/
theorem selfDualWord_deviation (x : ℂ) :
    selfDualWord x - 1 = (3 / 4 : ℂ) * (x - 1) := by
  unfold selfDualWord acceleratedOdd
  ring

/-- The self-dual point is the unique fixed point of the RL Collatz word. -/
theorem selfDualWord_fixed_iff (x : ℂ) :
    selfDualWord x = x ↔ x = 1 := by
  constructor
  · intro h
    have hd := selfDualWord_deviation x
    rw [h] at hd
    apply sub_eq_zero.mp
    linear_combination 4 * hd
  · rintro rfl
    norm_num [selfDualWord, acceleratedOdd]

/-- Real radial version: the same RL word contracts distance to q=1 by 3/4. -/
noncomputable def radialSelfDualWord (q : ℝ) : ℝ := (3 * q + 1) / 4

theorem radialSelfDualWord_deviation (q : ℝ) :
    radialSelfDualWord q - 1 = (3 / 4 : ℝ) * (q - 1) := by
  unfold radialSelfDualWord
  ring

theorem radialSelfDualWord_fixed_iff (q : ℝ) :
    radialSelfDualWord q = q ↔ q = 1 := by
  constructor
  · intro h
    unfold radialSelfDualWord at h
    linarith
  · rintro rfl
    norm_num [radialSelfDualWord]

/-- For the Riemann projective radius q=|omega(s)|, fixedness under the RL
radial Collatz selector is exactly the critical-line condition. -/
theorem radialSelfDualWord_omega_fixed_iff_re_half
    {s : ℂ} (hs1 : s ≠ 1) :
    radialSelfDualWord ‖omega s‖ = ‖omega s‖ ↔
      s.re = (1 / 2 : ℝ) := by
  rw [radialSelfDualWord_fixed_iff]
  exact omega_norm_one_iff_re_half hs1

/-- The dynamic fixed-point formulation for all non-trivial zeros. -/
def ZeroRadialCollatzFixedCondition : Prop :=
  ∀ (s : ℂ), riemannZeta s = 0 →
    (¬ ∃ n : ℕ, s = -2 * (n + 1)) →
    s ≠ 1 →
    radialSelfDualWord ‖omega s‖ = ‖omega s‖

/-- The radial Collatz fixed-point condition is exactly RH. Any proof route
using it must derive it independently from zeta/arithmetic structure. -/
theorem zeroRadialCollatzFixed_iff_riemannHypothesis :
    ZeroRadialCollatzFixedCondition ↔ RiemannHypothesis := by
  constructor
  · intro h s hz htriv hs1
    exact (radialSelfDualWord_omega_fixed_iff_re_half hs1).mp
      (h s hz htriv hs1)
  · intro h s hz htriv hs1
    exact (radialSelfDualWord_omega_fixed_iff_re_half hs1).mpr
      (h s hz htriv hs1)

end SecretOfAHalfFormal
