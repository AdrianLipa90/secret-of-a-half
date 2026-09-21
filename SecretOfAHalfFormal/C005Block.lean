import Mathlib

namespace SecretOfAHalfFormal

/-- Scalar Schur-complement certificate underlying the C005 2x2 block bound.

If the diagonal lower bounds are non-negative and the determinant margin is
non-negative, then the associated real quadratic form is non-negative. This is
an exact algebraic lemma only; it does not establish any of the analytic C005
operator bounds. -/
theorem c005_scalar_block_quadratic_nonneg
    {mu eps nu x y : ℝ}
    (hmu : 0 ≤ mu)
    (hnu : 0 ≤ nu)
    (hdet : eps ^ 2 ≤ mu * nu) :
    0 ≤ mu * x ^ 2 - 2 * eps * x * y + nu * y ^ 2 := by
  by_cases hmu0 : mu = 0
  · subst mu
    have heps : eps = 0 := by
      nlinarith [sq_nonneg eps]
    subst eps
    simpa using mul_nonneg hnu (sq_nonneg y)
  · have hmupos : 0 < mu := lt_of_le_of_ne hmu (Ne.symm hmu0)
    have hsquare : 0 ≤ (mu * x - eps * y) ^ 2 := sq_nonneg _
    have hmargin : 0 ≤ mu * nu - eps ^ 2 := by
      nlinarith
    have htail : 0 ≤ (mu * nu - eps ^ 2) * y ^ 2 := by
      exact mul_nonneg hmargin (sq_nonneg y)
    have hscaled :
        0 ≤ mu * (mu * x ^ 2 - 2 * eps * x * y + nu * y ^ 2) := by
      nlinarith
    nlinarith

/-- The determinant condition can be exposed as a non-negative margin. -/
theorem c005_determinant_margin_nonneg
    {mu eps nu : ℝ}
    (hdet : eps ^ 2 ≤ mu * nu) :
    0 ≤ mu * nu - eps ^ 2 := by
  linarith


/-- A strict Schur margin removes scalar zero modes completely.  This is the
finite-dimensional algebraic analogue of the nondegeneracy needed in the
localized spectral-flow route. -/
theorem c005_scalar_block_quadratic_eq_zero_iff
    {mu eps nu x y : ℝ}
    (hmu : 0 < mu)
    (hdet : eps ^ 2 < mu * nu) :
    mu * x ^ 2 - 2 * eps * x * y + nu * y ^ 2 = 0 ↔
      x = 0 ∧ y = 0 := by
  constructor
  · intro hq
    have hsquare : 0 ≤ (mu * x - eps * y) ^ 2 := sq_nonneg _
    have hmargin : 0 < mu * nu - eps ^ 2 := by
      linarith
    have hid :
        mu * (mu * x ^ 2 - 2 * eps * x * y + nu * y ^ 2) =
          (mu * x - eps * y) ^ 2 +
            (mu * nu - eps ^ 2) * y ^ 2 := by
      ring
    have htail : 0 ≤ (mu * nu - eps ^ 2) * y ^ 2 :=
      mul_nonneg hmargin.le (sq_nonneg y)
    have hsum :
        (mu * x - eps * y) ^ 2 +
            (mu * nu - eps ^ 2) * y ^ 2 = 0 := by
      rw [← hid, hq]
      ring
    have htail0 : (mu * nu - eps ^ 2) * y ^ 2 = 0 := by
      nlinarith
    have hy2 : y ^ 2 = 0 :=
      (mul_eq_zero.mp htail0).resolve_left hmargin.ne'
    have hy : y = 0 := (sq_eq_zero_iff).mp hy2
    subst y
    simp at hq
    have hx2 : x ^ 2 = 0 :=
      (mul_eq_zero.mp hq).resolve_left hmu.ne'
    exact ⟨(sq_eq_zero_iff.mp hx2), rfl⟩
  · rintro ⟨rfl, rfl⟩
    ring

end SecretOfAHalfFormal
