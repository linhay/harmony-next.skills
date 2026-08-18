#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import platform
import re
import shutil
import subprocess
import sys
import time
import uuid
from dataclasses import dataclass
from pathlib import Path

import device_evidence_bundle


DEVECO_APP_ENV_KEYS = ["DEVECO_STUDIO_APP", "DEVECO_APP", "HARMONY_DEVECO_APP"]
UX_SERVICE_ENV_KEYS = ["DEVECO_UX_TEST_SERVICE", "HARMONY_UX_TEST_SERVICE", "UX_TEST_SERVICE"]
UX_PYTHON_ENV_KEYS = ["HARMONY_UX_PYTHON", "DEVECO_UX_PYTHON", "UX_TEST_PYTHON"]
UX_PYTHON_IMPORT_MODULES = ["cv2", "numpy", "PIL", "requests", "scipy", "skimage", "werkzeug", "opencc"]
DEFAULT_TEST_CODES = [
    "7.1.1.2.1",
    "7.1.1.2.2",
    "7.1.1.3.3",
    "7.1.1.4.4",
    "7.1.1.4.5",
    "7.1.2.1.1",
    "7.1.2.6.1",
    "7.2.2.1.8",
]
SYSTEM_BUNDLE_NAMES = {
    "com.ohos.sceneboard",
    "com.ohos.systemui",
    "com.ohos.launcher",
    "com.ohos.settingsdata",
}
FEEDBACK_REPOSITORY = "linhay/harmony-next.skills"
FEEDBACK_ISSUE_TEMPLATE = "offline-ux-audit.yml"
FEEDBACK_ISSUE_URL = f"https://github.com/{FEEDBACK_REPOSITORY}/issues/new?template={FEEDBACK_ISSUE_TEMPLATE}"
FEEDBACK_ISSUE_GUIDE = "$HARMONY_NEXT_SKILL_DIR/ISSUE_GUIDE.md"
OFFICIAL_CLI_FALLBACK_RECOMMENDATIONS = [
    "If this wrapper is blocked, agents should fall back to official HarmonyOS CLI commands first.",
    "Start with `hdc list targets -v`, then run `hdc -t <target> shell uitest dumpLayout -p /data/local/tmp/layout.json -a` and `hdc -t <target> shell uitest screenCap -p /data/local/tmp/screen.png`.",
    "Use `hdc -t <target> file recv <remote> <local>` to preserve official CLI evidence, then retry `audit --layout <layout.json> --screenshot <screen.png> --bundle <bundle>`.",
]


class UxAuditPipelineError(RuntimeError):
    def __init__(self, message: str, payload: dict[str, object] | None = None) -> None:
        super().__init__(message)
        self.payload = payload


@dataclass(frozen=True)
class UxServiceProbe:
    path: Path | None
    source: str
    exists: bool
    runnable: bool
    version: str | None = None

    def to_json(self) -> dict[str, object]:
        return {
            "path": str(self.path) if self.path else None,
            "source": self.source,
            "exists": self.exists,
            "runnable": self.runnable,
            "version": self.version,
        }


