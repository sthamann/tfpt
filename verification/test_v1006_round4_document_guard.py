"""Regression tests for v1006's Round-4 memorandum guard."""

from __future__ import annotations

from tex_sources import read_tex

from pathlib import Path
import sys
import unittest


VERIFICATION_DIR = Path(__file__).resolve().parent
if str(VERIFICATION_DIR) not in sys.path:
    sys.path.insert(0, str(VERIFICATION_DIR))

import v1006_mmst_lemma_battery as audit


class Round4DocumentGuardTests(unittest.TestCase):
    def test_current_memorandum_has_norm_and_open_boundary(self) -> None:
        text = read_tex(Path(audit.MMST_TEX))
        self.assertTrue(audit.telb_round4_document_guard(text))

    def test_every_required_clause_is_load_bearing(self) -> None:
        complete = "\n".join(audit.ROUND4_TELB_DOCUMENT_SNIPPETS)
        for snippet in audit.ROUND4_TELB_DOCUMENT_SNIPPETS:
            with self.subTest(missing=snippet):
                self.assertFalse(
                    audit.telb_round4_document_guard(complete.replace(snippet, "", 1))
                )

    def test_historical_external_box_alone_is_rejected(self) -> None:
        stale = (
            "TEL-B-EXTERNAL. Matrix-valued two-edge estimate. "
            "No all-N constant is claimed. ALG-EXH remains open."
        )
        self.assertFalse(audit.telb_round4_document_guard(stale))


if __name__ == "__main__":
    unittest.main()
