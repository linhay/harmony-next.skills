# @ohos.bundle.launcherBundleManager (launcherBundleManager模块)

本模块支持launcher应用（桌面有图标的应用）所需的查询能力，支持[LauncherAbilityInfo](LauncherAbilityInfo.md)信息的查询。


本模块首批接口从API version 18开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { launcherBundleManager } from '@kit.AbilityKit';
```

#### launcherBundleManager.get[LauncherAbilityInfo](../../topics/misc/LauncherAbilityInfo.md)Sync

getLauncherAbilityInfoSync(bundleName: string, userId: number) : Array<[LauncherAbilityInfo](LauncherAbilityInfo.md)>

查询指定bundleName及用户的[LauncherAbilityInfo](LauncherAbilityInfo.md)。

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**系统能力：** SystemCapability.BundleManager.BundleFramework.Launcher

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 是 | 应用Bundle名称。 |
| userId | number | 是 | 被查询的用户ID，可以通过getOsAccountLocalId接口获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[LauncherAbilityInfo](../../topics/misc/LauncherAbilityInfo.md)> | Array形式返回bundle包含的LauncherAbilityInfo信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码]([通用错误码](../../errors/通用错误码.md).md)和[ohos.bundle错误码](包管理子系统通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Verify permission denied. |
| 801 | Capability not support. |
| 17700001 | The specified bundle name is not found. |
| 17700004 | The specified user ID is not found. |

**示例：**

```ets
import { launcherBundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = launcherBundleManager.getLauncherAbilityInfoSync("com.example.demo", 100);
  console.info("data is " + JSON.stringify(data));
} catch (errData) {
  let code = (errData as BusinessError).code;
  let message = (errData as BusinessError).message;
  console.error(`errData is errCode:${code}  message:${message}`);
}
```

#### [LauncherAbilityInfo](../../topics/misc/LauncherAbilityInfo.md)

type [LauncherAbilityInfo](../../topics/misc/LauncherAbilityInfo.md) = [_LauncherAbilityInfo](../../topics/misc/LauncherAbilityInfo.md)

[LauncherAbilityInfo](../../topics/misc/LauncherAbilityInfo.md)信息。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Launcher

| 类型 | 说明 |
| --- | --- |
| _[LauncherAbilityInfo](../../topics/misc/LauncherAbilityInfo.md) | 桌面应用的Ability信息。 |

#### ShortcutInfo20+

type ShortcutInfo = [_ShortcutInfo](../../topics/misc/ShortcutInfo.md#ZH-CN_TOPIC_0000002529284629__shortcutinfo-1)

应用[module.json5配置文件](../../guides/module.json5配置文件.md#shortcuts标签)中定义的快捷方式信息。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Launcher

| 类型 | 说明 |
| --- | --- |
| [_ShortcutInfo](../../topics/misc/ShortcutInfo.md#ZH-CN_TOPIC_0000002529284629__shortcutinfo-1) | 应用module.json5配置文件中定义的快捷方式信息。 |

#### ShortcutWant20+

type ShortcutWant = [_ShortcutWant](../../topics/misc/ShortcutInfo.md#ZH-CN_TOPIC_0000002529284629__shortcutwant)

快捷方式内定义的目标[wants](../../guides/module.json5配置文件.md#wants标签)信息集合。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Launcher

| 类型 | 说明 |
| --- | --- |
| [_ShortcutWant](../../topics/misc/ShortcutInfo.md#ZH-CN_TOPIC_0000002529284629__shortcutwant) | 快捷方式内定义的目标wants信息集合。 |

#### ParameterItem20+

type ParameterItem = [_ParameterItem](../../topics/misc/ShortcutInfo.md#ZH-CN_TOPIC_0000002529284629__parameteritem)

快捷方式配置信息中的自定义数据。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Launcher

| 类型 | 说明 |
| --- | --- |
| [_ParameterItem](../../topics/misc/ShortcutInfo.md#ZH-CN_TOPIC_0000002529284629__parameteritem) | 快捷方式配置信息中的自定义数据。 |