from __future__ import annotations

import unittest

from ssot_pack_contracts import InvalidPackManifestError

from ssot_registry_pack_template import (
    __pypi_package_name__,
    __ssot_package_name__,
    __version__,
    list_packaged_document_ids,
    load_document_manifest,
    load_pack_manifest,
    load_pack_metadata,
    load_pack_schema_version,
    read_packaged_document_text,
)


class TemplateManifestTests(unittest.TestCase):
    def test_pack_metadata_contract_is_exposed(self) -> None:
        metadata = load_pack_metadata()
        self.assertEqual("ssot-registry-pack-template", __ssot_package_name__)
        self.assertEqual("ssot-registry-pack-template", __pypi_package_name__)
        self.assertEqual("0.1.0", __version__)
        self.assertEqual("1.0.0", metadata["schema_version"])
        self.assertEqual("ssot-registry-pack-template", metadata["ssot_package_name"])
        self.assertEqual("ssot-registry-pack-template", metadata["pypi_package_name"])
        self.assertEqual("ssot-registry-pack-template", metadata["origin"]["package_name"])
        self.assertEqual("ssot_registry_pack_template", metadata["origin"]["import_name"])
        self.assertEqual("extension-pack", metadata["trust"]["origin"])
        self.assertEqual("extension-pack:ssot-registry-pack-template", metadata["trust"]["reservation_owner"])
        self.assertEqual("1.0.0", load_pack_schema_version())
        self.assertEqual("0.1.0", metadata["version"])

    def test_pack_manifest_contract_is_exposed(self) -> None:
        manifest = load_pack_manifest()
        self.assertEqual("ssot-registry-pack-template", manifest["metadata"]["origin"]["package_name"])
        self.assertEqual([], manifest["documents"]["adr"])
        self.assertEqual([], manifest["documents"]["spec"])
        self.assertEqual([], list_packaged_document_ids())

    def test_adr_manifest_starts_empty(self) -> None:
        manifest = load_document_manifest("adr")
        self.assertEqual([], manifest)

    def test_spec_manifest_starts_empty(self) -> None:
        manifest = load_document_manifest("spec")
        self.assertEqual([], manifest)

    def test_missing_packaged_document_raises_file_not_found(self) -> None:
        with self.assertRaises(InvalidPackManifestError):
            read_packaged_document_text("spec", "missing-document.yaml")


if __name__ == "__main__":
    unittest.main()
