# DevEco 模拟器私有接口 Agent Playbook

> 面向 AI agent 使用。这里不是团队过程记录，也不是稳定公开 API；它只说明 agent 在处理 DevEco Studio 本地 HarmonyOS Emulator 自动化请求时，如何选择命令、控制风险、采集最小证据并向用户报告。

## 何时使用

用户请求包含以下意图时使用本页：

- 免启动 IDE 启动或检查 HarmonyOS Emulator。
- 使用 `hdc`、`uitest`、`aa`、`bm`、`hilog`、`hidumper` 操作或诊断模拟器。
- 选择 HDC target、等待 boot completed、启动应用、做 UI 输入或截图。
- 排查 DevEco Studio 模拟器/HVD/命令行自动化链路。

## 先做什么

1. 明确用户目标：只读诊断、启动模拟器、操作 UI、安装/卸载应用、采集日志/截图，还是系统级调试。
2. 先执行只读能力探测，确认当前机器路径、版本、HVD 和 HDC target。
3. 需要真实 UI 内容、设备文件、端口转发、安装卸载、启动/停止模拟器或写文件时，按自动化策略记录风险、产物目录、脱敏状态和命令摘要；不进入等待输入流程。
4. 多 target 时必须让用户指定或基于明确上下文选择 `Connected` 的 `127.0.0.1:<port>`；不要默认选第一个。
5. 命令必须设置超时；禁止无界后台进程或无限日志流。

## 常见路径候选

先探测，不要假设一定存在：

```bash
EMULATOR="/Applications/DevEco-Studio.app/Contents/tools/emulator/Emulator"
HDC="/Applications/DevEco-Studio.app/Contents/sdk/default/openharmony/toolchains/hdc"
HVD_ROOT="$HOME/.Huawei/Emulator/deployed"
IMAGE_ROOT="$HOME/Library/Huawei/Sdk"
```

已知验证过的环境线索：DevEco Studio 6.0.2，HarmonyOS Emulator 6.0.2.200。其他版本必须重新探测。

## 模拟器本机目录与应用沙箱速查

- HVD 本机实例目录默认是 `$HOME/.Huawei/Emulator/deployed`；这是虚拟设备配置和镜像实例目录，不等于应用沙箱。
- 应用沙箱在模拟器系统内。应用视角常见路径：`/data/storage/el2/base/haps/entry/files`、`/data/storage/el2/base/haps/entry/cache`、`/data/storage/el2/database`。
- HDC/调试进程视角常见物理映射：`/data/storage/el2/base` -> `/data/app/el2/<USERID>/base/<bundleName>`，`/data/storage/el2/database` -> `/data/app/el2/<USERID>/database/<bundleName>`；普通调试用户常见 `<USERID>` 为 `100`。
- 定位应用沙箱优先用只读命令：`hdc -t <target> shell aa dump -l` 找前台 bundle，再查 `/data/app/el2/<USERID>/base/<bundleName>` 和 `/data/app/el2/<USERID>/database/<bundleName>`；应用内路径以 `Context.filesDir` / `cacheDir` / `databaseDir` 为准。`shell -b <bundleName> pwd` 可能只返回 `/mnt/debug/.../debug_hap/<bundleName>`，不能当数据沙箱路径。需要取回文件时，用 `hdc -t <target> file recv <remote> <local>`，并按 `evidence` 模式记录 artifact 目录和脱敏策略。

## 自动化策略模型

本 playbook 把风险分级和执行模式拆开：

- `riskLevel` 说明命令的敏感度和影响面。
- `policy` 说明本次 run 的自动化模式、产物目录和脱敏契约，不代表授权。
- 用户默认拥有完整执行权限；skill 不向用户索要许可，也不把高风险动作改写成等待输入。
- 长时间自动化必须非交互运行；只有缺少 target、artifact 目录、脱敏策略、timeout、命令参数等客观前置条件时，才返回 machine-readable `blocked` 结果。

策略可来自以下通道，优先级由具体 runner 固定并写入 run 记录：

```bash
HARMONY_NEXT_AUTOMATION_POLICY=automation
<runner> --policy <readonly|evidence|automation|diagnostic|break-glass>
```

也可以使用 repo-local 配置：

