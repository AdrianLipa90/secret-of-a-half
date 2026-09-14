from __future__ import annotations

from secret_of_a_half.half_kernel_wronskian_completion import build_receipt


def test_wronskian_completion_decomposition_and_blockwise_no_go() -> None:
    receipt = build_receipt()
    assert receipt["status"] == "PASS"
    assert receipt["rh_claim"] is False
    assert receipt["checks"]["decomposition_residual_z0_small"] is True
    assert receipt["checks"]["decomposition_residual_z1_small"] is True
    assert receipt["checks"]["blockwise_same_sign_route_rejected"] is True
    assert receipt["open"]["third_order_G024_complete_monotonicity"] is True
    assert receipt["open"]["riemann_hypothesis"] is True
