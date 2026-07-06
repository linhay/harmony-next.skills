---
name: harmony-next
description: Use for HarmonyOS NEXT development help and local DevEco automation. Covers ArkTS/ArkUI/NDK API lookup, offline guide navigation, DevEco Studio and HarmonyOS Emulator tasks, hdc/uitest/aa/bm/hilog/hidumper diagnostics, and private DevEco interfaces such as CodeGenie, MCP, LanceDB, devecostudio://, ArkUI Inspector, Previewer, Profiler, Doctor, and UxTestService offline UI/UX audits.
metadata:
  version: "1.3.30"
---

# HarmonyOS NEXT Agent Guide

Use this skill to answer HarmonyOS NEXT questions with the bundled offline references. Keep context small: route the request first, then open only the specific Markdown files needed for the answer or action.

Paths like `references/...` are relative to this skill directory (`harmony-next/`). If your current working directory is the repository root, either `cd harmony-next` first or prefix paths with `harmony-next/`.

## Version

Current local skill version: `v1.3.30`.

Reference snapshot: bundled `references/` are an offline HarmonyOS API 12-23 snapshot, not live web docs.

For "latest", "current", new API, or online-doc parity questions, compare this local version with GitHub Releases or nightly, and verify API behavior against Huawei online docs when precision matters.

Install/update entrypoints:

- Vercel Labs skills CLI: `npx skills add linhay/harmony-next.skills --skill harmony-next`; add `-a claude-code -g -y --copy` for a non-interactive global Claude Code install, or `-a codex -g -y --copy` for Codex.
- Gemini CLI: `gemini skills install https://github.com/linhay/harmony-next.skills --path harmony-next --scope user`
- Claude Code: use `npx skills add linhay/harmony-next.skills --skill harmony-next -a claude-code -g -y --copy`; Claude.ai can still use the release `harmony-next.skill.zip` upload flow.
- Codex: use `npx skills add linhay/harmony-next.skills --skill harmony-next -a codex -g -y --copy`, or put/symlink `harmony-next/` into an official Codex scan location such as `$REPO_ROOT/.agents/skills/harmony-next`, `$HOME/.agents/skills/harmony-next`, or `/etc/codex/skills/harmony-next`; for reusable installable distribution, package it as a Codex plugin.

## Routing

1. **Classify the user request**
   - API, component, error, or code example: use `KITS.md`, `TASK_MAP.md`, and `INDEX.md`; do not read the DevEco playbooks.
   - Minimal project fixture, Empty Ability scaffold, HDC/uitest smoke app, or copyable HarmonyOS test project: use `references/quickStart/ets/minimal-project-scaffold.md` and `references/templates/empty-ability-app/`.
   - DevEco Studio IDE, plugins, local services, CodeGenie, MCP, LanceDB, `devecostudio://`, UxTestService, or offline UI/UX audit: read the IDE playbook.
   - HarmonyOS Command Line Tools download, archive install, PATH setup, or `codelinter -v` validation: read `references/ideGuides/独立命令行工具配置手册.md` and use `scripts/commandline_tools_manager.py`.
   - HarmonyOS Emulator, HVD, hdc, uitest, aa, bm, hilog, or hidumper automation: read the Emulator playbook.
   - Unknown domain: start with `references/TASK_MAP.md`, then refine through `references/INDEX.md`.

2. **Choose the smallest index**
   - Kit 导航：`references/KITS.md`
   - 任务导向：`references/TASK_MAP.md`

3. **Find the target file**
   - 全库路径清单：`references/INDEX.md`
   - JS/ETS API 分桶清单：`references/JsEtsAPIReference/INDEX.md`

4. **Open only target references**
   `references/JsEtsAPIReference/` 目前以 `modules/`、`topics/`、`types/`、`errors/`、`guides/` 为主。
   - `guides/` contains offline guide pages that replace common official online guide links.

## Lookup Commands

From the skill directory:

