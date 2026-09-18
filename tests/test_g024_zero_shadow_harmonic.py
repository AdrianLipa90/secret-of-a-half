import mpmath as mp

from secret_of_a_half.g024_zero_shadow_harmonic import (
    conjugate_pair_shadow,
    harmonic_lift_residual,
    normalized_radial_gate,
    pair_control_entire,
    quartet_control_entire,
    quartet_shadow,
    real_pair_shadow,
)


def test_conjugate_pair_exact_shadow_identity():
    mp.mp.dps = 60
    u, v = mp.mpf("3.2"), mp.mpf("0.3")
    f = pair_control_entire(u, v)
    for x, q in [
        (mp.mpf("3.2"), mp.mpf("0.01")),
        (mp.mpf("3.2"), mp.mpf("0.04")),
        (mp.mpf("2.9"), mp.mpf("0.0225")),
        (mp.mpf("3.7"), mp.mpf("0.16")),
    ]:
        lhs = normalized_radial_gate(f, x, q)
        rhs = conjugate_pair_shadow(x, q, u, v)
        assert mp.almosteq(lhs, rhs, rel_eps=mp.mpf("1e-52"), abs_eps=mp.mpf("1e-55"))


def test_even_quartet_exact_shadow_identity():
    mp.mp.dps = 60
    u, v = mp.mpf("3.2"), mp.mpf("0.3")
    f = quartet_control_entire(u, v)
    x, q = mp.mpf("3.05"), mp.mpf("0.025")
    lhs = normalized_radial_gate(f, x, q)
    rhs = quartet_shadow(x, q, u, v)
    assert mp.almosteq(lhs, rhs, rel_eps=mp.mpf("1e-52"), abs_eps=mp.mpf("1e-55"))


def test_shadow_sign_is_exact_disk_geometry():
    mp.mp.dps = 60
    u, v = mp.mpf("4"), mp.mpf("0.3")
    # Inside: (x-u)^2+q < v^2.
    assert conjugate_pair_shadow(u, mp.mpf("0.04"), u, v) < 0
    # Outside.
    assert conjugate_pair_shadow(u, mp.mpf("0.16"), u, v) > 0
    # On the sign circle but away from the singular zero itself.
    x = u + mp.mpf("0.2")
    q = v*v - mp.mpf("0.2")**2
    assert abs(conjugate_pair_shadow(x, q, u, v)) < mp.mpf("1e-55")


def test_real_pair_is_strictly_positive():
    mp.mp.dps = 50
    for x, q in [(0, mp.mpf("0.01")), (10, mp.mpf("0.2")), (-3, mp.mpf("0.24"))]:
        assert real_pair_shadow(x, q, mp.mpf("5")) > 0


def test_outer_boundary_positive_for_any_quartet_inside_critical_strip():
    mp.mp.dps = 50
    q = mp.mpf("0.25")
    for u, v, x in [
        ("14", "0.1", "14"),
        ("25", "0.49", "25"),
        ("9", "0.25", "8.8"),
    ]:
        assert quartet_shadow(mp.mpf(x), q, mp.mpf(u), mp.mpf(v)) > 0


def test_harmonic_lift_pde_for_pair_control():
    mp.mp.dps = 50
    f = pair_control_entire(mp.mpf("3.2"), mp.mpf("0.3"))
    residual = harmonic_lift_residual(f, mp.mpf("2.7"), mp.mpf("0.04"))
    assert abs(residual) < mp.mpf("1e-40")
