# ArkWeb WebView CDP 调试与字段到达证明

> 面向需要证明“H5 已在 HarmonyOS ArkWeb 运行时收到某个原生桥字段”的 agent。目标是保存最小、可复现、可脱敏的运行时结果，不把截图、完整 payload、完整 layout 或全量日志当作默认产物。

## 适用范围

- 页面运行在 HarmonyOS 应用内的 ArkWeb / WebView。
- 需要确认 JavaScript bridge 回调或页面运行时对象中出现了预期字段。
- 高层自动化工具没有可用的 HarmonyOS WebView 运行时，必须回退到 HDC、`fport` 和 Chrome DevTools Protocol (CDP)。

若当前任务已经提供可用的 TritonKit Harmony 运行时，优先使用 TritonKit。只有高层运行时不可用或无法连接目标页面时，才进入本页的 HDC/CDP 路径。

## 证据优先级

1. CDP `Runtime.evaluate` 返回的最小 JSON 摘要是字段到达的主要证据。
2. `/json` 或 `/json/version` 只证明 DevTools 发现端点可用。
3. `aa dump`、`dumpLayout` 和截图只用于确认前台页面，不能替代 bridge callback JSON。
4. `Page.captureScreenshot` 可能挂起；字段证明流程不得等待它完成。
5. 如果 layout 或截图来自锁屏、系统弹窗或其他前台页面，应标记为无效 UI 证据。

## 第一步：诊断 WebView DevTools 转发

```bash
python3 "$HARMONY_NEXT_SKILL_DIR/scripts/device_evidence_bundle.py" webview-devtools \
  --deveco-app /Applications/DevEco-Studio.app \
  --target <target> \
  --artifact-dir .hvigor/outputs/webview-devtools \
  --json
```

多个 WebView socket 时必须显式选择：

```bash
python3 "$HARMONY_NEXT_SKILL_DIR/scripts/device_evidence_bundle.py" webview-devtools \
  --deveco-app /Applications/DevEco-Studio.app \
  --target <target> \
  --remote-socket webview_devtools_remote_<pid> \
  --local-port <port> \
  --artifact-dir .hvigor/outputs/webview-devtools \
  --keep-forward \
  --json
```

默认情况下，wrapper 会删除它本轮创建的转发。只有后续立即连接 CDP 时才使用 `--keep-forward`，完成后按返回的 `localPort` 执行：

```bash
hdc -t <target> fport rm tcp:<localPort>
```

不要执行全局 `hdc kill`、清空所有转发或移除未知 target。`--replace-stale` 只处理占用所选本地端口、且远端 socket 已不再存在的转发。

## 第二步：选择 CDP 页面

从 `http://127.0.0.1:<localPort>/json` 返回值中选择目标页面的 `webSocketDebuggerUrl`。选择依据应是当前前台页面、URL 或已知页面标题；不要把完整 URL、标题或内部路由写入公开 issue。

先发送：

```json
{"id":1,"method":"Runtime.enable"}
```

再使用 `Runtime.evaluate`：

```json
{
  "id": 2,
  "method": "Runtime.evaluate",
  "params": {
    "expression": "<bounded async JavaScript>",
    "awaitPromise": true,
    "returnByValue": true
  }
}
```

`expression` 应在固定超时内等待目标 bridge，例如 `window.DXYJSBridge.invoke`，调用任务指定的方法，并只返回需要证明的字段：

```json
{
  "bridgeReady": true,
  "callbackReceived": true,
  "fields": {
    "requestIdPresent": true,
    "sourceType": "native"
  }
}
```

不要返回完整 bridge payload、用户内容、token、cookie、账号标识、内部 URL 或大对象。

## 第三步：保存最小证据

建议只保存 CDP 方法、`awaitPromise`、`returnByValue` 和脱敏后的 `result.value`。本地原始 `/json` 结果可能包含页面标题、URL 和 WebSocket 地址；公开分享前只保留页面数量、JSON key 集合、选中 PID 和失败码。

## 前台页面核验

```bash
hdc -t <target> shell aa dump -r
hdc -t <target> shell uitest dumpLayout -p /data/local/tmp/webview-layout.json -a
hdc -t <target> shell uitest screenCap -p /data/local/tmp/webview-screen.png
```

只有 bundle、页面和可见内容与预期目标一致时，才把这些产物作为支持证据。若捕获到锁屏、系统桌面、权限弹窗或其他应用，记录 `foregroundEvidenceValid=false` 并忽略这些产物。

## 失败分类

| `failureCode` | 含义 | 下一步 |
| --- | --- | --- |
| `webview_socket_not_found` | 没有运行中的 DevTools socket | 确认 ArkWeb 页面已打开，并启用 Web 调试 |
| `multiple_webview_sockets` | 存在多个候选 WebView | 结合 PID 与前台页面传 `--remote-socket` |
| `stale_fport` | 本地端口指向已消失的远端 socket | 换端口，或确认后使用 `--replace-stale` |
| `fport_create_failed` | HDC 无法创建所选转发 | 检查 target、端口占用和 HDC 版本 |
| `devtools_connection_refused` | 本地端口没有可连接服务 | 检查转发生命周期和 WebView PID |
| `devtools_http_reset` | DevTools HTTP 连接被重置 | 检查 socket 是否仍存活、协议端点是否匹配 |
| `devtools_http_timeout` | `/json` 探测超时 | 用短超时重试，不等待 `Page.captureScreenshot` |
| `devtools_invalid_json` | 端点返回非 JSON 内容 | 检查是否转发到了正确的 DevTools socket |

字段到达证明失败时，应返回 bridge/CDP 阶段的结构化错误；不要用截图成功覆盖 `Runtime.evaluate` 失败。
