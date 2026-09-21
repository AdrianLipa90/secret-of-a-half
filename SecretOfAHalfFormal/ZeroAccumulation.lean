import Mathlib
import Mathlib.NumberTheory.LSeries.ZetaZeros

namespace SecretOfAHalfFormal

open Filter
open scoped Topology

/-- A sequence of zeta zeros converging to a zeta zero is eventually constant.
This packages mathlib's discreteness theorem for the zeta zero set into the
form needed by contraction-orbit arguments. -/
theorem zetaZero_sequence_eventually_eq_limit
    {z : ℕ → ℂ} {rho : ℂ}
    (hrho : riemannZeta rho = 0)
    (hz : ∀ n : ℕ, riemannZeta (z n) = 0)
    (hlim : Tendsto z atTop (𝓝 rho)) :
    ∀ᶠ n in atTop, z n = rho := by
  have hrho_mem : rho ∈ riemannZetaZeros :=
    (mem_riemannZetaZeros).2 hrho
  have hzmem : ∀ᶠ n in atTop, z n ∈ riemannZetaZeros :=
    Eventually.of_forall fun n => (mem_riemannZetaZeros).2 (hz n)
  have hwithin : Tendsto z atTop (𝓝[riemannZetaZeros] rho) :=
    tendsto_nhdsWithin_iff.mpr ⟨hlim, hzmem⟩
  rw [isDiscrete_riemannZetaZeros.nhdsWithin rho hrho_mem] at hwithin
  simpa only [tendsto_pure] using hwithin

/-- There is no sequence of pairwise-punctured zeta zeros converging to a zeta
zero. -/
theorem no_distinct_zetaZero_sequence_converges
    {z : ℕ → ℂ} {rho : ℂ}
    (hrho : riemannZeta rho = 0)
    (hz : ∀ n : ℕ, riemannZeta (z n) = 0)
    (hne : ∀ n : ℕ, z n ≠ rho)
    (hlim : Tendsto z atTop (𝓝 rho)) :
    False := by
  have hev := zetaZero_sequence_eventually_eq_limit hrho hz hlim
  obtain ⟨N, hN⟩ := eventually_atTop.mp hev
  exact hne N (hN N le_rfl)

/-- Any zero-preserving dynamical orbit that converges to a zeta zero must
eventually land exactly on that limiting zero. -/
theorem zero_preserving_orbit_eventually_hits_limit
    {F : ℂ → ℂ} {z0 rho : ℂ}
    (hrho : riemannZeta rho = 0)
    (hz0 : riemannZeta z0 = 0)
    (hpres : ∀ z : ℂ, riemannZeta z = 0 → riemannZeta (F z) = 0)
    (hlim : Tendsto (fun n : ℕ => (F^[n]) z0) atTop (𝓝 rho)) :
    ∀ᶠ n in atTop, (F^[n]) z0 = rho := by
  apply zetaZero_sequence_eventually_eq_limit hrho
  · intro n
    induction n with
    | zero =>
        simpa using hz0
    | succ n ih =>
        simpa [Function.iterate_succ_apply'] using hpres ((F^[n]) z0) ih
  · exact hlim


/-- Therefore a zero-preserving orbit cannot converge to a zeta zero while
remaining distinct from that limit at every finite iterate. -/
theorem no_zero_preserving_convergent_orbit_without_hit
    {F : ℂ → ℂ} {z0 rho : ℂ}
    (hrho : riemannZeta rho = 0)
    (hz0 : riemannZeta z0 = 0)
    (hpres : ∀ z : ℂ, riemannZeta z = 0 → riemannZeta (F z) = 0)
    (hlim : Tendsto (fun n : ℕ => (F^[n]) z0) atTop (𝓝 rho))
    (hne : ∀ n : ℕ, (F^[n]) z0 ≠ rho) :
    False := by
  have hev :=
    zero_preserving_orbit_eventually_hits_limit hrho hz0 hpres hlim
  obtain ⟨N, hN⟩ := eventually_atTop.mp hev
  exact hne N (hN N le_rfl)


/-- Any continuous real-parameter path that remains entirely inside the zeta
zero set is constant. This is the connected-domain counterpart of the
sequence accumulation obstruction. -/
theorem continuous_zetaZero_path_constant
    {gamma : ℝ → ℂ}
    (hgamma : Continuous gamma)
    (hzero : ∀ t : ℝ, riemannZeta (gamma t) = 0)
    (a b : ℝ) :
    gamma a = gamma b := by
  apply isPreconnected_univ.constant_of_mapsTo
      isDiscrete_riemannZetaZeros hgamma.continuousOn
  · intro t ht
    exact (mem_riemannZetaZeros).2 (hzero t)
  · exact Set.mem_univ a
  · exact Set.mem_univ b

/-- In particular, a continuous zero-preserving deformation cannot move a
zeta zero through a nonconstant real-parameter orbit. -/
theorem continuous_zetaZero_deformation_fixed
    {gamma : ℝ → ℂ} {rho : ℂ}
    (hgamma : Continuous gamma)
    (hzero : ∀ t : ℝ, riemannZeta (gamma t) = 0)
    (h0 : gamma 0 = rho) :
    ∀ t : ℝ, gamma t = rho := by
  intro t
  calc
    gamma t = gamma 0 := continuous_zetaZero_path_constant hgamma hzero t 0
    _ = rho := h0

end SecretOfAHalfFormal
