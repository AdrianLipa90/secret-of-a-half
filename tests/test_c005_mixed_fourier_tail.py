from __future__ import annotations

import math

import pytest

from secret_of_a_half.c005_mixed_fourier_tail import (
    KernelRegularityEnvelope,
    common_cutoff,
    cutoff_for_mixed_norm,
    mixed_fourier_tail_certificate,
    mixed_fourier_tail_norm_sq_upper,
    mixed_fourier_tail_norm_upper,
    mixed_tail_gate_map,
    screw_kernel_regularity_envelope_from_even_g,
    screw_mixed_tail_norm_upper_from_even_g,
)


def test_mixed_tail_bound_scales_as_inverse_sqrt_N() -> None:
    env = KernelRegularityEnvelope(a=2.0, boundary_jump_l2_sq=3.0, du_l2_sq=5.0)
    b10 = mixed_fourier_tail_norm_upper(env, 10)
    b40 = mixed_fourier_tail_norm_upper(env, 40)
    assert b40 == pytest.approx(b10 / 2.0)


def test_norm_square_formula() -> None:
    env = KernelRegularityEnvelope(a=1.5, boundary_jump_l2_sq=2.0, du_l2_sq=4.0)
    n = 7
    expected = (
        4.0 * env.a**2 / (math.pi**2 * n)
        * (env.boundary_jump_l2_sq / (2.0 * env.a) + env.du_l2_sq)
    )
    assert mixed_fourier_tail_norm_sq_upper(env, n) == pytest.approx(expected)
    assert mixed_fourier_tail_norm_upper(env, n) ** 2 == pytest.approx(expected)


def test_cutoff_for_mixed_norm_is_fail_closed_and_minimal_up_to_rounding() -> None:
    env = KernelRegularityEnvelope(a=1.0, boundary_jump_l2_sq=1.0, du_l2_sq=2.0)
    target = 0.1
    cert = cutoff_for_mixed_norm(env, target)
    assert cert.norm_upper <= target
    if cert.cutoff_N > 1:
        previous = mixed_fourier_tail_norm_upper(env, cert.cutoff_N - 1)
        assert previous > target


def test_certificate_reports_regularity_energy() -> None:
    env = KernelRegularityEnvelope(a=3.0, boundary_jump_l2_sq=6.0, du_l2_sq=8.0)
    cert = mixed_fourier_tail_certificate(env, 20)
    assert cert.regularity_energy == pytest.approx(9.0)
    assert cert.finite


def test_common_cutoff_takes_stricter_gate() -> None:
    assert common_cutoff(10, 25) == 25
    assert common_cutoff(30, 12) == 30


def test_gate_map_keeps_actual_kernel_envelopes_open() -> None:
    gates = mixed_tail_gate_map()
    assert gates["proof_of_rh"] is False
    assert (
        "rigorous boundary-jump L2 envelope for the actual zeta screw kernel"
        in gates["open"]
    )


def test_invalid_inputs_fail_closed() -> None:
    with pytest.raises(ValueError):
        mixed_fourier_tail_norm_upper(
            KernelRegularityEnvelope(a=0.0, boundary_jump_l2_sq=1.0, du_l2_sq=1.0),
            2,
        )
    with pytest.raises(ValueError):
        cutoff_for_mixed_norm(
            KernelRegularityEnvelope(a=1.0, boundary_jump_l2_sq=-1.0, du_l2_sq=1.0),
            0.1,
        )
    with pytest.raises(ValueError):
        common_cutoff(0, 1)


def test_screw_kernel_reduction_to_one_dimensional_norms() -> None:
    a = 1.5
    g0 = 2.0
    g1 = 3.0
    env = screw_kernel_regularity_envelope_from_even_g(a, g0, g1)
    assert env.boundary_jump_l2_sq == pytest.approx(4.0 * g0)
    assert env.du_l2_sq == pytest.approx(16.0 * a * g1)

    direct = screw_mixed_tail_norm_upper_from_even_g(a, 20, g0, g1)
    generic = mixed_fourier_tail_norm_upper(env, 20)
    assert direct == pytest.approx(generic)


def test_invalid_screw_norm_inputs_fail_closed() -> None:
    with pytest.raises(ValueError):
        screw_kernel_regularity_envelope_from_even_g(1.0, -1.0, 1.0)
