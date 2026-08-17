# Issue Guide

Use this guide when a HarmonyOS NEXT user reports a requirement, bug, missing capability, confusing behavior, documentation gap, or local DevEco/HVD automation problem that should become a GitHub issue for this repository.

Repository: `linhay/harmony-next.skills`

## Scenario Forms

Choose the issue form that matches the workflow under investigation:

| Scenario | Form | Direct URL |
| --- | --- | --- |
| DevEco Emulator / HVD launch, image root, license, HDC readiness, lifecycle | `deveco-emulator-hvd.yml` | `https://github.com/linhay/harmony-next.skills/issues/new?template=deveco-emulator-hvd.yml` |
| HarmonyOS Command Line Tools setup, archive install, PATH, `codelinter` | `commandline-tools.yml` | `https://github.com/linhay/harmony-next.skills/issues/new?template=commandline-tools.yml` |
| HDC evidence, bounded UI action, WebView DevTools socket/fport diagnostics | `device-evidence-bundle.yml` | `https://github.com/linhay/harmony-next.skills/issues/new?template=device-evidence-bundle.yml` |
| Offline UI/UX audit, UxTestService, Python deps, rule result, false positive/negative | `offline-ux-audit.yml` | `https://github.com/linhay/harmony-next.skills/issues/new?template=offline-ux-audit.yml` |
| Offline Profiler trace audit, `trace_streamer`, SQLite summary, long spans | `profiler-trace-audit.yml` | `https://github.com/linhay/harmony-next.skills/issues/new?template=profiler-trace-audit.yml` |
| Reference/API lookup, missing/stale docs, bad slug/anchor/routing | `reference-api-feedback.yml` | `https://github.com/linhay/harmony-next.skills/issues/new?template=reference-api-feedback.yml` |
| Skill packaging, release asset, `BUILD_INFO.json`, install/versioning | `skill-packaging-release.yml` | `https://github.com/linhay/harmony-next.skills/issues/new?template=skill-packaging-release.yml` |

## Workflow

1. Clarify only the minimum missing detail needed to avoid filing a wrong issue.
2. Reproduce or inspect locally when possible. Prefer machine-readable checks from this skill. Resolve `HARMONY_NEXT_SKILL_DIR` from the loaded `SKILL.md` first; do not assume `harmony-next/` exists at the current repository root:
   - `python3 "$HARMONY_NEXT_SKILL_DIR/scripts/hvd_manager.py" doctor --json`
   - `python3 "$HARMONY_NEXT_SKILL_DIR/scripts/hvd_manager.py" list --json`
   - `python3 "$HARMONY_NEXT_SKILL_DIR/scripts/hvd_manager.py" launch-preflight ... --json`
   - `python3 "$HARMONY_NEXT_SKILL_DIR/scripts/hvd_manager.py" launch ... --json`
   - `python3 "$HARMONY_NEXT_SKILL_DIR/scripts/commandline_tools_manager.py" doctor --tools-root <dir> --json`
   - `python3 "$HARMONY_NEXT_SKILL_DIR/scripts/device_evidence_bundle.py" doctor --deveco-app <DevEco-Studio.app> --json`
   - `python3 "$HARMONY_NEXT_SKILL_DIR/scripts/device_evidence_bundle.py" webview-devtools --deveco-app <DevEco-Studio.app> --target <target> --artifact-dir <dir> --json`
   - `python3 "$HARMONY_NEXT_SKILL_DIR/scripts/device_ui_action.py" tap --deveco-app <DevEco-Studio.app> --target <target> --artifact-dir <dir> --text "<text>" --json`
   - `python3 "$HARMONY_NEXT_SKILL_DIR/scripts/ux_audit_pipeline.py" doctor --deveco-app <DevEco-Studio.app> --python <python-with-ux-deps> --json`
   - `python3 "$HARMONY_NEXT_SKILL_DIR/scripts/reference_compat.py" check`
   - `python3 -m unittest discover -s "$HARMONY_NEXT_SKILL_DIR/tests"`
3. Preserve structured fields in the issue instead of flattening them into prose:
   - `decision`
   - `operation`
   - `missingConfig`
   - `issues`
   - `recommendations`
   - `hvdRoot`
   - `emulator`
   - `sdkRoot`
   - `imageRoot`
   - `imageSubPath`
   - `hdc`
   - `hdcWait`
   - `bootWait`
   - `stabilityWait`
   - `processExitCode`
   - `logPath`
   - `feedback`
   - `artifacts`
   - `commandLedger`
   - `layoutSummary`
   - `uxService`
   - `uxPython`
   - `resultCounts`
   - `uxSummary`
   - `report`
   - `traceStreamer`
   - `input`
   - `outputDir`
   - `topCallstack`
   - `thresholdHits`
   - `frameSlice`
   - `failureCode`
   - `failureCategory`
   - `failureSignal`
   - `sockets`
   - `staleForwards`
   - `fportStatus`
   - `httpProbe`
   - `coordinateSpace`