```json
{
  "policy": "automation",
  "artifactDir": "docs-linhay/screenshots/20260520/emulator",
  "redactionPolicy": "harmony-next-default-v1",
  "targets": ["127.0.0.1:10100"]
}
```

配置文件名建议固定为 `.harmony-next-policy.json`。进入 `evidence`、`automation`、`diagnostic` 或 `break-glass` 时，若操作会保存真实 UI、layout、日志、设备文件或录屏，必须提供显式 `artifactDir` 和脱敏策略；不满足时视为运行配置缺失，而不是权限不足。

策略档位：

| policy | 允许范围 |
| --- | --- |
| `readonly` | 只允许低风险只读探测、状态摘要、`/dev/null` layout/screenshot 能力探测 |
| `evidence` | 允许截图、layout、日志片段、`file recv` 保存到显式 `artifactDir`，并要求脱敏元数据 |
| `automation` | 允许 Emulator 生命周期、应用安装/启动、UI 输入、bounded logs、证据采集 |
| `diagnostic` | 执行有界 `hitrace`、更宽 `hilog`、诊断包，仍需 timeout、大小上限和脱敏 |
| `break-glass` | 标记刷写、格式化、清数据、root/daemon、通配删除等系统级动作；用户明确目标后可执行，并必须保留审计摘要 |

每个 gate 结果必须记录：

```json
{
  "riskLevel": "evidence",
  "policy": "readonly",
  "operation": "uitest.screenCap.recv",
  "target": "127.0.0.1:10100",
  "artifacts": [],
  "redactionStatus": "not_applicable",
  "sourceCommand": "hdc -t 127.0.0.1:10100 shell uitest screenCap -p /data/local/tmp/ai-screen.png",
  "decision": "blocked",
  "requiredMode": "evidence",
  "missingConfig": ["artifactDir", "redactionPolicy"],
  "reason": "artifactDir and redactionPolicy are required for real screenshot capture"
}
```

允许执行时也要记录同一批字段，`decision` 为 `allowed`，`artifacts` 指向已脱敏或待清理产物。严禁把 token、cookie、设备唯一标识、完整业务 payload 或未脱敏原文写入 gate 结果。

系统级动作不被 skill 禁止，但必须进入 `break-glass` 模式并写清目标、命令、恢复策略和审计摘要：`hdc target mount`、`hdc smode`、`hdc flash`、`hdc erase`、`hdc format`、`hdc sideload`、无边界清数据、刷写、root/daemon 模式、通配删除。`break-glass` 是风险标签，不是授权门槛。

## 最小只读探测流程

首轮只做能力和状态摘要，不保存真实 UI、layout、日志原文或设备文件。每条命令必须由上层 runner 设置超时；macOS 默认不一定有 GNU `timeout`，不要依赖 shell 内置超时能力。

```bash
# runner timeout: 5s
"$EMULATOR" -version

# runner timeout: 5s
"$EMULATOR" -list

# runner timeout: 8s
"$EMULATOR" -list -details

# runner timeout: 5s
"$HDC" list targets -v
```

只向用户摘要：Emulator 版本、HVD 名称/数量、HVD 是否运行、HDC target 数量、`Connected` target 列表。不要回显完整 JSON、完整 target 明细或日志。

## 风险分级

### 默认允许

只读、低敏、短生命周期命令：

```bash
"$EMULATOR" -version
"$EMULATOR" -list
"$EMULATOR" -list -details
"$HDC" list targets -v
"$HDC" -t "$TARGET" shell param get bootevent.boot.completed
"$HDC" -t "$TARGET" shell bm dump -g
"$HDC" -t "$TARGET" shell bm dump -n "<bundleName>"
"$HDC" -t "$TARGET" shell aa dump -l
"$HDC" -t "$TARGET" shell aa dump -r
"$HDC" -t "$TARGET" shell hidumper -ls
"$HDC" -t "$TARGET" shell hilog -z 100
"$HDC" -t "$TARGET" shell uitest dumpLayout -p /dev/null -a
"$HDC" -t "$TARGET" shell uitest screenCap -p /dev/null
```

`bm dump`、`aa dump`、`hilog` 输出可能包含应用名、路径或错误文本；报告时只保留必要摘要。

### 执行模式标注

