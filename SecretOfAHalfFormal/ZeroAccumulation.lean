import Mathlib
import Mathlib.NumberTheory.LSeries.ZetaZeros

namespace SecretOfAHalfFormal

open Filter

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

end SecretOfAHalfFormal
