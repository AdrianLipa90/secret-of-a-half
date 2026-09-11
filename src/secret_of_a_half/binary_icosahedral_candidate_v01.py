from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
import itertools
import math

import numpy as np

SCHEMA = "SOH_600CELL_BINARY_ICOSAHEDRAL_CANDIDATE_V0_1"
STATUS = "CANDIDATE"
ACTIVE_WORKING_VERSION = True
CANONICAL = False
PHYSICAL_BINDING = "OPEN"
PHI = (1.0 + math.sqrt(5.0)) / 2.0
ORDER_2I = 120
QUOTIENT_ORDER = 60


class BinaryIcosahedralCandidateError(ValueError):
    pass


@dataclass(frozen=True)
class BinaryIcosahedralStatus:
    schema: str = SCHEMA
    status: str = STATUS
    active_working_version: bool = ACTIVE_WORKING_VERSION
    canonical: bool = CANONICAL
    physical_binding: str = PHYSICAL_BINDING
    group_order: int = ORDER_2I
    antipodal_quotient_order: int = QUOTIENT_ORDER


def candidate_status() -> BinaryIcosahedralStatus:
    return BinaryIcosahedralStatus()


def _parity(p: tuple[int, ...]) -> int:
    return sum(
        p[i] > p[j]
        for i in range(len(p))
        for j in range(i + 1, len(p))
    ) % 2


@lru_cache(maxsize=1)
def _carrier_cached() -> np.ndarray:
    rows: list[tuple[float, float, float, float]] = []
    for axis in range(4):
        for sign in (-1.0, 1.0):
            v = [0.0] * 4
            v[axis] = sign
            rows.append(tuple(v))
    rows.extend(itertools.product((-0.5, 0.5), repeat=4))

    base = (0.0, 0.5, PHI / 2.0, 1.0 / (2.0 * PHI))
    for p in (p for p in itertools.permutations(range(4)) if _parity(p) == 0):
        q = [base[p[i]] for i in range(4)]
        nz = [i for i, value in enumerate(q) if value != 0.0]
        for signs in itertools.product((-1.0, 1.0), repeat=3):
            v = q.copy()
            for i, sign in zip(nz, signs):
                v[i] *= sign
            rows.append(tuple(v))

    out = np.unique(np.round(np.asarray(rows, dtype=np.float64), 14), axis=0)
    if out.shape != (ORDER_2I, 4):
        raise AssertionError(f"expected 120 unit quaternions, got {out.shape}")
    if not np.allclose(np.linalg.norm(out, axis=1), 1.0, rtol=0.0, atol=4e-14):
        raise AssertionError("binary icosahedral carrier left the unit 3-sphere")
    out.setflags(write=False)
    return out


def carrier_quaternions() -> np.ndarray:
    return _carrier_cached().copy()


def quaternion_multiply(a, b) -> np.ndarray:
    a = np.asarray(a, dtype=np.float64)
    b = np.asarray(b, dtype=np.float64)
    if a.shape != (4,) or b.shape != (4,) or not np.isfinite(a).all() or not np.isfinite(b).all():
        raise BinaryIcosahedralCandidateError("quaternions must be finite 4-vectors")
    w, x, y, z = a
    W, X, Y, Z = b
    return np.asarray(
        (
            w * W - x * X - y * Y - z * Z,
            w * X + x * W + y * Z - z * Y,
            w * Y - x * Z + y * W + z * X,
            w * Z + x * Y - y * X + z * W,
        ),
        dtype=np.float64,
    )


def nearest_carrier_index(q, *, tolerance: float = 2e-12) -> int:
    q = np.asarray(q, dtype=np.float64)
    if q.shape != (4,) or not np.isfinite(q).all():
        raise BinaryIcosahedralCandidateError("q must be a finite quaternion 4-vector")
    carrier = _carrier_cached()
    i = int(np.argmax(carrier @ q))
    if float(np.linalg.norm(carrier[i] - q)) > tolerance:
        raise BinaryIcosahedralCandidateError("quaternion is outside the verified 2I carrier")
    return i


def multiply_indices(left: int, right: int) -> int:
    carrier = _carrier_cached()
    if (
        isinstance(left, bool)
        or not isinstance(left, int)
        or isinstance(right, bool)
        or not isinstance(right, int)
        or not 0 <= left < ORDER_2I
        or not 0 <= right < ORDER_2I
    ):
        raise BinaryIcosahedralCandidateError("indices must be integers in [0,119]")
    return nearest_carrier_index(quaternion_multiply(carrier[left], carrier[right]))


def identity_index() -> int:
    return nearest_carrier_index((1.0, 0.0, 0.0, 0.0))


def negative_identity_index() -> int:
    return nearest_carrier_index((-1.0, 0.0, 0.0, 0.0))


def antipodal_partner(index: int) -> int:
    carrier = _carrier_cached()
    if isinstance(index, bool) or not isinstance(index, int) or not 0 <= index < ORDER_2I:
        raise BinaryIcosahedralCandidateError("index must be an integer in [0,119]")
    return nearest_carrier_index(-carrier[index])


def inverse_index(index: int) -> int:
    carrier = _carrier_cached()
    if isinstance(index, bool) or not isinstance(index, int) or not 0 <= index < ORDER_2I:
        raise BinaryIcosahedralCandidateError("index must be an integer in [0,119]")
    q = carrier[index]
    conjugate = np.asarray((q[0], -q[1], -q[2], -q[3]))
    return nearest_carrier_index(conjugate)


def rotation_matrix(q) -> np.ndarray:
    q = np.asarray(q, dtype=np.float64)
    if q.shape != (4,) or not np.isfinite(q).all():
        raise BinaryIcosahedralCandidateError("q must be a finite quaternion 4-vector")
    n = float(np.linalg.norm(q))
    if not math.isclose(n, 1.0, rel_tol=0.0, abs_tol=2e-12):
        raise BinaryIcosahedralCandidateError("rotation quaternion must be unit norm")
    w, x, y, z = q
    return np.asarray(
        (
            (1 - 2 * (y * y + z * z), 2 * (x * y - z * w), 2 * (x * z + y * w)),
            (2 * (x * y + z * w), 1 - 2 * (x * x + z * z), 2 * (y * z - x * w)),
            (2 * (x * z - y * w), 2 * (y * z + x * w), 1 - 2 * (x * x + y * y)),
        ),
        dtype=np.float64,
    )