- `automation`：启动或停止 Emulator。
- `automation`：安装、卸载、启动应用。
- `automation`：创建、复制、删除或清理 HVD，需限定实例名和恢复策略。
- `evidence`：`hdc file recv`、保存真实 layout、截图、录屏、日志包或沙箱内容，必须写入显式 `artifactDir`。
- `automation`：`hdc file send` 和新增或删除 `fport/rport` 端口转发，必须限定 target、端口和生命周期。
- `diagnostic`：有界 `hitrace`、底层 `uinput`、大范围 `hilog -x`。
- `diagnostic`：电源、显示、折叠、窗口策略切换，必须记录恢复动作。
- `break-glass`：清数据、刷写、格式化、root/daemon、通配删除等系统级动作。

### 系统级动作

用户明确目标时可以执行；执行前后必须记录 target、命令摘要、恢复策略、产物目录和脱敏状态：

```bash
hdc target mount
hdc smode
hdc flash
hdc erase
hdc format
hdc sideload
param set
bm clean
wukong exec
wukong special
wukong focus
```

无法分类的命令标记为 `riskLevel=unknown`，不请求确认；若缺少 target、timeout 或命令参数，返回 `blocked` 并给出 `missingConfig`。

## 启动模拟器

当前版本线索显示：直接启动 Emulator 通常需要 `-hvd`、`-path`、`-imageRoot`，并需要 `-t <trace-name>` 对应的本地占位通道。占位通道是启动期依赖，不要把它当稳定控制协议。

不要把 `Emulator -hvd ... -path ... -imageRoot ...` 当成完整启动命令。缺少 `-t <trace-name>` 或缺少已准备好的 trace pipe 时，DevEco Emulator 可能弹出以下登录/设备管理模态框：

```text
模拟器启动失败
请在DevEco Studio中登录华为账号，并从设备管理中启动模拟器
```

这类弹窗优先归类为不完整 CLI 启动路径的已知症状。不要立即引导用户登录；先停止启动尝试，检查 trace pipe helper 是否已准备并持有对应通道。

`<trace-name>` 处理规则：

- 优先沿用当前任务或已验证 helper 生成的唯一 trace name。
- 找不到已验证 helper 或 helper readiness 信号时，返回 machine-readable `blocked`，不要执行部分启动命令。
- 若缺少占位通道导致启动失败，停止本轮启动尝试，只报告 Emulator 版本、HVD 名称、命令类型、已知 modal 症状和裁剪后的错误摘要，不继续 UI 自动化。
- 不记录或沉淀 HVD 内部字段、trace pipe 私有协议或未验证 helper 细节。

脚本化时先用仓库 helper 做 preflight。该命令只验证 HVD、Emulator、SDK 和 trace helper readiness，不负责创建私有 trace pipe，也不直接启动 Emulator：

```bash
python3 "$HARMONY_NEXT_SKILL_DIR/scripts/hvd_manager.py" \
  --root "$HOME/.Huawei/Emulator/deployed" \
  --emulator "/Applications/DevEco-Studio.app/Contents/tools/emulator/Emulator" \
  --sdk-root "$HOME/Library/Huawei/Sdk" \
  launch-preflight \
  --name "<hvd-name>" \
  --trace-name "<trace-name>" \
  --trace-helper-ready-file "<helper-ready-file>" \
  --json
```

若 helper 不可用，期望输出 `decision=blocked`、`missingConfig=["tracePipeHelper"]`，并包含上述已知 modal 症状。

需要由仓库脚本直接执行启动时，使用 `launch`。当前实现会创建本轮启动用的有界 trace socket，detach Emulator 与 trace holder，启动 Emulator，并在默认路径下等待 HDC target；只想验证启动进程与 trace socket 连接时传 `--no-wait-target`：

```bash
python3 "$HARMONY_NEXT_SKILL_DIR/scripts/hvd_manager.py" \
  --root "$HOME/.Huawei/Emulator/deployed" \
  --emulator "/Applications/DevEco-Studio.app/Contents/tools/emulator/Emulator" \
  launch \
  --name "<hvd-name>" \
  --image-root "$HOME/Library/Huawei/Sdk" \
  --trace-name "<trace-name>" \
  --timeout 30 \
  --json
```

