import mpmath as mp

from secret_of_a_half.g024_unified_closure import (
    dual_gram_radial_response,
    laguerre_resummed_radial_response,
    pole_free_dual_gram_diagonals,
    q_from_quotient_point,
    q_partition_from_quotient,
    quotient_point,
    quotient_strip_membership,
    radial_response_from_quotient,
)


def F_linear(w):
    return 1 + w


def test_q_quotient_roundtrip():
    mp.mp.dps = 60
    for x, q in [
        (mp.mpf("0"), mp.mpf("0.01")),
        (mp.mpf("0.7"), mp.mpf("0.09")),
        (mp.mpf("14.134725"), mp.mpf("0.24")),
    ]:
        w = quotient_point(x, q)
        assert mp.almosteq(q_from_quotient_point(w), q, rel_eps=mp.mpf("1e-55"))


def test_dual_gram_sum_is_radial_response():
    mp.mp.dps = 70
    x = mp.mpf("0.7")
    q = mp.mpf("0.09")
    lhs = dual_gram_radial_response(F_linear, x, q)
    rhs = radial_response_from_quotient(F_linear, x, q)
    assert mp.almosteq(lhs, rhs, rel_eps=mp.mpf("1e-60"), abs_eps=mp.mpf("1e-65"))
    assert mp.almosteq(lhs, mp.mpf("1.58"), rel_eps=mp.mpf("1e-60"))


def test_real_axis_continuous_gram_limit():
    mp.mp.dps = 60
    q = mp.mpf("0.16")
    k0, k1 = pole_free_dual_gram_diagonals(F_linear, 0, q)
    assert mp.almosteq(k0, 1, rel_eps=mp.mpf("1e-55"))
    assert mp.almosteq(k1, 1, rel_eps=mp.mpf("1e-55"))
    expected = F_linear(q) * 1
    assert mp.almosteq(k0 + q * k1, expected, rel_eps=mp.mpf("1e-55"))


def test_laguerre_resummation_for_one_minus_z_squared():
    mp.mp.dps = 60
    # f(z)=1-z^2 = F(-z^2) with F(w)=1+w.
    # Q_x(q)=1/2[(1-x^2)^2+2(1+x^2)q+q^2].
    # Therefore L0=(1-x^2)^2, L1=2(1+x^2), L2=1.
    x = mp.mpf("0.7")
    q = mp.mpf("0.09")
    L0 = (1 - x*x) ** 2
    L1 = 2 * (1 + x*x)
    L2 = mp.mpf("1")
    radial = laguerre_resummed_radial_response([L0, L1, L2], q)
    assert mp.almosteq(radial, 1 + x*x + q, rel_eps=mp.mpf("1e-55"))
    assert mp.almosteq(radial, radial_response_from_quotient(F_linear, x, q), rel_eps=mp.mpf("1e-55"))


def test_critical_strip_image_condition():
    mp.mp.dps = 60
    assert quotient_strip_membership(quotient_point(mp.mpf("3"), mp.mpf("0.24")))
    assert not quotient_strip_membership(quotient_point(mp.mpf("3"), mp.mpf("0.25")))
    assert not quotient_strip_membership(quotient_point(mp.mpf("3"), mp.mpf("0.3")))


def test_partition_from_quotient_is_half_modulus_square():
    mp.mp.dps = 60
    x = mp.mpf("0.7")
    q = mp.mpf("0.09")
    z = mp.mpc(x, mp.sqrt(q))
    lhs = q_partition_from_quotient(F_linear, x, q)
    rhs = mp.mpf("0.5") * abs(1 - z*z) ** 2
    assert mp.almosteq(lhs, rhs, rel_eps=mp.mpf("1e-55"), abs_eps=mp.mpf("1e-58"))
