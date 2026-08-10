from __future__ import annotations

import unittest

from ssot_pack_web_performance_rum import (
    __pypi_package_name__,
    __ssot_package_name__,
    load_document_manifest,
    load_pack_manifest,
    load_pack_metadata,
    load_pack_schema_version,
    read_packaged_document_text,
)


class GovernancePackManifestTests(unittest.TestCase):
    def test_pack_metadata_contract_is_exposed(self) -> None:
        metadata = load_pack_metadata()
        self.assertEqual("web-performance-rum-governance-pack", __ssot_package_name__)
        self.assertEqual("web-performance-rum-governance-pack", __pypi_package_name__)
        self.assertEqual("1.0.0", metadata["schema_version"])
        self.assertEqual("web-performance-rum-governance-pack", metadata["ssot_package_name"])
        self.assertEqual("pack:web-performance-rum", metadata["origin"]["id"])
        self.assertEqual("ssot_pack_web_performance_rum", metadata["origin"]["import_name"])
        self.assertEqual("governance-pack", metadata["origin"]["kind"])
        self.assertEqual("extension-pack", metadata["trust"]["origin"])
        self.assertEqual("extension-pack:web-performance-rum-governance-pack", metadata["trust"]["reservation_owner"])
        self.assertFalse(metadata["trust"]["trusted_by_default"])
        self.assertEqual("1.0.0", load_pack_schema_version())

    def test_pack_manifest_contract_is_exposed(self) -> None:
        manifest = load_pack_manifest()
        self.assertEqual("web-performance-rum-governance-pack", manifest["metadata"]["origin"]["package_name"])
        self.assertEqual(7, len(manifest["documents"]["adr"]))
        self.assertEqual(18, len(manifest["documents"]["spec"]))

    def test_packaged_documents_are_readable(self) -> None:
        adr_manifest = load_document_manifest("adr")
        spec_manifest = load_document_manifest("spec")
        self.assertEqual("adr:navigation-timing-rum-policy", adr_manifest[0]["id"])
        self.assertEqual("spc:navigation-timing-entry-requirements", spec_manifest[0]["id"])
        self.assertIn("Navigation Timing RUM Policy", read_packaged_document_text("adr", adr_manifest[0]["filename"]))
        self.assertIn("Navigation Timing Entry Requirements", read_packaged_document_text("spec", spec_manifest[0]["filename"]))

    def test_packaged_adr_documents_are_downstream_portable(self) -> None:
        forbidden_terms = [
            "pack:",
            "This pack",
            "extension-pack",
            "governance-pack",
            "ssot-pack",
        ]
        for row in load_document_manifest("adr"):
            text = read_packaged_document_text("adr", row["filename"])
            for term in forbidden_terms:
                self.assertNotIn(term, text)

    def test_packaged_spec_documents_are_downstream_portable(self) -> None:
        forbidden_terms = [
            "pack:",
            "This pack",
            "extension-pack",
            "governance-pack",
            "ssot-pack",
        ]
        for row in load_document_manifest("spec"):
            text = read_packaged_document_text("spec", row["filename"])
            for term in forbidden_terms:
                self.assertNotIn(term, text)


if __name__ == "__main__":
    unittest.main()
