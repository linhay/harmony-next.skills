# LauncherAbilityInfo

桌面应用的Ability信息，可以通过[getLauncherAbilityInfoSync](@ohos.bundle.launcherBundleManager (launcherBundleManager模块).md#ZH-CN_TOPIC_0000002529444579__launcherbundlemanagergetlauncherabilityinfosync)获取。

本模块首批接口从API version 18 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { launcherBundleManager } from '@kit.AbilityKit';
```

#### LauncherAbilityInfo

**系统能力：** SystemCapability.BundleManager.BundleFramework.Launcher

名称类型只读可选说明applicationInfo[ApplicationInfo](ApplicationInfo.md)是否launcher ability的应用程序配置信息。elementName[ElementName](ElementName.md)是否launcher ability的ElementName信息。labelIdnumber是否launcher ability的名称的资源ID值。iconIdnumber是否launcher ability的图标的资源ID值。userIdnumber是否launcher ability的用户ID。installTimenumber是否launcher ability的安装时间戳，单位毫秒。