`launch` 输出 `decision=allowed`、`operation=emulator.launch`、`result=started`、`socketConnected=true`、`traceBytesRead` 和实际 `emulatorCommand`。缺少 HVD、Emulator、image root 或 trace name 时返回 machine-readable `blocked`，不要退回到裸 `Emulator -hvd ... -path ... -imageRoot ...`。

### 生命周期模型

后续 CLI 应区分两种启动生命周期：

| 模式 | 语义 | 清理责任 |
| --- | --- | --- |
| `attached` | 一个前台终端托管一个模拟器；终端活着，模拟器活着 | runner 捕获退出信号，调用 `Emulator -stop <hvd-name> -path <hvd-root>`，关闭 trace socket，并验证 HDC target 消失 |
| `detached` | 启动命令返回后模拟器继续运行，用于兼容已有后续自动化步骤 | 调用方必须显式停止 HVD，并持有足够长的 trace holder |

attached 模式是推荐方向，因为它更接近 Android Emulator 的终端会话模型，也能降低孤儿模拟器和悬空 trace holder 的概率。实现 attached 前不要把不存在的 `--lifecycle` 参数写入对外命令示例；当前脚本仍按 detached 行为描述。

attached 生命周期核查表：

1. 父 runner 保持前台运行，不能在启动成功后立即退出。
2. trace socket 由父 runner 或同一进程内 worker 持有，不再创建脱离终端的 trace holder。
3. `SIGINT`、`SIGTERM`、`SIGHUP` 和正常退出路径都进入同一个 cleanup。
4. cleanup 优先执行 `Emulator -stop "<hvd-name>" -path "<hvd-root>"`，再清理本轮创建的 trace path。
5. cleanup 只删除当前 `run_id` / `trace-name` 绑定的资源，不清理未知进程或固定路径。
6. 退出前采集裁剪后的 `Emulator -list -details` 与 `hdc list targets -v` 摘要，用于确认目标停止或记录清理失败。
7. detached 仍作为显式兼容模式保留，文档必须说明调用方负责后续停止。

使用模板：

```bash
cd "/Applications/DevEco-Studio.app/Contents/tools/emulator"

./Emulator \
  -hvd "<hvd-name>" \
  -path "$HOME/.Huawei/Emulator/deployed" \
  -t "<trace-name>" \
  -imageRoot "$HOME/Library/Huawei/Sdk"
```

多实例时显式指定不同 HDC 端口：

```bash
./Emulator \
  -hvd "<hvd-name>" \
  -path "$HOME/.Huawei/Emulator/deployed" \
  -t "<trace-name>" \
  -imageRoot "$HOME/Library/Huawei/Sdk" \
  -hdcport 10100
```

停止指定 HVD：

```bash
"/Applications/DevEco-Studio.app/Contents/tools/emulator/Emulator" \
  -stop "<hvd-name>" \
  -path "$HOME/.Huawei/Emulator/deployed"
```

## HVD 管理 CLI

仓库提供一个受控命令行封装：

```bash
python3 "$HARMONY_NEXT_SKILL_DIR/scripts/hvd_manager.py" list --json
python3 "$HARMONY_NEXT_SKILL_DIR/scripts/hvd_manager.py" doctor --json
python3 "$HARMONY_NEXT_SKILL_DIR/scripts/hvd_manager.py" create --from "<source-hvd>" --name "<new-hvd>" --hdc-port 10100
python3 "$HARMONY_NEXT_SKILL_DIR/scripts/hvd_manager.py" delete --name "<new-hvd>" --confirm-name "<new-hvd>"
python3 "$HARMONY_NEXT_SKILL_DIR/scripts/hvd_manager.py" launch-preflight --name "<hvd-name>" --trace-name "<trace-name>" --trace-helper-ready-file "<helper-ready-file>" --json
python3 "$HARMONY_NEXT_SKILL_DIR/scripts/hvd_manager.py" launch --name "<hvd-name>" --image-root "<sdk-image-root>" --trace-name "<trace-name>" --json
python3 "$HARMONY_NEXT_SKILL_DIR/scripts/hvd_manager.py" download-image --device-type phone --api-version 22
```

边界：

