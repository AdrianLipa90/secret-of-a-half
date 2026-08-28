#!/usr/bin/env python3
"""Read-only inventory of GitHub Actions artifact storage for this repository.

The script never deletes or mutates artifacts. It is intended for CI diagnostics
when repository-level artifact accumulation is suspected.
"""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from collections import defaultdict
from datetime import datetime, timezone


def _api_json(url: str, token: str) -> dict:
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "secret-of-a-half-artifact-inventory",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.load(response)
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as exc:
        raise RuntimeError(f"GitHub artifact inventory request failed: {exc}") from exc


def main() -> int:
    repository = os.environ.get("GITHUB_REPOSITORY", "").strip()
    token = os.environ.get("GITHUB_TOKEN", "").strip()
    if not repository or "/" not in repository:
        print("ARTIFACT_STORAGE_INVENTORY_FAIL missing GITHUB_REPOSITORY", file=sys.stderr)
        return 2
    if not token:
        print("ARTIFACT_STORAGE_INVENTORY_FAIL missing GITHUB_TOKEN", file=sys.stderr)
        return 2

    artifacts: list[dict] = []
    page = 1
    while True:
        payload = _api_json(
            f"https://api.github.com/repos/{repository}/actions/artifacts?per_page=100&page={page}",
            token,
        )
        batch = payload.get("artifacts")
        if not isinstance(batch, list):
            print("ARTIFACT_STORAGE_INVENTORY_FAIL malformed GitHub response", file=sys.stderr)
            return 2
        artifacts.extend(batch)
        if len(batch) < 100:
            break
        page += 1
        if page > 100:
            print("ARTIFACT_STORAGE_INVENTORY_FAIL pagination safety limit exceeded", file=sys.stderr)
            return 2

    active = [a for a in artifacts if not bool(a.get("expired"))]
    expired = [a for a in artifacts if bool(a.get("expired"))]
    active_bytes = sum(int(a.get("size_in_bytes") or 0) for a in active)
    expired_bytes = sum(int(a.get("size_in_bytes") or 0) for a in expired)

    by_name: dict[str, dict[str, int]] = defaultdict(lambda: {"count": 0, "bytes": 0})
    for artifact in active:
        name = str(artifact.get("name") or "<unnamed>")
        by_name[name]["count"] += 1
        by_name[name]["bytes"] += int(artifact.get("size_in_bytes") or 0)

    now = datetime.now(timezone.utc)
    ages = []
    for artifact in active:
        created = artifact.get("created_at")
        if isinstance(created, str):
            try:
                dt = datetime.fromisoformat(created.replace("Z", "+00:00"))
            except ValueError:
                continue
            ages.append((now - dt).total_seconds() / 86400.0)

    print(
        "ARTIFACT_STORAGE_INVENTORY "
        f"repository={repository} total_records={len(artifacts)} "
        f"active_count={len(active)} active_bytes={active_bytes} "
        f"active_mib={active_bytes / (1024 ** 2):.3f} "
        f"expired_count={len(expired)} expired_bytes={expired_bytes}"
    )
    if ages:
        print(f"ARTIFACT_STORAGE_AGE oldest_active_days={max(ages):.3f} newest_active_days={min(ages):.3f}")

    for name, stats in sorted(by_name.items(), key=lambda item: (-item[1]["bytes"], item[0])):
        print(
            "ARTIFACT_STORAGE_GROUP "
            f"name={json.dumps(name)} count={stats['count']} bytes={stats['bytes']} "
            f"mib={stats['bytes'] / (1024 ** 2):.3f}"
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
