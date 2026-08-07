"""Audit the native PhaseNav v0.7 identity/holonomy declaration.

This module deliberately audits structure, not truth.  A complete graph means
that every declared semantic node participates in at least one typed relation;
it does not promote MODEL or OPEN relations to proof status.
"""
from __future__ import annotations

from dataclasses import dataclass
import re
from pathlib import Path


_NODE_RE = re.compile(r"^(ID\d+):\s+name=([A-Z][A-Z0-9_]*)\b", re.MULTILINE)
_REL_RE = re.compile(
    r"^(R\d+):\s+from=([A-Z][A-Z0-9_]*),\s*to=([A-Z][A-Z0-9_]*),\s*(.*)$",
    re.MULTILINE,
)
_FIELD_RE = re.compile(r"(?:^|,\s*)([a-z_]+)=([^,]+)")

_ALLOWED_STATUS = frozenset({"EXACT", "STANDARD", "MODEL", "OPEN"})
_ALLOWED_KIND = frozenset({
    "FIXED_POINT",
    "DUAL",
    "IMPLIES",
    "REPRESENTS",
    "HOLONOMIC",
    "CROSS_REFERENCE",
    "PAIR_FACTOR",
    "OPEN_BRIDGE",
})


@dataclass(frozen=True)
class PNVNode:
    node_id: str
    name: str


@dataclass(frozen=True)
class PNVRelation:
    relation_id: str
    source: str
    target: str
    kind: str
    status: str
    requires: tuple[str, ...] = ()
    holonomy_turns: str | None = None


@dataclass(frozen=True)
class PNVGraphAudit:
    node_count: int
    relation_count: int
    degrees: dict[str, int]
    unpaired_nodes: tuple[str, ...]
    external_requirements: tuple[str, ...]
    issues: tuple[str, ...]

    @property
    def ok(self) -> bool:
        return not self.issues and not self.unpaired_nodes


def parse_pnv_identity_graph(text: str) -> tuple[tuple[PNVNode, ...], tuple[PNVRelation, ...]]:
    """Parse the IDxxx/Rxxx declarations from the native .pnv source."""
    nodes = tuple(PNVNode(node_id, name) for node_id, name in _NODE_RE.findall(text))
    relations: list[PNVRelation] = []
    for relation_id, source, target, tail in _REL_RE.findall(text):
        fields = {key: value.strip() for key, value in _FIELD_RE.findall(tail)}
        requires = tuple(
            item.strip()
            for item in fields.get("requires", "").split("+")
            if item.strip()
        )
        relations.append(PNVRelation(
            relation_id=relation_id,
            source=source,
            target=target,
            kind=fields.get("kind", ""),
            status=fields.get("status", ""),
            requires=requires,
            holonomy_turns=fields.get("holonomy_turns"),
        ))
    return nodes, tuple(relations)


def audit_pnv_identity_graph(text: str) -> PNVGraphAudit:
    """Check identifiers, references, relation types and degree >= 1 coverage."""
    nodes, relations = parse_pnv_identity_graph(text)
    issues: list[str] = []

    node_ids = [node.node_id for node in nodes]
    node_names = [node.name for node in nodes]
    relation_ids = [relation.relation_id for relation in relations]
    if len(node_ids) != len(set(node_ids)):
        issues.append("duplicate node id")
    if len(node_names) != len(set(node_names)):
        issues.append("duplicate node name")
    if len(relation_ids) != len(set(relation_ids)):
        issues.append("duplicate relation id")

    names = set(node_names)
    degrees = {name: 0 for name in node_names}
    external_requirements: set[str] = set()

    for relation in relations:
        if relation.source not in names:
            issues.append(f"unknown relation source: {relation.relation_id}:{relation.source}")
        else:
            degrees[relation.source] += 1
        if relation.target not in names:
            issues.append(f"unknown relation target: {relation.relation_id}:{relation.target}")
        else:
            degrees[relation.target] += 1
        if relation.kind not in _ALLOWED_KIND:
            issues.append(f"invalid relation kind: {relation.relation_id}:{relation.kind}")
        if relation.status not in _ALLOWED_STATUS:
            issues.append(f"invalid relation status: {relation.relation_id}:{relation.status}")
        if relation.holonomy_turns is not None and relation.holonomy_turns == "":
            issues.append(f"empty holonomy_turns: {relation.relation_id}")
        for requirement in relation.requires:
            if requirement in names:
                # Hyperedge premises count as semantic participation.
                degrees[requirement] += 1
            else:
                # External facts such as XI_ZERO are legal proof premises but not graph nodes.
                external_requirements.add(requirement)

    unpaired = tuple(sorted(name for name, degree in degrees.items() if degree < 1))
    return PNVGraphAudit(
        node_count=len(nodes),
        relation_count=len(relations),
        degrees=degrees,
        unpaired_nodes=unpaired,
        external_requirements=tuple(sorted(external_requirements)),
        issues=tuple(issues),
    )


def audit_pnv_identity_graph_file(path: str | Path) -> PNVGraphAudit:
    source = Path(path)
    return audit_pnv_identity_graph(source.read_text(encoding="utf-8"))
