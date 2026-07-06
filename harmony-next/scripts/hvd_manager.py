#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import platform
import re
import shutil
import socket
import subprocess
import sys
import tempfile
import time
import uuid
from dataclasses import asdict, dataclass
from pathlib import Path


DEFAULT_HVD_ROOT = Path.home() / ".Huawei" / "Emulator" / "deployed"
HVD_ROOT_ENV_KEYS = ["HARMONY_HVD_ROOT", "DEVECO_HVD_ROOT", "HVD_ROOT"]
EMULATOR_ENV_KEYS = ["HARMONY_EMULATOR", "DEVECO_EMULATOR", "EMULATOR"]
SDK_ROOT_ENV_KEYS = ["DEVECO_SDK_HOME", "HOS_SDK_HOME", "HARMONY_SDK_HOME"]
IMAGE_ROOT_ENV_KEYS = ["HARMONY_EMULATOR_IMAGE_ROOT", "DEVECO_IMAGE_ROOT", "HARMONY_IMAGE_ROOT"]
HDC_ENV_KEYS = ["HARMONY_HDC", "DEVECO_HDC", "HDC"]
NAME_PATTERN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9 _.-]{0,63}$")
TRACE_NAME_PATTERN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]{0,63}$")
LOGIN_GATED_MODAL_SYMPTOM = "模拟器启动失败 / 请在DevEco Studio中登录华为账号，并从设备管理中启动模拟器"
LICENSE_AGREEMENT_RESULT = "license-agreement-required"


class HvdManagerError(RuntimeError):
    pass


@dataclass(frozen=True)
class PathProbe:
    path: Path | None
    source: str
    exists: bool
    executable: bool = False

    def to_json(self) -> dict[str, object]:
        return {
            "path": str(self.path) if self.path else None,
            "source": self.source,
            "exists": self.exists,
            "executable": self.executable,
        }


@dataclass(frozen=True)
class HvdInfo:
    name: str
    path: Path
    root_ini: Path
    device_type: str | None = None
    api_version: str | None = None
    uuid: str | None = None
    hdc_port: str | None = None
    image_sub_path: str | None = None
    exists: bool = True

    def to_json(self) -> dict[str, object]:
        data = asdict(self)
        data["path"] = str(self.path)
        data["root_ini"] = str(self.root_ini)
        data.pop("uuid", None)
        return data


def first_env_path(keys: list[str]) -> tuple[Path | None, str | None]:
    for key in keys:
        value = os.environ.get(key)
        if value:
            return Path(value).expanduser(), key
    return None, None


def default_hvd_root() -> Path:
    env_path, _ = first_env_path(HVD_ROOT_ENV_KEYS)
    return env_path or DEFAULT_HVD_ROOT


def candidate_hvd_roots() -> list[tuple[Path, str]]:
    env_path, env_key = first_env_path(HVD_ROOT_ENV_KEYS)
    candidates: list[tuple[Path, str]] = []
    if env_path and env_key:
        candidates.append((env_path, f"env:{env_key}"))
    candidates.append((Path.home() / ".Huawei" / "Emulator" / "deployed", "default:user-home"))
    return dedupe_candidates(candidates)


def candidate_emulators() -> list[tuple[Path, str]]:
    env_path, env_key = first_env_path(EMULATOR_ENV_KEYS)
    candidates: list[tuple[Path, str]] = []
    if env_path and env_key:
        candidates.append((env_path, f"env:{env_key}"))

    system = platform.system()
    if system == "Darwin":
        candidates.extend(
            [
                (Path("/Applications/DevEco-Studio.app/Contents/tools/emulator/Emulator"), "macos:default-app"),
                (Path("/Applications/DevEco-Studio.app/Contents/tools/emulator/emulator"), "macos:default-app"),
            ]
        )
    elif system == "Windows":
        for root_env in ["ProgramFiles", "ProgramFiles(x86)", "LOCALAPPDATA"]:
            base = os.environ.get(root_env)
            if base:
                candidates.extend(
                    [
                        (Path(base) / "Huawei" / "DevEco Studio" / "tools" / "emulator" / "Emulator.exe", f"windows:{root_env}"),
                        (Path(base) / "DevEco-Studio" / "tools" / "emulator" / "Emulator.exe", f"windows:{root_env}"),
                    ]
                )
    else:
        candidates.extend(
            [
                (Path("/opt/DevEco-Studio/tools/emulator/Emulator"), "linux:/opt"),
                (Path("/opt/deveco-studio/tools/emulator/Emulator"), "linux:/opt"),
            ]
        )

    for name in ["Emulator", "emulator", "Emulator.exe", "emulator.exe"]:
        resolved = shutil.which(name)
        if resolved:
            candidates.append((Path(resolved), f"path:{name}"))
    return dedupe_candidates(candidates)


def candidate_sdk_roots() -> list[tuple[Path, str]]:
    env_path, env_key = first_env_path(SDK_ROOT_ENV_KEYS)
    candidates: list[tuple[Path, str]] = []
    if env_path and env_key:
        candidates.append((env_path, f"env:{env_key}"))

    system = platform.system()
    if system == "Darwin":
        candidates.append((Path("/Applications/DevEco-Studio.app/Contents/sdk"), "macos:default-app"))
    elif system == "Windows":
        for root_env in ["ProgramFiles", "ProgramFiles(x86)", "LOCALAPPDATA"]:
            base = os.environ.get(root_env)
            if base:
                candidates.extend(
                    [
                        (Path(base) / "Huawei" / "DevEco Studio" / "sdk", f"windows:{root_env}"),
                        (Path(base) / "DevEco-Studio" / "sdk", f"windows:{root_env}"),
                    ]
                )
    else:
        candidates.extend(
            [
                (Path("/opt/DevEco-Studio/sdk"), "linux:/opt"),
                (Path("/opt/deveco-studio/sdk"), "linux:/opt"),
            ]
        )
    return dedupe_candidates(candidates)


