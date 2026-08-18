#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import re
import shutil
import socket
import subprocess
import sys
import time
import urllib.error
import urllib.request
import uuid
from dataclasses import dataclass
from pathlib import Path


HDC_ENV_KEYS = ["HARMONY_HDC", "DEVECO_HDC", "HDC"]
DEVECO_APP_ENV_KEYS = ["DEVECO_STUDIO_APP", "DEVECO_APP", "HARMONY_DEVECO_APP"]
DEFAULT_REDACTION_POLICY = "harmony-next-default-v1"
REMOTE_TMP_ROOT = "/data/local/tmp"
FEEDBACK_REPOSITORY = "linhay/harmony-next.skills"
FEEDBACK_ISSUE_TEMPLATE = "device-evidence-bundle.yml"
FEEDBACK_ISSUE_URL = f"https://github.com/{FEEDBACK_REPOSITORY}/issues/new?template={FEEDBACK_ISSUE_TEMPLATE}"
FEEDBACK_ISSUE_GUIDE = "$HARMONY_NEXT_SKILL_DIR/ISSUE_GUIDE.md"
OFFICIAL_CLI_FALLBACK_RECOMMENDATIONS = [
    "If this wrapper is blocked, agents should fall back to official HarmonyOS CLI commands first.",
    "Run `hdc list targets -v` to select a target, then use `hdc -t <target> shell bm dump -g`, `hdc -t <target> shell aa dump -l`, and bounded `hdc -t <target> shell hilog -z <lines>` for state evidence.",
    "For UI evidence, run `hdc -t <target> shell uitest dumpLayout -p /data/local/tmp/layout.json -a`, `hdc -t <target> shell uitest screenCap -p /data/local/tmp/screen.png`, then `hdc -t <target> file recv <remote> <local>`.",
]


class DeviceEvidenceError(RuntimeError):
    def __init__(self, message: str, payload: dict[str, object] | None = None) -> None:
        super().__init__(message)
        self.payload = payload


@dataclass(frozen=True)
class HdcProbe:
    path: Path | None
    source: str
    exists: bool
    executable: bool
    version: str | None = None

    def to_json(self) -> dict[str, object]:
        return {
            "path": str(self.path) if self.path else None,
            "source": self.source,
            "exists": self.exists,
            "executable": self.executable,
            "version": self.version,
        }


def print_json(payload: object) -> None:
    print(json.dumps(payload, ensure_ascii=False, indent=2))


def first_env_path(keys: list[str]) -> tuple[Path | None, str | None]:
    for key in keys:
        value = os.environ.get(key)
        if value:
            return Path(value).expanduser(), key
    return None, None


def dedupe_candidates(candidates: list[tuple[Path, str]]) -> list[tuple[Path, str]]:
    seen: set[str] = set()
    deduped: list[tuple[Path, str]] = []
    for path, source in candidates:
        key = str(path.expanduser())
        if key not in seen:
            seen.add(key)
            deduped.append((path, source))
    return deduped


def hdc_from_deveco_app(path: Path) -> Path:
    expanded = path.expanduser()
    if expanded.name == "Contents":
        return expanded / "sdk" / "default" / "openharmony" / "toolchains" / "hdc"
    return expanded / "Contents" / "sdk" / "default" / "openharmony" / "toolchains" / "hdc"


def candidate_hdcs(hdc: Path | None = None, deveco_app: Path | None = None) -> list[tuple[Path, str]]:
    candidates: list[tuple[Path, str]] = []
    if hdc:
        candidates.append((hdc, "arg:hdc"))

    env_hdc, env_hdc_key = first_env_path(HDC_ENV_KEYS)
    if env_hdc and env_hdc_key:
        candidates.append((env_hdc, f"env:{env_hdc_key}"))

    if deveco_app:
        candidates.append((hdc_from_deveco_app(deveco_app), "arg:deveco-app"))

    env_app, env_app_key = first_env_path(DEVECO_APP_ENV_KEYS)
    if env_app and env_app_key:
        candidates.append((hdc_from_deveco_app(env_app), f"env:{env_app_key}"))

    if platform.system() == "Darwin":
        candidates.append(
            (
                Path("/Applications/DevEco-Studio.app")
                / "Contents"
                / "sdk"
                / "default"
                / "openharmony"
                / "toolchains"
                / "hdc",
                "macos:default-app",
            )
        )

    resolved = shutil.which("hdc")
    if resolved:
        candidates.append((Path(resolved), "path:hdc"))
    return dedupe_candidates(candidates)


def run_probe_command(command: list[str], timeout: float = 5) -> str:
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=timeout, check=False)
    except (OSError, subprocess.TimeoutExpired) as error:
        return str(error)
    return (result.stdout or result.stderr or "").strip()


def probe_single_hdc(path: Path, source: str) -> HdcProbe:
    expanded = path.expanduser()
    if not expanded.exists():
        return HdcProbe(path=expanded, source=source, exists=False, executable=False)
    resolved = expanded.resolve()
    executable = os.access(resolved, os.X_OK)
    version = run_probe_command([str(resolved), "-v"]) if executable else None
    return HdcProbe(path=resolved, source=source, exists=True, executable=executable, version=version or None)


def probe_hdc(hdc: Path | None = None, deveco_app: Path | None = None) -> HdcProbe:
    if hdc:
        return probe_single_hdc(hdc, "arg:hdc")

    if deveco_app:
        return probe_single_hdc(hdc_from_deveco_app(deveco_app), "arg:deveco-app")

    env_hdc, env_hdc_key = first_env_path(HDC_ENV_KEYS)
    if env_hdc and env_hdc_key:
        return probe_single_hdc(env_hdc, f"env:{env_hdc_key}")

    env_app, env_app_key = first_env_path(DEVECO_APP_ENV_KEYS)
    if env_app and env_app_key:
        return probe_single_hdc(hdc_from_deveco_app(env_app), f"env:{env_app_key}")

    fallback_path: Path | None = None
    fallback_source = "not-found"
    for path, source in candidate_hdcs(hdc, deveco_app):
        expanded = path.expanduser()
        if fallback_path is None:
            fallback_path = expanded
            fallback_source = source
        if expanded.exists():
            resolved = expanded.resolve()
            executable = os.access(resolved, os.X_OK)
            version = run_probe_command([str(resolved), "-v"]) if executable else None
            return HdcProbe(path=resolved, source=source, exists=True, executable=executable, version=version or None)
    return HdcProbe(path=fallback_path, source=fallback_source, exists=False, executable=False)


