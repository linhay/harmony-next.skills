from __future__ import annotations

import importlib.util
import json
import os
import signal
import shutil
import subprocess
import sys
import tempfile
import textwrap
import unittest
from unittest import mock
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "hvd_manager.py"
SPEC = importlib.util.spec_from_file_location("hvd_manager", SCRIPT_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class HvdManagerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name) / "deployed"
        self.root.mkdir()
        self.source_dir = self.root / "Source Phone"
        self.source_dir.mkdir()
        (self.source_dir / "config.ini").write_text(
            "\n".join(
                [
                    "name=Source Phone",
                    "deviceType=phone",
                    "productModel=Source Phone",
                    "uuid=source-uuid",
                    f"instancePath={self.source_dir}",
                    "os.apiVersion=22",
                    "hw.hdc.port=notset",
                    "",
                ]
            ),
            encoding="utf-8",
        )
        (self.source_dir / "hardware-qemu.ini").write_text(
            "\n".join(
                [
                    "[General]",
                    "hvd.id=Source Phone",
                    "hvd.name=Source Phone",
                    "",
                ]
            ),
            encoding="utf-8",
        )
        (self.source_dir / "userdata.img.qcow2").write_text("disk", encoding="utf-8")
        (self.source_dir / "Log").mkdir()
        (self.source_dir / "Log" / "Emulator.log").write_text("old log", encoding="utf-8")
        (self.root / "Source Phone.ini").write_text(
            f"hvd.ini.encoding=UTF-8\npath={self.source_dir}\n",
            encoding="utf-8",
        )
        (self.root / "lists.json").write_text(
            json.dumps(
                [
                    {
                        "name": "Source Phone",
                        "productModel": "Source Phone",
                        "uuid": "source-uuid",
                        "instancePath": str(self.source_dir),
                    }
                ]
            ),
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_list_hvds_reads_registered_instances(self) -> None:
        hvds = MODULE.list_hvds(self.root)

        self.assertEqual(len(hvds), 1)
        self.assertEqual(hvds[0].name, "Source Phone")
        self.assertEqual(hvds[0].device_type, "phone")
        self.assertEqual(hvds[0].api_version, "22")
        self.assertEqual(hvds[0].path, self.source_dir)

    def test_list_command_accepts_json_after_subcommand(self) -> None:
        result = subprocess.run(
            [sys.executable, str(SCRIPT_PATH), "--root", str(self.root), "list", "--json"],
            check=True,
            capture_output=True,
            text=True,
        )

        payload = json.loads(result.stdout)
        self.assertEqual(payload[0]["name"], "Source Phone")
        self.assertNotIn("uuid", payload[0])

    def test_list_command_uses_env_root_when_root_is_omitted(self) -> None:
        env = {**os.environ, "HARMONY_HVD_ROOT": str(self.root)}
        result = subprocess.run(
            [sys.executable, str(SCRIPT_PATH), "list", "--json"],
            check=True,
            capture_output=True,
            text=True,
            env=env,
        )

        payload = json.loads(result.stdout)
        self.assertEqual(payload[0]["name"], "Source Phone")

    def test_doctor_reports_environment_probes(self) -> None:
        emulator = Path(self.temp_dir.name) / "Emulator"
        emulator.write_text("#!/bin/sh\necho HarmonyOS Emulator 9.9.9\n", encoding="utf-8")
        emulator.chmod(0o755)
        sdk_root = Path(self.temp_dir.name) / "sdk"
        sdk_root.mkdir()

        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT_PATH),
                "--root",
                str(self.root),
                "--emulator",
                str(emulator),
                "--sdk-root",
                str(sdk_root),
                "doctor",
                "--json",
            ],
            check=True,
            capture_output=True,
            text=True,
        )

        payload = json.loads(result.stdout)
        self.assertEqual(payload["hvdRoot"]["path"], str(self.root.resolve()))
        self.assertEqual(payload["emulator"]["path"], str(emulator.resolve()))
        self.assertTrue(payload["emulator"]["executable"])
        self.assertEqual(payload["sdkRoot"]["path"], str(sdk_root.resolve()))
        self.assertEqual(payload["hvdCount"], 1)
        self.assertIn("HarmonyOS Emulator 9.9.9", payload["emulatorVersion"]["output"])
        self.assertNotIn("uuid", payload["hvds"][0])

    def test_candidate_emulators_prefers_deveco_default_before_path(self) -> None:
        env = {key: "" for key in MODULE.EMULATOR_ENV_KEYS}
        with mock.patch.dict(os.environ, env), mock.patch.object(MODULE.platform, "system", return_value="Darwin"), mock.patch.object(
            MODULE.shutil, "which", return_value="/Users/test/Library/Android/sdk/emulator/Emulator"
        ):
            candidates = MODULE.candidate_emulators()

        self.assertEqual(candidates[0][1], "macos:default-app")
        self.assertIn((Path("/Users/test/Library/Android/sdk/emulator/Emulator"), "path:Emulator"), candidates)

    def test_parse_connected_target_ignores_usb_for_emulator_launch_without_hint(self) -> None:
        output = "\n".join(
            [
                "ABC123PRIVATE  USB  Connected  localhost",
                "127.0.0.1:5555  TCP  Offline  localhost",
            ]
        )

        self.assertEqual(MODULE.parse_connected_target(output), "ABC123PRIVATE")
        self.assertIsNone(MODULE.parse_connected_target(output, tcp_only=True))
        self.assertEqual(MODULE.parse_connected_target(output, ":5555"), None)

    def test_parse_connected_target_prefers_tcp_for_emulator_launch_without_hint(self) -> None:
        output = "\n".join(
            [
                "ABC123PRIVATE  USB  Connected  localhost",
                "127.0.0.1:5555  TCP  Connected  localhost",
            ]
        )

        self.assertEqual(MODULE.parse_connected_target(output, tcp_only=True), "127.0.0.1:5555")

    def test_create_hvd_clones_source_and_refreshes_identity(self) -> None:
        created = MODULE.create_hvd(
            root=self.root,
            source_name="Source Phone",
            new_name="CLI Phone",
            hdc_port=10123,
            include_logs=False,
        )

        self.assertEqual(created.name, "CLI Phone")
        self.assertTrue((self.root / "CLI Phone.ini").is_file())
        self.assertTrue((self.root / "CLI Phone" / "config.ini").is_file())
        self.assertTrue((self.root / "CLI Phone" / "userdata.img.qcow2").is_file())
        self.assertFalse((self.root / "CLI Phone" / "Log" / "Emulator.log").exists())

        root_ini = MODULE.read_ini(self.root / "CLI Phone.ini")
        config = MODULE.read_ini(self.root / "CLI Phone" / "config.ini")
        hardware = MODULE.read_sectionless_ini(self.root / "CLI Phone" / "hardware-qemu.ini")
        lists = json.loads((self.root / "lists.json").read_text(encoding="utf-8"))

        expected_path = str((self.root / "CLI Phone").resolve())
        self.assertEqual(root_ini["path"], expected_path)
        self.assertEqual(config["name"], "CLI Phone")
        self.assertEqual(config["productModel"], "CLI Phone")
        self.assertEqual(config["instancePath"], expected_path)
        self.assertEqual(config["hw.hdc.port"], "10123")
        self.assertNotEqual(config["uuid"], "source-uuid")
        self.assertEqual(hardware["hvd.id"], "CLI Phone")
        self.assertEqual(hardware["hvd.name"], "CLI Phone")
        self.assertIn("CLI Phone", {item["name"] for item in lists})

    def test_create_hvd_refuses_duplicate_names(self) -> None:
        with self.assertRaises(MODULE.HvdManagerError):
            MODULE.create_hvd(
                root=self.root,
                source_name="Source Phone",
                new_name="Source Phone",
                hdc_port=None,
                include_logs=False,
            )

    def test_delete_hvd_requires_exact_confirmation(self) -> None:
        MODULE.create_hvd(
            root=self.root,
            source_name="Source Phone",
            new_name="CLI Phone",
            hdc_port=None,
            include_logs=False,
        )

        with self.assertRaises(MODULE.HvdManagerError):
            MODULE.delete_hvd(self.root, "CLI Phone", confirm_name="wrong")

        deleted = MODULE.delete_hvd(self.root, "CLI Phone", confirm_name="CLI Phone")

        self.assertEqual(deleted.name, "CLI Phone")
        self.assertFalse((self.root / "CLI Phone.ini").exists())
        self.assertFalse((self.root / "CLI Phone").exists())
        lists = json.loads((self.root / "lists.json").read_text(encoding="utf-8"))
        self.assertNotIn("CLI Phone", {item["name"] for item in lists})

    def test_delete_hvd_refuses_path_outside_root(self) -> None:
        outside_dir = Path(self.temp_dir.name) / "outside-hvd"
        outside_dir.mkdir()
        (outside_dir / "config.ini").write_text(
            "\n".join(
                [
                    "name=Outside Phone",
                    "deviceType=phone",
                    "os.apiVersion=22",
                    "",
                ]
            ),
            encoding="utf-8",
        )
        (self.root / "Outside Phone.ini").write_text(
            f"hvd.ini.encoding=UTF-8\npath={outside_dir}\n",
            encoding="utf-8",
        )

        with self.assertRaisesRegex(MODULE.HvdManagerError, "outside HVD root"):
            MODULE.delete_hvd(self.root, "Outside Phone", confirm_name="Outside Phone")

        self.assertTrue((self.root / "Outside Phone.ini").exists())
        self.assertTrue(outside_dir.exists())

    def test_download_image_command_reports_blocked(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT_PATH),
                "download-image",
                "--device-type",
                "phone",
                "--api-version",
                "22",
            ],
            check=False,
            capture_output=True,
            text=True,
        )

        self.assertEqual(result.returncode, 2)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["decision"], "blocked")
        self.assertEqual(payload["operation"], "image.download")

    def test_launch_preflight_blocks_without_trace_helper(self) -> None:
        emulator = Path(self.temp_dir.name) / "Emulator"
        emulator.write_text("#!/bin/sh\necho should-not-run\n", encoding="utf-8")
        emulator.chmod(0o755)
        sdk_root = Path(self.temp_dir.name) / "sdk"
        sdk_root.mkdir()

        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT_PATH),
                "--root",
                str(self.root),
                "--emulator",
                str(emulator),
                "--sdk-root",
                str(sdk_root),
                "launch-preflight",
                "--name",
                "Source Phone",
                "--json",
            ],
            check=False,
            capture_output=True,
            text=True,
        )

        self.assertEqual(result.returncode, 2)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["decision"], "blocked")
        self.assertEqual(payload["operation"], "emulator.launch.preflight")
        self.assertIn("traceName", payload["missingConfig"])
        self.assertIn("tracePipeHelper", payload["missingConfig"])
        self.assertIn("请在DevEco Studio中登录华为账号", payload["knownSymptom"])
        self.assertNotIn("emulatorCommand", payload)

    def test_launch_preflight_blocks_when_hvd_directory_is_missing(self) -> None:
        emulator = Path(self.temp_dir.name) / "Emulator"
        emulator.write_text("#!/bin/sh\necho should-not-run\n", encoding="utf-8")
        emulator.chmod(0o755)
        sdk_root = Path(self.temp_dir.name) / "sdk"
        sdk_root.mkdir()
        ready_file = Path(self.temp_dir.name) / "trace.ready"
        ready_file.write_text("ready\n", encoding="utf-8")
        shutil.rmtree(self.source_dir)

        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT_PATH),
                "--root",
                str(self.root),
                "--emulator",
                str(emulator),
                "--sdk-root",
                str(sdk_root),
                "launch-preflight",
                "--name",
                "Source Phone",
                "--trace-name",
                "ai-emu-test",
                "--trace-helper-ready-file",
                str(ready_file),
                "--json",
            ],
            check=False,
            capture_output=True,
            text=True,
        )

        self.assertEqual(result.returncode, 2)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["decision"], "blocked")
        self.assertIn("hvdDirectory", payload["missingConfig"])
        self.assertNotIn("emulatorCommand", payload)

    def test_launch_preflight_outputs_trace_guarded_command(self) -> None:
        emulator = Path(self.temp_dir.name) / "Emulator"
        emulator.write_text("#!/bin/sh\necho should-not-run\n", encoding="utf-8")
        emulator.chmod(0o755)
        sdk_root = Path(self.temp_dir.name) / "sdk"
        sdk_root.mkdir()
        ready_file = Path(self.temp_dir.name) / "trace.ready"
        ready_file.write_text("ready\n", encoding="utf-8")

        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT_PATH),
                "--root",
                str(self.root),
                "--emulator",
                str(emulator),
                "--sdk-root",
                str(sdk_root),
                "launch-preflight",
                "--name",
                "Source Phone",
                "--trace-name",
                "ai-emu-test",
                "--trace-helper-ready-file",
                str(ready_file),
                "--hdc-port",
                "10123",
                "--json",
            ],
            check=True,
            capture_output=True,
            text=True,
        )

        payload = json.loads(result.stdout)
        self.assertEqual(payload["decision"], "allowed")
        self.assertEqual(payload["operation"], "emulator.launch.preflight")
        self.assertEqual(payload["traceName"], "ai-emu-test")
        self.assertEqual(payload["emulatorCommand"][0], str(emulator.resolve()))
        self.assertIn("-t", payload["emulatorCommand"])
        self.assertIn("ai-emu-test", payload["emulatorCommand"])
        self.assertIn("-hdcport", payload["emulatorCommand"])
        self.assertIn("10123", payload["emulatorCommand"])

    def test_launch_preflight_blocks_when_image_subpath_is_missing(self) -> None:
        MODULE.update_key_value_file(
            self.source_dir / "config.ini",
            {"imageSubPath": "system-image/HarmonyOS-6.0.2/phone_all_arm/"},
        )
        emulator = Path(self.temp_dir.name) / "Emulator"
        emulator.write_text("#!/bin/sh\necho should-not-run\n", encoding="utf-8")
        emulator.chmod(0o755)
        image_root = Path(self.temp_dir.name) / "wrong-image-root"
        image_root.mkdir()
        ready_file = Path(self.temp_dir.name) / "trace.ready"
        ready_file.write_text("ready\n", encoding="utf-8")

        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT_PATH),
                "--root",
                str(self.root),
                "--emulator",
                str(emulator),
                "launch-preflight",
                "--name",
                "Source Phone",
                "--image-root",
                str(image_root),
                "--trace-name",
                "ai-emu-test",
                "--trace-helper-ready-file",
                str(ready_file),
                "--json",
            ],
            check=False,
            capture_output=True,
            text=True,
        )

        self.assertEqual(result.returncode, 2)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["decision"], "blocked")
        self.assertIn("imageRootSystemImage", payload["missingConfig"])
        self.assertNotIn("emulatorCommand", payload)
        self.assertIn("Library/Huawei/Sdk", " ".join(payload["recommendations"]))

    def test_launch_preflight_allows_matching_image_subpath(self) -> None:
        MODULE.update_key_value_file(
            self.source_dir / "config.ini",
            {"imageSubPath": "system-image/HarmonyOS-6.0.2/phone_all_arm/"},
        )
        emulator = Path(self.temp_dir.name) / "Emulator"
        emulator.write_text("#!/bin/sh\necho should-not-run\n", encoding="utf-8")
        emulator.chmod(0o755)
        image_root = Path(self.temp_dir.name) / "image-root"
        (image_root / "system-image" / "HarmonyOS-6.0.2" / "phone_all_arm").mkdir(parents=True)
        ready_file = Path(self.temp_dir.name) / "trace.ready"
        ready_file.write_text("ready\n", encoding="utf-8")

        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT_PATH),
                "--root",
                str(self.root),
                "--emulator",
                str(emulator),
                "launch-preflight",
                "--name",
                "Source Phone",
                "--image-root",
                str(image_root),
                "--trace-name",
                "ai-emu-test",
                "--trace-helper-ready-file",
                str(ready_file),
                "--json",
            ],
            check=True,
            capture_output=True,
            text=True,
        )

        payload = json.loads(result.stdout)
        self.assertEqual(payload["decision"], "allowed")
        self.assertIn(str(image_root.resolve()), payload["emulatorCommand"])

    def test_launch_blocks_bad_image_root_before_starting_emulator(self) -> None:
        MODULE.update_key_value_file(
            self.source_dir / "config.ini",
            {"imageSubPath": "system-image/HarmonyOS-6.0.2/phone_all_arm/"},
        )
        marker = Path(self.temp_dir.name) / "started.marker"
        emulator = Path(self.temp_dir.name) / "Emulator"
        emulator.write_text(f"#!/bin/sh\ntouch {marker}\n", encoding="utf-8")
        emulator.chmod(0o755)
        image_root = Path(self.temp_dir.name) / "wrong-image-root"
        image_root.mkdir()

        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT_PATH),
                "--root",
                str(self.root),
                "--emulator",
                str(emulator),
                "launch",
                "--name",
                "Source Phone",
                "--image-root",
                str(image_root),
                "--trace-name",
                "ai-emu-test-bad-root",
                "--no-wait-target",
                "--json",
            ],
            check=False,
            capture_output=True,
            text=True,
        )

        self.assertEqual(result.returncode, 2)
        payload = json.loads(result.stdout)
        self.assertIn("imageRootSystemImage", payload["missingConfig"])
        self.assertFalse(marker.exists())

    def test_launch_classifies_first_run_license_agreement_prompt(self) -> None:
        emulator = Path(self.temp_dir.name) / "Emulator"
        emulator.write_text(
            textwrap.dedent(
                """\
                #!/usr/bin/env python3
                import sys

                _ = sys.stdin.read()
                print("Please read carefully and confirm whether agree to the above agreement? (y/N): Please agree to the agreement first.")
                print("Unable to start the emulator")
                raise SystemExit(1)
                """
            ),
            encoding="utf-8",
        )
        emulator.chmod(0o755)
        image_root = Path(self.temp_dir.name) / "image-root"
        image_root.mkdir()

        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT_PATH),
                "--root",
                str(self.root),
                "--emulator",
                str(emulator),
                "launch",
                "--name",
                "Source Phone",
                "--image-root",
                str(image_root),
                "--trace-name",
                "ai-emu-license",
                "--no-wait-target",
                "--timeout",
                "0.2",
                "--json",
            ],
            check=False,
            capture_output=True,
            text=True,
        )

        self.assertEqual(result.returncode, 2)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["decision"], "blocked")
        self.assertEqual(payload["result"], "license-agreement-required")
        self.assertEqual(payload["missingConfig"], ["emulatorLicenseAgreement"])
        self.assertIn("--accept-license", " ".join(payload["recommendations"]))
        self.assertIn("Please agree to the agreement first", payload["logTail"])

    def test_launch_accept_license_writes_explicit_confirmation(self) -> None:
        marker = Path(self.temp_dir.name) / "accepted.marker"
        emulator = Path(self.temp_dir.name) / "Emulator"
        emulator.write_text(
            textwrap.dedent(
                f"""\
                #!/usr/bin/env python3
                import socket
                import sys

                accepted = sys.stdin.read().strip().lower() == "y"
                if not accepted:
                    print("Please agree to the agreement first.")
                    raise SystemExit(1)
                open({str(marker)!r}, "w", encoding="utf-8").write("accepted\\n")
                trace_name = sys.argv[sys.argv.index("-t") + 1]
                client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
                client.connect(f"/tmp/{{trace_name}}")
                client.sendall(b'{{"event":"fake-start"}}\\n')
                client.close()
                """
            ),
            encoding="utf-8",
        )
        emulator.chmod(0o755)
        image_root = Path(self.temp_dir.name) / "image-root"
        image_root.mkdir()

        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT_PATH),
                "--root",
                str(self.root),
                "--emulator",
                str(emulator),
                "launch",
                "--name",
                "Source Phone",
                "--image-root",
                str(image_root),
                "--trace-name",
                "ai-emu-accept-license",
                "--accept-license",
                "--no-wait-target",
                "--timeout",
                "3",
                "--json",
            ],
            check=True,
            capture_output=True,
            text=True,
        )

        payload = json.loads(result.stdout)
        self.assertEqual(payload["decision"], "allowed")
        self.assertEqual(payload["result"], "started")
        self.assertTrue(payload["socketConnected"])
        self.assertTrue(marker.exists())

    def test_launch_creates_trace_socket_and_starts_emulator(self) -> None:
        emulator = Path(self.temp_dir.name) / "Emulator"
        emulator.write_text(
            textwrap.dedent(
                """\
                #!/usr/bin/env python3
                import socket
                import sys

                trace_name = sys.argv[sys.argv.index("-t") + 1]
                client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
                client.connect(f"/tmp/{trace_name}")
                client.sendall(b'{"event":"fake-start"}\\n')
                client.close()
                """
            ),
            encoding="utf-8",
        )
        emulator.chmod(0o755)
        image_root = Path(self.temp_dir.name) / "image-root"
        image_root.mkdir()

        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT_PATH),
                "--root",
                str(self.root),
                "--emulator",
                str(emulator),
                "launch",
                "--name",
                "Source Phone",
                "--image-root",
                str(image_root),
                "--trace-name",
                "ai-emu-test-launch",
                "--no-wait-target",
                "--timeout",
                "3",
                "--json",
            ],
            check=True,
            capture_output=True,
            text=True,
        )

        payload = json.loads(result.stdout)
        self.assertEqual(payload["decision"], "allowed")
        self.assertEqual(payload["operation"], "emulator.launch")
        self.assertEqual(payload["result"], "started")
        self.assertEqual(payload["traceName"], "ai-emu-test-launch")
        self.assertTrue(payload["socketConnected"])
        self.assertGreater(payload["traceBytesRead"], 0)
        self.assertIn("traceHolder", payload)
        self.assertIn("-t", payload["emulatorCommand"])
        self.assertIn("ai-emu-test-launch", payload["emulatorCommand"])

    def test_launch_reports_unstable_process_after_boot(self) -> None:
        emulator = Path(self.temp_dir.name) / "Emulator"
        emulator.write_text(
            textwrap.dedent(
                """\
                #!/usr/bin/env python3
                import socket
                import sys
                import time

                trace_name = sys.argv[sys.argv.index("-t") + 1]
                client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
                client.connect(f"/tmp/{trace_name}")
                client.sendall(b'{"event":"fake-start"}\\n')
                time.sleep(0.1)
                client.close()
                raise SystemExit(9)
                """
            ),
            encoding="utf-8",
        )
        emulator.chmod(0o755)
        hdc = Path(self.temp_dir.name) / "hdc"
        hdc.write_text(
            textwrap.dedent(
                """\
                #!/bin/sh
                case "$*" in
                  *"list targets -v"*) echo "127.0.0.1:10123  TCP  Connected  localhost" ;;
                  *"param get bootevent.boot.completed"*) echo "true" ;;
                  *) echo "" ;;
                esac
                """
            ),
            encoding="utf-8",
        )
        hdc.chmod(0o755)
        image_root = Path(self.temp_dir.name) / "image-root"
        image_root.mkdir()

        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT_PATH),
                "--root",
                str(self.root),
                "--emulator",
                str(emulator),
                "launch",
                "--name",
                "Source Phone",
                "--image-root",
                str(image_root),
                "--trace-name",
                "ai-emu-unstable",
                "--hdc",
                str(hdc),
                "--hdc-port",
                "10123",
                "--timeout",
                "2",
                "--stability-seconds",
                "1",
                "--trace-hold-seconds",
                "0",
                "--json",
            ],
            check=False,
            capture_output=True,
            text=True,
        )

        self.assertEqual(result.returncode, 2)
        payload = json.loads(result.stdout)
        self.assertTrue(payload["hdcWait"]["connected"])
        self.assertTrue(payload["bootWait"]["completed"])
        self.assertFalse(payload["stabilityWait"]["stable"])
        self.assertEqual(payload["stabilityWait"]["reason"], "process-exited")
        self.assertEqual(payload["stabilityWait"]["processExitCode"], 9)

    def test_launch_reports_silent_exit_diagnostics(self) -> None:
        emulator = Path(self.temp_dir.name) / "Emulator"
        emulator.write_text("#!/bin/sh\nexit 7\n", encoding="utf-8")
        emulator.chmod(0o755)
        image_root = Path(self.temp_dir.name) / "image-root"
        image_root.mkdir()
        artifact_dir = Path(self.temp_dir.name) / "artifacts"

        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT_PATH),
                "--root",
                str(self.root),
                "--emulator",
                str(emulator),
                "launch",
                "--name",
                "Source Phone",
                "--image-root",
                str(image_root),
                "--trace-name",
                "ai-emu-silent-exit",
                "--artifact-dir",
                str(artifact_dir),
                "--no-wait-target",
                "--timeout",
                "0.2",
                "--json",
            ],
            check=False,
            capture_output=True,
            text=True,
        )

        self.assertEqual(result.returncode, 2)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["result"], "trace-timeout")
        self.assertIn(payload["processExitCode"], {7, -signal.SIGTERM})
        self.assertTrue(Path(payload["logPath"]).exists())
        self.assertIn("hvdRuntime", payload)
        self.assertIn("hdcSnapshot", payload)
        self.assertIn("traceTimeoutDiagnostics", payload)
        self.assertIn("Emulator process exited", " ".join(payload["traceTimeoutDiagnostics"]["likelyCauses"]))

    def test_launch_reports_trace_timeout_next_diagnostics(self) -> None:
        emulator = Path(self.temp_dir.name) / "Emulator"
        emulator.write_text(
            textwrap.dedent(
                """\
                #!/bin/sh
                if [ "$1" = "-list" ]; then
                  echo "name=Source Phone isRunning=false hw.hdc.port=10107"
                  exit 0
                fi
                sleep 10
                """
            ),
            encoding="utf-8",
        )
        emulator.chmod(0o755)
        hdc = Path(self.temp_dir.name) / "hdc"
        hdc.write_text("#!/bin/sh\necho '127.0.0.1:10107  TCP  Offline  localhost'\n", encoding="utf-8")
        hdc.chmod(0o755)
        image_root = Path(self.temp_dir.name) / "image-root"
        image_root.mkdir()

        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT_PATH),
                "--root",
                str(self.root),
                "--emulator",
                str(emulator),
                "launch",
                "--name",
                "Source Phone",
                "--image-root",
                str(image_root),
                "--trace-name",
                "ai-emu-hangs",
                "--hdc",
                str(hdc),
                "--no-wait-target",
                "--timeout",
                "0.2",
                "--json",
            ],
            check=False,
            capture_output=True,
            text=True,
        )

        self.assertEqual(result.returncode, 2)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["result"], "trace-timeout")
        diagnostics = payload["traceTimeoutDiagnostics"]
        self.assertEqual(diagnostics["socketPath"], "/tmp/ai-emu-hangs")
        self.assertIn("Offline targets", " ".join(diagnostics["likelyCauses"]))
        self.assertIn("nextDiagnosticCommands", diagnostics)
        command_purposes = {item["purpose"] for item in diagnostics["nextDiagnosticCommands"]}
        self.assertIn("Inspect HVD runtime state", command_purposes)
        self.assertIn("Inspect HDC target state", command_purposes)


if __name__ == "__main__":
    unittest.main()