@dataclass(frozen=True)
class UxPythonProbe:
    path: Path | None
    source: str
    exists: bool
    executable: bool
    version: str | None = None
    missing_modules: tuple[str, ...] = ()
    error: str | None = None

    def to_json(self) -> dict[str, object]:
        return {
            "path": str(self.path) if self.path else None,
            "source": self.source,
            "exists": self.exists,
            "executable": self.executable,
            "version": self.version,
            "requiredModules": UX_PYTHON_IMPORT_MODULES,
            "missingModules": list(self.missing_modules),
            "error": self.error,
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


def ux_service_from_deveco_app(path: Path) -> Path:
    expanded = path.expanduser()
    if expanded.name == "Contents":
        return expanded / "tools" / "UxTestService"
    return expanded / "Contents" / "tools" / "UxTestService"


def candidate_ux_services(ux_service_root: Path | None = None, deveco_app: Path | None = None) -> list[tuple[Path, str]]:
    candidates: list[tuple[Path, str]] = []
    if ux_service_root:
        candidates.append((ux_service_root, "arg:ux-service-root"))

    env_service, env_service_key = first_env_path(UX_SERVICE_ENV_KEYS)
    if env_service and env_service_key:
        candidates.append((env_service, f"env:{env_service_key}"))

    if deveco_app:
        candidates.append((ux_service_from_deveco_app(deveco_app), "arg:deveco-app"))

    env_app, env_app_key = first_env_path(DEVECO_APP_ENV_KEYS)
    if env_app and env_app_key:
        candidates.append((ux_service_from_deveco_app(env_app), f"env:{env_app_key}"))

    if platform.system() == "Darwin":
        candidates.append((Path("/Applications/DevEco-Studio.app") / "Contents" / "tools" / "UxTestService", "macos:default-app"))
    return dedupe_candidates(candidates)


def probe_single_ux_service(path: Path, source: str) -> UxServiceProbe:
    expanded = path.expanduser()
    if not expanded.exists():
        return UxServiceProbe(path=expanded, source=source, exists=False, runnable=False)
    root = expanded.resolve()
    runnable = (root / "ux_detect.py").is_file() and (root / "checkMethod").is_dir()
    version_path = root / "buildInfo.properties"
    version = version_path.read_text(encoding="utf-8", errors="replace").strip() if version_path.is_file() else None
    return UxServiceProbe(path=root, source=source, exists=True, runnable=runnable, version=version)


def probe_ux_service(ux_service_root: Path | None = None, deveco_app: Path | None = None) -> UxServiceProbe:
    if ux_service_root:
        return probe_single_ux_service(ux_service_root, "arg:ux-service-root")

    if deveco_app:
        return probe_single_ux_service(ux_service_from_deveco_app(deveco_app), "arg:deveco-app")

    env_service, env_service_key = first_env_path(UX_SERVICE_ENV_KEYS)
    if env_service and env_service_key:
        return probe_single_ux_service(env_service, f"env:{env_service_key}")

    env_app, env_app_key = first_env_path(DEVECO_APP_ENV_KEYS)
    if env_app and env_app_key:
        return probe_single_ux_service(ux_service_from_deveco_app(env_app), f"env:{env_app_key}")

    fallback_path: Path | None = None
    fallback_source = "not-found"
    for path, source in candidate_ux_services(ux_service_root, deveco_app):
        expanded = path.expanduser()
        if fallback_path is None:
            fallback_path = expanded
            fallback_source = source
        if expanded.exists():
            root = expanded.resolve()
            runnable = (root / "ux_detect.py").is_file() and (root / "checkMethod").is_dir()
            version_path = root / "buildInfo.properties"
            version = version_path.read_text(encoding="utf-8", errors="replace").strip() if version_path.is_file() else None
            return UxServiceProbe(path=root, source=source, exists=True, runnable=runnable, version=version)
    return UxServiceProbe(path=fallback_path, source=fallback_source, exists=False, runnable=False)


def candidate_python_interpreters(python: Path | None = None) -> list[tuple[Path, str]]:
    candidates: list[tuple[Path, str]] = []
    if python:
        candidates.append((python, "arg:python"))

    env_python, env_python_key = first_env_path(UX_PYTHON_ENV_KEYS)
    if env_python and env_python_key:
        candidates.append((env_python, f"env:{env_python_key}"))

    candidates.append((Path(sys.executable), "current:sys.executable"))
    resolved = shutil.which("python3")
    if resolved:
        candidates.append((Path(resolved), "path:python3"))
    candidates.append((Path("/usr/bin/python3"), "macos:system-python3"))
    return dedupe_candidates(candidates)


def probe_python_imports(python: Path, timeout: float = 10) -> tuple[str | None, tuple[str, ...], str | None]:
    code = """
import importlib.util
import json
import sys
modules = sys.argv[1:]
missing = [name for name in modules if importlib.util.find_spec(name) is None]
print(json.dumps({"version": sys.version.split()[0], "missing": missing}))
"""
    try:
        result = subprocess.run(
            [str(python), "-c", code, *UX_PYTHON_IMPORT_MODULES],
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as error:
        return None, tuple(UX_PYTHON_IMPORT_MODULES), str(error)
    if result.returncode != 0:
        return None, tuple(UX_PYTHON_IMPORT_MODULES), (result.stderr or result.stdout or "").strip()
    try:
        payload = json.loads(result.stdout)
    except json.JSONDecodeError as error:
        return None, tuple(UX_PYTHON_IMPORT_MODULES), str(error)
    missing = payload.get("missing", [])
    missing_modules = tuple(str(item) for item in missing) if isinstance(missing, list) else tuple(UX_PYTHON_IMPORT_MODULES)
    version = payload.get("version")
    return str(version) if version else None, missing_modules, None


def probe_single_ux_python(path: Path, source: str) -> UxPythonProbe:
    expanded = path.expanduser()
    if not expanded.exists():
        return UxPythonProbe(path=expanded, source=source, exists=False, executable=False)
    executable_path = expanded.absolute()
    executable = os.access(executable_path, os.X_OK)
    if not executable:
        return UxPythonProbe(path=executable_path, source=source, exists=True, executable=False)
    version, missing_modules, error = probe_python_imports(executable_path)
    return UxPythonProbe(
        path=executable_path,
        source=source,
        exists=True,
        executable=True,
        version=version,
        missing_modules=missing_modules,
        error=error,
    )


def probe_ux_python(python: Path | None = None) -> UxPythonProbe:
    if python:
        return probe_single_ux_python(python, "arg:python")

    env_python, env_python_key = first_env_path(UX_PYTHON_ENV_KEYS)
    if env_python and env_python_key:
        return probe_single_ux_python(env_python, f"env:{env_python_key}")

    fallback_path: Path | None = None
    fallback_source = "not-found"
    for path, source in candidate_python_interpreters(python):
        expanded = path.expanduser()
        if fallback_path is None:
            fallback_path = expanded
            fallback_source = source
        if expanded.exists():
            executable_path = expanded.absolute()
            executable = os.access(executable_path, os.X_OK)
            if not executable:
                return UxPythonProbe(path=executable_path, source=source, exists=True, executable=False)
            version, missing_modules, error = probe_python_imports(executable_path)
            return UxPythonProbe(
                path=executable_path,
                source=source,
                exists=True,
                executable=True,
                version=version,
                missing_modules=missing_modules,
                error=error,
            )
    return UxPythonProbe(path=fallback_path, source=fallback_source, exists=False, executable=False)


def feedback_payload(*include: str) -> dict[str, object]:
    include_items = [item for item in include if item]
    return {
        "repository": FEEDBACK_REPOSITORY,
        "issueUrl": FEEDBACK_ISSUE_URL,
        "issueTemplate": FEEDBACK_ISSUE_TEMPLATE,
        "issueGuide": FEEDBACK_ISSUE_GUIDE,
        "when": "Open a GitHub issue when the wrapper is blocked, audit output is misleading, a DevEco/UxTestService version is unsupported, or a useful workflow is missing.",
        "include": include_items
        or [
            "command line used",
            "structured JSON output",
            "DevEco Studio and UxTestService versions",
            "HDC target summary",
            "redacted summary.json / ux_summary.json",
        ],
        "redact": [
            "screenshots with private UI",
            "raw layout trees",
            "full hilog output",
            "private bundle IDs or app names",
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
    raise UxAuditPipelineError(message, payload)


def timestamp() -> str:
    return time.strftime("%Y%m%d-%H%M%S")


def ensure_not_inside_app_bundle(path: Path) -> None:
    expanded = path.expanduser()
    for part in expanded.parts:
        if part.endswith(".app"):
            block(
                "refusing to write UX audit artifacts inside an .app bundle",
                missing_config=["artifactDir"],
                artifactDir=str(expanded),
            )


def prepare_artifact_dir(artifact_dir: Path | None) -> Path:
    if artifact_dir:
        path = artifact_dir.expanduser().resolve()
    else:
        path = (Path(".hvigor") / "outputs" / f"ux-audit-pipeline-{timestamp()}").resolve()
    ensure_not_inside_app_bundle(path)
    path.mkdir(parents=True, exist_ok=True)
    return path


def prepare_ux_runtime(source_root: Path, artifact_dir: Path) -> Path:
    runtime_root = artifact_dir / "ux_service_runtime"
    if runtime_root.exists():
        shutil.rmtree(runtime_root)

    def ignore(_: str, names: list[str]) -> set[str]:
        return {name for name in names if name in {"uxlog", "__pycache__"} or name.endswith(".pyc")}

    shutil.copytree(source_root, runtime_root, ignore=ignore)
    return runtime_root


def artifact_path_from_summary(summary: dict[str, object], kind: str) -> Path | None:
    for item in summary.get("artifacts", []):
        if isinstance(item, dict) and item.get("kind") == kind and item.get("path"):
            return Path(str(item["path"])).expanduser().resolve()
    return None


def load_json(path: Path) -> object:
    return json.loads(path.expanduser().read_text(encoding="utf-8"))


def load_required_json(path: Path, description: str, missing_config: list[str]) -> object:
    try:
        return load_json(path)
    except FileNotFoundError:
        block(f"{description} was not found: {path}", missing_config=missing_config, jsonPath=str(path))
    except json.JSONDecodeError as error:
        block(
            f"{description} is not valid JSON: {path}",
            missing_config=missing_config,
            jsonPath=str(path),
            jsonError=str(error),
        )
    except OSError as error:
        block(
            f"{description} could not be read: {path}",
            missing_config=missing_config,
            jsonPath=str(path),
            readError=str(error),
        )
    raise AssertionError("unreachable")


def write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def collect_bundle_names_from_layout(layout_path: Path) -> list[str]:
    try:
        data = load_json(layout_path)
    except (OSError, json.JSONDecodeError):
        return []
    names: set[str] = set()

    def visit(value: object) -> None:
        if isinstance(value, dict):
            for key in ("bundleName", "bundle_name", "bundle"):
                bundle = value.get(key)
                if isinstance(bundle, str) and bundle:
                    names.add(bundle)
            for child in value.values():
                visit(child)
        elif isinstance(value, list):
            for item in value:
                visit(item)

    visit(data)
    return sorted(names)


def choose_bundle_name(
    explicit_bundle: str | None,
    evidence_summary: dict[str, object] | None,
    layout_path: Path,
) -> tuple[str, list[str]]:
    candidates: list[str] = []
    if explicit_bundle:
        return explicit_bundle, [explicit_bundle]
    if evidence_summary:
        bundle = evidence_summary.get("bundle")
        if isinstance(bundle, str) and bundle:
            candidates.append(bundle)
        layout_summary = evidence_summary.get("layoutSummary")
        if isinstance(layout_summary, dict):
            for name in layout_summary.get("bundleNames", []):
                if isinstance(name, str) and name:
                    candidates.append(name)
    candidates.extend(collect_bundle_names_from_layout(layout_path))
    deduped = list(dict.fromkeys(candidates))
    for name in deduped:
        if name not in SYSTEM_BUNDLE_NAMES and not name.startswith("com.ohos."):
            return name, deduped
    if deduped:
        block(
            "cannot infer foreground app bundle name from evidence; pass --bundle",
            missing_config=["bundleName"],
            bundleCandidates=deduped,
        )
    block("cannot infer foreground bundle name from evidence; pass --bundle", missing_config=["bundleName"])
    raise AssertionError("unreachable")


def build_check_param(
    layout_path: Path,
    screenshot_path: Path,
    bundle_name: str,
    ux_runtime_root: Path,
    task_id: str,
    test_codes: list[str],
    device_name: str,
    device_type: str,
    scale: float,
    dpi: float,
    dark_mode: bool,
    is_home_page: bool,
    language: str,
    level_second: str,
    level_third: str,
) -> dict[str, object]:
    page_id = "CAPTURE_PAGE"
    attribute = {
        "is_home_page": is_home_page,
        "dark_mode": dark_mode,
        "level": 1,
        "scene": [],
        "device_name": device_name,
        "device_type": device_type,
        "bundle_name": bundle_name,
        "is_emulator": True,
        "scale": scale,
        "detect_mode": "IDE",
        "dpi": dpi,
    }
    return {
        "page_infos": {
            page_id: {
                "attribute": attribute,
                "detail_infos": [
                    {
                        "state": "ori_state",
                        "json_path": str(layout_path),
                        "img_path": str(screenshot_path),
                        "ark_img_path": "",
                        "ark_json_path": "",
                        "direction": "natural",
                    }
                ],
            }
        },
        "record_infos": [],
        "hap_path": [],
        "device_type": device_type,
        "task_id": task_id,
        "resource_path": str(ux_runtime_root / "resource"),
        "extend_infos": {
            "language": language,
            "levelSecond": level_second,
            "levelThird": level_third,
        },
        "test_code": test_codes,
        "bundle_name": bundle_name,
        "detect_mode": "IDE",
        "device_name": device_name,
        "task_type": "UxTest",
        "request_id": f"{task_id}_req",
        "is_emulator": True,
        "dpi": dpi,
        "scale": scale,
    }


def run_ux_service(
    python: Path,
    ux_runtime_root: Path,
    check_param_path: Path,
    result_path: Path,
    stdout_path: Path,
    stderr_path: Path,
    timeout: float,
) -> dict[str, object]:
    code = r"""
import json
import os
import sys
ux_root, check_param_path, result_path = sys.argv[1:4]
os.chdir(ux_root)
sys.path.insert(0, ux_root)
with open(check_param_path, "r", encoding="utf-8") as handle:
    check_param = json.load(handle)
import ux_detect
result = ux_detect.main(check_param=check_param)
with open(result_path, "w", encoding="utf-8") as handle:
    json.dump(result, handle, ensure_ascii=False, indent=2)
    handle.write("\n")
"""
    command = [str(python), "-c", code, str(ux_runtime_root), str(check_param_path), str(result_path)]
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=timeout, check=False)
    except subprocess.TimeoutExpired as error:
        stdout_path.write_text(error.stdout if isinstance(error.stdout, str) else "", encoding="utf-8")
        stderr_path.write_text(error.stderr if isinstance(error.stderr, str) else f"timed out after {timeout:g}s", encoding="utf-8")
        block(
            f"UxTestService timed out after {timeout:g}s",
            missing_config=[],
            command=command,
            stdout=str(stdout_path),
            stderr=str(stderr_path),
        )
    stdout_path.write_text(result.stdout or "", encoding="utf-8")
    stderr_path.write_text(result.stderr or "", encoding="utf-8")
    if result.returncode != 0:
        missing_module_match = re.search(r"ModuleNotFoundError: No module named ['\"]([^'\"]+)['\"]", result.stderr or "")
        if missing_module_match:
            block(
                f"UxTestService Python dependency is missing: {missing_module_match.group(1)}",
                missing_config=["uxPythonDependencies"],
                command=command,
                stdout=str(stdout_path),
                stderr=str(stderr_path),
                missingModule=missing_module_match.group(1),
                stderrSnippet=(result.stderr or "")[-2000:],
            )
        block(
            f"UxTestService failed with exit code {result.returncode}",
            missing_config=[],
            command=command,
            stdout=str(stdout_path),
            stderr=str(stderr_path),
            stderrSnippet=(result.stderr or "")[-2000:],
        )
    if not result_path.is_file():
        block("UxTestService completed but did not write result JSON", missing_config=[], command=command)
    return {"command": command, "exitCode": result.returncode, "stdout": str(stdout_path), "stderr": str(stderr_path)}


def summarize_ux_results(result_path: Path) -> dict[str, object]:
    result = load_json(result_path)
    if not isinstance(result, list):
        block("UxTestService result JSON is not a list", missing_config=[], resultPath=str(result_path))
    counts: dict[str, int] = {}
    items: list[dict[str, object]] = []
    generated_paths: list[str] = []
    issue_items: list[dict[str, object]] = []
    for item in result:
        if not isinstance(item, dict):
            continue
        state = str(item.get("test_state", "unknown"))
        counts[state] = counts.get(state, 0) + 1
        detail = item.get("detail")
        detail = detail if isinstance(detail, dict) else {}
        paths = [detail.get("PassPath"), detail.get("ErrorPath"), detail.get("CustomDrawPath")]
        for path in paths:
            if isinstance(path, str) and path:
                generated_paths.append(path)
        issues = detail.get("Issues")
        issue_count = len(issues) if isinstance(issues, list) else 0
        summary_item = {
            "code": item.get("code", ""),
            "subRuleName": item.get("sub_rule_name", ""),
            "testState": item.get("test_state"),
            "errorCode": detail.get("ErrorCode", ""),
            "errorType": detail.get("ErrorType", ""),
            "message": detail.get("ErrorMsg") or item.get("reason", ""),
            "issues": issue_count,
            "passPath": bool(detail.get("PassPath")),
            "errorPath": bool(detail.get("ErrorPath")),
            "customDrawPath": bool(detail.get("CustomDrawPath")),
        }
        items.append(summary_item)
        if item.get("test_state") == 1 or issue_count:
            issue_items.append(summary_item)
    return {
        "counts": counts,
        "total": sum(counts.values()),
        "passCount": counts.get("0", 0),
        "issueCount": counts.get("1", 0),
        "ignoredCount": counts.get("2", 0),
        "exceptionCount": counts.get("4", 0) + counts.get("5", 0),
        "items": items,
        "issueItems": issue_items,
        "generatedPaths": sorted(set(generated_paths)),
    }


def write_markdown_report(path: Path, summary: dict[str, object], pipeline_payload: dict[str, object]) -> None:
    counts = summary.get("counts", {})
    feedback = pipeline_payload.get("feedback")
    lines = [
        "# HarmonyOS UI/UX Audit Report",
        "",
        f"- decision: `{pipeline_payload.get('decision')}`",
        f"- bundle: `{pipeline_payload.get('bundleName')}`",
        f"- target: `{pipeline_payload.get('target') or 'offline'}`",
        f"- evidence: `{pipeline_payload.get('evidenceSummary') or pipeline_payload.get('captureSummary') or ''}`",
        f"- result: `{pipeline_payload.get('uxResult')}`",
        "",
        "## Counts",
        "",
        f"- pass: `{summary.get('passCount', 0)}`",
        f"- issue: `{summary.get('issueCount', 0)}`",
        f"- ignored/no target: `{summary.get('ignoredCount', 0)}`",
        f"- exception/error: `{summary.get('exceptionCount', 0)}`",
        f"- raw states: `{counts}`",
        "",
        "## Items",
        "",
        "| code | rule | state | issues | message |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in summary.get("items", []):
        if not isinstance(item, dict):
            continue
        message = str(item.get("message", "")).replace("\n", " ").replace("|", "\\|")[:160]
        rule = str(item.get("subRuleName", "")).replace("|", "\\|")
        lines.append(
            f"| `{item.get('code', '')}` | {rule} | `{item.get('testState', '')}` | `{item.get('issues', 0)}` | {message} |"
        )
    if isinstance(feedback, dict):
        include_items = feedback.get("include", [])
        redact_items = feedback.get("redact", [])
        lines.extend(
            [
                "",
                "## Feedback",
                "",
                f"- repository: `{feedback.get('repository', '')}`",
                f"- issue: {feedback.get('issueUrl', '')}",
                f"- template: `{feedback.get('issueTemplate', '')}`",
                f"- guide: `{feedback.get('issueGuide', '')}`",
                f"- when: {feedback.get('when', '')}",
                "",
                "Include after redaction:",
            ]
        )
        if isinstance(include_items, list):
            lines.extend(f"- {item}" for item in include_items)
        lines.extend(["", "Redact before sharing:"])
        if isinstance(redact_items, list):
            lines.extend(f"- {item}" for item in redact_items)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def resolve_audit_inputs(args: argparse.Namespace) -> tuple[dict[str, object] | None, Path, Path]:
    evidence_summary: dict[str, object] | None = None
    if args.evidence_summary:
        evidence_summary_path = args.evidence_summary.expanduser().resolve()
        evidence_summary = load_required_json(evidence_summary_path, "evidence summary", ["evidenceSummary"])
        if not isinstance(evidence_summary, dict):
            block(
                "evidence summary is not a JSON object",
                missing_config=["evidenceSummary"],
                jsonPath=str(evidence_summary_path),
            )
        layout_path = artifact_path_from_summary(evidence_summary, "layout")
        screenshot_path = artifact_path_from_summary(evidence_summary, "screenshot")
    elif args.evidence_dir:
        summary_path = args.evidence_dir.expanduser().resolve() / "summary.json"
        evidence_summary = load_required_json(summary_path, "evidence summary", ["evidenceSummary"])
        if not isinstance(evidence_summary, dict):
            block(
                "evidence summary is not a JSON object",
                missing_config=["evidenceSummary"],
                jsonPath=str(summary_path),
            )
        layout_path = artifact_path_from_summary(evidence_summary, "layout")
        screenshot_path = artifact_path_from_summary(evidence_summary, "screenshot")
    else:
        layout_path = args.layout.expanduser().resolve() if args.layout else None
        screenshot_path = args.screenshot.expanduser().resolve() if args.screenshot else None

    if not layout_path or not layout_path.is_file():
        block("layout JSON is required for UX audit", missing_config=["layout"])
    if not screenshot_path or not screenshot_path.is_file():
        block("screenshot PNG is required for UX audit", missing_config=["screenshot"])
    return evidence_summary, layout_path, screenshot_path


def run_audit(args: argparse.Namespace, capture_payload: dict[str, object] | None = None) -> dict[str, object]:
    artifact_dir = prepare_artifact_dir(args.artifact_dir)
    if capture_payload:
        evidence_summary = capture_payload
        layout_path = artifact_path_from_summary(evidence_summary, "layout")
        screenshot_path = artifact_path_from_summary(evidence_summary, "screenshot")
        if not layout_path or not layout_path.is_file():
            block("captured evidence did not include layout JSON", missing_config=["layout"], captureSummary=capture_payload.get("summary"))
        if not screenshot_path or not screenshot_path.is_file():
            block("captured evidence did not include screenshot", missing_config=["screenshot"], captureSummary=capture_payload.get("summary"))
    else:
        evidence_summary, layout_path, screenshot_path = resolve_audit_inputs(args)

    probe = probe_ux_service(args.ux_service_root, args.deveco_app)
    if not probe.exists:
        block(f"UxTestService was not found: {probe.path}", missing_config=["uxServiceRoot"], uxService=probe.to_json())
    if not probe.runnable:
        block(f"UxTestService is missing ux_detect.py or checkMethod/: {probe.path}", missing_config=["uxServiceRunnable"], uxService=probe.to_json())
    assert probe.path is not None

    python_probe = probe_ux_python(args.python)
    if not python_probe.exists:
        block(f"Python for UxTestService was not found: {python_probe.path}", missing_config=["uxPython"], uxPython=python_probe.to_json())
    if not python_probe.executable:
        block(f"Python for UxTestService is not executable: {python_probe.path}", missing_config=["uxPython"], uxPython=python_probe.to_json())
    assert python_probe.path is not None

    bundle_name, bundle_candidates = choose_bundle_name(args.bundle, evidence_summary, layout_path)
    ux_runtime_root = prepare_ux_runtime(probe.path, artifact_dir)
    task_id = args.task_id or f"ux_audit_{timestamp()}"
    test_codes = args.test_code or DEFAULT_TEST_CODES
    check_param = build_check_param(
        layout_path=layout_path,
        screenshot_path=screenshot_path,
        bundle_name=bundle_name,
        ux_runtime_root=ux_runtime_root,
        task_id=task_id,
        test_codes=test_codes,
        device_name=args.device_name,
        device_type=args.device_type,
        scale=args.scale,
        dpi=args.dpi,
        dark_mode=args.dark_mode,
        is_home_page=args.is_home_page,
        language=args.language,
        level_second=args.level_second,
        level_third=args.level_third,
    )
    check_param_path = artifact_dir / "check_param.json"
    result_path = artifact_dir / "ux_result.json"
    stdout_path = artifact_dir / "ux_stdout.txt"
    stderr_path = artifact_dir / "ux_stderr.txt"
    write_json(check_param_path, check_param)
    ux_run = run_ux_service(
        python_probe.path,
        ux_runtime_root,
        check_param_path,
        result_path,
        stdout_path,
        stderr_path,
        args.ux_timeout,
    )
    ux_summary = summarize_ux_results(result_path)
    ux_summary_path = artifact_dir / "ux_summary.json"
    write_json(ux_summary_path, ux_summary)

    payload: dict[str, object] = {
        "decision": "audited",
        "operation": "ux.audit.pipeline",
        "artifactDir": str(artifact_dir),
        "target": capture_payload.get("target") if capture_payload else (evidence_summary or {}).get("target") if evidence_summary else None,
        "bundleName": bundle_name,
        "bundleCandidates": bundle_candidates,
        "layout": str(layout_path),
        "screenshot": str(screenshot_path),
        "captureSummary": capture_payload.get("summary") if capture_payload else None,
        "evidenceSummary": (evidence_summary or {}).get("summary") if evidence_summary else None,
        "uxService": probe.to_json(),
        "uxPython": python_probe.to_json(),
        "uxRuntimeRoot": str(ux_runtime_root),
        "checkParam": str(check_param_path),
        "uxResult": str(result_path),
        "uxSummary": str(ux_summary_path),
        "uxRun": ux_run,
        "resultCounts": ux_summary.get("counts", {}),
        "rawSensitiveContentStored": True,
        "notes": [
            "The pipeline stores raw local screenshot/layout/log-derived evidence and UxTestService marked images.",
            "UxTestService is run from an artifact-local copy so the DevEco .app bundle is not modified.",
        ],
    }
    report_path = artifact_dir / "report.md"
    summary_path = artifact_dir / "summary.json"
    payload["report"] = str(report_path)
    payload["summary"] = str(summary_path)
    payload["feedback"] = feedback_payload(
        str(summary_path),
        str(ux_summary_path),
        str(report_path),
        "redacted ux_stdout.txt / ux_stderr.txt snippets when failures occur",
        "DevEco Studio and UxTestService versions from uxService",
        "foreground bundle only if it is safe to disclose",
    )
    write_markdown_report(report_path, ux_summary, payload)
    write_json(summary_path, payload)
    return payload


def run_capture_audit(args: argparse.Namespace) -> dict[str, object]:
    artifact_dir = prepare_artifact_dir(args.artifact_dir)
    capture_dir = artifact_dir / "capture"
    audit_dir = artifact_dir / "audit"
    capture_args = argparse.Namespace(
        hdc=args.hdc,
        deveco_app=args.deveco_app,
        timeout=args.timeout,
        target=args.target,
        bundle=args.bundle,
        artifact_dir=capture_dir,
        policy="evidence",
        redaction_policy=args.redaction_policy,
        hilog_lines=args.hilog_lines,
        skip_hilog=args.skip_hilog,
        skip_layout=False,
        skip_screenshot=False,
        no_cleanup=False,
        json=True,
    )
    capture_payload = device_evidence_bundle.run_capture(capture_args)
    audit_args = argparse.Namespace(**vars(args))
    audit_args.artifact_dir = audit_dir
    audit_payload = run_audit(audit_args, capture_payload=capture_payload)
    payload = {
        "decision": "completed",
        "operation": "ux.capture-audit.pipeline",
        "artifactDir": str(artifact_dir),
        "captureSummary": capture_payload.get("summary"),
        "auditSummary": audit_payload.get("summary"),
        "report": audit_payload.get("report"),
        "target": capture_payload.get("target"),
        "bundleName": audit_payload.get("bundleName"),
        "resultCounts": audit_payload.get("resultCounts", {}),
        "rawSensitiveContentStored": True,
    }
    summary_path = artifact_dir / "summary.json"
    payload["summary"] = str(summary_path)
    payload["feedback"] = feedback_payload(
        str(summary_path),
        str(capture_payload.get("summary") or ""),
        str(audit_payload.get("summary") or ""),
        str(audit_payload.get("report") or ""),
        "redacted resultCounts and bundleName if safe to disclose",
    )
    write_json(summary_path, payload)
    return payload


def run_doctor(args: argparse.Namespace) -> tuple[int, dict[str, object]]:
    ux_probe = probe_ux_service(args.ux_service_root, args.deveco_app)
    python_probe = probe_ux_python(args.python)
    hdc_exit, hdc_payload = device_evidence_bundle.run_doctor(args)
    missing_config: list[str] = []
    issues: list[str] = []
    if not ux_probe.exists:
        missing_config.append("uxServiceRoot")
        issues.append("UxTestService was not found")
    elif not ux_probe.runnable:
        missing_config.append("uxServiceRunnable")
        issues.append("UxTestService is missing ux_detect.py or checkMethod/")
    if not python_probe.exists:
        missing_config.append("uxPython")
        issues.append("Python for UxTestService was not found")
    elif not python_probe.executable:
        missing_config.append("uxPython")
        issues.append("Python for UxTestService is not executable")
    elif python_probe.missing_modules:
        missing_config.append("uxPythonDependencies")
        issues.append("Python for UxTestService is missing modules: " + ", ".join(python_probe.missing_modules))
    elif python_probe.error:
        missing_config.append("uxPythonDependencies")
        issues.append("Python dependency probe failed: " + python_probe.error)
    if hdc_exit != 0:
        missing_config.extend(str(item) for item in hdc_payload.get("missingConfig", []))
        issues.extend(str(item) for item in hdc_payload.get("issues", []))
    payload = {
        "decision": "allowed" if not missing_config else "blocked",
        "operation": "ux.capture-audit.doctor",
        "uxService": ux_probe.to_json(),
        "uxPython": python_probe.to_json(),
        "hdc": hdc_payload.get("hdc"),
        "connectedTargets": hdc_payload.get("connectedTargets", []),
        "missingConfig": list(dict.fromkeys(missing_config)),
        "issues": issues,
        "recommendations": [
            "Use capture-audit with --target and --artifact-dir for a one-shot device UI/UX report.",
            "Use audit with --evidence-summary when re-running UxTestService against an existing evidence bundle.",
            "Review or redact raw screenshots, layouts, logs, and marked images before sharing artifacts.",
            *OFFICIAL_CLI_FALLBACK_RECOMMENDATIONS,
        ],
        "feedback": feedback_payload("doctor JSON output", "uxService / uxPython fields", "connectedTargets with private labels redacted"),
    }
    return (0 if not missing_config else 2), payload


def add_common_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--deveco-app", type=Path, help="Path to DevEco-Studio.app or its Contents directory")
    parser.add_argument("--ux-service-root", type=Path, help="Path to tools/UxTestService")
    parser.add_argument("--python", type=Path, help="Python interpreter used to run UxTestService")
    parser.add_argument("--timeout", type=float, default=10, help="Per-HDC-command timeout in seconds")
    parser.add_argument("--ux-timeout", type=float, default=180, help="UxTestService timeout in seconds")


def add_audit_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--bundle", help="Foreground bundle name; inferred from layout/evidence when omitted")
    parser.add_argument("--test-code", action="append", help="UxTestService rule code; repeat to override defaults")
    parser.add_argument("--device-name", default="ALN")
    parser.add_argument("--device-type", default="phone")
    parser.add_argument("--scale", type=float, default=3.0)
    parser.add_argument("--dpi", type=float, default=480.0)
    parser.add_argument("--language", default="zh", choices=["zh", "en"])
    parser.add_argument("--level-second", default="Utilities")
    parser.add_argument("--level-third", default="Communication")
    parser.add_argument("--dark-mode", action="store_true")
    parser.add_argument("--is-home-page", action="store_true")
    parser.add_argument("--task-id")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Capture HarmonyOS UI evidence, run DevEco UxTestService, and write a report.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    doctor = subparsers.add_parser("doctor", help="Validate hdc and UxTestService availability")
    add_common_arguments(doctor)
    doctor.add_argument("--hdc", type=Path, help="Path to hdc")
    doctor.add_argument("--json", action="store_true")

    audit = subparsers.add_parser("audit", help="Run UxTestService against an existing evidence bundle or local files")
    add_common_arguments(audit)
    add_audit_arguments(audit)
    audit.add_argument("--artifact-dir", type=Path, help="Output directory; defaults to .hvigor/outputs/ux-audit-pipeline-*")
    audit.add_argument("--evidence-summary", type=Path, help="Path to device_evidence_bundle summary.json")
    audit.add_argument("--evidence-dir", type=Path, help="Directory containing device_evidence_bundle summary.json")
    audit.add_argument("--layout", type=Path, help="Layout JSON when not using --evidence-summary")
    audit.add_argument("--screenshot", type=Path, help="Screenshot PNG when not using --evidence-summary")
    audit.add_argument("--json", action="store_true")

    capture_audit = subparsers.add_parser("capture-audit", help="Capture HDC evidence and immediately run UxTestService")
    add_common_arguments(capture_audit)
    add_audit_arguments(capture_audit)
    capture_audit.add_argument("--hdc", type=Path, help="Path to hdc")
    capture_audit.add_argument("--target", help="HDC target, for example 127.0.0.1:10100")
    capture_audit.add_argument("--artifact-dir", type=Path, help="Output directory; defaults to .hvigor/outputs/ux-audit-pipeline-*")
    capture_audit.add_argument("--redaction-policy", default=device_evidence_bundle.DEFAULT_REDACTION_POLICY)
    capture_audit.add_argument("--hilog-lines", type=int, default=100)
    capture_audit.add_argument("--skip-hilog", action="store_true")
    capture_audit.add_argument("--json", action="store_true")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        if args.command == "doctor":
            exit_code, payload = run_doctor(args)
        elif args.command == "audit":
            payload = run_audit(args)
            exit_code = 0
        elif args.command == "capture-audit":
            payload = run_capture_audit(args)
            exit_code = 0
        else:
            parser.error(f"Unknown command: {args.command}")
            return 2
        if args.json:
            print_json(payload)
        else:
            print(json.dumps(payload, ensure_ascii=False))
        return exit_code
    except (UxAuditPipelineError, device_evidence_bundle.DeviceEvidenceError) as error:
        payload = getattr(error, "payload", None) or {"decision": "blocked", "error": str(error), "missingConfig": []}
        if getattr(args, "json", False):
            print_json(payload)
        else:
            print(f"blocked: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
