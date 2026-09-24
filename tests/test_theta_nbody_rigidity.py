from __future__ import annotations

import mpmath as mp

from secret_of_a_half.theta_nbody_rigidity import (
    external_bilinear_value,
    hermitian_jensen_value,
    nbody_log_partition_hessian_real,
    riemann_external_bilinear,
    riemann_hermitian_jensen,
    tent_external_tilt_fourier,
    tent_kernel,
    tent_nu2,
    tent_transform,
    theta_transverse_potential,
)


def test_tent_transform_matches_direct_fourier_integral():
    with mp.workdps(60):
        z = mp.mpc("0.7", "0.2")
        direct = mp.quad(lambda t: tent_kernel(t) * mp.exp(-1j * z * t), [-2, 0, 2])
        assert abs(direct - tent_transform(z)) < mp.mpf("1e-50")


def _direct_tent_nu2(t: mp.mpf) -> mp.mpf:
    lo = max(mp.mpf(-2), t - 2)
    hi = min(mp.mpf(2), t + 2)
    if lo >= hi:
        return mp.mpf(0)
    pts = [lo]
    for p in (mp.mpf(0), t):
        if lo < p < hi:
            pts.append(p)
    pts.append(hi)
    return mp.quad(lambda s: (t - 2 * s) ** 2 * tent_kernel(t - s) * tent_kernel(s), pts)


def test_tent_nu2_piecewise_polynomial_matches_definition():
    with mp.workdps(60):
        for t in (mp.mpf("0.5"), mp.mpf("2.5")):
            assert abs(tent_nu2(t) - _direct_tent_nu2(t)) < mp.mpf("1e-50")


def test_external_and_hermitian_tent_quantities_are_distinct():
    with mp.workdps(70):
        y = mp.mpf("0.1")
        x = mp.pi
        z = mp.mpc(x, y)
        external = external_bilinear_value(tent_transform, z)
        hermitian = hermitian_jensen_value(tent_transform, z)
        transformed = tent_external_tilt_fourier(x, y)
        # Exact Fourier/Wronskian normalization for Psi_y(t)=cosh(yt)nu_2(t).
        assert abs(transformed - 2 * external) < mp.mpf("1e-55")
        assert external < 0
        assert hermitian > 0


def test_theta_transverse_potential_has_unique_sampled_minimum_at_zero():
    with mp.workdps(50):
        v0 = theta_transverse_potential(0, n_terms=8, cutoff=4)
        assert abs(v0) < mp.mpf("1e-45")
        for y in (mp.mpf("0.1"), mp.mpf("0.25"), mp.mpf("0.49")):
            assert theta_transverse_potential(y, n_terms=8, cutoff=4) > 0


def test_nbody_real_free_energy_hessian_is_positive_definite_on_sample_grid():
    with mp.workdps(50):
        for alpha, beta in ((0, 0), (mp.mpf("0.1"), mp.mpf("0.05")), (mp.mpf("0.3"), mp.mpf("0.1"))):
            faa, fab, fbb, det = nbody_log_partition_hessian_real(
                alpha, beta, n_terms=8, cutoff=4
            )
            assert faa > 0
            assert fbb > 0
            assert det > 0
            assert faa * fbb - fab * fab > 0


def test_riemann_internal_and_external_complex_forms_are_not_identical():
    with mp.workdps(70):
        x = mp.mpf("14")
        y = mp.mpf("0.3")
        external = riemann_external_bilinear(x, y)
        hermitian = riemann_hermitian_jensen(x, y)
        assert abs(external - hermitian) > mp.mpf("1e-20") * max(abs(external), abs(hermitian))
        assert hermitian > 0


def test_riemann_external_sign_change_is_recorded_only_as_finite_diagnostic():
    # This is deliberately NOT promoted to a theorem about RH or about the
    # Dimitrov--Xu criterion. It records a stable high-precision conflict that
    # requires a separate source/convention audit.
    with mp.workdps(100):
        y = mp.mpf("0.499")
        e110 = riemann_external_bilinear(mp.mpf("110"), y)
        e111 = riemann_external_bilinear(mp.mpf("111"), y)
        h110 = riemann_hermitian_jensen(mp.mpf("110"), y)
        h111 = riemann_hermitian_jensen(mp.mpf("111"), y)
        assert e110 > 0
        assert e111 < 0
        assert h110 > 0
        assert h111 > 0