- 跨机器分发时，先运行 `doctor --json`，根据输出中的 `hvdRoot`、`emulator`、`sdkRoot`、`issues` 和 `recommendations` 判断是否需要让用户补路径。
- `list` 只读解析 `$HOME/.Huawei/Emulator/deployed/*.ini` 和每个实例的 `config.ini`。
- `doctor` 探测本机平台、HVD root、Emulator 可执行文件、SDK root、Emulator 版本和已注册 HVD；输出不包含 HVD UUID。
- `create` 克隆一个同版本本地实例，刷新根 `<name>.ini`、实例 `config.ini`、`hardware-qemu.ini` 中的名称、路径、UUID 与可选 HDC 端口；默认不复制 `Log`。
- `delete` 删除根 `<name>.ini`、实例目录和 `lists.json` 中的同名条目；必须传 `--confirm-name` 且值与目标名完全一致。
- `launch-preflight` 验证 HVD、Emulator、SDK root、`traceName` 和 trace helper readiness；缺少 helper 时返回 `blocked`，满足时只输出包含 `-t <trace-name>` 的启动命令计划，不直接执行 Emulator。
- 当前 `launch` 创建 `/tmp/<trace-name>` 启动期 trace socket，执行带 `-t <trace-name>` 的 Emulator 命令，并可等待 `hdc list targets -v` 中出现 `Connected`；多实例必须使用不同 trace name 和 HDC 端口。后续新增生命周期参数时，attached 应成为推荐路径，detached 应保留为显式兼容路径。
- `download-image` 目前不下载，只输出 machine-readable `blocked`。DevEco Studio 6.0.2.642 中下载镜像走 SDK Manager UI API，尚未验证稳定的非 UI 下载入口。

环境适配：

- HVD root：优先 `--root`，其次 `HARMONY_HVD_ROOT` / `DEVECO_HVD_ROOT` / `HVD_ROOT`，最后 `$HOME/.Huawei/Emulator/deployed`。
- Emulator：优先 `--emulator`，其次 `HARMONY_EMULATOR` / `DEVECO_EMULATOR` / `EMULATOR`，再查 PATH 与常见 DevEco Studio 安装路径。
- SDK root：优先 `--sdk-root`，其次 `DEVECO_SDK_HOME` / `HOS_SDK_HOME` / `HARMONY_SDK_HOME`，再查常见 DevEco Studio SDK 路径。

## 等待可操作状态

1. 等待 `hdc list targets -v` 中目标为 `TCP Connected`。
2. 查询启动完成：

```bash
"$HDC" -t "$TARGET" shell param get bootevent.boot.completed
```

期望返回 `true`。如果不可用，只能把 Emulator 日志中的 `Guest OS Boot Completed!!` 当辅助线索。

超时后停止 UI 操作，只报告 target 状态、boot 状态和裁剪后的日志摘要。

## 失败分流

- 没有 HDC target：停止 UI 自动化，报告 Emulator/HVD 探测摘要；非交互 run 返回 `blocked`，`missingConfig` 为 `target`。
- 只有 `Offline` target：不执行 shell、uitest 或输入动作；报告 target 状态并建议重启/等待连接。
- 多个 `Connected` target 且用户未指定：停止，要求用户选择 `127.0.0.1:<port>`。
- boot completed 超时或不是 `true`：不点击、不输入，只保留 boot 参数和连接摘要。
- `uitest dumpLayout -p /dev/null -a` 不支持或返回权限错误：不默认改为真实路径采集；先降级到其他只读诊断，真实 layout/screenshot 需要 `artifactDir` 和脱敏配置。
- 脱敏失败：不归档、不回显原文。

## UI 自动化

优先使用设备侧 `uitest`，不要盲点桌面坐标。

只读探测：

```bash
"$HDC" -t "$TARGET" shell uitest dumpLayout -p /dev/null -a
"$HDC" -t "$TARGET" shell uitest screenCap -p /dev/null
```

真实内容采集需要显式 `artifactDir` 和脱敏配置：

```bash
"$HDC" -t "$TARGET" shell uitest dumpLayout -p /data/local/tmp/ai-layout.json -a
"$HDC" -t "$TARGET" shell cat /data/local/tmp/ai-layout.json
"$HDC" -t "$TARGET" shell uitest screenCap -p /data/local/tmp/ai-screen.png
"$HDC" -t "$TARGET" file recv /data/local/tmp/ai-screen.png ./ai-screen.png
```

输入模板：

