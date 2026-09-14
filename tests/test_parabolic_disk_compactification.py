from __future__ import annotations

from secret_of_a_half.parabolic_disk_compactification import build_receipt


def test_parabolic_disk_compactification_receipt() -> None:
    receipt = build_receipt()
    assert receipt["status"] == "PASS"
    assert receipt["rh_claim"] is False
    assert receipt["checks"]["parabolic_identity"] is True
    assert receipt["checks"]["roundtrip"] is True
    assert receipt["checks"]["exponential_cayley_identity"] is True
    assert receipt["checks"]["outer_boundary_to_unit_circle"] is True
    assert receipt["checks"]["critical_line_to_positive_radius"] is True
    assert receipt["checks"]["g018_transfer_radius"] is True
    assert receipt["checks"]["g019_sample_real_part_positive"] is True
    assert receipt["open"]["riemann_hypothesis"] is True
