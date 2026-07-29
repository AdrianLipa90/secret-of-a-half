import math

from secret_of_a_half.core import binary_entropy, complementary_amplitude, involution


def test_entropy_at_half_is_ln2() -> None:
    assert math.isclose(binary_entropy(0.5), math.log(2.0), rel_tol=0.0, abs_tol=1e-14)


def test_exact_cancellation_at_half_and_pi() -> None:
    assert abs(complementary_amplitude(0.5, math.pi)) < 1e-14


def test_involution_fixes_critical_line() -> None:
    s = 0.5 + 17.0j
    assert involution(s) == s
