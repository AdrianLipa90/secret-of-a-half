from fractions import Fraction


def test_soh_g004_conservative_variance_bound_is_below_two():
    n2_bound = Fraction(14112, 8000)
    n3_bound = Fraction(98 * 81 * 64, 20**8)
    tail_ratio = Fraction(12, 20**7)
    tail_bound = n3_bound / (1 - tail_ratio)
    variance_bound = n2_bound + tail_bound
    assert variance_bound < 2


def test_soh_g004_global_compactified_margin_is_strictly_negative():
    channel_margin = Fraction(-7, 1)
    conservative_variance_ceiling = Fraction(2, 1)
    assert channel_margin + conservative_variance_ceiling < 0


def test_soh_g004_elementary_e3_lower_bound_uses_finite_series():
    # e^3 > sum_{k=0}^8 3^k/k! > 20.
    partial = sum(Fraction(3**k, 1) / _factorial(k) for k in range(9))
    assert partial > 20


def _factorial(n: int) -> int:
    value = 1
    for k in range(2, n + 1):
        value *= k
    return value