def feedback_payload(*include: str) -> dict[str, object]:
    include_items = [item for item in include if item]
    return {
        "repository": FEEDBACK_REPOSITORY,
        "issueUrl": FEEDBACK_ISSUE_URL,
        "issueTemplate": FEEDBACK_ISSUE_TEMPLATE,
        "issueGuide": FEEDBACK_ISSUE_GUIDE,
        "when": "Open a GitHub issue when the wrapper is blocked, output is misleading, a device/DevEco version is unsupported, or a useful workflow is missing.",
        "include": include_items
        or [
            "command line used",
            "structured JSON output",
            "DevEco Studio version",
            "HDC target summary",
            "redacted command ledger when available",
        ],
        "redact": [
            "screenshots with private UI",
            "raw layout trees",
            "full hilog output",
            "bundle IDs or app names if private",
            "local usernames and private paths",
            "account IDs, tokens, emails, phone numbers, and internal URLs",
        ],
    }


def block(message: str, missing_config: list[str] | None = None, **extra: object) -> None:
    recommendations = extra.pop("recommendations", OFFICIAL_CLI_FALLBACK_RECOMMENDATIONS)
    feedback = extra.pop("feedback", feedback_payload())
    payload: dict[str, object] = {
        "decision": "blocked",
        "error": message,
        "missingConfig": missing_config or [],
        "recommendations": recommendations,
        "feedback": feedback,
    }
    payload.update(extra)
    raise DeviceEvidenceError(message, payload)


def timestamp() -> str:
    return time.strftime("%Y%m%d-%H%M%S")


def ensure_not_inside_app_bundle(path: Path) -> None:
    expanded = path.expanduser()
    for part in expanded.parts:
        if part.endswith(".app"):
            block(
                "refusing to write device evidence artifacts inside an .app bundle",
                missing_config=["artifactDir"],
                artifactDir=str(expanded),
            )


def prepare_artifact_dir(artifact_dir: Path | None) -> Path:
    if artifact_dir is None:
        block("artifact directory is required for real device evidence capture", missing_config=["artifactDir"])
    ensure_not_inside_app_bundle(artifact_dir)
    path = artifact_dir.expanduser().resolve()
    path.mkdir(parents=True, exist_ok=True)
    return path


def parse_connected_targets(output: str) -> list[dict[str, str]]:
    targets: list[dict[str, str]] = []
    for raw_line in output.splitlines():
        line = raw_line.strip()
        if not line or line == "[Empty]" or "Connected" not in line:
            continue
        parts = line.split()
        if not parts:
            continue
        targets.append(
            {
                "target": parts[0],
                "transport": parts[1] if len(parts) > 1 else "",
                "status": parts[2] if len(parts) > 2 else "Connected",
                "label": " ".join(parts[3:]) if len(parts) > 3 else "",
            }
        )
    return targets


def redact_target(target: str, transport: str) -> tuple[str, bool]:
    if transport.upper() != "USB":
        return target, False
    digest = hashlib.sha256(target.encode("utf-8")).hexdigest()[:12]
    return f"<usb-target:{digest}>", True


def public_connected_targets(targets: list[dict[str, str]]) -> list[dict[str, object]]:
    public_targets: list[dict[str, object]] = []
    for item in targets:
        target, sensitive = redact_target(item.get("target", ""), item.get("transport", ""))
        public_item: dict[str, object] = dict(item)
        public_item["target"] = target
        public_item["sensitive"] = sensitive
        public_targets.append(public_item)
    return public_targets


def redact_hdc_list_output(output: str) -> str:
    lines: list[str] = []
    for raw_line in output.splitlines():
        parts = raw_line.split()
        if len(parts) >= 2:
            parts[0], sensitive = redact_target(parts[0], parts[1])
            if sensitive:
                raw_line = "\t".join(parts)
        lines.append(raw_line)
    return "\n".join(lines)


def run_command(command: list[str], timeout: float) -> subprocess.CompletedProcess[str]:
    try:
        return subprocess.run(command, capture_output=True, text=True, timeout=timeout, check=False)
    except subprocess.TimeoutExpired as error:
        completed = subprocess.CompletedProcess(command, returncode=124)
        completed.stdout = error.stdout if isinstance(error.stdout, str) else ""
        completed.stderr = error.stderr if isinstance(error.stderr, str) else f"timed out after {timeout:g}s"
        return completed


def list_targets(hdc: Path, timeout: float) -> tuple[str, list[dict[str, str]], dict[str, object]]:
    command = [str(hdc), "list", "targets", "-v"]
    result = run_command(command, timeout)
    output = (result.stdout or result.stderr or "").strip()
    return output, parse_connected_targets(output), {
        "purpose": "hdc.list.targets",
        "command": command,
        "exitCode": result.returncode,
        "stdoutSnippet": (result.stdout or "")[:1000],
        "stderrSnippet": (result.stderr or "")[:1000],
    }


def choose_target(hdc: Path, requested_target: str | None, timeout: float) -> tuple[str, list[dict[str, str]], dict[str, object]]:
    output, targets, command_info = list_targets(hdc, timeout)
    if requested_target:
        if not targets:
            block(
                "no connected HDC target found",
                missing_config=["target"],
                connectedTargets=[],
                hdcListOutput=output[:2000],
            )
        if requested_target not in {item["target"] for item in targets}:
            block(
                f"requested target is not connected: {requested_target}",
                missing_config=["target"],
                connectedTargets=targets,
                hdcListOutput=output[:2000],
            )
        return requested_target, targets, command_info
    if len(targets) == 1:
        return targets[0]["target"], targets, command_info
    if not targets:
        block(
            "no connected HDC target found",
            missing_config=["target"],
            connectedTargets=[],
            hdcListOutput=output[:2000],
        )
    block(
        "multiple connected HDC targets found; pass --target explicitly",
        missing_config=["target"],
        connectedTargets=targets,
        hdcListOutput=output[:2000],
    )
    raise AssertionError("unreachable")


