import mpmath as mp

from secret_of_a_half.negative_inversion import (
    euler_half_turn_u,
    negative_inversion_u,
    riemann_reflection_u,
)
from secret_of_a_half.spinor_lift import (
    add_matrix,
    bloch_vector_from_u,
    dagger,
    determinant2,
    identity2,
    matrix_residual,
    pauli_fixed_pairs,
    pauli_spinor_lifts,
    pi_rotation_lifts,
    projective_action,
    projective_class_label,
    q8_elements,
    scale_matrix,
)


def _mclose(a, b, tol="1e-50") -> bool:
    return matrix_residual(a, b) < mp.mpf(tol)


def _close(a, b, tol="1e-50") -> bool:
    if a == mp.inf or b == mp.inf:
        return a == b
    return abs(a - b) < mp.mpf(tol)


def test_spinor_lifts_are_su2() -> None:
    mp.mp.dps = 70
    ident = identity2()
    for lift in pauli_spinor_lifts().values():
        assert abs(determinant2(lift) - 1) < mp.mpf("1e-60")
        assert _mclose(dagger(lift) * lift, ident)


def test_each_noncentral_lift_has_order_four() -> None:
    mp.mp.dps = 70
    ident = identity2()
    minus_ident = scale_matrix(-1, ident)
    for lift in pauli_spinor_lifts().values():
        assert _mclose(lift * lift, minus_ident)
        assert _mclose(lift * lift * lift * lift, ident)
        assert not _mclose(lift * lift, ident)


def test_quaternion_multiplication_and_anticommutation() -> None:
    mp.mp.dps = 70
    lifts = pauli_spinor_lifts()
    r, e, n = lifts["R"], lifts["E"], lifts["N"]
    assert _mclose(r * e, n)
    assert _mclose(e * r, scale_matrix(-1, n))
    assert _mclose(e * n, r)
    assert _mclose(n * e, scale_matrix(-1, r))
    assert _mclose(n * r, e)
    assert _mclose(r * n, scale_matrix(-1, e))
    assert _mclose(add_matrix(r * e, e * r), scale_matrix(0, identity2()))


def test_q8_is_closed_and_projectivizes_to_v4() -> None:
    mp.mp.dps = 70
    elements = q8_elements()
    values = list(elements.values())
    for a in values:
        for b in values:
            product = a * b
            assert any(_mclose(product, c) for c in values)
            assert projective_class_label(product) in {"I", "R", "E", "N"}

    assert projective_class_label(elements["+I"]) == "I"
    assert projective_class_label(elements["-I"]) == "I"
    assert projective_class_label(elements["+R"]) == "R"
    assert projective_class_label(elements["-R"]) == "R"
    assert projective_class_label(elements["+E"]) == "E"
    assert projective_class_label(elements["-E"]) == "E"
    assert projective_class_label(elements["+N"]) == "N"
    assert projective_class_label(elements["-N"]) == "N"


def test_projective_actions_match_g012_operators() -> None:
    mp.mp.dps = 70
    lifts = pauli_spinor_lifts()
    samples = [mp.mpc("0.7", "0.2"), mp.mpc("-0.3", "0.8"), mp.mpc("1.2", "-0.5")]
    for u in samples:
        assert _close(projective_action(lifts["R"], u), riemann_reflection_u(u))
        assert _close(projective_action(lifts["E"], u), euler_half_turn_u(u))
        assert _close(projective_action(lifts["N"], u), negative_inversion_u(u))


def test_central_minus_identity_is_projectively_invisible() -> None:
    mp.mp.dps = 70
    u = mp.mpc("0.47", "0.31")
    for lift in pauli_spinor_lifts().values():
        assert _close(projective_action(lift, u), projective_action(scale_matrix(-1, lift), u))


def test_pi_rotation_lifts_differ_only_by_central_minus_identity() -> None:
    mp.mp.dps = 70
    chosen = pauli_spinor_lifts()
    rotations = pi_rotation_lifts()
    for label in ["R", "E", "N"]:
        assert _mclose(rotations[label], scale_matrix(-1, chosen[label]))
        for u in [mp.mpc("0.4", "0.7"), mp.mpc("-1.2", "0.3")]:
            assert _close(projective_action(rotations[label], u), projective_action(chosen[label], u))


def test_pauli_fixed_pairs_are_projective_fixed_lines() -> None:
    mp.mp.dps = 70
    lifts = pauli_spinor_lifts()
    for label, pair in pauli_fixed_pairs().items():
        for u in pair:
            assert _close(projective_action(lifts[label], u), u)


def test_fixed_pairs_are_three_bloch_axes() -> None:
    mp.mp.dps = 70
    pairs = pauli_fixed_pairs()

    r_vectors = [bloch_vector_from_u(u) for u in pairs["R"]]
    assert any(all(abs(a - b) < mp.mpf("1e-50") for a, b in zip(v, (1, 0, 0))) for v in r_vectors)
    assert any(all(abs(a - b) < mp.mpf("1e-50") for a, b in zip(v, (-1, 0, 0))) for v in r_vectors)

    e_vectors = [bloch_vector_from_u(u) for u in pairs["E"]]
    assert any(all(abs(a - b) < mp.mpf("1e-50") for a, b in zip(v, (0, 0, 1))) for v in e_vectors)
    assert any(all(abs(a - b) < mp.mpf("1e-50") for a, b in zip(v, (0, 0, -1))) for v in e_vectors)

    n_vectors = [bloch_vector_from_u(u) for u in pairs["N"]]
    assert any(all(abs(a - b) < mp.mpf("1e-50") for a, b in zip(v, (0, 1, 0))) for v in n_vectors)
    assert any(all(abs(a - b) < mp.mpf("1e-50") for a, b in zip(v, (0, -1, 0))) for v in n_vectors)
