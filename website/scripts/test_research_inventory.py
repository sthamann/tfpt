"""Focused regression for explicit metadata-only publication omissions."""
import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


spec = importlib.util.spec_from_file_location(
    "research_inventory_export", Path(__file__).with_name("build-research-inventory.py")
)
inventory = importlib.util.module_from_spec(spec)
spec.loader.exec_module(inventory)


class ResearchInventoryTests(unittest.TestCase):
    def test_withheld_source_keeps_metadata_and_reason_but_cannot_publish_payload(self):
        ref = {
            "id": "source:db19a580b8ce8c1fa806be0b",
            "path": "experiments/tfpt-discovery/ccc_kms_bridge_closure_probe.py",
            "sha256": "a" * 64,
            "lineStart": 1,
            "lineEnd": 2,
            "href": None,
            "freshness": "not-published",
            "publicationState": "withheld-root",
            "historicalSource": False,
        }
        omissions = [{"sourceId": ref["id"], "path": ref["path"],
                      "reason": "outside approved scientific publication roots"}]
        filename = "sources/" + ref["id"].split(":", 1)[1] + ".txt"
        with tempfile.TemporaryDirectory() as directory, patch.object(inventory, "PUBLIC", Path(directory)):
            inventory.validate_source_ref(ref, omissions, [])
            for payload in ({"href": "/research/leak.txt"}, {"remoteHref": "https://example.com/leak"},
                            {"excerptSha256": "b" * 64}, {"text": "unpublished source bytes"}):
                with self.subTest(payload=payload), self.assertRaises(AssertionError):
                    inventory.validate_source_ref({**ref, **payload}, omissions, [])
            with self.assertRaises(AssertionError):
                inventory.validate_source_ref(ref, [], [])
            with self.assertRaises(AssertionError):
                inventory.validate_source_ref(ref, omissions, [{"path": filename, "sha256": "b" * 64}])
            excerpt = Path(directory) / filename
            excerpt.parent.mkdir()
            excerpt.write_text("unpublished source bytes")
            with self.assertRaises(AssertionError):
                inventory.validate_source_ref(ref, omissions, [])


if __name__ == "__main__":
    unittest.main()
