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
  field_simp [hs1, hs2]
  ring

/-- In the projective coordinate omega, the triple branch is u ↦ 3u+2. -/
theorem omega_tripleMobius
    {s : ℂ} (hs1 : s ≠ 1) :
    omega (tripleMobius s) = 3 * omega s + 2 := by
  unfold omega tripleMobius
  field_simp [hs1]
  ring

/-- Exact conjugacy of the half Möbius branch to x ↦ x/2. -/
theorem collatzCoord_halfMobius
    {s : ℂ} (hs1 : s ≠ 1) (hs2 : s ≠ 2) :
    collatzCoord (halfMobius s) = collatzEven (collatzCoord s) := by
  unfold collatzCoord collatzEven
  rw [omega_halfMobius hs1 hs2]
  ring

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
    simp [collatzCoord, norm_div]
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

end SecretOfAHalfFormal
