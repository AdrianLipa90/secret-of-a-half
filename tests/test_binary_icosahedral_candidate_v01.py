import numpy as np
import pytest

from secret_of_a_half.binary_icosahedral_candidate_v01 import (
    BinaryIcosahedralCandidateError,
    antipodal_partner,
    candidate_status,
    carrier_quaternions,
    identity_index,
    inverse_index,
    multiply_indices,
    negative_identity_index,
    quaternion_multiply,
    rotation_matrix,
)


def test_candidate_is_active_working_and_not_physical_canon():
    s = candidate_status()
    assert s.status == "CANDIDATE"
    assert s.active_working_version
    assert not s.canonical
    assert s.physical_binding == "OPEN"
    assert s.group_order == 120
    assert s.antipodal_quotient_order == 60


def test_carrier_is_120_unit_quaternions_and_antipodal():
    q = carrier_quaternions()
    assert q.shape == (120, 4)
    assert np.allclose(np.linalg.norm(q, axis=1), 1.0, rtol=0.0, atol=4e-14)
    assert len({tuple(sorted((i, antipodal_partner(i)))) for i in range(120)}) == 60


def test_binary_icosahedral_carrier_is_closed_under_quaternion_multiplication():
    q = carrier_quaternions()
    max_error = 0.0
    for i in range(120):
        for j in range(120):
            k = multiply_indices(i, j)
            product = quaternion_multiply(q[i], q[j])
            max_error = max(max_error, float(np.linalg.norm(product - q[k])))
    assert max_error < 1e-12


def test_identity_inverse_and_central_minus_one():
    e = identity_index()
    minus = negative_identity_index()
    for i in range(120):
        inv = inverse_index(i)
        assert multiply_indices(e, i) == i
        assert multiply_indices(i, e) == i
        assert multiply_indices(i, inv) == e
        assert multiply_indices(inv, i) == e
        assert multiply_indices(minus, i) == antipodal_partner(i)
        assert multiply_indices(i, minus) == antipodal_partner(i)


def test_antipodal_pair_has_same_so3_rotation():
    q = carrier_quaternions()
    for i in range(120):
        j = antipodal_partner(i)
        assert np.allclose(rotation_matrix(q[i]), rotation_matrix(q[j]), rtol=0.0, atol=3e-14)


@pytest.mark.parametrize("bad", [-1, 120, True, 1.5])
def test_bad_indices_fail_closed(bad):
    with pytest.raises(BinaryIcosahedralCandidateError):
        antipodal_partner(bad)
