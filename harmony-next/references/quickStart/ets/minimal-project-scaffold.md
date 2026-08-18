# 可复制 Empty Ability 最小工程

当 agent 需要在任意仓库内生成 HarmonyOS NEXT 测试工程，但不能打开 DevEco Studio 向导时，优先复制本仓库模板：

```bash
cp -R "$HARMONY_NEXT_SKILL_DIR/references/templates/empty-ability-app" <target-repo>/harmony-empty-ability
```

模板入口：

- [`references/templates/empty-ability-app/`](../../templates/empty-ability-app/)
- [`references/templates/empty-ability-app/README.md`](../../templates/empty-ability-app/README.md)

该模板来自本机 DevEco Studio `New Project` 与 `Empty Ability` 模板的最小化整理，保留 Stage 模型、`EntryAbility`、`pages/Index`、`main_pages.json` 和基本资源文件，删除本机签名材料、IDE 缓存与向导占位符。

## 包含文件

```text
empty-ability-app/
├── oh-package.json5
├── package.json
├── build-profile.json5
├── hvigorfile.ts
├── hvigor/hvigor-config.json5
├── AppScope/app.json5
├── AppScope/resources/base/element/string.json
├── AppScope/resources/base/media/app_icon.png
└── entry/
    ├── oh-package.json5
    ├── build-profile.json5
    ├── hvigorfile.ts
    └── src/main/
        ├── module.json5
        ├── ets/entryability/EntryAbility.ets
        ├── ets/components/SmokeCounter.ets
        ├── ets/pages/Index.ets
        └── resources/base/
            ├── element/color.json
            ├── element/float.json
            ├── element/string.json
            └── profile/main_pages.json
```

默认边界：

| 字段 | 值 |
| --- | --- |
| Compatible SDK | `5.0.0(12)` |
| targetSdkVersion | `5.0.0(12)` |
| modelVersion | `5.0.0` |
| bundleName | `com.example.emptyability` |
| module name | `entry` |
| ability name | `EntryAbility` |
| runtimeOS | `HarmonyOS` |

复制后按目标项目修改 `AppScope/app.json5` 中的 `bundleName`，并同步更新 smoke 脚本里的 `BUNDLE`。如果需要签名构建，由目标项目自行生成 `signingConfigs`；模板不携带任何个人证书、p12、profile 或本机绝对路径。应用图标来自 DevEco Studio 官方 `New Project` 模板的 `app_icon.png`，可在目标工程内替换。

页面入口与 smoke 组件解耦：`pages/Index.ets` 只作为 `main_pages.json` 指向的 `@Entry` 路由页，负责挂载 `SmokeCounter()`；`components/SmokeCounter.ets` 承载 smoke 文本、节点 ID、状态和点击逻辑。复制到业务仓库后，可以替换路由页、移动组件或接入自己的导航结构，而不需要改写 Ability 入口。

## 静态校验

```bash
cd <target-repo>/harmony-empty-ability
/Applications/DevEco-Studio.app/Contents/tools/ohpm/bin/ohpm install
/Applications/DevEco-Studio.app/Contents/tools/hvigor/bin/hvigorw --mode module -p module=entry@default assembleHap
```

若本机 DevEco 路径不同，先按 Emulator playbook 的规则探测工具路径。不同 hvigor 版本的 HAP 输出路径可能不同，可用：

```bash
find entry/build -name '*.hap' -print
```

### SDK 版本适配验证

模板默认面向 `5.0.0(12)`。当目标环境需要验证其他 SDK 版本时，在复制出的 fixture 中覆盖 `compatibleSdkVersion` 和 `targetSdkVersion` 即可；例如 HarmonyOS 6.0.2 / API 22 使用 `6.0.2(22)`：

1. 保持模板默认 SDK 不变，把目标版本覆盖放在复制出的 fixture 内。
2. 将根 `build-profile.json5` 内 `compatibleSdkVersion` 和 `targetSdkVersion` 设置为目标 SDK，例如 `6.0.2(22)`。
3. 构建时将 `DEVECO_SDK_HOME` 指向 SDK 根目录，而不是 `sdk/default`。

```bash
DEVECO_SDK_HOME=/Applications/DevEco-Studio.app/Contents/sdk \
  /Applications/DevEco-Studio.app/Contents/tools/hvigor/bin/hvigorw \
  --mode module -p module=entry@default assembleHap
```

API 22 schema 会校验图标字段。模板必须保留：

- `AppScope/resources/base/media/app_icon.png`
- `AppScope/app.json5` 中的 app `icon`
- `entry/src/main/module.json5` 中 Ability 的 `icon` 和 `startWindowIcon`

模板不携带签名材料，生成 unsigned HAP 时出现 `No signingConfig` 类警告属于预期边界；支持使用 unsigned HAP 在模拟器上做安装、启动和 UI smoke 验证。

## Emulator smoke

```bash
HDC="/Applications/DevEco-Studio.app/Contents/sdk/default/openharmony/toolchains/hdc"
TARGET="127.0.0.1:10100"
BUNDLE="com.example.emptyability"
ABILITY="EntryAbility"
HAP="$(find entry/build -name '*.hap' | head -1)"

"$HDC" -t "$TARGET" install "$HAP"
"$HDC" -t "$TARGET" shell aa start -b "$BUNDLE" -a "$ABILITY"
"$HDC" -t "$TARGET" shell uitest dumpLayout -p /dev/null -a
"$HDC" -t "$TARGET" shell uitest screenCap -p /dev/null
```

`SmokeCounter.ets` 暴露稳定文本和节点 ID：

- `Harmony Smoke Ready`
- `smoke-title`
- `smoke-counter`
- `smoke-increment`

这些信号可用于 HDC / `uitest dumpLayout` / screenshot / log 采集链路的自动化 smoke。

### 点击 smoke

如果要验证页面状态流转，先保存一份 layout，定位 `smoke-increment` 的 `bounds`，再用中心点点击并重新 dump：

```bash
"$HDC" -t "$TARGET" shell uitest dumpLayout -p /data/local/tmp/empty_ability_before.json -a
"$HDC" -t "$TARGET" file recv /data/local/tmp/empty_ability_before.json ./empty_ability_before.json

# 示例 bounds 为 [468,1526][841,1666] 时，中心点约为 654,1596。
"$HDC" -t "$TARGET" shell uitest uiInput click 654 1596

"$HDC" -t "$TARGET" shell uitest dumpLayout -p /data/local/tmp/empty_ability_after.json -a
"$HDC" -t "$TARGET" file recv /data/local/tmp/empty_ability_after.json ./empty_ability_after.json
```

点击后应从 `Harmony Smoke Ready` / `tapCount=0` 变为 `Harmony Smoke Tapped` / `tapCount=1`。
