import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RECEIPT = ROOT / "research" / "GREMLIN_G024_COMPLETE_MONOTONICITY_ROUTE_AUDIT_V0_1.json"
THEOREM = ROOT / "research" / "SOH_G024_COMPLETE_MONOTONICITY_SUPEREXPONENTIAL_NOGO_V0_1.md"


def _load_receipt():
    return json.loads(RECEIPT.read_text(encoding="utf-8"))


def test_g024_gremlin_route_receipt_is_candidate_only_and_bound():
    data = _load_receipt()

    assert data["schema"] == "SOH_GREMLIN_G024_ROUTE_AUDIT_V0_1"
    assert data["status"] == "CANDIDATE_THEOREM_PENDING_REPOSITORY_REVIEW"
    assert data["router_schema"] == "GREMLIN_MCP_OCTOPUS_ROUTER_V0_5"
    assert data["route_mask"] == ["OWL", "MOLE", "HOUND"]
    assert len(data["route_commitment"]) == 64

    authority = data["authority"]
    assert authority["canon_allowed"] is False
    assert authority["scientific_promotion_performed"] is False
    assert authority["production_runtime_write"] is False
    assert authority["execution_admitted"] is False

    finding = data["finding"]
    assert finding["id"] == "SOH.G024.CM.SUPEREXPONENTIAL_NOGO"
    assert finding["closes_candidate_route"] == "FULL_COMPLETE_MONOTONICITY_TO_GAUSSIAN_MIXTURE"
    assert finding["next_candidate_surface"] == "DIRECT_ONE_DIMENSIONAL_POSITIVE_DEFINITENESS_OR_FOURIER_POSITIVITY"

    assert THEOREM.is_file()
    for relative in data["source_bindings"]:
        assert (ROOT / relative).is_file(), relative
