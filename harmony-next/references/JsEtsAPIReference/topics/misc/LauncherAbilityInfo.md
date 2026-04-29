# LauncherAbilityInfo

桌面应用的Ability信息，可以通过[getLauncherAbilityInfoSync](@ohos.bundle.launcherBundleManager (launcherBundleManager模块).md#ZH-CN_TOPIC_0000002522240562__launcherbundlemanagergetlauncherabilityinfosync)获取。

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

本模块首批接口从API version 18 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

**导入模块**

```ets
import { launcherBundleManager } from '@kit.AbilityKit';
```

**LauncherAbilityInfo**

系统能力： SystemCapability.BundleManager.BundleFramework.Launcher

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| applicationInfo | ApplicationInfo | 是 | 否 | launcher ability的应用程序配置信息。 |
| elementName | ElementName | 是 | 否 | launcher ability的ElementName信息。 |
| labelId | number | 是 | 否 | launcher ability的名称的资源ID值。 |
| iconId | number | 是 | 否 | launcher ability的图标的资源ID值。 |
| userId | number | 是 | 否 | launcher ability的用户ID。 |
| installTime | number | 是 | 否 | launcher ability的安装时间戳，单位毫秒。 |