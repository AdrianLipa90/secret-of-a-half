import Mathlib
import SecretOfAHalfFormal.RadialDefect

namespace SecretOfAHalfFormal

open Filter
open scoped Topology

/-- Endgame lemma for a Suzuki-type real-zero approximation:
if points with real spectral coordinate converge to the Suzuki coordinate of s,
then s lies on the critical line. -/
theorem re_half_of_real_suzuki_approximation
    {s : ℂ} {z : ℕ → ℂ}
    (hreal : ∀ n : ℕ, (z n).im = 0)
    (hlim : Tendsto z atTop (𝓝 (suzukiCoord s))) :
    s.re = (1 / 2 : ℝ) := by
  have him :
      Tendsto (fun n : ℕ => (z n).im) atTop
        (𝓝 (suzukiCoord s).im) :=
    Complex.continuous_im.continuousAt.tendsto.comp hlim
  have hfun : (fun n : ℕ => (z n).im) = (fun _ : ℕ => (0 : ℝ)) := by
    funext n
    exact hreal n
  rw [hfun] at him
  have hzero :
      Tendsto (fun _ : ℕ => (0 : ℝ)) atTop (𝓝 (0 : ℝ)) :=
    tendsto_const_nhds
  have him0 : (suzukiCoord s).im = 0 :=
    tendsto_nhds_unique him hzero
  exact (suzukiCoord_im_zero_iff_re_half s).mp him0

/-- Abstract Suzuki-limit incoming edge.

It is enough that every non-trivial zeta zero's Suzuki coordinate can be
obtained as a limit of real spectral points. The theorem does not construct the
approximating points or prove any compact convergence of characteristic
functions. -/
theorem riemannHypothesis_of_real_suzuki_zero_approximation
    (happrox :
      ∀ (s : ℂ), riemannZeta s = 0 →
        (¬ ∃ n : ℕ, s = -2 * (n + 1)) →
        s ≠ 1 →
        ∃ z : ℕ → ℂ,
          (∀ n : ℕ, (z n).im = 0) ∧
          Tendsto z atTop (𝓝 (suzukiCoord s))) :
    RiemannHypothesis := by
  intro s hz htriv hs1
  obtain ⟨z, hreal, hlim⟩ := happrox s hz htriv hs1
  exact re_half_of_real_suzuki_approximation hreal hlim

/-- Defect form of the same limit endgame: real spectral approximants force
the native half-axis defect to vanish. -/
theorem halfAxisDefect_eq_zero_of_real_suzuki_approximation
    {s : ℂ} {z : ℕ → ℂ}
    (hreal : ∀ n : ℕ, (z n).im = 0)
    (hlim : Tendsto z atTop (𝓝 (suzukiCoord s))) :
    halfAxisDefect s = 0 := by
  exact (halfAxisDefect_eq_zero_iff_re_half s).mpr
    (re_half_of_real_suzuki_approximation hreal hlim)

end SecretOfAHalfFormal
