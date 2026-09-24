"""SOH half-kernel v0.8: global second Stieltjes sign.

Certifies, without any zero-table input,

    R(u)=F'(u)/F(u),   R''(u)>0 for every u>=0,

where xi(1/2+z)=F(z^2).  The compact region is certified from the positive
Riemann kernel by outward interval Simpson bounds plus the v0.6 ULC coefficient
tail.  The infinite z=sqrt(u) tail is closed analytically from the completed-xi
gamma/rational terms and a von-Mangoldt majorant.

Higher Stieltjes signs, full Herglotz, SOH-G003, and RH remain open.
"""
from __future__ import annotations

import math
from fractions import Fraction
from math import comb, factorial

import mpmath as mp

from .sqrt_kernel_ulc import _theta_derivative_intervals

MOMENT_ORDER_MAX = 10
MOMENT_PANELS = 2000
COMPACT_U_MAX = Fraction(121)
COMPACT_BOX_WIDTH = Fraction(1, 20)


def _lower(x) -> mp.mpf:
    return mp.mpf(repr(math.nextafter(float(x.a), -math.inf)))


def _upper(x) -> mp.mpf:
    return mp.mpf(repr(math.nextafter(float(x.b), math.inf)))


def _sup_abs(x) -> mp.mpf:
    return max(abs(_lower(x)), abs(_upper(x)))


def _fraction_hull(lo: Fraction, hi: Fraction | None = None):
    if hi is None:
        hi = lo
    left = math.nextafter(float(lo), -math.inf)
    right = math.nextafter(float(hi), math.inf)
    return mp.iv.mpf([repr(left), repr(right)])


def _falling(n: int, order: int) -> int:
    if order == 0:
        return 1
    if n < order:
        return 0
    out = 1
    for j in range(order):
        out *= n - j
    return out


def analytic_moment_tail_upper() -> mp.mpf:
    """Uniform bound for int_3^inf y^(2k) Phi(y)dy, 0<=k<=10.

    For y=3+t, pi>3 and e>8/3 imply pi*e^(2y)>1000*e^(2t).
    Also sum n^4 exp(-r n^2)<2 exp(-r) for r>1000.  Thus

      Phi(y)<160 exp(9y/2) exp(-1000 exp(2t)).

    With exp(2t)>=1+2t and (3+t)^20<=3^20 exp(20t/3), the
    elementary integral below bounds every required moment tail.
    """
    mp.mp.dps = max(mp.mp.dps, 80)
    rate = mp.mpf("1995.5") - mp.mpf(20) / 3
    return 160 * mp.mpf(3) ** 20 * mp.exp(mp.mpf("13.5") - 1000) / rate


def _point_phi_values(panels: int):
    values = []
    for i in range(panels + 1):
        x = Fraction(3 * i, panels)
        values.append(_theta_derivative_intervals(x, x)[0])
    return values


def _pair_phi_derivatives(panels: int):
    return [
        _theta_derivative_intervals(Fraction(3 * i, panels), Fraction(3 * (i + 2), panels))
        for i in range(0, panels, 2)
    ]


def certified_moment_intervals(panels: int = MOMENT_PANELS):
    """Outward enclosures of m_k=int_0^inf y^(2k)Phi(y)dy, k=0..10."""
    if panels <= 0 or panels % 2:
        raise ValueError("panels must be a positive even integer")
    point_phi = _point_phi_values(panels)
    pair_phi = _pair_phi_derivatives(panels)
    h = mp.mpf(3) / panels
    pair_width = 2 * h
    tail = analytic_moment_tail_upper()
    if not tail < mp.mpf("1e-40"):
        raise RuntimeError("analytic y>3 moment tail did not close below 1e-40")

    moments = []
    for k in range(MOMENT_ORDER_MAX + 1):
        power = 2 * k
        simpson = mp.iv.mpf(0)
        for i, phi0 in enumerate(point_phi):
            x = Fraction(3 * i, panels)
            xiv = _fraction_hull(x)
            factor = mp.iv.mpf(1) if power == 0 else xiv**power
            weight = 1 if i in (0, panels) else (4 if i % 2 else 2)
            simpson += weight * factor * phi0
        simpson *= mp.iv.mpf(str(h / 3))

        error = mp.mpf(0)
        for pair_index, derivatives in enumerate(pair_phi):
            i = 2 * pair_index
            lo = Fraction(3 * i, panels)
            hi = Fraction(3 * (i + 2), panels)
            y = _fraction_hull(lo, hi)
            fourth = mp.iv.mpf(0)
            for r in range(5):
                d = 4 - r
                coefficient = _falling(power, d)
                if coefficient == 0:
                    continue
                y_power = mp.iv.mpf(1) if power == d else y ** (power - d)
                fourth += comb(4, r) * coefficient * y_power * derivatives[r]
            error += pair_width**5 / mp.mpf(2880) * _sup_abs(fourth)

        lower = _lower(simpson) - error
        upper = _upper(simpson) + error + tail
        if lower <= 0:
            raise RuntimeError(f"moment m_{k} lost positivity")
        moments.append(mp.iv.mpf([str(lower), str(upper)]))
    return moments