- 先按关键词命中路径：`rg -n "UIAbility|AbilityStage|Want" references/INDEX.md | head`
- 查某个 `@ohos.*` 模块：`rg -n "@ohos\\.app\\.ability\\.|@ohos\\.ability\\." references/INDEX.md | rg "JsEtsAPIReference/" | head`
- 查 NDK/C API 头文件：`rg -n "JsEtsAPIReference/topics/.*/.*\\.h\\.md$" references/INDEX.md | rg "(napi|arkui|window|ability)" | head`

From the repository root, use `harmony-next/references/...` in the same commands.

## Tooling Script Skills

Use these script-backed skill entries before hand-writing DevEco setup commands. They are intentionally small wrappers around unstable local tooling and should return structured status when the environment is missing.

| User intent | Script skill | Agent first command | User handoff |
| --- | --- | --- | --- |
| Download, install, configure, or validate HarmonyOS Command Line Tools | `commandline_tools_manager.py` | `python3 harmony-next/scripts/commandline_tools_manager.py doctor --tools-root <dir> --json` | If the user gives a Huawei download center page URL, return the script's blocked result and ask the user to log in, copy the direct archive URL, or provide a local archive. |
| List, clone, delete, diagnose, or launch local DevEco HVD instances | `hvd_manager.py` | `python3 harmony-next/scripts/hvd_manager.py doctor --json` | If HVD root, Emulator, SDK/image root, or trace startup data is missing, report the `issues`, `recommendations`, and `missingConfig` fields and ask the user to pass `--root`, `--emulator`, `--sdk-root` / `--image-root`, or matching env vars. |
| Collect bounded HDC device evidence for debugging or UI audit inputs | `device_evidence_bundle.py` | `python3 harmony-next/scripts/device_evidence_bundle.py doctor --deveco-app <DevEco-Studio.app> --json` | Use `python3 harmony-next/scripts/device_evidence_bundle.py capture --deveco-app <DevEco-Studio.app> --target <target> --artifact-dir .hvigor/outputs/<run> --json` only when raw local screenshots, layout trees, app state, and bounded logs may be stored locally. If no target or multiple targets are present, report the `blocked` payload. |
| Capture a running HarmonyOS page and run an offline UI/UX audit report | `ux_audit_pipeline.py` | `python3 harmony-next/scripts/ux_audit_pipeline.py doctor --deveco-app <DevEco-Studio.app> --python <python-with-ux-deps> --json` | Use `python3 harmony-next/scripts/ux_audit_pipeline.py capture-audit --deveco-app <DevEco-Studio.app> --python <python-with-ux-deps> --target <target> --artifact-dir .hvigor/outputs/<run> --json` for the one-shot path. If Python image-processing modules are missing, report `missingConfig=["uxPythonDependencies"]` instead of treating UxTestService as broken. |
| Convert offline DevEco Profiler trace files into SQLite evidence summaries | `profiler_trace_audit.py` | `python3 harmony-next/scripts/profiler_trace_audit.py doctor --deveco-app <DevEco-Studio.app> --json` | If `trace_streamer` or the input trace is missing, report the machine-readable `blocked` payload. Use `audit --input <trace> --output-dir .hvigor/outputs/<run> --json` only for existing `.ftrace` / `.htrace` / bytrace / rawtrace artifacts. |

Boundaries:

