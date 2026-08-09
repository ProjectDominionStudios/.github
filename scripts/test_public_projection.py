from __future__ import annotations

import shutil
import tempfile
import unittest
from pathlib import Path

import yaml

from scripts.validate_public_projection import ROOT, validate


class PublicProjectionNegativeCases(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(prefix="pds-public-projection-")
        self.root = Path(self.temporary.name) / "repository"
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns(".git", "__pycache__"))

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def assert_rejected(self, phrase: str) -> None:
        failures = validate(self.root)
        self.assertTrue(any(phrase in failure for failure in failures), failures)

    def test_unpublished_product_content_is_rejected(self) -> None:
        path = self.root / "profile/README.md"
        unpublished_name = "ANTON" + ".AOS launch"
        path.write_text(path.read_text(encoding="utf-8") + f"\n{unpublished_name}\n", encoding="utf-8")
        self.assert_rejected("unpublished product name")

    def test_local_path_is_rejected(self) -> None:
        path = self.root / "README.md"
        local_path = "C:" + chr(92) + "private" + chr(92) + "file"
        path.write_text(path.read_text(encoding="utf-8") + f"\n{local_path}\n", encoding="utf-8")
        self.assert_rejected("local Windows path")

    def test_source_revision_drift_is_rejected(self) -> None:
        path = self.root / "publication-provenance.machine.yaml"
        document = yaml.safe_load(path.read_text(encoding="utf-8"))
        document["source"]["revision"] = "0" * 40
        path.write_text(yaml.safe_dump(document, sort_keys=False), encoding="utf-8")
        self.assert_rejected("canonical source revision drift")

    def test_projection_checksum_drift_is_rejected(self) -> None:
        path = self.root / "CONTRIBUTING.md"
        path.write_text(path.read_text(encoding="utf-8") + "\nDrift\n", encoding="utf-8")
        self.assert_rejected("projection checksum mismatch")


if __name__ == "__main__":
    unittest.main()