def artifact_record(kind: str, path: Path, redaction_status: str = "raw-local-artifact") -> dict[str, object]:
    return {
        "kind": kind,
        "path": str(path),
        "exists": path.exists(),
        "bytes": path.stat().st_size if path.exists() else 0,
        "redactionStatus": redaction_status,
    }


def safe_name(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "-", value).strip("-") or "target"


def run_hdc_capture_command(
    hdc: Path,
    target: str,
    args: list[str],
    purpose: str,
    artifact_dir: Path,
    timeout: float,
    stdout_name: str,
    stderr_name: str | None = None,
    snippet: bool = False,
) -> dict[str, object]:
    command = [str(hdc), "-t", target, *args]
    result = run_command(command, timeout)
    stdout_path = artifact_dir / stdout_name
    stderr_path = artifact_dir / (stderr_name or stdout_name.replace(".txt", ".stderr.txt"))
    stdout_path.write_text(result.stdout or "", encoding="utf-8")
    stderr_path.write_text(result.stderr or "", encoding="utf-8")
    record: dict[str, object] = {
        "purpose": purpose,
        "command": command,
        "exitCode": result.returncode,
        "stdout": str(stdout_path),
        "stderr": str(stderr_path),
    }
    if snippet:
        record["stdoutSnippet"] = (result.stdout or "")[:1000]
        record["stderrSnippet"] = (result.stderr or "")[:1000]
    return record


def remote_path(run_id: str, name: str) -> str:
    return f"{REMOTE_TMP_ROOT}/harmony-next-{run_id}-{name}"


def receive_remote_file(
    hdc: Path,
    target: str,
    remote: str,
    local: Path,
    artifact_dir: Path,
    timeout: float,
    purpose: str,
) -> dict[str, object]:
    command = [str(hdc), "-t", target, "file", "recv", remote, str(local)]
    result = run_command(command, timeout)
    stdout_path = artifact_dir / f"{purpose}.stdout.txt"
    stderr_path = artifact_dir / f"{purpose}.stderr.txt"
    stdout_path.write_text(result.stdout or "", encoding="utf-8")
    stderr_path.write_text(result.stderr or "", encoding="utf-8")
    return {
        "purpose": purpose,
        "command": command,
        "exitCode": result.returncode,
        "stdout": str(stdout_path),
        "stderr": str(stderr_path),
    }


