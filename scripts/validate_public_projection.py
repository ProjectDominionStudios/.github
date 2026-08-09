"""Validate the public organization projection without mutating the repository."""

from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
MACHINE = "publication-provenance.machine.yaml"
SOURCE_REVISION = "53ccd17bce8ab586070918445537eb81c8d0c022"
REQUIRED = {
    "README.md",
    "profile/README.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "PULL_REQUEST_TEMPLATE.md",
    "PUBLICATION-PROVENANCE.md",
    MACHINE,
    ".github/workflows/validate.yml",
    "scripts/validate_public_projection.py",
    "scripts/test_public_projection.py",
}
FORBIDDEN_PATTERNS = {
    "unpublished product name": re.compile(r"ANTON\.AOS", re.IGNORECASE),
    "private repository URL": re.compile(
        r"https?://github\.com/ProjectDominionStudios/(?:Studio|ANTON-AOS)",
        re.IGNORECASE,
    ),
    "local Windows path": re.compile(r"[A-Za-z]:\\"),
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "credential-like token": re.compile(r"\b(?:gh[opsu]_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16})\b"),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes().replace(b"\r\n", b"\n")).hexdigest()


def validate(root: Path = ROOT) -> list[str]:
    root = root.resolve()
    failures: list[str] = []
    for relative in sorted(REQUIRED):
        if not (root / relative).is_file():
            failures.append(f"missing required public file: {relative}")

    machine_path = root / MACHINE
    try:
        machine = yaml.safe_load(machine_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, yaml.YAMLError) as exc:
        return failures + [f"cannot parse publication provenance: {exc}"]

    document = machine.get("document") or {}
    if document.get("knowledge_role") != "published":
        failures.append("publication provenance must use the Published role")
    if document.get("security_classification") != "public":
        failures.append("publication provenance must be classified public")
    if machine.get("source", {}).get("revision") != SOURCE_REVISION:
        failures.append("canonical source revision drift")
    publication = machine.get("publication") or {}
    for field in ("deployment_authorized", "permission_change_authorized", "product_launch_authorized"):
        if publication.get(field) is not False:
            failures.append(f"public projection may not authorize {field}")

    for projection in machine.get("projections") or []:
        relative = projection.get("path", "")
        path = root / relative
        if not path.is_file():
            failures.append(f"missing declared projection: {relative}")
            continue
        if sha256(path) != projection.get("sha256"):
            failures.append(f"projection checksum mismatch: {relative}")
        content = path.read_text(encoding="utf-8")
        if projection.get("object_id") not in content:
            failures.append(f"projection does not declare its Knowledge Object ID: {relative}")

    for path in root.rglob("*"):
        if not path.is_file() or ".git" in path.parts or path.suffix.lower() not in {".md", ".py", ".yaml", ".yml"}:
            continue
        relative = path.relative_to(root).as_posix()
        content = path.read_text(encoding="utf-8")
        for label, pattern in FORBIDDEN_PATTERNS.items():
            if pattern.search(content):
                failures.append(f"{label} found in public file: {relative}")
    return failures


def main() -> int:
    failures = validate()
    if failures:
        print("Public projection validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("Published profile, community defaults, provenance, integrity, and sanitization validated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
