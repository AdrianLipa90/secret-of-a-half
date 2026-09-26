"""Validated archimedean rank witness for the localized Weil first correction.

This module proves a rank-three witness in a prime-free localization window:
    a = 69/200 < (log 2)/2,
so exp(2a) < 2 and Suzuki's finite prime-power sum is empty.

The sample points are purely imaginary:
    z = i/20, i/4, 9i/20.

All transcendental evaluation is performed with mpmath.iv outward-rounded
interval arithmetic. The only non-elementary quantity that would normally
appear is digamma at rational arguments; it is evaluated instead by Gauss'
finite digamma formula using interval pi/log/sin/cos arithmetic.

No zeta zeros and no RH input are used.
"""
from __future__ import annotations

from fractions import Fraction
import mpmath as mp


iv = mp.iv
iv.dps = 80


A = Fraction(69, 200)
Y_POINTS = (Fraction(1, 20), Fraction(1, 4), Fraction(9, 20))


def _q(x: Fraction | int):
    f = Fraction(x)
    return iv.mpf(f.numerator) / iv.mpf(f.denominator)


def _gauss_digamma(x: Fraction):
    """Rigorous interval enclosure of psi(x) for positive rational x."""
    x = Fraction(x)
    if x <= 0:
        raise ValueError("Gauss digamma evaluator requires x>0")
    p, q = x.numerator, x.denominator
    xx = _q(x)
    out = (
        -iv.euler
        - iv.ln(iv.mpf(2 * q))
        - (iv.pi / 2) * (iv.cos(iv.pi * xx) / iv.sin(iv.pi * xx))
    )
    for n in range(1, (q - 1) // 2 + 1):
        angle = 2 * iv.pi * iv.mpf(p * n) / iv.mpf(q)
        s = iv.sin(iv.pi * iv.mpf(n) / iv.mpf(q))
        out += 2 * iv.cos(angle) * iv.ln(s)
    return out


def _phi(k: Fraction, T: Fraction):
    """Integral_0^T exp(k t) dt."""
    k = Fraction(k)
    if k == 0:
        return _q(T)
    kk = _q(k)
    TT = _q(T)
    return (iv.exp(kk * TT) - 1) / kk


def _atanh(x):
    return iv.ln((1 + x) / (1 - x)) / 2


def _finite_H(lam: Fraction, T: Fraction, terms: int = 60):
    """Validated enclosure of H(lam,T).

    H(lam,T) = integral_0^T
        (exp(-lam*t)-exp(-t))/(1-exp(-2*t)) dt,
    for 0 < lam < 1.

    The infinite integral is evaluated by Gauss digamma. The tail from T to
    infinity is summed for the requested number of geometric terms and the
    unsummed positive remainder is bounded by the first exponential series.
    """
    lam = Fraction(lam)
    if not (0 < lam < 1):
        raise ValueError("lam must lie in (0,1)")
    TT = _q(T)
    lam_iv = _q(lam)

    h_inf = (
        _gauss_digamma(Fraction(1, 2))
        - _gauss_digamma(lam / 2)
    ) / 2

    tail = iv.mpf(0)
    for k in range(terms):
        aa = lam_iv + 2 * k
        bb = iv.mpf(1 + 2 * k)
        tail += iv.exp(-aa * TT) / aa - iv.exp(-bb * TT) / bb

    aa = lam_iv + 2 * terms
    remainder_upper = (
        iv.exp(-aa * TT)
        / aa
        / (1 - iv.exp(-2 * TT))
    )

    return h_inf - tail - iv.mpf([0, remainder_upper.b])


def prime_free_cross_form(
    y: Fraction,
    v: Fraction,
    *,
    a: Fraction = A,
    tail_terms: int = 60,
):
    """Validated Q_W^a(e^(y x), e^(v x)) in the prime-free window."""
    a = Fraction(a)
    y = Fraction(y)
    v = Fraction(v)
    T = 2 * a

    # Prime-free condition: exp(2a)<2. It is enough to check 2a<log 2
    # with outward-rounded interval arithmetic.
    assert _q(T) < iv.ln(2)

    c = y + v
    c_iv = _q(c)
    exp_ca = iv.exp(_q(c * a))
    exp_minus_ca = 1 / exp_ca
    f0 = (exp_ca - exp_minus_ca) / c_iv

    half = Fraction(1, 2)

    elementary = exp_ca / c_iv * (
        _phi(half - v, T)
        + _phi(-(v + half), T)
        + _phi(-(y + half), T)
        + _phi(half - y, T)
    )
    elementary -= exp_minus_ca / c_iv * (
        _phi(y + half, T)
        + _phi(y - half, T)
        + _phi(v - half, T)
        + _phi(v + half, T)
    )

    core = exp_ca / c_iv * _finite_H(v + half, T, tail_terms)
    core += exp_ca / c_iv * _finite_H(y + half, T, tail_terms)
    core -= exp_minus_ca / c_iv * _finite_H(half - y, T, tail_terms)
    core -= exp_minus_ca / c_iv * _finite_H(half - v, T, tail_terms)

    constant = (iv.ln(4 * iv.pi) + iv.euler) * f0
    tail = 2 * f0 * _atanh(iv.exp(-_q(T)))

    return elementary - constant - core + tail


def displacement_matrix(
    *,
    a: Fraction = A,
    points: tuple[Fraction, ...] = Y_POINTS,
    tail_terms: int = 60,
):
    """First-correction displacement matrix for z_j=i*y_j.

    For z=i y and w=i v,
        2 i (conj(w)-z) = 2(y+v).
    """
    n = len(points)
    out = [[None for _ in range(n)] for _ in range(n)]
    for j, y in enumerate(points):
        for k, v in enumerate(points):
            qwv = prime_free_cross_form(
                y, v, a=a, tail_terms=tail_terms
            )
            out[j][k] = 2 * _q(y + v) * qwv
    return out


def determinant_3x3(M):
    if len(M) != 3 or any(len(row) != 3 for row in M):
        raise ValueError("3x3 matrix required")
    return (
        M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
        - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
        + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0])
    )


def certified_rank_witness():
    M = displacement_matrix()
    det = determinant_3x3(M)
    if not (det > 0):
        raise AssertionError(
            f"determinant interval does not exclude zero: {det}"
        )
    return {
        "a": "69/200",
        "points": ["i/20", "i/4", "9i/20"],
        "prime_free": True,
        "determinant_interval": iv.nstr(det, 60),
        "rank_lower_bound": 3,
        "tail_terms": 60,
        "interval_backend": "mpmath.iv outward-rounded mpi arithmetic",
    }