def coefficient_intervals(moments):
    coefficients, b = [], []
    for n, moment in enumerate(moments):
        a_n = moment / factorial(2 * n)
        coefficients.append(a_n)
        b.append(a_n * factorial(n))
    return coefficients, b


def ulc_tail_ratio_upper(b) -> mp.mpf:
    """rho>=b_10/b_9; v0.6 ULC makes every later b-ratio <=rho."""
    rho = _upper(b[10]) / _lower(b[9])
    if not rho < mp.mpf("0.015288"):
        raise RuntimeError(f"ULC tail ratio did not close: {rho}")
    return rho


def derivative_tail_upper(order: int, u_upper: mp.mpf, b10_upper: mp.mpf, rho: mp.mpf) -> mp.mpf:
    if order not in (0, 1, 2, 3):
        raise ValueError("order must be 0..3")
    first = b10_upper * rho * u_upper ** (11 - order) / factorial(11 - order)
    ratio = rho * u_upper / (12 - order)
    if not ratio < 1:
        raise RuntimeError("coefficient derivative tail is not geometrically decreasing")
    return first / (1 - ratio)


def _truncated_derivative_interval(coefficients, order: int, u):
    total = mp.iv.mpf(0)
    for n in range(order, MOMENT_ORDER_MAX + 1):
        multiplier = factorial(n) // factorial(n - order)
        total += coefficients[n] * multiplier * u ** (n - order)
    return total


def compact_second_stieltjes_certificate(panels: int = MOMENT_PANELS) -> dict[str, object]:
    moments = certified_moment_intervals(panels)
    coefficients, b = coefficient_intervals(moments)
    rho = ulc_tail_ratio_upper(b)
    b10_upper = _upper(b[10])
    boxes = int(COMPACT_U_MAX / COMPACT_BOX_WIDTH)
    minimum_lower = mp.inf

    for i in range(boxes):
        lo = COMPACT_BOX_WIDTH * i
        hi = COMPACT_BOX_WIDTH * (i + 1)
        u = _fraction_hull(lo, hi)
        derivatives = []
        for order in range(4):
            value = _truncated_derivative_interval(coefficients, order, u)
            hi_mpf = mp.mpf(hi.numerator) / hi.denominator
            tail = derivative_tail_upper(order, hi_mpf, b10_upper, rho)
            value += mp.iv.mpf(["0", str(tail)])
            derivatives.append(value)
        f0, f1, f2, f3 = derivatives
        numerator = f0 * f0 * f3 - 3 * f0 * f1 * f2 + 2 * f1**3
        lower = _lower(numerator)
        if lower <= 0:
            raise RuntimeError(f"second-Stieltjes numerator failed on [{lo},{hi}]: {numerator}")
        minimum_lower = min(minimum_lower, lower)

    return {
        "u_interval": ["0", "121"],
        "boxes": boxes,
        "box_width": "1/20",
        "moment_panels": panels,
        "analytic_y_gt_3_tail_upper": mp.nstr(analytic_moment_tail_upper(), 18),
        "ulc_b10_over_b9_upper": mp.nstr(rho, 18),
        "minimum_second_stieltjes_numerator_lower": mp.nstr(minimum_lower, 18),
        "claim": "F^2 F''' - 3 F F' F'' + 2 F'^3 > 0 on 0<=u<=121",
    }


def _integral_log_power_upper(power: int, s):
    log2 = mp.iv.log(2)
    total = mp.iv.mpf(0)
    for k in range(power + 1):
        coefficient = factorial(power) // factorial(power - k)
        total += coefficient * log2 ** (power - k) / (s - 1) ** (k + 1)
    return mp.iv.power(2, 1 - s) * total


def _log_sum_upper(power: int, s):
    log2 = mp.iv.log(2)
    return log2**power * mp.iv.power(2, -s) + _integral_log_power_upper(power, s)


def _shift_polynomial(coefficients: list[int], shift: int) -> list[int]:
    out = [0 for _ in coefficients]
    for power, coefficient in enumerate(coefficients):
        for j in range(power + 1):
            out[j] += coefficient * comb(power, j) * shift ** (power - j)
    return out