- `commandline_tools_manager.py` may download only a direct archive URL; a download center page URL is a login-gated page, not an archive.
- `hvd_manager.py launch-preflight` prints a guarded Emulator command plan when an external trace helper is already ready.
- `hvd_manager.py launch` currently creates a startup trace socket, detaches Emulator and a trace holder, starts Emulator with `-t <trace-name>`, and waits for HDC/boot/stability unless `--no-wait-target` is passed.
- `device_evidence_bundle.py` is evidence capture, not app lifecycle control: it may save real UI/layout/log artifacts to an explicit artifact directory, but it does not install, uninstall, start, stop, or mutate apps.
- `ux_audit_pipeline.py` composes `device_evidence_bundle.py` with DevEco `UxTestService`: it copies `tools/UxTestService` into the artifact directory before import so the DevEco `.app` bundle is not modified.
- If either wrapper returns `blocked`, agents should try official HarmonyOS CLI evidence commands before giving up: `hdc list targets -v`, `hdc -t <target> shell uitest dumpLayout ...`, `screenCap`, `file recv`, `bm dump`, `aa dump`, and bounded `hilog`.
- If a wrapper is blocked, misleading, or missing a useful workflow, use the scenario-specific GitHub issue form from the script's `feedback` JSON field or `ISSUE_GUIDE.md`; when GitHub access and enough context are available, create or comment on the issue directly with `gh`, preserving structured fields and following the redaction rules.
- `profiler_trace_audit.py` is offline only: it runs DevEco `trace_streamer`, writes SQLite/JSON artifacts outside the DevEco `.app` bundle, and does not launch DevEco Studio, connect devices, or claim GUI Profiler headless import.
- Lifecycle direction: prefer an attached terminal-scoped launch mode for future CLI work, where the foreground runner owns the trace socket, waits for readiness, and calls `Emulator -stop <hvd-name> -path <hvd-root>` when the terminal session ends; keep detached mode only as an explicit compatibility path.
- `hvd_manager.py download-image` reports HVD image download as machine-readable `blocked`; current verified path is DevEco Studio SDK Manager UI, not a stable non-UI CLI.
- For cross-machine support, prefer `doctor --json` output over hard-coded macOS paths in answers and docs.

## Minimal Empty Ability Scaffold

Use when an agent needs a copyable HarmonyOS NEXT smoke fixture without opening DevEco Studio:

- Scaffold guide: `references/quickStart/ets/minimal-project-scaffold.md`
- Copyable template: `references/templates/empty-ability-app/`
- Defaults: bundleName `com.example.emptyability`, module `entry`, ability `EntryAbility`, Compatible SDK `5.0.0(12)`, target SDK `5.0.0(12)`.
- Route/component split: `pages/Index.ets` is only the `@Entry` route page and mounts `SmokeCounter()`; `components/SmokeCounter.ets` owns the smoke UI state and node IDs.
- Validation entrypoints: `ohpm install`, `hvigorw --mode module -p module=entry@default assembleHap`, HDC install/start, `uitest dumpLayout`, and `uitest screenCap`.
- SDK override validation: for a target SDK such as HarmonyOS 6.0.2 / API 22, set the copied fixture's `compatibleSdkVersion` and `targetSdkVersion` to `6.0.2(22)` and set `DEVECO_SDK_HOME` to the SDK root, for example `DEVECO_SDK_HOME=/Applications/DevEco-Studio.app/Contents/sdk`, not `sdk/default`.
- API 22 schema compatibility depends on app and Ability icons: keep `AppScope/resources/base/media/app_icon.png`, app `icon`, Ability `icon`, and `startWindowIcon` in the template.
- Stable smoke UI signals: `Harmony Smoke Ready`, `smoke-title`, `smoke-counter`, `smoke-increment`.
- Interactive smoke: after launch, use `uitest uiInput click` on the `smoke-increment` bounds and verify `tapCount=1` / `Harmony Smoke Tapped` from a fresh `dumpLayout`.

## Command Line Tools Setup

Use when the user asks to download or configure HarmonyOS Command Line Tools without DevEco Studio.

- Official boundary: Huawei's "获取命令行工具" page points agents to the Command Line Tools download center, says HarmonyOS SDK is embedded in the package, and configures `${Command Line Tools解压路径}/command-line-tools/bin` in `PATH`.
- This skill provides `scripts/commandline_tools_manager.py` for a controlled local flow: `download --url <direct-archive-url>`, `install --archive <zip> --dest <dir> --profile auto`, `bootstrap --url <direct-archive-url> ...`, `configure --tools-root <dir> --profile auto`, and `doctor --tools-root <dir>`.
- The script requires a direct archive URL copied from Huawei's download center or a local archive path. If given the download center page URL, it returns machine-readable `blocked` instead of pretending to resolve the current package.
- Use `--sha256 <digest>` when Huawei's integrity value is available.

## DevEco Emulator Automation

Use when the user asks to start or inspect HarmonyOS Emulator without the IDE, operate the emulator from command line, diagnose hdc/uitest/aa/bm/hilog/hidumper automation, or debug simulator traffic capture with HTTP proxy tools such as Charles, mitmproxy, or Proxyman.