4. Redact private data before filing:
   - Replace local usernames, absolute private repo paths, app names, bundle IDs, team IDs, account IDs, emails, phone numbers, internal hosts, and private URLs with stable placeholders.
   - Keep reproducibility-critical public facts such as DevEco Studio version, Emulator version, HVD type/API version, CLI command shape, error codes, and sanitized JSON field names.
   - Do not attach full private logs, screenshots with personal data, HAPs, app source, or raw UI dumps unless the user explicitly asked and redaction is verified.
5. Choose the scenario form from the table above. If a script output includes `feedback.issueTemplate`, prefer that form.
6. Classify the issue:
   - `bug`: behavior is broken, unstable, misleading, or inconsistent with documented/script behavior.
   - `feature`: user needs a new capability, script command, fixture, or workflow.
   - `docs`: documentation, onboarding, examples, routing, or troubleshooting are unclear.
   - `question`: only if no concrete repository change is identifiable yet.
7. Create the issue with the matching direct URL, or use `gh issue create --repo linhay/harmony-next.skills --template <form>` when the local GitHub CLI supports the selected issue form.
8. Report the issue URL back to the user with a short summary and local verification result.

## Scenario Template Fields

### DevEco Emulator / HVD

Form: `deveco-emulator-hvd.yml`

Include:

- DevEco Studio path and version.
- `Emulator -version`.
- `Emulator -list -details` redacted summary.
- HVD name/type/API version and `imageSubPath`.
- Whether the path is build SDK root or emulator image root.
- `hdc list targets -v` before and after launch.
- `hvd_manager.py doctor --json` redacted output.
- `launch-preflight` or `launch` JSON result.
- Whether `hdcWait`, `bootWait`, and `stabilityWait` succeeded.

### Command Line Tools

Form: `commandline-tools.yml`

Include:

- OS and shell.
- Existing tools root.
- Whether the user has a direct archive URL or only a Huawei download-center page.
- `commandline_tools_manager.py doctor --tools-root <dir>` output.
- Install/bootstrap command and structured blocked/error output.

### Device Evidence Bundle

Form: `device-evidence-bundle.yml`

Include:

- Command line used for `device_evidence_bundle.py` or `device_ui_action.py`.
- `doctor --json` output with private target labels redacted.
- `capture`, `webview-devtools`, or UI action JSON output, especially `decision`, `failureCode`, `missingConfig`, `layoutSummary`, `coordinateSpace`, `staleForwards`, `httpProbe`, and `artifacts`.
- `command_ledger.json` only after redacting private paths, bundle/app names, and stdout/stderr snippets.
- Whether official CLI fallback was attempted: `hdc list targets -v`, `bm dump`, `aa dump`, bounded `hilog`, `uitest dumpLayout`, `screenCap`, and `file recv`.

Do not attach raw screenshots, raw layout trees, full logs, or app-specific bundle/ability names unless the user explicitly approves and redaction is verified.

### Offline UI/UX Audit

Form: `offline-ux-audit.yml`

Include:

- Command line used for `ux_audit_pipeline.py`.
- `doctor --json` output, including `uxService`, `uxPython`, `connectedTargets`, and `missingConfig`.
- `summary.json`, `ux_summary.json`, and `report.md` after redacting private paths, bundle IDs, and screenshots/layout/log references.
- `resultCounts`, rule codes, `test_state`, `ErrorCode`, `ErrorType`, and short sanitized error snippets.
- Whether `capture-audit` or `audit --evidence-summary` was used.
- If blocked, whether official CLI capture fallback was attempted and whether retrying `audit --layout ... --screenshot ... --bundle ...` changed the result.

Do not attach UxTestService marked images, screenshots, raw `ux_result.json`, raw `layout.json`, or full `hilog` unless the user explicitly approves and redaction is verified.

### Offline Profiler Trace Audit

Form: `profiler-trace-audit.yml`

Include:

- Command line used for `profiler_trace_audit.py`.
- `doctor --json` output, including `traceStreamer`, version, and supported abilities when available.
- `audit` JSON output, especially `decision`, `missingConfig`, `recommendations`, `summary`, `topCallstack`, `thresholdHits`, and `frameSlice`.
- Trace metadata such as file type, `source_type`, `parse_tool`, `tool_version`, `trace_range`, and whether SQLite was created.
- Short sanitized stdout/stderr snippets if `trace_streamer` fails.

Do not attach private raw trace files, private process names, app names, usernames, paths, internal URLs, or account identifiers unless sharing is explicitly approved and redaction is verified.

### Offline Reference / API Lookup

Form: `reference-api-feedback.yml`

Include:

- User query and expected HarmonyOS API/topic.
- Local reference path used.
- Missing/incorrect slug, anchor, API signature, or guide mapping.
- `reference_compat.py check` output when relevant.

### Skill Packaging / Release

Form: `skill-packaging-release.yml`

Include:

- Release tag or nightly run.
- `BUILD_INFO.json` fields from the packaged `.skill.zip`.
- GitHub Actions run URL.
- Expected asset name and actual asset name.