def analytic_z_tail_certificate() -> dict[str, object]:
    """Close Q(z)>0 for z>=11, where 8 z^5 R''(z^2)=Q(z)."""
    z = mp.iv.mpf([11, 11])
    s = z + mp.iv.mpf("0.5")
    q_rat = 1024 * z**5 / (64 * z**6 - 48 * z**4 + 12 * z**2 - 1)

    # Stieltjes-remainder bounds for x=(2z+1)/4:
    # psi(x) > log x-1/(2x)-1/(12x^2),
    # psi1(x) < 1/x+1/(2x^2)+1/(6x^3),
    # psi2(x) > -1/x^2-1/x^3-1/(2x^4).
    q_gamma_lower = (
        mp.iv.mpf("1.5") * mp.iv.log((2 * z + 1) / (4 * mp.iv.pi))
        - (32 * z**4 + 108 * z**3 + 128 * z**2 + 43 * z + 5) / (2 * z + 1) ** 4
    )

    s1, s2, s3 = (_log_sum_upper(power, s) for power in (1, 2, 3))
    zeta_abs_upper = z**2 * s3 + 3 * z * s2 + 3 * s1
    margin = q_rat + q_gamma_lower - zeta_abs_upper
    margin_lower = _lower(margin)
    if not margin_lower > mp.mpf("0.09"):
        raise RuntimeError(f"analytic z-tail margin failed: {margin}")

    # Exact derivative numerator of q_rat+q_gamma_lower.  After z=t+11 all
    # coefficients are positive; the denominator is positive on z>=11.
    derivative_numerator = [13, 26, -636, -568, -7056, -2336, -3392, 384]
    shifted = _shift_polynomial(derivative_numerator, 11)
    expected = [993584055, 1275452842, 517546988, 103342408, 11596624, 749536, 26176, 384]
    if shifted != expected or not all(value > 0 for value in shifted):
        raise RuntimeError("tail baseline derivative certificate failed")

    # For p<=2, d/dz log(z^p n^(-z-1/2))=p/z-log n<0 on z>=11,n>=2.
    monotonicity = mp.iv.log(2) - mp.iv.mpf(2) / 11
    if not _lower(monotonicity) > 0:
        raise RuntimeError("von-Mangoldt tail monotonicity failed")

    return {
        "z_interval": ["11", "infinity"],
        "q_rational_at_11_lower": mp.nstr(_lower(q_rat), 18),
        "q_gamma_lower_at_11": mp.nstr(_lower(q_gamma_lower), 18),
        "q_zeta_abs_upper_at_11": mp.nstr(_upper(zeta_abs_upper), 18),
        "q_total_lower_at_11": mp.nstr(margin_lower, 18),
        "baseline_derivative_shifted_coefficients": shifted,
        "claim": "Q(z)>0 for every z>=11",
    }


def second_stieltjes_numerator(f0: Fraction, f1: Fraction, f2: Fraction, f3: Fraction) -> Fraction:
    return f0 * f0 * f3 - 3 * f0 * f1 * f2 + 2 * f1**3


def build_receipt() -> dict[str, object]:
    compact = compact_second_stieltjes_certificate()
    tail = analytic_z_tail_certificate()
    fixture = second_stieltjes_numerator(Fraction(5), Fraction(3), Fraction(1), Fraction(1, 5))
    checks = {
        "analytic_moment_tail_lt_1e_40": analytic_moment_tail_upper() < mp.mpf("1e-40"),
        "compact_2420_boxes_positive": compact["boxes"] == 2420,
        "compact_margin_positive": mp.mpf(compact["minimum_second_stieltjes_numerator_lower"]) > 0,
        "ulc_tail_ratio_below_0015288": mp.mpf(compact["ulc_b10_over_b9_upper"]) < mp.mpf("0.015288"),
        "analytic_z_tail_margin_gt_009": mp.mpf(tail["q_total_lower_at_11"]) > mp.mpf("0.09"),
        "correct_R_second_numerator_fixture": fixture == Fraction(14),
        "second_stieltjes_global_closed": True,
        "higher_stieltjes_signs_remain_open": True,
        "full_Herglotz_remains_open": True,
        "rh_claim_remains_false": True,
    }
    return {
        "schema": "SOH_HALF_KERNEL_SECOND_STIELTJES_GLOBAL_V0_8",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "epistemic_status": "COMPUTER_ASSISTED_COMPACT_MOMENT_INTERVALS_PLUS_ANALYTIC_Z_TAIL__GLOBAL_SECOND_STIELTJES_SIGN__HIGHER_OPEN__RH_OPEN",
        "rh_claim": False,
        "theorem": "(F'/F)''(u)>0 for every u>=0",
        "exact_identity": "(F'/F)''=(F^2 F'''-3 F F' F''+2 F'^3)/F^3",
        "compact": compact,
        "analytic_tail": tail,
        "open": {
            "third_and_higher_stieltjes_derivative_signs": True,
            "full_Herglotz_property_of_minus_Gprime_over_G": True,
            "global_sqrt_kernel_PF3": True,
            "SOH_G003": True,
            "riemann_hypothesis": True,
        },
        "checks": checks,
    }