def candidate_image_roots() -> list[tuple[Path, str]]:
    env_path, env_key = first_env_path(IMAGE_ROOT_ENV_KEYS)
    candidates: list[tuple[Path, str]] = []
    if env_path and env_key:
        candidates.append((env_path, f"env:{env_key}"))

    system = platform.system()
    if system == "Darwin":
        candidates.append((Path.home() / "Library" / "Huawei" / "Sdk", "macos:user-emulator-images"))
    elif system == "Windows":
        local_app_data = os.environ.get("LOCALAPPDATA")
        if local_app_data:
            candidates.append((Path(local_app_data) / "Huawei" / "Sdk", "windows:LOCALAPPDATA"))
    else:
        candidates.append((Path.home() / ".Huawei" / "Sdk", "linux:user-emulator-images"))
    return dedupe_candidates(candidates)


def candidate_hdcs(sdk_root: Path | None = None) -> list[tuple[Path, str]]:
    env_path, env_key = first_env_path(HDC_ENV_KEYS)
    candidates: list[tuple[Path, str]] = []
    if env_path and env_key:
        candidates.append((env_path, f"env:{env_key}"))
    if sdk_root:
        candidates.append((sdk_root / "default" / "openharmony" / "toolchains" / "hdc", "arg:sdk-root"))

    for root, source in candidate_sdk_roots():
        candidates.append((root / "default" / "openharmony" / "toolchains" / "hdc", source))

    resolved = shutil.which("hdc")
    if resolved:
        candidates.append((Path(resolved), "path:hdc"))
    return dedupe_candidates(candidates)


def dedupe_candidates(candidates: list[tuple[Path, str]]) -> list[tuple[Path, str]]:
    seen: set[str] = set()
    deduped: list[tuple[Path, str]] = []
    for path, source in candidates:
        key = str(path.expanduser())
        if key not in seen:
            seen.add(key)
            deduped.append((path, source))
    return deduped


def probe_first_existing(candidates: list[tuple[Path, str]], executable: bool = False) -> PathProbe:
    fallback_path: Path | None = None
    fallback_source = "not-found"
    for path, source in candidates:
        expanded = path.expanduser()
        if fallback_path is None:
            fallback_path = expanded
            fallback_source = source
        if expanded.exists():
            return PathProbe(
                path=expanded.resolve(),
                source=source,
                exists=True,
                executable=os.access(expanded, os.X_OK) if executable else False,
            )
    return PathProbe(path=fallback_path, source=fallback_source, exists=False, executable=False)


def run_version_command(executable: Path) -> dict[str, object]:
    try:
        result = subprocess.run([str(executable), "-version"], capture_output=True, text=True, check=False, timeout=10)
    except OSError as error:
        return {"ok": False, "error": str(error)}
    except subprocess.TimeoutExpired:
        return {"ok": False, "error": "version command timed out"}
    output = (result.stdout or result.stderr).strip()
    return {"ok": result.returncode == 0, "exitCode": result.returncode, "output": output[:2000]}


def run_doctor(root: Path | None = None, emulator: Path | None = None, sdk_root: Path | None = None) -> dict[str, object]:
    root_candidates = [(root, "arg:root")] if root else candidate_hvd_roots()
    emulator_candidates = [(emulator, "arg:emulator")] if emulator else candidate_emulators()
    sdk_candidates = [(sdk_root, "arg:sdk-root")] if sdk_root else candidate_sdk_roots()

    root_probe = probe_first_existing(root_candidates)
    emulator_probe = probe_first_existing(emulator_candidates, executable=True)
    sdk_probe = probe_first_existing(sdk_candidates)
    image_root_probe = probe_first_existing(candidate_image_roots())
    hdc_probe = probe_first_existing(candidate_hdcs(sdk_root), executable=True)

    issues: list[str] = []
    recommendations: list[str] = []
    hvds: list[HvdInfo] = []

    if root_probe.path and root_probe.exists and root_probe.path.is_dir():
        try:
            hvds = list_hvds(root_probe.path)
        except HvdManagerError as error:
            issues.append(str(error))
    else:
        issues.append("HVD root was not found")
        recommendations.append("Create an HVD in DevEco Studio first, or pass --root / set HARMONY_HVD_ROOT.")

    if not emulator_probe.exists:
        issues.append("Emulator executable was not found")
        recommendations.append("Pass --emulator or set HARMONY_EMULATOR to DevEco Studio tools/emulator/Emulator.")
    elif not emulator_probe.executable:
        issues.append(f"Emulator is not executable: {emulator_probe.path}")

    if not sdk_probe.exists:
        recommendations.append("Pass --sdk-root or set DEVECO_SDK_HOME when launch workflows need SDK image roots.")

    payload: dict[str, object] = {
        "platform": {
            "system": platform.system(),
            "machine": platform.machine(),
            "python": platform.python_version(),
        },
        "hvdRoot": root_probe.to_json(),
        "emulator": emulator_probe.to_json(),
        "sdkRoot": sdk_probe.to_json(),
        "imageRoot": image_root_probe.to_json(),
        "hdc": hdc_probe.to_json(),
        "hvdCount": len(hvds),
        "hvds": [hvd.to_json() for hvd in hvds],
        "issues": issues,
        "recommendations": recommendations,
    }
    if emulator_probe.path and emulator_probe.exists and emulator_probe.executable:
        payload["emulatorVersion"] = run_version_command(emulator_probe.path)
    return payload


def validate_name(name: str) -> None:
    if not NAME_PATTERN.fullmatch(name):
        raise HvdManagerError(
            "HVD name must be 1-64 chars and contain only letters, numbers, spaces, dots, underscores, or hyphens"
        )
    if "/" in name or "\\" in name or name in {".", ".."}:
        raise HvdManagerError("HVD name must not contain path separators")


def normalize_root(root: Path) -> Path:
    return root.expanduser().resolve()


def ensure_root(root: Path) -> Path:
    root = normalize_root(root)
    if not root.exists():
        raise HvdManagerError(f"HVD root does not exist: {root}")
    if not root.is_dir():
        raise HvdManagerError(f"HVD root is not a directory: {root}")
    return root