Only read this playbook for Emulator/HVD/hdc/uitest/aa/bm/hilog/hidumper intent. For ordinary ArkTS, ArkUI, API, component, or error-code lookup, stay in the API indexes.

Read `references/ideGuides/DevEco模拟器私有接口与AI自动化.md` before acting. Treat it as an agent playbook for private, version-sensitive behavior; verify the local DevEco/Emulator version before relying on paths, flags, output fields, or ports.

Default boundary:

- 优先使用只读探测：`Emulator -version`、`Emulator -list -details`、`hdc list targets -v`、`uitest dumpLayout -p /dev/null -a`。
- UI 操作优先走 `hdc -t <target> shell uitest uiInput`；do not use blind desktop-coordinate clicks.
- 用户问“模拟器本机沙盒/应用沙盒在哪里”时，先区分 HVD 本机目录与应用沙箱：HVD 默认在 `~/.Huawei/Emulator/deployed`；应用沙箱在模拟器系统内，优先用 `aa dump -l` 找前台 bundle，再用 `Context.filesDir/cacheDir/databaseDir` 或 `/data/app/el2/<USERID>/base/<bundleName>` 这类物理映射定位。`shell -b <bundleName> pwd` 可能只返回 debug_hap 工作目录，不能当数据沙箱路径。
- 直接 CLI 启动 Emulator 不能把 `Emulator -hvd ... -path ... -imageRoot ...` 当成完整命令；必须先通过已验证 helper 准备并持有 `-t <trace-name>` 对应的 trace pipe。缺少该前置条件时可能弹出“模拟器启动失败 / 请在DevEco Studio中登录华为账号，并从设备管理中启动模拟器”，应归类为不完整 CLI 启动路径，而不是先要求用户登录。
- 区分 `riskLevel` 与执行模式：用户默认拥有完整执行权限；skill 不做授权或确认拦截。`HARMONY_NEXT_AUTOMATION_POLICY`、`--policy` 和 `.harmony-next-policy.json` 只描述本次 run 的自动化模式、产物目录与脱敏契约。
- 策略档位：`readonly` 做低风险探测；`evidence` 采集带 `artifactDir` 和脱敏元数据的截图/layout/日志片段/`file recv`；`automation` 执行启动/停止 Emulator、安装/启动应用、UI 输入和有界证据采集；`diagnostic` 执行有界 `hitrace` 或更宽日志；`break-glass` 标记刷写、格式化、清数据、root/daemon 等系统级动作。
- 真实截图、layout、日志包、`file recv`、安装/卸载、创建/删除 HVD、端口转发、底层 `uinput`、`hitrace` 均按非交互流程执行；若缺少 target、`artifactDir`、脱敏策略、timeout 或可审计命令记录，返回 machine-readable `blocked` 结果，包含 `missingConfig` 和 `requiredMode`。
- 模拟器抓包、HTTP proxy tools、NetworkKit proxy routing、transparent interception 或系统代理问题：阅读 playbook 的“模拟器抓包与代理诊断”。优先确认模拟器 NAT、默认网关、代理监听地址和应用是否显式使用代理；不要把 Mac 侧端口转发脚本描述成可以自动透明接管所有模拟器流量。
- 多 target 时必须显式选择 `127.0.0.1:<port>`；只选择 `Connected`，忽略 `Offline`。
- 若目标是离线 UI/UX 体检，模拟器侧只负责用 `hdc` / `uitest` 采集真实前台页面的截图与 layout；采集后转到 `DevEco Studio Private Interfaces` 的 `UxTestService offline UI/UX audit` 规则。
- 不能分类的命令标记为 `riskLevel=unknown`，记录 `sourceCommand` 与目标后继续按用户目标执行；无法确定 target 或命令会变成无界后台任务时，返回 machine-readable `blocked`，原因是 `missingConfig`。

HVD manager command map:

