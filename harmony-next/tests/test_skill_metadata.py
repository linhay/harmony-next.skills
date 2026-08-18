from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
SKILL_PATH = SKILL_ROOT / "SKILL.md"
EMULATOR_PLAYBOOK_PATH = SKILL_ROOT / "references" / "ideGuides" / "DevEco模拟器私有接口与AI自动化.md"
WEBVIEW_CDP_GUIDE_PATH = SKILL_ROOT / "references" / "ideGuides" / "ArkWeb WebView CDP调试与字段到达证明.md"
EMPTY_ABILITY_TEMPLATE_ROOT = SKILL_ROOT / "references" / "templates" / "empty-ability-app"
MINIMAL_SCAFFOLD_DOC_PATH = SKILL_ROOT / "references" / "quickStart" / "ets" / "minimal-project-scaffold.md"
SCRIPT_ROOT = SKILL_ROOT / "scripts"
sys.path.insert(0, str(SCRIPT_ROOT))

import sync_release_version  # noqa: E402
import package_skill  # noqa: E402


def find_repo_root(skill_root: Path) -> Path | None:
    for candidate in [skill_root.parent, *skill_root.parents]:
        if (candidate / "README.md").is_file() and (candidate / "README_en.md").is_file():
            return candidate
    return None


REPO_ROOT = find_repo_root(SKILL_ROOT)
README_PATH = REPO_ROOT / "README.md" if REPO_ROOT else None
README_EN_PATH = REPO_ROOT / "README_en.md" if REPO_ROOT else None
PORTABILITY_PATH = REPO_ROOT / "docs" / "agent-portability.md" if REPO_ROOT else None
PACKAGE_PATH = REPO_ROOT / "package.json" if REPO_ROOT else None


