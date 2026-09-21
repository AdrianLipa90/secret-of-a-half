import Mathlib
import SecretOfAHalfFormal.RiemannSeam
import SecretOfAHalfFormal.RHBridge

namespace SecretOfAHalfFormal

open scoped ComplexConjugate

/-- Exact reciprocal--conjugation defect. It vanishes precisely when the
reciprocal and conjugation actions coincide. -/
noncomputable def reciprocalConjugationDefect (u : ℂ) : ℝ :=
  ‖u⁻¹ - conj u‖ ^ 2

theorem reciprocalConjugationDefect_nonneg (u : ℂ) :
    0 ≤ reciprocalConjugationDefect u := by
  unfold reciprocalConjugationDefect
  exact sq_nonneg _

/-- Vanishing of the exact defect is equivalent to the reciprocal--conjugation
seam, with no nonzero hypothesis needed for this direction. -/
theorem reciprocalConjugationDefect_eq_zero_iff_seam (u : ℂ) :
    reciprocalConjugationDefect u = 0 ↔ reciprocalConjugationSeam u := by
  unfold reciprocalConjugationDefect reciprocalConjugationSeam
  rw [sq_eq_zero_iff]
  rw [norm_eq_zero]
  exact sub_eq_zero

/-- For the projective Riemann coordinate, vanishing of the exact defect is
equivalent to the critical-line condition away from the exceptional points. -/
theorem omega_defect_eq_zero_iff_re_half
    {s : ℂ} (hs0 : s ≠ 0) (hs1 : s ≠ 1) :
    reciprocalConjugationDefect (omega s) = 0 ↔
      s.re = (1 / 2 : ℝ) := by
  rw [reciprocalConjugationDefect_eq_zero_iff_seam]
  exact omega_reciprocalConjugationSeam_iff_re_half hs0 hs1


/-- Native half-axis / PhaseNav closure defect in scalar form. -/
noncomputable def halfAxisDefect (s : ℂ) : ℝ :=
  (s.re - (1 / 2 : ℝ)) ^ 2

theorem halfAxisDefect_nonneg (s : ℂ) :
    0 ≤ halfAxisDefect s := by
  unfold halfAxisDefect
  exact sq_nonneg _

theorem halfAxisDefect_eq_zero_iff_re_half (s : ℂ) :
    halfAxisDefect s = 0 ↔ s.re = (1 / 2 : ℝ) := by
  unfold halfAxisDefect
  rw [sq_eq_zero_iff, sub_eq_zero]

/-- The native PhaseNav half-axis defect and the reciprocal--conjugation defect
have exactly the same zero locus away from the projective exceptional points. -/
theorem omega_reciprocalDefect_zero_iff_halfAxisDefect_zero
    {s : ℂ} (hs0 : s ≠ 0) (hs1 : s ≠ 1) :
    reciprocalConjugationDefect (omega s) = 0 ↔
      halfAxisDefect s = 0 := by
  rw [omega_defect_eq_zero_iff_re_half hs0 hs1,
      halfAxisDefect_eq_zero_iff_re_half]


/-- Exact radial form of the reciprocal--conjugation defect. -/
theorem reciprocalConjugationDefect_eq_normSq_formula
    {u : ℂ} (hu : u ≠ 0) :
    reciprocalConjugationDefect u =
      (1 - Complex.normSq u) ^ 2 / Complex.normSq u := by
  have hid :
      u⁻¹ - conj u =
        (((1 - Complex.normSq u : ℝ) : ℂ) / u) := by
    apply (eq_div_iff hu).2
    rw [sub_mul]
    simp [hu, Complex.normSq_eq_conj_mul_self]
  unfold reciprocalConjugationDefect
  rw [← Complex.normSq_eq_norm_sq, hid, Complex.normSq_div,
      Complex.normSq_ofReal]
  ring

/-- Exact positive-weight crosswalk between the reciprocal--conjugation defect
and the native half-axis / PhaseNav closure defect. -/
theorem omega_reciprocalDefect_eq_weighted_halfAxisDefect
    {s : ℂ} (hs0 : s ≠ 0) (hs1 : s ≠ 1) :
    reciprocalConjugationDefect (omega s) =
      4 * halfAxisDefect s /
        (Complex.normSq s * Complex.normSq (1 - s)) := by
  have hden : (1 : ℂ) - s ≠ 0 := sub_ne_zero.mpr (Ne.symm hs1)
  have homega : omega s ≠ 0 := by
    unfold omega
    exact div_ne_zero hs0 hden
  have hA : Complex.normSq s ≠ 0 :=
    ne_of_gt ((Complex.normSq_pos).2 hs0)
  have hB : Complex.normSq (1 - s) ≠ 0 :=
    ne_of_gt ((Complex.normSq_pos).2 hden)
  have hdiff :
      Complex.normSq s - Complex.normSq (1 - s) =
        2 * s.re - 1 := by
    simp [Complex.normSq_apply]
    ring
  rw [reciprocalConjugationDefect_eq_normSq_formula homega]
  unfold omega
  rw [Complex.normSq_div]
  unfold halfAxisDefect
  field_simp [hA, hB]
  rw [hdiff]
  ring

