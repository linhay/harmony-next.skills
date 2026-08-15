from __future__ import annotations

import shutil
import sys
import tempfile
import unittest
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = SKILL_ROOT.parent
SCRIPT_ROOT = SKILL_ROOT / "scripts"
sys.path.insert(0, str(SCRIPT_ROOT))

import check_packaging_docs  # noqa: E402


class PackagingDocsTests(unittest.TestCase):
    def test_packaging_docs_do_not_drift(self) -> None:
        errors = check_packaging_docs.check(REPO_ROOT)
        self.assertEqual(errors, [])

    def test_missing_smoke_set_is_reported_as_error(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = self.copy_minimal_fixture(Path(temp_dir))
            (root / "docs-linhay" / "spaces" / "20260706-ponytail-portability-plan" / "smoke-set.md").unlink()

            errors = check_packaging_docs.check(root)

        self.assertIn("missing smoke-set.md", errors)

    def test_readme_install_command_drift_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = self.copy_minimal_fixture(Path(temp_dir))
            readme = root / "README.md"
            readme.write_text(
                readme.read_text(encoding="utf-8").replace(
                    "npx skills add linhay/harmony-next.skills --skill harmony-next -a codex -g -y --copy",
                    "npx skills add linhay/harmony-next.skills -a codex -g -y --copy",
                ),
                encoding="utf-8",
            )

            errors = check_packaging_docs.check(root)

        self.assertTrue(any("README.md missing" in error and "--skill harmony-next -a codex" in error for error in errors))

    def test_smoke_case_missing_validation_fragment_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = self.copy_minimal_fixture(Path(temp_dir))
            smoke = root / "docs-linhay" / "spaces" / "20260706-ponytail-portability-plan" / "smoke-set.md"
            smoke.write_text(smoke.read_text(encoding="utf-8").replace("capture-audit", "capture audit"), encoding="utf-8")

            errors = check_packaging_docs.check(root)

        self.assertIn("smoke-set.md Offline UI/UX Audit missing: capture-audit", errors)

    def copy_minimal_fixture(self, root: Path) -> Path:
        for relative in [
            "README.md",
            "README_en.md",
            "package.json",
            "cordis.patch.yml",
            "index.js",
            "docs/agent-portability.md",
            "docs-linhay/spaces/20260706-ponytail-portability-plan/smoke-set.md",
            "harmony-next/SKILL.md",
        ]:
            source = REPO_ROOT / relative
            target = root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)

        for paths, _fragments in [(paths, fragments) for _title, paths, fragments in check_packaging_docs.SMOKE_CASES]:
            for relative in paths:
                source = REPO_ROOT / relative
                target = root / relative
                if target.exists():
                    continue
                target.parent.mkdir(parents=True, exist_ok=True)
                if source.is_file():
                    shutil.copy2(source, target)
                else:
                    target.write_text("# fixture\n", encoding="utf-8")
        return root


if __name__ == "__main__":
    unittest.main()