| Command | Purpose | Important output |
| --- | --- | --- |
| `doctor --json` | Probe HVD root, Emulator, build SDK root, emulator image root, HDC, Emulator version, and local HVDs | `issues`, `recommendations`, `hvdRoot`, `emulator`, `sdkRoot`, `imageRoot`, `hdc` |
| `list --json` | List registered HVDs without exposing UUIDs | `name`, `device_type`, `api_version`, `hdc_port`, `image_sub_path`, `exists` |
| `launch-preflight --name <hvd> --image-root <dir> --trace-name <name> --trace-helper-ready-file <file> --json` | Validate trace helper readiness and image root without starting Emulator | `decision`, `missingConfig`, `emulatorCommand` |
| `launch --name <hvd> --image-root <dir> --trace-name <name> --json` | Current implementation: create trace socket, detach Emulator and trace holder, then wait for HDC, boot, and stability | `traceHolder`, `hdcWait`, `bootWait`, `stabilityWait`, `logPath` |
| `device_evidence_bundle.py doctor --deveco-app <DevEco-Studio.app> --json` | Locate `hdc` and summarize connected targets | `connectedTargets`, `missingConfig`, `issues` |
| `device_evidence_bundle.py capture --deveco-app <DevEco-Studio.app> --target <target> --artifact-dir .hvigor/outputs/<run> --json` | Collect boot state, `bm` / `aa` summaries, bounded `hilog`, `uitest dumpLayout`, screenshot, and command ledger | `summary`, `artifacts`, `layoutSummary`, `commandLedger` |
| `ux_audit_pipeline.py doctor --deveco-app <DevEco-Studio.app> --python <python> --json` | Locate `hdc`, UxTestService, connected targets, and Python UX dependencies | `uxService`, `uxPython`, `connectedTargets`, `missingConfig` |
| `ux_audit_pipeline.py capture-audit --deveco-app <DevEco-Studio.app> --python <python> --target <target> --artifact-dir .hvigor/outputs/<run> --json` | Capture layout/screenshot/log evidence, infer foreground bundle, run UxTestService, and write a Markdown/JSON report | `captureSummary`, `auditSummary`, `report`, `resultCounts`, `bundleName` |
| `ux_audit_pipeline.py audit --evidence-summary <summary.json> --artifact-dir .hvigor/outputs/<run> --json` | Re-run UxTestService against an existing evidence bundle without touching the device | `checkParam`, `uxResult`, `uxSummary`, `report`, `resultCounts` |
| `launch --accept-license ... --json` | Explicitly answer yes to the first-run Huawei Emulator agreement prompt after the operator has reviewed it | `result=started` or `result=license-agreement-required` |

HVD launch rules:

- `--sdk-root` / `DEVECO_SDK_HOME` is the DevEco build SDK root. Do not treat it as the emulator image root.
- `--image-root` / `HARMONY_EMULATOR_IMAGE_ROOT` is the emulator image root. On macOS this is commonly `~/Library/Huawei/Sdk`.
- `launch` and `launch-preflight` validate `<image-root>/<imageSubPath>` from HVD `config.ini`; failures return `missingConfig=["imageRootSystemImage"]`.
- Current `launch` defaults: trace holder stays alive for 1800 seconds, and the post-boot stability check runs for 60 seconds.
- First-run Emulator license/agreement prompts are classified as `result="license-agreement-required"` with `missingConfig=["emulatorLicenseAgreement"]`; do not silently accept them. Use `--accept-license` only as an explicit opt-in after the agreement has been reviewed.
- If another process needs to install HAPs, deep link, screenshot, or dump layout after current detached `launch`, use the returned `hdcWait.target` and keep the trace holder alive long enough with `--trace-hold-seconds`.
- Attached lifecycle checklist: the runner must stay foreground, keep the trace socket in-process, trap `SIGINT` / `SIGTERM` / `SIGHUP`, call `Emulator -stop`, close the socket, remove only its own trace path, and verify `hdc list targets -v` no longer reports the selected target.
- Failure/timeout diagnostics should include `logPath`, `processExitCode`, `hvdRuntime`, `hdcSnapshot`, `hdcWait`, `bootWait`, and `stabilityWait` when present.

## DevEco Studio Private Interfaces