```bash
"$HDC" -t "$TARGET" shell uitest uiInput click <x> <y>
"$HDC" -t "$TARGET" shell uitest uiInput swipe <x1> <y1> <x2> <y2>
"$HDC" -t "$TARGET" shell uitest uiInput drag <x1> <y1> <x2> <y2>
"$HDC" -t "$TARGET" shell uitest uiInput keyEvent Home
"$HDC" -t "$TARGET" shell uitest uiInput keyEvent Back
"$HDC" -t "$TARGET" shell uitest uiInput text "<escaped-text>"
```

规则：

- 坐标来源优先级：可解析的 dumpLayout 节点坐标 -> 截图辅助定位 -> 用户明确给出的坐标 -> `uinput` 或桌面坐标兜底。
- 每步输入后重新探测状态。
- 用户输入文本必须转义，不能拼接原文 shell。
- `uinput` 作为底层输入兜底，必须记录 `riskLevel=diagnostic`。

## 应用启动与诊断

启动前先定位 bundle 和 ability：

```bash
"$HDC" -t "$TARGET" shell bm dump -n "$BUNDLE"
"$HDC" -t "$TARGET" shell aa start -b "$BUNDLE" -a "$ABILITY"
```

不知道 ability 时，从 `bm dump -n` 的裁剪输出中查 `mainAbility`、`mainElementName` 或 `abilityInfos[].name`。

## WebView DevTools 与 CDP 字段证明

当目标是 ArkWeb/H5 bridge 字段到达证明时，先阅读 `ArkWeb WebView CDP调试与字段到达证明.md`。不要用项目私有转发脚本或全局 HDC 重启替代结构化诊断。

```bash
python3 "$HARMONY_NEXT_SKILL_DIR/scripts/device_evidence_bundle.py" webview-devtools \
  --deveco-app /Applications/DevEco-Studio.app \
  --target <target> \
  --artifact-dir .hvigor/outputs/webview-devtools \
  --json
```

- wrapper 枚举 `webview_devtools_remote_*`、列出 `fport`、识别 stale forward，并探测 `/json` 与 `/json/version`。
- 多 socket 时必须传 `--remote-socket webview_devtools_remote_<pid>`。
- 默认只删除本轮创建的转发；`--replace-stale` 只处理占用所选本地端口且远端 socket 已消失的任务。
- 字段到达使用 CDP `Runtime.evaluate`，设置 `awaitPromise=true`、`returnByValue=true`，只返回小型脱敏 JSON。
- `Page.captureScreenshot` 挂起时立即放弃截图路径；bridge callback JSON 才是主证据。
- `dumpLayout` 或截图若来自锁屏、桌面或其他前台页面，标记为无效支持证据。

常用只读诊断：

```bash
"$HDC" -t "$TARGET" shell hidumper --cpuusage <pid>
"$HDC" -t "$TARGET" shell hidumper --mem <pid> --prune
"$HDC" -t "$TARGET" shell hidumper --net <pid>
"$HDC" -t "$TARGET" shell hidumper --storage <pid>
"$HDC" -t "$TARGET" shell hilog -z 100
```

## 模拟器抓包与代理诊断

本节面向使用者处理 HarmonyOS Emulator 流量无法被抓包工具捕获的问题，适用于 Charles、mitmproxy、Proxyman 或其他显式 HTTP 代理工具。先区分三种能力：应用级代理、系统/全局代理、透明接管流量。不要把其中一种能力的结论外推到另一种。

### 已验证的网络形态

常见 DevEco 模拟器网络是 NAT：

- 模拟器设备 IP 可能是 `10.0.2.15`。
- 默认网关可能是 `10.0.2.2`。
- Mac 上的 `127.0.0.1:<port>` 只代表宿主机本机回环地址；模拟器内访问 `127.0.0.1` 时指向模拟器自身，不会自动到达宿主机代理。
- 抓包工具的显式 HTTP 代理端口通常要以宿主机可达地址暴露，例如 `10.0.2.2:9090` 或宿主机局域网 IP 对应端口。具体端口以所使用工具的监听配置为准。

只读诊断建议：

```bash
hdc list targets -v
hdc -t <target> shell ifconfig
hdc -t <target> shell netstat -rn
hdc -t <target> shell netstat -ant
```

