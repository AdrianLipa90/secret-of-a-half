from __future__ import annotations
import cmath
import math


def T(x: float) -> float:
    return 2.0 * x + 1.0


def iterate_closed(x: float, n: int) -> float:
    if n < 0:
        raise ValueError("n must be non-negative")
    return (2.0 ** n) * x + (2.0 ** n - 1.0)


def iterate_direct(x: float, n: int) -> float:
    y = float(x)
    for _ in range(n):
        y = T(y)
    return y


def plus_half(n: int) -> float:
    if n < 1:
        raise ValueError("n must be >=1")
    return 3.0 * (2.0 ** (n - 1)) - 1.0


def minus_half(n: int) -> float:
    if n < 1:
        raise ValueError("n must be >=1")
    return 2.0 ** (n - 1) - 1.0


def moire_identity(phi1: float, phi2: float) -> tuple[complex, complex]:
    direct = cmath.exp(1j * phi1) + cmath.exp(1j * phi2)
    factored = 2.0 * cmath.exp(0.5j * (phi1 + phi2)) * math.cos(0.5 * (phi1 - phi2))
    return direct, factored


def validate() -> dict:
    checks = {}
    for x in (-0.5, 0.5, 1.25, -3.0):
        for n in range(8):
            checks[f"closed_{x}_{n}"] = abs(iterate_closed(x, n) - iterate_direct(x, n)) < 1e-12
    checks["minus_half_zero"] = T(-0.5) == 0.0
    checks["plus_half_two"] = T(0.5) == 2.0
    checks["positive_initial"] = [int(plus_half(n)) for n in range(1, 7)] == [2,5,11,23,47,95]
    checks["negative_initial"] = [int(minus_half(n)) for n in range(1, 7)] == [0,1,3,7,15,31]
    d, f = moire_identity(0.17, 2.01)
    checks["moire_identity"] = abs(d-f) < 1e-12
    checks["antiphase_null"] = abs(cmath.exp(0.37j)+cmath.exp(1j*(0.37+math.pi))) < 1e-12
    return {"status":"PASS" if all(checks.values()) else "FAIL", "checks":checks}

if __name__ == "__main__":
    import json
    print(json.dumps(validate(), indent=2, sort_keys=True))
