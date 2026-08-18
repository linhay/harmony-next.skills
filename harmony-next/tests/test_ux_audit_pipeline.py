from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "ux_audit_pipeline.py"


class UxAuditPipelineTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.ux_root = self.root / "UxTestService"
        self.remote_root = self.root / "remote"
        self.remote_root.mkdir()
        self.fake_hdc = self.root / "hdc"
        self.env = {**os.environ, "FAKE_HDC_REMOTE_ROOT": str(self.remote_root)}
        self.create_fake_ux_service(self.ux_root)
        self.create_fake_hdc(self.fake_hdc)

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def create_fake_ux_service(self, root: Path) -> None:
        (root / "checkMethod").mkdir(parents=True)
        (root / "buildInfo.properties").write_text("fake-ux=1.0\n", encoding="utf-8")
        (root / "ux_detect.py").write_text(
            textwrap.dedent(
                """\
                from pathlib import Path

                def main(argument=None, check_param=None):
                    assert check_param["bundle_name"] == "com.example.emptyability"
                    image = check_param["page_infos"]["CAPTURE_PAGE"]["detail_infos"][0]["img_path"]
                    marked = str(Path(image).with_name("marked_issue.jpeg"))
                    Path(marked).write_bytes(b"JPEG")
                    return [
                        {
                            "code": "7.1.1.3.3",
                            "test_state": 1,
                            "reason": "点击热区过小",
                            "sub_rule_name": "点击热区大小",
                            "detail": {
                                "ErrorCode": "",
                                "ErrorType": "hot_area",
                                "ErrorMsg": "点击热区过小",
                                "Issues": [{"bounds": [0, 0, 10, 10]}],
                                "IssueComponents": [],
                                "PassPath": "",
                                "ErrorPath": marked,
                                "CustomDrawPath": "",
                            },
                        },
                        {
                            "code": "7.1.1.4.4",
                            "test_state": 0,
                            "reason": "",
                            "sub_rule_name": "界面图标大小",
                            "detail": {
                                "ErrorCode": "",
                                "ErrorType": "icon_size",
                                "ErrorMsg": "未发现相关问题",
                                "Issues": [],
                                "IssueComponents": [],
                                "PassPath": image,
                                "ErrorPath": "",
                                "CustomDrawPath": "",
                            },
                        },
                    ]
                """
            ),
            encoding="utf-8",
        )

    def create_fake_hdc(self, path: Path) -> None:
        path.write_text(
            textwrap.dedent(
                """\
                #!/usr/bin/env python3
                import json
                import os
                import shutil
                import sys
                from pathlib import Path

                args = sys.argv[1:]
                remote_root = Path(os.environ["FAKE_HDC_REMOTE_ROOT"])

                def remote_file(remote):
                    return remote_root / remote.strip("/").replace("/", "_")

                if args == ["-v"]:
                    print("Ver: 3.1.0")
                    sys.exit(0)
                if args[:2] == ["list", "targets"]:
                    print("127.0.0.1:10100 TCP Connected localhost")
                    sys.exit(0)
                if len(args) < 3 or args[0] != "-t":
                    print("unexpected args: " + " ".join(args), file=sys.stderr)
                    sys.exit(2)
                rest = args[2:]
                if rest[:2] == ["file", "recv"]:
                    src = remote_file(rest[2])
                    dst = Path(rest[3])
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copyfile(src, dst)
                    sys.exit(0)
                shell = rest[1:]
                if rest[0] != "shell":
                    print("unexpected target command", file=sys.stderr)
                    sys.exit(2)
                if shell[:3] == ["param", "get", "bootevent.boot.completed"]:
                    print("true")
                    sys.exit(0)
                if shell[:3] == ["bm", "dump", "-g"]:
                    print("Debug bundle: com.example.emptyability")
                    sys.exit(0)
                if shell[:3] == ["bm", "dump", "-n"]:
                    print("bundleName: " + shell[3])
                    sys.exit(0)
                if shell[:3] == ["aa", "dump", "-l"]:
                    print("AbilityRecord bundleName=com.example.emptyability")
                    sys.exit(0)
                if shell[:3] == ["aa", "dump", "-r"]:
                    print("Running ability")
                    sys.exit(0)
                if shell[:2] == ["hilog", "-z"]:
                    print("Harmony Smoke Ready")
                    sys.exit(0)
                if shell[:2] == ["uitest", "dumpLayout"]:
                    remote = shell[shell.index("-p") + 1]
                    remote_file(remote).write_text(
                        json.dumps(
                            {
                                "bundleName": "com.example.emptyability",
                                "type": "Window",
                                "children": [{"type": "Text", "bounds": "[0,0][100,40]"}],
                            }
                        ),
                        encoding="utf-8",
                    )
                    print("No Error")
                    sys.exit(0)
                if shell[:2] == ["uitest", "screenCap"]:
                    remote = shell[shell.index("-p") + 1]
                    remote_file(remote).write_bytes(b"\\x89PNG\\r\\n\\x1a\\nsynthetic")
                    print("No Error")
                    sys.exit(0)
                if shell[:2] == ["rm", "-f"]:
                    for remote in shell[2:]:
                        path = remote_file(remote)
                        if path.exists():
                            path.unlink()
                    print("removed")
                    sys.exit(0)
                print("unknown shell: " + " ".join(shell), file=sys.stderr)
                sys.exit(2)
                """
            ),
            encoding="utf-8",
        )
        path.chmod(0o755)

    def write_evidence_bundle(self, directory: Path, bundle: str = "com.example.emptyability") -> Path:
        directory.mkdir(parents=True)
        layout = directory / "layout.json"
        screen = directory / "screen.png"
        layout.write_text(
            json.dumps({"bundleName": bundle, "type": "Window", "children": [{"type": "Text", "bounds": "[0,0][1,1]"}]}),
            encoding="utf-8",
        )
        screen.write_bytes(b"\x89PNG\r\n\x1a\nsynthetic")
        summary = {
            "decision": "collected",
            "target": "127.0.0.1:10100",
            "bundle": None,
            "layoutSummary": {"available": True, "nodeCount": 2, "bundleNames": [bundle, "com.ohos.sceneboard"]},
            "artifacts": [
                {"kind": "layout", "path": str(layout), "exists": True},
                {"kind": "screenshot", "path": str(screen), "exists": True},
            ],
        }
        summary_path = directory / "summary.json"
        summary["summary"] = str(summary_path)
        summary_path.write_text(json.dumps(summary), encoding="utf-8")
        return summary_path

    def test_audit_existing_evidence_bundle(self) -> None:
        evidence_summary = self.write_evidence_bundle(self.root / "evidence")
        output_dir = self.root / "audit"

        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT_PATH),
                "audit",
                "--ux-service-root",
                str(self.ux_root),
                "--evidence-summary",
                str(evidence_summary),
                "--artifact-dir",
                str(output_dir),
                "--json",
            ],
            check=True,
            capture_output=True,
            text=True,
        )

        payload = json.loads(result.stdout)
        check_param = json.loads((output_dir / "check_param.json").read_text(encoding="utf-8"))
        ux_summary = json.loads((output_dir / "ux_summary.json").read_text(encoding="utf-8"))

        self.assertEqual(payload["decision"], "audited")
        self.assertEqual(payload["bundleName"], "com.example.emptyability")
        self.assertEqual(payload["feedback"]["repository"], "linhay/harmony-next.skills")
        self.assertEqual(payload["feedback"]["issueTemplate"], "offline-ux-audit.yml")
        self.assertIn("https://github.com/linhay/harmony-next.skills/issues/new", payload["feedback"]["issueUrl"])
        self.assertIn("template=offline-ux-audit.yml", payload["feedback"]["issueUrl"])
        self.assertEqual(check_param["extend_infos"]["language"], "zh")
        self.assertEqual(ux_summary["counts"], {"1": 1, "0": 1})
        self.assertTrue((output_dir / "ux_result.json").is_file())
        self.assertTrue((output_dir / "report.md").is_file())
        report = (output_dir / "report.md").read_text(encoding="utf-8")
        self.assertIn("## Feedback", report)
        self.assertIn("offline-ux-audit.yml", report)
        self.assertTrue((output_dir / "ux_service_runtime" / "ux_detect.py").is_file())

    def test_capture_audit_runs_end_to_end(self) -> None:
        output_dir = self.root / "pipeline"

        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT_PATH),
                "capture-audit",
                "--hdc",
                str(self.fake_hdc),
                "--ux-service-root",
                str(self.ux_root),
                "--target",
                "127.0.0.1:10100",
                "--artifact-dir",
                str(output_dir),
                "--json",
            ],
            check=True,
            capture_output=True,
            text=True,
            env=self.env,
        )

        payload = json.loads(result.stdout)
        self.assertEqual(payload["decision"], "completed")
        self.assertEqual(payload["bundleName"], "com.example.emptyability")
        self.assertEqual(payload["resultCounts"], {"1": 1, "0": 1})
        self.assertEqual(payload["feedback"]["repository"], "linhay/harmony-next.skills")
        self.assertTrue((output_dir / "capture" / "summary.json").is_file())
        self.assertTrue((output_dir / "audit" / "summary.json").is_file())
        self.assertTrue((output_dir / "summary.json").is_file())

    def test_audit_blocks_when_bundle_cannot_be_inferred(self) -> None:
        evidence_summary = self.write_evidence_bundle(self.root / "evidence", bundle="")
        output_dir = self.root / "audit"

        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT_PATH),
                "audit",
                "--ux-service-root",
                str(self.ux_root),
                "--evidence-summary",
                str(evidence_summary),
                "--artifact-dir",
                str(output_dir),
                "--json",
            ],
            check=False,
            capture_output=True,
            text=True,
        )

        payload = json.loads(result.stdout)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(payload["decision"], "blocked")
        self.assertIn("bundleName", payload["missingConfig"])
        self.assertEqual(payload["feedback"]["repository"], "linhay/harmony-next.skills")

    def test_audit_blocks_with_json_when_evidence_summary_is_missing(self) -> None:
        missing_summary = self.root / "missing-summary.json"
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT_PATH),
                "audit",
                "--ux-service-root",
                str(self.ux_root),
                "--evidence-summary",
                str(missing_summary),
                "--json",
            ],
            check=False,
            capture_output=True,
            text=True,
        )

        payload = json.loads(result.stdout)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(payload["decision"], "blocked")
        self.assertIn("evidenceSummary", payload["missingConfig"])
        self.assertEqual(payload["jsonPath"], str(missing_summary.resolve()))
        self.assertIn("official HarmonyOS CLI", " ".join(payload["recommendations"]))
        self.assertEqual(result.stderr, "")

    def test_audit_blocks_with_json_when_evidence_summary_is_malformed(self) -> None:
        bad_summary = self.root / "bad-summary.json"
        bad_summary.write_text("{not json", encoding="utf-8")
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT_PATH),
                "audit",
                "--ux-service-root",
                str(self.ux_root),
                "--evidence-summary",
                str(bad_summary),
                "--json",
            ],
            check=False,
            capture_output=True,
            text=True,
        )

        payload = json.loads(result.stdout)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(payload["decision"], "blocked")
        self.assertIn("evidenceSummary", payload["missingConfig"])
        self.assertEqual(payload["jsonPath"], str(bad_summary.resolve()))
        self.assertIn("jsonError", payload)
        self.assertEqual(result.stderr, "")

    def test_audit_reports_missing_python_dependency(self) -> None:
        bad_ux_root = self.root / "BadUxTestService"
        (bad_ux_root / "checkMethod").mkdir(parents=True)
        (bad_ux_root / "ux_detect.py").write_text("import definitely_missing_ux_dependency\n", encoding="utf-8")
        evidence_summary = self.write_evidence_bundle(self.root / "evidence")
        output_dir = self.root / "audit"

        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT_PATH),
                "audit",
                "--ux-service-root",
                str(bad_ux_root),
                "--evidence-summary",
                str(evidence_summary),
                "--artifact-dir",
                str(output_dir),
                "--json",
            ],
            check=False,
            capture_output=True,
            text=True,
        )

        payload = json.loads(result.stdout)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(payload["decision"], "blocked")
        self.assertIn("uxPythonDependencies", payload["missingConfig"])
        self.assertEqual(payload["missingModule"], "definitely_missing_ux_dependency")
        self.assertTrue(any("hdc list targets -v" in item for item in payload["recommendations"]))
        self.assertEqual(payload["feedback"]["issueGuide"], "$HARMONY_NEXT_SKILL_DIR/ISSUE_GUIDE.md")

    def test_explicit_missing_ux_service_root_does_not_fall_back_to_default_app(self) -> None:
        evidence_summary = self.write_evidence_bundle(self.root / "evidence")
        output_dir = self.root / "audit"
        missing_ux_root = self.root / "MissingUxTestService"

        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT_PATH),
                "audit",
                "--ux-service-root",
                str(missing_ux_root),
                "--evidence-summary",
                str(evidence_summary),
                "--artifact-dir",
                str(output_dir),
                "--json",
            ],
            check=False,
            capture_output=True,
            text=True,
        )

        payload = json.loads(result.stdout)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(payload["decision"], "blocked")
        self.assertIn("uxServiceRoot", payload["missingConfig"])
        self.assertEqual(payload["uxService"]["source"], "arg:ux-service-root")
        self.assertEqual(payload["uxService"]["path"], str(missing_ux_root))

    def test_explicit_missing_python_does_not_fall_back_to_current_python(self) -> None:
        missing_python = self.root / "missing-python"
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT_PATH),
                "doctor",
                "--hdc",
                str(self.fake_hdc),
                "--ux-service-root",
                str(self.ux_root),
                "--python",
                str(missing_python),
                "--json",
            ],
            check=False,
            capture_output=True,
            text=True,
            env=self.env,
        )

        payload = json.loads(result.stdout)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(payload["decision"], "blocked")
        self.assertIn("uxPython", payload["missingConfig"])
        self.assertEqual(payload["uxPython"]["source"], "arg:python")
        self.assertEqual(payload["uxPython"]["path"], str(missing_python))


if __name__ == "__main__":
    unittest.main()