/-- The missing statement written as defect vanishing on every non-trivial
zeta zero. -/
def ZeroReciprocalDefectCondition : Prop :=
  ∀ (s : ℂ), riemannZeta s = 0 →
    (¬ ∃ n : ℕ, s = -2 * (n + 1)) →
    s ≠ 1 →
    reciprocalConjugationDefect (omega s) = 0

/-- The defect-vanishing formulation is exactly RH-equivalent. -/
theorem zeroReciprocalDefect_iff_riemannHypothesis :
    ZeroReciprocalDefectCondition ↔ RiemannHypothesis := by
  constructor
  · intro h s hz htriv hs1
    have hs0 : s ≠ 0 := riemannZeta_zero_point_ne_zero hz
    exact (omega_defect_eq_zero_iff_re_half hs0 hs1).mp
      (h s hz htriv hs1)
  · intro h s hz htriv hs1
    have hs0 : s ≠ 0 := riemannZeta_zero_point_ne_zero hz
    exact (omega_defect_eq_zero_iff_re_half hs0 hs1).mpr
      (h s hz htriv hs1)


/-- The native half-axis / PhaseNav closure condition on all non-trivial zeta
zeros. -/
def ZeroHalfAxisDefectCondition : Prop :=
  ∀ (s : ℂ), riemannZeta s = 0 →
    (¬ ∃ n : ℕ, s = -2 * (n + 1)) →
    s ≠ 1 →
    halfAxisDefect s = 0

theorem zeroHalfAxisDefect_iff_riemannHypothesis :
    ZeroHalfAxisDefectCondition ↔ RiemannHypothesis := by
  constructor
  · intro h s hz htriv hs1
    exact (halfAxisDefect_eq_zero_iff_re_half s).mp
      (h s hz htriv hs1)
  · intro h s hz htriv hs1
    exact (halfAxisDefect_eq_zero_iff_re_half s).mpr
      (h s hz htriv hs1)

theorem zeroHalfAxisDefect_iff_zeroReciprocalDefect :
    ZeroHalfAxisDefectCondition ↔ ZeroReciprocalDefectCondition := by
  rw [zeroHalfAxisDefect_iff_riemannHypothesis,
      zeroReciprocalDefect_iff_riemannHypothesis]

/-- Abstract incoming-edge interface for an operator/energy construction.

To prove RH through an independently constructed scalar certificate E, it is
enough to prove on every non-trivial zero that (i) E vanishes and (ii) E is
exactly the reciprocal--conjugation defect. This theorem deliberately does not
provide either analytic/operator premise. -/
theorem riemannHypothesis_of_zero_energy_representation
    {E : ℂ → ℝ}
    (hEzero :
      ∀ (s : ℂ), riemannZeta s = 0 →
        (¬ ∃ n : ℕ, s = -2 * (n + 1)) →
        s ≠ 1 →
        E s = 0)
    (hErepr :
      ∀ (s : ℂ), riemannZeta s = 0 →
        (¬ ∃ n : ℕ, s = -2 * (n + 1)) →
        s ≠ 1 →
        E s = reciprocalConjugationDefect (omega s)) :
    RiemannHypothesis := by
  rw [← zeroReciprocalDefect_iff_riemannHypothesis]
  intro s hz htriv hs1
  rw [← hErepr s hz htriv hs1]
  exact hEzero s hz htriv hs1


/-- Stronger operator-facing interface: an independently constructed energy
that vanishes on non-trivial zeros and coercively dominates the projective
defect with a strictly positive constant forces RH. -/
theorem riemannHypothesis_of_coercive_zero_energy
    {E : ℂ → ℝ} {c : ℝ}
    (hc : 0 < c)
    (hEzero :
      ∀ (s : ℂ), riemannZeta s = 0 →
        (¬ ∃ n : ℕ, s = -2 * (n + 1)) →
        s ≠ 1 →
        E s = 0)
    (hcoercive :
      ∀ (s : ℂ), riemannZeta s = 0 →
        (¬ ∃ n : ℕ, s = -2 * (n + 1)) →
        s ≠ 1 →
        c * reciprocalConjugationDefect (omega s) ≤ E s) :
    RiemannHypothesis := by
  rw [← zeroReciprocalDefect_iff_riemannHypothesis]
  intro s hz htriv hs1
  have hnonneg : 0 ≤ reciprocalConjugationDefect (omega s) :=
    reciprocalConjugationDefect_nonneg _
  have hupper :
      c * reciprocalConjugationDefect (omega s) ≤ 0 := by
    simpa [hEzero s hz htriv hs1] using hcoercive s hz htriv hs1
  have hdefect_le : reciprocalConjugationDefect (omega s) ≤ 0 := by
    nlinarith
  exact le_antisymm hdefect_le hnonneg

end SecretOfAHalfFormal
