from __future__ import annotations

import mpmath as mp

from secret_of_a_half.localized_weil_fourier_matrix import (
    hermitian_residual,
    localized_fourier_matrix,
    low_high_blocks,
    parity_residual,
)


mp.mp.dps=60


def test_prime_free_n1_matrix_is_hermitian_and_parity_symmetric():
    modes,M=localized_fourier_matrix("0.345",1,near_zero_eps="1e-8")
    assert hermitian_residual(M)<mp.mpf("1e-40")
    assert parity_residual(modes,M)<mp.mpf("1e-40")


def test_low_high_api_dimensions():
    out=low_high_blocks("0.345",1,2,near_zero_eps="1e-8")
    assert out["A_LL"].rows==3
    assert out["A_LL"].cols==3
    assert out["B"].rows==3
    assert out["B"].cols==2
    assert out["A_HH"].rows==2
    assert out["A_HH"].cols==2
