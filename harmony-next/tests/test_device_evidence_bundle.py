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


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "device_evidence_bundle.py"


class DeviceEvidenceBundleTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.remote_root = self.root / "remote"
        self.remote_root.mkdir()
        self.fake_hdc = self.root / "hdc"
        self.create_fake_hdc(self.fake_hdc)
        self.env = {**os.environ, "FAKE_HDC_REMOTE_ROOT": str(self.remote_root)}

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

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
                    mode = os.environ.get("FAKE_HDC_TARGETS", "single")
                    if mode == "empty":
                        print("[Empty]")
                    elif mode == "multi":
                        print("127.0.0.1:10100 TCP Connected localhost")
                        print("127.0.0.1:10101 TCP Connected localhost")
                    elif mode == "usb":
                        print("127.0.0.1:10100 TCP Connected localhost")
                        print("ABC123PRIVATE USB Connected localhost")
                    else:
                        print("127.0.0.1:10100 TCP Connected localhost")
                    sys.exit(0)

                if len(args) < 3 or args[0] != "-t":
                    print("unexpected args: " + " ".join(args), file=sys.stderr)
                    sys.exit(2)

                target = args[1]
                rest = args[2:]
                if rest[:2] == ["file", "recv"]:
                    if os.environ.get("FAKE_HDC_FAIL_RECV_LAYOUT") and rest[2].endswith("layout.json"):
                        print("layout recv failed", file=sys.stderr)
                        sys.exit(9)
                    src = remote_file(rest[2])
                    dst = Path(rest[3])
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copyfile(src, dst)
                    print(f"recv {rest[2]} -> {dst}")
                    sys.exit(0)

                if rest[0] != "shell":
                    print("unexpected target command: " + " ".join(rest), file=sys.stderr)
                    sys.exit(2)

                shell = rest[1:]
                if shell[:3] == ["param", "get", "bootevent.boot.completed"]:
                    print("true")
                    sys.exit(0)
                if shell[:3] == ["bm", "dump", "-g"]:
                    print("Debug bundle: com.example.emptyability")
                    sys.exit(0)
                if shell[:3] == ["bm", "dump", "-n"]:
                    print("bundleName: " + shell[3])
                    print("mainAbility: EntryAbility")
                    sys.exit(0)
                if shell[:3] == ["aa", "dump", "-l"]:
                    print("AbilityRecord #1 bundleName=com.example.emptyability ability=EntryAbility")
                    sys.exit(0)
                if shell[:3] == ["aa", "dump", "-r"]:
                    print("Running ability: com.example.emptyability/EntryAbility")
                    sys.exit(0)
                if shell[:2] == ["hilog", "-z"]:
                    print("01-01 00:00:00.000 I App: Harmony Smoke Ready")
                    print("01-01 00:00:00.001 W App: synthetic warning")
                    sys.exit(0)
                if shell[:2] == ["uitest", "dumpLayout"]:
                    if os.environ.get("FAKE_HDC_FAIL_LAYOUT"):
                        print("layout capture failed", file=sys.stderr)
                        sys.exit(7)
                    remote = shell[shell.index("-p") + 1]
                    remote_file(remote).write_text(
                        json.dumps(
                            {
                                "bundleName": "com.example.emptyability",
                                "type": "Window",
                                "children": [
                                    {
                                        "type": "Text",
                                        "id": "smoke-title",
                                        "bounds": "[0,0][100,40]",
                                    }
                                ],
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

    def test_doctor_reports_connected_target(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT_PATH),
                "doctor",
                "--hdc",
                str(self.fake_hdc),
                "--json",
            ],
            check=True,
            capture_output=True,
            text=True,
            env=self.env,
        )

        payload = json.loads(result.stdout)
        self.assertEqual(payload["decision"], "allowed")
        self.assertEqual(payload["connectedTargets"][0]["target"], "127.0.0.1:10100")
        self.assertEqual(payload["hdc"]["version"], "Ver: 3.1.0")
        self.assertEqual(payload["feedback"]["repository"], "linhay/harmony-next.skills")
        self.assertEqual(payload["feedback"]["issueTemplate"], "device-evidence-bundle.yml")

    def test_doctor_keeps_usb_target_identifiers_by_default(self) -> None:
        env = {**self.env, "FAKE_HDC_TARGETS": "usb"}
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT_PATH),
                "doctor",
                "--hdc",
                str(self.fake_hdc),
                "--json",
            ],
            check=True,
            capture_output=True,
            text=True,
            env=env,
        )

        payload = json.loads(result.stdout)
        encoded = json.dumps(payload)
        self.assertIn("ABC123PRIVATE", encoded)
        self.assertEqual(payload["connectedTargets"][1]["target"], "ABC123PRIVATE")
        self.assertIn("rerun doctor --public --json before public filing", payload["feedback"]["include"])

    def test_doctor_public_redacts_usb_target_identifiers(self) -> None:
        env = {**self.env, "FAKE_HDC_TARGETS": "usb"}
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT_PATH),
                "doctor",
                "--hdc",
                str(self.fake_hdc),
                "--public",
                "--json",
            ],
            check=True,
            capture_output=True,
            text=True,
            env=env,
        )

        payload = json.loads(result.stdout)
        encoded = json.dumps(payload)
        usb_target = payload["connectedTargets"][1]
        self.assertNotIn("ABC123PRIVATE", encoded)
        self.assertEqual(usb_target["transport"], "USB")
        self.assertEqual(usb_target["target"][:12], "<usb-target:")
        self.assertTrue(usb_target["sensitive"])
        self.assertIn("doctor --public --json output", payload["feedback"]["include"])

    def test_capture_writes_evidence_bundle(self) -> None:
        artifact_dir = self.root / "artifacts"
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT_PATH),
                "capture",
                "--hdc",
                str(self.fake_hdc),
                "--artifact-dir",
                str(artifact_dir),
                "--bundle",
                "com.example.emptyability",
                "--json",
            ],
            check=True,
            capture_output=True,
            text=True,
            env=self.env,
        )

        payload = json.loads(result.stdout)
        kinds = {item["kind"] for item in payload["artifacts"]}
        self.assertEqual(payload["decision"], "collected")
        self.assertEqual(payload["target"], "127.0.0.1:10100")
        self.assertEqual(payload["feedback"]["repository"], "linhay/harmony-next.skills")
        self.assertEqual(payload["feedback"]["issueTemplate"], "device-evidence-bundle.yml")
        self.assertIn("https://github.com/linhay/harmony-next.skills/issues/new", payload["feedback"]["issueUrl"])
        self.assertIn("template=device-evidence-bundle.yml", payload["feedback"]["issueUrl"])
        self.assertIn("layout", kinds)
        self.assertIn("screenshot", kinds)
        self.assertIn("hilog-tail", kinds)
        self.assertIn("bm-bundle", kinds)
        self.assertEqual(payload["layoutSummary"]["nodeCount"], 2)
        self.assertTrue((artifact_dir / "summary.json").is_file())
        self.assertTrue((artifact_dir / "command_ledger.json").is_file())
        self.assertTrue((artifact_dir / "127.0.0.1-10100-layout.json").is_file())
        self.assertTrue((artifact_dir / "127.0.0.1-10100-screen.png").is_file())
        self.assertTrue((artifact_dir / "hilog_tail.txt").is_file())

    def test_capture_blocks_when_multiple_targets_need_selection(self) -> None:
        artifact_dir = self.root / "artifacts"
        env = {**self.env, "FAKE_HDC_TARGETS": "multi"}
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT_PATH),
                "capture",
                "--hdc",
                str(self.fake_hdc),
                "--artifact-dir",
                str(artifact_dir),
                "--json",
            ],
            check=False,
            capture_output=True,
            text=True,
            env=env,
        )

        payload = json.loads(result.stdout)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(payload["decision"], "blocked")
        self.assertIn("target", payload["missingConfig"])
        self.assertEqual(len(payload["connectedTargets"]), 2)
        self.assertTrue(any("hdc list targets -v" in item for item in payload["recommendations"]))
        self.assertIn("ISSUE_GUIDE.md", payload["feedback"]["issueGuide"])

    def test_capture_blocks_when_requested_target_has_no_connected_targets(self) -> None:
        artifact_dir = self.root / "artifacts"
        env = {**self.env, "FAKE_HDC_TARGETS": "empty"}
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT_PATH),
                "capture",
                "--hdc",
                str(self.fake_hdc),
                "--target",
                "127.0.0.1:10100",
                "--artifact-dir",
                str(artifact_dir),
                "--json",
            ],
            check=False,
            capture_output=True,
            text=True,
            env=env,
        )

        payload = json.loads(result.stdout)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(payload["decision"], "blocked")
        self.assertIn("target", payload["missingConfig"])
        self.assertEqual(payload["connectedTargets"], [])

    def test_capture_blocks_when_required_layout_command_fails(self) -> None:
        artifact_dir = self.root / "artifacts"
        env = {**self.env, "FAKE_HDC_FAIL_LAYOUT": "1"}
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT_PATH),
                "capture",
                "--hdc",
                str(self.fake_hdc),
                "--artifact-dir",
                str(artifact_dir),
                "--json",
            ],
            check=False,
            capture_output=True,
            text=True,
            env=env,
        )

        payload = json.loads(result.stdout)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(payload["decision"], "blocked")
        self.assertIn("layout", payload["missingConfig"])
        self.assertEqual(payload["failedCommand"]["purpose"], "uitest.dump-layout")
        self.assertEqual(payload["failedCommand"]["exitCode"], 7)
        self.assertTrue((artifact_dir / "command_ledger.json").is_file())

    def test_capture_cleans_remote_files_when_required_recv_fails(self) -> None:
        artifact_dir = self.root / "artifacts"
        env = {**self.env, "FAKE_HDC_FAIL_RECV_LAYOUT": "1"}
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT_PATH),
                "capture",
                "--hdc",
                str(self.fake_hdc),
                "--artifact-dir",
                str(artifact_dir),
                "--json",
            ],
            check=False,
            capture_output=True,
            text=True,
            env=env,
        )

        payload = json.loads(result.stdout)
        ledger = json.loads((artifact_dir / "command_ledger.json").read_text(encoding="utf-8"))
        self.assertEqual(result.returncode, 2)
        self.assertEqual(payload["decision"], "blocked")
        self.assertEqual(payload["failedCommand"]["purpose"], "recv_layout")
        self.assertIn("layout", payload["missingConfig"])
        self.assertTrue(any(item["purpose"] == "cleanup.remote-artifacts" for item in ledger))
        self.assertEqual(list(self.remote_root.iterdir()), [])

    def test_capture_refuses_artifact_dir_inside_app_bundle(self) -> None:
        artifact_dir = self.root / "DevEco-Studio.app" / "Contents" / "artifacts"
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT_PATH),
                "capture",
                "--hdc",
                str(self.fake_hdc),
                "--artifact-dir",
                str(artifact_dir),
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
        self.assertIn(".app bundle", payload["error"])
        self.assertEqual(payload["feedback"]["repository"], "linhay/harmony-next.skills")

    def test_explicit_missing_hdc_does_not_fall_back_to_default_app(self) -> None:
        missing_hdc = self.root / "missing-hdc"
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT_PATH),
                "doctor",
                "--hdc",
                str(missing_hdc),
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
        self.assertEqual(payload["hdc"]["source"], "arg:hdc")
        self.assertEqual(payload["hdc"]["path"], str(missing_hdc))


if __name__ == "__main__":
    unittest.main()