如果使用的抓包工具提供 CLI，可以额外读取它的代理监听地址；例如 Proxyman 可用 `proxyman-cli proxy-host`。没有 CLI 时，从工具 UI 中确认 HTTP/HTTPS 代理端口和是否允许外部设备连接。

若打开测试页面后，设备侧 `netstat` 显示从模拟器 IP 直接连接目标站点的 `:80` 或 `:443`，且没有连接代理端口，则说明调试目标应用或系统组件没有走代理。

### DevEco/Emulator 自带代理入口的边界

DevEco Studio 6.1.1 / HarmonyOS Emulator 6.1.1.200 暴露了两类容易被误读的代理入口：

- `Emulator -http_proxy <url>` 只出现在 `-imageList`、`-install`、`-screenProfileList` 和 `-config` 这类宿主侧管理命令上。二进制字符串显示它会进入 `InputParametersParser::ApplyNetworkProxyEnvironment()`，并在下载镜像或访问远端元数据失败时提示 `Please check your network or use -http_proxy to configure a proxy`。这应归类为管理器代理或下载代理，不等于已经启动的 guest 业务流量代理。
- Emulator UI 里存在 `networkProxyPanel` / `WidgetNetworkProxy`，支持 `use.ide.proxy`、`manual.proxy.configuration`、`no.proxy`、SOCKS、认证、DNS 和连接测试。二进制字符串显示它会调用 `WidgetNetworkProxy::SetNetworkProxyAndSendRequest()` / `SendProxySettingsToAgent()` / `ApplyProxySettings()` / `ApplyDnsSettings()`，说明 UI 可能通过私有 agent 把代理配置发送进 guest。该入口尚未验证为稳定 CLI，也不应等同于透明抓取所有 TCP/TLS 流量。

只读运行态可用以下证据区分代理层级：

```bash
Emulator -help | grep -A20 http_proxy
strings -a "$EMULATOR" | grep -i -E 'WidgetNetworkProxy|ApplyNetworkProxyEnvironment|proxy-settings.ini'
hdc -t <target> shell param get | grep -i proxy
hdc -t <target> shell netstat -ant
lsof -Pan -p <emulator-pid> -i
```

若 `param get` 没有默认代理配置，`netstat` 和宿主 `lsof` 仍显示 guest 通过 QEMU/slirp 直接连接外部 IP，而不是连接 `10.0.2.2:<proxy-port>` 或抓包工具端口，则说明当前流量没有走显式代理。

### 可稳定使用的方案

应用级代理是最稳定的调试入口。对 `@kit.NetworkKit` 的 HTTP 请求，调试目标应用应显式设置应用代理，并在请求参数中启用代理：

```ts
import { connection, http } from '@kit.NetworkKit';

connection.setAppHttpProxy({
  host: '10.0.2.2',
  port: 9090,
  exclusionList: []
} as connection.HttpProxy);

let request = http.createHttp();
request.request(url, {
  usingProxy: true
});
```

WebSocket、RCP、下载组件、Socket/TLSSocket 等网络栈各有自己的代理配置项；不要假设设置 HTTP 请求后能覆盖所有网络调用。HTTPS 明文抓包还需要让调试目标应用信任抓包工具 CA；如果启用了 certificate pinning，需要在调试构建中关闭或替换对应 pin。

证书信任和代理路由要分开处理。HarmonyOS SDK 暴露了 `certificateManagerDialog.openInstallCertificateDialog` 与 `certificateManager.installUserTrustedCertificateSync`，说明平台存在安装用户信任 CA 的能力；但这些入口受 `ACCESS_CERT_MANAGER`、`ACCESS_USER_TRUSTED_CERT` 或企业证书权限限制，并可能受设备安全策略影响。普通三方调试应用不应默认能静默安装全局 CA。

对调试目标应用，NetworkKit HTTP 请求可用 `HttpRequestOptions.caPath` 或 `caData` 指定抓包工具 CA，其中 `caPath` 目前要求 `.pem` 文本证书路径，`caData` 传入 `.pem` 证书内容。该方式只影响对应 HTTP 请求，不等于系统全局安装证书。

因此不要把 HarmonyOS Emulator 写成 iOS 模拟器式的一步流程。当前可验证的抓包链路是：

