from __future__ import annotations

from secret_of_a_half.halfplane_weyl_bridge import build_receipt


def test_halfplane_weyl_bridge_receipt() -> None:
    receipt = build_receipt()
    assert receipt["status"] == "PASS"
    assert receipt["rh_claim"] is False
    assert receipt["checks"]["sin_cos_quotient_identity"] is True
    assert receipt["checks"]["disk_cayley_parent_identity"] is True
    assert receipt["checks"]["critical_strip_maps_right_halfplane"] is True
    assert receipt["checks"]["critical_line_maps_positive_real"] is True
    assert receipt["checks"]["hyperbolic_distance_identity"] is True
    assert receipt["checks"]["synthetic_offaxis_squared_pole_in_upper_halfplane"] is True
    assert receipt["open"]["construct_weyl_M_from_Xi_theta_without_zero_input"] is True
    assert receipt["open"]["riemann_hypothesis"] is True
