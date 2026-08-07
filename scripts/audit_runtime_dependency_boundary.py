#!/usr/bin/env python3
"""Audit the runtime dependency boundary for the reviewed Secret-of-a-Half core.

This audit does not claim that the whole repository is dependency-free.  It
records a narrower architectural contract:

* native semantic components must use only the Python standard library plus
  local ``secret_of_a_half`` modules;
* DHSE Stage M may use NumPy as a declared vectorized accelerator;
* the prime-side Weil arithmetic audit may use mpmath as a declared numerical
  oracle for high-precision transcendental evaluation and quadrature.

The distinction is intentional: an accelerator/oracle is not the source of the
mathematical semantics.  Any new third-party import in the audited components
fails the receipt until its role is explicitly reviewed.
"""
from __future__ import annotations

import ast
import json
from pathlib import Path
import sys
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "data" / "processed" / "runtime_dependency_boundary.json"
LOCAL_ROOT = "secret_of_a_half"

COMPONENTS: dict[str, dict[str, object]] = {
    "native_semantics": {
        "role": "STDLIB_NATIVE_SEMANTICS",
        "files": (
            "src/secret_of_a_half/phasenav_theta_bridge.py",
            "src/secret_of_a_half/phasenav_weil_probe.py",
            "src/secret_of_a_half/zero_undefined_duality.py",
        ),
        "allowed_third_party": frozenset(),
    },
    "dhse_stage_m": {
        "role": "DECLARED_VECTORIZED_ACCELERATOR",
        "files": ("src/secret_of_a_half/dhse_001_stage_m.py",),
        "allowed_third_party": frozenset({"numpy"}),
    },
    "weil_arithmetic": {
        "role": "DECLARED_NUMERICAL_ORACLE",
        "files": ("src/secret_of_a_half/phasenav_weil_arithmetic.py",),
        "allowed_third_party": frozenset({"mpmath"}),
    },
}


def top_level_imports(path: Path) -> set[str]:
    """Return top-level absolute import roots from one Python source file."""
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    imports: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.update(alias.name.split(".", 1)[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.level == 0 and node.module:
            imports.add(node.module.split(".", 1)[0])
    return imports


def classify_imports(imports: Iterable[str]) -> tuple[list[str], list[str], list[str]]:
    """Split imports into standard-library, local-package and third-party roots."""
    standard: list[str] = []
    local: list[str] = []
    third_party: list[str] = []
    stdlib = set(sys.stdlib_module_names)
    for name in sorted(set(imports)):
        if name == LOCAL_ROOT:
            local.append(name)
        elif name in stdlib:
            standard.append(name)
        else:
            third_party.append(name)
    return standard, local, third_party


def build_receipt() -> dict[str, object]:
    """Build the deterministic dependency-boundary receipt."""
    component_rows: dict[str, object] = {}
    overall_pass = True

    for component, specification in COMPONENTS.items():
        allowed = set(specification["allowed_third_party"])
        file_rows: list[dict[str, object]] = []
        observed_third_party: set[str] = set()

        for relative in specification["files"]:
            path = ROOT / str(relative)
            if not path.is_file():
                file_rows.append({"path": str(relative), "exists": False, "pass": False})
                overall_pass = False
                continue

            standard, local, third_party = classify_imports(top_level_imports(path))
            observed_third_party.update(third_party)
            file_rows.append(
                {
                    "path": str(relative),
                    "exists": True,
                    "standard_library": standard,
                    "local_package": local,
                    "third_party": third_party,
                    "pass": set(third_party) <= allowed,
                }
            )

        unexpected = sorted(observed_third_party - allowed)
        component_pass = not unexpected and all(bool(row["pass"]) for row in file_rows)
        overall_pass = overall_pass and component_pass
        component_rows[component] = {
            "role": specification["role"],
            "allowed_third_party": sorted(allowed),
            "observed_third_party": sorted(observed_third_party),
            "unexpected_third_party": unexpected,
            "files": file_rows,
            "pass": component_pass,
        }

    return {
        "schema": "SOH_RUNTIME_DEPENDENCY_BOUNDARY_V1",
        "claim_boundary": {
            "whole_repository_dependency_free": False,
            "native_semantics_third_party_free": True,
            "numpy_role": "ACCELERATOR_NOT_SEMANTIC_SOURCE",
            "mpmath_role": "NUMERICAL_ORACLE_NOT_SEMANTIC_SOURCE",
        },
        "components": component_rows,
        "technical_status": "PASS" if overall_pass else "FAIL",
    }


def main() -> None:
    """Write and print the receipt, failing when the reviewed boundary drifts."""
    receipt = build_receipt()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2, sort_keys=True))
    if receipt["technical_status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