1. 让目标网络栈显式走 `10.0.2.2:<proxy-port>` 或 Emulator UI 已验证的系统代理。
2. 让同一网络栈信任抓包 CA，优先使用调试构建里的 `caPath` / `caData` 或对应框架的证书配置。
3. 若目标启用 certificate pinning，在调试构建关闭或替换 pin。

### 不能透明接管全部流量的方案

Mac 侧中转脚本可以把 `10.0.2.2:<local-port>` 转发到某个抓包工具的代理端口，但前提是调试目标应用主动连接这个端口。它不能透明接管全部流量，也不能让已经直连目标服务器的连接自动进入抓包工具。

直接把原始 TCP 流量转发到显式 HTTP 代理端口通常也不可行：HTTP 代理端口期望收到 HTTP 请求或 `CONNECT host:443`，而普通 HTTPS 直连发送的是 TLS 握手，协议不匹配。HTTP `:80` 的透明重定向也需要恢复原始目标地址和代理支持，不能作为通用能力写入自动化契约。

真正站到全部流量路径上的方案是设备侧 VPN/TUN。HarmonyOS 提供 `VpnExtension` 能力，可创建虚拟网卡、配置 routes、DNS 和 `trustedApplications` / `blockedApplications`。这需要实现一个调试 VPN Extension，在设备侧读取 TUN 包并转发，不是单独的 Mac 脚本可以完成的能力。

系统或全局代理属于受限能力：企业设备管理的全局代理需要设备管理员身份和 `ohos.permission.ENTERPRISE_MANAGE_NETWORK`；PAC 设置需要 `ohos.permission.SET_PAC_URL`。普通三方调试应用不应把这些能力当成默认可用路径。

## 参数白名单

默认健康检查只读取这些低风险参数：

```bash
param get bootevent.boot.completed
param get const.product.model
param get const.product.name
param get const.product.devicetype
param get const.product.os.dist.name
param get const.product.os.dist.version
param get const.product.os.dist.apiversion
param get const.ohos.fullname
param get const.ohos.apiversion
param get persist.sys.hilog.loggable.global
```

不默认读取或记录包含这些关键词的参数：`udid`、`uuid`、`serial`、`sn`、`account`、`user`、`token`、`auth`、`wifi`、`wlan`、`mac`、`ip`。

## 超时

| 场景 | 建议 timeout | 超时处理 |
| --- | ---: | --- |
| `hdc list targets -v` | 5s | 停止本轮自动化 |
| boot completed 轮询 | 单次 3s，总 60-120s | 超时不做 UI 输入 |
| `uitest dumpLayout` / `screenCap` | 10s | 降级到日志摘要 |
| `aa dump` / `bm dump` | 8s | 裁剪输出，失败则跳过 |
| `hidumper` | 8s | 跳过该指标 |
| `hilog -z 100` | 5s | 保留已返回内容 |

禁止无超时运行：不带 `-z` / `-x` 的 `hilog`、`track-jpid`、`hitrace --record`、`wukong exec`、`uitest uiRecord record`、`uitest start-daemon`。

## 执行记录模板

高风险或会写入产物的动作必须记录读取范围、写入位置、脱敏策略和停止条件：

```text
动作：<启动/停止/安装/采集/端口转发>。
范围：<HVD/target/bundle/path>。
读取：<target 状态/boot 参数/裁剪日志/截图/layout/设备文件>。
写入：<无/本地路径/设备路径>。
脱敏：<只保留摘要，不保存原文/保存附件前裁剪字段>。
停止条件：<无 Connected target/boot 超时/命令失败/脱敏失败>。
```

## 输出与脱敏

默认只向用户报告能力、状态、错误摘要、资源数值和可复现命令模板。不要保存或回显完整 layout、截图、日志、token、cookie、设备唯一标识、用户 ID、URL query、请求体、响应体、证书、fingerprint、真实沙箱路径、完整窗口树或完整业务 payload。

推荐摘要格式：

```text
target: 127.0.0.1:<port>
boot: true|false
foreground: <bundle>/<ability>, pid=<pid>
display: <w>x<h>, density=<n>, rotation=<n>
resources: cpu=<percent>, memPss=<kb>
logs: errors=<n>, warnings=<n>, topError=<summary>
ui: layoutProbe=true|false, screenshotProbe=true|false, rawContentStored=false
```

脱敏失败时，不归档原文。
