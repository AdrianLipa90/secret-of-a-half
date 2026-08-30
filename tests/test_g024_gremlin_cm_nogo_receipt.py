import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RECEIPT = ROOT / "research" / "GREMLIN_G024_COMPLETE_MONOTONICITY_ROUTE_AUDIT_V0_1.json"
THEOREM = ROOT / "research" / "SOH_G024_COMPLETE_MONOTONICITY_SUPEREXPONENTIAL_NOGO_V0_1.md"
PROMOTED_CLAIM = ROOT / "claims" / "SOH_G024_T_COMPLETE_MONOTONICITY_ROUTE_NOGO_V0_1.json"


def _load_receipt():
    return json.loads(RECEIPT.read_text(encoding="utf-8"))


def _load_promoted_claim():
    return json.loads(PROMOTED_CLAIM.read_text(encoding="utf-8"))


def test_g024_gremlin_route_receipt_preserves_candidate_only_tool_authority():
    data = _load_receipt()

    assert data["schema"] == "SOH_GREMLIN_G024_ROUTE_AUDIT_V0_1"
    assert data["status"] == "REPOSITORY_REVIEWED_BRANCH_PROMOTED"
    assert data["router_schema"] == "GREMLIN_MCP_OCTOPUS_ROUTER_V0_5"
    assert data["route_mask"] == ["OWL", "MOLE", "HOUND"]
    assert len(data["route_commitment"]) == 64

    authority = data["authority"]
    assert authority["canon_allowed"] is False
    assert authority["gremlin_self_promotion"] is False
    assert authority["scientific_promotion_performed"] is True
    assert authority["promotion_authority"] == "repository-owner instruction"
    assert authority["main_merge_performed"] is False
    assert authority["production_runtime_write"] is False
    assert authority["execution_admitted"] is False

    finding = data["finding"]
    assert finding["id"] == "SOH.G024.CM.SUPEREXPONENTIAL_NOGO"
    assert finding["classification"] == "THEOREM_LEVEL_ROUTE_NOGO"
    assert finding["promoted_claim_id"] == "SOH-G024-T"
    assert finding["closes_candidate_route"] == "FULL_COMPLETE_MONOTONICITY_TO_GAUSSIAN_MIXTURE"
    assert finding["next_candidate_surface"] == "DIRECT_ONE_DIMENSIONAL_POSITIVE_DEFINITENESS_OR_FOURIER_POSITIVITY"

    assert THEOREM.is_file()
    assert PROMOTED_CLAIM.is_file()
    assert data["promotion_binding"] == str(PROMOTED_CLAIM.relative_to(ROOT))
    for relative in data["source_bindings"]:
        assert (ROOT / relative).is_file(), relative


def test_g024_promoted_claim_is_reviewed_but_not_main_canonical():
    claim = _load_promoted_claim()

    assert claim["schema"] == "SOH_G024_PROMOTED_CLAIM_V0_1"
    assert claim["claim_id"] == "SOH-G024-T"
    assert claim["status"] == "REPOSITORY_REVIEWED_BRANCH_PROMOTED_THEOREM"
    assert claim["promotion_level"] == "REVIEWED_THEOREM_CLAIM"
    assert claim["canonical_on_main"] is False
    assert claim["proof_of_rh"] is False
    assert claim["promotion"]["gremlin_self_promotion"] is False
    assert claim["promotion"]["gremlin_canon_authority"] is False
    assert claim["promotion"]["main_merge_performed"] is False
    assert claim["route_effect"]["closed_route"] == "FULL_COMPLETE_MONOTONICITY_TO_GAUSSIAN_MIXTURE"
    assert claim["review_firewall"]["first_failing_derivative_order"] == "UNKNOWN_M_GE_3"
