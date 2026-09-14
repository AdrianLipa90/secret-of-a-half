#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "REPOSITORY_HOLONOMY_V1.json"
GITMODULES_PATH = ROOT / ".gitmodules"
GITLINK_PATH = ROOT / "½"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"HOLONOMY_FAIL: {message}")


manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
require(manifest["schema"] == "sohalf.repository-holonomy/v1", "unexpected local schema")
require(manifest["repository"] == "AdrianLipa90/secret-of-a-half", "wrong local repository")
require(
    manifest["peer_repository"]
    == "AdrianLipa90/The-Fundamental-Theory-of-Informational-Relations",
    "wrong peer repository",
)
require(manifest["peer_branch"] == "main", "peer branch must be main")
require(manifest["gitlink_path"] == "½", "gitlink must be exposed directly as ½")
require(manifest["module_path"] == "½/TIR/zeta_information_axis", "module path mismatch")
require(manifest["rh_status"] == "OPEN", "RH firewall changed")
require(manifest["scientific_claim_impact"] == "NONE", "repository wiring changed claim status")
require(manifest["recursive_submodules"] is False, "recursive submodules are forbidden")

modules = GITMODULES_PATH.read_text(encoding="utf-8")
require('path = ½' in modules, "½ gitlink path missing from .gitmodules")
require(
    'url = https://github.com/AdrianLipa90/The-Fundamental-Theory-of-Informational-Relations.git'
    in modules,
    "TIR submodule URL mismatch",
)

require(GITLINK_PATH.is_dir(), "TIR gitlink ½ was not initialized")
actual_peer_commit = subprocess.check_output(
    ["git", "-C", str(GITLINK_PATH), "rev-parse", "HEAD"], text=True
).strip()
require(actual_peer_commit == manifest["peer_commit"], "TIR gitlink SHA mismatch")

module_root = ROOT / manifest["module_path"]
require(module_root.is_dir(), "critical-axis module is missing below ½")
peer_manifest_path = module_root / "REPOSITORY_HOLONOMY_V1.json"
require(peer_manifest_path.is_file(), "TIR backlink manifest missing")
peer = json.loads(peer_manifest_path.read_text(encoding="utf-8"))
require(peer["schema"] == "tir.soh-repository-holonomy/v1", "unexpected peer schema")
require(peer["dedicated_repository"] == "AdrianLipa90/secret-of-a-half", "peer backlink mismatch")
require(peer["local_path"] == "TIR/zeta_information_axis", "peer module path mismatch")
require(peer["recursive_submodule"] is False, "peer recursive submodule forbidden")
require(peer["physical_gitlink_direction"] == "secret-of-a-half -> TIR", "gitlink direction mismatch")
require(peer["riemann_hypothesis_status"] == "OPEN", "peer RH firewall changed")
require(peer["scientific_claim_impact"] == "NONE", "peer repository wiring changed claim status")

print(
    json.dumps(
        {
            "status": "PASS",
            "local_repository": manifest["repository"],
            "peer_repository": manifest["peer_repository"],
            "peer_commit": actual_peer_commit,
            "gitlink": "½",
            "module_path": manifest["module_path"],
            "rh_status": "OPEN",
        },
        sort_keys=True,
    )
)