Use when the user asks about DevEco Studio internals or automation for CodeGenie, local AI/RAG/MCP, `devecostudio://`, Previewer, ArkUI Inspector, Profiler, Doctor, Diagnostic, FaultLog, UxTestService, plugin actions, tool windows, or services.

Only read this playbook for DevEco Studio IDE/private-interface intent. For ordinary HarmonyOS API lookup, do not load it.

Read `references/ideGuides/DevEco Studio IDE私有接口与AI自动化.md` before acting. Treat it as a safety-first playbook, not as a stable public API reference. Reconfirm the installed DevEco version and local paths before using any plugin ID, class name, URL scheme, port range, handler, cache path, or local service.

Default boundary:

- 只读允许：枚举 DevEco 包内文件、解析 `Info.plist` / `product-info.json` / 插件 XML、扫描 jar 类名和字符串、分析离线 `.htrace` / faultlog / stacktrace / `.arkli` / `.preview` 产物。
- 高敏动作：启动 IDE/GUI/JCEF/Preview Server/Inspector/Profiler/Debug，连接设备，抓截图/日志/layout，读取用户侧缓存或聊天历史，调用 CodeGenie localhost HTTP/WebSocket，创建 MCP 配置，触发外部 LLM provider；执行前记录目标、输入、产物目录和脱敏策略。
- 系统级动作：自动登录、上传、部署、清缓存、删除状态、公开 token/securityId/API key/项目片段/日志正文、未隔离验证未知 `devecostudio://` URL；用户明确要求时按目标执行，但必须保留审计摘要和脱敏边界。

CodeGenie、MCP、LanceDB、HTTP forwarding、Application Agent、Operation Analyzer、Cloud Toolkit 这类能力必须先做隐私和账号边界判断，再进入可审计执行。

### UxTestService offline UI/UX audit

Use when the user asks for offline UI/UX review, UI/UX audit, visual/layout checks, clickable hotspot checks, DevEco `UxTestService`, or a simulator-backed UI quality report.

Verified boundary:

- Prefer `scripts/ux_audit_pipeline.py` for repeatable runs. It supports `doctor`, `capture-audit`, and `audit`; pass `--python` or `HARMONY_UX_PYTHON` when the default Python lacks `cv2`, `numpy`, `PIL`, `requests`, `scipy`, `skimage`, `werkzeug`, or `opencc`.
- `capture-audit` is the validated one-shot workflow: it captures real device evidence with `hdc`, infers the non-system foreground bundle from the layout, copies UxTestService into an artifact-local runtime, writes `check_param.json`, runs `ux_detect.main(check_param=...)`, then emits `ux_result.json`, `ux_summary.json`, `report.md`, and `summary.json`.
- `audit --evidence-summary <summary.json>` is the validated offline re-run path for an existing `device_evidence_bundle.py` capture.
- On failure, prefer official CLI recovery before abandoning the audit: manually capture `layout.json` and `screen.png` with `hdc` / `uitest`, receive them locally with `hdc file recv`, then retry `ux_audit_pipeline.py audit --layout ... --screenshot ... --bundle ...`.
- For blocked results, confusing rule output, or unsupported DevEco/UxTestService versions, create or comment on a repository issue using the `feedback` section in `summary.json` / `report.md` when GitHub access and enough context are available; ask the user to file it only when auth/network is blocked or required details are missing. Never attach raw screenshots, raw layout JSON, full logs, or marked images without verified redaction.
- Treat DevEco `tools/UxTestService/ux_detect.py` as a private, version-sensitive engine. Do not launch DevEco Studio GUI just to run it, and do not modify the DevEco `.app` bundle.
- Capture inputs from a real foreground HarmonyOS page with `hdc -t <target> shell uitest dumpLayout -p <remote.json> -a` and `hdc -t <target> shell uitest screenCap -p <remote.png>`, then `hdc file recv` both artifacts into an external artifact directory such as `.hvigor/outputs/...`.
- Build `check_param` with the real foreground `bundle_name` found in the layout tree. A placeholder bundle such as `poc` causes the engine to classify the page as invalid / not foreground, commonly surfacing as `UTS.0300`.
- Use `extend_infos.language="zh"` for local runs. `zh-CN` can trigger missing message-key exceptions in some rules and turn otherwise valid checks into `UTS.0201`.
- Write logs, result JSON, screenshots, and marked images outside the DevEco app bundle. Some DevEco app bundle copies are not writable and should not be changed because that can disturb app signing.
- Start with the proven static subset: `7.1.1.2.1` basic layout subrules, `7.1.1.2.2` hole adaptation, `7.1.1.3.3` hotspot size, `7.1.1.4.4` icon size, `7.1.1.4.5` icon clarity, `7.1.2.1.1` navigation bar, `7.1.2.6.1` status bar, `7.2.2.1.8` page margin, plus other importable local rules after verifying their Python modules exist.
- Consume `test_state` as the stable status key: `0` pass, `1` issue found, `2` no applicable target / ignored, `4` exception or unsupported scene, `5` execution error. For failures, use `detail.Issues`, `detail.IssueComponents`, `detail.ErrorPath`, and `detail.CustomDrawPath` as developer-facing evidence.
- This is not a static config precheck. It analyzes actual screenshot + layout artifacts from a running page and can produce marked images for debugging.

