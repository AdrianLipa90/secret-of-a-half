from __future__ import annotations

from pathlib import Path

from secret_of_a_half.pnv_graph_audit import (
    audit_pnv_identity_graph,
    audit_pnv_identity_graph_file,
    parse_pnv_identity_graph,
)


ROOT = Path(__file__).resolve().parents[1]
PNV = ROOT / "construction" / "phasenav" / "secret_of_half_identity_holonomy_v0_7.pnv"


def test_native_identity_graph_is_structurally_complete() -> None:
    audit = audit_pnv_identity_graph_file(PNV)
    assert audit.ok
    assert audit.node_count == 22
    assert audit.relation_count == 16
    assert audit.unpaired_nodes == ()
    assert audit.issues == ()
    assert set(audit.external_requirements) == {
        "ALL_NONTRIVIAL_XI_ZEROS",
        "RADIAN_REPRESENTATION",
        "XI_ZERO",
    }
    assert all(degree >= 1 for degree in audit.degrees.values())


def test_native_graph_keeps_holonomy_typed_and_open_edges_open() -> None:
    nodes, relations = parse_pnv_identity_graph(PNV.read_text(encoding="utf-8"))
    by_id = {relation.relation_id: relation for relation in relations}
    assert len(nodes) == 22
    assert by_id["R004"].kind == "HOLONOMIC"
    assert by_id["R004"].status == "STANDARD"
    assert by_id["R004"].holonomy_turns == "1/2"
    assert by_id["R005"].requires == ("HALF_TURN_PHASE",)
    assert by_id["R007"].holonomy_turns == "1/2"
    assert by_id["R014"].status == "OPEN"
    assert by_id["R016"].kind == "OPEN_BRIDGE"
    assert by_id["R016"].status == "OPEN"


def test_graph_audit_rejects_unknown_endpoint() -> None:
    text = PNV.read_text(encoding="utf-8") + "\nR999: from=SIGMA_AXIS, to=NOT_A_NODE, kind=DUAL, status=EXACT\n"
    audit = audit_pnv_identity_graph(text)
    assert not audit.ok
    assert any("unknown relation target: R999:NOT_A_NODE" in issue for issue in audit.issues)