def block_required_capture_failure(
    message: str,
    missing_config: list[str],
    artifact_dir: Path,
    commands: list[dict[str, object]],
    artifacts: list[dict[str, object]],
    cleanup_hdc: Path | None = None,
    cleanup_target: str | None = None,
    cleanup_remote_files: list[str] | None = None,
    cleanup_timeout: float = 10,
    no_cleanup: bool = False,
    **extra: object,
) -> None:
    if cleanup_hdc and cleanup_target and cleanup_remote_files and not no_cleanup:
        commands.append(
            run_hdc_capture_command(
                cleanup_hdc,
                cleanup_target,
                ["shell", "rm", "-f", *cleanup_remote_files],
                "cleanup.remote-artifacts",
                artifact_dir,
                cleanup_timeout,
                "cleanup_remote.txt",
                snippet=True,
            )
        )
    ledger_path = artifact_dir / "command_ledger.json"
    ledger_path.write_text(json.dumps(commands, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    payload_extra = {
        "artifactDir": str(artifact_dir),
        "commandLedger": str(ledger_path),
        "artifacts": artifacts + [artifact_record("command-ledger", ledger_path, "summary-safe")],
    }
    payload_extra.update(extra)
    block(message, missing_config=missing_config, **payload_extra)


def require_command_success(
    record: dict[str, object],
    missing_config: list[str],
    artifact_dir: Path,
    commands: list[dict[str, object]],
    artifacts: list[dict[str, object]],
    cleanup_hdc: Path | None = None,
    cleanup_target: str | None = None,
    cleanup_remote_files: list[str] | None = None,
    cleanup_timeout: float = 10,
    no_cleanup: bool = False,
) -> None:
    if record.get("exitCode") == 0:
        return
    block_required_capture_failure(
        f"required HDC command failed: {record.get('purpose')}",
        missing_config=missing_config,
        artifact_dir=artifact_dir,
        commands=commands,
        artifacts=artifacts,
        cleanup_hdc=cleanup_hdc,
        cleanup_target=cleanup_target,
        cleanup_remote_files=cleanup_remote_files,
        cleanup_timeout=cleanup_timeout,
        no_cleanup=no_cleanup,
        failedCommand=record,
    )


def require_artifact_file(
    path: Path,
    kind: str,
    missing_config: list[str],
    artifact_dir: Path,
    commands: list[dict[str, object]],
    artifacts: list[dict[str, object]],
    cleanup_hdc: Path | None = None,
    cleanup_target: str | None = None,
    cleanup_remote_files: list[str] | None = None,
    cleanup_timeout: float = 10,
    no_cleanup: bool = False,
) -> None:
    if path.is_file() and path.stat().st_size > 0:
        return
    block_required_capture_failure(
        f"required {kind} artifact was not captured",
        missing_config=missing_config,
        artifact_dir=artifact_dir,
        commands=commands,
        artifacts=artifacts,
        cleanup_hdc=cleanup_hdc,
        cleanup_target=cleanup_target,
        cleanup_remote_files=cleanup_remote_files,
        cleanup_timeout=cleanup_timeout,
        no_cleanup=no_cleanup,
        missingArtifact=artifact_record(kind, path),
    )


def summarize_layout(path: Path) -> dict[str, object]:
    if not path.exists():
        return {"available": False}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {"available": False, "reason": "not-json"}

    node_count = 0
    bundle_names: set[str] = set()

    def visit(value: object) -> None:
        nonlocal node_count
        if isinstance(value, dict):
            if any(key in value for key in ("bounds", "origBounds", "type", "bundleName", "bundle_name")):
                node_count += 1
            for key in ("bundleName", "bundle_name", "bundle"):
                bundle = value.get(key)
                if isinstance(bundle, str) and bundle:
                    bundle_names.add(bundle)
            for child_value in value.values():
                visit(child_value)
        elif isinstance(value, list):
            for item in value:
                visit(item)

    visit(data)
    return {"available": True, "nodeCount": node_count, "bundleNames": sorted(bundle_names)[:20]}


def parse_webview_sockets(output: str) -> list[dict[str, object]]:
    sockets: list[dict[str, object]] = []
    seen: set[str] = set()
    for match in re.finditer(r"@?(webview_devtools_remote_(\d+))", output):
        name = match.group(1)
        if name in seen:
            continue
        seen.add(name)
        sockets.append({"remoteSocket": name, "pid": int(match.group(2))})
    return sockets


def parse_fport_tasks(output: str) -> list[dict[str, object]]:
    tasks: list[dict[str, object]] = []
    for raw_line in output.splitlines():
        local_match = re.search(r"\btcp:(\d+)\b", raw_line)
        remote_match = re.search(r"\blocalabstract:(webview_devtools_remote_(\d+))\b", raw_line)
        if not local_match or not remote_match:
            continue
        tasks.append(
            {
                "localPort": int(local_match.group(1)),
                "localNode": f"tcp:{local_match.group(1)}",
                "remoteSocket": remote_match.group(1),
                "pid": int(remote_match.group(2)),
            }
        )
    return tasks


def choose_free_local_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listener:
        listener.bind(("127.0.0.1", 0))
        return int(listener.getsockname()[1])


def summarize_json_value(value: object) -> dict[str, object]:
    if isinstance(value, list):
        item_keys: set[str] = set()
        for item in value[:20]:
            if isinstance(item, dict):
                item_keys.update(str(key) for key in item)
        return {
            "jsonType": "array",
            "itemCount": len(value),
            "itemKeys": sorted(item_keys)[:30],
        }
    if isinstance(value, dict):
        return {"jsonType": "object", "keys": sorted(str(key) for key in value)[:40]}
    return {"jsonType": type(value).__name__}


def probe_devtools_http(local_port: int, endpoint: str, timeout: float) -> dict[str, object]:
    url = f"http://127.0.0.1:{local_port}{endpoint}"
    try:
        with urllib.request.urlopen(url, timeout=timeout) as response:
            body = response.read(65537)
            truncated = len(body) > 65536
            body = body[:65536]
            status = int(response.status)
    except urllib.error.HTTPError as error:
        return {
            "endpoint": endpoint,
            "ok": False,
            "failureCode": "devtools_http_error",
            "status": error.code,
            "error": str(error)[:500],
        }
    except urllib.error.URLError as error:
        reason = error.reason
        if isinstance(reason, (socket.timeout, TimeoutError)):
            failure_code = "devtools_http_timeout"
        elif isinstance(reason, ConnectionResetError):
            failure_code = "devtools_http_reset"
        elif isinstance(reason, ConnectionRefusedError):
            failure_code = "devtools_connection_refused"
        else:
            failure_code = "devtools_connection_failed"
        return {
            "endpoint": endpoint,
            "ok": False,
            "failureCode": failure_code,
            "error": str(error)[:500],
        }
    except (ConnectionResetError, ConnectionRefusedError, socket.timeout, TimeoutError) as error:
        if isinstance(error, ConnectionResetError):
            failure_code = "devtools_http_reset"
        elif isinstance(error, ConnectionRefusedError):
            failure_code = "devtools_connection_refused"
        else:
            failure_code = "devtools_http_timeout"
        return {
            "endpoint": endpoint,
            "ok": False,
            "failureCode": failure_code,
            "error": str(error)[:500],
        }

    try:
        decoded = json.loads(body.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        return {
            "endpoint": endpoint,
            "ok": False,
            "failureCode": "devtools_invalid_json",
            "status": status,
            "bytesRead": len(body),
            "truncated": truncated,
            "error": str(error)[:500],
        }
    return {
        "endpoint": endpoint,
        "ok": 200 <= status < 300,
        "status": status,
        "bytesRead": len(body),
        "truncated": truncated,
        "jsonSummary": summarize_json_value(decoded),
    }


def write_webview_diagnostic_summary(
    payload: dict[str, object],
    artifact_dir: Path,
    commands: list[dict[str, object]],
) -> dict[str, object]:
    ledger_path = artifact_dir / "command_ledger.json"
    ledger_path.write_text(json.dumps(commands, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    summary_path = artifact_dir / "summary.json"
    payload["artifactDir"] = str(artifact_dir)
    payload["commandLedger"] = str(ledger_path)
    payload["summary"] = str(summary_path)
    payload["artifacts"] = [
        artifact_record("command-ledger", ledger_path, "summary-safe"),
    ]
    summary_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return payload


def run_webview_devtools(args: argparse.Namespace) -> tuple[int, dict[str, object]]:
    if args.timeout <= 0 or args.http_timeout <= 0:
        block("command and HTTP timeouts must be positive", missing_config=["timeout"])
    probe = probe_hdc(args.hdc, args.deveco_app)
    if not probe.exists:
        block(f"hdc was not found: {probe.path}", missing_config=["hdc"], hdc=probe.to_json())
    if not probe.executable:
        block(f"hdc is not executable: {probe.path}", missing_config=["hdcExecutable"], hdc=probe.to_json())
    assert probe.path is not None

    artifact_dir = prepare_artifact_dir(args.artifact_dir)
    target, connected_targets, list_command = choose_target(probe.path, args.target, args.timeout)
    commands: list[dict[str, object]] = [list_command]

    socket_record = run_hdc_capture_command(
        probe.path,
        target,
        ["shell", "cat", "/proc/net/unix"],
        "webview.list-sockets",
        artifact_dir,
        args.timeout,
        "webview_sockets.txt",
        snippet=True,
    )
    commands.append(socket_record)
    socket_stdout = artifact_dir / "webview_sockets.txt"
    socket_stderr = artifact_dir / "webview_sockets.stderr.txt"
    socket_output = socket_stdout.read_text(encoding="utf-8", errors="replace")
    sockets = parse_webview_sockets(socket_output) if socket_record["exitCode"] == 0 else []

    fport_record = run_hdc_capture_command(
        probe.path,
        target,
        ["fport", "ls"],
        "webview.list-fports",
        artifact_dir,
        args.timeout,
        "webview_fports.txt",
        snippet=True,
    )
    commands.append(fport_record)
    fport_stdout = artifact_dir / "webview_fports.txt"
    fport_stderr = artifact_dir / "webview_fports.stderr.txt"
    fport_output = fport_stdout.read_text(encoding="utf-8", errors="replace")
    fport_tasks = parse_fport_tasks(fport_output) if fport_record["exitCode"] == 0 else []
    live_socket_names = {str(item["remoteSocket"]) for item in sockets}
    stale_forwards = [item for item in fport_tasks if str(item["remoteSocket"]) not in live_socket_names]
    for path in (socket_stdout, socket_stderr, fport_stdout, fport_stderr):
        path.unlink(missing_ok=True)
    if socket_record["exitCode"] == 0:
        socket_record["stdoutSnippet"] = f"discovered {len(sockets)} webview_devtools_remote_* socket(s)"
        socket_record["stderrSnippet"] = ""
    if fport_record["exitCode"] == 0:
        fport_record["stdoutSnippet"] = f"discovered {len(fport_tasks)} WebView fport task(s)"
        fport_record["stderrSnippet"] = ""
    socket_record["stdout"] = None
    socket_record["stderr"] = None
    fport_record["stdout"] = None
    fport_record["stderr"] = None

    payload: dict[str, object] = {
        "decision": "blocked",
        "operation": "device.webview-devtools.diagnose",
        "riskLevel": "automation",
        "target": target,
        "connectedTargets": connected_targets,
        "hdc": probe.to_json(),
        "sockets": sockets,
        "fportTasks": fport_tasks,
        "staleForwards": stale_forwards,
        "redactionPolicy": args.redaction_policy,
        "rawSensitiveContentStored": False,
        "recommendations": [],
        "feedback": feedback_payload(
            "webview-devtools JSON output",
            "redacted command ledger",
            "DevEco Studio and HDC versions",
        ),
    }

    if socket_record["exitCode"] != 0:
        payload.update(
            {
                "failureCode": "webview_socket_enumeration_failed",
                "failureCategory": "device_shell",
                "failureSignal": socket_record.get("stderrSnippet") or socket_record.get("stdoutSnippet"),
            }
        )
        return 2, write_webview_diagnostic_summary(payload, artifact_dir, commands)
    if fport_record["exitCode"] != 0:
        payload.update(
            {
                "failureCode": "fport_list_failed",
                "failureCategory": "fport",
                "failureSignal": fport_record.get("stderrSnippet") or fport_record.get("stdoutSnippet"),
            }
        )
        return 2, write_webview_diagnostic_summary(payload, artifact_dir, commands)

    requested_socket = args.remote_socket.removeprefix("localabstract:") if args.remote_socket else None
    if requested_socket and not re.fullmatch(r"webview_devtools_remote_\d+", requested_socket):
        payload.update(
            {
                "failureCode": "invalid_remote_socket",
                "failureCategory": "configuration",
                "failureSignal": "--remote-socket must look like webview_devtools_remote_<pid>.",
                "missingConfig": ["remoteSocket"],
            }
        )
        return 2, write_webview_diagnostic_summary(payload, artifact_dir, commands)
    if requested_socket and requested_socket not in live_socket_names:
        payload.update(
            {
                "failureCode": "webview_socket_not_found",
                "failureCategory": "webview_runtime",
                "failureSignal": f"Requested socket is not present on the selected target: {requested_socket}",
                "remoteSocket": requested_socket,
                "recommendations": [
                    "Confirm the intended WebView process is alive and Web debugging is enabled before retrying."
                ],
            }
        )
        return 2, write_webview_diagnostic_summary(payload, artifact_dir, commands)
    if not requested_socket and len(sockets) != 1:
        failure_code = "webview_socket_not_found" if not sockets else "multiple_webview_sockets"
        payload.update(
            {
                "failureCode": failure_code,
                "failureCategory": "webview_runtime",
                "failureSignal": (
                    "No webview_devtools_remote_* socket was found."
                    if not sockets
                    else "Multiple WebView DevTools sockets were found; pass --remote-socket."
                ),
                "missingConfig": ["remoteSocket"] if sockets else [],
                "recommendations": [
                    "Open the intended ArkWeb page and confirm Web debugging is enabled."
                    if not sockets
                    else "Select the socket whose PID belongs to the intended foreground WebView."
                ],
            }
        )
        return 2, write_webview_diagnostic_summary(payload, artifact_dir, commands)

    selected_socket = requested_socket or str(sockets[0]["remoteSocket"])
    local_port = args.local_port or choose_free_local_port()
    if not 1 <= local_port <= 65535:
        payload.update(
            {
                "failureCode": "invalid_local_port",
                "failureCategory": "configuration",
                "failureSignal": "--local-port must be in range 1..65535.",
                "missingConfig": ["localPort"],
            }
        )
        return 2, write_webview_diagnostic_summary(payload, artifact_dir, commands)
    conflicting = next((item for item in fport_tasks if item["localPort"] == local_port), None)
    created_forward = False
    reused_forward = False
    cleanup_record: dict[str, object] | None = None

    if conflicting and conflicting["remoteSocket"] == selected_socket:
        reused_forward = True
    elif conflicting:
        is_stale = conflicting in stale_forwards
        if is_stale and args.replace_stale:
            remove_record = run_hdc_capture_command(
                probe.path,
                target,
                ["fport", "rm", f"tcp:{local_port}"],
                "webview.remove-stale-fport",
                artifact_dir,
                args.timeout,
                "webview_remove_stale_fport.txt",
                snippet=True,
            )
            commands.append(remove_record)
            if remove_record["exitCode"] != 0:
                payload.update(
                    {
                        "failureCode": "stale_fport_remove_failed",
                        "failureCategory": "fport",
                        "failureSignal": remove_record.get("stderrSnippet") or remove_record.get("stdoutSnippet"),
                    }
                )
                return 2, write_webview_diagnostic_summary(payload, artifact_dir, commands)
        else:
            payload.update(
                {
                    "failureCode": "stale_fport" if is_stale else "local_port_in_use",
                    "failureCategory": "fport",
                    "failureSignal": f"tcp:{local_port} is already forwarded to {conflicting['remoteSocket']}.",
                    "localPort": local_port,
                    "remoteSocket": selected_socket,
                    "recommendations": [
                        "Pass another --local-port, or use --replace-stale only when the conflicting WebView socket is no longer live."
                    ],
                }
            )
            return 2, write_webview_diagnostic_summary(payload, artifact_dir, commands)

    if not reused_forward:
        create_record = run_hdc_capture_command(
            probe.path,
            target,
            ["fport", f"tcp:{local_port}", f"localabstract:{selected_socket}"],
            "webview.create-fport",
            artifact_dir,
            args.timeout,
            "webview_create_fport.txt",
            snippet=True,
        )
        commands.append(create_record)
        if create_record["exitCode"] != 0:
            payload.update(
                {
                    "failureCode": "fport_create_failed",
                    "failureCategory": "fport",
                    "failureSignal": create_record.get("stderrSnippet") or create_record.get("stdoutSnippet"),
                    "localPort": local_port,
                    "remoteSocket": selected_socket,
                }
            )
            return 2, write_webview_diagnostic_summary(payload, artifact_dir, commands)
        created_forward = True

    probes = [
        probe_devtools_http(local_port, "/json", args.http_timeout),
        probe_devtools_http(local_port, "/json/version", args.http_timeout),
    ]
    probe_ok = any(bool(item.get("ok")) for item in probes)

    if created_forward and not args.keep_forward:
        cleanup_record = run_hdc_capture_command(
            probe.path,
            target,
            ["fport", "rm", f"tcp:{local_port}"],
            "webview.cleanup-fport",
            artifact_dir,
            args.timeout,
            "webview_cleanup_fport.txt",
            snippet=True,
        )
        commands.append(cleanup_record)

    payload.update(
        {
            "decision": "allowed" if probe_ok else "blocked",
            "localPort": local_port,
            "remoteSocket": selected_socket,
            "pid": int(selected_socket.rsplit("_", 1)[1]),
            "fportStatus": {
                "created": created_forward,
                "reused": reused_forward,
                "kept": bool(args.keep_forward or reused_forward),
                "cleanupExitCode": cleanup_record.get("exitCode") if cleanup_record else None,
            },
            "httpProbe": probes,
            "recommendations": (
                [
                    "Use the returned webSocketDebuggerUrl with CDP Runtime.evaluate; keep bridge evidence small and redacted.",
                    "Treat screenshots and layout dumps as supporting evidence only after confirming the intended foreground page.",
                ]
                if probe_ok
                else [
                    "Confirm the selected PID is still alive and ArkWeb debugging is enabled.",
                    "Re-run after removing only stale forwards; do not restart or clear every HDC target by default.",
                ]
            ),
        }
    )
    if not probe_ok:
        first_failure = next((item for item in probes if item.get("failureCode")), {})
        payload["failureCode"] = first_failure.get("failureCode", "devtools_endpoint_unavailable")
        payload["failureCategory"] = "devtools_http"
        payload["failureSignal"] = first_failure.get("error", "Neither /json nor /json/version returned valid JSON.")
    if cleanup_record and cleanup_record.get("exitCode") != 0:
        payload["cleanupWarning"] = "The diagnostic forward could not be removed; inspect fportTasks before retrying."

    return (0 if probe_ok else 2), write_webview_diagnostic_summary(payload, artifact_dir, commands)


def run_capture(args: argparse.Namespace) -> dict[str, object]:
    probe = probe_hdc(args.hdc, args.deveco_app)
    if not probe.exists:
        block(f"hdc was not found: {probe.path}", missing_config=["hdc"], hdc=probe.to_json())
    if not probe.executable:
        block(f"hdc is not executable: {probe.path}", missing_config=["hdcExecutable"], hdc=probe.to_json())
    assert probe.path is not None

    artifact_dir = prepare_artifact_dir(args.artifact_dir)
    target, connected_targets, list_command = choose_target(probe.path, args.target, args.timeout)

    run_id = f"{timestamp()}-{uuid.uuid4().hex[:8]}"
    target_slug = safe_name(target)
    commands: list[dict[str, object]] = [list_command]
    artifacts: list[dict[str, object]] = []
    remote_files: list[str] = []

    commands.append(
        run_hdc_capture_command(
            probe.path,
            target,
            ["shell", "param", "get", "bootevent.boot.completed"],
            "boot.completed",
            artifact_dir,
            args.timeout,
            "boot_completed.txt",
            snippet=True,
        )
    )
    artifacts.append(artifact_record("boot-completed", artifact_dir / "boot_completed.txt", "summary-safe"))

    commands.append(
        run_hdc_capture_command(
            probe.path,
            target,
            ["shell", "bm", "dump", "-g"],
            "bm.debug-bundles",
            artifact_dir,
            args.timeout,
            "bm_debug_bundles.txt",
        )
    )
    artifacts.append(artifact_record("bm-debug-bundles", artifact_dir / "bm_debug_bundles.txt"))

    if args.bundle:
        bundle_file = artifact_dir / "bm_bundle.txt"
        commands.append(
            run_hdc_capture_command(
                probe.path,
                target,
                ["shell", "bm", "dump", "-n", args.bundle],
                "bm.bundle",
                artifact_dir,
                args.timeout,
                bundle_file.name,
            )
        )
        artifacts.append(artifact_record("bm-bundle", bundle_file))

    commands.append(
        run_hdc_capture_command(
            probe.path,
            target,
            ["shell", "aa", "dump", "-l"],
            "aa.dump-list",
            artifact_dir,
            args.timeout,
            "aa_dump_l.txt",
        )
    )
    artifacts.append(artifact_record("aa-dump-list", artifact_dir / "aa_dump_l.txt"))

    commands.append(
        run_hdc_capture_command(
            probe.path,
            target,
            ["shell", "aa", "dump", "-r"],
            "aa.dump-running",
            artifact_dir,
            args.timeout,
            "aa_dump_r.txt",
        )
    )
    artifacts.append(artifact_record("aa-dump-running", artifact_dir / "aa_dump_r.txt"))

    if not args.skip_hilog:
        commands.append(
            run_hdc_capture_command(
                probe.path,
                target,
                ["shell", "hilog", "-z", str(args.hilog_lines)],
                "hilog.tail",
                artifact_dir,
                args.timeout,
                "hilog_tail.txt",
            )
        )
        artifacts.append(artifact_record("hilog-tail", artifact_dir / "hilog_tail.txt"))

    layout_summary: dict[str, object] = {"available": False, "skipped": args.skip_layout}
    if not args.skip_layout:
        remote_layout = remote_path(run_id, "layout.json")
        local_layout = artifact_dir / f"{target_slug}-layout.json"
        remote_files.append(remote_layout)
        layout_dump = run_hdc_capture_command(
            probe.path,
            target,
            ["shell", "uitest", "dumpLayout", "-p", remote_layout, "-a"],
            "uitest.dump-layout",
            artifact_dir,
            args.timeout,
            "uitest_dump_layout.txt",
            snippet=True,
        )
        commands.append(layout_dump)
        require_command_success(
            layout_dump,
            ["layout"],
            artifact_dir,
            commands,
            artifacts,
            cleanup_hdc=probe.path,
            cleanup_target=target,
            cleanup_remote_files=remote_files,
            cleanup_timeout=args.timeout,
            no_cleanup=args.no_cleanup,
        )
        recv_layout = receive_remote_file(
            probe.path,
            target,
            remote_layout,
            local_layout,
            artifact_dir,
            args.timeout,
            "recv_layout",
        )
        commands.append(recv_layout)
        require_command_success(
            recv_layout,
            ["layout"],
            artifact_dir,
            commands,
            artifacts,
            cleanup_hdc=probe.path,
            cleanup_target=target,
            cleanup_remote_files=remote_files,
            cleanup_timeout=args.timeout,
            no_cleanup=args.no_cleanup,
        )
        artifacts.append(artifact_record("layout", local_layout))
        require_artifact_file(
            local_layout,
            "layout",
            ["layout"],
            artifact_dir,
            commands,
            artifacts,
            cleanup_hdc=probe.path,
            cleanup_target=target,
            cleanup_remote_files=remote_files,
            cleanup_timeout=args.timeout,
            no_cleanup=args.no_cleanup,
        )
        layout_summary = summarize_layout(local_layout)
        if not layout_summary.get("available"):
            block_required_capture_failure(
                "captured layout artifact is not valid JSON",
                missing_config=["layout"],
                artifact_dir=artifact_dir,
                commands=commands,
                artifacts=artifacts,
                cleanup_hdc=probe.path,
                cleanup_target=target,
                cleanup_remote_files=remote_files,
                cleanup_timeout=args.timeout,
                no_cleanup=args.no_cleanup,
                layoutSummary=layout_summary,
            )

    if not args.skip_screenshot:
        remote_screen = remote_path(run_id, "screen.png")
        local_screen = artifact_dir / f"{target_slug}-screen.png"
        remote_files.append(remote_screen)
        screencap = run_hdc_capture_command(
            probe.path,
            target,
            ["shell", "uitest", "screenCap", "-p", remote_screen],
            "uitest.screencap",
            artifact_dir,
            args.timeout,
            "uitest_screencap.txt",
            snippet=True,
        )
        commands.append(screencap)
        require_command_success(
            screencap,
            ["screenshot"],
            artifact_dir,
            commands,
            artifacts,
            cleanup_hdc=probe.path,
            cleanup_target=target,
            cleanup_remote_files=remote_files,
            cleanup_timeout=args.timeout,
            no_cleanup=args.no_cleanup,
        )
        recv_screen = receive_remote_file(
            probe.path,
            target,
            remote_screen,
            local_screen,
            artifact_dir,
            args.timeout,
            "recv_screen",
        )
        commands.append(recv_screen)
        require_command_success(
            recv_screen,
            ["screenshot"],
            artifact_dir,
            commands,
            artifacts,
            cleanup_hdc=probe.path,
            cleanup_target=target,
            cleanup_remote_files=remote_files,
            cleanup_timeout=args.timeout,
            no_cleanup=args.no_cleanup,
        )
        artifacts.append(artifact_record("screenshot", local_screen))
        require_artifact_file(
            local_screen,
            "screenshot",
            ["screenshot"],
            artifact_dir,
            commands,
            artifacts,
            cleanup_hdc=probe.path,
            cleanup_target=target,
            cleanup_remote_files=remote_files,
            cleanup_timeout=args.timeout,
            no_cleanup=args.no_cleanup,
        )

    if remote_files and not args.no_cleanup:
        commands.append(
            run_hdc_capture_command(
                probe.path,
                target,
                ["shell", "rm", "-f", *remote_files],
                "cleanup.remote-artifacts",
                artifact_dir,
                args.timeout,
                "cleanup_remote.txt",
                snippet=True,
            )
        )

    ledger_path = artifact_dir / "command_ledger.json"
    ledger_path.write_text(json.dumps(commands, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    artifacts.append(artifact_record("command-ledger", ledger_path, "summary-safe"))

    payload: dict[str, object] = {
        "decision": "collected",
        "operation": "device.evidence.bundle",
        "riskLevel": "evidence",
        "policy": args.policy,
        "redactionPolicy": args.redaction_policy,
        "target": target,
        "connectedTargets": connected_targets,
        "bundle": args.bundle,
        "artifactDir": str(artifact_dir),
        "hdc": probe.to_json(),
        "layoutSummary": layout_summary,
        "artifacts": artifacts,
        "commandLedger": str(ledger_path),
        "rawSensitiveContentStored": True,
        "notes": [
            "Artifacts can include real UI, bundle, ability, and log content. Keep them local or redact before sharing.",
            "This script does not install apps, start apps, stop apps, or launch DevEco Studio.",
        ],
    }
    summary_path = artifact_dir / "summary.json"
    payload["summary"] = str(summary_path)
    payload["feedback"] = feedback_payload(
        str(summary_path),
        str(ledger_path),
        "redacted hdcListOutput / connectedTargets",
        "redacted command stdout/stderr snippets from command_ledger.json",
    )
    summary_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return payload


def run_doctor(args: argparse.Namespace) -> tuple[int, dict[str, object]]:
    probe = probe_hdc(args.hdc, args.deveco_app)
    missing_config: list[str] = []
    issues: list[str] = []
    target_output = ""
    connected_targets: list[dict[str, str]] = []
    list_command: dict[str, object] | None = None

    if not probe.exists:
        missing_config.append("hdc")
        issues.append("hdc was not found")
    elif not probe.executable:
        missing_config.append("hdcExecutable")
        issues.append("hdc exists but is not executable")
    else:
        assert probe.path is not None
        target_output, connected_targets, list_command = list_targets(probe.path, args.timeout)
        if not connected_targets:
            missing_config.append("target")
            issues.append("no connected HDC target found")

    public_output = getattr(args, "public", False)
    hdc_list_command = list_command
    if public_output and list_command:
        hdc_list_command = dict(list_command)
        hdc_list_command["stdoutSnippet"] = redact_hdc_list_output(str(hdc_list_command.get("stdoutSnippet", "")))
        hdc_list_command["stderrSnippet"] = redact_hdc_list_output(str(hdc_list_command.get("stderrSnippet", "")))
    feedback = (
        feedback_payload("doctor --public --json output", "hdcListOutput with private target labels redacted")
        if public_output
        else feedback_payload("doctor JSON output for local diagnosis", "rerun doctor --public --json before public filing")
    )

    payload: dict[str, object] = {
        "decision": "allowed" if not missing_config else "blocked",
        "operation": "device.evidence.doctor",
        "hdc": probe.to_json(),
        "connectedTargets": public_connected_targets(connected_targets) if public_output else connected_targets,
        "hdcListOutput": redact_hdc_list_output(target_output)[:2000] if public_output else target_output[:2000],
        "hdcListCommand": hdc_list_command,
        "missingConfig": missing_config,
        "issues": issues,
        "recommendations": [
            "Use doctor --public --json before sharing output in public issues.",
            "Pass --target when multiple HDC targets are connected.",
            "Use capture --artifact-dir <dir> to save real screenshots, layouts, and bounded logs.",
            "Do not share raw artifacts until screenshots, layout trees, bundle dumps, and logs have been reviewed or redacted.",
            *OFFICIAL_CLI_FALLBACK_RECOMMENDATIONS,
        ],
        "feedback": feedback,
    }
    return (0 if not missing_config else 2), payload


def add_hdc_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--deveco-app", type=Path, help="Path to DevEco-Studio.app or its Contents directory")
    parser.add_argument("--hdc", type=Path, help="Path to the hdc executable")
    parser.add_argument("--timeout", type=float, default=10, help="Per-command timeout in seconds")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Collect a bounded HarmonyOS HDC device evidence bundle.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    doctor = subparsers.add_parser("doctor", help="Locate hdc and report connected targets")
    add_hdc_arguments(doctor)
    doctor.add_argument("--public", action="store_true", help="Redact USB target identifiers for public issue reports")
    doctor.add_argument("--json", action="store_true", help="Print machine-readable JSON")

    capture = subparsers.add_parser("capture", help="Collect screenshot, layout, app state, and bounded logs")
    add_hdc_arguments(capture)
    capture.add_argument("--target", help="HDC target, for example 127.0.0.1:10100")
    capture.add_argument("--bundle", help="Optional bundle name for bm dump -n")
    capture.add_argument("--artifact-dir", type=Path, help="Required directory for raw local evidence artifacts")
    capture.add_argument("--policy", default="evidence", choices=["evidence", "automation", "diagnostic"], help="Audit policy label")
    capture.add_argument("--redaction-policy", default=DEFAULT_REDACTION_POLICY)
    capture.add_argument("--hilog-lines", type=int, default=100)
    capture.add_argument("--skip-hilog", action="store_true")
    capture.add_argument("--skip-layout", action="store_true")
    capture.add_argument("--skip-screenshot", action="store_true")
    capture.add_argument("--no-cleanup", action="store_true", help="Leave remote /data/local/tmp artifacts in place")
    capture.add_argument("--json", action="store_true", help="Print machine-readable JSON")

    webview = subparsers.add_parser(
        "webview-devtools",
        help="Diagnose an ArkWeb/WebView DevTools socket, bounded fport, and HTTP discovery endpoints",
    )
    add_hdc_arguments(webview)
    webview.add_argument("--target", help="HDC target, required when multiple targets are connected")
    webview.add_argument("--artifact-dir", type=Path, help="Required directory for the diagnostic ledger and summary")
    webview.add_argument("--remote-socket", help="webview_devtools_remote_<pid> or localabstract:webview_devtools_remote_<pid>")
    webview.add_argument("--local-port", type=int, help="Host TCP port; an available loopback port is selected when omitted")
    webview.add_argument("--http-timeout", type=float, default=3, help="Timeout for each /json HTTP probe")
    webview.add_argument("--replace-stale", action="store_true", help="Remove a conflicting forward only when its remote socket is no longer live")
    webview.add_argument("--keep-forward", action="store_true", help="Keep a forward created by this run")
    webview.add_argument("--redaction-policy", default=DEFAULT_REDACTION_POLICY)
    webview.add_argument("--json", action="store_true", help="Print machine-readable JSON")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        if args.command == "doctor":
            exit_code, payload = run_doctor(args)
        elif args.command == "capture":
            payload = run_capture(args)
            exit_code = 0
        elif args.command == "webview-devtools":
            exit_code, payload = run_webview_devtools(args)
        else:
            parser.error(f"Unknown command: {args.command}")
            return 2

        if args.json:
            print_json(payload)
        else:
            print(json.dumps(payload, ensure_ascii=False))
        return exit_code
    except DeviceEvidenceError as error:
        payload = error.payload or {"decision": "blocked", "error": str(error), "missingConfig": []}
        if getattr(args, "json", False):
            print_json(payload)
        else:
            print(f"blocked: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