class SkillMetadataTests(unittest.TestCase):
    def setUp(self) -> None:
        self.skill_text = SKILL_PATH.read_text(encoding="utf-8")
        self.readme_text = README_PATH.read_text(encoding="utf-8") if README_PATH else None
        self.readme_en_text = README_EN_PATH.read_text(encoding="utf-8") if README_EN_PATH else None
        self.portability_text = PORTABILITY_PATH.read_text(encoding="utf-8") if PORTABILITY_PATH else None
        self.package_text = PACKAGE_PATH.read_text(encoding="utf-8") if PACKAGE_PATH else None
        self.emulator_playbook_text = EMULATOR_PLAYBOOK_PATH.read_text(encoding="utf-8")
        self.webview_cdp_guide_text = WEBVIEW_CDP_GUIDE_PATH.read_text(encoding="utf-8")
        self.minimal_scaffold_text = MINIMAL_SCAFFOLD_DOC_PATH.read_text(encoding="utf-8")

    def require_repo_root(self) -> Path:
        if REPO_ROOT is None:
            self.skipTest("repository-level README files are not available in this skill installation")
        return REPO_ROOT

    def require_readmes(self) -> tuple[str, str]:
        if self.readme_text is None or self.readme_en_text is None:
            self.skipTest("repository-level README files are not available in this skill installation")
        return self.readme_text, self.readme_en_text

    def require_portability(self) -> str:
        if self.portability_text is None:
            self.skipTest("repository-level portability documentation is not available in this skill installation")
        return self.portability_text

    def require_dsh_bundle(self) -> tuple[Path, str]:
        if REPO_ROOT is None or self.package_text is None:
            self.skipTest("repository-level DSH bundle files are not available in this skill installation")
        return REPO_ROOT, self.package_text

    def test_dsh_filesystem_skill_contract(self) -> None:
        self.assertEqual(SKILL_ROOT.name, "harmony-next")
        self.assertEqual(SKILL_PATH.relative_to(SKILL_ROOT.parent).as_posix(), "harmony-next/SKILL.md")
        self.assertRegex(SKILL_ROOT.name, r"^[a-z0-9]+(?:-[a-z0-9]+)*$")

        frontmatter = re.match(r"\A---\n(?P<body>.*?)\n---\n", self.skill_text, re.DOTALL)
        self.assertIsNotNone(frontmatter)
        assert frontmatter is not None
        body = frontmatter.group("body")
        name = re.search(r"(?m)^name:\s*([a-z0-9]+(?:-[a-z0-9]+)*)\s*$", body)
        description = re.search(r"(?m)^description:\s*(\S.*)$", body)
        self.assertIsNotNone(name)
        self.assertIsNotNone(description)
        assert name is not None
        assert description is not None
        self.assertEqual(name.group(1), SKILL_ROOT.name)
        self.assertTrue(description.group(1).strip())

    def test_readmes_document_dsh_filesystem_installation(self) -> None:
        readme_text, readme_en_text = self.require_readmes()
        portability_text = self.require_portability()
        required_readme_fragments = [
            "DeepSeek Harness",
            "dsh plugin --profile demo add github:linhay/harmony-next.skills",
            "dsh-harmony-next",
            "DSH_SOURCE=/path/to/harmony-next.skills",
            ".dsh/skills/harmony-next",
            "filesystem skill",
            "不安装 MCP、tools 或 apps",
        ]
        required_readme_en_fragments = [
            "DeepSeek Harness (DSH)",
            "dsh plugin --profile demo add github:linhay/harmony-next.skills",
            "dsh-harmony-next",
            "DSH_SOURCE=/path/to/harmony-next.skills",
            ".dsh/skills/harmony-next",
            "filesystem skill",
            "does not install MCP servers, tools, or apps",
        ]
        required_portability_fragments = [
            "dsh-skill-filesystem",
            "$HOME/.dsh/skills/harmony-next",
            "$DSH_HOME/skills/harmony-next",
            "dsh.bundle.patch",
            "Verified on 2026-08-15 with `@deepseek-ai/dsh@",
        ]

        for fragment in required_readme_fragments:
            with self.subTest(readme_fragment=fragment):
                self.assertIn(fragment, readme_text)
        for fragment in required_readme_en_fragments:
            with self.subTest(readme_en_fragment=fragment):
                self.assertIn(fragment, readme_en_text)
        for fragment in required_portability_fragments:
            with self.subTest(portability_fragment=fragment):
                self.assertIn(fragment, portability_text)

    def test_dsh_bundle_manifest_contract(self) -> None:
        repo_root, package_text = self.require_dsh_bundle()
        manifest = json.loads(package_text)
        skill_version = re.search(r'version:\s*"(\d+\.\d+\.\d+)"', self.skill_text)
        self.assertIsNotNone(skill_version)
        assert skill_version is not None

        self.assertEqual(manifest["name"], "dsh-harmony-next")
        self.assertEqual(manifest["version"], skill_version.group(1))
        self.assertEqual(manifest["dsh"]["bundle"]["patch"], "./cordis.patch.yml")
        for included in ["index.js", "cordis.patch.yml", "harmony-next/SKILL.md", "harmony-next/references/**"]:
            with self.subTest(included=included):
                self.assertIn(included, manifest["files"])

        patch_text = (repo_root / "cordis.patch.yml").read_text(encoding="utf-8")
        provider_text = (repo_root / "index.js").read_text(encoding="utf-8")
        self.assertIn("id: harmony-next-skill", patch_text)
        self.assertIn("name: dsh-harmony-next", patch_text)
        self.assertIn("harmony-next/SKILL.md", provider_text)
        self.assertIn("resourceBase", provider_text)
        self.assertIn("ctx.skills.registerProvider", provider_text)

    def test_find_repo_root_supports_agents_skill_install_path(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir)
            skill_root = repo_root / ".agents" / "skills" / "harmony-next"
            skill_root.mkdir(parents=True)
            (repo_root / "README.md").write_text("# zh\n", encoding="utf-8")
            (repo_root / "README_en.md").write_text("# en\n", encoding="utf-8")

            self.assertEqual(find_repo_root(skill_root), repo_root)

    def test_skill_resolves_paths_from_loaded_skill_md(self) -> None:
        required_fragments = [
            "HARMONY_NEXT_SKILL_DIR",
            'HARMONY_NEXT_SKILL_DIR="<skill-dir>"',
            "$HARMONY_NEXT_SKILL_DIR/references/INDEX.md",
            'python3 "$HARMONY_NEXT_SKILL_DIR/scripts/hvd_manager.py" doctor --json',
            "$REPO_ROOT/.agents/skills/harmony-next",
        ]
        forbidden_fragments = [
            "From the repository root, use `harmony-next/references/",
            "python3 harmony-next/scripts/hvd_manager.py",
            "python3 harmony-next/scripts/commandline_tools_manager.py",
        ]

        for fragment in required_fragments:
            with self.subTest(required=fragment):
                self.assertIn(fragment, self.skill_text)
        for fragment in forbidden_fragments:
            with self.subTest(forbidden=fragment):
                self.assertNotIn(fragment, self.skill_text)

        with tempfile.TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir)
            skill_dir = repo_root / ".agents" / "skills" / "harmony-next"
            (skill_dir / "references").mkdir(parents=True)
            (skill_dir / "scripts").mkdir(parents=True)
            shutil.copy2(SKILL_PATH, skill_dir / "SKILL.md")
            shutil.copy2(SKILL_ROOT / "references" / "INDEX.md", skill_dir / "references" / "INDEX.md")
            shutil.copy2(SKILL_ROOT / "scripts" / "hvd_manager.py", skill_dir / "scripts" / "hvd_manager.py")

            env = {
                **os.environ,
                "HARMONY_NEXT_SKILL_DIR": str(skill_dir),
                "HARMONY_NEXT_PYTHON": sys.executable,
            }
            self.assertFalse((repo_root / "harmony-next" / "references" / "INDEX.md").exists())
            self.assertFalse((repo_root / "harmony-next" / "scripts" / "hvd_manager.py").exists())
            self.assertTrue((Path(env["HARMONY_NEXT_SKILL_DIR"]) / "references" / "INDEX.md").is_file())
            self.assertTrue((Path(env["HARMONY_NEXT_SKILL_DIR"]) / "scripts" / "hvd_manager.py").is_file())
            self.assertTrue((Path(env["HARMONY_NEXT_SKILL_DIR"]) / "SKILL.md").is_file())

            shell = shutil.which("sh")
            self.assertIsNotNone(shell)
            assert shell is not None

            help_result = subprocess.run(
                [
                    shell,
                    "-c",
                    '"$HARMONY_NEXT_PYTHON" "$HARMONY_NEXT_SKILL_DIR/scripts/hvd_manager.py" --help',
                ],
                cwd=repo_root,
                env=env,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(help_result.returncode, 0, help_result.stderr)
            self.assertIn("Manage local DevEco HarmonyOS HVD instances", help_result.stdout)

            rg = shutil.which("rg")
            if rg:
                env["HARMONY_NEXT_RG"] = rg
                lookup_result = subprocess.run(
                    [
                        shell,
                        "-c",
                        '"$HARMONY_NEXT_RG" -n "UIAbility|AbilityStage|Want" '
                        '"$HARMONY_NEXT_SKILL_DIR/references/INDEX.md"',
                    ],
                    cwd=repo_root,
                    env=env,
                    capture_output=True,
                    text=True,
                    check=False,
                )
                self.assertEqual(lookup_result.returncode, 0, lookup_result.stderr)
                self.assertIn("UIAbility", lookup_result.stdout)

    def test_bundled_playbooks_do_not_use_repo_root_skill_commands(self) -> None:
        forbidden_fragments = [
            "python3 harmony-next/scripts/",
            "cp -R harmony-next/references/",
        ]

        for path in sorted((SKILL_ROOT / "references").rglob("*.md")):
            text = path.read_text(encoding="utf-8")
            for fragment in forbidden_fragments:
                with self.subTest(path=path.relative_to(SKILL_ROOT), forbidden=fragment):
                    self.assertNotIn(fragment, text)

    def test_skill_exposes_current_version_for_agents(self) -> None:
        metadata_version = re.search(r"version:\s*\"(\d+\.\d+\.\d+)\"", self.skill_text)
        visible_version = re.search(r"Current local skill version:\s*`v\d+\.\d+\.\d+`", self.skill_text)
        hidden_version = re.search(r"<!-- version:\s*(\d+\.\d+\.\d+)\s*-->", self.skill_text)

        self.assertIsNotNone(metadata_version)
        self.assertIsNotNone(visible_version)
        self.assertIsNotNone(hidden_version)
        self.assertEqual(metadata_version.group(1), hidden_version.group(1))
        self.assertIn(f"`v{metadata_version.group(1)}`", visible_version.group(0))

    def test_readme_release_badges_match_skill_version(self) -> None:
        readme_text, readme_en_text = self.require_readmes()
        for text in [readme_text, readme_en_text]:
            with self.subTest(readme=text[:20]):
                self.assertIn(
                    "https://img.shields.io/github/v/release/linhay/harmony-next.skills?style=flat-square",
                    text,
                )
                self.assertIn("https://github.com/linhay/harmony-next.skills/releases/latest", text)

    def test_readmes_have_language_switches(self) -> None:
        readme_text, readme_en_text = self.require_readmes()
        self.assertIn("readme-English", readme_text)
        self.assertIn("(./README_en.md)", readme_text)
        self.assertIn("readme-中文", readme_en_text)
        self.assertIn("(./README.md)", readme_en_text)

    def test_readmes_document_official_codex_skill_locations(self) -> None:
        readme_text, readme_en_text = self.require_readmes()
        required_readme_fragments = [
            "npx skills add linhay/harmony-next.skills",
            "npx skills add linhay/harmony-next.skills --list",
            "npx skills add linhay/harmony-next.skills --skill harmony-next -a claude-code -g -y --copy",
            "npx skills add linhay/harmony-next.skills --skill harmony-next -a codex -g -y --copy",
            "https://skills.sh/b/linhay/harmony-next.skills",
            "https://skills.sh/linhay/harmony-next.skills",
            "$HOME/.agents/skills/harmony-next",
            "本仓库当前还不是 Codex plugin",
        ]
        required_readme_en_fragments = [
            "npx skills add linhay/harmony-next.skills",
            "npx skills add linhay/harmony-next.skills --list",
            "npx skills add linhay/harmony-next.skills --skill harmony-next -a claude-code -g -y --copy",
            "npx skills add linhay/harmony-next.skills --skill harmony-next -a codex -g -y --copy",
            "https://skills.sh/b/linhay/harmony-next.skills",
            "https://skills.sh/linhay/harmony-next.skills",
            "$HOME/.agents/skills/harmony-next",
            "not currently packaged as a Codex plugin",
        ]

        for fragment in required_readme_fragments:
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, readme_text)
        for fragment in required_readme_en_fragments:
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, readme_en_text)

    def test_skill_documents_freshness_and_installation_paths(self) -> None:
        required_fragments = [
            "Reference snapshot:",
            "not live web docs",
            "GitHub Releases or nightly",
            "Huawei online docs",
            "Install/update entrypoints:",
            "Vercel Labs skills CLI",
            "npx skills add linhay/harmony-next.skills --skill harmony-next",
            "npx skills add linhay/harmony-next.skills --skill harmony-next -a claude-code -g -y --copy",
            "npx skills add linhay/harmony-next.skills --skill harmony-next -a codex -g -y --copy",
            "gemini skills install",
            "Claude.ai",
            "Claude Code",
            "Codex",
            "$REPO_ROOT/.agents/skills/harmony-next",
            "$HOME/.agents/skills/harmony-next",
            "/etc/codex/skills/harmony-next",
            "package it as a Codex plugin",
        ]

        for fragment in required_fragments:
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, self.skill_text)

    def test_emulator_automation_policy_is_non_interactive(self) -> None:
        readme_text, readme_en_text = self.require_readmes()
        required_skill_fragments = [
            "HARMONY_NEXT_AUTOMATION_POLICY",
            "readonly",
            "evidence",
            "automation",
            "diagnostic",
            "break-glass",
            "blocked",
            "missingConfig",
            "requiredMode",
            "用户默认拥有完整执行权限",
        ]
        required_playbook_fragments = [
            "## 自动化策略模型",
            "riskLevel",
            "policy",
            "operation",
            "target",
            "artifacts",
            "redactionStatus",
            "sourceCommand",
            "artifactDir",
            ".harmony-next-policy.json",
            "--policy <readonly|evidence|automation|diagnostic|break-glass>",
            "HARMONY_NEXT_AUTOMATION_POLICY",
            "blocked",
            "missingConfig",
            "requiredMode",
            "break-glass",
            "用户默认拥有完整执行权限",
            "不是权限不足",
        ]
        required_readme_fragments = [
            "必须先阅读对应的私有接口文档",
            "产物目录",
            "脱敏边界",
            "非交互模式",
        ]
        required_readme_en_fragments = [
            "must read the corresponding private-interface documents first",
            "artifact directories",
            "redaction boundaries",
            "non-interactive execution policy",
        ]
        forbidden_fragments = [
            "需要用户确认",
            "人工确认",
            "预授权",
            "human confirmation",
            "authorization gate",
            "forbidden",
            "requiredPolicy",
        ]

        for fragment in required_skill_fragments:
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, self.skill_text)
        for fragment in required_playbook_fragments:
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, self.emulator_playbook_text)
        for fragment in required_readme_fragments:
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, readme_text)
        for fragment in required_readme_en_fragments:
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, readme_en_text)
        for fragment in forbidden_fragments:
            with self.subTest(fragment=fragment):
                self.assertNotIn(fragment, self.skill_text)
                self.assertNotIn(fragment, self.emulator_playbook_text)

    def test_tooling_script_skills_are_routed_and_documented(self) -> None:
        required_skill_fragments = [
            "## Tooling Script Skills",
            "`commandline_tools_manager.py`",
            "`hvd_manager.py`",
            "Agent first command",
            "User handoff",
            "launch --name <hvd> --image-root <dir> --trace-name <name>",
            "download center page URL",
            "HVD image download",
            "device_ui_action.py",
            "webview-devtools",
            "emulator_kernel_panic",
        ]
        required_emulator_fragments = [
            "## HVD 管理 CLI",
            "先运行 `doctor --json`",
            "跨机器分发",
            "HARMONY_HVD_ROOT",
            "socketConnected=true",
            "traceBytesRead",
            "emulator.launch",
            "download-image",
            "## 生命周期模型",
            "attached 生命周期核查表",
            "Emulator -stop",
            "detached",
            "WebView DevTools 与 CDP 字段证明",
        ]

        for fragment in required_skill_fragments:
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, self.skill_text)
        for fragment in required_emulator_fragments:
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, self.emulator_playbook_text)

    def test_webview_cdp_field_arrival_workflow_is_bounded(self) -> None:
        required_skill_fragments = [
            "ArkWeb/WebView DevTools",
            "Runtime.evaluate",
            "awaitPromise=true",
            "returnByValue=true",
            "Page.captureScreenshot",
            "device_evidence_bundle.py webview-devtools",
            "device_ui_action.py tap",
        ]
        required_guide_fragments = [
            "TritonKit",
            "Runtime.evaluate",
            '"awaitPromise": true',
            '"returnByValue": true',
            "bridge callback JSON",
            "Page.captureScreenshot",
            "foregroundEvidenceValid=false",
            "webview_socket_not_found",
            "devtools_http_reset",
        ]

        for fragment in required_skill_fragments:
            with self.subTest(skill_fragment=fragment):
                self.assertIn(fragment, self.skill_text)
        for fragment in required_guide_fragments:
            with self.subTest(guide_fragment=fragment):
                self.assertIn(fragment, self.webview_cdp_guide_text)

    def test_release_workflow_uses_skill_zip_asset(self) -> None:
        repo_root = self.require_repo_root()
        workflow_path = repo_root / ".github" / "workflows" / "release.yml"
        if not workflow_path.is_file():
            self.skipTest("release workflow is not available in this skill installation")
        workflow_text = workflow_path.read_text(encoding="utf-8")

        self.assertIn("harmony-next.skill.zip", workflow_text)
        self.assertIn("package_skill.py", workflow_text)
        self.assertIn("node --check index.js", workflow_text)
        self.assertIn("npm pack --dry-run --json", workflow_text)
        self.assertNotIn("harmony-next.skill\n", workflow_text)

    def test_package_skill_includes_build_info_and_issue_guide(self) -> None:
        repo_root = self.require_repo_root()
        if not (repo_root / ".git").exists():
            self.skipTest("git metadata is not available in this skill installation")
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "harmony-next.skill.zip"
            payload = package_skill.package_skill(repo_root, SKILL_ROOT, output, release_tag="v9.9.9")

            self.assertTrue(output.is_file())
            self.assertEqual(payload["buildInfo"]["name"], "harmony-next")
            self.assertEqual(payload["buildInfo"]["releaseTag"], "v9.9.9")

            with zipfile.ZipFile(output) as archive:
                names = set(archive.namelist())
                self.assertIn("SKILL.md", names)
                self.assertIn("ISSUE_GUIDE.md", names)
                self.assertIn("BUILD_INFO.json", names)
                build_info = json.loads(archive.read("BUILD_INFO.json").decode("utf-8"))
                issue_guide = archive.read("ISSUE_GUIDE.md").decode("utf-8")

            metadata_version = re.search(r"version:\s*\"(\d+\.\d+\.\d+)\"", self.skill_text)
            self.assertIsNotNone(metadata_version)
            self.assertEqual(build_info["version"], metadata_version.group(1))
            self.assertRegex(build_info["git"]["commit"], r"^[0-9a-f]{40}$")
            self.assertRegex(build_info["git"]["shortCommit"], r"^[0-9a-f]{7}$")
            self.assertIn("gh issue create --repo linhay/harmony-next.skills", issue_guide)
            self.assertIn("hvd_manager.py doctor --json", issue_guide)

    def test_emulator_proxy_capture_guidance_is_external_user_facing(self) -> None:
        readme_text, readme_en_text = self.require_readmes()
        required_skill_fragments = [
            "simulator traffic capture",
            "HTTP proxy tools",
            "NetworkKit proxy routing",
            "transparent interception",
        ]
        required_playbook_fragments = [
            "## 模拟器抓包与代理诊断",
            "面向使用者",
            "10.0.2.15",
            "10.0.2.2",
            "显式 HTTP 代理",
            "抓包工具",
            "setAppHttpProxy",
            "usingProxy: true",
            "Mac 侧中转脚本",
            "不能透明接管全部流量",
            "Emulator -http_proxy",
            "WidgetNetworkProxy",
            "管理器代理",
            "certificateManagerDialog",
            "caData",
            "iOS 模拟器式",
            "VpnExtension",
            "调试目标应用",
        ]
        required_readme_fragments = [
            "抓包诊断",
            "DevEco 模拟器自动化",
        ]
        required_readme_en_fragments = [
            "proxy diagnostics",
            "DevEco Emulator automation",
        ]

        for fragment in required_skill_fragments:
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, self.skill_text)
        for fragment in required_playbook_fragments:
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, self.emulator_playbook_text)
        for fragment in required_readme_fragments:
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, readme_text)
        for fragment in required_readme_en_fragments:
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, readme_en_text)

    def test_empty_ability_template_is_copyable_for_smoke_tests(self) -> None:
        readme_text, readme_en_text = self.require_readmes()
        required_paths = [
            "README.md",
            "oh-package.json5",
            "package.json",
            "build-profile.json5",
            "hvigorfile.ts",
            "hvigor/hvigor-config.json5",
            "AppScope/app.json5",
            "AppScope/resources/base/element/string.json",
            "AppScope/resources/base/media/app_icon.png",
            "entry/oh-package.json5",
            "entry/build-profile.json5",
            "entry/hvigorfile.ts",
            "entry/src/main/module.json5",
            "entry/src/main/ets/entryability/EntryAbility.ets",
            "entry/src/main/ets/components/SmokeCounter.ets",
            "entry/src/main/ets/pages/Index.ets",
            "entry/src/main/resources/base/element/color.json",
            "entry/src/main/resources/base/element/float.json",
            "entry/src/main/resources/base/element/string.json",
            "entry/src/main/resources/base/profile/main_pages.json",
        ]
        required_fragments = [
            "references/templates/empty-ability-app",
            "com.example.emptyability",
            "EntryAbility",
            "5.0.0(12)",
            "6.0.2(22)",
            "DEVECO_SDK_HOME=/Applications/DevEco-Studio.app/Contents/sdk",
            "ohpm install",
            "hvigorw --mode module",
            "startWindowIcon",
            "uitest dumpLayout",
            "uitest uiInput click",
            "Harmony Smoke Tapped",
            "smoke-increment",
            "SmokeCounter",
        ]
        required_readme_fragments = [
            "references/templates/empty-ability-app",
            "empty-ability-app",
            "smoke fixture",
            "Codex plugin",
        ]
        required_readme_en_fragments = [
            "references/templates/empty-ability-app",
            "empty-ability-app",
            "smoke fixture",
            "Codex plugin",
        ]

        for relative_path in required_paths:
            with self.subTest(path=relative_path):
                self.assertTrue((EMPTY_ABILITY_TEMPLATE_ROOT / relative_path).is_file())

        app_json = json.loads((EMPTY_ABILITY_TEMPLATE_ROOT / "AppScope" / "app.json5").read_text(encoding="utf-8"))
        module_json = json.loads((EMPTY_ABILITY_TEMPLATE_ROOT / "entry" / "src" / "main" / "module.json5").read_text(encoding="utf-8"))
        build_profile = json.loads((EMPTY_ABILITY_TEMPLATE_ROOT / "build-profile.json5").read_text(encoding="utf-8"))
        main_pages = json.loads(
            (EMPTY_ABILITY_TEMPLATE_ROOT / "entry" / "src" / "main" / "resources" / "base" / "profile" / "main_pages.json").read_text(
                encoding="utf-8"
            )
        )

        self.assertEqual(app_json["app"]["bundleName"], "com.example.emptyability")
        self.assertEqual(app_json["app"]["icon"], "$media:app_icon")
        self.assertEqual(module_json["module"]["name"], "entry")
        self.assertEqual(module_json["module"]["mainElement"], "EntryAbility")
        self.assertEqual(module_json["module"]["abilities"][0]["srcEntry"], "./ets/entryability/EntryAbility.ets")
        self.assertEqual(module_json["module"]["abilities"][0]["icon"], "$media:app_icon")
        self.assertEqual(module_json["module"]["abilities"][0]["startWindowIcon"], "$media:app_icon")
        self.assertEqual(main_pages["src"], ["pages/Index"])
        self.assertEqual(build_profile["app"]["products"][0]["compatibleSdkVersion"], "5.0.0(12)")
        self.assertEqual(build_profile["app"]["products"][0]["targetSdkVersion"], "5.0.0(12)")
        self.assertEqual(build_profile["app"]["products"][0]["runtimeOS"], "HarmonyOS")
        self.assertEqual(build_profile["app"]["signingConfigs"], [])

        index_text = (EMPTY_ABILITY_TEMPLATE_ROOT / "entry" / "src" / "main" / "ets" / "pages" / "Index.ets").read_text(
            encoding="utf-8"
        )
        smoke_counter_text = (
            EMPTY_ABILITY_TEMPLATE_ROOT / "entry" / "src" / "main" / "ets" / "components" / "SmokeCounter.ets"
        ).read_text(encoding="utf-8")
        self.assertIn("import { SmokeCounter } from '../components/SmokeCounter';", index_text)
        self.assertIn("SmokeCounter()", index_text)
        self.assertNotIn("@State", index_text)
        self.assertIn("export struct SmokeCounter", smoke_counter_text)
        self.assertIn("@State message: string = 'Harmony Smoke Ready';", smoke_counter_text)
        self.assertIn(".id('smoke-increment')", smoke_counter_text)

        for path in EMPTY_ABILITY_TEMPLATE_ROOT.rglob("*"):
            if path.is_file():
                if path.suffix == ".png":
                    continue
                text = path.read_text(encoding="utf-8")
                with self.subTest(path=path.relative_to(EMPTY_ABILITY_TEMPLATE_ROOT).as_posix()):
                    self.assertNotIn("${", text)
                    self.assertNotIn("/Users/", text)
                    self.assertNotIn("certpath", text)
                    self.assertNotIn("storePassword", text)
                    self.assertNotIn("keyPassword", text)

        for fragment in required_fragments:
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, self.minimal_scaffold_text)
                self.assertIn(fragment, self.skill_text)

        for fragment in required_readme_fragments:
            with self.subTest(readme_fragment=fragment):
                self.assertIn(fragment, readme_text)

        for fragment in required_readme_en_fragments:
            with self.subTest(readme_en_fragment=fragment):
                self.assertIn(fragment, readme_en_text)

        self.assertIn("页面入口与 smoke 组件解耦", self.minimal_scaffold_text)
        self.assertIn("Route/component split", self.skill_text)

    def test_sync_release_version_updates_skill_and_readmes(self) -> None:
        self.require_readmes()
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            (temp_root / "harmony-next").mkdir()
            shutil.copy2(SKILL_PATH, temp_root / "harmony-next" / "SKILL.md")
            assert PACKAGE_PATH is not None
            shutil.copy2(PACKAGE_PATH, temp_root / "package.json")
            assert README_PATH is not None
            assert README_EN_PATH is not None
            shutil.copy2(README_PATH, temp_root / "README.md")
            shutil.copy2(README_EN_PATH, temp_root / "README_en.md")

            bare_version, tag_version = sync_release_version.sync_release_version(temp_root, "v9.8.7")

            self.assertEqual(bare_version, "9.8.7")
            self.assertEqual(tag_version, "v9.8.7")
            self.assertEqual(json.loads((temp_root / "package.json").read_text(encoding="utf-8"))["version"], "9.8.7")
            self.assertIn('version: "9.8.7"', (temp_root / "harmony-next" / "SKILL.md").read_text(encoding="utf-8"))
            self.assertIn("Current local skill version: `v9.8.7`.", (temp_root / "harmony-next" / "SKILL.md").read_text(encoding="utf-8"))
            self.assertIn("<!-- version: 9.8.7 -->", (temp_root / "harmony-next" / "SKILL.md").read_text(encoding="utf-8"))
            self.assertIn(
                "https://img.shields.io/github/v/release/linhay/harmony-next.skills?style=flat-square",
                (temp_root / "README.md").read_text(encoding="utf-8"),
            )
            self.assertIn(
                "https://github.com/linhay/harmony-next.skills/releases/latest",
                (temp_root / "README_en.md").read_text(encoding="utf-8"),
            )
            self.assertIn("| `v9.8.7` |", (temp_root / "README.md").read_text(encoding="utf-8"))
            self.assertIn("| `v9.8.7` |", (temp_root / "README_en.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
