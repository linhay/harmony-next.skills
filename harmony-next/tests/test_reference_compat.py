from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "reference_compat.py"
SPEC = importlib.util.spec_from_file_location("reference_compat", SCRIPT_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class ReferenceCompatTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.repo_root = Path(self.temp_dir.name)
        self.references_root = self.repo_root / "references"
        self.js_root = self.references_root / "JsEtsAPIReference"
        (self.js_root / "topics" / "misc").mkdir(parents=True)
        (self.js_root / "modules" / "ohos").mkdir(parents=True)
        (self.references_root / "quickStart").mkdir(parents=True)

        (self.js_root / "topics" / "misc" / "native_handwrite_api.h.md").write_text(
            "# native_handwrite_api.h\n\n起始版本： 23\n",
            encoding="utf-8",
        )
        (self.js_root / "topics" / "misc" / "HandWrite.md").write_text(
            "[native_handwrite_api.h](../../capi/headers/native_handwrite_api.h.md)\n",
            encoding="utf-8",
        )
        (self.js_root / "modules" / "ohos" / "@ohos.demo.md").write_text(
            "# @ohos.demo\n",
            encoding="utf-8",
        )
        (self.references_root / "quickStart" / "intro.md").write_text(
            "# intro\n",
            encoding="utf-8",
        )
        self.paths = MODULE.build_paths(self.repo_root)

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_generate_creates_compat_pages_and_indexes_them(self) -> None:
        rewritten = MODULE.rewrite_header_links(self.paths)
        MODULE.generate_references_index(self.paths)
        MODULE.generate_index(self.paths)

        self.assertEqual(rewritten, 1)
        self.assertIn(
            "../../topics/misc/native_handwrite_api.h.md",
            (self.js_root / "topics" / "misc" / "HandWrite.md").read_text(encoding="utf-8"),
        )

        index_lines = self.paths.js_index.read_text(encoding="utf-8").splitlines()
        self.assertIn("topics/misc/native_handwrite_api.h.md", index_lines)
        self.assertIn("topics/misc/HandWrite.md", index_lines)
        self.assertNotIn("capi/headers/native_handwrite_api.h.md", index_lines)
        references_index_lines = self.paths.references_index.read_text(encoding="utf-8").splitlines()
        self.assertIn("JsEtsAPIReference/topics/misc/native_handwrite_api.h.md", references_index_lines)
        self.assertIn("quickStart/intro.md", references_index_lines)

    def test_check_detects_index_drift(self) -> None:
        MODULE.rewrite_header_links(self.paths)
        self.paths.js_index.write_text("topics/misc/native_handwrite_api.h.md\n", encoding="utf-8")
        self.paths.references_index.write_text("quickStart/intro.md\n", encoding="utf-8")

        self.assertEqual(MODULE.check(self.paths), 1)

    def test_check_passes_after_generate(self) -> None:
        MODULE.rewrite_header_links(self.paths)
        MODULE.generate_references_index(self.paths)
        MODULE.generate_index(self.paths)

        self.assertEqual(MODULE.check(self.paths), 0)

    def test_classify_residual_detects_actionable_table_entry(self) -> None:
        text = "| params | LoginWithHuaweiIDButtonParams | 是 |\n"
        classification = MODULE.classify_residual(
            text,
            "LoginWithHuaweiIDButtonParams",
            "loginComponentManager (华为账号登录组件管理).md#section4717249182518",
        )
        self.assertEqual(classification, "actionable_internal_link")

    def test_classify_residual_ignores_code_only_occurrence(self) -> None:
        text = "```ets\nlet value: retrieval.RetrievalConfig = {}\n```\n"
        classification = MODULE.classify_residual(
            text,
            "retrieval.RetrievalConfig",
            "retrieval（检索器）.md#section95236010016",
        )
        self.assertEqual(classification, "code_or_signature_false_positive")

    def test_classify_residual_marks_external_and_guides_targets(self) -> None:
        self.assertEqual(
            MODULE.classify_residual("AppGallery Connect", "AppGallery Connect", "https://example.com/foo.md"),
            "external_link",
        )
        self.assertEqual(
            MODULE.classify_residual("collections类型", "collections类型", "../../guides/模块描述.md"),
            "historical_missing_guides_link",
        )


if __name__ == "__main__":
    unittest.main()