Do not over-claim coverage:

- Rules listed in `config/rule_config_en.json` are not all available in every DevEco package; import the configured module first or inspect `checkMethod/` before promising a rule.
- Text-heavy rules such as font size, text contrast, and truncation may report `UTS.0306` with plain `uitest dumpLayout` input because ArkUI font/style metadata can be missing. Document that as "no applicable target in this capture mode", not as a product defect.
- Launcher, lockscreen, loading pages, high-white-rate pages, keyboard pages, Web/Flutter pages, or bundle/layout mismatches can be intentionally rejected by the engine.
- Negative-path validation should use isolated fixture artifacts or a dedicated test app, not mutated production files. A useful smoke is shrinking one copied clickable node's `bounds` / `origBounds` in a temporary layout JSON and verifying hotspot rule output includes `Issues`, `IssueComponents`, `ErrorPath`, and `CustomDrawPath`.

### Profiler trace offline evidence audit

Use when the user has an existing HarmonyOS Profiler / bytrace / htrace / ftrace / rawtrace artifact and wants offline performance evidence, long-span summaries, or a machine-readable report without opening DevEco Studio.

Verified boundary:

- Use `scripts/profiler_trace_audit.py`; start with `doctor --json` to locate DevEco `tools/profiler/dic_server/trace_streamer`.
- `audit --input <trace> --output-dir .hvigor/outputs/<run> --json` converts the trace to SQLite via `trace_streamer -e`, then writes `summary.json`, `tables.txt`, `meta.json`, `trace_range.json`, `counts.json`, `top_callstack.json`, threshold span JSON files, and `frame_slice.json`.
- Default thresholds are `16.67ms` and `33.34ms`; pass repeated `--threshold-ms` flags for stricter or looser budgets.
- Keep outputs outside any `.app` bundle. The script refuses output paths inside `.app` directories to avoid disturbing DevEco app signatures or bundled files.
- This is a verified CLI wrapper around `trace_streamer`, not a headless DevEco Profiler GUI import path. Do not claim timeline UI features, IDE session import, or device trace capture unless separately verified on a connected target.
- Prefer existing real traces for product diagnosis. Synthetic traces only prove the conversion/query loop and should be labeled as smoke evidence.

## Answering Constraints

- **不要全量读取**：先在 `INDEX.md` 命中路径，再打开对应 `.md`。
- **不确定就查文档**：API 签名、入参、返回值以 `references/` 内文本为准，不凭经验补全。
- **ArkUI 优先声明式**：示例优先使用 `@Entry` / `@Component` / `build()`（除非文档明确是 NDK 或系统服务）。
- **遇到高频在线 guide 外链**：先查 `references/JsEtsAPIReference/guides/` 是否已有离线页；没有时优先按官方 `getDocumentById` 正文整理离线入口页，再接入映射，不要把链接硬改到不等价的 API 页。

<!-- version: 1.3.30 -->