def read_ini(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    if not path.exists():
        return values
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or stripped.startswith(";") or stripped.startswith("["):
            continue
        key, separator, value = stripped.partition("=")
        if separator:
            values[key.strip()] = value.strip()
    return values


def read_sectionless_ini(path: Path) -> dict[str, str]:
    return read_ini(path)


def write_ini(path: Path, values: dict[str, str], key_order: list[str] | None = None) -> None:
    ordered_keys: list[str] = []
    for key in key_order or []:
        if key in values and key not in ordered_keys:
            ordered_keys.append(key)
    ordered_keys.extend(key for key in values if key not in ordered_keys)
    text = "".join(f"{key}={values[key]}\n" for key in ordered_keys)
    path.write_text(text, encoding="utf-8")


def update_key_value_file(path: Path, updates: dict[str, str]) -> None:
    if not path.exists():
        return
    seen: set[str] = set()
    output: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        key, separator, _ = stripped.partition("=")
        if separator and key in updates:
            output.append(f"{key}={updates[key]}")
            seen.add(key)
        else:
            output.append(line)
    for key, value in updates.items():
        if key not in seen:
            output.append(f"{key}={value}")
    path.write_text("\n".join(output) + "\n", encoding="utf-8")


def list_hvds(root: Path = DEFAULT_HVD_ROOT) -> list[HvdInfo]:
    root = ensure_root(root)
    hvds: list[HvdInfo] = []
    for root_ini in sorted(root.glob("*.ini")):
        root_values = read_ini(root_ini)
        name = root_ini.stem
        hvd_path = Path(root_values.get("path", root / name)).expanduser()
        if not hvd_path.is_absolute():
            hvd_path = root / hvd_path
        config = read_ini(hvd_path / "config.ini")
        hvds.append(
            HvdInfo(
                name=config.get("name", name),
                path=hvd_path,
                root_ini=root_ini,
                device_type=config.get("deviceType"),
                api_version=config.get("os.apiVersion"),
                uuid=config.get("uuid"),
                hdc_port=config.get("hw.hdc.port"),
                image_sub_path=config.get("imageSubPath"),
                exists=hvd_path.exists(),
            )
        )
    return hvds


def find_hvd(root: Path, name: str) -> HvdInfo:
    validate_name(name)
    for hvd in list_hvds(root):
        if hvd.name == name or hvd.root_ini.stem == name:
            return hvd
    raise HvdManagerError(f"HVD not found: {name}")


def copy_source_tree(source: Path, destination: Path, include_logs: bool) -> None:
    ignore = None
    if not include_logs:
        ignore = shutil.ignore_patterns("Log", "*.log")
    shutil.copytree(source, destination, ignore=ignore)


def update_lists_json(root: Path, source_name: str, new_name: str, new_path: Path, new_uuid: str) -> None:
    lists_path = root / "lists.json"
    if not lists_path.exists():
        return
    try:
        data = json.loads(lists_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return
    if not isinstance(data, list):
        return

    template = None
    for item in data:
        if isinstance(item, dict) and item.get("name") == source_name:
            template = dict(item)
            break
    if template is None:
        template = {"name": source_name}

    template["name"] = new_name
    if "productModel" in template:
        template["productModel"] = new_name
    if "uuid" in template:
        template["uuid"] = new_uuid
    if "instancePath" in template:
        template["instancePath"] = str(new_path)

    data = [item for item in data if not (isinstance(item, dict) and item.get("name") == new_name)]
    data.append(template)
    lists_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def remove_from_lists_json(root: Path, name: str) -> None:
    lists_path = root / "lists.json"
    if not lists_path.exists():
        return
    try:
        data = json.loads(lists_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return
    if not isinstance(data, list):
        return
    data = [item for item in data if not (isinstance(item, dict) and item.get("name") == name)]
    lists_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def create_hvd(
    root: Path = DEFAULT_HVD_ROOT,
    source_name: str | None = None,
    new_name: str | None = None,
    hdc_port: int | None = None,
    include_logs: bool = False,
) -> HvdInfo:
    root = ensure_root(root)
    if not source_name or not new_name:
        raise HvdManagerError("Both source_name and new_name are required")
    validate_name(source_name)
    validate_name(new_name)
    if hdc_port is not None and not 10000 <= hdc_port <= 16555:
        raise HvdManagerError("hdc_port must be in range 10000..16555")

    source = find_hvd(root, source_name)
    destination = root / new_name
    destination_ini = root / f"{new_name}.ini"
    if destination.exists() or destination_ini.exists():
        raise HvdManagerError(f"HVD already exists: {new_name}")
    if not source.path.exists():
        raise HvdManagerError(f"Source HVD directory does not exist: {source.path}")

    copy_source_tree(source.path, destination, include_logs=include_logs)
    new_uuid = str(uuid.uuid4())

    root_values = {"hvd.ini.encoding": "UTF-8", "path": str(destination)}
    write_ini(destination_ini, root_values, ["hvd.ini.encoding", "path"])

    config_path = destination / "config.ini"
    config = read_ini(config_path)
    config.update(
        {
            "name": new_name,
            "productModel": new_name,
            "uuid": new_uuid,
            "instancePath": str(destination),
            "hw.hdc.port": str(hdc_port) if hdc_port is not None else "notset",
        }
    )
    write_ini(config_path, config)

    update_key_value_file(destination / "hardware-qemu.ini", {"hvd.id": new_name, "hvd.name": new_name})
    update_lists_json(root, source.name, new_name, destination, new_uuid)

    return find_hvd(root, new_name)


def delete_hvd(root: Path = DEFAULT_HVD_ROOT, name: str | None = None, confirm_name: str | None = None) -> HvdInfo:
    root = ensure_root(root)
    if not name:
        raise HvdManagerError("name is required")
    validate_name(name)
    if confirm_name != name:
        raise HvdManagerError("--confirm-name must exactly match the HVD name")

    hvd = find_hvd(root, name)
    root_real = root.resolve()
    hvd_real = hvd.path.resolve()
    if hvd_real == root_real or root_real not in hvd_real.parents:
        raise HvdManagerError(f"Refusing to delete path outside HVD root: {hvd.path}")

    if hvd.root_ini.exists():
        hvd.root_ini.unlink()
    if hvd.path.exists():
        shutil.rmtree(hvd.path)
    remove_from_lists_json(root, hvd.name)
    return hvd


def format_table(hvds: list[HvdInfo]) -> str:
    if not hvds:
        return "No HVDs found"
    rows = [["NAME", "TYPE", "API", "HDC", "EXISTS", "PATH"]]
    for hvd in hvds:
        rows.append(
            [
                hvd.name,
                hvd.device_type or "",
                hvd.api_version or "",
                hvd.hdc_port or "",
                "yes" if hvd.exists else "no",
                str(hvd.path),
            ]
        )
    widths = [max(len(row[index]) for row in rows) for index in range(len(rows[0]))]
    return "\n".join("  ".join(value.ljust(widths[index]) for index, value in enumerate(row)) for row in rows)


def print_json(payload: object) -> None:
    print(json.dumps(payload, ensure_ascii=False, indent=2))


def run_download_image(args: argparse.Namespace) -> int:
    payload = {
        "decision": "blocked",
        "operation": "image.download",
        "deviceType": args.device_type,
        "apiVersion": args.api_version,
        "reason": (
            "DevEco Studio exposes image download through SDK Manager UI APIs; "
            "no stable non-UI CLI entrypoint has been verified yet."
        ),
        "nextStep": "Open DevEco Studio HVD Manager or implement a dedicated SDK Manager bridge after isolating its API contract.",
    }
    print_json(payload)
    return 2


def validate_hdc_port(hdc_port: int | None) -> None:
    if hdc_port is not None and not 10000 <= hdc_port <= 16555:
        raise HvdManagerError("hdc_port must be in range 10000..16555")


def validate_trace_name(trace_name: str) -> None:
    if not TRACE_NAME_PATTERN.fullmatch(trace_name):
        raise HvdManagerError(
            "trace_name must be 1-64 chars and contain only letters, numbers, dots, underscores, or hyphens"
        )


def build_emulator_command(
    emulator: Path,
    root: Path,
    hvd: HvdInfo,
    trace_name: str,
    image_root: Path,
    hdc_port: int | None = None,
) -> list[str]:
    validate_hdc_port(hdc_port)
    validate_trace_name(trace_name)
    command = [
        str(emulator),
        "-hvd",
        hvd.name,
        "-path",
        str(root),
        "-t",
        trace_name,
        "-imageRoot",
        str(image_root),
    ]
    if hdc_port is not None:
        command.extend(["-hdcport", str(hdc_port)])
    return command


def resolve_image_root(args: argparse.Namespace, sdk_root: Path | None) -> PathProbe:
    arg_image_root = getattr(args, "image_root", None)
    if arg_image_root:
        return probe_first_existing([(arg_image_root, "arg:image-root")])

    image_probe = probe_first_existing(candidate_image_roots())
    if image_probe.exists:
        return image_probe

    if sdk_root:
        return probe_first_existing([(sdk_root, "arg:sdk-root")])
    return image_probe


def validate_image_root_for_hvd(image_root: Path | None, hvd: HvdInfo) -> tuple[list[str], list[str]]:
    missing_config: list[str] = []
    recommendations: list[str] = []

    if not image_root or not image_root.expanduser().exists():
        missing_config.append("imageRoot")
        recommendations.append(
            "Pass --image-root or set HARMONY_EMULATOR_IMAGE_ROOT to the emulator image root, for example ~/Library/Huawei/Sdk on macOS."
        )
        return missing_config, recommendations

    if hvd.image_sub_path:
        image_sub_path = hvd.image_sub_path.strip().lstrip("/\\")
        system_image_path = image_root.expanduser() / image_sub_path
        if not system_image_path.exists():
            missing_config.append("imageRootSystemImage")
            recommendations.append(
                "Use the emulator image root that contains "
                f"{image_sub_path}; on macOS this is often ~/Library/Huawei/Sdk, not /Applications/DevEco-Studio.app/Contents/sdk."
            )

    return missing_config, recommendations


def create_artifact_dir(trace_name: str, artifact_dir: Path | None) -> Path:
    if artifact_dir:
        path = artifact_dir.expanduser()
    else:
        safe_trace = re.sub(r"[^A-Za-z0-9_.-]+", "-", trace_name)
        path = Path(tempfile.gettempdir()) / f"harmony-hvd-launch-{safe_trace}"
    path.mkdir(parents=True, exist_ok=True)
    return path.resolve()


def read_text_snippet(path: Path, limit: int = 4000) -> str:
    if not path.exists():
        return ""
    data = path.read_bytes()
    if len(data) > limit:
        data = data[-limit:]
    return data.decode("utf-8", errors="replace")


def log_indicates_license_agreement_required(text: str) -> bool:
    lowered = text.lower()
    return (
        "please agree to the agreement first" in lowered
        or "confirm whether agree to the above agreement" in lowered
        or ("agreement" in lowered and "unable to start the emulator" in lowered)
    )


def apply_license_agreement_result(payload: dict[str, object]) -> None:
    payload["decision"] = "blocked"
    payload["result"] = LICENSE_AGREEMENT_RESULT
    payload["missingConfig"] = ["emulatorLicenseAgreement"]
    payload["issues"] = ["Emulator requires first-run Huawei license/agreement confirmation before CLI launch can continue."]
    payload["recommendations"] = [
        "Run the Emulator once interactively and accept the agreement, or retry with launch --accept-license after reviewing the agreement.",
        "The script does not auto-accept this prompt unless --accept-license is passed explicitly.",
    ]


def run_short_command(command: list[str], timeout: float = 5) -> dict[str, object]:
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=timeout, check=False)
    except (OSError, subprocess.TimeoutExpired) as error:
        return {"ok": False, "error": str(error), "command": command}
    return {
        "ok": result.returncode == 0,
        "exitCode": result.returncode,
        "stdout": (result.stdout or "")[:4000],
        "stderr": (result.stderr or "")[:4000],
        "command": command,
    }


def probe_emulator_runtime(emulator: Path | None, hvd_name: str) -> dict[str, object]:
    if emulator is None:
        return {"ok": False, "error": "emulator path unavailable"}
    result = run_short_command([str(emulator), "-list", "-details"], timeout=10)
    output = f"{result.get('stdout', '')}\n{result.get('stderr', '')}"
    details: dict[str, object] = {"ok": result.get("ok", False), "exitCode": result.get("exitCode"), "output": output[:4000]}
    name_index = output.find(hvd_name)
    if name_index >= 0:
        window = output[max(0, name_index - 500) : name_index + 1000]
        running_match = re.search(r"isRunning['\"]?\s*[:=]\s*['\"]?(true|false)", window, re.IGNORECASE)
        port_match = re.search(r"hw\.hdc\.port['\"]?\s*[:=]\s*['\"]?([A-Za-z0-9_.:-]+)", window)
        if running_match:
            details["hvdIsRunning"] = running_match.group(1).lower() == "true"
        if port_match:
            details["hvdHdcPort"] = port_match.group(1)
    return details


def snapshot_hdc(hdc: Path | None) -> dict[str, object]:
    if hdc is None:
        return {"ok": False, "error": "hdc path unavailable"}
    return run_short_command([str(hdc), "list", "targets", "-v"], timeout=5)


def has_offline_hdc_target(output: str) -> bool:
    return any("Offline" in line for line in output.splitlines())


def build_trace_timeout_diagnostics(
    emulator: Path,
    root: Path,
    hvd: HvdInfo,
    image_root: Path,
    trace_name: str,
    socket_path: Path,
    timeout: float,
    hdc: Path | None,
    process_exit_code: int | None,
    hvd_runtime: dict[str, object],
    hdc_snapshot: dict[str, object],
) -> dict[str, object]:
    likely_causes = [
        "Emulator did not open the guarded trace socket before the launch timeout.",
        "The DevEco Emulator CLI may be blocked by a login-gated modal, stale runtime state, or changed private startup contract.",
    ]

    if process_exit_code is not None:
        likely_causes.insert(1, f"Emulator process exited before trace connection with exit code {process_exit_code}.")
    elif hvd_runtime.get("ok") is False:
        likely_causes.append("Emulator -list -details failed or timed out, so the local Emulator runtime may be unhealthy.")

    hdc_output = f"{hdc_snapshot.get('stdout', '')}\n{hdc_snapshot.get('stderr', '')}"
    if has_offline_hdc_target(hdc_output) and not parse_connected_target(hdc_output):
        likely_causes.append("HDC reports only Offline targets; restart the HDC server or clear stale Emulator targets before retrying.")

    commands: list[dict[str, object]] = [
        {
            "purpose": "Verify Emulator binary responsiveness",
            "command": [str(emulator), "-version"],
        },
        {
            "purpose": "Inspect HVD runtime state",
            "command": [str(emulator), "-list", "-details"],
        },
    ]
    if hdc:
        commands.append(
            {
                "purpose": "Inspect HDC target state",
                "command": [str(hdc), "list", "targets", "-v"],
            }
        )
    commands.append(
        {
            "purpose": "Validate launch inputs without starting Emulator",
            "command": [
                sys.executable,
                "harmony-next/scripts/hvd_manager.py",
                "--root",
                str(root),
                "--emulator",
                str(emulator),
                "launch-preflight",
                "--name",
                hvd.name,
                "--image-root",
                str(image_root),
                "--trace-name",
                trace_name,
                "--trace-helper-ready-file",
                "<ready-file>",
                "--json",
            ],
        }
    )

    return {
        "summary": "Trace socket connection was not established before timeout.",
        "timeoutSeconds": timeout,
        "socketPath": str(socket_path),
        "likelyCauses": likely_causes,
        "nextDiagnosticCommands": commands,
        "manualChecks": [
            "If Emulator -list -details also hangs, start the same HVD once from DevEco Studio Device Manager to surface any login or image repair dialog.",
            "If HDC keeps showing an Offline localhost target, run hdc kill/start from the same SDK toolchain and retry with an explicit --hdc-port.",
        ],
    }


def parse_connected_target(output: str, target_hint: str | None = None, tcp_only: bool = False) -> str | None:
    for line in output.splitlines():
        parts = line.split()
        if len(parts) < 3 or parts[2] != "Connected":
            continue
        target = parts[0] if parts else ""
        transport = parts[1].upper() if len(parts) > 1 else ""
        if target_hint and target_hint not in target:
            continue
        if tcp_only and transport != "TCP":
            continue
        return target
    return None


def start_trace_holder(connection: socket.socket, emulator_pid: int, hold_seconds: float, log_path: Path) -> dict[str, object] | None:
    if hold_seconds <= 0:
        return None
    helper_code = r"""
import os
import socket
import sys
import time
import traceback

fd = int(sys.argv[1])
emulator_pid = int(sys.argv[2])
hold_seconds = float(sys.argv[3])
log_path = sys.argv[4]
deadline = time.monotonic() + hold_seconds
bytes_read = 0
reason = "starting"
try:
    with open(log_path, "w", encoding="utf-8") as log:
        log.write("reason=started\nbytesRead=0\n")
    sock = socket.socket(fileno=fd)
    sock.settimeout(1.0)
    reason = "timeout"
    try:
        while time.monotonic() < deadline:
            try:
                os.kill(emulator_pid, 0)
            except OSError:
                reason = "emulator-exited"
                break
            try:
                chunk = sock.recv(4096)
                if not chunk:
                    reason = "trace-closed"
                    break
                bytes_read += len(chunk)
            except socket.timeout:
                continue
    finally:
        sock.close()
except BaseException:
    reason = "helper-error"
    details = traceback.format_exc()
finally:
    with open(log_path, "w", encoding="utf-8") as log:
        log.write(f"reason={reason}\nbytesRead={bytes_read}\n")
        if reason == "helper-error":
            log.write(details)
"""
    helper_log = log_path.parent / "trace-holder.log"
    process = subprocess.Popen(
        [sys.executable, "-c", helper_code, str(connection.fileno()), str(emulator_pid), str(hold_seconds), str(helper_log)],
        pass_fds=(connection.fileno(),),
        start_new_session=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        text=True,
    )
    return {"pid": process.pid, "holdSeconds": hold_seconds, "logPath": str(helper_log)}


def wait_for_runtime_stability(
    seconds: float,
    process: subprocess.Popen[str],
    hdc: Path | None,
    target: str | None,
) -> dict[str, object]:
    if seconds <= 0:
        return {"stable": True, "seconds": 0}
    deadline = time.monotonic() + seconds
    last_hdc = snapshot_hdc(hdc) if target else {"ok": False, "error": "target unavailable"}
    while True:
        exit_code = process.poll()
        if exit_code is not None:
            return {"stable": False, "seconds": seconds, "reason": "process-exited", "processExitCode": exit_code, "hdcSnapshot": last_hdc}
        if target and hdc:
            last_hdc = snapshot_hdc(hdc)
            output = f"{last_hdc.get('stdout', '')}\n{last_hdc.get('stderr', '')}"
            if not parse_connected_target(output, target):
                return {"stable": False, "seconds": seconds, "reason": "hdc-disconnected", "hdcSnapshot": last_hdc}
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            break
        time.sleep(min(1, remaining))
    return {"stable": True, "seconds": seconds, "hdcSnapshot": last_hdc}


def run_launch_preflight(args: argparse.Namespace, root: Path, emulator: Path | None, sdk_root: Path | None) -> int:
    root = ensure_root(root)
    hvd = find_hvd(root, args.name)
    emulator_probe = probe_first_existing([(emulator, "arg:emulator")] if emulator else candidate_emulators(), executable=True)
    image_root_probe = resolve_image_root(args, sdk_root)

    missing_config: list[str] = []
    issues: list[str] = []
    recommendations: list[str] = []

    if not emulator_probe.exists:
        missing_config.append("emulator")
        issues.append("Emulator executable was not found")
        recommendations.append("Pass --emulator or set HARMONY_EMULATOR to DevEco Studio tools/emulator/Emulator.")
    elif not emulator_probe.executable:
        missing_config.append("emulatorExecutable")
        issues.append(f"Emulator is not executable: {emulator_probe.path}")

    image_missing, image_recommendations = validate_image_root_for_hvd(image_root_probe.path, hvd)
    missing_config.extend(image_missing)
    recommendations.extend(image_recommendations)

    if not hvd.exists:
        missing_config.append("hvdDirectory")
        issues.append(f"HVD directory was not found: {hvd.path}")
        recommendations.append("Create or repair the HVD in DevEco Studio before launching from CLI.")

    if not args.trace_name:
        missing_config.append("traceName")
    if not args.trace_helper_ready_file or not args.trace_helper_ready_file.expanduser().is_file():
        missing_config.append("tracePipeHelper")
        recommendations.append(
            "Start a verified trace-pipe helper first and pass --trace-helper-ready-file for this preflight."
        )

    payload: dict[str, object] = {
        "decision": "blocked" if missing_config else "allowed",
        "operation": "emulator.launch.preflight",
        "hvdName": hvd.name,
        "hvdRoot": str(root),
        "hvdExists": hvd.exists,
        "imageRoot": image_root_probe.to_json(),
        "imageSubPath": hvd.image_sub_path,
        "traceName": args.trace_name,
        "knownSymptom": LOGIN_GATED_MODAL_SYMPTOM,
        "missingConfig": missing_config,
        "issues": issues,
        "recommendations": recommendations,
    }

    if missing_config:
        print_json(payload)
        return 2

    payload["emulatorCommand"] = build_emulator_command(
        emulator_probe.path,
        root,
        hvd,
        args.trace_name,
        image_root_probe.path,
        args.hdc_port,
    )
    payload["traceHelperReadyFile"] = str(args.trace_helper_ready_file.expanduser().resolve())
    print_json(payload)
    return 0


def wait_for_hdc_target(timeout: float, hdc: Path | str = "hdc", target_hint: str | None = None) -> dict[str, object]:
    deadline = time.monotonic() + timeout
    last_output = ""
    while time.monotonic() < deadline:
        try:
            result = subprocess.run([str(hdc), "list", "targets", "-v"], capture_output=True, text=True, timeout=5)
        except (OSError, subprocess.TimeoutExpired) as error:
            return {"connected": False, "error": str(error), "lastOutput": last_output[:2000]}
        last_output = (result.stdout or result.stderr).strip()
        target = parse_connected_target(last_output, target_hint, tcp_only=target_hint is None)
        if target:
            return {"connected": True, "target": target, "lastOutput": last_output[:2000]}
        time.sleep(1)
    return {"connected": False, "error": "timed out waiting for hdc target", "lastOutput": last_output[:2000]}


def wait_for_boot_completed(timeout: float, hdc: Path | str, target: str) -> dict[str, object]:
    deadline = time.monotonic() + timeout
    last_output = ""
    while time.monotonic() < deadline:
        try:
            result = subprocess.run(
                [str(hdc), "-t", target, "shell", "param", "get", "bootevent.boot.completed"],
                capture_output=True,
                text=True,
                timeout=5,
            )
        except (OSError, subprocess.TimeoutExpired) as error:
            return {"completed": False, "error": str(error), "lastOutput": last_output[:2000]}
        last_output = (result.stdout or result.stderr).strip()
        if last_output.lower() in {"true", "1"}:
            return {"completed": True, "lastOutput": last_output[:2000]}
        time.sleep(1)
    return {"completed": False, "error": "timed out waiting for boot completion", "lastOutput": last_output[:2000]}


def run_launch(args: argparse.Namespace, root: Path, emulator: Path | None, sdk_root: Path | None) -> int:
    root = ensure_root(root)
    hvd = find_hvd(root, args.name)
    emulator_probe = probe_first_existing([(emulator, "arg:emulator")] if emulator else candidate_emulators(), executable=True)
    image_root_probe = resolve_image_root(args, sdk_root)
    launch_hdc = getattr(args, "launch_hdc", None) or getattr(args, "hdc", None)
    hdc_probe = probe_first_existing([(launch_hdc, "arg:hdc")] if launch_hdc else candidate_hdcs(sdk_root), executable=True)

    missing_config: list[str] = []
    issues: list[str] = []
    recommendations: list[str] = []

    if not emulator_probe.exists:
        missing_config.append("emulator")
        issues.append("Emulator executable was not found")
        recommendations.append("Pass --emulator or set HARMONY_EMULATOR to DevEco Studio tools/emulator/Emulator.")
    elif not emulator_probe.executable:
        missing_config.append("emulatorExecutable")
        issues.append(f"Emulator is not executable: {emulator_probe.path}")

    image_missing, image_recommendations = validate_image_root_for_hvd(image_root_probe.path, hvd)
    missing_config.extend(image_missing)
    recommendations.extend(image_recommendations)

    if not args.no_wait_target:
        if not hdc_probe.exists:
            missing_config.append("hdc")
            recommendations.append("Pass --hdc or set HARMONY_HDC to the DevEco hdc executable when waiting for target boot.")
        elif not hdc_probe.executable:
            missing_config.append("hdcExecutable")
            issues.append(f"HDC is not executable: {hdc_probe.path}")

    if not hvd.exists:
        missing_config.append("hvdDirectory")
        issues.append(f"HVD directory was not found: {hvd.path}")
        recommendations.append("Create or repair the HVD in DevEco Studio before launching from CLI.")

    if not args.trace_name:
        missing_config.append("traceName")

    payload: dict[str, object] = {
        "decision": "blocked" if missing_config else "allowed",
        "operation": "emulator.launch",
        "hvdName": hvd.name,
        "hvdRoot": str(root),
        "hvdExists": hvd.exists,
        "imageRoot": image_root_probe.to_json(),
        "imageSubPath": hvd.image_sub_path,
        "hdc": hdc_probe.to_json(),
        "traceName": args.trace_name,
        "knownSymptom": LOGIN_GATED_MODAL_SYMPTOM,
        "missingConfig": missing_config,
        "issues": issues,
        "recommendations": recommendations,
    }

    if missing_config:
        print_json(payload)
        return 2

    assert emulator_probe.path is not None
    assert image_root_probe.path is not None
    image_root = image_root_probe.path.expanduser().resolve()
    command = build_emulator_command(emulator_probe.path, root, hvd, args.trace_name, image_root, args.hdc_port)
    payload["emulatorCommand"] = command
    artifact_dir = create_artifact_dir(args.trace_name, args.artifact_dir)
    log_path = artifact_dir / "emulator-launch.log"
    payload["artifactDir"] = str(artifact_dir)
    payload["logPath"] = str(log_path)

    socket_path = Path("/tmp") / args.trace_name
    if socket_path.exists():
        payload["decision"] = "blocked"
        payload["result"] = "trace-socket-exists"
        payload["missingConfig"] = ["traceSocketPath"]
        payload["issues"] = [f"Trace socket path already exists: {socket_path}"]
        print_json(payload)
        return 2

    trace_bytes = b""
    process: subprocess.Popen[str] | None = None
    log_file = log_path.open("w", encoding="utf-8")
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as server:
        server.bind(str(socket_path))
        server.listen(1)
        server.settimeout(args.timeout)
        try:
            process = subprocess.Popen(
                command,
                stdin=subprocess.PIPE,
                stdout=log_file,
                stderr=subprocess.STDOUT,
                text=True,
                start_new_session=True,
            )
            if process.stdin:
                try:
                    if args.accept_license:
                        process.stdin.write("y\n")
                        process.stdin.flush()
                except BrokenPipeError:
                    pass
                finally:
                    try:
                        process.stdin.close()
                    except BrokenPipeError:
                        pass
        except OSError as error:
            payload["decision"] = "blocked"
            payload["result"] = "launch-failed"
            payload["issues"] = [str(error)]
            log_file.close()
            if socket_path.exists():
                socket_path.unlink()
            print_json(payload)
            return 2

        try:
            connection, _ = server.accept()
            payload["socketConnected"] = True
            with connection:
                connection.settimeout(0.2)
                try:
                    trace_bytes = connection.recv(4096)
                except socket.timeout:
                    trace_bytes = b""
                trace_holder = start_trace_holder(connection, process.pid, args.trace_hold_seconds, log_path)
                if trace_holder:
                    payload["traceHolder"] = trace_holder
        except socket.timeout:
            payload["socketConnected"] = False
            payload["decision"] = "blocked"
            payload["result"] = "trace-timeout"
            payload["missingConfig"] = ["tracePipeConnection"]
            process_exit_code = process.poll()
            if process_exit_code is None:
                try:
                    process.wait(timeout=0.5)
                except subprocess.TimeoutExpired:
                    process.terminate()
                    try:
                        process.wait(timeout=5)
                    except subprocess.TimeoutExpired:
                        process.kill()
                        process.wait(timeout=5)
            log_file.close()
            payload["processExitCode"] = process.poll()
            payload["logTail"] = read_text_snippet(log_path)
            if log_indicates_license_agreement_required(str(payload["logTail"])):
                payload["socketConnected"] = False
                apply_license_agreement_result(payload)
                print_json(payload)
                return 2
            hvd_runtime = probe_emulator_runtime(emulator_probe.path, hvd.name)
            hdc_snapshot = snapshot_hdc(hdc_probe.path if hdc_probe.exists else None)
            payload["hvdRuntime"] = hvd_runtime
            payload["hdcSnapshot"] = hdc_snapshot
            payload["traceTimeoutDiagnostics"] = build_trace_timeout_diagnostics(
                emulator_probe.path,
                root,
                hvd,
                image_root,
                args.trace_name,
                socket_path,
                args.timeout,
                hdc_probe.path if hdc_probe.exists else None,
                payload["processExitCode"],
                hvd_runtime,
                hdc_snapshot,
            )
            print_json(payload)
            return 2
        finally:
            if socket_path.exists():
                socket_path.unlink()
            if not log_file.closed:
                log_file.flush()

    payload["result"] = "started"
    payload["pid"] = process.pid
    payload["processExitCode"] = process.poll()
    payload["traceBytesRead"] = len(trace_bytes)
    if not log_file.closed:
        log_file.close()

    if not args.no_wait_target:
        assert hdc_probe.path is not None
        target_hint = f":{args.hdc_port}" if args.hdc_port is not None else None
        payload["hdcWait"] = wait_for_hdc_target(args.timeout, hdc_probe.path, target_hint)
        if payload["hdcWait"].get("connected") and payload["hdcWait"].get("target"):
            payload["bootWait"] = wait_for_boot_completed(args.timeout, hdc_probe.path, str(payload["hdcWait"]["target"]))
        payload["stabilityWait"] = wait_for_runtime_stability(
            args.stability_seconds,
            process,
            hdc_probe.path,
            str(payload["hdcWait"].get("target")) if payload.get("hdcWait", {}).get("target") else None,
        )

    payload["logTail"] = read_text_snippet(log_path)
    payload["hvdRuntime"] = probe_emulator_runtime(emulator_probe.path, hvd.name)
    payload["hdcSnapshot"] = snapshot_hdc(hdc_probe.path if hdc_probe.exists else None)

    print_json(payload)
    if payload.get("stabilityWait", {}).get("stable") is False:
        return 2
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Manage local DevEco HarmonyOS HVD instances.")
    parser.add_argument(
        "--root",
        type=Path,
        default=None,
        help=f"HVD root, default: env {','.join(HVD_ROOT_ENV_KEYS)} or {DEFAULT_HVD_ROOT}",
    )
    parser.add_argument("--emulator", type=Path, help=f"Emulator executable, or env {','.join(EMULATOR_ENV_KEYS)}")
    parser.add_argument("--sdk-root", type=Path, help=f"DevEco SDK root, or env {','.join(SDK_ROOT_ENV_KEYS)}")
    parser.add_argument("--hdc", type=Path, help=f"HDC executable, or env {','.join(HDC_ENV_KEYS)}")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON")
    subparsers = parser.add_subparsers(dest="command", required=True)

    doctor_parser = subparsers.add_parser("doctor", help="Probe local HVD, Emulator, and SDK environment")
    doctor_parser.add_argument("--json", action="store_true", help="Print machine-readable JSON")

    list_parser = subparsers.add_parser("list", help="List registered local HVD instances")
    list_parser.add_argument("--json", action="store_true", help="Print machine-readable JSON")

    create_parser = subparsers.add_parser("create", help="Clone a local HVD instance with refreshed identity")
    create_parser.add_argument("--from", dest="source_name", required=True, help="Source HVD name")
    create_parser.add_argument("--name", dest="new_name", required=True, help="New HVD name")
    create_parser.add_argument("--hdc-port", type=int, help="Optional HDC port, 10000..16555")
    create_parser.add_argument("--include-logs", action="store_true", help="Copy source Log directory as well")
    create_parser.add_argument("--json", action="store_true", help="Print machine-readable JSON")

    delete_parser = subparsers.add_parser("delete", help="Delete a local HVD registration and instance directory")
    delete_parser.add_argument("--name", required=True, help="HVD name to delete")
    delete_parser.add_argument("--confirm-name", required=True, help="Must exactly match --name")
    delete_parser.add_argument("--json", action="store_true", help="Print machine-readable JSON")

    download_parser = subparsers.add_parser("download-image", help="Report current command-line image download support")
    download_parser.add_argument("--device-type", required=True)
    download_parser.add_argument("--api-version", required=True)

    launch_preflight_parser = subparsers.add_parser(
        "launch-preflight",
        help="Validate trace-pipe startup preconditions and print a guarded Emulator command plan",
    )
    launch_preflight_parser.add_argument("--name", required=True, help="HVD name to launch")
    launch_preflight_parser.add_argument("--image-root", type=Path, help="Emulator image root passed to Emulator -imageRoot")
    launch_preflight_parser.add_argument("--trace-name", help="Trace pipe name prepared by a verified helper")
    launch_preflight_parser.add_argument(
        "--trace-helper-ready-file",
        type=Path,
        help="Readiness marker written by the verified trace pipe helper",
    )
    launch_preflight_parser.add_argument("--hdc-port", type=int, help="Optional HDC port, 10000..16555")
    launch_preflight_parser.add_argument("--json", action="store_true", help="Print machine-readable JSON")

    launch_parser = subparsers.add_parser(
        "launch",
        help="Create a bounded trace socket and start Emulator with the guarded CLI command",
    )
    launch_parser.add_argument("--name", required=True, help="HVD name to launch")
    launch_parser.add_argument("--image-root", type=Path, help="Emulator image root passed to Emulator -imageRoot")
    launch_parser.add_argument("--trace-name", required=True, help="Trace pipe name for this launch")
    launch_parser.add_argument("--hdc-port", type=int, help="Optional HDC port, 10000..16555")
    launch_parser.add_argument("--hdc", dest="launch_hdc", type=Path, help=f"HDC executable, or env {','.join(HDC_ENV_KEYS)}")
    launch_parser.add_argument("--artifact-dir", type=Path, help="Directory for launch logs and diagnostic artifacts")
    launch_parser.add_argument("--timeout", type=float, default=30, help="Seconds to wait for trace socket / hdc target")
    launch_parser.add_argument("--trace-hold-seconds", type=float, default=1800, help="Seconds to keep the trace connection alive after startup")
    launch_parser.add_argument("--stability-seconds", type=float, default=60, help="Seconds to verify the Emulator process and HDC target stay alive after boot")
    launch_parser.add_argument("--no-wait-target", action="store_true", help="Return after Emulator connects to trace socket")
    launch_parser.add_argument(
        "--accept-license",
        action="store_true",
        help="Explicitly answer yes to the Emulator first-run Huawei license/agreement prompt",
    )
    launch_parser.add_argument("--json", action="store_true", help="Print machine-readable JSON")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        root = args.root or default_hvd_root()
        if args.command == "doctor":
            payload = run_doctor(args.root, args.emulator, args.sdk_root)
            if args.json:
                print_json(payload)
            else:
                print_json(payload)
            return 0

        if args.command == "list":
            hvds = list_hvds(root)
            if args.json:
                print_json([hvd.to_json() for hvd in hvds])
            else:
                print(format_table(hvds))
            return 0

        if args.command == "create":
            hvd = create_hvd(root, args.source_name, args.new_name, args.hdc_port, args.include_logs)
            if args.json:
                print_json({"created": hvd.to_json()})
            else:
                print(f"Created HVD: {hvd.name}")
            return 0

        if args.command == "delete":
            hvd = delete_hvd(root, args.name, args.confirm_name)
            if args.json:
                print_json({"deleted": hvd.to_json()})
            else:
                print(f"Deleted HVD: {hvd.name}")
            return 0

        if args.command == "download-image":
            return run_download_image(args)

        if args.command == "launch-preflight":
            return run_launch_preflight(args, root, args.emulator, args.sdk_root)

        if args.command == "launch":
            return run_launch(args, root, args.emulator, args.sdk_root)

    except HvdManagerError as error:
        payload = {"decision": "blocked", "error": str(error)}
        if getattr(args, "json", False):
            print_json(payload)
        else:
            print(f"blocked: {error}", file=sys.stderr)
        return 2

    parser.error(f"Unknown command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
